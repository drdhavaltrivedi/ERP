# Call, visit and email playbook

Per-account scripts live in `scripts/accounts/`. This page covers what applies to every call.

## Which language to use

You speak English, Hindi and Gujarati, so use the language the buyer is most comfortable in, not one fixed choice.

| Channel | Language | Why |
|---|---|---|
| Phone, first 10 seconds | **Gujarati** by default | Most targets are promoter-led Ahmedabad family businesses. A Gujarati opener sounds like a local partner, not a call centre. |
| Phone, after their first reply | **Mirror them** | If they answer in Hindi or English, switch at once and stay there. |
| Companies run from outside Gujarat | **Hindi** first | Marked in each script (for example, a registered office in Delhi or Maharashtra). |
| Plant visits | Gujarati or Hindi with the owner and plant team, English for the CA or CFO if they prefer | Shop-floor staff and owners talk operations in Gujarati or Hindi. Finance people often prefer English terms. |
| Email, LinkedIn | **English** | Written business communication in Gujarat is mostly English, and emails get forwarded to CAs and finance heads. |
| WhatsApp follow-up | Same language as the call | Keeps continuity. |

Keep technical words in English inside Gujarati or Hindi sentences: ERP, stock, batch, GST, e-invoice, BOM, costing. That is how people actually talk about this, and pure-Gujarati terms sound odd.

This is a judgement call, not tested data. After 20 calls, look at `logs/calls.csv` (column `language_used` against `outcome`) and adjust.

## Call flow (about 3 minutes)

1. **Gatekeeper:** ask for the decision maker by name. If asked "what is it about?": "It's about their ERP and stock system. Two minutes."
2. **Opener:** use the account's hook (the specific fact in the script). It shows you did your homework.
3. **One question:** the pain question from the script. Then listen.
4. **Ask for a visit**, not a demo: "Can I come by for 30 minutes next week?"
5. **Log the call** in `logs/calls.csv` the same day.

If they are busy: "When should I call back?" Write the date in `next_step_date`.

## Objections (short answers)

| They say | You say |
|---|---|
| "Tally is enough." | "Tally is great for accounts. Where it runs out is stock across plants, batch costing and approvals. How do you handle those today?" |
| "Too costly." | "Phase 1 is inventory, purchase, sales and accounts with GST, from ₹2 lakh. We can do ERPNext if you'd rather not pay per-user licences." |
| "We tried an ERP before and it failed." | "What went wrong? We go live in phases, so nothing breaks on day one." |
| "We use Tranzact or a Tally add-on." | "What still lives in Excel or WhatsApp?" |
| "Who else uses it?" | "We built the ERP for a building-materials manufacturer in MP. We're also taking two or three Ahmedabad plants on reference terms this year." Never name the MP client. |
| "Send me details." | "Sure. What should I focus on: stock, production or accounts?" Then email within the hour and log it. |
| "After March." | "That's a good time to go live, on 1 April. To go live then, we'd need to start scoping in January. Can we meet before that?" |

## How to log

All logs are CSV files in `gtm/logs/`. Open them in Excel or Google Sheets, or edit them on GitHub. Use one row per activity.

- `calls.csv`: every dial, including no answer.
- `visits.csv`: every in-person visit.
- `emails.csv`: every email sent, with the `step` column set to `first`, `day4` or `day10`.
- `linkedin_whatsapp.csv`: connection requests, DMs and WhatsApp messages.

Use `account_id` (for example `AMD-007`) so activity links to the tracker. Use `date_ist` as `YYYY-MM-DD HH:MM`.

Then update `status`, `next_step` and `next_step_date` for that account in `leads/accounts.csv`. Statuses: Researched, Called - no answer, Called - gatekeeper, Called - spoke to DM, Meeting booked, Visited, Discovery done, Proposal sent, Won, Lost, Not a fit, Do not contact.

To refresh the Excel view and the summary counts, run `python3 gtm/tools/build.py`.

## Rules

- No email, DM or sequence goes out until it is approved. The email drafts in each script are drafts.
- Check names and roles before every call. One LinkedIn result named a director whom the company's own site lists as late.
- Never name the MP client in any message, file or call.
- If someone says "no", set status to `Do not contact` and stop.
