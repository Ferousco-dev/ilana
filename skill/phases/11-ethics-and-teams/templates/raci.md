# RACI: Roles and Responsibilities

The single cheapest fix for the most common team failure: two people building the same thing, or
nobody building a thing everyone assumed was covered.

**R** Responsible (does the work) - **A** Accountable (answers for it, exactly one per row)
**C** Consulted (input sought before) - **I** Informed (told after)

## Decisions and activities

| Activity | Project Manager | Business Analyst | Architect | Developer | Tester / QA | DevOps | Ethics |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Elicit requirements | A | R | C | I | C | I | I |
| Approve requirements baseline | A | R | C | I | C | I | C |
| Architecture decisions | I | C | A/R | C | I | C | I |
| Data model | I | C | A | R | I | C | C |
| Interface design | I | C | C | R | C | I | I |
| Coding standard | I | I | C | A/R | C | C | I |
| Code review | I | I | C | A/R | I | I | I |
| Test plan | C | C | I | C | A/R | I | I |
| Acceptance testing | C | R | I | I | C | I | I |
| Branching strategy | I | I | C | C | I | A/R | I |
| Change approval | A | R | C | C | C | C | C |
| Release go/no-go | A | C | C | C | R | R | C |
| Rollback decision | A | I | C | C | C | R | I |
| Ethics halt | I | I | I | I | I | I | A/R |
| Process improvement | A | C | C | C | C | C | C |

## Rules

1. **Exactly one A per row.** Two accountable people means nobody is accountable.
2. **A may also be R.** That is normal on small teams.
3. **Minimise C.** Every consulted person is a delay. Consult those whose objection would change
   the decision.
4. **I is not a courtesy.** Informing someone who will act on the information is real; informing
   everyone about everything is noise that trains people to ignore updates.

## Component ownership

Separate from activity RACI, and equally important. This is the table that prevents duplicate
implementation.

| Component / module | Owner | Backup | Documentation |
| --- | --- | --- | --- |

Every component has exactly one owner. Unowned components rot; jointly-owned components rot
faster.

## Small-team collapse

On a team of two or three, one person holds several roles. That is fine and normal. What is not
fine is leaving it implicit. Write it down:

| Person | Roles held | Conflict of interest | Mitigation |
| --- | --- | --- | --- |
| | developer + tester | cannot independently verify own work | acceptance testing by the client |
| | developer + release manager | no separation of duties on release | second pair of eyes on the go/no-go |

Naming the conflict is what lets you compensate for it.
