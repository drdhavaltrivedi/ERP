# ERP lead generation and tracking

This repo holds the go-to-market work for selling Odoo and ERPNext implementations to manufacturers, starting in Ahmedabad.

## Layout

| Path | What it is |
|---|---|
| `gtm/01-icp-odoo-mid-market.md` | Ideal customer profile: industries, pain signals, personas, objections, qualification |
| `gtm/02-phase-plan.md` | Phases (Ahmedabad, rest of Gujarat, India, export market) and the credit plan |
| `gtm/leads/accounts.csv` | **The lead tracker.** One row per account, with status, owner and next step. This is the source of truth. |
| `gtm/leads/ahmedabad-tracker.xlsx` | Excel view built from the CSVs, with a summary sheet and a status dropdown |
| `gtm/leads/held.csv` | Accounts researched but held back, with the reason |
| `gtm/logs/*.csv` | Activity logs: calls, visits, emails, LinkedIn and WhatsApp |
| `gtm/scripts/00-call-playbook.md` | Conversational cold-call playbook (v3): opener, curiosity moves, branches for reception, wrong person, busy, "send an email", already on an ERP, not required and dead numbers; exits, objections, outcome codes, round-1 lessons |
| `gtm/scripts/02-follow-up-emails.md` | Follow-up email template for "send me an email", with drafts for Mediwin and Rohan Dyes |
| `gtm/scripts/01-buyer-faq.md` | 31 questions prospects will ask, with answers (top 10 also in Gujarati) |
| `gtm/scripts/accounts/AMD-xxx-*.md` | One conversational call script per account (v2): receptionist line, permission opener, who we are, what we saw on their site, five easy questions, reflect the pain, one line of value, visit ask, pushback table; Gujarati and English lines; likely FAQ; email draft with follow-ups; WhatsApp; visit checklist |
| `gtm/research/ahmedabad-web-research.jsonl` | Website research for every candidate (qualified or not, with the reason) |
| `gtm/research/pending.txt` | Candidates not researched yet |
| `gtm/tools/` | `research_seed.py` and `hooks.py` (first 27 accounts), `v2_27.py` and `v3_27.py` (their conversational lines, curiosity questions and round-1 follow-up plans), `research_rules.py` (review decisions on the web research), `script_v3.py` (script template), `build.py` (rebuilds tracker, held list and scripts) |

## Daily routine

1. Pick accounts from `leads/accounts.csv` where `next_step_date` is today or empty, Tier A first, grouped by `cluster` for visits.
2. Open the account's script in `scripts/accounts/`.
3. Log every call, visit or message in the matching file in `logs/`.
4. Update `status`, `next_step` and `next_step_date` in `leads/accounts.csv`.
5. Run `python3 gtm/tools/build.py` to refresh the Excel view, then commit.

Commit messages like `log: AMD-007 call, meeting booked 20 Nov` keep the history readable, so `git log` doubles as an activity feed.

## Rules

- No outreach is sent without approval. Email drafts in the scripts are drafts.
- Never name the past MP client. Refer to them as "a building-materials manufacturer in MP".
- Personal data here is limited to business contact details published by the companies themselves or on public profiles. Keep the repo private.
