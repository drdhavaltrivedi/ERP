# AMD-023 · Alps Chemicals Pvt Ltd

| | |
|---|---|
| Industry | Chemicals: Dyes and pigments (paper, leather, food, inks) |
| Ask for | Haresh Bhuta |
| Other contacts | Haresh Bhuta (Owner); Nikhil Mehta (Director); Vandana Bhuta (Director) [LinkedIn] |
| Board phone | +91 96011 26325 (site also links +91 97244 08067) |
| Address / cluster | 612, Phase 4, Vatva GIDC, Ahmedabad 382445 (Vatva) |
| Website | alpschemicals.com |
| LinkedIn | https://in.linkedin.com/in/haresh-bhuta-857a7430 |
| Fit | Score 60, Tier B. ERPNext first (single site, price-sensitive); Odoo if they want CRM/website |
| Call language | Gujarati |
| Hook (verified) | you sell dyes and pigments in 40+ countries. Source: https://www.alpschemicals.com/contact/ |
| Pain to probe | Export documents, multi-currency receivables, batch shade records |

Before calling: check the person's current role on LinkedIn or the company site. Log every attempt in `gtm/logs/calls.csv`.

## 1. Call opener (30 seconds)

**Gujarati**

> નમસ્તે, હું [તમારું નામ] બોલું છું, [કંપનીનું નામ] માંથી. શું હું Hareshજી સાથે વાત કરી શકું?
>
> (DM મળે ત્યારે) Hareshજી, બે મિનિટ લઈશ. અમે Ahmedabad ની manufacturing કંપનીઓ માટે Odoo અને ERPNext implement કરીએ છીએ. મેં જોયું કે તમે 40 થી વધુ દેશમાં dyes અને pigments વેચો છો. આવા setup માં stock, costing અને હિસાબ એક સાથે Tally અને Excel માં સંભાળવું ઘણી વાર મુશ્કેલ બને છે. તમારે ત્યાં અત્યારે આ કેવી રીતે ચાલે છે?

**English**

> Hi, this is [your name] from [company]. Could I speak with Haresh Bhuta?
>
> (Once connected) I'll take two minutes. We implement Odoo and ERPNext for manufacturers in Ahmedabad. I saw that you sell dyes and pigments in 40+ countries. In a setup like that, keeping track of export documents in Tally and Excel usually gets hard. How are you handling it today?

**Goal of the call:** a 30-minute visit at Vatva, not a demo over the phone.

> Close: "Can I come by your office for 30 minutes next week? I'll bring a short walkthrough of how a similar plant runs stock, production and accounts in one system."

## 2. Discovery questions

1. How do you cost a batch today, including yield loss and by-products?
2. How do you move stock between plants or to job workers, and how often do the numbers not match?
3. How much of your export paperwork (invoices, packing lists, COAs) is made by hand?
4. Who besides you would be involved in choosing a system: your CA, accounts head, plant head?
5. Is there a date that matters, like 1 April, a new plant, or an audit?

## 3. What to show them (their version of the value)

1. Export documents and multi-currency receivables for 40+ countries
2. Batch and shade records per dye or pigment lot
3. A simple single-plant setup; ERPNext keeps running cost low

Lead with the first point. It is the one tied to their hook.

## 4. Questions they will probably ask

- **What is the licence cost?** - Odoo: priced per user per month, billed yearly. The India Standard plan was listed around ₹725 per user per month. [verify on odoo.com/pricing]
- **Does it handle GST, e-invoicing and e-way bills?** Both have Indian localisation for GST invoices and returns data. E-invoice (IRN) and e-way bill generation through the government portals is supported. [verify: which edition and connector you deploy, and whether a GSP subscription is needed]
- **Can you move our Tally data?** Yes. We move masters (customers, suppliers, items, ledgers) and opening balances as standard. Moving past transactions is possible but costs more, and is usually not needed.

Full answers are in `scripts/01-buyer-faq.md`. Fill the [fill] items there before calling.

## 5. Likely objections

- "Tally is enough." Agree it's good for accounts. Ask about export documents, which is where Tally runs out.
- "Too expensive." Phase 1 (inventory, purchase, sales, accounts, GST) starts from ₹2 lakh. ERPNext has no per-user licence if budget is tight.
- "We already use Tranzact / a Tally add-on." Ask what still lives in Excel or WhatsApp.
- "Who else uses it?" Mention a building-materials manufacturer in MP where you built the ERP (never name the client), and offer reference-deal terms.

## 6. Email draft (not sent; send only after approval)

**Subject:** alps plant-wise costing

Hi Haresh,

I noticed you sell dyes and pigments in 40+ countries.

When a manufacturer grows like that, the work behind export documents, multi-currency receivables, batch shade records tends to end up split across Tally, Excel and WhatsApp, and the owner sees the real numbers weeks late.

We implement Odoo and ERPNext for manufacturers in Ahmedabad, starting with a fixed-scope first phase.

How are you handling export documents today?

[Your name]
[Title], [Company] | Odoo and ERPNext partner
[Phone]

If this isn't relevant, just reply "no thanks" and I won't follow up.
[Postal address]

**Follow-up, day 4 (same thread):** One thing we see often in chemical plants: the first quick win is getting stock and batch movements into one place, before touching production planning. Happy to share what that would look like for Alps Chemicals Pvt Ltd if useful.

**Follow-up, day 10 (same thread):** I'll leave this here. If it helps, I can send a one-page sketch of how your stock, production and accounts would sit in one system. No call needed, just reply "send it".

## 7. After the call: WhatsApp and LinkedIn (send only after approval)

**WhatsApp, same day (Gujarati):**

> Hareshજી, આજે વાત કરવા બદલ આભાર. [તમારું નામ], [કંપનીનું નામ]. આપણે ચર્ચા કરી તેમ, stock, costing અને હિસાબ એક જ system માં કેવી રીતે ચાલે તેનું ટૂંકું overview મોકલું છું. [visit date] એ મળવાનું ફાવશે?

**WhatsApp, same day (English):**

> Thanks for your time today, Haresh. This is [your name] from [company]. As discussed, I'll share a short note on export documents and multi-currency receivables for 40+ countries. Would [visit date] work for a 30-minute visit?

**LinkedIn connection note (under 300 characters):**

> Hi Haresh, I saw that you sell dyes and pigments in 40+ countries. We implement Odoo and ERPNext for manufacturers in Ahmedabad and I'd like to connect.

## 8. Visit checklist

- Bring: one-page Odoo/ERPNext overview, the MP building-materials case (anonymised), a phase 1 price range.
- Ask to see: the stock register, a costing sheet, and how a purchase order is approved.
- Leave with: the main pain in their words, who else decides, and a date for a demo or a proposal.
