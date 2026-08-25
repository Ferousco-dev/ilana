# Gemini CLI

Gemini CLI reads `GEMINI.md` from the repository root and from `~/.gemini/`.

## Install

```bash
git clone https://github.com/Ferousco-dev/ilana.git ~/.ilana-src
ln -s ~/.ilana-src/skill ~/.gemini/ilana
```

## Global pointer

`~/.gemini/GEMINI.md`:

```markdown
## Ìlànà software engineering process

For any task touching requirements, design, testing, configuration management, quality assurance,
process improvement, tooling, ethics or team structure, read `~/.gemini/ilana/SKILL.md` and run its
boot sequence before starting.

Begin by asking the user whether to run a fleet of specialist agents or a single focused task.
```

## Project pointer

`GEMINI.md` in the repository root, with the project's posture recorded:

```markdown
## Process

Ìlànà, rigour 3, hybrid style. Ledger in `.ilana/`.
Definition: `~/.gemini/ilana/SKILL.md`.
```

## Notes

Gemini CLI has no sub-agent mechanism, so fleet mode runs as a sequential rotation. Ìlànà will say
so at boot rather than pretending otherwise.
