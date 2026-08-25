# PROTOCOL: DEFECT LIFECYCLE

## States

```
New -> Assigned -> Open -> Fixed -> Retest -> Verified -> Closed
                                       |
                                    Reopened  (retest failed)

From any state: Deferred, Rejected
```

| State | Means | Who moves it |
| --- | --- | --- |
| New | recorded, not yet triaged | reporter |
| Assigned | triaged, owner set | triage |
| Open | owner is working it | owner |
| Fixed | a fix exists in a build | owner |
| Retest | awaiting verification | verifier |
| Verified | the fix is confirmed | verifier |
| Closed | verified and a regression test exists | verifier |
| Reopened | retest failed | verifier |
| Deferred | real, but not now, with an owner and a date | triage |
| Rejected | not a defect, with a reason | triage |

## Raising

All nine fields, always: Defect ID, Title, Description, Severity, Priority, Steps to Reproduce,
Expected Result, Actual Result, Status.

Plus, from Ìlànà: found-during (which level), related requirement, reproduction rate, environment,
evidence path.

A defect without steps to reproduce is a rumour. If it cannot be reproduced, say so explicitly and
record what was tried; intermittent defects are real and must not be rejected for being hard.

## Triage

Set severity and priority **independently**. They are different questions.

| | Severity asks | Priority asks |
| --- | --- | --- |
| | how badly does the system misbehave? | how soon must it be fixed? |
| Owned by | technical judgement | business judgement |

A cosmetic typo on the payment page: low severity, urgent priority.
A data corruption bug in an unused legacy import: critical severity, low priority.

Cadence: at `RIGOUR` 3 and above, triage runs on a defined schedule. Untriaged defects accumulate
into a backlog nobody reads.

## Fixing

1. Reproduce it first. A fix for a defect you could not reproduce is a guess.
2. Find the root cause, not the symptom.
3. **Write the failing test before the fix.** It must fail without the fix and pass with it.
4. Categorise the root cause by phase. That distribution is the process-leak signal.
5. Check whether the same root cause exists elsewhere in the codebase.

## Closing

**A defect may not be closed without a named regression test case.**

This one rule prevents more recurrence than any amount of coverage. Ìlànà enforces it at G5.

## Root cause categories

| Category | The leak is in |
| --- | --- |
| Requirement missing or wrong | phase 01 |
| Design flaw | phase 02 |
| Interface or usability flaw | phase 03 |
| Coding error | phase 04 |
| Test gap | phase 05 |
| Configuration or environment | phase 06 |
| Third-party dependency | phase 10 |
| Communication or handoff failure | phase 11 |

The last category is real and under-used. When two components disagree about a data type because
their owners never spoke, the root cause is not "coding error".

## Flaky defects

A test that fails intermittently is a defect with a severity and an owner. Quarantine it out of the
blocking suite within one day; fix or delete it within an agreed window. Never leave it failing
intermittently, because it teaches the whole team to ignore red, and that habit is what lets a
real failure through.

## Never

- Close a defect to make a report look better.
- Reject a defect because it is hard to reproduce.
- Attach defect counts to individual performance evaluation. Do that once and defect data stops
  being true, which costs far more than any individual's performance.
