# PHASE 10 CHECKLIST

## Selection
- [ ] Every tool has a recorded reason for being chosen
- [ ] At least one alternative was considered for each significant tool
- [ ] Licence and cost recorded
- [ ] Lock-in and exit path considered
- [ ] Training need identified

## Version control
- [ ] Repository hosting chosen and access controlled
- [ ] Branch protection configured
- [ ] Secret scanning enabled

## CI/CD
- [ ] Pipeline defined as code, in the repository
- [ ] Stages ordered so the cheapest check fails first
- [ ] Lint, build, unit, integration, static analysis, security scan all present
- [ ] Pipeline blocks merge on failure (RIGOUR 3+)
- [ ] Pipeline runtime is short enough that people wait for it
- [ ] Deployment is automated, not manual

## Project management
- [ ] Board or tracker chosen and configured to the actual workflow, not the tool default
- [ ] Workflow states match reality
- [ ] Everyone updates it, and staleness is visible
- [ ] Reporting supports a decision someone actually makes

## Defect tracking
- [ ] Tracker supports all nine defect report fields
- [ ] Severity and priority are separate fields
- [ ] Lifecycle states match the defect life cycle
- [ ] Defects link to requirements and to test cases

## Documentation tooling
- [ ] Documentation lives in the repository, diffable
- [ ] Generated documentation (API, code) is produced by the pipeline, not by hand

## Health
- [ ] No tool in the chain is unmaintained by its vendor or community
- [ ] Every tool has a named owner inside the team
- [ ] Tools that nobody uses have been removed
