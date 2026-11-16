# AMD-027 · Mahavir Industries (Mahavir Pigments)

| | |
|---|---|
| Industry | Chemicals: Organic and inorganic pigments |
| Ask for | the owner or managing director |
| Other contacts | Not named in fetched pages (site has a Management page to check) |
| Board phone | +91 90338 97601 ; +91 79 4008 5720 |
| Address / cluster | C-1/58 GIDC Phase-2, Vatva, Ahmedabad 382445 (Vatva) |
| Website | mahavirpigments.com |
| LinkedIn | not found yet |
| Fit | Score 50, Tier B. ERPNext first (single site, price-sensitive); Odoo if they want CRM/website |
| Call language | Gujarati |
| Hook (verified) | you're a Two Star Export House shipping to 40+ countries since 1979. Source: https://www.mahavirpigments.com/facility-certifications/ |
| Pain to probe | Export documentation, REACH/GOTS paperwork, batch records |

Before calling: check the person's current role on LinkedIn or the company site. Log every attempt in `gtm/logs/calls.csv`.

## 1. Call opener (30 seconds)

**Gujarati**

> નમસ્તે, હું [તમારું નામ] બોલું છું, [કંપનીનું નામ] માંથી. શું હું MD સાથે વાત કરી શકું?
>
> (DM મળે ત્યારે) નમસ્તે, બે મિનિટ લઈશ. અમે Ahmedabad ની manufacturing કંપનીઓ માટે Odoo અને ERPNext implement કરીએ છીએ. મેં જોયું કે તમે Two Star Export House છો અને 1979 થી 40 થી વધુ દેશમાં export કરો છો. આવા setup માં stock, costing અને હિસાબ એક સાથે Tally અને Excel માં સંભાળવું ઘણી વાર મુશ્કેલ બને છે. તમારે ત્યાં અત્યારે આ કેવી રીતે ચાલે છે?

**English**

> Hi, this is [your name] from [company]. Could I speak with the owner or managing director?
>
> (Once connected) I'll take two minutes. We implement Odoo and ERPNext for manufacturers in Ahmedabad. I saw that you're a Two Star Export House shipping to 40+ countries since 1979. In a setup like that, keeping track of export documentation in Tally and Excel usually gets hard. How are you handling it today?

**Goal of the call:** a 30-minute visit at Vatva, not a demo over the phone.

> Close: "Can I come by your office for 30 minutes next week? I'll bring a short walkthrough of how a similar plant runs stock, production and accounts in one system."

## 2. Discovery questions

1. How do you cost a batch today, including yield loss and by-products?
2. How do you move stock between plants or to job workers, and how often do the numbers not match?
3. How much of your export paperwork (invoices, packing lists, COAs) is made by hand?
4. Who besides you would be involved in choosing a system: your CA, accounts head, plant head?
5. Is there a date that matters, like 1 April, a new plant, or an audit?

## 3. What to show them (their version of the value)

1. Export documentation for 40+ countries from the sales order
2. REACH, GOTS and Halal paperwork linked to each batch
3. Moving a 1979-founded business off legacy systems in phases

Lead with the first point. It is the one tied to their hook.

## 4. Questions they will probably ask

- **Does it handle GST, e-invoicing and e-way bills?** Both have Indian localisation for GST invoices and returns data. E-invoice (IRN) and e-way bill generation through the government portals is supported. [verify: which edition and connector you deploy, and whether a GSP subscription is needed]
- **Can you move our Tally data?** Yes. We move masters (customers, suppliers, items, ledgers) and opening balances as standard. Moving past transactions is possible but costs more, and is usually not needed.
- **Will our business stop during the switch?** No. We run the new system alongside the old one for one or two weeks before go-live, so you can compare the numbers. Many clients go live on 1 April or at a month start, so the books open clean.

Full answers are in `scripts/01-buyer-faq.md`. Fill the [fill] items there before calling.

## 5. Likely objections

- "Tally is enough." Agree it's good for accounts. Ask about export documentation, which is where Tally runs out.
- "Too expensive." Phase 1 (inventory, purchase, sales, accounts, GST) starts from ₹2 lakh. ERPNext has no per-user licence if budget is tight.
- "We already use Tranzact / a Tally add-on." Ask what still lives in Excel or WhatsApp.
- "Who else uses it?" Mention a building-materials manufacturer in MP where you built the ERP (never name the client), and offer reference-deal terms.

## 6. Email draft (not sent; send only after approval)

**Subject:** mahavir plant-wise costing

Hello,

I noticed you're a Two Star Export House shipping to 40+ countries since 1979.

When a manufacturer grows like that, the work behind export documentation, REACH/GOTS paperwork, batch records tends to end up split across Tally, Excel and WhatsApp, and the owner sees the real numbers weeks late.

We implement Odoo and ERPNext for manufacturers in Ahmedabad, starting with a fixed-scope first phase.

How are you handling export documentation today?

[Your name]
[Title], [Company] | Odoo and ERPNext partner
[Phone]

If this isn't relevant, just reply "no thanks" and I won't follow up.
[Postal address]

**Follow-up, day 4 (same thread):** One thing we see often in chemical plants: the first quick win is getting stock and batch movements into one place, before touching production planning. Happy to share what that would look like for Mahavir Industries if useful.

**Follow-up, day 10 (same thread):** I'll leave this here. If it helps, I can send a one-page sketch of how your stock, production and accounts would sit in one system. No call needed, just reply "send it".

## 7. After the call: WhatsApp and LinkedIn (send only after approval)

**WhatsApp, same day (Gujarati):**

> નમસ્તે, આજે વાત કરવા બદલ આભાર. [તમારું નામ], [કંપનીનું નામ]. આપણે ચર્ચા કરી તેમ, stock, costing અને હિસાબ એક જ system માં કેવી રીતે ચાલે તેનું ટૂંકું overview મોકલું છું. [visit date] એ મળવાનું ફાવશે?

**WhatsApp, same day (English):**

> Thanks for your time today, sir/madam. This is [your name] from [company]. As discussed, I'll share a short note on export documentation for 40+ countries from the sales order. Would [visit date] work for a 30-minute visit?

**LinkedIn connection note (under 300 characters):**

> Hi there, I saw that you're a Two Star Export House shipping to 40+ countries since 1979. We implement Odoo and ERPNext for manufacturers in Ahmedabad and I'd like to connect.

## 8. Visit checklist

- Bring: one-page Odoo/ERPNext overview, the MP building-materials case (anonymised), a phase 1 price range.
- Ask to see: the stock register, a costing sheet, and how a purchase order is approved.
- Leave with: the main pain in their words, who else decides, and a date for a demo or a proposal.
