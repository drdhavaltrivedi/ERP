# Source data for the Ahmedabad account list. Rebuild xlsx with build_xlsx.py.
# Headcount band is from Apollo's 51-200 filter unless noted. All other fields from company websites fetched 13 Nov 2026.
A = []
def add(**k): A.append(k)

add(company="HOF Pharmaceuticals Ltd", industry="Pharma", sub="Formulations (tablets, capsules, oral liquids), exporter", hc="51-200 (Apollo)",
    address="Survey No. 211-4/5/6, Village Pipan, Sanand-Bavla Road, Sanand, Ahmedabad 382110", cluster="Sanand / Bavla",
    website="hofpharma.com", phone="+91 63535 34530", email_generic="info@hofpharma.com",
    dm="Abhigna Patel (CEO); Darshan Dhanani (COO); Pravin Patel (Chairman, HOF Group); Mansukh Dhanani (Director Ops & Technology)",
    signal="WHO-GMP plant exporting to 21 countries; site says it is targeting PIC/S and EU-GMP approvals (needs batch traceability, QC, audit trail)",
    multi_loc=False, rank=1, src="https://hofpharma.com/ ; /contact-us/ ; /about-us/")
add(company="APDM Pharmaceuticals Pvt Ltd", industry="Pharma", sub="CDMO, oral solids (4 bn pills/yr capacity)", hc="51-200 (Apollo)",
    address="403 Patron, 4th Floor, Opp Epic Hospital, Rajpath Rangoli Road, Bodakdev, Ahmedabad 380054 (plant near Ahmedabad, address not published)", cluster="SG Highway / Bodakdev (office)",
    website="apdmpharma.com", phone="+91 2717 651000 ; +91 79 4603 2554", email_generic="info@apdmpharma.com ; bd@apdmpharma.com",
    dm="Jayanta Kumar Mandal (CEO & MD); Shashank Patel (COO)",
    signal="New plant commissioned Q1 2025, acquired two ANDAs Q1 2025, targets US/UK/EU. Young company likely still on starter systems",
    multi_loc=True, rank=1, src="https://apdmpharma.com/about/")
add(company="Mediwin Pharmaceuticals", industry="Pharma", sub="Formulations, nutraceuticals, cosmetics; exporter", hc="51-200 (Apollo)",
    address="203 Anmol Business Centre, Near Navrang School Six Roads, Navrangpura, Ahmedabad 380009. Plants: 128/A Phase 1&2 GIDC Naroda 382330; Plot 28 Gujarat Pharma Techno Park, Sari, Sarkhej-Bavla Rd 382220", cluster="Naroda / Changodar-Sari",
    website="mediwinpharma.com", phone="+91 79 2640 5517 ; +91 98244 48575 ; WhatsApp +91 76005 35517", email_generic="info@mediwinpharma.com",
    dm="Kathan Patel (Director, Business Strategy & Execution); Bhavin Patel (Director); Harshal Patel (Director)",
    signal="2 plants + corporate office; 225 products to 20 countries, target 350 products in 50 countries by 2030; hiring production chemist and export marketing. Second-generation directors",
    multi_loc=True, rank=1, src="https://mediwinpharma.com/about-us/ ; /career/")
add(company="Vasa Pharmachem Pvt Ltd", industry="Pharma / Chemicals", sub="Mineral salts and excipients (pharma, food, nutra)", hc="51-200 (Apollo)",
    address="R.V. Vasa House, 88 Pankaj Society, Bhattha, Paldi, Ahmedabad 380007. Units: 11 GIDC Behrampura; Survey 1354 Bhetawada, Trasad Rd, Dholka", cluster="Paldi / Behrampura / Dholka",
    website="vasapharmachem.com", phone="+91 79 2660 8012/13/14 ; +91 80002 78789 (domestic) ; +91 80003 06011 (export)", email_generic="mktgdom@vasapharmachem.com ; exports@vasapharmachem.com",
    dm="Dr. Jaimin Vasa (Chairman & MD)",
    signal="2 plants + central warehouse; exports to 50+ countries; FSSC 22000 / ICH Q7 claims need lot traceability",
    multi_loc=True, rank=1, src="https://vasapharmachem.com/about-us/ ; /contact-us/")
