# PROTOCOL: RELEASE

## Pre-flight

Every box, before anything is deployed.

- [ ] Built from a **tagged** commit, not a branch
- [ ] CI green on that exact commit
- [ ] Test exit criteria met, or the shortfall accepted by a named person
- [ ] No open critical or high defects, or each is accepted by a named person
- [ ] Security scan clean or every finding individually triaged
- [ ] Every item in the release traces to a `CR` or a `REQ`
- [ ] Changelog written, in language a user can read
- [ ] Documentation updated
- [ ] **Rollback plan current and rehearsed**, with the rehearsal date
- [ ] Irreversible steps identified and flagged at the top of the release plan
- [ ] Monitoring configured for the new behaviour, with thresholds
- [ ] Support briefed on what changed
- [ ] Dependent teams notified
- [ ] Release type classified: major, minor, patch, emergency

## Go / no-go

At `RIGOUR` 3 and above this is a decision with more than one voice:

| Role | Provides |
| --- | --- |
| `release-manager` | readiness assessment and the recommendation |
| `quality-auditor` | quality evidence |
| `verifier` | test report and open defect position |
| operations | environment and capacity readiness |
| business owner | acceptance of any risk carried |

Every risk carried into production has a **named** accepter. Not "the team".

## Deploy

1. Announce the start.
2. Execute the steps in the release plan, in order, verifying each.
3. Watch the trigger conditions defined **before** the deploy started.
4. Do not improvise. If the plan is wrong, stop and revise it; do not extemporise under pressure.

## The point of no return

Every release plan names the step after which rollback is no longer possible, usually an
irreversible migration. Before that step, pause and confirm explicitly.

## Post-release

| Window | Watch |
| --- | --- |
| First 15 minutes | error rate, health checks, core flow synthetic checks |
| First hour | latency, throughput, queue depths |
| First 24 hours | business metrics, support ticket volume and themes |
| First week | the metric the change was supposed to move |

That last row is the one everyone skips. A perfective change with no after-measurement is a change
whose value was never established.

## Rollback

Trigger conditions were defined in advance. When one fires, roll back; do not debate. Debating
during an incident is how a five-minute outage becomes an hour.

After a rollback:
1. Restore service first, diagnose second.
2. Record the timeline.
3. Raise a defect for the cause.
4. Update the rollback plan with anything that did not work as documented.
5. Run `incident.md`.

## Emergency releases

Still take a version number. Still get a change request, retrospectively, within one working day.
Still get a rollback plan, even a rushed one. The pressure to skip these is exactly proportional to
how much they are needed.
