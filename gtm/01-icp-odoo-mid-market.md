# ICP: Odoo for 50 to 200 employee companies (Ahmedabad first)

Version 0.2, 13 Nov 2026. Updated with your answers (no live references yet, ₹2 lakh minimum deal, Odoo or ERPNext per client) and with desk research on buyer pain.

Labels used in this document:
- **Fact**: verifiable rule or data point.
- **Assumption**: my working belief, to be validated on the first 20 to 30 conversations.
- **Verify**: I believe this is right but it should be checked before it goes in a pitch.

---

## 1. One-line ICP

A promoter-led Indian manufacturer or distributor with 50 to 200 employees, running its business on Tally plus Excel (sometimes a local or custom tool), with more than one location or warehouse, inventory that needs batch, lot or job-work tracking, and a visible trigger (growth, new plant, export start, compliance pressure, a second-generation owner, or an SME IPO plan) that makes the current setup break.

## 2. Firmographics

| Attribute | Target | Notes |
|---|---|---|
| Headcount | 50 to 200 (sweet spot 70 to 150) | Below 50, Tally plus add-ons usually wins on price. Above 200, SAP B1 and S/4 partners compete harder and sales cycles lengthen. |
| Revenue | Roughly ₹25 Cr to ₹300 Cr | **Assumption.** Headcount is a weak proxy in manufacturing; a 60-person chemical unit can turn over more than a 180-person garment unit. |
| Ownership | Private, promoter or family owned, or PE backed | Skip subsidiaries of large groups or MNCs: they buy centrally and usually standardise on SAP or Oracle. |
| Location (Phase 2) | HQ, plant or main warehouse in Ahmedabad district | Clusters to route visits by: Naroda, Vatva, Odhav, Kathwada GIDC (chemicals, engineering); Changodar, Moraiya, Sanand, Bavla (pharma, engineering, FMCG); Narol, Odhav, Pirana (textile processing); Aslali, Sarkhej, Kathwada (warehousing, distribution). |
| Current systems | Tally Prime / ERP 9, Busy, Marg (common in pharma distribution), Excel, custom FoxPro or VB apps, standalone payroll | Companies already live on SAP B1 within the last 3 years are low priority; rip and replace is rare. |
| Structure | 2+ locations, or 2+ GSTINs, or plant + depot(s) | Single-location traders are a poor fit. |

## 2b. Decisions from your answers (v0.2)

- **Manufacturing only for the first 100.** Pharma, chemicals and engineering are the core. Distribution and textiles move to "later".
- **Add building materials** (bricks, AAC blocks, ceramics, cement products) as a segment. You have built an ERP for a brick manufacturer in Madhya Pradesh. Refer to it only as "a building-materials manufacturer in MP" and never name the client. In Ahmedabad this segment is thin; it matters more in Phase 3 (Morbi ceramics cluster, Himmatnagar).
- **Reference-first strategy.** With no live Odoo/ERPNext references, the first 2 or 3 deals should be priced as reference deals (fixed-price pilot or discount in exchange for a case study and a site visit). Concentrate early effort in one cluster (Vatva chemicals is the densest in the current list) so one win becomes a story for the neighbours.
- **Pricing floor.** ₹2 lakh minimum. My view: treat it as the entry price for Phase 1 (inventory, purchase, sales, accounting, GST) and quote manufacturing, QC and costing as Phase 2. Pricing a full manufacturing rollout at ₹2 lakh risks a loss-making or under-delivered first reference. This is judgement, not market data.
- **Product choice per client.** Every account in the list carries an "Odoo vs ERPNext (initial)" column. Rule of thumb in section 7.

## 3. Industries and why each one needs an ERP

Ranked by my estimate of fit for a first 100 accounts. Ranking is an **assumption**, mainly driven by complexity of inventory, regulatory pull, and density in Ahmedabad.

