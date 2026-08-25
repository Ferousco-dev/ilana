# Rollback Plan: <version>

A rollback plan that has never been executed is a hypothesis. This template forces the
rehearsal record.

| Field | Value |
| --- | --- |
| Applies to release | |
| Last rehearsed on | (mandatory; "never" is a G6 failure at RIGOUR 2+) |
| Rehearsed by | |
| Estimated time to roll back | |
| Point of no return | the step after which rollback is no longer possible |

## 1. Trigger conditions

Roll back automatically or immediately when any of these hold. Decide these **before** the
deploy, when nobody is panicking.

| # | Condition | Threshold | Detected by |
| --- | --- | --- | --- |
| 1 | Error rate above baseline | | monitoring alert |
| 2 | p95 latency above | | monitoring alert |
| 3 | Any data integrity error | any occurrence | alert |
| 4 | Core business flow failing | | synthetic check |

## 2. Rollback procedure

| Step | Action | Command / mechanism | Owner | Verification |
| --- | --- | --- | --- | --- |
| 1 | Stop the rollout | | | |
| 2 | Redeploy previous tag | `deploy v<previous>` | | health check green |
| 3 | Reverse migration (if reversible) | | | data spot check |
| 4 | Invalidate caches | | | |
| 5 | Confirm core flows | | | synthetic check |
| 6 | Notify | | | |

## 3. Irreversible elements

| Element | Why irreversible | Compensating control |
| --- | --- | --- |
| e.g. a destructive column drop | data is gone | pre-deploy backup, restore procedure, tested |

If anything in the release is irreversible, say so at the top of the release plan. Teams
routinely assume rollback is always possible, and that assumption is where the worst outages
come from.

## 4. Data considerations

- Was a backup taken immediately before deployment? Where is it? Has restore been tested?
- Do rolled-back application versions tolerate data written by the new version?
- What happens to in-flight transactions?

## 5. Rehearsal record

| Date | Environment | Performed by | Time taken | Issues found | Plan updated |
| --- | --- | --- | --- | --- | --- |

Re-rehearse whenever the architecture, the data model, or the deployment mechanism changes.
