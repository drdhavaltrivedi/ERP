"""Builds the lead tracker, activity logs, per-account scripts and the Excel view.

Source of truth after the first run: gtm/leads/accounts.csv (edit status columns there) and gtm/logs/*.csv.
research_seed.py is only used to seed accounts.csv when it does not exist yet, or to add new accounts.

Run from the repo root:  python3 gtm/tools/build.py
"""
import csv, os, re, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
GTM = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from hooks import H, P
FAQ = {}
_faq = os.path.join(GTM, "scripts", "01-buyer-faq.md")
if os.path.exists(_faq):
    for m in re.finditer(r"^\*\*(\d+)\. (.+?)\*\*\s*\n(.+?)$", open(_faq, encoding="utf-8").read(), re.M):
        FAQ[int(m.group(1))] = (m.group(2), m.group(3).strip())

seed = {}
exec(open(os.path.join(HERE, "research_seed.py")).read(), seed)
A, HOLD = seed["A"], seed["HOLD"]

COLS = ["account_id","company","industry","sub_segment","headcount","address","cluster","website","phone_board","email_generic",
        "decision_makers","linkedin_main","work_email","email_verification","pain_signal","signal_source","fit_score","tier",
        "odoo_vs_erpnext","call_language","owner","status","last_activity","next_step","next_step_date","notes"]
STATUSES = ["Researched","Called - no answer","Called - gatekeeper","Called - spoke to DM","Meeting booked","Visited",
            "Discovery done","Proposal sent","Won","Lost","Not a fit","Do not contact"]

def score(a):
    s = 20 if a["rank"] <= 3 else 10
    s += 10
    s += 15 if a["multi_loc"] else 0
    t = a["signal"].lower()
    kinds = [("hiring",), ("new plant","commissioned","planned","launched","acquired","acquisition"),
             ("subsidiar","sister company","group","offices"), ("listed",), ("export",)]
    s += min(30, 10 * sum(1 for ks in kinds if any(k in t for k in ks)))
    s += 0 if a["dm"].lower().startswith("not ") else 10
    s += 10 if a["phone"] and not a["phone"].startswith("(") else 0
    return min(s, 100)

def tier(s): return "A" if s >= 70 else ("B" if s >= 50 else "C")

def fit(a):
    t = (a["signal"] + a["sub"] + a["address"]).lower()
    if any(k in t for k in ["subsidiar","brazil","vietnam","uae","dubai","thailand","shanghai","us procurement","us outsourcing","acquired"]) or a["industry"].startswith("Pharma"):
        return "Odoo (multi-company/multi-currency or pharma QC + lots)"
    if not a["multi_loc"]:
        return "ERPNext first (single site, price-sensitive); Odoo if they want CRM/website"
    return "Either: decide on budget at discovery"

def first_dm(a):
    d = a["dm"]
    if d.lower().startswith("not "): return ""
    return d.split(" (")[0].split("|")[0].split(";")[0].replace("[LinkedIn]","").strip()

def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:40]

# ---------- 1. tracker CSV (seed once, then preserve human edits) ----------
path = os.path.join(GTM, "leads", "accounts.csv")
existing = {}
if os.path.exists(path):
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f): existing[r["company"]] = r
ranked = sorted(A, key=lambda a: (-score(a), a["cluster"]))
rows, used_ids = [], {r["account_id"] for r in existing.values()}
n = len(used_ids)
for a in ranked:
    if a["company"] in existing:
        rows.append(existing[a["company"]]); continue
    n += 1
    aid = f"AMD-{n:03d}"
    while aid in used_ids: n += 1; aid = f"AMD-{n:03d}"
    used_ids.add(aid)
    s = score(a); h = H.get(a["company"], {})
    dm = first_dm(a)
    rows.append(dict(account_id=aid, company=a["company"], industry=a["industry"], sub_segment=a["sub"], headcount=a["hc"],
        address=a["address"], cluster=a["cluster"], website=a["website"], phone_board=a["phone"], email_generic=a["email_generic"],
        decision_makers=a["dm"], linkedin_main=a.get("li",""), work_email="", email_verification="", pain_signal=a["signal"],
        signal_source=a["src"], fit_score=s, tier=tier(s), odoo_vs_erpnext=fit(a), call_language=h.get("lang","Gujarati"),
        owner="", status="Researched", last_activity="", next_step=(f"Call board line, ask for {dm}" if dm else "Find owner name (MCA / Google Maps), then call"),
        next_step_date="", notes=("Do not contact Manish Patel: company site lists him as late." if "Mediwin" in a["company"] else "")))
for c, r in existing.items():
    if c not in {a["company"] for a in A}: rows.append(r)
