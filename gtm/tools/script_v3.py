"""Writes one conversational call script per account (v3 format, follows scripts/00-call-playbook.md).

v3 replaces the straight-line v2 flow with branches: where we stand (from logs/calls.csv and the round-1 plan),
open the call (reception or decision maker, honest cold-call opener, one easy question about their current system),
a bank of questions to pick from based on their answer, a "they say / you say" table for the common branches
(busy, send an email, Tally and Excel, already on an ERP, just bought an ERP, not required, wrong person, clear no),
reflect the pain, value and visit ask, and an exit with a next step.
Main lines are Hinglish (Hindi in Roman script); Gujarati and English versions follow for switching.
"""
import os, re

PROOF = '[fill: one line of proof, e.g. "Humne MP mein ek building-materials manufacturer ke liye poora ERP banaya hai."]'
TITLES = ("Dr", "Mr", "Mrs", "Ms", "Miss", "Shri", "Smt", "Prof")
DEFAULT_ASKS = {"Pharma": [24, 23, 16, 5, 11], "Chemicals": [25, 27, 16, 5, 21], "Engineering": [26, 29, 16, 5, 11],
                "Electrical": [26, 29, 16, 5, 11], "Medical devices": [24, 23, 16, 5, 11]}
OTHER_ASKS = [16, 17, 5, 21, 28]

def _strip(s, prefixes):
    s = (s or "").strip()
    for p in prefixes:
        s = re.sub(r"^\s*" + p + r"[\s.:,]*", "", s, flags=re.I)
    return s.strip()

def people(dm):
    """First two named people from 'Name (Role); Name (Role)'."""
    if not dm or dm.lower().startswith("not "): return []
    out = []
    for part in re.split(r";|\|", dm):
        n = part.split(" (")[0].replace("[LinkedIn]", "").strip()
        n = re.sub(r"^LinkedIn:\s*", "", n)
        if " and " in n: n = n.split(" and ")[0].strip()
        words = [w for w in n.split() if w.rstrip(".") not in TITLES]
        if len(words) >= 2 and not any(ch.isdigit() for ch in n) and n.lower() != "manish patel":
            out.append(" ".join(words))
        if len(out) == 2: break
    return out

def ji(name): return name.split()[0] + " ji"

def fields(a, h, v):
    """Merge per-account v2 fields with fallbacks from the original hooks."""
    f = dict(v or {})
    f["seen_hi"] = _strip(f.get("seen_hi"), ["Main aapki website dekh raha tha"])
    f["seen_gu"] = _strip(f.get("seen_gu"), ["મેં તમારી વેબસાઇટ જોઈ રહ્યો હતો", "હું તમારી વેબસાઇટ જોઈ રહ્યો હતો", "મેં તમારી વેબસાઇટ જોઈ"])
    f["seen_en"] = _strip(f.get("seen_en"), ["I was looking at your website"])
    if not f["seen_gu"] and h.get("gu"): f["seen_gu"] = "મેં જોયું કે " + h["gu"] + "."
    if not f["seen_en"] and h.get("en"): f["seen_en"] = "I saw that " + h["en"] + "."
    if not f.get("visit"): f["visit"] = (a["cluster"] or "your office").split("/")[0].strip() + " office"
    return f

def lang_line(r):
    l = r["call_language"]
    if l.startswith("Hindi"): return "Hindi first (Hinglish lines below). Switch to Gujarati or English the moment they do."
    if l.startswith("English"): return "English first (English section below). Switch to Hindi or Gujarati as they reply."
    return "Gujarati first (Gujarati section below), then mirror them. If they answer in Hindi, use the Hinglish lines."

GENERIC_EMAIL_AB = ("stock aur batch tracking", "production costing")
GENERIC_DIG = ["Yeh kaam abhi kaun sambhalta hai, aur kitni baar?",
               "Yeh hamesha se aisa hai, ya naya plant ya naya product aane ke baad shuru hua?"]
GENERIC_ERP_Q = "Ab bhi koi report hai jo har mahine Excel mein bahar nikaal ke banani padti hai?"

