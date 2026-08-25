# WORKED EXAMPLE: LIBRARY MANAGEMENT SYSTEM

A complete `FLEET` run, compressed. This is what Ìlànà actually looks like in use.

The example is deliberately small enough to read and real enough to be useful. It is the system the
course itself uses for its practical exercises.

---

## Boot

```
Ìlànà v1.0.0 online. Kernel loaded. Awaiting mode selection.

No .ilana/ found. Cold start.

How should Ìlànà run this?
  [1] FLEET - a bundle of specialist agents, full gated lifecycle
  [2] TASK  - one specialist, one focused operation

Other modes: AUDIT, TUTOR, DOCTOR, DRILL.
```

> User: fleet. building a library management system for a department.

```
FLEET selected. Intake, seven questions, one batch:

1. Who uses this, and how often?
2. What is the single task it must make possible that is painful today?
3. Does it hold personal data about borrowers?
4. What must it explicitly NOT do?
5. Does anything already exist: a spreadsheet, a previous system?
6. Deadline, and what happens if it is missed?
7. Three months in, what number tells you it worked?
```

> User: librarians daily, students weekly. Today borrowing is a paper ledger and nobody knows
> where anything is. Yes, it holds student names and ID numbers. It should not handle fines
> payment, that stays at the bursary. There is a spreadsheet. Deadline is the start of next
> semester, and if we miss it we run on paper for another term. Success is knowing where every
> item is.

```
Rigour 3. It holds student personal data, so privacy obligations apply, but it is departmental
scale and a missed deadline is inconvenient rather than harmful. Gates enforce; overrides are
recorded.

Process style: hybrid. Requirements are mostly knowable up front (this is a well-understood
domain) but the librarians will change their minds once they see it.

ETH-001 logged: personal data of students. Data minimisation and access control are DOM
requirements, not optional features.

Writing .ilana/. Agents: analyst, architect, interaction-designer, constructor, verifier,
configuration-engineer, quality-auditor, metrologist, documentarian, ethics-officer,
release-manager, conductor. Twelve of thirteen. Proceed?
```

---

## Phase 01, and the first gate failure

```
[analyst] Phase 01. Elicitation: interviews with two librarians, document analysis of the
spreadsheet and the paper ledger, plus one scenario pass.

Produced docs/srs.md.
  REQ-001..REQ-019 functional
  NFR-001..NFR-006 non-functional
  DOM-001..DOM-003 domain

DOM-002 is the fine schedule. It is a departmental rule, not software, and it changes annually.
It is a requirement so it is written down, with its source.

[analyst] Attempting G1.
```

```
[conductor] G1 attempt 1  verdict: FAIL

| # | Criterion | Met | Evidence |
| 1 | unique stable IDs | yes | 28 rows in traceability.csv |
| 2 | all three types present | yes | 19 / 6 / 3 |
| 3 | no unmeasurable adjectives | NO | 3 hits |
| 4 | independently testable | NO | REQ-011 |
| 5 | out of scope written | yes | SRS 2.6 |
| 6 | NFRs quantified | NO | NFR-002, NFR-005 |
| 7 | validated with a stakeholder | yes | docs/reviews/2026-08-19.md |

Adjective scan:
  docs/srs.md:41   "the search should be fast"
  docs/srs.md:58   "the interface must be simple for librarians"
  docs/srs.md:72   "student records must be secure"

Remediate.
```

```
[analyst] Rewritten and confirmed with the head librarian.

  NFR-002  Search returns results within 1 second at the 95th percentile, over a catalogue
           of up to 50,000 items, on the department's existing hardware.
  NFR-005  A librarian who has not used the system before completes a borrow transaction
           within 90 seconds without consulting documentation.
  DOM-003  Student personal data is limited to name, matriculation number and department.
           No addresses, no contact details, no photographs. Access is restricted to
           library staff accounts. Records are deleted 12 months after graduation.

REQ-011 was "the system should handle reservations well". Split into REQ-011 (place a
reservation), REQ-020 (cancel a reservation), REQ-021 (notify when an item becomes available)
and REQ-022 (expire an unclaimed reservation after 48 hours).

REQ-022 did not exist before. Nobody had considered what happens to an unclaimed reservation.
That is what the testability criterion is for.
```

```
[conductor] G1 attempt 2  verdict: PASS
32 requirements. Advancing to phase 02. Handoff to architect.
```

The important thing in that exchange: the gate did not just catch three sloppy adjectives. Forcing
REQ-011 to be testable **discovered a missing requirement**, which is exactly the class of defect
that is cheapest to fix here and most expensive to fix after launch.

---

## Phase 02, and a design caught by the orphan check

```
[architect] Phase 02. Three levels done. docs/design.md, DES-001..DES-024.

NFR mechanism table:
| NFR-002 search under 1s | in-memory index rebuilt on catalogue change | DES-009 |
| NFR-005 90s to first borrow | single-screen borrow flow, barcode first | DES-014 |
| NFR-004 99% availability in opening hours | single node, nightly backup, documented restore | DES-002 |

ADR-001: single-node SQLite rather than a client-server database.
Rejected: PostgreSQL. Reason: 50,000 items and 6 concurrent staff do not need it, and the
department has nobody who operates a database server. Revisit trigger: if the catalogue exceeds
500,000 items or concurrent staff exceeds 25.

[architect] Attempting G2.
```

