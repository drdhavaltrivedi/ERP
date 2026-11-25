# Follow-up emails after "send me an email"

Use these when a call ends with "mail kar dijiye" (playbook branch D). Drafts only: nothing is sent until it is approved.

**Rules for these emails**

- Send within an hour of the call, while they still remember it.
- Under 120 words. One question they can answer in one line.
- Mention the call in the first line, so it doesn't read as a mass mailer.
- Subject line: company name plus one specific topic. No "Introduction" or "Partnership opportunity".
- If they chose a topic on the call (stock or costing, for example), write only about that topic.
- Log it in `logs/emails.csv` with `step` = `first`, and put the callback date in `leads/accounts.csv`.

## Template

**Subject:** [Company]: [topic in 3 to 6 words]

Hi [Name],

I called your office [today / on Tuesday] and was asked to send a short note, so here it is.

I'm Dhaval from Brilworks, an Odoo and ERPNext partner in Ahmedabad. I was reading about [one fact from their website], and it made me curious about one thing: [the account's pain question].

If that's already handled well, a one-line reply saying so is genuinely useful to me. If it isn't, I'd like to show you in 30 minutes at [plant] how it could work, with Tally staying in place for accounts and GST if you prefer.

I'll call on [day] to see whether this is worth a conversation.

Regards,
Dhaval
Brilworks | Odoo and ERPNext partner
[Phone]

---

## AMD-001 · Mediwin Pharmaceuticals

**To:** Kathan Patel (confirm the address; fallback `info@mediwinpharma.com`, marked "Attn: Kathan Patel")
**Assumed:** the notes say "asked to mail him". We assume "him" is Kathan Patel, the first person the script asks for. Confirm before sending.

**Subject:** Mediwin: batch and expiry across Naroda and Sari

Hi Kathan,

I called your office recently and was asked to send you a short note, so here it is.

I'm Dhaval from Brilworks, an Odoo and ERPNext partner in Ahmedabad. Your website mentions two WHO-GMP plants at Naroda and Sari and a target of 50 export countries by 2030, and it made me curious about one thing: can your team see batch and expiry stock for both plants on one screen today, or does each plant keep its own register and Excel?

If that's already handled well, a one-line reply saying so is genuinely useful to me. If it isn't, I'd like to show you in 30 minutes at the Naroda plant how it could work, with Tally staying in place for accounts and GST if you prefer.

I'll call on Tuesday 1 December to see whether this is worth a conversation.

Regards,
Dhaval
Brilworks | Odoo and ERPNext partner
[Phone]

## AMD-003 · Rohan Dyes & Intermediates Ltd

**To:** the person who asked for the email (not recorded). If unknown, Rohan Jindal (CEO) at `info@rohanchemicals.com`, marked "Attn: Rohan Jindal".
**Assumed:** who asked and which address they gave are not in the call notes.

**Subject:** Rohan Dyes: stock transfers between Vatva, Khambhat and Dahej

Hi Rohan,

I called recently and was asked to send a short note, so here it is.

I'm Dhaval from Brilworks, an Odoo and ERPNext partner in Ahmedabad. Your website mentions plants at Vatva, Khambhat and Dahej and a new sulfuryl chloride line coming in 2026, and it made me curious about one thing: when stock moves between the three plants, does it match at all three, or do mismatches turn up at month-end?

If that's already handled well, a one-line reply saying so is genuinely useful to me. If it isn't, I'd like to show you in 30 minutes at the Vatva plant how plant-wise stock and yield costing could sit in one system, with Tally staying in place for accounts and GST if you prefer.

I'll call on Tuesday 1 December to see whether this is worth a conversation.

Regards,
Dhaval
Brilworks | Odoo and ERPNext partner
[Phone]

## If there's no reply after the callback

**Day 7, same thread:**

Hi [Name], one last note from me. If [topic] isn't a priority right now, no problem at all. Would it make sense for me to check back in [month]?

Then set status to `Nurture` with that month as `next_step_date`.
