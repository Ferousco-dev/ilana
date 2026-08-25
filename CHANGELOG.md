# Changelog

All notable changes to this project are documented in this file.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Because Ìlànà is a process definition rather than a library, "breaking" means a change that
alters gate criteria, constitutional articles, or the ledger format in a way that changes how
existing projects behave.

## [Unreleased]

### Added

- `AGENTS.md` at the repository root, written for an agent that has been handed the repo URL and
  asked to install it. Carries the exact commands, the symlink fallback, per-host paths, and an
  explicit list of things not to do. Makes `install this skill: <url>` a first-class path.
- `docs/USING.md`, the usage guide: what to say, how to read gate verdicts and handoffs, the rigour
  dial, recipes for the things people actually want, what gets written to `.ilana/`, steering and
  overriding, team setup, and troubleshooting.

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
