# SECURITY POLICY

## Supported versions

| Version | Supported |
| --- | --- |
| 1.x | yes |
| < 1.0 | no |

## What is in scope

Ìlànà is mostly markdown, plus a shell CLI and four Python scripts. The realistic attack surface:

| Component | Concern |
| --- | --- |
| `bin/ilana` | path handling, symlink target validation, the update path |
| `install.sh` | it is designed to be piped to `sh`; anything that lets it execute unintended code is critical |
| `skill/instruments/scripts/*.py` | file reading, subprocess use, path traversal |
| `.github/workflows/*` | workflow injection, excessive token permission |
| Skill content | instructions that would cause an agent to take an unsafe action |

That last row is real and unusual. Ìlànà is read by autonomous agents. Content that could induce an
agent to exfiltrate data, disable a control, or execute untrusted input **is a security issue**, not
a documentation issue. Report it as one.

## Reporting

**Do not open a public issue for a vulnerability.**

Use GitHub's private vulnerability reporting on this repository (Security tab, "Report a
vulnerability"), or the private contact in `SUPPORT.md`.

Include: what it is, how to reproduce it, what an attacker gains, and the version or commit.

## What to expect

| Stage | Target |
| --- | --- |
| Acknowledgement | 3 working days |
| Initial assessment | 7 working days |
| Fix for critical or high | 30 days |
| Fix for medium or low | next release |
| Public disclosure | after a fix ships, coordinated with you |

You will be credited unless you ask not to be.

## Safe harbour

Good-faith research on this repository is welcome. We will not pursue action against you if you:

- avoid privacy violations, data destruction, and service disruption,
- test only against your own installations,
- give us reasonable time to fix before public disclosure,
- do not exploit beyond what is needed to demonstrate the issue.

## Ìlànà's own security posture

Worth stating plainly, because users should not have to infer it:

- **No network access** except when you run `ilana check` or `ilana update`. Nothing in the skill
  itself contacts a server.
- **No telemetry.** No usage data is collected or transmitted.
- **No credentials.** Ìlànà never asks for, stores, or transmits a credential.
- **`ilana uninstall` never removes `.ilana/` ledgers.** Those are the user's data.
- **Instruments are read-only** except `ledger.py`, which writes only inside `.ilana/`.
- **No third-party runtime dependencies.** Standard library only, so the supply chain is git and
  your operating system.

## Reporting content that would make an agent unsafe

If you find skill content that could cause a coding agent to take a harmful action, report it
privately as above. Examples: a template that suggests logging a credential; a gate criterion that
could be satisfied by disabling a security control; wording that an agent could read as permission
to fabricate evidence.

`skill/kernel/refusal-protocol.md` is the intended defence. Gaps in it are security bugs.
