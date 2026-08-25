# PHASE 06 - SOFTWARE CONFIGURATION MANAGEMENT

Owner: `configuration-engineer`. Support: `release-manager`. Entry gate: G5. Exit gate: G6.

> Software Configuration Management is the process of systematically controlling changes made to
> software artifacts throughout the software lifecycle.

SCM is the phase that makes every other phase auditable. Without it you cannot answer "what
exactly is in production", "who changed this and why", or "how do we get back".

---

## What this phase produces

| Artifact | Path | Template |
| --- | --- | --- |
| SCM plan | `docs/scm-plan.md` | `templates/scm-plan.md` |
| Release plan | `docs/release-plan.md` | `templates/release-plan.md` |
| Rollback plan | `docs/rollback.md` | `templates/rollback-plan.md` |
| Change log | `CHANGELOG.md` | `templates/changelog.md` |
| Change requests | `.ilana/changes.md` | phase 01 `change-request.md` |

---

## What is under configuration control

Not just source code. The artifacts named in the course material:

- source code
- documentation
- test cases
- requirements
- design documents

Ìlànà adds, because modern systems need them: infrastructure definitions, CI pipeline
definitions, database migrations, configuration schemas, dependency lock files, and the
`.ilana/` ledger itself.

If it can differ between environments and change behaviour, it is a configuration item.

---

## Objectives of SCM

Maintain consistency, track changes, prevent conflicts, support team collaboration, maintain a
history of revisions, maintain integrity and traceability, ensure software integrity, manage
software changes, track versions.

---

## The four pillars

### 1. Version control

A version control system records changes to files over time so developers can track and manage
modifications.

| Type | Example | Structure |
| --- | --- | --- |
| Centralized | SVN | a single central repository |
| Distributed | Git | each developer has a full local repository |

**Git.** Key concepts: repository, commit, branch, merge, remote repository.
Features: distributed architecture, branching and merging, fast performance, collaboration
support, history tracking.
Benefits: supports collaboration, enables rollback, tracks project history, simplifies branching.

| Command | Function |
| --- | --- |
| `git init` | initialise repository |
| `git clone` | create a local copy of a remote repository |
| `git add` | stage changes for commit |
| `git commit` | create a snapshot of changes |
| `git push` | send local commits to remote |
| `git pull` | fetch and integrate remote changes |
| `git branch` | list, create or delete branches |
| `git merge` | merge branches |

Workflow: modify files in the working directory, stage with `git add`, commit with
`git commit`, push to remote, pull updates.

**Branching strategy** is a decision, not a default. Ìlànà requires it to be written down.

| Strategy | Fits | Cost |
| --- | --- | --- |
| Trunk-based with short-lived branches | continuous delivery, strong test suite | needs feature flags and fast CI |
| GitHub flow | web services, frequent deploys | assumes one production version |
| Git flow | versioned products with support branches | heavier, more merge overhead |
| Release branches | regulated or plan-driven contexts needing long-lived support | must backport fixes |

### 2. Change management

Change management is the process of handling modifications to software systems in a controlled
and systematic manner.

Objectives: minimise disruption, maintain stability, ensure traceability, evaluate change impact.

Process:
```
Change Request Submission -> Change Evaluation (impact analysis) -> Approval or Rejection
   -> Implementation -> Testing -> Documentation
```

**Types of software change:**

| Type | Definition | What it must be accompanied by |
| --- | --- | --- |
| Corrective | fixes a fault | a regression test proving the fault is gone |
| Adaptive | fits a changed environment | environment-matrix testing |
| Perfective | improves what already works | a before and after metric (Article 10) |
| Preventive | forestalls a future fault | a stated hypothesis about what is prevented |

### 3. Build management

Build management involves converting source code into executable software applications:
compilation, linking, packaging, dependency management, testing.

| Tool | Usage |
| --- | --- |
| Maven | Java projects |
| Gradle | build automation |
| Ant | Java builds |
| Make | C and C++ projects |

**Continuous Integration** automatically builds and tests software whenever code changes are
committed. Benefits: early bug detection, faster development, improved software quality.
Tools: Jenkins, GitHub Actions, GitLab CI/CD.

Ìlànà rule: the build must be reproducible from a tagged commit by a machine with no memory of
how it was done last time. If a human has to remember a step, that step is a defect.

### 4. Release management

Release management is the process of planning, scheduling and controlling software releases.

Objectives: deliver stable software, coordinate deployment, reduce deployment risks, ensure user
readiness.

Activities: release planning, build preparation, testing, deployment, monitoring, maintenance,
version labelling, deployment planning, documentation, rollback planning, post-release
monitoring.

| Release type | Description |
| --- | --- |
| Major | significant changes |
| Minor | small improvements |
| Patch | bug fixes |
| Emergency | critical fixes |

---

## The relationship between testing and SCM

| Testing | SCM |
| --- | --- |
| detects defects | controls changes |
| ensures functionality | maintains integrity |
| validates requirements | tracks versions |

Together they improve reliability, maintainability, collaboration and deployment success.
Neither works without the other: testing an artifact you cannot identify is meaningless, and
controlling changes you have not verified is bureaucracy.

---

## Why SCM matters more now

Supports Agile methodology. Enables DevOps practices. Facilitates CI/CD pipelines. Improves
collaboration. Ensures traceability.

---

## SCM best practices

Use branching strategies. Commit code frequently. Maintain proper documentation. Automate
builds. Use release tagging.

Ìlànà adds:
- **Protect the main branch.** No direct pushes above `RIGOUR` 2.
- **Tag every release.** An untagged release cannot be reproduced or rolled back to.
- **Commit messages describe why.** The diff already says what.
- **Never commit secrets.** History is forever; rotating is the only real fix.
- **Rehearse the rollback.** A rollback plan that has never been executed is a hypothesis.

---

## Exit

Run `checklist.md`, attempt G6. Handoff goes to `quality-auditor` with the release candidate,
the change log, and the rollback rehearsal record.