add(company="Elixir Pharma Chem Pvt Ltd", industry="Pharma", sub="API and intermediates", hc="51-200 (Apollo)",
    address="Plot No. 164, Phase II, Opp. Lathia Industries, GIDC Naroda, Ahmedabad 382330", cluster="Naroda",
    website="elixirpharma.in", phone="+91 79 2281 1986 ; +91 97123 78624", email_generic="info@elixirpharma.in",
    dm="Not named on site (find via LinkedIn/Apollo)",
    signal="Hiring 20 chemists (10 production, 5 R&D, 4 QC); three new APIs in development; WHO-GMP and EU-GMP claimed",
    multi_loc=False, rank=1, src="https://www.elixirpharma.in/career.html")
add(company="Verito Engineering Pvt Ltd", industry="Engineering", sub="Agitators, dosing pumps, dosing systems", hc="51-200 (Apollo)",
    address="Verito Tower, Near Express Highway, Ramol, Vatva GIDC Phase-IV, Ahmedabad 382449 (2 units in Vatva/Ramol)", cluster="Vatva / Ramol",
    website="veritoengineering.com", phone="+91 76005 52286 ; 079-9004 5766 ; purchase +91 76005 52291", email_generic="(obfuscated on site)",
    dm="Not named on site (find via LinkedIn/Apollo)",
    signal="2 units + 6 India regional offices + 7 international offices; exports to 25+ countries; 4 product divisions. Classic make-to-order with multi-location sales",
    multi_loc=True, rank=3, src="https://www.veritoengineering.com/contact-us.php")
add(company="YCUBE Engineered Solutions Pvt Ltd", industry="Engineering / Distribution", sub="Valves, pumps, actuators distribution + valve manufacturing", hc="51-200 (Apollo)",
    address="#310, Central by Sangath IPL, B/H 4D Square, Visat-Gandhinagar Hwy, Motera, Ahmedabad 380005. Plant: Shed 03-04 Block B, Kuha, Ahmedabad-Indore Hwy 382433", cluster="Motera / Kuha",
    website="ycubeindia.com", phone="+91 79 4941 0313 ; +91 89809 51008", email_generic="sales@ycubeholdings.com",
    dm="Sam Yamdagni (Group CEO & Chairman); Bhupender Singh (MD); Sonia Yamdagni (Director)",
    signal="Plant + 5 India sales offices + UAE and Thailand entities: multi-company, multi-currency, distribution plus manufacturing",
    multi_loc=True, rank=3, src="https://www.ycubeindia.com/about-us.php ; /contact-us.php")
add(company="Fluid Logic Systems Pvt Ltd (Systems Group)", industry="Engineering", sub="Hydraulic systems for machine tools", hc="51-200 (Apollo)",
    address="11-12 Maha-Gujarat Industrial Nagar, B/h Hotel Surbhi, NH 8A, Sarkhej-Bavla Rd, Moraiya 382213, Sanand, Ahmedabad", cluster="Changodar / Moraiya",
    website="systemshydraulics.com", phone="+91 79 2979 6404-406", email_generic="info@systemshydraulics.com",
    dm="Not named on site (find via LinkedIn/Apollo)",
    signal="Weak external signal; engineered-to-order hydraulics (job costing, BOM). Needs a call to qualify",
    multi_loc=False, rank=3, src="https://www.systemshydraulics.com/")
