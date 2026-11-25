# AMD-071 · MAAN Pharmaceuticals Ltd.: call script

**Call:** +91 8657484001/02; +91 93218 65230
**Ask for:** owner or MD (name not on the site; ask the receptionist)
**Language:** Gujarati first (Gujarati section below), then mirror them. If they answer in Hindi, use the Hinglish lines.
**Status:** Researched · next: Find owner name (MCA / Google Maps), then call
**What we know (from their website):** De-addiction, cardiology, nephrology and general pharma formulations. 506 Samedh, Near Associate Petrol Pump, C G Road, Ahmedabad-380009 (contact office). WHO-GMP Mehsana facility; approvals from various country regulators claimed; present in 30+ markets; Careers page with apply form, openings not listed; annual return 2024-25 posted; listing status not stated
**Fit:** score 65, tier B. Odoo (multi-company/multi-currency or pharma QC + lots)
**Goal of the call:** leave with one of: a visit date at the Ahmedabad CG Road office, the right person's name and a good time, one real fact about how they run today, or a callback date. Do not sell on the phone.

**Caution:** Plant in Mehsana; office in Ahmedabad.

Source: https://maanpharma.com/ (reached via redirect from http://www.maanpharmaindia.com, 302). Check the person's current role on LinkedIn or the site before calling. How to run the conversation: `scripts/00-call-playbook.md`.

---

## 1. Open the call (15 seconds)

**If reception answers** (playbook branch A): get the name, the best time and a direct number.

> **Dhaval:** Namaste, main Dhaval, Brilworks se, Ahmedabad. Ek chhoti si help chahiye thi. Aapke yahan operations aur accounts ka software ya system kaun dekhta hai? Owner ya MD sahab?
>
> **If "sir abhi nahi hain":** Koi baat nahi. Woh usually kab milte hain, subah ya shaam? Aur unka extension ya direct number mil sakta hai?
>
> **If "mail kar dijiye":** Zaroor. Kis naam se bhejun, aur unka email kya hai? Mail ke baad Thursday ko call karun toh baat ho jayegi?

*Ask the receptionist's name and use it next time.*

**When you reach {name} ji:**

> **Dhaval:** Namaste {name} ji, main Dhaval, Brilworks se, Ahmedabad. Seedha bolun toh yeh ek cold call hai. 30 second de sakte hain? Phir aap batana baat karni hai ya nahi.
>
> **If yes:** Main aapki website dekh raha tha. Ahmedabad se aap 30+ markets ke liye de-addiction aur generic formulations export karte hain, aur Mehsana mein WHO-GMP plant hai. Hum manufacturers ke saath ERP ka kaam karte hain, Odoo aur ERPNext. Toh ek cheez samajhni thi: abhi stock aur accounts ke liye kya use karte hain, Tally ya koi ERP?

*Their answer picks the branch in section 3. Stop talking and listen.*

## 2. Questions to have ready (ask one, then follow their answer)

Pick the next question from what they just said, not from the list order.

- **Easy, about their setup:** "Mehsana plant aur Ahmedabad office ke beech stock aur production planning kaise sync hoti hai?"
- **The pain question:** "Multi-country export ke liye export documents aur batch-wise stock ka record abhi kaise rakhte hain?"
- **Another angle:** "Buprenorphine jaise regulated products ke liye batch tracking aur dispatch approvals manually hote hain kya?"
- **Dig deeper:** "Yeh kaam abhi kaun sambhalta hai, aur kitni baar?"
- **Dig deeper:** "Yeh hamesha se aisa hai, ya naya plant ya naya product aane ke baad shuru hua?"
- **Who feels it:** "Yeh sabse zyada kisko pareshan karta hai, accounts ko, plant ko, ya aapko?"
- **The last time:** "Last time yeh hua tha, toh kya hua? Kitna time laga?"

*Echo their last few words when they go vague ("Thoda manual?"). Don't ask about revenue or margins on the first call.*

## 3. What they say, what you say

