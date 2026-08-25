# ADAPTERS

Ìlànà is one payload (`skill/`) installed differently depending on the agent. Every adapter here
points at the same directory, so an update reaches all of them at once.

| Agent | Guide | Mechanism |
| --- | --- | --- |
| Claude Code | `claude-code.md` | `~/.claude/skills/ilana/` |
| Claude Code (project) | `claude-code.md` | `.claude/skills/ilana/` |
| OpenAI Codex | `codex.md` | `AGENTS.md` pointer plus `~/.codex/skills/` |
| Cursor | `cursor.md` | `.cursor/rules/ilana.mdc` |
| Windsurf | `windsurf.md` | `.windsurf/rules/` |
| Gemini CLI | `gemini-cli.md` | `GEMINI.md` pointer |
| GitHub Copilot | `copilot.md` | `.github/copilot-instructions.md` |
| Continue | `continue.md` | `.continue/rules/` |
| Aider | `aider.md` | `CONVENTIONS.md` |
| OpenCode | `opencode.md` | `~/.config/opencode/skills/` |
| Anything else | `generic.md` | paste `ILANA.md` into the system prompt |

## The universal fallback

If your agent has no skill mechanism at all, `templates/ILANA.md` is a single self-contained file
that carries the boot sequence, the constitution, the gates and the routing table. Paste it into a
system prompt, a custom instructions box, or a project rules file. It is deliberately compact
enough to fit in most of them.

## One installation, many hosts

```bash
ilana install --link --all
```

This symlinks `skill/` into every location above that exists on your machine. Because they are
symlinks to one directory, `ilana update` moves all of them at once. Nothing diverges.