add(company="Techflow Enterprises Pvt Ltd", industry="Engineering", sub="Air pollution control: dust collectors, fans, ESPs", hc="51-200 (Apollo)",
    address="Block No. 803/B/1, Nr. Canal, Kubadthal Village, Off Kunjad-Kathlal Rd, Via Kathwada SP Ring Road Circle, Ahmedabad 382430", cluster="Kathwada / Kubadthal",
    website="techflow.net", phone="+91 78747 19999 ; +91 88669 80744", email_generic="sales@techflow.net ; info@techflow.net",
    dm="D. K. Parikh (Chairman & Founder); Monil Parikh and Chintan Parikh (sons, titles not on site)",
    signal="Project-based engineering with large orders (Tata group); exports 22% of FY2025-26 sales to 58 markets; tripled paint shop capacity. Second generation in business",
    multi_loc=False, rank=3, src="https://techflow.net/ ; /about-us/")
add(company="Ecosafe Agriscience India Pvt Ltd", industry="Chemicals", sub="Agrochemical formulations and fertilisers", hc="51-200 (Apollo)",
    address="250/A 22 Uma Industrial Estate, Vasna Iyava, Sanand 382170; office C/902-903 Signature 2, Sarkhej-Sanand Cross Rd 382210", cluster="Sanand / Sarkhej",
    website="ecosafe.co.in", phone="+91 88875 10198", email_generic="info@ecosafe.co.in",
    dm="Not named on site (find via LinkedIn/Apollo)",
    signal="70+ formulations, dealer distribution network (seasonal stock, schemes, credit control)",
    multi_loc=True, rank=2, src="https://www.ecosafe.co.in/contact/")
add(company="Mahavir Industries (Mahavir Pigments)", industry="Chemicals", sub="Organic and inorganic pigments", hc="51-200 (Apollo)",
    address="C-1/58 GIDC Phase-2, Vatva, Ahmedabad 382445", cluster="Vatva",
    website="mahavirpigments.com", phone="+91 90338 97601 ; +91 79 4008 5720", email_generic="info@mahavirpigments.com",
    dm="Not named in fetched pages (site has a Management page to check)",
    signal="Two Star Export House, exports to 40+ countries; REACH/GOTS/Halal documentation load; est. 1979 (likely legacy systems)",
    multi_loc=False, rank=2, src="https://www.mahavirpigments.com/facility-certifications/")
add(company="JEE Pumps Ltd", industry="Engineering", sub="Industrial process pumps, own foundry", hc="51-200 (Apollo)",
    address="HO: Plot L-1 & 2, GIDC Nr Water Tank, Odhav, Ahmedabad 382415. Plant: Block 407-B & 408-B, Kubadthal-Pasunj Rd, Kubadthal 382433", cluster="Odhav / Kubadthal",
    website="jeepumps.com", phone="+91 96876 50618", email_generic="info@jeepumps.com",
    dm="Prakash Patel (Managing Director, founder)",
    signal="Converted from Pvt Ltd to Ltd (often an IPO precursor; verify); three manufacturing campuses + foundry; hiring application engineer",
    multi_loc=True, rank=3, src="https://www.jeepumps.com/about-jeepumps/ ; /careers")

# Held / excluded with reason (kept for transparency, not in the 100)
HOLD = [
 ("Swiss Pharma Pvt Ltd", "Site states 300+ staff, above the 200 band. Vatva. Tier C unless you want larger accounts."),
 ("Remus Pharmaceuticals", "Group revenue USD 150M (FY23) and US office; likely buys at group level. Bopal office only."),
 ("Asahi Songwon Colors Ltd", "Listed company with large board; probably above band and on an established ERP. Verify before adding."),
 ("HCP Plastene Bulkpack Ltd", "Listed, part of Plastene group with 8 plants; above band. Hold."),
 ("Skycare Pharmaceuticals / Aash Biotech / Stivaph / Veer Plastics", "Website not readable; research via other sources later."),
]

