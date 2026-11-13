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
| `gtm/scripts/00-call-playbook.md` | Language guide, call flow, objection answers, logging rules |
| `gtm/scripts/accounts/AMD-xxx-*.md` | One personalised script per account: call opener in Gujarati, Hindi or English, discovery questions, objections, email draft, visit checklist |
| `gtm/tools/` | `research_seed.py` (research data), `hooks.py` (personalisation), `build.py` (rebuilds the tracker view and scripts) |

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
