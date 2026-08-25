# PHASE 11 ANTI-PATTERNS

## Ethics as a Final Checkbox
A review performed just before release, when the architecture is already fixed and the data model
already collects more than it should.
**Fix:** ethics is part of every stage. Questions 1 and 2 are asked at intake.

## Skipping Verification for the Date
The canonical case in the source material. Not a trade-off; a transfer of risk onto users who
did not agree to carry it.
**Fix:** Article 6. `ethics-officer` may halt. If the decision is taken anyway, it is recorded
with a named accountable person.

## The Hidden Defect at Release
Shipping with a known critical defect and not telling anyone. The concurrency bug in the health
records system that occasionally writes to the wrong patient, shipped because it affects fewer
than 0.01% of transactions.
**Fix:** the correct action is to delay, disclose the risk to stakeholders, resolve the defect,
and repeat verification before release. Article 1 and Article 2.

## Role Ambiguity
Two developers independently implement the same module. Neither is at fault; the missing
mechanism is a written ownership map.
**Fix:** RACI. One owner per component.

## Blame Culture
A developer hesitates to report a critical defect because the team assigns blame. Now defects go
unreported, which is strictly worse than the defect.
**Fix:** trust and respect are listed characteristics of an effective team. Never attach
individual performance evaluation to defect data.

## Seniority as a Technical Argument
Two architects disagree; the more senior one wins. The decision may be right, but the mechanism
is wrong and will be wrong next time.
**Fix:** evaluate both alternatives objectively against agreed technical criteria.

## The Undocumented Domain Rule
A regulation applies, nobody checked, and it surfaces during acceptance testing when the
architecture cannot accommodate it.
**Fix:** phase 01 domain requirements, and G0 criterion 6.

## Licence Blindness
An open-source library with a restrictive licence is used in proprietary commercial software
without complying with the licensing obligations.
**Fix:** the dependency register. Article 8.

## Cargo-Cult Agile
Standups, sprints and retrospectives, with fixed scope, fixed date, no customer availability and
no process change from any retrospective. The ceremonies without the mechanism.
**Fix:** name what Agile is buying you here. If the answer is nothing, choose a different style
honestly.

## Plan-Driven by Default
Heavy documentation applied to a two-week experimental prototype because "that is how we do
things".
**Fix:** the four lessons. No single process fits all projects. Choose by project
characteristics, not by habit.

## Exaggerating Capability
Overstating system performance in a client demonstration despite benchmark evidence to the
contrary. Overstating the accuracy of an AI-assisted feature despite incomplete validation.
**Fix:** Article 2. Capabilities are stated with their evidence and their limits.