| Rank | Industry | What breaks in Tally/Excel | Odoo modules that matter |
|---|---|---|---|
| 1 | **Pharma formulations and API (small/mid units)** | Batch and expiry tracking, QC release, BMR/BPR linkage, near-expiry write-offs, loan-licence and third-party manufacturing, regulator audit trails | Inventory (lots, expiry, FEFO), MRP, Quality, PLM, Purchase, Accounting |
| 2 | **Specialty and dye/pigment chemicals** | Formula/recipe BOMs, yield and by-product costing, multi-UoM (kg, drum, tanker), hazardous storage, export documentation | MRP with by-products, Inventory, Quality, multi-currency Accounting |
| 3 | **Engineering and fabrication (pumps, valves, machine parts, auto components)** | Make-to-order, job work with GST ITC-04, subcontracting, project and job costing, spare parts | MRP, Subcontracting, Project, Timesheets, Maintenance |
| 4 | **Distribution (pharma, FMCG, building materials, electricals)** | Multi-warehouse stock, schemes and discounts, credit control, e-way bills at volume, salesman tracking | Inventory, Sales, CRM, Accounting, Field Service / mobile |
| 5 | **Textiles (processing, yarn, technical textiles, garments)** | Job work across processing houses, lot/shade tracking, meter-to-kg conversions, high wastage | MRP, Subcontracting, Inventory with lots |
| 6 | **Plastics, packaging, and other process manufacturing** | Machine-level production, scrap, mould tracking | MRP, Maintenance, Quality |

**Risk on textiles:** margins in commodity textile processing are thin and many units are price-driven. I would treat textiles as a lower-priority segment unless you already have a textile reference customer. Technical textiles and branded apparel are better targets than job-work process houses.

## 4. Pain signals (what tells us a company needs an ERP now)

Split into signals we can **observe from outside** (usable for list building) and signals we can only **confirm in a conversation** (usable for qualification).

### 4a. Observable signals (for list building)

| Signal | How to detect | Strength |
|---|---|---|
| Hiring for "Tally accountant", "MIS executive", "store keeper", "inventory controller", "billing executive" (multiple openings) | Naukri, LinkedIn Jobs, Apollo job postings, Indeed | High: they are throwing people at a systems problem |
| Hiring for "ERP executive", "SAP B1", "ERP implementation" | Same sources | Very high: active project, but a competitor may already be shortlisted |
| New plant, capacity expansion, new warehouse, new depot | Company news, Gujarat government MoUs, local press, LinkedIn posts, environmental clearance notices (chemicals/pharma) | High |
| Started or expanding exports | DGFT/export award mentions, trade fair participation (CPHI, Chemexcil, etc.), website "export" pages | Medium-high |
| SME IPO filed or planned (NSE Emerge, BSE SME) | DRHP filings, news | Very high: auditors and merchant bankers push for proper systems and controls |
| Second-generation family member (often MBA) joining as director | LinkedIn, website "about us" | Medium-high: modernisation champion |
| WHO-GMP / EU-GMP / USFDA inspection plans, or revised Schedule M upgrade (pharma) | Website certifications, news | High for pharma. **Verify** the current Schedule M compliance deadline for MSMEs before using it in a pitch. |
| Multiple GSTINs / branches across states | GST portal search, website "our offices" | Medium |
| Website and branding look modern but no ERP or portal visible (no dealer/customer login) | Website review | Low, supporting only |

### 4b. Confirmed-in-conversation signals (for qualification)

- Month-end close takes more than 7 to 10 days, or depends on one person.
- Stock in Tally does not match physical stock; annual stock-take surprises.
- Costing per product or per batch is done in Excel, or not at all.
- E-invoicing and e-way bills are generated manually or through a separate utility. **Fact:** e-invoicing is mandatory above ₹5 Cr aggregate turnover. **Verify** the IRP 30-day reporting rule for businesses above ₹10 Cr before quoting it.
- Owner cannot see live sales, receivables, or stock on a phone.
- Purchase approvals are on WhatsApp.
- Different departments keep their own Excel files (production plan, dispatch plan, QC register).
- A key accounts or stores person left recently and things fell apart.

## 4c. What buyers say online (desk research, 13 Nov 2026)

Sources: Capterra reviews of TallyPrime (about 25 full reviews read), G2 Odoo vs TallyPrime comparison, Google-indexed Reddit threads in r/IndiaBusiness, r/Indian_Business, r/StartUpIndia, r/Odoo (Reddit itself blocks automated reading, so only titles and snippets were seen), and two vendor blogs (marked). Most Capterra reviewers are accountants, not factory owners, so treat this as directional.