add(company="MBH Pumps (Gujarat) Pvt Ltd", industry="Engineering", sub="Submersible and dewatering pumps, exporter (est. 1969)", hc="51-200 (Apollo)",
    address="14 GIDC Naroda Industrial Estate, Ahmedabad 382330", cluster="Naroda",
    website="mbhpumps.com", phone="(079) 2282 3066 ; +91 94275 33830", email_generic="marketing@mbhpumps.com ; purchase@mbhpumps.com",
    dm="Parth Kamania (Director; listed as parth@mbhpumps.com on site)",
    signal="Hiring export sales manager and proposal engineer; separate service/spares desk (after-sales tracking); published 2023 integrated report",
    multi_loc=False, rank=3, src="https://www.mbhpumps.com/contact-us/ ; /careers/")
add(company="PressureJet Systems Pvt Ltd", industry="Engineering", sub="High-pressure plunger pumps and systems", hc="51-200 (Apollo)",
    address="Plant: Plot 21-24 Panchratna Industrial Estate, Near Ode Village, Paldi Kankaj, Pirana, Ahmedabad 382427. HO: Krish Cubical B-1201-1212, Off Sindhu Bhavan Rd, Thaltej 380059", cluster="Pirana / Thaltej",
    website="pressurejet.com", phone="+91 93750 22359 (sales) ; +91 93760 22353 (procurement)", email_generic="sales@pressurejet.com ; Purchase@pressurejet.com",
    dm="Not named on site (find via LinkedIn/Apollo)",
    signal="Serves 50+ countries, 5000+ customers; separate spares and service lines (spares inventory, field service)",
    multi_loc=True, rank=3, src="https://www.pressurejet.com/about-us ; /contact-us")
add(company="Airmax Pneumatics Ltd", industry="Engineering", sub="Pneumatic cylinders, valves, FRLs", hc="51-200 (Apollo)",
    address="HO: Plot 133 'Hydint House', B/h Cozy Hotel, Narol Road, Ahmedabad 382405. Factory: Plot 205-206 Kagdi Estate, Ranipur Rd, Narol 382405", cluster="Narol",
    website="airmaxindia.com", phone="+91 75678 60865 ; export +91 63570 57600", email_generic="export@airmaxindia.com (decoded, verify)",
    dm="Not named on site (find via LinkedIn/Apollo)",
    signal="HO + factory; supplies BHEL, NTPC, Reliance, Adani (project documentation, tender-driven orders)",
    multi_loc=True, rank=3, src="https://www.airmaxindia.com/contact/")
add(company="Indo-Air Compressors Pvt Ltd", industry="Engineering", sub="Air compressors and vacuum pumps", hc="51-200 (Apollo)",
    address="Plot No. 550, Main Road GIDC Estate, Kathwada, Ahmedabad 382430", cluster="Kathwada",
    website="indoair.com", phone="+91 79 2290 1951 ; +91 98244 03616", email_generic="info@indoair.com",
    dm="C. M. Panchal (Managing Director)",
    signal="Hiring GM Sales & Marketing plus 5 service roles across West/North/South India (field service + spares across regions); exports to 27 countries",
    multi_loc=False, rank=3, src="https://www.indoair.com/careers.php ; /about.php")
add(company="Gopani Product Systems / Gopani Filters Pvt Ltd", industry="Engineering / Distribution", sub="Industrial filtration products", hc="51-200 (Apollo)",
    address="104 Kashi Parekh Complex, Swastik Cross Rd, C.G. Road, Navrangpura, Ahmedabad 380009", cluster="Navrangpura (office)",
    website="gopani.com", phone="+91 70690 18049", email_generic="sales@gopani.com",
    dm="Pathik Gopani (Founder)",
    signal="Hiring 7 sales roles incl. regional managers; acquired Uniexcel and started two more companies (multi-company consolidation); claims double-digit YoY growth",
    multi_loc=True, rank=3, src="https://www.gopani.com/about-us/ ; /career/")
