# Quality Management Plan: <PROJECT>

| Field | Value |
| --- | --- |
| Document ID | QMP-<project>-v<n> |
| **Written on** | (must predate construction; G7 checks this) |
| Author | |
| Approved by | |
| Rigour | |

---

## 1. What quality means for this project

Not a definition of quality in general. What "good enough to ship" means **here**, as numbers.

| Attribute | Objective | Threshold | How measured | Verified at |
| --- | --- | --- | --- | --- |
| Correctness | every requirement verified | 100% of REQ with a passing test | traceability matrix | G5 |
| Reliability | | e.g. 99.9% monthly availability | monitoring | post-release |
| Efficiency | | e.g. p95 under 2s at 500 concurrent | load test | G5 |
| Usability | | e.g. new user completes primary task in under 3 min | usability session | G3 |
| Maintainability | | e.g. complexity ceiling, review turnaround | static analysis | G4 |
| Portability | | e.g. passes on Linux and macOS, Chrome and Firefox | CI matrix | G5 |
| Security | | e.g. no high findings unresolved | scan and review | G4, G6 |

## 2. Standards applied

| Standard | Scope | How compliance is demonstrated |
| --- | --- | --- |
| IEEE 830 | requirements specification | SRS structure |
| IEEE 1016 | design description | SDD structure |
| IEEE 829 | test documentation | test plan structure |
| ISO/IEC 12207 | lifecycle processes | process map |
| ISO/IEC 25010 | quality model | attribute definitions |
| Organisational coding standard | construction | `docs/coding-standard.md` |

## 3. Review programme

| Artifact | Review type | When | Participants | Roles (if inspection) |
| --- | --- | --- | --- | --- |
| SRS | inspection | before G1 | | Moderator, Reader, Recorder |
| Design | inspection | before G2 | | Moderator, Reader, Recorder |
| Interface spec | walkthrough | before G3 | | |
| Code | peer review | every change | | |
| Test plan | walkthrough | before execution | | |
| Release | inspection | before G6 | | Moderator, Reader, Recorder |

Choose by risk. High-risk artifacts get inspections; low-risk ones get walkthroughs. Record which
was actually performed.

## 4. Audit programme

| Audit | Scope | Auditor (independent) | When | Output |
| --- | --- | --- | --- | --- |
| Process compliance | standards adherence, documentation completeness | | before G7 | `docs/audit-report.md` |

## 5. Metrics programme

| Metric | Category | Collected how | Frequency | Decision it informs |
| --- | --- | --- | --- | --- |
| Defect density | product | defects / KLOC | per release | whether to add review depth |
| Defect rate | process | defects found per week | weekly | whether quality is degrading |
| Process cycle time | process | task start to finish | per task | where the workflow stalls |
| Cost variance | project | planned minus actual | per milestone | budget correction |
| Schedule adherence | project | planned vs actual dates | per milestone | replanning |
| Review finding rate | process | findings per review | per review | whether reviews are real |

The last column is mandatory. A metric that informs no decision is deleted from this plan.

## 6. Defect management

| Aspect | Policy |
| --- | --- |
| Severity scale | critical, high, medium, low (defined in the defect template) |
| Priority scale | urgent, high, medium, low |
| Triage cadence | |
| Closure rule | no defect closes without a named regression test |
| Root cause categorisation | mandatory; categories map to phases |

## 7. Tools

| Purpose | Tool |
| --- | --- |
| Defect tracking | Jira / Bugzilla / Redmine / MantisBT / Azure DevOps |
| Static analysis | |
| Security scanning | |
| Test automation | |
| Coverage | |
| CI | Jenkins / GitHub Actions / GitLab CI |

## 8. Roles and authority

| Role | Person | Authority |
| --- | --- | --- |
| Quality lead | | may block a release |
| Independent auditor | | reports outside the delivery line |
| Moderator (inspections) | | |
| Ethics officer | | may halt on public interest grounds |

## 9. Records

What is kept, where, and for how long. In regulated contexts this section is the difference
between passing and failing an external audit.
