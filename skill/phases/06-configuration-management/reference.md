# PHASE 06 REFERENCE

## Definition

Software Configuration Management is the process of systematically controlling changes made to
software artifacts throughout the software development life cycle.

Artifacts include source code, documentation, test cases, requirements and design documents.

SCM helps maintain consistency, integrity, traceability and version control.

## Objectives of SCM

Maintain consistency. Track changes. Prevent conflicts. Support team collaboration. Maintain a
history of revisions. Manage software changes. Track versions. Ensure software integrity.

## Version Control Systems

A Version Control System records changes to files over time so that developers can track and
manage modifications.

**Types**
1. **Centralized VCS.** Example: SVN. A single central repository.
2. **Distributed VCS.** Example: Git. Each developer has a local repository.

### Git

Git is a distributed version control system.

Key concepts: repository, commit, branch, merge, remote repository.

Features: distributed architecture, branching and merging, fast performance, collaboration
support, history tracking.

| Command | Function |
| --- | --- |
| `git init` | Initialize repository |
| `git clone` | Copy repository / create local copy of remote |
| `git add` | Stage changes |
| `git commit` | Save changes / create snapshot |
| `git push` | Upload changes / send local commits to remote |
| `git pull` | Download changes / fetch and integrate remote changes |
| `git branch` | Create branch / list, create or delete branches |
| `git merge` | Merge branches |

Basic workflow: modify files (working directory), stage changes (`git add`), commit changes
(`git commit`), push to remote repository (`git push`), pull updates (`git pull`).

Benefits: supports collaboration, enables rollback, tracks project history, simplifies branching.

## Change management

Change management is the process of handling modifications to software systems in a controlled
and systematic manner, and of handling change requests systematically.

**Objectives:** minimise disruption, maintain stability, ensure traceability, evaluate change
impact.

**Process:** Change Request Submission, Change Evaluation, Approval or Rejection,
Implementation, Testing, Documentation. (Also expressed as: submit change request, impact
analysis, approval, implementation, review and documentation.)

**Types of software changes:** corrective, adaptive, perfective, preventive.

## Build management

Build management involves converting source code into executable software applications, and
includes compilation, linking, packaging, dependency management and testing.

| Tool | Usage |
| --- | --- |
| Maven | Java projects |
| Gradle | Build automation |
| Ant | Java builds |
| Make | C/C++ projects |

### Continuous Integration

Continuous Integration automatically builds and tests software whenever code changes are
committed.

Benefits: early bug detection, faster development, improved software quality.
CI tools: Jenkins, GitHub Actions, GitLab CI/CD.

## Release management

Release management is the process of planning, scheduling and controlling software releases.

**Objectives:** deliver stable software, coordinate deployment, reduce deployment risks, ensure
user readiness.

**Activities:** release planning, build preparation, testing, deployment, monitoring,
maintenance. Also: version labelling, deployment planning, documentation, rollback planning,
post-release monitoring.

**Types of software releases**

| Release Type | Description |
| --- | --- |
| Major Release | Significant changes |
| Minor Release | Small improvements |
| Patch Release | Bug fixes |
| Emergency Release | Critical fixes |

## Relationship between testing and SCM

| Testing | SCM |
| --- | --- |
| Detects defects | Controls changes |
| Ensures functionality | Maintains integrity |
| Validates requirements | Tracks versions |

Together they improve reliability, maintainability, collaboration and deployment success.

## Importance of SCM in modern development

Supports Agile methodology. Enables DevOps practices. Facilitates CI/CD pipelines. Improves
collaboration. Ensures traceability.

## SCM best practices

Use branching strategies. Commit code frequently. Maintain proper documentation. Automate builds.
Use release tagging.