add(company="Cair Euromatic Automation Pvt Ltd", industry="Engineering", sub="Electric actuators and motorised valves", hc="51-200 (Apollo)",
    address="Unit 1: Plot 129/2 Shed 1, Cair Estate, Ranipur Rd, Nr Kashiram Textile Mill, Narol 382405. Unit 2: Plot 177 Shiv Shakti Estate, Narol Rd 382405", cluster="Narol",
    website="cairindia.com", phone="+91 79 2970 8286 ; +91 99250 11360", email_generic="inquiry@cairindia.com",
    dm="Not named on site (find via LinkedIn/Apollo)",
    signal="Hiring 9 roles incl. 3 QC inspectors, QMS compliance exec and GeM tender exec (quality and tender paperwork load); 2 units",
    multi_loc=True, rank=3, src="https://www.cairindia.com/current-jobs/")
add(company="Leistung Engineering Pvt Ltd", industry="Engineering", sub="Filtration systems, valves, bioreactors for pharma", hc="51-200 (Apollo)",
    address="Survey No. 1009/2, 1004/3, 1005/1&2, Navsari Lat, Pirana Temple Rd, Paldi-Kankaj, Daskroi, Ahmedabad 382425", cluster="Pirana",
    website="leistung.in", phone="+91 89058 28423", email_generic="info@leistung.in",
    dm="Atish Parikh (Chairman)",
    signal="ASME/PED/US FDA compliance documentation; engineered-to-order for pharma (BOM, traceability of materials)",
    multi_loc=False, rank=3, src="https://leistung.in/company-profile/")
add(company="Rohan Dyes & Intermediates Ltd", industry="Chemicals", sub="Sulphur chemicals, dye intermediates, dyes", hc="51-200 (Apollo; verify, may be larger)",
    address="Dyes plant: GIDC Vatva, Ahmedabad (plot not published). Other plants: Khambhat (2), Dahej", cluster="Vatva",
    website="rohanchemicals.com", phone="+91 79 2642 2997 ; +91 99099 09124", email_generic="info@rohanchemicals.com",
    dm="Rohan Jindal (CEO); Radheshyam Jindal (Chairman)",
    signal="4 plants across 3 locations; new SO2 line 2023, sulfuryl chloride planned 2026; exports 35-50+ countries",
    multi_loc=True, rank=2, src="https://rohanchemicals.com/about/")
add(company="Ishan Dyes and Chemicals Ltd", industry="Chemicals", sub="Phthalocyanine pigments, sulphur chemicals", hc="51-200 (Apollo)",
    address="Plot no. 18, GIDC Vatva Phase 1, Ahmedabad 382445", cluster="Vatva",
    website="ishandyes.com", phone="+91 79 2583 2144 ; 2589 3607", email_generic="ishan@ishandyes.com",
    dm="Not on fetched pages (listed company: check BSE filings for MD)",
    signal="Listed (BSE) with 2 units: statutory reporting and audit pressure; exports to 15+ countries",
    multi_loc=True, rank=2, src="https://www.ishandyes.com/")
add(company="Alps Chemicals Pvt Ltd", industry="Chemicals", sub="Dyes and pigments (paper, leather, food, inks)", hc="51-200 (Apollo)",
    address="612, Phase 4, Vatva GIDC, Ahmedabad 382445", cluster="Vatva",
    website="alpschemicals.com", phone="+91 96011 26325 (site also links +91 97244 08067)", email_generic="info@alpschem.com",
    dm="Not named on site (find via LinkedIn/Apollo)",
    signal="Exports to 40+ countries across 6 continents (multi-currency, export docs)",
    multi_loc=False, rank=2, src="https://www.alpschemicals.com/contact/")
