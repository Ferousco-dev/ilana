# PHASE 01 ANTI-PATTERNS

## The Solution Disguised as a Requirement
"We need a Kafka queue." That is a design decision wearing a requirement's clothes.
**Fix:** ask "what does that let a user do that they cannot do now?" until you reach a `REQ`.

## The Unmeasurable Adjective
"Fast", "secure", "user-friendly", "scalable", "robust", "intuitive", "seamless".
**Why it is fatal:** it cannot be tested, so it cannot be verified, so it will be argued about
at acceptance instead of at specification, when arguing is 50 times more expensive.
**Fix:** number and unit, or move it to the goals section and stop calling it a requirement.

## The Requirement Written by the Developer
The person who will build it also invents what it should do, then validates it themselves.
**Fix:** every requirement carries a `source` that is a human other than the author.

## The Missing Domain Requirement
Nobody asked which regulator applies, so PCI-DSS or a privacy regime surfaces during
acceptance testing, when the architecture is already wrong for it.
**Fix:** G1 criterion 10. Name the regulator you checked, even if the answer is "none applies".

## The Happy Path Only
Every requirement describes success. Nothing describes what happens when the payment gateway
times out, the disk is full, or the user closes the tab mid-transaction.
**Fix:** one explicit failure-path pass over every functional requirement before G1.

## Requirements as a One-Time Event
The SRS is written in week one and never touched again while the product diverges from it.
**Fix:** requirements management is the fifth stage, not an epilogue. Every `CR` updates the SRS.

## Scope Creep Rebranded as Agility
"We're Agile, so we just add things." Agile changes priority within a controlled backlog; it
does not abolish impact analysis.
**Fix:** Article 11. Every change is a `CR` with an impact analysis, even in a two-week sprint.

## The Silent Assumption
"Obviously it's single-tenant." Nobody wrote that down. Eighteen months later a customer asks
for tenant isolation and the data model cannot do it.
**Fix:** assumptions are `DEC-###` entries, visible in the SRS, not implicit in someone's head.

## Consensus by Exhaustion
The workshop runs long, the loudest stakeholder wins, and the quiet one whose department will
actually use the system never speaks.
**Fix:** structured elicitation. Written follow-up to every participant individually.
