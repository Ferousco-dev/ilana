# AGENTS.md

This file has two audiences. Find yours.

- **You were pointed at this repository and asked to install it.** Read section 1, then stop.
- **You are working on this repository as a contributor.** Skip to section 2.

---

# 1. INSTALLING ÌLÀNÀ

Ìlànà is a software engineering process definition. It is documentation, shell and Python. It has
no build step and no runtime dependencies.

**What you are installing:** the `skill/` directory. Everything else in this repository is
scaffolding around it.

## The install, in full

Run these. Substitute nothing.

```bash
git clone https://github.com/Ferousco-dev/ilana.git ~/.ilana-src
~/.ilana-src/bin/ilana install --link --all
~/.ilana-src/bin/ilana doctor
```

`install --link --all` creates symlinks from every coding-agent skills directory it finds on this
machine to `~/.ilana-src/skill`. Because they are symlinks to one directory, a later
`git -C ~/.ilana-src pull` updates every agent at once.

`doctor` prints what it installed and where. **Show the user that output.** It is how they know it
worked.

## About the `ilana` command

`install --link --all` already links the command into `~/.local/bin`. If that directory is not on
the user's PATH, the installer says so and prints the exact line for their shell.

**Relay that line to the user. Do not edit their shell profile yourself without asking.**

Only `ilana update`, `ilana doctor` and the shell shortcuts need the command. The skill and the
slash commands work regardless, and the command always works by full path:

```bash
~/.ilana-src/bin/ilana doctor
```

To put it somewhere already on PATH: `ILANA_BIN=/usr/local/bin ~/.ilana-src/bin/ilana install --link --all`.
To skip it: add `--no-cli`.

## If symlinks are not possible

Some sandboxes and some Windows setups will not follow them.

```bash
~/.ilana-src/bin/ilana install --copy --all
```

Updates then require `ilana update` rather than a bare `git pull`.

## Installing for one project instead of the whole machine

```bash
git submodule add https://github.com/Ferousco-dev/ilana.git .ilana-src
mkdir -p .claude/skills
ln -s ../../.ilana-src/skill .claude/skills/ilana
```

This pins the process definition to a commit for the whole team, which is usually what you want on
a regulated project.

## Host-specific paths

If `--all` did not cover the user's agent, the per-host guides are in `adapters/`. Each one names
the exact directory and the exact pointer file that agent reads.

| Agent | Guide |
| --- | --- |
| Claude Code | `adapters/claude-code.md` |
| OpenAI Codex | `adapters/codex.md` |
| Cursor | `adapters/cursor.md` |
| Windsurf | `adapters/windsurf.md` |
| Gemini CLI | `adapters/gemini-cli.md` |
| GitHub Copilot | `adapters/copilot.md` |
| Continue | `adapters/continue.md` |
| Aider | `adapters/aider.md` |
| OpenCode | `adapters/opencode.md` |
| Anything else | `adapters/generic.md` |

## If you cannot run shell commands

Then you cannot install it, and you should say so rather than improvising. Tell the user to run
the three commands above themselves.

The one thing you **can** do without a shell: read
`adapters/templates/ILANA.md`. It is a single self-contained file carrying the boot sequence, the
constitution, the gates and the routing table. Present it to the user and tell them to paste it
into their agent's system prompt or rules file. They lose the templates and question banks; they
keep the process.

## After installing, tell the user this

> Ìlànà is installed. In a new session, say **`use ilana`**.
>
> It will ask whether you want a **fleet** of specialist agents running a full gated lifecycle, or
> a single focused **task**. Answer, and it takes over from there.
>
> The usage guide is at `docs/USING.md`.

## What not to do

- Do not run `install.sh` piped from the internet on the user's behalf without showing them the
  script first. They can pipe it themselves if they want to.
- Do not copy `skill/` into their project repository. It belongs in an agent skills directory or a
  submodule, not vendored loose into their source tree.
- Do not modify any `.ilana/` directory you find. That is a user's process ledger, not yours.
- Do not claim the install worked without showing `ilana doctor` output.

---

# 2. CONTRIBUTING TO ÌLÀNÀ

You are editing this repository. Read `CONTRIBUTING.md` in full before your first change. The rules
below are the ones most often broken.

## Before you finish, this must pass

```bash
make check
```

That runs structural validation, shell syntax checks, Python compilation, and the house-style check.

## House style, enforced mechanically

- **No em dashes. Anywhere.** Use commas, colons, semicolons, parentheses, or a new sentence. CI
  fails the build on a single one.
- **No en dashes used as em dashes** either.
- Wrap markdown at 100 columns. Tables and URLs may exceed it.
- Tables over prose wherever the content is a comparison or a lookup.
- Direct and concrete. Never "it is important to note that".

## Structural rules

- Every phase directory contains exactly: `PHASE.md`, `checklist.md`, `questions.md`,
  `antipatterns.md`, `gate.md`, `reference.md`, and `templates/`. `tests/validate.sh` enforces this.
- Every agent directory contains `AGENT.md` with: charter, owns, inputs, outputs, operating rules,
  never does, refusals, handoff produced, questions this agent asks.
- Gate criteria carry a rigour threshold: `R1+`, `R3+`, `R5`.
- Version appears in three places and they must agree: `VERSION`, `skill/manifest.json`, and the
  `metadata.version` field in `skill/SKILL.md`. CI checks this.

## Code rules

- **Python: standard library only.** Python 3.8 compatible. No third-party dependencies, ever. The
  instruments must run on a machine with nothing installed.
- **Shell: POSIX `sh`, not bash.** `sh -n` must pass.
- Every script degrades gracefully when a tool it wants is absent, and says so rather than failing
  silently.

## Traceability

Ìlànà holds itself to its own Article 3. Every commit references what it serves:

```
<type>(<scope>): <what changed, imperative, one line>

<why it changed, and what would break without it>

Refs: #issue
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `phase`, `gate`, `agent`, `adapter`.

## Attribution

Do not add yourself, your model, or your vendor as a commit co-author or contributor. Contributions
are attributed to the human who made them. `AUTHORS.md` lists people.

## What will be declined

- A new phase without a strong case. Eleven is already a lot.
- Removing a gate criterion because it is inconvenient. Argue it is *wrong*, with an example.
- Making Ìlànà less strict in general. The rigour dial exists for that.
- Vendor-specific content in the core. It belongs in `adapters/`.
