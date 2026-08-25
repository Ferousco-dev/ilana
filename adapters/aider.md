# Aider

Aider reads `CONVENTIONS.md` when you add it to the chat, and honours `.aider.conf.yml`.

## Install

```bash
git clone https://github.com/OWNER/ilana.git ~/.ilana-src
cp ~/.ilana-src/adapters/templates/ILANA.md CONVENTIONS.md
```

Or append to an existing `CONVENTIONS.md` under its own heading.

## Load it automatically

`.aider.conf.yml`:

```yaml
read: [CONVENTIONS.md]
```

## Working with Aider specifically

Aider is strongest at `TASK` mode: one artifact, one operation, focused edits. Use it for:

- writing the test plan,
- implementing a module against a design element,
- applying code review findings,
- generating an SRS from an existing codebase.

For fleet mode, Ìlànà rotates agent cards sequentially. Aider's file-scoped editing model actually
suits this well: add only the files the current agent owns to the chat, and the single-writer rule
enforces itself.

## Commit discipline

Aider commits automatically. Configure it to carry the traceability that Article 3 requires:

```yaml
attribute-author: false
commit-prompt: >
  Write a commit message with a one-line summary of what changed, a paragraph on why,
  and a trailing line "Refs: REQ-### / CR-### / DEF-###" naming the requirement,
  change request or defect this addresses.
```
