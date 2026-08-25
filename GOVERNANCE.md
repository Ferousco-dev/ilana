# GOVERNANCE

Small project, light governance, stated plainly so nobody has to guess.

## Roles

| Role | Who | Can |
| --- | --- | --- |
| Maintainer | listed in `.github/CODEOWNERS` | merge, release, resolve disputes |
| Contributor | anyone with a merged pull request | propose, review, discuss |
| User | anyone | file issues, ask questions |

Becoming a maintainer: three substantive merged contributions and a maintainer nomination, with no
objection from the others within a week.

## How decisions are made

The same way Ìlànà tells you to resolve a technical disagreement, because it would be embarrassing
to do otherwise.

1. **Agree the criteria before evaluating the options.** For a content change the criteria are
   usually: is it traceable to the source material or defensible practice; does it catch a real
   defect class; what does it cost the reader; does it hold at every rigour level.
2. **Evaluate the options against those criteria**, in the pull request.
3. **Record the decision and the rejected alternatives.** For anything structural, that record is a
   file under `docs/adr/`.
4. **Disagree and commit.** Once decided, it is decided until new evidence arrives.

Where consensus does not emerge, a maintainer decides and records why. Seniority is not a score.

## Change classes

| Class | Examples | Requires |
| --- | --- | --- |
| Editorial | typos, clarity, formatting | one maintainer approval |
| Additive | a new adapter, a new anti-pattern, new questions | one maintainer approval |
| Substantive | a new gate criterion, a new template, a changed default | two maintainer approvals |
| Structural | a new phase, a changed constitutional article, a ledger format change | two approvals, an ADR, and a minor version bump |
| Breaking | anything that changes how existing projects behave | two approvals, an ADR, a major version bump, a migration note |

## Releases

Semantic versioning.

- **Major**: gate criteria, constitutional articles or the ledger format change in a way that alters
  existing projects' behaviour.
- **Minor**: new phases, agents, adapters, instruments, templates.
- **Patch**: corrections, clarifications, fixes.

`make release V=1.1.0` tags it. `CHANGELOG.md` is updated in the same commit.

## Scope discipline

Ìlànà is a **software engineering process** skill. It is not a general coding assistant, a
framework, a linter, or a project management tool.

Proposals are declined when they:

- add capability unrelated to process,
- couple the core to a specific vendor or tool,
- make the payload larger without making the process better,
- reduce strictness generally rather than at a specific rigour level.

The rigour dial exists so that strictness is a user choice, not a maintainer compromise.

## Forking

MIT licensed. Fork freely. If you build something better, say so in an issue and we will link to it.
A process definition that cannot be forked is a process definition nobody can adapt, and adaptation
is the whole point.
