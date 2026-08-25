# Error Catalogue

Every user-visible error is a row. Four columns are mandatory. An error not in this table is a
finding at G3.

| ID | Condition | What the user sees | Why (if actionable) | What to do next | Work preserved | Logged as |
| --- | --- | --- | --- | --- | --- | --- |
| ERR-001 | payment card expired | "We could not take payment: that card expired in June 2025." | expiry date in the past | "Add a different card, or update the expiry date." | basket retained 24h | `payment.declined.expired` |
| ERR-002 | upstream catalogue unavailable | "Search is temporarily unavailable. Browsing still works." | dependency down | "Try again in a few minutes, or browse by category." | query text retained | `catalogue.unavailable` |

## Rules

1. **Never leak implementation detail.** Stack traces, SQL, internal hostnames and class names
   are for the log, not the user. This is a security control as well as a usability one.
2. **Never say "something went wrong" alone.** If you genuinely cannot say more, give the user
   a reference code that support can trace, and say so.
3. **Always preserve work.** An error that discards what the user typed is a second, larger
   failure on top of the first.
4. **Always give a next action.** Even "wait and retry" is an action. "Contact support" is only
   acceptable when the user genuinely cannot resolve it.
5. **The log line and the user message are different strings.** The log carries the diagnosis;
   the message carries the recovery.
