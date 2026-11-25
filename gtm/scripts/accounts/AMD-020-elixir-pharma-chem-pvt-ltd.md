# AMD-020 · Elixir Pharma Chem Pvt Ltd: call script

**Call:** +91 79 2281 1986 ; +91 97123 78624
**Ask for:** Bipin Patel (Chairman); Daleep Malhotra (Executive Director BD) [LinkedIn]
**Language:** Gujarati first (Gujarati section below), then mirror them. If they answer in Hindi, use the Hinglish lines.
**Status:** Researched · next: Call board line, ask for Bipin Patel
**What we know (from their website):** API and intermediates. Plot No. 164, Phase II, Opp. Lathia Industries, GIDC Naroda, Ahmedabad 382330. Hiring 20 chemists (10 production, 5 R&D, 4 QC); three new APIs in development; WHO-GMP and EU-GMP claimed
**Fit:** score 60, tier B. Odoo (multi-company/multi-currency or pharma QC + lots)
**Goal of the call:** leave with one of: a visit date at the Naroda plant, the right person's name and a good time, one real fact about how they run today, or a callback date. Do not sell on the phone.

Source: https://www.elixirpharma.in/career.html. Check the person's current role on LinkedIn or the site before calling. How to run the conversation: `scripts/00-call-playbook.md`.

---

## 1. Open the call (15 seconds)

**If reception answers** (playbook branch A): get the name, the best time and a direct number.

> **Dhaval:** Namaste, main Dhaval, Brilworks se, Ahmedabad. Ek chhoti si help chahiye thi. Aapke yahan operations aur accounts ka software ya system kaun dekhta hai? Bipin ji, Daleep ji, ya koi aur?
>
> **If "sir abhi nahi hain":** Koi baat nahi. Woh usually kab milte hain, subah ya shaam? Aur unka extension ya direct number mil sakta hai?
>
> **If "mail kar dijiye":** Zaroor. Kis naam se bhejun, aur unka email kya hai? Mail ke baad Thursday ko call karun toh baat ho jayegi?

*Ask the receptionist's name and use it next time.*

**When you reach Bipin ji:**

> **Dhaval:** Namaste Bipin ji, main Dhaval, Brilworks se, Ahmedabad. Seedha bolun toh yeh ek cold call hai. 30 second de sakte hain? Phir aap batana baat karni hai ya nahi.
>
> **If yes:** Main aapki website dekh raha tha. Aap lagbhag 20 chemists hire kar rahe hain, aur teen nayi APIs develop kar rahe hain. Hum manufacturers ke saath ERP ka kaam karte hain, Odoo aur ERPNext. Toh ek cheez samajhni thi: abhi stock aur accounts ke liye kya use karte hain, Tally ya koi ERP?

*Their answer picks the branch in section 3. Stop talking and listen.*

## 2. Questions to have ready (ask one, then follow their answer)

Pick the next question from what they just said, not from the list order.

- **Easy, about their setup:** "Naroda plant mein abhi kitne reactors aur kitni production team hai?"
- **The pain question:** "Batch records aur QC release abhi paper par hain ya kisi system mein, jab production staff badh raha hai?"
- **Another angle:** "API ka costing solvent recovery aur yield ke saath kaise nikalte hain?"
- **Dig deeper:** "Naye chemists aane ke baad batch record ka format badla hai?"
- **Dig deeper:** "Solvent recovery ka hisaab kaun rakhta hai?"
- **Who feels it:** "Yeh sabse zyada kisko pareshan karta hai, accounts ko, plant ko, ya aapko?"
- **The last time:** "Last time yeh hua tha, toh kya hua? Kitna time laga?"

*Echo their last few words when they go vague ("Thoda manual?"). Don't ask about revenue or margins on the first call.*

## 3. What they say, what you say