| Theme | Evidence | Strength |
|---|---|---|
| Tally UI is dated and hard to learn | 8 of 25 Capterra reviews; G2 tags "poor interface" (13) and "learning curve" (12) | Medium. Owners still like Tally for accounts, so do not attack Tally; position Odoo/ERPNext as the operations layer |
| Limited customisation and reporting, "extract everything piece by piece" | 7 of 25 Capterra reviews | Medium-high. Ties to the MIS-executive hiring signal |
| Slow with several users or large data | 4 of 25 Capterra reviews | Medium |
| Multi-location stock weak in Tally | 1 Capterra review, plus Reddit snippets about "Excel, Tally, Busy, WhatsApp orders and disconnected inventory" | Medium. Matches the ICP multi-location filter |
| Owners already bolt a production tool onto Tally | Reddit r/IndiaBusiness: owners report using Tranzact plus Tally for BOM, job cards, work orders, quoted at about ₹5,000 to ₹7,000 per month | **High. Tranzact is a direct competitor in this segment** and was missing from v0.1 |
| "Odoo implementation is too costly" | Reddit snippet comparing Odoo and Tranzact | High. Lead with ERPNext or a fixed-scope Odoo phase 1 for price-sensitive buyers |
| Accountants resist cloud | Reddit r/IndiaBusiness: "No real accountant wants cloud" style comments | Medium. Offer on-premise or hybrid, and involve the CA early |
| Pharma needs batch and expiry | Reddit snippets on batch/expiry tracking in pharma | Medium |

Published pricing seen (to verify on vendor sites before quoting): TallyPrime Silver about ₹22,500 one-time, Gold multi-user about ₹2,250/month; Odoo Standard about ₹725 per user per month billed yearly; ERPNext software free, Frappe Cloud hosting from about ₹410/month. Source: an editorial comparison on echai.ventures citing vendor price pages. Implementation timelines: G2 users report about 6 months for both Odoo and Tally; one Odoo implementer claims 10 to 12 weeks (vendor claim).

**Competitors to name in the ICP:** Tally plus add-ons (TDL customisations), Tranzact, Busy, Marg (pharma distribution), Zoho Inventory/Books, SAP Business One partners, local custom-ERP developers.

**What I could not get:** first-hand Reddit threads and Quora answers (both block automated reading). If you want this deeper, the fastest route is 5 to 10 short calls with plant owners you know, using the questions in section 9b.

## 5. Buyer personas

Indian mid-market manufacturing is promoter-led. In practice one person decides, and two or three people can kill the deal.

| Persona | Typical title | Role in deal | What they care about | What they fear |
|---|---|---|---|---|
| **Promoter / MD** | Managing Director, Director, Owner, Partner | Economic buyer, final decision | Control and visibility, growth without adding headcount, cost, "what are others in my industry using" | Overpaying, a failed project, data leaking to staff, being locked to a vendor |
| **Second-generation director** | Director, Executive Director, Director Operations | Champion, often initiates | Modern tools, dashboards, scaling the business they will inherit | Being overruled by the senior generation |
| **Finance head** | CFO, GM Finance, Accounts Manager, often a CA | Influencer, frequently the blocker | GST compliance, audit trail, faster close, TDS/TCS, bank reconciliation | Losing Tally familiarity, migration errors, his team's workload during go-live, the external CA's opinion |
| **Operations / plant head** | Plant Head, Production Manager, GM Operations | Influencer, key user | Production planning, material availability, reducing firefighting | More data entry on the shop floor |
| **Purchase / stores** | Purchase Manager, Store In-charge | User, can sabotage adoption | Simple GRN, reorder alerts | Being exposed for stock mismatches |
| **IT** | IT Manager or "the computer person", often absent | Gatekeeper on tech, rarely a buyer | Hosting, backups, access control | Extra work |
| **External CA** | Auditing CA firm | Hidden influencer | Clean books in a format he can audit | Losing his Tally-based workflow |

**Implication:** the first meeting should be with the promoter or the second-generation director. Starting with the accounts manager usually ends in "Tally is fine".

## 6. Objections and how to answer them

