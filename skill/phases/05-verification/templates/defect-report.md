# Defect Report

```
DEF-###
Title:                (one line, specific: not "login broken")

Reported by:                        Date:
Found in:             version / build / commit
Found during:         unit | integration | system | acceptance | production | review
Component:            DES-### / module path
Related requirement:  REQ-### / NFR-###

Severity:  critical | high | medium | low        (technical impact)
Priority:  urgent | high | medium | low          (business urgency)

Description:
  What is wrong, in enough detail that someone who has never seen the system
  can understand the problem.

Steps to reproduce:
  1.
  2.
  3.
  Reproduction rate:  always | intermittent (n of m) | once

Expected result:
Actual result:
Evidence:             log excerpt, screenshot path, stack trace path

Environment:
  OS / browser / runtime / data set / configuration

Workaround:           none | <description>

Assigned to:                        Status: New
Fixed in:             commit / build
Root cause:           (filled at fix time, categorised)
Regression test:      TC-###            <-- mandatory before Closed
Verified by:                        Date:
Closed on:
```

## Severity scale

| Severity | Meaning |
| --- | --- |
| Critical | data loss, data corruption, security breach, system unusable, no workaround |
| High | major function unusable, significant workaround required |
| Medium | function impaired, reasonable workaround exists |
| Low | cosmetic, minor inconvenience, no functional impact |

## Priority scale

| Priority | Meaning |
| --- | --- |
| Urgent | fix now, block the release |
| High | fix in this release |
| Medium | fix in a coming release |
| Low | fix if convenient |

Severity and priority are independent. A cosmetic error on the payment page can be low severity
and urgent priority. Setting them from one field destroys the ability to triage.

## Root cause categories

Categorise every fixed defect. The distribution is the input `metrologist` needs at phase 08 to
tell you where your process is leaking.

| Category | Means the leak is in |
| --- | --- |
| Requirement missing or wrong | phase 01 |
| Design flaw | phase 02 |
| Interface or usability flaw | phase 03 |
| Coding error | phase 04 |
| Test gap (should have been caught earlier) | phase 05 |
| Configuration or environment | phase 06 |
| Third-party dependency | phase 10 |
| Communication or handoff failure | phase 11 |

## Lifecycle

```
New -> Assigned -> Open -> Fixed -> Retest -> Verified -> Closed
                                       |
                                    Reopened (retest failed)
Alternatives from any state: Deferred, Rejected
```

**A defect may not move to Closed without a named regression test case.**
