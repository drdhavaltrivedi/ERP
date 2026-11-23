"""Writes one conversational call script per account (v2 format, approved on AMD-009 YCUBE).

Flow: receptionist -> permission opener -> who we are -> what I saw on your site -> five easy questions
-> reflect the pain -> one line of value -> visit ask with two day options -> pushback table -> close.
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

def write_scripts(ranked, rows, H, P, V2, FAQ, outdir, first_dm, slug):
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
        caution = f"\n**Caution:** {r['notes']}\n" if r.get("notes") else ""
        short = a["company"].split(" (")[0].split(" /")[0]
        topic = f.get("keyq_en", "").rstrip("?")

        md = f"""# {r['account_id']} · {a['company']}: call script

**Call:** {a['phone'] or 'not on site; find on Google Maps or IndiaMART'}
**Ask for:** {a['dm'] if not a['dm'].lower().startswith('not ') else 'owner or MD (name not on the site; ask the receptionist)'}
**Language:** {lang_line(r)}
**What we know (from their website):** {a['sub']}. {a['address']}. {a['signal']}
**Fit:** score {r['fit_score']}, tier {r['tier']}. {r['odoo_vs_erpnext']}
**Goal of the call:** learn two or three facts and book a 30-minute visit at the {f['visit']}. Do not sell on the phone.
{caution}
Source: {a['src']}. Check the person's current role on LinkedIn or the site before calling.

---

## 1. Receptionist (20 seconds)

> **Dhaval:** Namaste, main Dhaval bol raha hoon, Brilworks se, Ahmedabad. Ek chhoti si help chahiye thi.
>
> {ask_line}

*Receptionists answer "who handles X" easily. Write the name down.*

> **If they ask "kis baare mein?":** Business software ke baare mein, stock aur accounts ka. Do minute ki baat hai.
>
> **If they say "mail kar dijiye":** Zaroor. Kis naam se bhejun, aur kya aap unka email bata sakte hain?

## 2. Opening with the decision maker (20 seconds)

> **Dhaval:** Namaste {nm}, main Dhaval, Brilworks se, Ahmedabad. Kya abhi do minute baat kar sakte hain, ya baad mein call karun?

*If they say later: "Kal subah 11 baje theek rahega?" and log it.*

## 3. Who we are (15 seconds, then stop talking)

> **Dhaval:** Hum Brilworks hain, Ahmedabad ki software company. Hum Odoo aur ERPNext ke partner hain, aur manufacturers ke liye stock, production, sales aur accounts ek system mein laate hain. {PROOF}
>
> Main aapki website dekh raha tha. {f['seen_hi']} Isliye socha seedha aapse baat karun.

## 4. Easy questions first (two-way, 1 to 2 minutes)

Ask one at a time. Wait for the answer. Repeat back one detail before the next question.

1. **Their role (easy):** "Aap khud operations side dekhte hain ya finance side?"
2. **Their setup (easy, flattering):** "{f.get('q1_hi','')}"
3. **Current system (easy):** "Abhi billing aur stock ke liye Tally use hota hai ya koi aur software?"
4. **Opens the pain:** "{f.get('q2_hi','')}"
5. **Opens the pain, another angle:** "{f.get('q3_hi','')}"

*Don't ask about revenue or margins on the first call.*

## 5. Listen for the pain, then reflect it back

If they mention Excel, WhatsApp, registers, phoning the plant or month-end delays:

> **Dhaval:** {f.get('reflect_hi','')}

## 6. One line of value, specific to them (15 seconds)

> **Dhaval:** Hum yahi karte hain. {_strip(f.get('value_hi',''), [])}

## 7. Ask for the visit (not a demo)

> **Dhaval:** Kya main next week {f['visit']} aa ke 30 minute mil sakta hoon? Main dikhaunga ki aapke jaisa setup ek system mein kaisa dikhta hai. Tuesday ya Thursday, kaunsa theek rahega?

*Always offer two options. When they agree:* "Main aapko WhatsApp pe confirm bhej deta hoon. Yeh number sahi hai?"

## 8. If they push back

| They say | Dhaval says |
|---|---|
| "Humare paas Tally hai, sab chal raha hai." | "Tally accounts aur GST ke liye bahut achha hai, woh chalu rahega. Main sirf yeh samajhna chahta tha: {f.get('q2_hi','')}" |
| "Abhi zaroorat nahi." | "Theek hai. Ek sawaal: agle saal production ya branches badhe, toh kya yahi system chalega?" Then: "Main 3 mahine baad call karun?" |
| "Details bhej do." | "Zaroor. Kis cheez pe focus karun, stock aur batch, production costing, ya accounts? Taaki aapke kaam ka ho." Get the email, send within an hour. |
| "Kitna kharcha hoga?" | "Phase 1 (stock, purchase, sales, accounts) ₹2 lakh se shuru hota hai. Exact quote aapka setup dekh ke dunga. Isliye milna zaroori hai." |
| "Pehle bhi ERP try kiya, kaam nahi kiya." | "Kya problem hua tha? Hum phase mein go-live karte hain, ek saath sab nahi badalte." |
| "Aapke clients kaun hain Ahmedabad mein?" | "Ahmedabad mein hum abhi pehle 2-3 manufacturers ke saath reference terms pe kaam shuru kar rahe hain. MP mein humne ek building-materials manufacturer ka ERP banaya hai." (Never name the client. Don't claim local clients.) |

## 9. Close every call the same way

> **Dhaval:** Bahut shukriya {nm}, aapka time dene ke liye. Main abhi WhatsApp pe meeting confirm karta hoon.

## Gujarati lines

> નમસ્તે, હું ધવલ બોલું છું, Brilworks માંથી, Ahmedabad. તમારે ત્યાં operations અને accounts નું software કોણ જુએ છે?{(' ' + ', '.join(p.split()[0] + 'જી' for p in ppl) + '?') if ppl else ''}
>
> નમસ્તે {nm_gu}, હું ધવલ, Brilworks માંથી, Ahmedabad. બે મિનિટ વાત થઈ શકે?
>
> અમે Odoo અને ERPNext ના partner છીએ. Manufacturers માટે stock, production, sales અને accounts એક system માં લાવીએ છીએ. હું તમારી website જોઈ રહ્યો હતો. {f['seen_gu']}
>
> {f.get('keyq_gu','')}
>
> આવતા અઠવાડિયે {f['visit']} પર 30 મિનિટ મળવા આવી શકું? મંગળવાર કે ગુરુવાર, શું ફાવશે?

## English lines

> Hi {nm_en}, this is Dhaval from Brilworks in Ahmedabad. Is now a bad time for two minutes?
>
> We're Odoo and ERPNext partners. We help manufacturers run stock, production, sales and accounts in one system. I was looking at your website. {f['seen_en']}
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

Log in `gtm/logs/calls.csv`: who you spoke to, their role, language used, the answers to questions 3 to 5, the objection, and the next step and date.
"""
        md = md.replace("\n\n\n", "\n\n")
        with open(os.path.join(outdir, f"{r['account_id']}-{slug(a['company'])}.md"), "w", encoding="utf-8") as fh:
            fh.write(md)
