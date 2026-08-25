# Windsurf

Windsurf reads rules from `.windsurf/rules/`.

## Install

```bash
git clone https://github.com/Ferousco-dev/ilana.git ~/.ilana-src
mkdir -p .windsurf/rules
ln -s ~/.ilana-src/skill .windsurf/ilana
cp ~/.ilana-src/adapters/templates/ILANA.md .windsurf/rules/ilana.md
```

## Rule file

`.windsurf/rules/ilana.md` should start with the trigger paragraph and point at the payload:

```markdown
# Ìlànà process

Activate for any work touching requirements, design, interface design, coding standards, testing,
configuration management, quality assurance, metrics, process assessment, process modeling,
tooling, ethics or team structure.

Full definition: `.windsurf/ilana/SKILL.md`. Read it and run its boot sequence.

Boot always begins by asking: fleet of specialist agents, or a single focused task?
```

If your Windsurf configuration has a size limit for rules, use `adapters/templates/ILANA.md`
directly rather than the pointer. It is a compact, self-contained version of the whole process.
