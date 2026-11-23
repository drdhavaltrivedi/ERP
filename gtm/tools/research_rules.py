# Manual review decisions applied on top of the web research in gtm/research/ahmedabad-web-research.jsonl.

# Industry rank used in scoring (1-3 = core ICP). Building materials is core because of the MP reference project.
RANK = {"Pharma": 1, "Chemicals": 2, "Engineering": 3, "Electrical": 3, "Medical devices": 3, "Building materials": 3,
        "Plastics & packaging": 4, "Textiles": 4, "Food": 4, "Other": 5}

# Company names where the site did not state one clearly (confirm the legal name on the first call).
NAMES = {
    "viprolifescience.com": "Vipro Lifescience",
    "shyamplastic.com": "Shyam Plastic Machinery",
    "armstrongex.com": "Armstrong Extrusion (name to confirm)",
    "mechpowertech.com": "Mech Power Tech",
    "tacklers.in": "Tacklers",
    "activeengineers.com": "Active Engineers",
    "saielectronicsindia.com": "SAI Electronics",
    "shailjaindia.com": "Shailja",
    "deedygroup.com": "Deedy Chemicals Pvt Ltd",
    "friendssteel.com": "Friends Steel Group (Friends Ispat Ltd)",
    "powertracgroup.com": "Powertrac Group",
    "biotekortho.com": "Chetan Meditech Pvt. Ltd. (Biotek)",
}

# Researched as "Q" but held back after review.
HOLD_OVERRIDE = {
    "qchem.in": "set up in 2024; team size unclear (site counter shows 1+). Revisit in 2027",
    "hpbl.in": "part of the Plastene group with 8 plants; likely over 500 staff",
    "bloomdekor.com": "site links an insolvency (CIRP) page; check status before any outreach",
    "raghuvirexim.com": "listed, several large units; likely over 500 staff",
    "apisyn.com": "350+ scientists stated; total headcount likely over 500",
}

# Kept, with a caution for the caller.
NOTES = {
    "yamir.in": "Plant in Kadi; head office in Ahmedabad.",
    "gcacpl.co.in": "Plant at Mundra; office in Ahmedabad. Visit the office.",
    "satvam.in": "Factory in Prantij; office on SG Highway.",
    "maanpharmaindia.com": "Plant in Mehsana; office in Ahmedabad.",
    "puniska.com": "Factory in Goa; office on Ambli-Bopal Road.",
    "sunhearrt.com": "Plant in Morbi; office on SG Highway.",
    "vasantmasala.com": "Factory in Dehgam; confirm head office.",
    "supernovagenset.com": "Plants at Rajpur (Kadi) and Silvassa; head office on SG Road.",
    "powertracgroup.com": "Factory in Surendranagar; corporate office in Ahmedabad.",
    "jainsoncablesindia.com": "Factory at Chandarda (Kadi taluka); sales office in Ahmedabad.",
    "swatiswitchgears.com": "Site says 350-450 people; confirm headcount, may be above the ICP band.",
    "hpautomation.in": "Much of the business is brand distribution; confirm the panel-building side.",
    "saielectronicsindia.com": "Own plant not confirmed on the site; confirm on the call.",
    "nandanterry.com": "Part of the Chiripal group; confirm headcount, may be above the ICP band.",
    "stovecindustries.com": "Listed subsidiary of SPGPrints (Netherlands); decision may sit with the parent.",
    "tech-long.in": "Indian arm of a Chinese group; decision may sit with the parent.",
    "dubondindia.com": "Factory address not on site; confirm.",
    "hitechelastomers.com": "Headcount was 350 in 2010; confirm current number.",
    "aztecindia.org": "Factory location not stated; confirm.",
    "vikramthermo.com": "Listed company; manufacturing unit location not stated.",
}
