# CI/CD Pipeline Definition

The pipeline is the enforcement surface. Whatever the standards documents say, what the pipeline
blocks is what actually holds.

## Stage order

Cheapest and fastest checks first, so failures surface in seconds rather than minutes.

| # | Stage | Blocks merge | Typical duration | Fails when |
| --- | --- | --- | --- | --- |
| 1 | Format check | yes | seconds | formatter would change files |
| 2 | Lint | yes | seconds | coding standard violated |
| 3 | Secret scan | yes | seconds | a credential pattern is detected |
| 4 | Build | yes | | compilation fails |
| 5 | Unit tests | yes | under 60s | any test fails |
| 6 | Integration tests | yes | under 5 min | any boundary test fails |
| 7 | Static analysis | yes | | complexity or quality threshold exceeded |
| 8 | Dependency and vulnerability scan | yes above low severity | | a known advisory affects a used version |
| 9 | Coverage check | warn or block per rigour | | below the threshold in the quality plan |
| 10 | Package | yes | | artifact cannot be produced |
| 11 | Deploy to staging | on main only | | deployment fails |
| 12 | Smoke test | on main only | | a core flow fails in staging |
| 13 | End-to-end suite | post-merge, nightly | | |

## Example: GitHub Actions skeleton

```yaml
name: pipeline

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0          # secret scanning needs history
      - name: Format check
        run: make fmt-check
      - name: Lint
        run: make lint
      - name: Secret scan
        run: make secret-scan
      - name: Build
        run: make build
      - name: Unit tests
        run: make test-unit
      - name: Integration tests
        run: make test-integration
      - name: Static analysis
        run: make analyse
      - name: Dependency audit
        run: make audit
```

## Rules

1. **The pipeline is defined as code, in the repository.** A pipeline configured through a web
   interface is not under configuration management.
2. **Required checks on the protected branch.** A pipeline that runs but does not block is a
   report, not a control.
3. **Budget the runtime.** If people stop waiting for it, it has failed regardless of what it
   checks.
4. **No secrets in logs.** Mask them, and verify the masking.
5. **Least privilege.** The pipeline's token gets the narrowest permission set that works.
6. **Deterministic builds.** Pin versions. A pipeline that passes today and fails tomorrow with
   no code change destroys trust in the whole apparatus.
7. **Suppressions expire.** Every suppressed finding carries a justification and an expiry date.

## Deployment

| Environment | Trigger | Approval | Rollback |
| --- | --- | --- | --- |
| Staging | merge to main | none | redeploy previous tag |
| Production | tag push | named approver (RIGOUR 4+) | see `docs/rollback.md` |

## Pipeline metrics

Feed these to `metrologist` at phase 08.

| Metric | Why it matters |
| --- | --- |
| Pipeline duration (median, p95) | determines whether people wait for it |
| Failure rate by stage | shows where the real defects are caught |
| Flaky failure rate | erodes trust in the whole pipeline |
| Time from merge to production | the core delivery cycle time |
| Deployment failure rate | the honest measure of release quality |
