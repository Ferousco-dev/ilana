# Changelog

All notable changes to this project are documented in this file.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Because Ìlànà is a process definition rather than a library, "breaking" means a change that
alters gate criteria, constitutional articles, or the ledger format in a way that changes how
existing projects behave.

## [Unreleased]

## [1.0.3] - 2026-08-25

### Fixed

- `ilana update` printed the wrong changelog section. It extracted from the first heading in the
  file, which is `[Unreleased]`, so the notes shown after an update belonged to the previous
  release. It now extracts the section for the version actually installed.

## [1.0.2] - 2026-08-25

Two bugs found by installing into a clean environment and using it on a deliberately flawed
project, rather than by testing the parts in isolation.

### Fixed

- **G5 passed "regression suite runs in CI" on a repository with zero tests.** The check only
  looked for a CI config file, so a pipeline doing nothing but a syntax check satisfied it. A gate
  that passes when it should not is worse than no gate, because it manufactures confidence. The
  criterion now requires tests to actually exist as well.
- **`SKILL.md` hardcoded a version string in the boot announcement**, which went stale the moment
  1.0.1 shipped and would have drifted on every release. The announcement no longer carries a
  version, and the skill is told to read `manifest.json` if the user asks rather than recalling it.

### Added

- Structural validation fails if any hardcoded version string reappears in the skill prose.
- A CI regression step asserting G5 fails the regression criterion without tests and passes it once
  tests are present, checked in both directions.

## [1.0.1] - 2026-08-25

A field-reported installation bug and everything around it.

### Fixed

- **`bin/ilana` did not resolve `$0` through symlinks.** Invoking it through the symlink on PATH,
  which is the normal setup, made `REPO_ROOT` resolve to the symlink's own directory. `ilana doctor`
  then reported `version: unknown`, `MISSING SKILL.md`, `phases: 0`, `agents: 0` and
  `installation incomplete`, while the same command run by absolute path reported `healthy`. Now
  resolved with a bounded loop and `pwd -P`.
- **`ilana install` never put the CLI on PATH**, so `ilana: command not found` immediately after a
  successful install was the expected outcome. Only `install.sh` linked it. `install --all` now
  links the command into `~/.local/bin` (override with `ILANA_BIN`, opt out with `--no-cli`).

### Added

- `ilana doctor` reports a `cli on PATH:` section: whether the command resolves, where it resolves
  to, and a warning if another installation is shadowing this one.
- When `~/.local/bin` is not on PATH, both `install` and `doctor` name the user's actual shell
  profile and print the exact command, for zsh, bash and fish. "Add it to your shell profile" is
  useless advice if you do not know which file that is.
- `--no-cli` flag on `ilana install`.
- Three CI regression steps pinned to the reported path: `ilana doctor` must report `healthy`
  through `~/.local/bin/ilana` and must resolve `repository:` to the real clone; `install` must
  print concrete PATH advice when the command will not resolve; `--no-cli` must be respected.

### Changed

- Troubleshooting in `docs/USING.md`, the FAQ and `AGENTS.md` all now state plainly that the skill
  and slash commands work without the CLI on PATH, so a missing PATH entry is an inconvenience
  rather than a broken install.

### Added

- **Slash commands.** `/ilana` plus eleven subcommands: `task`, `fleet`, `audit`, `ship`, `review`,
  `gate`, `doctor`, `drill`, `tutor`, `status`, `rigour`. Installed automatically by
  `ilana install`, symlinked so they update with the skill. Every command has a prose equivalent,
  because most agents have no slash-command mechanism.
- **CLI shortcuts for the instruments.** `ilana status`, `ilana gate G4`, `ilana metrics`,
  `ilana trace`, `ilana commands`. `ilana gate` reads rigour from `.ilana/state.json` when not
  given one, so the common case is two words.

- `AGENTS.md` at the repository root, written for an agent that has been handed the repo URL and
  asked to install it. Carries the exact commands, the symlink fallback, per-host paths, and an
  explicit list of things not to do. Makes `install this skill: <url>` a first-class path.
- `docs/USING.md`, the usage guide: what to say, how to read gate verdicts and handoffs, the rigour
  dial, recipes for the things people actually want, what gets written to `.ilana/`, steering and
  overriding, team setup, and troubleshooting.

### Fixed

- `bin/ilana` now resolves `$0` through symlinks. Invoking it via a symlink on PATH, which is the
  normal setup, made `REPO_ROOT` point at the symlink's directory instead of the clone, so
  `ilana doctor` reported the payload as missing and every derived path was wrong.

### Changed

- README install section restructured around the three real paths, with agent-driven install first,
  followed by a "Use it" section showing the fork question and the phrasings that land.
- `install.sh` now detects the shell and prints the exact profile file and command for the PATH
  fix, rather than saying "your shell profile". It also states that the CLI is optional.
- FAQ answers "can I just point my agent at the repo" and "how do I know it installed correctly".

## [1.0.0] - 2026-08-25

First release.

### Added

- **Kernel.** Sixteen-article constitution ordered by precedence, gated state machine, ledger
  specification, refusal protocol, glossary.
- **Six modes.** FLEET, TASK, AUDIT, TUTOR, DOCTOR, DRILL, plus MEMO degradation for hosts with
  no filesystem.
- **The boot fork.** Every invocation asks whether to run a bundle of specialist agents or a
  single focused task, before doing anything else.
- **Nine gates**, G0 through G8, with criteria scaled by a rigour dial from 1 (throwaway) to 5
  (safety-critical). Overrides are recorded, never silent. Rigour 5 permits no overrides.
- **Eleven phases**: requirements, architecture and design, interface design, construction,
  verification, configuration management, quality assurance, process assessment, process modeling
  and documentation, tooling, ethics and teams. Each with a phase guide, checklist, question set,
  anti-patterns, gate summary, condensed reference, and templates.
- **Thirteen agents** with charters, refusal lists, handoff contracts and enforced separation of
  duties. Runs with real sub-agents where available, or as a sequential role rotation where not.
- **Ten protocols**: question engine, elicitation, reviews and inspections, defect lifecycle,
  change control, conflict resolution, escalation, release, incident, handoff.
- **Four instruments**, dependency-free Python 3: metrics engine computing product, process and
  project metrics; gate checker; traceability checker; ledger tool. Each with a documented manual
  fallback.
- **Twelve assessment banks** plus an integrated scenario bank, used by DRILL mode.
- **Seven reference cards**: quick reference, standards, CMMI, ACM/IEEE ethics, methodology,
  tools map, reading list.
- **Ten host adapters**: Claude Code, Codex, Cursor, Windsurf, Gemini CLI, GitHub Copilot,
  Continue, Aider, OpenCode, generic. Plus a self-contained single-file version for any agent
  that reads one instruction file.
- **`ilana` CLI**: install, update, check, doctor, channel, pin, autoupdate, init, uninstall.
  Symlink installs mean one `git pull` updates every agent on the machine.
- **Update mechanism** with stable and edge channels, version pinning, scheduled background
  checks via launchd or systemd, and a local overrides directory whose contents survive updates.
- **Worked examples**: a full fleet run on a library management system, and an audit run.
- **Syllabus map** connecting every course topic to its location in the skill.

### Notes

- Ìlànà never touches the network except when you run `ilana check` or `ilana update`.
- `.ilana/` ledgers belong to the user and are never removed by `ilana uninstall`.
- CMMI figures are always reported as indicative self-assessments, never as appraisals.
