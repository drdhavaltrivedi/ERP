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
A, HOLD = seed["A"], [tuple(x) for x in seed["HOLD"]]
from v2_27 import V as V27
from v3_27 import V3
from research_rules import NAMES, HOLD_OVERRIDE, NOTES, RANK, ADMIT

# Web research (one JSON record per company), merged into A (qualified) or HOLD (not a fit)
RES = os.path.join(GTM, "research", "ahmedabad-web-research.jsonl")
V2, PENDING = {}, []
known_sites = {a["website"].lower().replace("https://","").replace("http://","").replace("www.","").strip("/") for a in A}
if os.path.exists(RES):
    import json
    for line in open(RES, encoding="utf-8"):
        r = json.loads(line); d = r["d"].replace("http://","").replace("https://","").replace("www.","").strip("/")
        if d in known_sites: continue
        v = r.get("v") or ""
        if not v or "budget" in v: PENDING.append(d); continue
        if d in HOLD_OVERRIDE: v = "H:" + HOLD_OVERRIDE[d]
        if d in ADMIT: v = "Q"
        name = NAMES.get(d) or r.get("n") or d
        name = re.sub(r"\s*\((legal suffix|per |trading).*?\)", "", name).strip()
        if v != "Q":
            HOLD.append((name, v[2:].strip(), "http://www." + d)); continue
        ml = r.get("ml"); ml = ml is True or str(ml).lower() == "true"
        A.append(dict(company=name, industry=r.get("ind") or "Other", sub=r.get("sub",""), hc=r.get("hc",""),
            address=r.get("addr",""), cluster=(r.get("cl") or r.get("visit","")).split(";")[0].strip(), website="http://www." + d,
            phone=r.get("ph",""), email_generic=r.get("em",""), dm=r.get("dm") or "Not named on site", signal=r.get("sig",""),
            multi_loc=ml, rank=RANK.get(r.get("ind"), 5), src=r.get("src",""), li="", lang_code=r.get("lang") or "gu",
            note="; ".join(x for x in (ADMIT.get(d, ""), NOTES.get(d, "")) if x)))
        for k, pre in (("seen_hi", r"^main aapki website dekh raha tha[.,]?\s*"), ("seen_en", r"^i was looking at your website[.:,]?\s*(your website says\s*)?"), ("seen_gu", r"^(હું )?(આપની|તમારી) વેબસાઇટ જોઈ રહ્યો હતો[.,]?\s*")):
            if r.get(k): r[k] = re.sub(pre, "", r[k], flags=re.I)
        V2[name] = r
    with open(os.path.join(GTM, "research", "pending.txt"), "w") as f:
        f.write("# Not researched yet (web-fetch limit). Re-run research on these.\n" + "\n".join(PENDING) + "\n")
for c, x in V27.items(): V2[c] = x

COLS = ["account_id","company","industry","sub_segment","headcount","address","cluster","website","phone_board","email_generic",
        "decision_makers","linkedin_main","work_email","email_verification","pain_signal","signal_source","fit_score","tier",
        "odoo_vs_erpnext","call_language","owner","status","last_activity","next_step","next_step_date","notes"]
STATUSES = ["Researched","Called - no answer","Called - gatekeeper","Called - spoke to DM","Bad number","Nurture","Meeting booked","Visited",
            "Discovery done","Proposal sent","Won","Lost","Not a fit","Do not contact"]

def score(a):
    s = 20 if a["rank"] <= 3 else 10
    s += 10
    s += 15 if a["multi_loc"] else 0
    t = a["signal"].lower()
    kinds = [("hiring",), ("new plant","commissioned","planned","launched","acquired","acquisition"),
             ("subsidiar","sister company","group","offices","branch"), ("expansion","added","new unit","unit ii","unit 2"), ("listed",), ("export",)]
    s += min(30, 10 * sum(1 for ks in kinds if any(k in t for k in ks)))
    s += 0 if a["dm"].lower().startswith("not ") else 10
    s += 10 if a["phone"] and not a["phone"].startswith("(") else 0
    return min(s, 100)

LANG = {"gu": "Gujarati", "hi": "Hindi first (switch to Gujarati if they reply in it)", "en": "English first (switch to Hindi or Gujarati as they reply)"}

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
        signal_source=a["src"], fit_score=s, tier=tier(s), odoo_vs_erpnext=fit(a), call_language=h.get("lang") or LANG.get(a.get("lang_code","gu"), "Gujarati"),
        owner="", status="Researched", last_activity="", next_step=(f"Call board line, ask for {dm}" if dm else "Find owner name (MCA / Google Maps), then call"),
        next_step_date="", notes=("Do not contact Manish Patel: company site lists him as late." if "Mediwin" in a["company"] else a.get("note",""))))
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
    w = csv.writer(f); w.writerow(["company","reason","website"]); w.writerows([list(x) + [""] * (3 - len(x)) for x in HOLD])

# ---------- 3. per-account personalised scripts (v3 conversational format, see scripts/00-call-playbook.md) ----------
from script_v3 import write_scripts
write_scripts(ranked, rows, H, P, V2, FAQ, os.path.join(GTM, "scripts", "accounts"), first_dm, slug, V3=V3, calls=logs["calls.csv"])

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
    h2 = wb.create_sheet("Held"); h2.append(["company","reason","website"])
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
