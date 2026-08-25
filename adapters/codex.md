# OpenAI Codex

Codex reads `AGENTS.md` from the repository root and from `~/.codex/`. Ìlànà installs as a
directory Codex can read, plus a pointer in `AGENTS.md`.

## Install

```bash
git clone https://github.com/Ferousco-dev/ilana.git ~/.ilana-src
~/.ilana-src/bin/ilana install --link --target ~/.codex/skills/ilana
```

## Global pointer

`~/.codex/AGENTS.md`:

```markdown
## Ìlànà: software engineering process

Whenever a task touches requirements, design, interface design, coding standards, testing,
configuration management, quality assurance, metrics, process improvement, process modeling,
tooling, ethics or team structure, load the process definition at `~/.codex/skills/ilana/SKILL.md`
and follow its boot sequence before doing anything else.

The first thing the boot sequence does is ask whether to run a fleet of specialist agents or a
single focused task. Ask it. Do not assume.
```

## Project pointer

`AGENTS.md` in the repository root:

```markdown
## Process

This project follows Ìlànà. Before non-trivial work, read `.ilana-src/skill/SKILL.md`
and run its boot sequence.

Current rigour: 3.  Process style: hybrid.  Ledger: `.ilana/`.

Gates in force: G1 requirements, G4 construction, G5 verification, G6 release.
No merge to main without G4. No release without a rehearsed rollback.
```

## Vendoring for a team

```bash
git submodule add https://github.com/Ferousco-dev/ilana.git .ilana-src
git commit -m "vendor the ilana process definition"
```

Everyone on the team then reads the same process from the same commit, which is what makes a
process definition auditable.

## Sub-agents

Where Codex can delegate, fleet mode uses it. Where it cannot, Ìlànà rotates the thirteen agent
cards sequentially in one context. Say "rotate, do not spawn" if you prefer the sequential runtime.
