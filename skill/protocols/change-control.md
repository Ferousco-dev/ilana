# PROTOCOL: CHANGE CONTROL

Requirements change. That is normal and expected. **Uncontrolled** change is not.

## The sequence

```
Submit -> Impact analysis -> Approve or reject -> Implement -> Test -> Document -> Close
```

The order is the protocol. Approving before analysing is the mechanism by which schedules die.

## 1. Submit

Anyone may raise a `CR`. Minimum content: what is being asked for, in the requester's own words;
why it is needed now; what breaks or is lost if it is not done.

## 2. Impact analysis

Performed by `configuration-engineer` with `analyst` and `architect`. **Mandatory before
approval.** Article 11.

| Dimension | Question |
| --- | --- |
| Requirements | which change, which are withdrawn, which conflict |
| Design | which `DES` elements are affected |
| Code | which modules, and how much of the change is in code the team is afraid to touch |
| Tests | which `TC` must be rewritten, which are new |
| Documentation | which documents fall out of date |
| Schedule | days, with a confidence level |
| Cost | |
| Risk | new `RSK` entries |

State confidence. An impact analysis with false precision is worse than one that says "between 3
and 10 days, because we have not touched that module in a year".

## 3. Approve or reject

Decided by the named approver in the SCM plan. **Rejection is a legitimate outcome and is
recorded with its reason.** A change log containing only approvals is a log of a process nobody is
running.

Three outcomes: approved, rejected, deferred. Deferred carries an owner and a date, or it is a
rejection wearing a kinder word.

## 4. Implement

The change is traced. Every commit references the `CR`. Article 3 still applies: the change must
trace to a requirement, and if the change *is* a new requirement, the SRS is updated.

## 5. Test

Corrective changes need a regression test proving the fault is gone.
Adaptive changes need environment-matrix testing.
Perfective changes need a before and an after metric.
Preventive changes need a stated hypothesis about the fault prevented.

## 6. Document

The SRS, the design description, the user documentation and the changelog. **The SRS is not a
historical document.** A system whose SRS describes an earlier version has no requirements
baseline at all.

## Emergency changes

Production is down; the fix goes straight in. That is often correct.

The failure is not writing the `CR` afterwards. Emergency changes get a retrospective change
request within one working day, with the emergency justification recorded, the impact analysis
performed after the fact, and any follow-up work identified.

## Scope creep

Scope creep is a process failure, not a personality trait. It happens when changes accumulate
without any of them individually passing through impact analysis.

Detection: compare the current work item list against the last approved baseline. More than one
unapproved item is a `conductor` escalation.

The Agile version of the same failure: "we're Agile so we just add things". Agile changes priority
within a controlled backlog. It does not abolish impact analysis.
