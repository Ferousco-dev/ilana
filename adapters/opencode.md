# OpenCode

## Install

```bash
git clone https://github.com/OWNER/ilana.git ~/.ilana-src
~/.ilana-src/bin/ilana install --link --target ~/.config/opencode/skills/ilana
```

`ilana install --all` includes this location automatically.

## Project instructions

`AGENTS.md` in the repository root:

```markdown
## Process

This project follows Ìlànà. Read `~/.config/opencode/skills/ilana/SKILL.md` and run its boot
sequence before non-trivial work.

Rigour 3. Hybrid process style. Ledger in `.ilana/`.
Boot always asks: fleet of agents, or a single task?
```

## Notes

Where OpenCode supports sub-agents, fleet mode uses them. Where it does not, Ìlànà rotates the
agent cards sequentially and says so at boot.