rows.sort(key=lambda r: r["account_id"])

# ---------- 2. activity logs (create headers once; never overwrite) ----------
LOGS = {
 "calls.csv": ["date_ist","account_id","company","caller","person_spoken_to","role","language_used","outcome","pain_heard","objection","next_step","next_step_date","notes"],
 "emails.csv": ["date_ist","account_id","company","from","to","subject","step","status","reply_summary","notes"],
 "visits.csv": ["date_ist","account_id","company","visited_by","met_with","role","outcome","pain_heard","objection","next_step","next_step_date","notes"],
 "linkedin_whatsapp.csv": ["date_ist","account_id","company","channel","by","to","message_summary","status","notes"],
}
logs = {}
for fn, hdr in LOGS.items():
    p = os.path.join(GTM, "logs", fn)
    if not os.path.exists(p):
        with open(p, "w", newline="", encoding="utf-8") as f: csv.writer(f).writerow(hdr)
    with open(p, newline="", encoding="utf-8") as f: logs[fn] = list(csv.DictReader(f))

# latest activity per account from logs
last = {}
for fn, lst in logs.items():
    for r in lst:
        k = r.get("account_id")
        if k and r.get("date_ist","") >= last.get(k, ("",""))[0]:
            last[k] = (r["date_ist"], f'{fn.split(".")[0]}: {r.get("outcome") or r.get("status","")}')
for r in rows:
    if r["account_id"] in last: r["last_activity"] = f"{last[r['account_id']][0]} {last[r['account_id']][1]}"

with open(path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLS); w.writeheader()
    for r in rows: w.writerow({k: r.get(k, "") for k in COLS})
