# Continue

Continue reads rules from `.continue/rules/` and from `config.yaml`.

## Install

```bash
git clone https://github.com/OWNER/ilana.git ~/.ilana-src
mkdir -p .continue/rules
ln -s ~/.ilana-src/skill .continue/ilana
cp ~/.ilana-src/adapters/templates/ILANA.md .continue/rules/ilana.md
```

## Rule file

`.continue/rules/ilana.md`:

```markdown
---
name: ilana
description: Software engineering process. Requirements, design, testing, SCM, quality, process, ethics.
---

Read `.continue/ilana/SKILL.md` and run its boot sequence before non-trivial work.
Begin by asking whether to run a fleet of specialist agents or a single focused task.
```

## Slash command

`config.yaml`:

```yaml
customCommands:
  - name: ilana
    description: Run the Ilana software engineering process
    prompt: |
      Read .continue/ilana/SKILL.md and run its boot sequence now.
      Ask the FLEET or TASK question before doing anything else.
```