add(company="Hindprakash Chemicals Pvt Ltd", industry="Chemicals / Distribution", sub="Dyes, intermediates, solvents, pigments, resins (est. 1942)", hc="51-200 (Apollo; verify, may be larger)",
    address="101 'Hindprakash House', Plot 10/6, Phase 1, GIDC Vatva, Ahmedabad 382445", cluster="Vatva",
    website="hindprakash.com", phone="(not on site; find via Google Maps)", email_generic="info@hindprakash.com",
    dm="Not named on site (find via LinkedIn/Apollo)",
    signal="5 plants + subsidiaries in Shanghai, Vietnam, UAE; 2,185 customers: multi-company, multi-currency consolidation",
    multi_loc=True, rank=2, src="https://www.hindprakash.com/")
add(company="Ushanti Colour Chem Ltd", industry="Chemicals", sub="Reactive, direct, acid dyes; CPC pigments", hc="51-200 (Apollo)",
    address="88/6, 88/7, 88/8, Phase 1, GIDC Vatva, Ahmedabad 382445", cluster="Vatva",
    website="ushanti.com", phone="+91 79 2589 4903 ; 2583 3315", email_generic="marketing@ushanti.com",
    dm="Minku Shantilal Gandhi (Jt. MD); Maunal Shantilal Gandhi (Jt. MD)",
    signal="Listed SME with plants at Vatva and Saykha plus a subsidiary: consolidation and audit load",
    multi_loc=True, rank=2, src="https://ushanti.com/about-us/")
add(company="Anar Chemicals LLP", industry="Chemicals", sub="Solvent dyes, phthalocyanines, flame retardants, CDMO", hc="51-200 (Apollo)",
    address="Factory: 12,14 GIDC Phase 1, Vatva 382445. Corporate: Chitrakoot, Opp C.N. Vidyalaya, Ambawadi, Ahmedabad 380006", cluster="Vatva / Ambawadi",
    website="anarchem.com", phone="+91 84258 38227 (WhatsApp)", email_generic="info@anarchem.com",
    dm="Sanjay Choksi (CEO); Ajay Choksi (Executive Chairman); Kalpesh Sura (GM Operations); Piyush Suthar (Manager Finance & Accounts)",
    signal="Launched US outsourcing/procurement division Jan 2024; Mumbai office; AEO T2 and EcoVadis (compliance data); Two Star Export House",
    multi_loc=True, rank=2, src="https://anarchem.com/about-us/")
add(company="Crystal Quinone Pvt Ltd", industry="Chemicals", sub="Specialty intermediates, antioxidants, CDMO", hc="51-200 (Apollo)",
    address="Corporate: 403/404 Abhijeet-III, Law Garden, Mithakhali Rd, Ahmedabad 380006. Plants: Plots 143, A-2/20-21, 145 GIDC Vatva Ph II 382445", cluster="Vatva / Law Garden",
    website="crystalquinone.com", phone="+91 79 4807 8000 ; +91 98250 06600", email_generic="info@crystalquinone.com",
    dm="Anang Shah and Aniket Shah (promoters; titles not on site)",
    signal="Commissioned new plant at Saykha in 2024; 4-5 units + sister company + stock in Antwerp; BRC/FAMIQS/ISO 22000 traceability",
    multi_loc=True, rank=2, src="https://www.crystalquinone.com/about-us")
add(company="Molkem", industry="Chemicals / Pharma trading + CDMO", sub="APIs, excipients, specialty chemicals; R&D lab", hc="51-200 (Apollo)",
    address="Reg: 401 Naindhara, Nr GNFC Info Tower, SG Highway, Bodakdev 380054. Corporate: Opp DoubleTree by Hilton, Ambli Rd 380058. Lab: Palodia, Kalol (Gandhinagar)", cluster="SG Highway / Bodakdev",
    website="molkem.com", phone="+91 79 6120 2500", email_generic="hello@molkem.com",
    dm="Preet Shah (Founder & CEO); Meet Shah (Director Global Sales & Partnerships); Nutan Patel (GM HR & Corporate Affairs)",
    signal="16 open roles incl. purchase, sourcing, QA; subsidiaries in Brazil, Vietnam, Dubai and offices in 3 more countries: multi-company, multi-currency",
    multi_loc=True, rank=2, src="https://www.molkem.com/career ; https://www.molkem.com/")