def history(r, calls, plan):
    """'Where we stand' section from logged calls and the next-touch plan."""
    mine = sorted((c for c in calls if c.get("account_id") == r["account_id"]), key=lambda c: c.get("date_ist", ""))
    if not mine and not plan: return ""
    out = ["\n## Where we stand\n"]
    if mine:
        out.append("| Date | Outcome | Spoke to | Notes |\n|---|---|---|---|")
        for c in mine:
            who = " ".join(x for x in (c.get("person_spoken_to", ""), f"({c['role']})" if c.get("role") else "") if x) or "not recorded"
            out.append(f"| {c.get('date_ist','')} | {c.get('outcome','')} | {who} | {c.get('notes','').replace('|','/')} |")
        out.append("")
    if plan:
        if plan.get("learned"): out.append(f"**What we learned:** {plan['learned']}\n")
        if plan.get("next"): out.append(f"**Next touch:** {plan['next']}\n")
        if plan.get("angle"): out.append(f"**Angle:** {plan['angle']}\n")
        if plan.get("opener_hi") or plan.get("opener_en"):
            out.append("**Open the next call with this** (it shows you remember them):\n")
            if plan.get("opener_hi"): out.append(f"> **Dhaval:** {plan['opener_hi']}\n>")
            if plan.get("opener_en"): out.append(f"> **English:** {plan['opener_en']}\n")
        if plan.get("ask"):
            out.append("**Ask or do next:**\n")
            out += [f"- {q}" for q in plan["ask"]]
            out.append("")
        if plan.get("assumed"):
            out.append("**Not confirmed yet (check on the next touch):**\n")
            out += [f"- {q}" for q in plan["assumed"]]
            out.append("")
    out.append("\n---\n")
    return "\n".join(out)

