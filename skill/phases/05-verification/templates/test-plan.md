# Test Plan: <SYSTEM>

Structure aligned with IEEE 829.

| Field | Value |
| --- | --- |
| Document ID | TP-<project>-v<n> |
| Written on | (must predate test execution) |
| Author | |
| Approved by | |
| Baselined SRS | SRS-<project>-v<n> |

---

## 1. Test objectives
What this testing effort intends to achieve. Not "find bugs"; the specific risks it retires.

## 2. Scope

### 2.1 Features to be tested
| Feature | Requirements | Level(s) | Priority |
| --- | --- | --- | --- |

### 2.2 Features NOT to be tested
| Feature | Why not | Risk accepted | Accepted by |
| --- | --- | --- | --- |

This section is mandatory. A test plan without it is claiming complete coverage.

## 3. Test strategy

| Level | In scope | Technique | Tools | Owner | Entry criteria | Exit criteria |
| --- | --- | --- | --- | --- | --- | --- |
| Unit | | | | developers | code compiles | all pass, coverage target met |
| Integration | | top-down / bottom-up / big bang | | | units pass | all boundaries exercised |
| System | | functional, performance, security, usability, stress | | independent testers | integration passes | SRS covered |
| Acceptance | | UAT / alpha / beta | | users, clients | system passes | business sign-off |

## 4. Test environment

| Element | Test | Production | Difference | Blind spot created |
| --- | --- | --- | --- | --- |

The last two columns are the point of this section. Every difference is a class of defect you
will not find here.

### 4.1 Test data
Source, volume, refresh policy. **No real personal, medical or financial data.** State how the
data is synthesised or anonymised.

## 5. Roles and responsibilities

| Role | Person | Responsibility |
| --- | --- | --- |
| Test lead | | plan, report, exit decision |
| Developer | | unit and integration tests |
| Independent tester | | system testing |
| Acceptance tester | | acceptance, must not be a developer |
| Defect triage | | severity and priority assignment |

## 6. Risk analysis

| ID | Risk | Likelihood | Impact | Mitigation | Owner |
| --- | --- | --- | --- | --- | --- |
| RSK-01 | acceptance testers unavailable before the release date | | | schedule UAT window now, in writing | |
| RSK-02 | test environment diverges from production | | | infrastructure as code for both | |

## 7. Schedule

| Milestone | Date | Depends on |
| --- | --- | --- |

## 8. Deliverables

- Test cases (`docs/test-cases.md` or the suite itself)
- Test execution report (`docs/test-report.md`)
- Defect log (`.ilana/defects.md`)
- Traceability matrix update
- Exit criteria evidence

## 9. Exit criteria

Objective and checkable. This is the most important section in the document.

| # | Criterion | Target | Actual | Met |
| --- | --- | --- | --- | --- |
| 1 | Requirements covered by at least one passing test | 100% | | |
| 2 | Open defects, severity critical | 0 | | |
| 3 | Open defects, severity high | 0 | | |
| 4 | Unit test pass rate | 100% | | |
| 5 | Regression suite green | yes | | |
| 6 | Performance NFR met under stated load | yes | | |
| 7 | Acceptance sign-off obtained | yes | | |

"We ran out of time" is not an exit criterion. If testing stops short, the shortfall is recorded
against these rows and accepted by a named person.

## 10. Suspension and resumption

What stops testing (for example, a build that fails smoke tests) and what must be true to resume.