HOLD += [
 ("Jay Pumps / Kevin Process Technologies / La Gajjar (Varuna Pumps)", "Websites unreadable; Varuna likely above band. Research via browser."),
]

# LinkedIn finds via Google site:linkedin.com/in search, 13 Nov 2026. Title as shown in the Google snippet; verify current role before outreach.
LI = {
 "Verito Engineering Pvt Ltd": ("Samadhan Sonawane (Technical Director)", "https://in.linkedin.com/in/samadhan-sonawane-18460a184"),
 "Fluid Logic Systems Pvt Ltd (Systems Group)": ("Anish Nanavati (Managing Director)", "https://in.linkedin.com/in/anish-nanavati-8b61a475"),
 "Ecosafe Agriscience India Pvt Ltd": ("Rajiv Kumar Hudda (Founder & MD; company name truncated in snippet, verify)", "https://in.linkedin.com/in/rajiv-kumar-hudda-27b304108"),
 "PressureJet Systems Pvt Ltd": ("Vishal Shah (Managing Director); Abhi Shah (Director)", "https://in.linkedin.com/in/vishal-shah-pressurejet"),
 "Cair Euromatic Automation Pvt Ltd": ("Atique Kothawala (Director)", "https://in.linkedin.com/in/atique-kothawala-88158854"),
 "Alps Chemicals Pvt Ltd": ("Haresh Bhuta (Owner); Nikhil Mehta (Director); Vandana Bhuta (Director)", "https://in.linkedin.com/in/haresh-bhuta-857a7430"),
 "Hindprakash Chemicals Pvt Ltd": ("Sanjay Mangal (Owner & Director, Hindprakash Group); Abhinav Agrawal (MD)", "https://in.linkedin.com/in/sanjay-mangal-a0254321"),
 "Ishan Dyes and Chemicals Ltd": ("Shrinal Patel (Executive Director)", "https://in.linkedin.com/in/shrinal-patel-9a4bb7193"),
 "Elixir Pharma Chem Pvt Ltd": ("Bipin Patel (Chairman); Daleep Malhotra (Executive Director BD)", "https://in.linkedin.com/in/bipin-patel-422560132"),
 "HOF Pharmaceuticals Ltd": ("Abhigna Patel (CEO per site, Director per LinkedIn)", "https://in.linkedin.com/in/abhigna-patel-7962a3202"),
 "APDM Pharmaceuticals Pvt Ltd": ("Jayanta Mandal (MD & CEO)", "https://in.linkedin.com/in/jayanta-mandal-5674a316"),
 "Vasa Pharmachem Pvt Ltd": ("Purav Patel (Executive Director); Dr. Runal Vasa Patel (Executive Director)", "https://in.linkedin.com/in/purav-patel-478aba112"),
 "YCUBE Engineered Solutions Pvt Ltd": ("Dimple Chauhan (Sr. Manager Accounts & HR, finance contact)", "https://in.linkedin.com/in/dimple-chauhan-96a3b516a"),
 "Techflow Enterprises Pvt Ltd": ("Chintan Parikh (Executive Director); Dhiren Parikh (Chairman)", "https://in.linkedin.com/in/chintan-parikh-techflow"),
}
for a in A:
    if a["company"] in LI:
        who, url = LI[a["company"]]
        a["li"] = url
        if a["dm"].lower().startswith("not "):
            a["dm"] = who + " [LinkedIn]"
        else:
            a["dm"] = a["dm"] + " | LinkedIn: " + who
    else:
        a.setdefault("li", "")
# Caution: Mediwin's LinkedIn shows "Manish Patel, Director", but the company site lists him as late. Do not contact.