| They say | Dhaval says |
|---|---|
| "Busy hoon." | "Bilkul. Ek line mein bataun kyon call kiya: Aap lagbhag 20 chemists hire kar rahe hain, aur teen nayi APIs develop kar rahe hain. Isliye ek sawaal tha. Kal 11 baje ya shaam 5 ke baad, kya theek rahega?" |
| "Email bhej do." | "Zaroor. Taaki generic mail na ho: aapke liye zyada important kya hai, batch records aur QC release ya API costing with yield aur solvent recovery? ... Aur mail ke baad Friday ko 2 minute call kar lun?" Confirm the address letter by letter. |
| "Tally aur Excel pe chal raha hai." | "Tally accounts ke liye best hai, woh chalu rahega. Excel mein sabse badi sheet kaunsi hai? ... Batch records aur QC release abhi paper par hain ya kisi system mein, jab production staff badh raha hai?" |
| "Humare paas ERP hai." | "Achha, kaunsa? Kab se chal raha hai? Ise kaun own karta hai?" Then: "Batch records aur QC release us ERP mein hain, ya paper pe?" Get a follow-up date (playbook branch E). |
| "Abhi naya ERP liya hai." | "Congratulations. Kaunsa, aur partner kaun hai? Go-live kab ka target hai? Pehle phase mein kya aa raha hai?" Exit: "Go-live ke 2-3 mahine baad ek baar call karun?" |
| "Zaroorat nahi hai." | "Fair hai. Ek cheez pooch sakta hoon: kya isliye ki sab already system mein hai, ya abhi priority kuch aur hai?" (playbook branch F) |
| Wrong person (IT, accounts staff) | "Aap hi sahi insaan ho yeh samajhne ke liye. Abhi kya system hai? ... Iska decision usually kaun leta hai?" Ask for an introduction. |
| "Kitna kharcha hoga?" | "Phase 1 (stock, purchase, sales, accounts) ₹2 lakh se shuru hota hai. Exact quote aapka setup dekh ke dunga. Isliye milna zaroori hai." |
| "Pehle bhi ERP try kiya, kaam nahi kiya." | "Kya hua tha? ... Hum phase mein go-live karte hain, ek saath sab nahi badalte." |
| "Aapke clients kaun hain Ahmedabad mein?" | "MP mein humne ek building-materials manufacturer ka ERP banaya hai. Ahmedabad mein is saal pehle 2-3 manufacturers ke saath reference terms pe shuru kar rahe hain." (Never name the client. Don't claim local clients.) |
| Clear no, "dobara call mat karna" | "Bilkul, sorry for disturbing. Thank you." Set status to `Do not contact`. |

## 4. When you hear the pain

Ask one more question about it first. Then reflect it back:

> **Dhaval:** Toh batch records aur API costing abhi manual hain, aur team doubling ke saath yeh sambhalna mushkil hoga. Sahi samjha?

One line of value, then the visit ask:

> **Dhaval:** Hum yahi karte hain. Ek ERP mein batch records, QC release aur API costing yield aur solvent recovery ke saath ek jagah, GMP audit trail ke saath. Tally accounts ke liye reh sakta hai. Kya main next week Naroda plant aa ke 30 minute dikha sakta hoon ki aapke setup mein yeh kaisa dikhega? Tuesday ya Thursday?

*When they agree:* "Main WhatsApp pe confirm bhejta hoon. Yeh number sahi hai?"

## 5. Leave with a next step

Never end with "main contact karta hoon". End with a date, a name or a number, and thank them by name:

> **Dhaval:** Bahut shukriya Bipin ji, aapka time dene ke liye. Toh main [day] ko [time] call karta hoon.

## Gujarati lines

> નમસ્તે, હું ધવલ બોલું છું, Brilworks માંથી, Ahmedabad. તમારે ત્યાં operations અને accounts નું software કોણ જુએ છે? Bipinજી, Daleepજી?
>
> નમસ્તે Bipinજી, હું ધવલ, Brilworks માંથી, Ahmedabad. બે મિનિટ વાત થઈ શકે?
>
> અમે Odoo અને ERPNext ના partner છીએ. Manufacturers માટે stock, production, sales અને accounts એક system માં લાવીએ છીએ. હું તમારી website જોઈ રહ્યો હતો. મેં જોયું કે તમે લગભગ 20 chemist hire કરી રહ્યા છો અને ત્રણ નવી API develop કરો છો.
>
> અત્યારે stock અને accounts માટે શું વાપરો છો, Tally કે કોઈ ERP?
>
> Production staff વધે છે ત્યારે batch records અને QC release અત્યારે કાગળ પર છે કે કોઈ system માં?
>
> આવતા અઠવાડિયે Naroda plant પર 30 મિનિટ મળવા આવી શકું? મંગળવાર કે ગુરુવાર, શું ફાવશે?

## English lines

> Hi Bipin, this is Dhaval from Brilworks in Ahmedabad. To be upfront, this is a cold call. Can I take 30 seconds, and then you tell me if it's worth continuing?
>
> I was looking at your website. I saw that you're hiring about 20 chemists and developing three new APIs. We're Odoo and ERPNext partners, so I wanted to ask: what do you use for stock and accounts today, Tally or an ERP?
>
> As production staff grows, are batch records and QC release on paper today, or in a system?
>
> Could I come by the Naroda plant for 30 minutes next week? Would Tuesday or Thursday suit you better?

## Questions they will probably ask

- **Pharma: batch, expiry, FEFO, QC release?** Yes: lot and serial tracking with expiry dates, FEFO picking, quality checks before release, and quarantine stock. QC module availability differs by product and edition [verify for Odoo: Quality is an Enterprise app].
- **Will it pass audits? (pharma: GMP, chemicals: REACH, BRC and similar)** The system keeps a full audit trail of who changed what and when, plus lot and batch traceability from raw material to dispatch. It supports your compliance work, but certification is still your process. In pharma, say: "Batch records and QC release can be tracked in the system; we'll map it to your SOPs in discovery."
- **How much of our team's time does it need?** One owner-side decision maker for an hour a week, one key user per department for a few hours a week during setup, and full-day training sessions before go-live.

Full answers are in `scripts/01-buyer-faq.md`. Fill the [fill] items there before calling.

## What to show them on the visit

1. Batch records and QC release as production staff doubles
2. API costing including solvent recovery and yield
3. WHO-GMP and EU-GMP audit trail

## Email draft (not sent; send only after approval)

**Subject:** Elixir Pharma Chem Pvt Ltd: as production staff grows, are batch records and qc release 

Hi Bipin,

I was looking at your website. I saw that you're hiring about 20 chemists and developing three new APIs.

As production staff grows, are batch records and QC release on paper today, or in a system? In plants like yours this often ends up split across Tally, Excel and WhatsApp, and the owner sees the real numbers late.

I'm Dhaval from Brilworks, an Odoo and ERPNext partner in Ahmedabad. We put stock, production, sales and accounts in one system, starting with a fixed-scope first phase. Tally can stay for accounts and GST while you move.

Could I come by the Naroda plant for 30 minutes next week?

Dhaval
Brilworks | Odoo and ERPNext partner
[Phone]

If this isn't relevant, just reply "no thanks" and I won't follow up.

**Follow-up, day 4 (same thread):** One quick win we usually start with: getting stock and batch movements into one place before touching production planning. Happy to show what that would look like for Elixir Pharma Chem Pvt Ltd.

**Follow-up, day 10 (same thread):** I'll leave this here. If useful, I can send a one-page sketch of how your stock, production and accounts would sit in one system. Just reply "send it".

## WhatsApp after the call (send only after approval)

> Bipinજી, આજે વાત કરવા બદલ આભાર. ધવલ, Brilworks. આપણે વાત કરી તેમ [visit date] એ Naroda plant પર 30 મિનિટ મળીએ. Confirm કરશો?

## Visit checklist

- Bring: one-page Odoo/ERPNext overview, the MP building-materials case (anonymised), a phase 1 price range.
- Ask to see: the stock register, a costing sheet, and how a purchase order is approved.
- Leave with: the main pain in their words, who else decides, and a date for a demo or a proposal.

## After the call (2 minutes)

Log in `gtm/logs/calls.csv` with an `outcome` code from the playbook: who you spoke to, their role, language used, what system they use, the pain in their words, the objection, and the next step and date. Then update the account row in `leads/accounts.csv` and run `python3 gtm/tools/build.py`.