with open(os.path.join(GTM, "leads", "held.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["company","reason"]); w.writerows(HOLD)

# ---------- 3. per-account personalised scripts ----------
Q = {
 "Pharma": ["How do you track batch and expiry across plants today: Tally, Excel or a separate tool?",
            "When an auditor or a foreign regulator asks for a batch's full history, how long does it take to pull?",
            "How do you handle near-expiry stock and returns from export markets?"],
 "Chemicals": ["How do you cost a batch today, including yield loss and by-products?",
               "How do you move stock between plants or to job workers, and how often do the numbers not match?",
               "How much of your export paperwork (invoices, packing lists, COAs) is made by hand?"],
 "Engineering": ["How does an enquiry become a quote, a BOM and a work order today?",
                 "Do you know the actual cost of each job after it ships, or only the estimate?",
                 "How do you track spares, service visits and installed units at customer sites?"],
}
def qs(ind):
    for k in Q:
        if ind.startswith(k) or k in ind: return Q[k]
    return Q["Engineering"]

used_subjects = set()
def subject(a, h):
    base = {"Pharma":"batch records","Chemicals":"plant-wise costing","Engineering":"job costing"}
    key = next((k for k in base if k in a["industry"]), "Engineering")
    s = f"{a['company'].split()[0].lower()} {base[key]}"
    i = 2
    while s in used_subjects: s = f"{s} {i}"; i += 1
    used_subjects.add(s); return s

for a in ranked:
    r = next(x for x in rows if x["company"] == a["company"])
    h = H.get(a["company"], dict(lang="Gujarati", en="", gu="", pain=""))
    dm = first_dm(a) or "the owner or managing director"
    _n = [w for w in dm.split() if w.rstrip('.') not in ("Dr","Mr","Mrs","Ms","Miss")]
    dm_first = _n[0] if dm != "the owner or managing director" and _n else ""
    q = qs(a["industry"])
    hi_line = h.get("hi")
    md = f"""# {r['account_id']} · {a['company']}

| | |
|---|---|
| Industry | {a['industry']}: {a['sub']} |
| Ask for | {dm} |
| Other contacts | {a['dm']} |
| Board phone | {a['phone']} |
| Address / cluster | {a['address']} ({a['cluster']}) |
| Website | {a['website']} |
| LinkedIn | {a.get('li') or 'not found yet'} |
| Fit | Score {r['fit_score']}, Tier {r['tier']}. {r['odoo_vs_erpnext']} |
| Call language | {h['lang']} |
| Hook (verified) | {h['en']}. Source: {a['src']} |
| Pain to probe | {h['pain']} |
{"| Caution | " + r['notes'] + " |" if r['notes'] else ""}

Before calling: check the person's current role on LinkedIn or the company site. Log every attempt in `gtm/logs/calls.csv`.

## 1. Call opener (30 seconds)

**Gujarati**

> નમસ્તે, હું [તમારું નામ] બોલું છું, [કંપનીનું નામ] માંથી. શું હું {(dm_first + 'જી') if dm_first else 'MD'} સાથે વાત કરી શકું?
>
> (DM મળે ત્યારે) {dm_first + 'જી' if dm_first else 'નમસ્તે'}, બે મિનિટ લઈશ. અમે Ahmedabad ની manufacturing કંપનીઓ માટે Odoo અને ERPNext implement કરીએ છીએ. મેં જોયું કે {h['gu']}. આવા setup માં stock, costing અને હિસાબ એક સાથે Tally અને Excel માં સંભાળવું ઘણી વાર મુશ્કેલ બને છે. તમારે ત્યાં અત્યારે આ કેવી રીતે ચાલે છે?
"""
    if hi_line:
        md += f"""
**Hindi**

> नमस्ते, मैं [आपका नाम] बोल रहा/रही हूँ, [कंपनी का नाम] से। क्या {(dm_first + 'जी') if dm_first else 'MD'} से बात हो सकती है?
>
> (DM मिलने पर) दो मिनट लूँगा। हम Ahmedabad की manufacturing कंपनियों के लिए Odoo और ERPNext implement करते हैं। मैंने देखा कि {hi_line}। ऐसे setup में stock, costing और हिसाब एक साथ Tally और Excel में संभालना अक्सर मुश्किल हो जाता है। आपके यहाँ अभी यह कैसे चलता है?
"""
    md += f"""
**English**

> Hi, this is [your name] from [company]. Could I speak with {dm}?
>
> (Once connected) I'll take two minutes. We implement Odoo and ERPNext for manufacturers in Ahmedabad. I saw that {h['en']}. In a setup like that, keeping track of {h['pain'].split(',')[0][0].lower() + h['pain'].split(',')[0][1:]} in Tally and Excel usually gets hard. How are you handling it today?

**Goal of the call:** a 30-minute visit at {a['cluster']}, not a demo over the phone.

> Close: "Can I come by your office for 30 minutes next week? I'll bring a short walkthrough of how a similar plant runs stock, production and accounts in one system."

## 2. Discovery questions

1. {q[0]}
2. {q[1]}
3. {q[2]}
4. Who besides you would be involved in choosing a system: your CA, accounts head, plant head?
5. Is there a date that matters, like 1 April, a new plant, or an audit?

## 3. What to show them (their version of the value)

{{talk_md}}

Lead with the first point. It is the one tied to their hook.

## 4. Questions they will probably ask

{{asks_md}}

Full answers are in `scripts/01-buyer-faq.md`. Fill the [fill] items there before calling.

## 5. Likely objections

- "Tally is enough." Agree it's good for accounts. Ask about {h['pain'].split(',')[0][0].lower() + h['pain'].split(',')[0][1:]}, which is where Tally runs out.
- "Too expensive." Phase 1 (inventory, purchase, sales, accounts, GST) starts from ₹2 lakh. {"ERPNext has no per-user licence if budget is tight." if "ERPNext" in r['odoo_vs_erpnext'] or "Either" in r['odoo_vs_erpnext'] else "Offer a fixed-scope phase 1 so cost is known up front."}
- "We already use Tranzact / a Tally add-on." Ask what still lives in Excel or WhatsApp.
- "Who else uses it?" Mention a building-materials manufacturer in MP where you built the ERP (never name the client), and offer reference-deal terms.

## 6. Email draft (not sent; send only after approval)

**Subject:** {subject(a, h)}

{('Hi ' + dm_first + ',') if dm_first else 'Hello,'}

I noticed {h['en']}.

When a manufacturer grows like that, the work behind {h['pain'][0].lower() + h['pain'][1:]} tends to end up split across Tally, Excel and WhatsApp, and the owner sees the real numbers weeks late.

We implement Odoo and ERPNext for manufacturers in Ahmedabad, starting with a fixed-scope first phase.

How are you handling {h['pain'].split(',')[0][0].lower() + h['pain'].split(',')[0][1:]} today?

[Your name]
[Title], [Company] | Odoo and ERPNext partner
[Phone]

If this isn't relevant, just reply "no thanks" and I won't follow up.
[Postal address]

**Follow-up, day 4 (same thread):** One thing we see often in {a['industry'].split(' ')[0].lower().replace('chemicals','chemical').replace('engineering','engineering')} plants: the first quick win is getting stock and batch movements into one place, before touching production planning. Happy to share what that would look like for {a['company'].split(' (')[0]} if useful.

**Follow-up, day 10 (same thread):** I'll leave this here. If it helps, I can send a one-page sketch of how your stock, production and accounts would sit in one system. No call needed, just reply "send it".

## 7. After the call: WhatsApp and LinkedIn (send only after approval)

**WhatsApp, same day (Gujarati):**

> {dm_first + 'જી' if dm_first else 'નમસ્તે'}, આજે વાત કરવા બદલ આભાર. [તમારું નામ], [કંપનીનું નામ]. આપણે ચર્ચા કરી તેમ, stock, costing અને હિસાબ એક જ system માં કેવી રીતે ચાલે તેનું ટૂંકું overview મોકલું છું. [visit date] એ મળવાનું ફાવશે?

**WhatsApp, same day (English):**

> Thanks for your time today, {dm_first or 'sir/madam'}. This is [your name] from [company]. As discussed, I'll share a short note on {{short_talk_en}}. Would [visit date] work for a 30-minute visit?

**LinkedIn connection note (under 300 characters):**

> {{li_note}}

## 8. Visit checklist

- Bring: one-page Odoo/ERPNext overview, the MP building-materials case (anonymised), a phase 1 price range.
- Ask to see: the stock register, a costing sheet, and how a purchase order is approved.
- Leave with: the main pain in their words, who else decides, and a date for a demo or a proposal.
"""
    pp = P.get(a["company"], dict(talk=[], asks=[]))
    talk_md = "\n".join(f"{i}. {t}" for i, t in enumerate(pp["talk"], 1)) or "1. Stock, purchase, sales and accounts in one system"
    asks_md = "\n".join(f"- **{FAQ[n][0]}** {FAQ[n][1]}" for n in pp["asks"] if n in FAQ) or "- See the FAQ."
    first_talk = (pp["talk"][0] if pp["talk"] else "stock and accounts in one system")
    li_note = f"Hi {dm_first or 'there'}, I saw that {h['en']}. We implement Odoo and ERPNext for manufacturers in Ahmedabad and I'd like to connect."
    if len(li_note) > 295: li_note = f"Hi {dm_first or 'there'}, we implement Odoo and ERPNext for Ahmedabad manufacturers. I saw {a['company'].split(' (')[0]}'s recent growth and would like to connect."
    md = md.replace("{talk_md}", talk_md).replace("{asks_md}", asks_md).replace("{li_note}", li_note)
    md = md.replace("{short_talk_en}", first_talk[0].lower() + first_talk[1:]).replace("{short_talk_gu}", "stock, costing અને હિસાબ એક system માં")
    md = md.replace("\n\n\n", "\n\n")
    with open(os.path.join(GTM, "scripts", "accounts", f"{r['account_id']}-{slug(a['company'])}.md"), "w", encoding="utf-8") as f:
        f.write(md)

# ---------- 4. Excel view ----------
try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.utils import get_column_letter
    from openpyxl.worksheet.datavalidation import DataValidation
    wb = Workbook(); ws = wb.active; ws.title = "Accounts"
    ws.append(COLS)
    for r in rows: ws.append([int(r[k]) if k == "fit_score" and str(r[k]).isdigit() else r.get(k, "") for k in COLS])
    dv = DataValidation(type="list", formula1='"' + ",".join(STATUSES) + '"', allow_blank=True)
    ws.add_data_validation(dv); dv.add(f"V2:V{len(rows)+50}")
    for fn, hdr in LOGS.items():
        s = wb.create_sheet(fn.replace(".csv","").replace("_"," ").title()); s.append(hdr)
        for r in logs[fn]: s.append([r.get(k,"") for k in hdr])
    h2 = wb.create_sheet("Held"); h2.append(["company","reason"])
    for x in HOLD: h2.append(list(x))
    summ = wb.create_sheet("Summary", 0)
    summ.append(["Metric","Value"])
    summ.append(["Accounts", len(rows)])
    for k, v in sorted(Counter(r["tier"] for r in rows).items()): summ.append([f"Tier {k}", v])
    for k, v in Counter(r["status"] for r in rows).most_common(): summ.append([f"Status: {k}", v])
    for fn in LOGS: summ.append([f"Logged {fn.replace('.csv','')}", len(logs[fn])])
    for sh in wb.worksheets:
        for c in sh[1]: c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="1F3864")
        for i in range(1, sh.max_column + 1): sh.column_dimensions[get_column_letter(i)].width = 22
        for row in sh.iter_rows(min_row=2):
            for c in row: c.alignment = Alignment(wrap_text=True, vertical="top")
        sh.freeze_panes = "A2"
    for col, w in {"B":30,"F":45,"K":45,"O":55}.items(): ws.column_dimensions[col].width = w
    ws.freeze_panes = "C2"; ws.auto_filter.ref = ws.dimensions
    wb.save(os.path.join(GTM, "leads", "ahmedabad-tracker.xlsx"))
except ImportError:
    print("openpyxl not installed: skipped Excel view")
print("accounts:", len(rows), dict(Counter(r["tier"] for r in rows)))
