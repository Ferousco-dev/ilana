# Communication Plan

Poor communication during requirements gathering produces incorrect requirements that affect the
whole project. Poor coordination during testing leaves defects unresolved. Poor synchronisation
during deployment produces failures and downtime. This plan exists because those are engineering
failures with engineering fixes.

## 1. Channels

| Purpose | Channel | Participants | Cadence | Written record |
| --- | --- | --- | --- | --- |
| Requirements clarification | | analyst, stakeholder | as needed | yes, always |
| Daily synchronisation | | delivery team | daily | decisions only |
| Design decisions | | architect, developers, data owner | per decision | ADR |
| Defect reporting | tracker | anyone | continuous | yes |
| Escalation | | | as needed | yes |
| Release coordination | | delivery, operations, support | per release | yes |
| Incident | | on-call, operations, support | during incident | yes, timeline |
| Stakeholder status | | | weekly or per milestone | yes |

## 2. The written-first rule

Anything that changes what gets built is written down, in a place the whole team can find, before
it is acted on. Verbal agreement is fine for reaching the decision; it is not a record of it.

This applies with full force to distributed and asynchronous teams, where verbal context is not
shared by default.

## 3. Requirements confirmation loop

The specific mechanism that prevents the most expensive class of defect:

1. Stakeholder states the need.
2. Analyst writes it as a requirement with an acceptance criterion.
3. Analyst reads it back to the stakeholder.
4. Stakeholder confirms, in writing, with a date.
5. It enters the SRS.

Step 3 is the one teams skip, and it is the one that catches the misunderstanding.

## 4. Escalation path

| Situation | First | Then | Then |
| --- | --- | --- | --- |
| Technical disagreement | between the engineers, on agreed criteria | architect | conductor |
| Requirement conflict between stakeholders | facilitated session | product owner or sponsor | |
| Quality concern | quality-auditor | conductor | sponsor |
| Safety or ethics concern | ethics-officer | halt, then the user | |
| Blocked over 1 day | owner raises it | conductor | |

An escalation path that exists but nobody knows is the same as no escalation path. State where it
is documented and confirm the team has read it.

## 5. Handoff protocol between phases

Every phase transition emits an explicit handoff (see `kernel/KERNEL.md` section 4) naming what
was produced, the ID range, what remains open, and what was assumed. Silent handoffs are how open
conflicts get inherited and forgotten.

## 6. Meeting discipline

| Meeting | Purpose | Length | Output |
| --- | --- | --- | --- |
| Daily synchronisation | surface impediments | 15 min | impediment list |
| Design review | evaluate alternatives objectively | 60 min | ADR |
| Inspection | detect defects | max 2 hours | findings log |
| Retrospective | one process change | 60 min | one change with an owner |

A meeting with no output artifact did not need to be a meeting.

## 7. Conflict management

Open discussion to identify the root cause. Negotiation to find a fair compromise. Respectful
resolution that preserves the working relationship.

For technical disagreements specifically: agree the evaluation criteria **before** evaluating the
options. Deciding criteria after seeing the options is how seniority wins arguments that
evidence should have decided.
