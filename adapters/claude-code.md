# Claude Code

## Personal install (all your projects)

```bash
git clone https://github.com/Ferousco-dev/ilana.git ~/.ilana-src
ln -s ~/.ilana-src/skill ~/.claude/skills/ilana
```

Or, with the CLI:

```bash
~/.ilana-src/bin/ilana install --link
```

## Project install (this repository only, shared with your team)

```bash
mkdir -p .claude/skills
git submodule add https://github.com/Ferousco-dev/ilana.git .ilana-src
ln -s ../../.ilana-src/skill .claude/skills/ilana
```

Committing the submodule pins the process definition for the whole team, which is often exactly
what you want in a regulated project.

## Verify

Start Claude Code and ask:

```
what skills do you have available?
```

`ilana` should appear. If it does not, run `ilana doctor`.

## Invoke

Ìlànà loads automatically when your request touches requirements, design, testing, SCM, quality,
process, ethics or team topics, because its description covers them. You can also call it
explicitly:

```
use ilana
/ilana
run the process on this
gate this before I ship
audit this repo with ilana
```

The first thing it does is ask whether you want a **fleet of agents** or a **single task**.

## Fleet mode with real sub-agents

Claude Code has the `Agent` tool, so fleet mode can run specialists in parallel. Ìlànà states the
expected agent count before spawning anything, and offers a trimmed variant at low rigour.

If you would rather it never spawn sub-agents, say so once and it will rotate the agent cards
sequentially in one context instead. The artifacts are identical.

## Optional: check for updates at session start

`~/.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          { "type": "command", "command": "ilana check --quiet --max-age 7" }
        ]
      }
    ]
  }
}
```

At most one line, at most once a week.

## Optional: enforce a gate before commits

`~/.claude/settings.json`, or the project `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command",
            "command": "case \"$CLAUDE_TOOL_INPUT\" in *'git commit'*) python3 ~/.ilana-src/skill/instruments/scripts/gate_check.py --gate G4 --rigour 3 --repo . ;; esac" }
        ]
      }
    ]
  }
}
```

This runs the construction gate whenever a commit is attempted. Adjust the gate and rigour to your
project.