def write_scripts(ranked, rows, H, P, V2, FAQ, outdir, first_dm, slug, V3=None, calls=None):
    V3, calls = V3 or {}, calls or []
    for old in os.listdir(outdir):
        if old.endswith(".md"): os.remove(os.path.join(outdir, old))
    byco = {r["company"]: r for r in rows}
    for a in ranked:
        r = byco[a["company"]]
        h = H.get(a["company"], {})
        f = fields(a, h, V2.get(a["company"]))
        ppl = people(a["dm"])
        names_hi = ", ".join(ji(p) for p in ppl) + (", ya koi aur?" if ppl else "")
        ask_line = (f"Aapke yahan operations aur accounts ka software ya system kaun dekhta hai? {names_hi}" if ppl
                    else "Aapke yahan operations aur accounts ka software ya system kaun dekhta hai? Owner ya MD sahab?")
        nm = ji(ppl[0]) if ppl else "{name} ji"
        nm_gu = (ppl[0].split()[0] + "જી") if ppl else "{name}જી"
        nm_en = ppl[0].split()[0] if ppl else "{name}"
        ind = a["industry"]
        pp = P.get(a["company"])
        asks = (pp["asks"] if pp else None) or next((v for k, v in DEFAULT_ASKS.items() if ind.startswith(k)), OTHER_ASKS)
        asks_md = "\n".join(f"- **{FAQ[n][0]}** {FAQ[n][1]}" for n in asks if n in FAQ) or "- See `scripts/01-buyer-faq.md`."
        talk_md = ("\n".join(f"{i}. {t}" for i, t in enumerate(pp["talk"], 1)) if pp and pp.get("talk") else "")
        note = " | ".join(x for x in (r.get("notes") or "").split(" | ") if not x.startswith("Round 1")).strip()
        caution = f"\n**Caution:** {note}\n" if note else ""
        short = a["company"].split(" (")[0].split(" /")[0]
        topic = f.get("keyq_en", "").rstrip("?")
        v3 = V3.get(a["company"], {})
        email_a, email_b = v3.get("email_ab") or GENERIC_EMAIL_AB
        dig_md = "\n".join(f'- **Dig deeper:** "{q}"' for q in (v3.get("dig") or GENERIC_DIG))
        erp_q = v3.get("erp_q") or GENERIC_ERP_Q
        seen_short = f["seen_hi"] or "aapke jaise manufacturers ke saath stock aur accounts ka kaam karte hain."
        history_md = history(r, calls, v3.get("plan"))

        md = f"""# {r['account_id']} · {a['company']}: call script

**Call:** {a['phone'] or 'not on site; find on Google Maps or IndiaMART'}
**Ask for:** {a['dm'] if not a['dm'].lower().startswith('not ') else 'owner or MD (name not on the site; ask the receptionist)'}
**Language:** {lang_line(r)}
**Status:** {r.get('status') or 'Researched'}{(' · next: ' + r['next_step'] + (' (' + r['next_step_date'] + ')' if r.get('next_step_date') else '')) if r.get('next_step') else ''}
**What we know (from their website):** {a['sub']}. {a['address']}. {a['signal']}
**Fit:** score {r['fit_score']}, tier {r['tier']}. {r['odoo_vs_erpnext']}
**Goal of the call:** leave with one of: a visit date at the {f['visit']}, the right person's name and a good time, one real fact about how they run today, or a callback date. Do not sell on the phone.
{caution}
Source: {a['src']}. Check the person's current role on LinkedIn or the site before calling. How to run the conversation: `scripts/00-call-playbook.md`.

---
{history_md}
## 1. Open the call (15 seconds)

**If reception answers** (playbook branch A): get the name, the best time and a direct number.

> **Dhaval:** Namaste, main Dhaval, Brilworks se, Ahmedabad. Ek chhoti si help chahiye thi. {ask_line}
>
> **If "sir abhi nahi hain":** Koi baat nahi. Woh usually kab milte hain, subah ya shaam? Aur unka extension ya direct number mil sakta hai?
>
> **If "mail kar dijiye":** Zaroor. Kis naam se bhejun, aur unka email kya hai? Mail ke baad Thursday ko call karun toh baat ho jayegi?

*Ask the receptionist's name and use it next time.*

**When you reach {nm}:**

> **Dhaval:** Namaste {nm}, main Dhaval, Brilworks se, Ahmedabad. Seedha bolun toh yeh ek cold call hai. 30 second de sakte hain? Phir aap batana baat karni hai ya nahi.
>
> **If yes:** Main aapki website dekh raha tha. {f['seen_hi']} Hum manufacturers ke saath ERP ka kaam karte hain, Odoo aur ERPNext. Toh ek cheez samajhni thi: abhi stock aur accounts ke liye kya use karte hain, Tally ya koi ERP?

*Their answer picks the branch in section 3. Stop talking and listen.*

## 2. Questions to have ready (ask one, then follow their answer)

Pick the next question from what they just said, not from the list order.

- **Easy, about their setup:** "{f.get('q1_hi','')}"
- **The pain question:** "{f.get('q2_hi','')}"
- **Another angle:** "{f.get('q3_hi','')}"
{dig_md}
- **Who feels it:** "Yeh sabse zyada kisko pareshan karta hai, accounts ko, plant ko, ya aapko?"
- **The last time:** "Last time yeh hua tha, toh kya hua? Kitna time laga?"

*Echo their last few words when they go vague ("Thoda manual?"). Don't ask about revenue or margins on the first call.*

## 3. What they say, what you say

| They say | Dhaval says |
|---|---|
| "Busy hoon." | "Bilkul. Ek line mein bataun kyon call kiya: {seen_short} Isliye ek sawaal tha. Kal 11 baje ya shaam 5 ke baad, kya theek rahega?" |
| "Email bhej do." | "Zaroor. Taaki generic mail na ho: aapke liye zyada important kya hai, {email_a} ya {email_b}? ... Aur mail ke baad Friday ko 2 minute call kar lun?" Confirm the address letter by letter. |
| "Tally aur Excel pe chal raha hai." | "Tally accounts ke liye best hai, woh chalu rahega. Excel mein sabse badi sheet kaunsi hai? ... {f.get('q2_hi','')}" |
| "Humare paas ERP hai." | "Achha, kaunsa? Kab se chal raha hai? Ise kaun own karta hai?" Then: "{erp_q}" Get a follow-up date (playbook branch E). |
| "Abhi naya ERP liya hai." | "Congratulations. Kaunsa, aur partner kaun hai? Go-live kab ka target hai? Pehle phase mein kya aa raha hai?" Exit: "Go-live ke 2-3 mahine baad ek baar call karun?" |
| "ERP achha chal raha hai, koi problem nahi." | Don't hunt for pain. "Bahut badhiya. Kya cheez sabse achhi lagti hai usmein? ... Agar ek cheez add kar sakte toh kya hoti? ... AMC ya renewal kab hota hai?" Exit: "Main aapka time aur nahi leta. 6 mahine baad ek baar check karun?" (playbook branch E5) |
| "Zaroorat nahi hai." | "Fair hai. Ek cheez pooch sakta hoon: kya isliye ki sab already system mein hai, ya abhi priority kuch aur hai?" (playbook branch F) |
| Wrong person (IT, accounts staff) | "Aap hi sahi insaan ho yeh samajhne ke liye. Abhi kya system hai? ... Iska decision usually kaun leta hai?" Ask for an introduction. |
| "Kitna kharcha hoga?" | "Phase 1 (stock, purchase, sales, accounts) ₹2 lakh se shuru hota hai. Exact quote aapka setup dekh ke dunga. Isliye milna zaroori hai." |
| "Pehle bhi ERP try kiya, kaam nahi kiya." | "Kya hua tha? ... Hum phase mein go-live karte hain, ek saath sab nahi badalte." |
| "Aapke clients kaun hain Ahmedabad mein?" | "MP mein humne ek building-materials manufacturer ka ERP banaya hai. Ahmedabad mein is saal pehle 2-3 manufacturers ke saath reference terms pe shuru kar rahe hain." (Never name the client. Don't claim local clients.) |
| Clear no, "dobara call mat karna" | "Bilkul, sorry for disturbing. Thank you." Set status to `Do not contact`. |

## 4. When you hear the pain

Ask one more question about it first. Then reflect it back:

> **Dhaval:** {f.get('reflect_hi','')} Sahi samjha?

One line of value, then the visit ask:

> **Dhaval:** Hum yahi karte hain. {_strip(f.get('value_hi',''), [])} Kya main next week {f['visit']} aa ke 30 minute dikha sakta hoon ki aapke setup mein yeh kaisa dikhega? Tuesday ya Thursday?

*When they agree:* "Main WhatsApp pe confirm bhejta hoon. Yeh number sahi hai?"

## 5. Leave with a next step

Never end with "main contact karta hoon". End with a date, a name or a number, and thank them by name:

> **Dhaval:** Bahut shukriya {nm}, aapka time dene ke liye. Toh main [day] ko [time] call karta hoon.

## Gujarati lines

> નમસ્તે, હું ધવલ બોલું છું, Brilworks માંથી, Ahmedabad. તમારે ત્યાં operations અને accounts નું software કોણ જુએ છે?{(' ' + ', '.join(p.split()[0] + 'જી' for p in ppl) + '?') if ppl else ''}
>
> નમસ્તે {nm_gu}, હું ધવલ, Brilworks માંથી, Ahmedabad. બે મિનિટ વાત થઈ શકે?
>
> અમે Odoo અને ERPNext ના partner છીએ. Manufacturers માટે stock, production, sales અને accounts એક system માં લાવીએ છીએ. હું તમારી website જોઈ રહ્યો હતો. {f['seen_gu']}
>
> અત્યારે stock અને accounts માટે શું વાપરો છો, Tally કે કોઈ ERP?
>
> {f.get('keyq_gu','')}
>
> આવતા અઠવાડિયે {f['visit']} પર 30 મિનિટ મળવા આવી શકું? મંગળવાર કે ગુરુવાર, શું ફાવશે?

## English lines

> Hi {nm_en}, this is Dhaval from Brilworks in Ahmedabad. To be upfront, this is a cold call. Can I take 30 seconds, and then you tell me if it's worth continuing?
>
> I was looking at your website. {f['seen_en']} We're Odoo and ERPNext partners, so I wanted to ask: what do you use for stock and accounts today, Tally or an ERP?
>
> {f.get('keyq_en','')}
>
> Could I come by the {f['visit']} for 30 minutes next week? Would Tuesday or Thursday suit you better?

## Questions they will probably ask

{asks_md}

Full answers are in `scripts/01-buyer-faq.md`. Fill the [fill] items there before calling.
"""
        if talk_md:
            md += f"\n## What to show them on the visit\n\n{talk_md}\n"
        md += f"""
## Email draft (not sent; send only after approval)

**Subject:** {short}: {topic[:60].lower() if topic else 'stock and accounts in one system'}

{('Hi ' + nm_en + ',') if ppl else 'Hello,'}

I was looking at your website. {f['seen_en']}

{f.get('keyq_en','')} In plants like yours this often ends up split across Tally, Excel and WhatsApp, and the owner sees the real numbers late.

I'm Dhaval from Brilworks, an Odoo and ERPNext partner in Ahmedabad. We put stock, production, sales and accounts in one system, starting with a fixed-scope first phase. Tally can stay for accounts and GST while you move.

Could I come by the {f['visit']} for 30 minutes next week?

Dhaval
Brilworks | Odoo and ERPNext partner
[Phone]

If this isn't relevant, just reply "no thanks" and I won't follow up.

**Follow-up, day 4 (same thread):** One quick win we usually start with: getting stock and batch movements into one place before touching production planning. Happy to show what that would look like for {short}.

**Follow-up, day 10 (same thread):** I'll leave this here. If useful, I can send a one-page sketch of how your stock, production and accounts would sit in one system. Just reply "send it".

## WhatsApp after the call (send only after approval)

> {nm_gu if ppl else 'નમસ્તે'}, આજે વાત કરવા બદલ આભાર. ધવલ, Brilworks. આપણે વાત કરી તેમ [visit date] એ {f['visit']} પર 30 મિનિટ મળીએ. Confirm કરશો?

## Visit checklist

- Bring: one-page Odoo/ERPNext overview, the MP building-materials case (anonymised), a phase 1 price range.
- Ask to see: the stock register, a costing sheet, and how a purchase order is approved.
- Leave with: the main pain in their words, who else decides, and a date for a demo or a proposal.

## After the call (2 minutes)

Log in `gtm/logs/calls.csv` with an `outcome` code from the playbook: who you spoke to, their role, language used, what system they use, the pain in their words, the objection, and the next step and date. Then update the account row in `leads/accounts.csv` and run `python3 gtm/tools/build.py`.
"""
        md = md.replace("\n\n\n", "\n\n")
        with open(os.path.join(outdir, f"{r['account_id']}-{slug(a['company'])}.md"), "w", encoding="utf-8") as fh:
            fh.write(md)
