# Change Request

```
CR-###
Title:
Raised by:                          Date:
Type: corrective | adaptive | perfective | preventive
Affects: REQ-... / NFR-... / DOM-... / DES-... / TC-...

## 1. Description
What is being asked for, in the requester's words.

## 2. Justification
Why this is needed now. What breaks or is lost if it is not done.

## 3. Impact analysis                    (mandatory before approval, Article 11)
| Dimension | Impact | Estimate | Confidence |
|---|---|---|---|
| Requirements  | which change, which are withdrawn | | |
| Design        | which DES elements are affected | | |
| Code          | which modules | | |
| Tests         | which TCs must be rewritten or added | | |
| Documentation | which documents | | |
| Schedule      | days | | |
| Cost          | | | |
| Risk          | new RSK entries | | |

## 4. Alternatives considered
Including "do nothing", and what "do nothing" costs.

## 5. Disposition
Decision: approved | rejected | deferred
Decided by:                         Date:
Reason:

## 6. Implementation
Implemented in:  <commit / branch / release tag>
Verified by:     <TC ids>
Documentation updated: yes / no / n/a
Traceability updated:  yes / no
Closed on:
```

## Rules

1. **Impact analysis precedes approval.** Approving first and analysing after is the mechanism
   by which schedules die.
2. **Rejection is a legitimate outcome** and is recorded with its reason. A change log
   containing only approvals is a log of a process nobody is running.
3. **A change that touches a requirement touches the SRS.** The SRS is not a historical
   document.
4. **Emergency changes still get a CR**, written after the fact, within one working day, with
   the emergency justification recorded.
