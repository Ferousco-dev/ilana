# PHASE 11 GATE

This phase is continuous and constrains all the others. It is checked at G0 (exposure scan) and
G8 (register disposition), and `ethics-officer` may raise a halt at any point in between.

## The two questions, at every rigour

Asked at intake, in every mode:

1. Who is harmed if this software is wrong?
2. What data does this hold, and what happens to a person if it leaks?

If both answers are genuinely "nobody, nothing", record that and proceed lightly. If either
answer names a real person or a real harm, `RIGOUR` is at least 3, and probably 4.

## Halt authority

`ethics-officer` may halt any phase when:

- a known defect that can cause harm is scheduled to ship undisclosed,
- verification is being skipped to meet a date on a system that can harm people,
- the request is for a control-defeating mechanism (see `kernel/refusal-protocol.md`),
- personal, medical or financial data is being handled in a way the user has not sanctioned,
- a licence obligation is being knowingly breached.

The halt is recorded as `ETH-###`. Only the human user lifts it, and the lift is recorded with
their stated justification. Ìlànà does not argue a second time.
