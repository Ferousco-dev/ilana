# Release Plan: <version>

| Field | Value |
| --- | --- |
| Version | |
| Type | major / minor / patch / emergency |
| Tag | |
| Built from commit | |
| Target date | |
| Release manager | |
| Authorised by | |

## 1. Contents

| Change | Type | Traces to | Verified by |
| --- | --- | --- | --- |
| | corrective / adaptive / perfective / preventive | CR-### / REQ-### | TC-### |

Every line traces. An item that traces to nothing does not ship.

## 2. Readiness

| # | Check | Status | Evidence |
| --- | --- | --- | --- |
| 1 | All tests green on the release commit | | CI run |
| 2 | Exit criteria from the test plan met | | test report |
| 3 | No open critical or high defects | | defect log |
| 4 | Security scan clean or triaged | | scan output |
| 5 | Changelog written | | `CHANGELOG.md` |
| 6 | Documentation updated | | |
| 7 | Rollback plan current and rehearsed | | `docs/rollback.md`, rehearsal date |
| 8 | Monitoring and alerts configured for new behaviour | | |
| 9 | Dependent teams notified | | |
| 10 | Support briefed on what changed | | |

## 3. Deployment

| Step | Action | Owner | Duration | Verification | If it fails |
| --- | --- | --- | --- | --- | --- |
| 1 | | | | | |

Include database migrations explicitly, with their reversibility stated. An irreversible
migration changes the rollback plan fundamentally and must be flagged here.

## 4. Post-release monitoring

| Metric | Baseline | Alert threshold | Watched by | For how long |
| --- | --- | --- | --- | --- |
| Error rate | | | | 24h |
| Latency p95 | | | | 24h |
| Throughput | | | | 24h |
| Business metric | | | | 7d |

## 5. Go / no-go

| Role | Name | Decision | Date |
| --- | --- | --- | --- |
| Release manager | | | |
| Quality | | | |
| Operations | | | |
| Business owner | | | |

Recorded risks carried into production, and who accepted each one:

| Risk | Accepted by | Mitigation in place |
| --- | --- | --- |
