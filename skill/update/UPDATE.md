# UPDATE MECHANISM

Ìlànà updates on the user's side, not only in the repository. This file describes the mechanism;
the CLI that implements it is `bin/ilana` at the repository root.

---

## The problem this solves

A skill installed by copying files becomes stale the moment the upstream changes. Users end up
running a version nobody maintains, with none of the fixes and none of the new phases.

Ìlànà solves this three ways, in order of preference.

---

## Method 1: symlink install (recommended)

```bash
git clone https://github.com/OWNER/ilana.git ~/.ilana-src
ln -s ~/.ilana-src/skill ~/.claude/skills/ilana
```

Now `git -C ~/.ilana-src pull` updates every agent on the machine at once. Nothing to copy,
nothing to diverge.

`bin/ilana install --link` does exactly this and registers the source path.

## Method 2: managed copy

For hosts that will not follow symlinks.

```bash
ilana install --copy
```

The CLI records the installed version and a manifest of file checksums in
`~/.config/ilana/state.json`. `ilana update` fetches upstream, compares, and replaces only files
the user has not modified. Modified files are reported, never silently overwritten.

## Method 3: manual

```bash
git pull && cp -r skill/* ~/.claude/skills/ilana/
```

Supported, but the user is responsible for noticing that upstream changed.

---

## Update checking

`bin/ilana check` compares the local `VERSION` against the upstream `VERSION` file and prints the
result. It touches the network only when run.

State lives in `~/.config/ilana/state.json` and, per project, `.ilana/update-state.json`:

```json
{
  "installed_version": "1.0.0",
  "install_method": "link",
  "source": "/home/user/.ilana-src",
  "channel": "stable",
  "last_checked": "2026-08-25",
  "pinned": false
}
```

### At boot

`SKILL.md` step 0.3 reads `.ilana/update-state.json`. If `last_checked` is older than seven days
or missing, Ìlànà emits **one line** and continues:

```
Update check is stale. Run `ilana update` when convenient. Continuing.
```

It never blocks. It never fetches the network on its own. A process tool that interrupts your work
to talk about itself has misunderstood its job.

---

## Automatic updating

Three optional mechanisms, all opt-in. None is installed by default.

### Scheduled check

```bash
ilana autoupdate --enable --interval weekly
```

Installs a `launchd` agent on macOS or a `systemd` timer on Linux that runs
`ilana update --quiet` on the chosen interval. `ilana autoupdate --disable` removes it.

### Shell hook

Add to `~/.zshrc` or `~/.bashrc`:

```bash
ilana check --quiet --max-age 7 &>/dev/null &
```

Non-blocking. Prints a single line at most once per week.

### Git hook, for teams

For a team that vendors Ìlànà into a project repository, `.git/hooks/post-merge`:

```bash
#!/bin/sh
[ -x "$(command -v ilana)" ] && ilana check --quiet
```

### Claude Code SessionStart hook

For users who want the check to run when a session begins, in `~/.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      { "hooks": [ { "type": "command", "command": "ilana check --quiet --max-age 7" } ] }
    ]
  }
}
```

---

## Channels

| Channel | Tracks | For |
| --- | --- | --- |
| `stable` | latest tagged release | everyone, default |
| `edge` | `main` | contributors and people who want new phases early |

```bash
ilana channel edge
ilana channel stable
```

## Pinning

Teams that need a fixed process definition across a project:

```bash
ilana pin 1.2.0     # stay here until unpinned
ilana unpin
```

A pinned installation reports its pin at boot so nobody wonders why an update never arrives.

---

## Local customisation that survives updates

Never edit files under the installed skill; they are replaced. Instead:

```
~/.config/ilana/overrides/
  constitution.append.md      appended to the constitution
  gates/G4.append.md          extra criteria for one gate
  phases/04.append.md         house rules for a phase
  agents/constructor.append.md
```

Ìlànà reads `overrides/` after the corresponding core file and treats its content as additive.
Local rules therefore survive every update, and the diff between your process and upstream stays
visible.

`ilana doctor` reports which overrides are active.

---

## Verifying an installation

```bash
ilana doctor
```

Reports: installed version, install method, channel, whether the installation is complete, whether
any file has been modified locally, which overrides are active, whether the agent hosts it can
detect have Ìlànà registered, and whether Python 3 is available for the instruments.

---

## Uninstalling

```bash
ilana uninstall
```

Removes the installed skill and the config directory. **It never touches any project's `.ilana/`
ledger**, because that is the user's process history, not Ìlànà's.
