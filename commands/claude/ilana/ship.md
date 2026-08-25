---
description: Ìlànà release readiness. Runs gate G6 before you deploy.
argument-hint: [version or tag, optional]
---

Run the Ìlànà release readiness gate, G6. Read `~/.claude/skills/ilana/SKILL.md`,
`gates/G6-release.md` and `protocols/release.md`.

Release under review: $ARGUMENTS

Adopt the `release-manager` agent card. Determine the project's rigour from `.ilana/state.json` if
it exists; otherwise ask once, and default to 3.

Work through the G6 criteria that apply at this rigour, gathering **evidence rather than
assertions**:

```bash
git status --porcelain          # working tree clean?
git tag | tail -5               # is there a tag to build from?
git log --oneline -20           # what is actually in this release?
ls .github/workflows 2>/dev/null
ls docs/rollback.md 2>/dev/null
```

Pay particular attention to the two criteria teams reliably fail:

- **Is the rollback plan rehearsed, with a date?** A rollback plan that has never been executed is a
  hypothesis. Ask when it was last actually performed and by whom.
- **Are there irreversible steps in this release?** Database migrations that drop data change the
  rollback story fundamentally. Teams routinely assume rollback is always possible. Name them at the
  top of the verdict if any exist.

Also ask the environment-drift question every time: *can you rebuild the production environment
from source, from scratch, with nobody remembering a step? If not, which step lives only in
someone's head?*

Produce a gate verdict in the standard format: a criteria table with met, unmet and the evidence for
each. If criteria are unmet, state the specific consequence **for this project**, not in general
terms. Then either recommend proceeding, proceeding with named risks each having a named accepter,
or not proceeding.

Record the verdict in `.ilana/gates/G6.md`.
