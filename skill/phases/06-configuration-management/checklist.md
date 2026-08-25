# PHASE 06 CHECKLIST

## Configuration identification
- [ ] All configuration items identified: source, docs, tests, requirements, design, infrastructure, pipeline, migrations
- [ ] Nothing important exists only on a developer machine
- [ ] `.ilana/` is committed

## Version control
- [ ] Branching strategy documented in `docs/scm-plan.md`
- [ ] Main branch protected (RIGOUR 2+)
- [ ] Commit messages state why, not just what
- [ ] No secrets in the working tree
- [ ] No secrets in the history
- [ ] Release commits are tagged

## Change management
- [ ] Every change traces to a `CR-###` or a `REQ-###`
- [ ] Impact analysis performed before approval, not after
- [ ] Rejections recorded with reasons
- [ ] Change type classified: corrective, adaptive, perfective, preventive
- [ ] Affected documents updated with the change

## Build
- [ ] Build is automated
- [ ] Build is reproducible from a tagged commit
- [ ] Dependencies are pinned or locked
- [ ] CI runs build, tests, lint, and security scan
- [ ] Build artifacts are versioned and stored

## Release
- [ ] Release type classified: major, minor, patch, emergency
- [ ] `CHANGELOG` entry written and human-readable
- [ ] Rollback plan exists
- [ ] Rollback has been rehearsed at least once, with a date
- [ ] Post-release monitoring defined: what is watched, by whom, threshold
- [ ] Deployment environments reproducible from source
- [ ] Release authorised by a named person (RIGOUR 4+)