| Objection | What is usually behind it | Response approach |
|---|---|---|
| "Tally is enough for us." | Accounting works; the pain is in operations, which the finance person does not feel | Agree Tally is good accounting software. Move the conversation to stock accuracy, costing, production planning. Offer to keep Tally for statutory books during transition if needed (Odoo integrates or replaces). |
| "ERP projects fail. We tried one before." | Real history with a local vendor or a stalled SAP B1 project | Ask what failed. Offer phased go-live (inventory and purchase first, then manufacturing), fixed-scope first phase, and a reference visit. |
| "Too expensive." | Comparing to Tally licence cost, not to the cost of extra staff and stock losses | Build a simple ROI: one or two fewer clerical hires, a percentage reduction in dead or expired stock, faster collections. Offer ERPNext as the lower-cost option if budget is the real block. |
| "Odoo is a foreign product. Does it handle Indian GST?" | Unfamiliarity | Show Indian localisation live: GST returns, e-invoice and e-way bill integration, TDS. **Verify** exactly which India features are native in the Odoo version you deploy versus partner add-ons. |
| "Our staff will not use it." | Low computer literacy on the floor | Mobile and barcode-based screens, Gujarati-speaking trainers, a super-user in each department. |
| "Our CA does not want it." | CA's workflow is Tally-based | Offer to involve the CA early, give them an accountant login, show audit trail and standard reports. |
| "We already use Tranzact / a Tally add-on for production." | Cheap tool covers the shop floor, accounts stay in Tally | Do not fight it head on. Ask what breaks: multi-plant stock, QC, costing, approvals, dashboards. Pitch ERPNext where price decides, Odoo where they want one system for sales, CRM, purchase and QC. |
| "We are evaluating SAP B1 / a local ERP." | Active buying cycle | Good sign. Compete on total cost (licences, hardware, customisation), flexibility, and modules beyond accounting. Ask for the evaluation criteria. |
| "Not now. After Diwali / after March close." | Timing or low priority | Agree a date. Position a discovery workshop now so implementation can start in the quiet period. April 1 is a natural go-live date for a new financial year. |
| "Our data is confidential." | Cloud trust | Offer on-premise or Odoo.sh / private cloud hosting, role-based access. |

## 7. Odoo or ERPNext: when to switch the pitch

You are partnered with both. Pitch Odoo first, but switch when:

- Budget is the hard block and the company accepts a more hands-on implementation: **ERPNext** (no per-user licence).
- The buyer wants deep custom workflows and owns an in-house developer: **ERPNext** can fit.
- The buyer wants polished UI, broad modules (CRM, e-commerce, website, HR, helpdesk) and a large partner ecosystem: **Odoo**.

This keeps a lost Odoo deal from becoming a lost customer.

## 8. Disqualifiers (do not add to the list)

- Fewer than 40 or more than 300 employees.
- Subsidiary of an MNC or of a large listed group that buys centrally.
- Went live on SAP B1, S/4, Oracle, Microsoft Dynamics, or Odoo with another partner in the last 3 years.
- Pure trading with one location and no inventory complexity.
- Signs of distress: plant closure, insolvency proceedings, mass layoffs.
- Staffing agencies, consultancies, research associations, job boards (these show up in database searches and must be filtered out).

## 9. Lead qualification

### 9a. Fit score (desk research, 0 to 100, decides whether an account enters the list)

| Factor | Points |
|---|---|
| Industry rank 1 to 3 | 20 (rank 4 to 6: 10) |
| Headcount 70 to 150 | 15 (50 to 69 or 151 to 200: 10) |
| Multi-location / multi-GSTIN | 15 |
| Observable pain signal from 4a | 10 per signal, max 30 |
| Decision maker identified by name with a dated source | 10 |
| Phone and address verified | 10 |

Tier A: 70+. Tier B: 50 to 69. Tier C: below 50 (keep for later nurture, do not visit).

### 9b. Conversation qualification (after first call or visit)

A simple version of BANT adapted for promoter-led companies:

1. **Pain:** Can they name a specific, costly problem (stock mismatch, slow close, costing blind spot)? Required.
2. **Power:** Is the promoter or a director in the conversation, or will they be at the next meeting? Required by meeting two.
3. **Trigger and timing:** Is there a reason to act within 6 months (new financial year, new plant, audit, IPO)? Strongly preferred.
4. **Budget reality:** Do they accept that a proper implementation costs more than a Tally licence? Required before proposal.
5. **Current state:** What runs today, who maintains it, what has been tried? Needed for scoping.

Move to proposal only when 1, 2 and 4 are true.

## 10. Open questions

Answered on 13 Nov 2026: no live references yet (one past ERP build for a building-materials manufacturer in MP), ₹2 lakh minimum deal, product chosen per client.

Still open:
1. How many people will visit and call, and can they pitch in Gujarati? This sets how many accounts per week are realistic.
2. Apollo credit budget for work emails (estimate 60 to 100 credits for Ahmedabad).