```
[conductor] G2 attempt 1  verdict: FAIL

Orphan check, design-to-requirement direction:
  DES-018 "email notification service" traces to no requirement.

REQ-021 says notify when a reserved item becomes available. It does not say by email. The
librarians said students do not read departmental email.

This is unrequested work. Article 3.
```

```
[analyst] Checked with the librarians. They want a notice printed at the desk and the student
told when they next visit. Email was the architect's assumption, not a requirement.

DES-018 withdrawn. REQ-021 clarified: notification is a desk-queue entry, visible to staff.
That is one screen, not a mail service.
```

```
[conductor] G2 attempt 2  verdict: PASS
Two weeks of work avoided by one check.
```

---

## Phase 05, and the coverage trap

```
[verifier] Phase 05. Test plan written 2026-08-21, before execution. Exit criteria set.

  unit         61 tests, 61 pass
  integration  14 tests, 14 pass
  system        6 scenarios, 6 pass
  acceptance    pending, scheduled with the head librarian Thursday

  coverage 78%
  Requirement coverage: 32/32 have at least one test.

Failure paths tested: 19 of 19 functional requirements have a negative case.
DEF-001 through DEF-007 raised during system testing. Six closed, each with a named
regression test. DEF-004 open, severity low, cosmetic label truncation.

[verifier] Attempting G5.
```

```
[conductor] G5 attempt 1  verdict: FAIL

Criterion 10: acceptance testing signed by a user or client, not by the development team.
Acceptance has not happened. It is scheduled, not done.

This is not a technicality. Acceptance is the only level that asks whether the system is fit
for the business, and the development team cannot answer that question on the librarians'
behalf.
```

> User: can we just proceed, the demo is Friday

```
[conductor] G5 OVERRIDE ACCEPTED

Unmet: criterion 10, acceptance testing.
Consequence here: you will demonstrate on Friday a system no librarian has used unsupervised.
The 90-second borrow target (NFR-005) is unverified, and that is the number your users will
judge this on.
Your reason (recorded): "demo Friday, UAT Thursday of the following week".
Recorded as OVERRIDE-001 in .ilana/gates/G5.md.

Advancing to phase 06. G6 will report this as a risk carried into release, with your name
against it.
```

Note what happened: Ìlànà did not argue, did not lecture, and did not pretend. It named the
specific consequence for this project, recorded the decision, and carried it forward so it appears
again at the release gate where it matters.

---

## Phase 06, and the rollback nobody had tried

```
[release-manager] G6 attempt 1  verdict: FAIL

Criterion 5: rollback plan exists and has been rehearsed. docs/rollback.md exists.
Last rehearsed: never.

Your release includes a migration that drops the old `borrower_name` column. That is
irreversible without the pre-deploy backup, and the backup restore has also never been tested.

If Friday's demo goes wrong you currently have no way back.
```

```
[configuration-engineer] Rehearsed on a copy of the spreadsheet import.
Restore took 4 minutes. Two problems found:

  1. the restore script assumed a path that only exists on the developer's machine
  2. the migration is not reversible, so the plan now says so at the top,
     and takes the backup automatically as step 0

docs/rollback.md updated. Rehearsal recorded 2026-08-24.
```

```
[conductor] G6 attempt 2  verdict: PASS with one risk carried.
Risk: acceptance testing outstanding (OVERRIDE-001), accepted by <named person>.
```

---

## Phase 08, closure

```
[metrologist] Metrics for this run.

  product   defect density        2.1 per KLOC     .ilana/defects.md + source scan
  process   defect rate           7 per week       .ilana/defects.md
  process   process cycle time    3.4 days median  git log
  project   schedule adherence    0.87             plan vs actual
  project   cost variance         UNVERIFIED       no budget was tracked

  Defect root cause distribution:
    phase 01 requirements   2   (both found at G1, before any code existed)
    phase 02 design         1   (DES-018, found by the orphan check)
    phase 04 construction   4
    phase 05 test gap       0

  Prevention ratio: 3 of 7 = 43%.
  No previous run. This is the baseline.
```

```
[conductor] G8. Retrospective.

What the process caught:
  - three unmeasurable requirements, before design
  - one missing requirement (REQ-022, unclaimed reservation expiry), discovered by the
    testability criterion
  - one unrequested subsystem (DES-018 email service), discovered by the orphan check
  - a rollback plan that did not work, discovered by being made to rehearse it

What the process missed:
  - four construction defects reached system testing. G4 has no static analysis step;
    two of the four would have been caught by one.

Where the process cost more than it returned:
  - the BPMN model of the borrowing workflow. Nobody read it. The activity diagram was
    enough at this scale. Trim at rigour 3.

One change for the next run:
  Add static analysis to the G4 criteria and to CI.
  Owner: configuration-engineer. Start: next sprint.
  Metric: construction-phase defects reaching system testing. Baseline 4. Target 2.
  Recheck: end of next release.

Run closed. Baseline recorded for comparison.
```

---

## What this run actually cost and bought

**Cost:** two gate failures at G1, one at G2, one at G5, one at G6. Perhaps a day and a half of
extra work spread across three weeks.

**Bought:**

- A missing requirement found before any code was written, rather than by a student whose
  reservation silently never expired.
- A subsystem not built at all.
- A rollback that works, discovered on a Tuesday afternoon rather than on a Friday evening.
- A baseline number, so the next run can be compared to this one instead of to a feeling.

**Not bought:** acceptance testing, which was overridden. That is recorded, with a name against it,
and it will be the first thing the next retrospective looks at.
