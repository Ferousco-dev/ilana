# COMMANDS

Slash commands, so the common operations are one word instead of a sentence.

Installed automatically by `ilana install`. Verified by `ilana doctor`.

## The set

| Command | Does | Argument |
| --- | --- | --- |
| `/ilana` | boot, ask the fork question | what you are working on, optional |
| `/ilana:task` | one specialist, one artifact | what you want |
| `/ilana:fleet` | the full gated lifecycle | what you are building |
| `/ilana:audit` | score this repo, read-only | path, optional |
| `/ilana:ship` | release readiness, gate G6 | version, optional |
| `/ilana:review` | code review against the standard and G4 | branch or range, optional |
| `/ilana:gate` | run one gate | `G0`..`G8` and an optional rigour |
| `/ilana:doctor` | diagnose the process from symptoms | the symptom |
| `/ilana:drill` | quiz yourself, get a scorecard | format |
| `/ilana:tutor` | learn a concept properly | the concept |
| `/ilana:status` | where am I in the process | none |
| `/ilana:rigour` | set or explain the strictness dial | 1 to 5, optional |

## Which to reach for

```
/ilana:task write a test plan for the payments service
/ilana:review
/ilana:ship
/ilana:audit
/ilana:gate G4
/ilana:doctor the same bugs keep coming back
/ilana:status
/ilana:rigour 2
```

`/ilana:task` and `/ilana:review` are the two you will use most. `/ilana:audit` is the one to run
first on a codebase you have inherited.

## Where they install

| Host | Path |
| --- | --- |
| Claude Code, personal | `~/.claude/commands/ilana.md` and `~/.claude/commands/ilana/` |
| Claude Code, project | `.claude/commands/` (copy them there to share with a team) |

They are symlinked to this directory, so `git pull` updates the commands along with the skill.

## Other hosts

Most agents have no slash-command mechanism. The commands are a convenience layer on top of the
skill, never a requirement: everything they do can be triggered in prose.

```
/ilana:audit                    is the same as    audit this repo with ilana
/ilana:task write a test plan   is the same as    ilana: write me a test plan
```

If your agent supports custom commands in some other form, the bodies in `claude/` are plain
markdown prompts and will usually port directly. A contribution adding a `commands/<host>/`
directory is welcome.

## Writing your own

Each file is a prompt with YAML frontmatter.

```markdown
---
description: shown in the command list
argument-hint: what to type after the command
allowed-tools: optional tool restriction
---

The prompt. $ARGUMENTS carries whatever the user typed.
```

Keep them thin. A command should route into the skill and set the mode, not restate the process.
The skill is the source of truth; the command is a shortcut to it.
