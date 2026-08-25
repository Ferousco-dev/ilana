# G5 - VERIFICATION COMPLETE

Owner: `verifier`. Closes: phase 05. Opens: phase 06 Configuration management.

## Criteria

| # | Criterion | Rigour | Evidence |
|---|---|---|---|
| 1 | A test plan exists with objectives, scope, strategy, environment, roles, risks, schedule, deliverables and exit criteria | R1+ | `docs/test-plan.md` |
| 2 | Unit tests exist and pass | R1+ | runner output, counts |
| 3 | Every `REQ` and every `NFR` maps to at least one `TC` | R1+ | traceability, no untested requirement |
| 4 | Integration tests cover every module boundary | R2+ | boundary list vs test list |
| 5 | System testing performed against the SRS as a whole | R2+ | system test report |
| 6 | Defects recorded with the full report fields and a lifecycle state | R2+ | `.ilana/defects.md` |
| 7 | Exit criteria met, or the shortfall is explicit | R2+ | criteria table with actuals |
| 8 | Regression suite runs automatically on every change | R3+ | CI config |
| 9 | Non-functional testing performed: performance, security, usability, stress | R3+ | one report per applicable NFR |
| 10 | Acceptance testing signed by a user or client, not by the development team | R3+ | dated sign-off |
| 11 | Independent test team, separate from the developers | R4+ | named |
| 12 | Alpha and Beta cycles completed | R4+ | dated |
| 13 | Full traceability from requirement to test to result, auditable | R5 | matrix export |
| 14 | No open defects of severity high or critical | R5 | defect log |

## The four levels, and the trap

```
Acceptance   few tests    does it satisfy the business?        users, clients
System       some         does the whole thing meet the SRS?   independent testers
Integration  more         do the modules talk correctly?       developers or testers
Unit         many         is each component correct alone?     developers
```

The trap: a project with 90% unit coverage and no integration level is not well tested. Unit
tests cannot find interface defects, and interface defects between components are the classic
integration failure. Coverage is a product metric, not a substitute for having all four levels.

## Defect report fields

Every defect carries all nine, per the source material:

`Defect ID`, `Title`, `Description`, `Severity`, `Priority`, `Steps to Reproduce`,
`Expected Result`, `Actual Result`, `Status`.

Lifecycle: New -> Assigned -> Open -> Fixed -> Retest -> Verified -> Closed.
Alternatives: Reopened, Deferred, Rejected.

A defect closed without a regression test case is a defect that will come back.