| They say | Dhaval says |
|---|---|
| "Busy hoon." | "Bilkul. Ek line mein bataun kyon call kiya: Ahmedabad se aap 30+ markets ke liye de-addiction aur generic formulations export karte hain, aur Mehsana mein WHO-GMP plant hai. Isliye ek sawaal tha. Kal 11 baje ya shaam 5 ke baad, kya theek rahega?" |
| "Email bhej do." | "Zaroor. Taaki generic mail na ho: aapke liye zyada important kya hai, stock aur batch tracking ya production costing? ... Aur mail ke baad Friday ko 2 minute call kar lun?" Confirm the address letter by letter. |
| "Tally aur Excel pe chal raha hai." | "Tally accounts ke liye best hai, woh chalu rahega. Excel mein sabse badi sheet kaunsi hai? ... Multi-country export ke liye export documents aur batch-wise stock ka record abhi kaise rakhte hain?" |
| "Humare paas ERP hai." | "Achha, kaunsa? Kab se chal raha hai? Ise kaun own karta hai?" Then: "Ab bhi koi report hai jo har mahine Excel mein bahar nikaal ke banani padti hai?" Get a follow-up date (playbook branch E). |
| "Abhi naya ERP liya hai." | "Congratulations. Kaunsa, aur partner kaun hai? Go-live kab ka target hai? Pehle phase mein kya aa raha hai?" Exit: "Go-live ke 2-3 mahine baad ek baar call karun?" |
| "Zaroorat nahi hai." | "Fair hai. Ek cheez pooch sakta hoon: kya isliye ki sab already system mein hai, ya abhi priority kuch aur hai?" (playbook branch F) |
| Wrong person (IT, accounts staff) | "Aap hi sahi insaan ho yeh samajhne ke liye. Abhi kya system hai? ... Iska decision usually kaun leta hai?" Ask for an introduction. |
| "Kitna kharcha hoga?" | "Phase 1 (stock, purchase, sales, accounts) ₹2 lakh se shuru hota hai. Exact quote aapka setup dekh ke dunga. Isliye milna zaroori hai." |
| "Pehle bhi ERP try kiya, kaam nahi kiya." | "Kya hua tha? ... Hum phase mein go-live karte hain, ek saath sab nahi badalte." |
| "Aapke clients kaun hain Ahmedabad mein?" | "MP mein humne ek building-materials manufacturer ka ERP banaya hai. Ahmedabad mein is saal pehle 2-3 manufacturers ke saath reference terms pe shuru kar rahe hain." (Never name the client. Don't claim local clients.) |
| Clear no, "dobara call mat karna" | "Bilkul, sorry for disturbing. Thank you." Set status to `Do not contact`. |

## 4. When you hear the pain

Ask one more question about it first. Then reflect it back:

> **Dhaval:** Toh Mehsana aur Ahmedabad ka stock alag registers mein rehta hoga, jise milana mushkil hota hoga. Sahi samjha?

One line of value, then the visit ask:

> **Dhaval:** Hum yahi karte hain. Ek ERP mein Mehsana plant ka stock, batch aur export docs Ahmedabad office se ek jagah dikhenge, aur Tally accounts aur GST ke liye rehne de sakte hain. Kya main next week Ahmedabad CG Road office aa ke 30 minute dikha sakta hoon ki aapke setup mein yeh kaisa dikhega? Tuesday ya Thursday?

*When they agree:* "Main WhatsApp pe confirm bhejta hoon. Yeh number sahi hai?"

## 5. Leave with a next step

Never end with "main contact karta hoon". End with a date, a name or a number, and thank them by name:

> **Dhaval:** Bahut shukriya {name} ji, aapka time dene ke liye. Toh main [day] ko [time] call karta hoon.

## Gujarati lines

> નમસ્તે, હું ધવલ બોલું છું, Brilworks માંથી, Ahmedabad. તમારે ત્યાં operations અને accounts નું software કોણ જુએ છે?
>
> નમસ્તે {name}જી, હું ધવલ, Brilworks માંથી, Ahmedabad. બે મિનિટ વાત થઈ શકે?
>
> અમે Odoo અને ERPNext ના partner છીએ. Manufacturers માટે stock, production, sales અને accounts એક system માં લાવીએ છીએ. હું તમારી website જોઈ રહ્યો હતો. તમે 30થી વધુ માર્કેટમાં એક્સપોર્ટ કરો છો, અને મહેસાણામાં WHO-GMP પ્લાન્ટ છે.
>
> અત્યારે stock અને accounts માટે શું વાપરો છો, Tally કે કોઈ ERP?
>
> મલ્ટી-કન્ટ્રી એક્સપોર્ટ માટે એક્સપોર્ટ ડોક્યુમેન્ટ અને બેચ વાઇઝ સ્ટોકનો રેકોર્ડ અત્યારે કેવી રીતે રખાય છે?
>
> આવતા અઠવાડિયે Ahmedabad CG Road office પર 30 મિનિટ મળવા આવી શકું? મંગળવાર કે ગુરુવાર, શું ફાવશે?

## English lines

> Hi {name}, this is Dhaval from Brilworks in Ahmedabad. To be upfront, this is a cold call. Can I take 30 seconds, and then you tell me if it's worth continuing?
>
> I was looking at your website. Your WHO-GMP plant at Mehsana and exports to 30+ markets are clear from your website. We're Odoo and ERPNext partners, so I wanted to ask: what do you use for stock and accounts today, Tally or an ERP?
>
> How do you keep export documents and batch-wise stock records today across markets?
>
> Could I come by the Ahmedabad CG Road office for 30 minutes next week? Would Tuesday or Thursday suit you better?

## Questions they will probably ask

- **Pharma: batch, expiry, FEFO, QC release?** Yes: lot and serial tracking with expiry dates, FEFO picking, quality checks before release, and quarantine stock. QC module availability differs by product and edition [verify for Odoo: Quality is an Enterprise app].
- **Will it pass audits? (pharma: GMP, chemicals: REACH, BRC and similar)** The system keeps a full audit trail of who changed what and when, plus lot and batch traceability from raw material to dispatch. It supports your compliance work, but certification is still your process. In pharma, say: "Batch records and QC release can be tracked in the system; we'll map it to your SOPs in discovery."
- **Can you move our Tally data?** Yes. We move masters (customers, suppliers, items, ledgers) and opening balances as standard. Moving past transactions is possible but costs more, and is usually not needed.
- **How much does it cost?** Two parts: the implementation (our fee) and the software licence or hosting. Phase 1 (inventory, purchase, sales, accounting and GST) starts from ₹2 lakh for implementation. The final number depends on users, plants and how much data we migrate. We give a fixed quote after a half-day discovery.
- **How long will it take?** Phase 1 typically takes 8 to 12 weeks from kickoff to go-live, depending on how quickly your team gives us data and decisions. [fill: confirm from your own delivery plan] Manufacturing, QC and costing come in phase 2.

Full answers are in `scripts/01-buyer-faq.md`. Fill the [fill] items there before calling.

## Email draft (not sent; send only after approval)

**Subject:** MAAN Pharmaceuticals Ltd.: how do you keep export documents and batch-wise stock record

Hello,

I was looking at your website. Your WHO-GMP plant at Mehsana and exports to 30+ markets are clear from your website.

How do you keep export documents and batch-wise stock records today across markets? In plants like yours this often ends up split across Tally, Excel and WhatsApp, and the owner sees the real numbers late.

I'm Dhaval from Brilworks, an Odoo and ERPNext partner in Ahmedabad. We put stock, production, sales and accounts in one system, starting with a fixed-scope first phase. Tally can stay for accounts and GST while you move.

Could I come by the Ahmedabad CG Road office for 30 minutes next week?

Dhaval
Brilworks | Odoo and ERPNext partner
[Phone]

If this isn't relevant, just reply "no thanks" and I won't follow up.

**Follow-up, day 4 (same thread):** One quick win we usually start with: getting stock and batch movements into one place before touching production planning. Happy to show what that would look like for MAAN Pharmaceuticals Ltd..

**Follow-up, day 10 (same thread):** I'll leave this here. If useful, I can send a one-page sketch of how your stock, production and accounts would sit in one system. Just reply "send it".

## WhatsApp after the call (send only after approval)

> નમસ્તે, આજે વાત કરવા બદલ આભાર. ધવલ, Brilworks. આપણે વાત કરી તેમ [visit date] એ Ahmedabad CG Road office પર 30 મિનિટ મળીએ. Confirm કરશો?

## Visit checklist

- Bring: one-page Odoo/ERPNext overview, the MP building-materials case (anonymised), a phase 1 price range.
- Ask to see: the stock register, a costing sheet, and how a purchase order is approved.
- Leave with: the main pain in their words, who else decides, and a date for a demo or a proposal.

## After the call (2 minutes)

Log in `gtm/logs/calls.csv` with an `outcome` code from the playbook: who you spoke to, their role, language used, what system they use, the pain in their words, the objection, and the next step and date. Then update the account row in `leads/accounts.csv` and run `python3 gtm/tools/build.py`.
