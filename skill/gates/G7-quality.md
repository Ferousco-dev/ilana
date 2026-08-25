# G7 - QUALITY SIGN-OFF

Owner: `quality-auditor`. Closes: phase 07. Opens: phase 08 Process assessment.

Distinct from G5. G5 asked "did the tests pass". G7 asks "was quality *assured*", which is a
process question, not a product question.

## Criteria

| # | Criterion | Rigour | Evidence |
|---|---|---|---|
| 1 | A quality management plan exists and was written before construction began | R2+ | `docs/quality-plan.md`, dated |
| 2 | Reviews were performed on requirements, design and code, before execution testing | R2+ | review records |
| 3 | The seven quality attributes are assessed with evidence | R2+ | scorecard |
| 4 | At least one product, one process and one project metric are recorded | R3+ | `.ilana/metrics.csv` |
| 5 | An audit of process compliance was performed by someone not on the delivery team | R3+ | `docs/audit-report.md` |
| 6 | Review type matches the risk: walkthrough for low, inspection for high | R3+ | review records name the type |
| 7 | Inspections carried defined roles: Moderator, Reader, Recorder | R4+ | inspection record with names |
| 8 | Defect data is analysed for cause, not just counted | R4+ | cause categories with counts |
| 9 | Standards compliance demonstrated against a named standard | R4+ | ISO/IEC 12207, IEEE 829/830/1016 mapping |
| 10 | Independent quality assurance function with authority to stop a release | R5 | organisational evidence |

## The seven quality attributes

Score each on evidence, not on impression. Absent evidence, mark `UNVERIFIED`, never `good`.

| Attribute | The question | Typical evidence |
| --- | --- | --- |
| Correctness | Does it do exactly what the requirements say? | requirement-to-test traceability, all green |
| Reliability | Does it work every time under normal conditions? | uptime, mean time between failures, crash rate |
| Efficiency | Does it use CPU, memory and storage well? | profiling, resource ceilings under load |
| Usability | Can users learn and operate it? | task completion rate, time on task, support ticket themes |
| Maintainability | Can it be modified safely? | complexity, coupling, mean time to implement a change |
| Portability | Does it run elsewhere with minimal change? | platform matrix run in CI |
| Security | Is data protected from unauthorised access? | scan results, authentication and authorisation model, encryption at rest and in transit |

## Review, walkthrough, inspection, audit

The four are not interchangeable, and G7 fails if the record calls something an inspection
that was actually a walkthrough.

| Activity | Led by | Formality | Roles | Purpose |
| --- | --- | --- | --- | --- |
| Peer review | a peer | low | none fixed | catch obvious problems |
| Walkthrough | the author | informal | none fixed | explain logic, gather early feedback |
| Inspection | a Moderator | formal, strict procedure | Moderator, Reader, Recorder | detect defects systematically and early |
| Audit | independent personnel | formal | auditor | verify process and standards compliance |
