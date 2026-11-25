# v3 conversational fields for the first 27 accounts, used by script_v3.py on top of the v2 fields in v2_27.py.
#
# email_ab: two topics to offer when they say "send me an email" (playbook branch D). Hinglish, short.
# dig:      follow-up questions to ask after their first answer (playbook move "ask the second question").
# erp_q:    what to ask if they say they already have an ERP (playbook branch E), specific to this account.
# plan:     only for accounts called in round 1 (Nov 2026). What we learned, the next touch, the angle and the opener.
#           "assumed" lists anything we inferred from the call notes and must confirm on the next call.
#
# Facts here come from the company's own website (see v2_27.py and accounts.csv) or from the caller's notes.
# Nothing else is assumed about the companies; inferences are flagged in "assumed".

V3 = {
 "Mediwin Pharmaceuticals": dict(
   email_ab=("dono plants ka batch aur expiry stock", "export registrations ka tracking"),
   dig=["Near-expiry stock ka pata kab chalta hai, dispatch se pehle ya month-end pe?",
        "Naye countries add karte waqt registration ka kaam kaun sambhalta hai, regulatory team ya export team?"],
   erp_q="Woh ERP dono plants aur export registrations dono sambhalta hai, ya registrations abhi bhi Excel mein hain?",
   plan=dict(
     learned="Kathan Patel was not available. Whoever answered asked us to email him.",
     next="Send the follow-up email to Kathan Patel (after approval), then call on Tue 1 Dec to ask whether it was useful.",
     angle="Batch and expiry across Naroda and Sari, and export registrations on the way to 50 countries.",
     opener_hi="Namaste Kathan ji, Dhaval, Brilworks se. Pichhli baar call kiya tha, aapke office ne mail karne ko kaha tha, maine batch aur expiry wala mail bheja tha. Do minute mein bataun kyon?",
     opener_en="Hi Kathan, Dhaval from Brilworks. I called recently and your office asked me to email you, so I sent a short note on batch and expiry tracking across your two plants. Can I take two minutes on why?",
     assumed=["We don't know who took the call or which email address they meant. Confirm the address before sending; use info@mediwinpharma.com marked for Kathan Patel only if no direct address is available."])),
 "Gopani Product Systems / Gopani Filters Pvt Ltd": dict(
   email_ab=("group companies ka consolidated hisaab", "regional sales team ka enquiry tracking"),
   dig=["Uniexcel aane ke baad uski books aur stock alag chal rahe hain ya merge ho gaye?",
        "Naye regional managers ka target aur pipeline aap kahan dekhte hain?"],
   erp_q="Microsoft mein saari group companies ek saath ja rahi hain, ya pehle sirf Gopani Filters?",
   plan=dict(
     learned="They signed up for Microsoft last month.",
     next="Nurture. Call around 24 Feb 2027, roughly three months after sign-up, to ask how the rollout is going.",
     angle="Be the name they remember for the gaps a first phase leaves: CRM for the regional sales team, inter-company billing, production or plant reporting. Ask, don't assert.",
     opener_hi="Namaste Pathik ji, Dhaval, Brilworks se. November mein baat hui thi, aapne bataya tha Microsoft le liya hai. Bas yeh poochne ke liye call kiya ki rollout kaisa chal raha hai?",
     opener_en="Hi Pathik, Dhaval from Brilworks. We spoke in November when you'd just signed with Microsoft. I'm calling to ask how the rollout is going.",
     ask=["Kaunsa product hai, Business Central ya kuch aur? Partner kaun hai?",
          "Go-live ho gaya, ya kab ka target hai?",
          "Pehle phase mein kya aaya, aur kya baad ke liye rakha hai? Sales CRM aur regional pipeline bhi usi mein hai?",
          "Saari group companies, Uniexcel bhi, usi mein hain?"],
     assumed=["'Microsoft' most likely means Microsoft Dynamics 365 (Business Central or similar). The product, the partner and the person we spoke to are not recorded. Confirm on the next call."])),
 "Rohan Dyes & Intermediates Ltd": dict(
   email_ab=("teeno plants ka stock transfer", "plant-wise yield aur by-product costing"),
   dig=["Inter-plant transfer ka mismatch kaun theek karta hai, plant ka store ya HO accounts?",
        "Nayi sulfuryl chloride line ke liye costing ka format ab tak decide hua hai?"],
   erp_q="Woh ERP teeno plants mein chal raha hai, ya Dahej aur Khambhat ka alag system hai?",
   plan=dict(
     learned="Asked us to send an email.",
     next="Send the follow-up email (after approval), then call on Tue 1 Dec.",
     angle="Inter-plant stock transfers across Vatva, Khambhat and Dahej, and per-plant yield costing as the new line comes in.",
     opener_hi="Namaste Rohan ji, Dhaval, Brilworks se. Pichhli baar baat hui thi, maine teeno plants ke stock transfer ke baare mein mail bheja tha. Mil gaya tha?",
     opener_en="Hi Rohan, Dhaval from Brilworks. We spoke recently and I sent a short email on stock transfers between your three plants. Did it reach you?",
     assumed=["Who asked for the email and which address they gave are not recorded. Confirm before sending; info@rohanchemicals.com marked for Rohan Jindal is the fallback.",
              "The script opens in Hindi because the registered office is outside Gujarat. Use whatever language was used on the first call."])),
 "Ishan Dyes and Chemicals Ltd": dict(
   email_ab=("unit-wise P&L", "quarterly close aur audit trail"),
   dig=["Quarterly results ke liye numbers kaun jodta hai, aur kitne din pehle shuru karte hain?",
        "Pigment aur sulphur ka common cost, jaise power aur ETP, kaise baantte hain?"],
   erp_q="Listed company hone ke naate audit trail ke liye koi ERP hai, ya Tally ke saath Excel?",
   plan=dict(
     learned="The number we called was not in service.",
     next="Find a working number before calling again (see playbook branch H).",
     angle="Unchanged: unit-wise P&L and quarterly close.",
     ask=["Try the second listed board number (+91 79 2589 3607) if the first one failed, then the other way round.",
          "Check the Google Maps listing and the website contact page for a newer number.",
          "As a listed company, its annual report and stock-exchange filings should list a registered office phone and a company secretary or investor email. Use those to ask for the right contact.",
          "Look up Shrinal Patel (Executive Director) on LinkedIn."],
     assumed=["The call notes don't say which listed number was dead."])),
 "Ushanti Colour Chem Ltd": dict(
   email_ab=("Vatva, Saykha aur subsidiary ka consolidation", "batch shade records"),
   dig=["Consolidation ka kaam aapke yahan hota hai ya CA firm karti hai?",
        "Shade complaint aane par batch ka record dhoondhne mein kitna time lagta hai?"],
   erp_q="Woh system Saykha plant aur subsidiary dono mein hai, ya sirf Vatva mein?",
   plan=dict(
     learned="The number we called was not in service.",
     next="Find a working number before calling again (see playbook branch H).",
     angle="Unchanged: consolidation across Vatva, Saykha and the subsidiary.",
     ask=["Try the other listed board number (+91 79 2589 4903 or 2583 3315).",
          "Check the Google Maps listing and the website contact page for a newer number.",
          "As a listed company, its annual report and stock-exchange filings should list a registered office phone and a company secretary or investor email.",
          "marketing@ushanti.com is published on the site and could ask for the right number, but only send after approval."],
     assumed=["The call notes don't say which listed number was dead."])),
 "Anar Chemicals LLP": dict(
   email_ab=("multi-currency purchase", "EcoVadis aur AEO ka data"),
   dig=["US division ka purchase bhi usi system mein jaata hai, ya alag?",
        "EcoVadis renewal ke liye data jodne mein kitne din lagte hain, aur kaun karta hai?"],
   erp_q="Woh ERP kisne lagaya tha, aur ab bhi wahi vendor support deta hai? 2024 mein US division aaya toh woh bhi usi mein add hua?",
   plan=dict(
     learned="They have used an ERP for 7 to 8 years. The person we spoke to didn't know its name.",
     next="Call on Wed 2 Dec to reach the ERP owner, most likely Piyush Suthar (Manager Finance & Accounts) or Kalpesh Sura (GM Operations). Goal: the ERP's name, who supports it, and what still happens outside it.",
     angle="Long-running ERP (playbook branch E2): what still lives in Excel, how the 2024 US procurement division fits, vendor support, and compliance data for EcoVadis and AEO.",
     opener_hi="Namaste Piyush ji, Dhaval, Brilworks se. Aapke office se pata chala ki aap 7-8 saal se ek ERP use kar rahe ho. Main samajhna chahta tha, woh kaunsa hai aur kaisa chal raha hai? Do minute?",
     opener_en="Hi Piyush, Dhaval from Brilworks. Your office mentioned you've run an ERP for seven or eight years. I'd like to understand which one it is and how it's working for you. Do you have two minutes?",
     ask=["Kaunsa ERP hai, aur kisne implement kiya tha?",
          "Ab bhi koi report hai jo har mahine Excel mein bahar nikaal ke banti hai?",
          "US procurement division ka dollar purchase usi system mein hai?",
          "Agla upgrade ya renewal kab hai?"],
     assumed=["We don't know who we spoke to. Piyush Suthar and Kalpesh Sura are named on the company site; their ownership of the ERP is a guess."])),
 "Crystal Quinone Pvt Ltd": dict(
   email_ab=("paanch units aur Antwerp ka stock", "BRC aur FAMIQS ke liye lot traceability"),
   dig=["Antwerp ka stock India se kaise dikhta hai, unka alag system hai?",
        "Naye Saykha plant ke liye system pehle din se tha, ya baad mein jodna pada?"],
   erp_q="Microsoft mein Antwerp ka stock aur lot traceability bhi aa raha hai, ya pehle sirf India ke units?",
   plan=dict(
     learned="They have just started on Microsoft.",
     next="Nurture. Call around 24 Feb 2027 to ask how the rollout is going.",
     angle="First-phase gaps across five units and Antwerp: lot traceability for BRC and FAMIQS audits, plant-level stock, production costing. Ask, don't assert.",
     opener_hi="Namaste Anang ji, Dhaval, Brilworks se. November mein baat hui thi, aapne Microsoft shuru kiya tha. Bas yeh poochne ke liye call kiya ki kaisa chal raha hai, paanchon units mein live ho gaya?",
     opener_en="Hi Anang, Dhaval from Brilworks. We spoke in November when you'd just started on Microsoft. I'm calling to ask how it's going and whether all five units are live.",
     ask=["Kaunsa product hai, Business Central ya kuch aur? Partner kaun hai?",
          "Saare units aur Antwerp ek saath, ya phase mein?",
          "Audit ke liye lot traceability usi mein aa gayi?",
          "Production costing aur QC bhi pehle phase mein hai?"],
     assumed=["'Just started Microsoft practice' most likely means they have started implementing Microsoft Dynamics 365. It could also mean something else, such as Microsoft 365. Confirm on the next call.",
              "We don't know whom we spoke to; the site names Anang Shah and Aniket Shah as promoters."])),
 "Verito Engineering Pvt Ltd": dict(
   email_ab=("enquiry se quote aur BOM ka flow", "actual job costing"),
   dig=["Quote banate waqt BOM kaun banata hai, design team ya sales?",
        "Regional offices order status ke liye kisko call karte hain?"],
   erp_q="Woh ERP quote aur BOM bhi sambhalta hai, ya sirf accounts aur stock?",
   plan=dict(
     learned="Call did not connect.",
     next="Retry Thu 26 Nov at a different time of day (try 15:30 or after 18:00). Up to 3 attempts in 7 days, then email or LinkedIn.",
     angle="Unchanged: enquiry to quote to BOM to job cost.")),
 "YCUBE Engineered Solutions Pvt Ltd": dict(
   email_ab=("sales offices ka live stock", "UAE aur Thailand entities ka hisaab"),
   dig=["Quote mein delivery date dene se pehle sales office kisse confirm karta hai?",
        "Overseas entities ka month-end kaun close karta hai, yahan se ya wahan?"],
   erp_q="Woh ERP India aur overseas entities dono mein hai, ya sirf India?",
   plan=dict(
     learned="Call did not connect.",
     next="Retry Thu 26 Nov at a different time of day. Up to 3 attempts in 7 days, then email or LinkedIn.",
     angle="Unchanged: live stock for the sales offices, and India plus overseas entities.")),
 "Cair Euromatic Automation Pvt Ltd": dict(
   email_ab=("QC inspection records", "GeM tender aur order status"),
   dig=["Third-party inspection ke liye documents kaun ready karta hai?",
        "Naye QC inspectors aane ke baad records ka format badlega?"],
   erp_q="QC aur tender documents bhi us ERP mein hain, ya alag files mein?",
   plan=dict(
     learned="The person was busy and declined to listen.",
     next="One more attempt on Mon 7 Dec at a different time, opening with the one-line reason (playbook branch C). If that fails, an email to Atique Kothawala on the QC hiring angle (after approval), then stop.",
     angle="They are hiring three QC inspectors, a QMS compliance executive and a GeM tender executive: QC records and tender tracking.",
     opener_hi="Namaste Atique ji, Dhaval, Brilworks se. Pichhli baar aap busy the, isliye ek line mein bataata hoon: aap teen QC inspectors hire kar rahe ho, toh QC records ke baare mein ek sawaal tha. 30 second?",
     opener_en="Hi Atique, Dhaval from Brilworks. You were busy last time, so in one line: I saw you're hiring three QC inspectors, and I had one question about how QC records are kept. Thirty seconds?",
     assumed=["We don't know whether the person was Atique Kothawala or someone else. If they gave a clear 'no', change the status to Do not contact and stop."])),
 "JEE Pumps Ltd": dict(
   email_ab=("pump model ka actual cost, foundry se assembly tak", "teeno campus ka stock aur work orders"),
   dig=["Excel mein sabse badi sheet kaunsi hai, costing ya production planning?",
        "Foundry ka casting weight aur rejection kahan record hota hai?"],
   erp_q="Tally ke saath koi production software bhi hai, ya baaki sab Excel mein?",
   plan=dict(
     learned="They run Tally and Excel. The contact will connect us to Niyati on their team.",
     next="Call back on Fri 27 Nov to get Niyati's role and direct number, or to be put through. This is the warmest lead from round 1.",
     angle="Tally plus Excel (playbook branch E4): actual cost per pump model from foundry through machining and assembly, and stock across three campuses.",
     opener_hi="Namaste, Dhaval, Brilworks se. Pichhli baar baat hui thi, aapne kaha tha Niyati ji se connect karenge. Kya unse baat ho sakti hai, ya unka number mil sakta hai?",
     opener_en="Hi, this is Dhaval from Brilworks. We spoke recently and you said you'd connect me with Niyati. Could I speak with Niyati now, or could I have the direct number?",
     ask=["(to Niyati) Aap accounts side dekhte hain ya production planning?",
          "Tally mein kya hai aur Excel mein kya? Sabse badi Excel sheet kaunsi hai?",
          "Ek pump model ka actual cost abhi kaise nikalte hain?",
          "Prakash sir ke alawa yeh decision aur kaun leta hai?"],
     assumed=["Niyati's surname and role are not recorded. Ask, and don't assume which department.",
              "We don't know who we spoke to on the first call."])),
 "Vasa Pharmachem Pvt Ltd": dict(
   email_ab=("plant se customer tak lot traceability", "domestic aur export desk ka live stock"),
   dig=["FSSC 22000 audit mein lot trace karne ke liye data kahan se aata hai?",
        "Dholka aur Behrampura ka production plan kaun banata hai, aur kis mein?"],
   erp_q="Zoho mein production bhi hai, matlab BOM, batch aur QC? Ya woh register aur Excel mein?",
   plan=dict(
     learned="They use Zoho for accounting, stock and HR.",
     next="Nurture. Call around 20 Jan 2027 with the production angle.",
     angle="Zoho covers accounting, stock and HR. Ask whether production (BOM, batches, QC) and lot traceability for FSSC 22000 sit in Zoho or in registers and Excel (playbook branch E3). Don't claim what Zoho can or can't do.",
     opener_hi="Namaste, Dhaval, Brilworks se. November mein baat hui thi, aapne bataya tha accounts, stock aur HR Zoho mein hai. Ek cheez poochni thi: production aur batch records bhi Zoho mein hain, ya woh alag?",
     opener_en="Hi, Dhaval from Brilworks. When we spoke in November you mentioned Zoho runs your accounts, stock and HR. One question: are production and batch records in Zoho too, or kept separately?",
     ask=["Zoho Books aur Inventory, ya Zoho One?",
          "Production aur QC kis mein hota hai?",
          "FSSC audit mein ek lot plant se customer tak kaise trace karte hain?"],
     assumed=["Which Zoho products they use, and whom we spoke to, are not recorded. Dr. Jaimin Vasa is named on the site as Chairman and MD."])),
 "Molkem": dict(
   email_ab=("chaaron countries ka consolidated view", "purchase approvals"),
   dig=["Brazil aur Vietnam ki books yahan se dikhti hain, ya local accountant bhejta hai?",
        "Purchase approval abhi kaun deta hai, aur kitne level hain?"],
   erp_q="Woh ERP saari subsidiaries mein hai, ya sirf India?",
   plan=dict(
     learned="Call did not connect.",
     next="Retry Thu 26 Nov at a different time of day. Up to 3 attempts in 7 days, then email or LinkedIn.",
     angle="Unchanged: consolidated view across four countries, purchase approvals.")),
 "APDM Pharmaceuticals Pvt Ltd": dict(
   email_ab=("batch records aur QC release", "CDMO client-wise costing"),
   dig=["US aur UK audit ke liye abhi kaunsa system validate kiya hai?",
        "Naye plant ke liye systems ka decision kisne liya tha, IT ya QA?"],
   erp_q="Naye plant ke saath ERP bhi naya liya, ya pehle wala hi extend kiya?",
   plan=dict(
     learned="Sanket from the IT team said it is not required.",
     next="Nurture. Don't call IT again. Around Wed 9 Dec, reach Shashank Patel (COO) through LinkedIn or email (after approval) with the audit angle. If he also says no, stop.",
     angle="Plant commissioned in 2025 and two ANDAs acquired: batch records, QC release and CDMO client-wise costing ahead of US and UK audits. The owner of that problem is operations or QA, not IT.",
     opener_hi="Namaste Shashank ji, Dhaval, Brilworks se. Naye plant aur US-UK audits ke baare mein ek sawaal tha: batch records aur QC release abhi kis system mein ho raha hai?",
     opener_en="Hi Shashank, Dhaval from Brilworks. I had one question about your new plant and the US and UK audits: which system holds batch records and QC release today?",
     assumed=["'Not required' came from IT and may mean they already have a system. We don't know which. Ask before pitching."])),
 "Indo-Air Compressors Pvt Ltd": dict(
   email_ab=("installed compressors ka AMC aur service history", "regional engineers ki visit reports"),
   dig=["AMC renewal ka reminder kaun deta hai, aur kaise?",
        "Spares ka stock regional engineers ke paas bhi rehta hai?"],
   erp_q="Service aur AMC bhi us ERP mein hai, ya alag software ya Excel?"),
 "Techflow Enterprises Pvt Ltd": dict(
   email_ab=("har order ka project cost", "milestone billing aur payment follow-up"),
   dig=["Order khatam hone ke baad actual cost estimate se compare hota hai?",
        "Export orders ka hisaab domestic se alag rakhte hain?"],
   erp_q="Project costing aur milestone billing bhi usi ERP mein hai?"),
 "PressureJet Systems Pvt Ltd": dict(
   email_ab=("har pump ka spares aur service history", "Thaltej aur Pirana ka stock sync"),
   dig=["Customer spares ke liye call kare toh model aur serial number kaise dhoondhte hain?",
        "Export orders ke documents kaun banata hai?"],
   erp_q="Sales, spares aur service teeno desk us ERP mein hain?"),
 "Ecosafe Agriscience India Pvt Ltd": dict(
   email_ab=("dealer schemes aur credit", "season se pehle stock planning"),
   dig=["Season ke end mein dealer ke paas bacha stock kaise wapas track hota hai?",
        "Scheme ka calculation kaun karta hai, aur kis mein?"],
   erp_q="Dealer schemes aur credit limit bhi us system mein hain?"),
 "Hindprakash Chemicals Pvt Ltd": dict(
   email_ab=("India aur overseas companies ka consolidation", "trading vs manufacturing margin"),
   dig=["Overseas companies ka month-end kitne din mein yahan aata hai?",
        "Trading ka maal aur apna maal ek hi godown mein rehta hai?"],
   erp_q="Overseas companies bhi us ERP mein hain, ya sirf India?"),
 "Elixir Pharma Chem Pvt Ltd": dict(
   email_ab=("batch records aur QC release", "API costing with yield aur solvent recovery"),
   dig=["Naye chemists aane ke baad batch record ka format badla hai?",
        "Solvent recovery ka hisaab kaun rakhta hai?"],
   erp_q="Batch records aur QC release us ERP mein hain, ya paper pe?"),
 "MBH Pumps (Gujarat) Pvt Ltd": dict(
   email_ab=("export enquiry se dispatch tak", "spares aur service desk"),
   dig=["Export quote banane mein kitna time lagta hai, aur kaun banata hai?",
        "Dealer ka credit limit cross ho toh kaun rokta hai?"],
   erp_q="Export documents aur service desk bhi us ERP mein hain?"),
 "HOF Pharmaceuticals Ltd": dict(
   email_ab=("audit ke liye batch history", "21 markets ke registrations aur near-expiry stock"),
   dig=["EU-GMP ke liye systems mein kya badalna padega, yeh discussion hua hai?",
        "Near-expiry stock ka pata kab chalta hai?"],
   erp_q="Woh ERP EU-GMP ki tayyari mein bhi kaam aayega, ya usmein badlav chahiye?"),
 "Alps Chemicals Pvt Ltd": dict(
   email_ab=("export invoice, packing list aur COA", "multi-currency receivables"),
   dig=["Ek shipment ke documents banane mein kitna time lagta hai?",
        "Shade complaint aaye toh lot ka record kahan se nikalte hain?"],
   erp_q="Export documents aur COA bhi us ERP se nikalte hain?"),
 "Airmax Pneumatics Ltd": dict(
   email_ab=("PSU tender aur order status", "order-wise actual cost"),
   dig=["Tender ke documents kaun ready karta hai, aur kitne din pehle?",
        "PSU payment follow-up kaun karta hai?"],
   erp_q="Tender tracking aur order costing us ERP mein hai?"),
 "Fluid Logic Systems Pvt Ltd (Systems Group)": dict(
   email_ab=("har project ka BOM aur bought-out parts", "actual vs estimated job cost"),
   dig=["Bought-out part late aaye toh delivery date kaun update karta hai?",
        "Design change hone par BOM kaise update hota hai?"],
   erp_q="Project-wise BOM aur job costing us ERP mein hai?"),
 "Leistung Engineering Pvt Ltd": dict(
   email_ab=("MTC aur heat number traceability", "customer documentation pack"),
   dig=["Documentation pack kaun banata hai, QA ya project team?",
        "Kabhi kisi job ka MTC dhoondhne mein dikkat hui hai?"],
   erp_q="MTC aur heat numbers us ERP mein job se jude hain?"),
 "Mahavir Industries (Mahavir Pigments)": dict(
   email_ab=("export documents aur REACH-GOTS paperwork", "batch aur customer-wise records"),
   dig=["Ek shipment ke documents mein kitna time lagta hai?",
        "REACH ya GOTS ka data kaun maintain karta hai?"],
   erp_q="Export aur compliance documents us ERP se bante hain?"),
}
