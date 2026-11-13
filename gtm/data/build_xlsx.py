import sys, os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
here = os.path.dirname(os.path.abspath(__file__))
ns = {}
exec(open(os.path.join(here, "accounts.py")).read(), ns)
A, HOLD = ns["A"], ns["HOLD"]

def score(a):
    s = 20 if a["rank"] <= 3 else 10
    s += 10  # headcount band 51-200 from Apollo (exact count unknown)
    s += 15 if a["multi_loc"] else 0
    t = a["signal"].lower()
    kinds = [("hiring",), ("new plant","commissioned","new manufacturing","planned","new sox","launched","acquired","acquisition"),
             ("subsidiar","sister company","multi-company","group","offices"), ("listed",), ("export",)]
    sig = sum(1 for ks in kinds if any(k in t for k in ks))
    s += min(30, 10 * sig)
    named = not a["dm"].lower().startswith("not ")
    s += 10 if named else 0
    s += 10 if a["phone"] and not a["phone"].startswith("(") else 0
    return min(s, 100)

def tier(s): return "A" if s >= 70 else ("B" if s >= 50 else "C")

def fit(a):
    t = (a["signal"] + a["sub"] + a["address"]).lower()
    multi = any(k in t for k in ["subsidiar", "brazil", "vietnam", "uae", "dubai", "thailand", "shanghai", "us outsourcing", "malaysia", "acquired"])
    if multi or a["industry"].startswith("Pharma"):
        return "Odoo (multi-company / multi-currency or pharma QC + lots)"
    if not a["multi_loc"]:
        return "ERPNext first (single site, cost-sensitive); Odoo if they want CRM/website"
    return "Odoo or ERPNext (decide on budget at discovery)"

cols = ["ID","Company","Industry","Sub-segment","Headcount","Address","Cluster (for visit routing)","Website","Phone (board)","Generic email",
        "Decision makers (from company site)","Pain signal","Signal source","Fit score","Tier","Odoo vs ERPNext (initial)","Work email (Apollo, pending)",
        "LinkedIn (main contact)","Owner","Status","Next step","Notes"]
wb = Workbook(); ws = wb.active; ws.title = "Ahmedabad accounts"
ws.append(cols)
rows = []
for a in A:
    s = score(a); rows.append((s, a))
rows.sort(key=lambda x: (-x[0], x[1]["cluster"]))
for i, (s, a) in enumerate(rows, 1):
    ws.append([f"AMD-{i:03d}", a["company"], a["industry"], a["sub"], a["hc"], a["address"], a["cluster"], a["website"], a["phone"],
               a["email_generic"], a["dm"], a["signal"], a["src"], s, tier(s), fit(a), "", a.get("li",""), "", "Researched", ("Call board line, ask for " + a["dm"].split(" (")[0].split("|")[0].strip()) if not a["dm"].lower().startswith("not ") else "Find owner name (Google Maps / MCA)", ("Do not contact Manish Patel (site lists him as late)" if "Mediwin" in a["company"] else "")])
hdr = PatternFill("solid", fgColor="1F3864")
for c in ws[1]:
    c.font = Font(bold=True, color="FFFFFF"); c.fill = hdr; c.alignment = Alignment(wrap_text=True, vertical="top")
widths = [9,30,16,30,14,48,20,22,26,28,40,55,35,8,6,32,22,22,10,12,22,20]
for i, w in enumerate(widths, 1): ws.column_dimensions[get_column_letter(i)].width = w
for row in ws.iter_rows(min_row=2):
    for c in row: c.alignment = Alignment(wrap_text=True, vertical="top")
ws.freeze_panes = "C2"; ws.auto_filter.ref = ws.dimensions

h = wb.create_sheet("Held - excluded"); h.append(["Company","Reason"])
for r in HOLD: h.append(list(r))
h.column_dimensions["A"].width = 45; h.column_dimensions["B"].width = 90

n = wb.create_sheet("How to read")
for line in [
 "Source: company websites read 13 Nov 2026; headcount band from Apollo free lookup (51-200). No Apollo credits used yet.",
 "Fit score (0-100) follows ICP section 9a. Headcount scored at 10 because only the band is known.",
 "Odoo vs ERPNext column is an initial guess from public info. Confirm at discovery: budget, users, customisation needs.",
 "Decision makers are as named on the company's own site. Verify current role on LinkedIn before outreach.",
 "Phone numbers are board/sales lines published on the site. Apollo has no mobile credits on this plan.",
 "Nothing in this sheet has been contacted. No outreach without approval.",
]: n.append([line])
n.column_dimensions["A"].width = 120
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "..", "ahmedabad-accounts.xlsx")
wb.save(out); print("saved", out, len(rows))
from collections import Counter
print(Counter(tier(s) for s,_ in rows))
