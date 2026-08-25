# GitHub Copilot

Copilot reads `.github/copilot-instructions.md` from the repository root.

## Install

Because Copilot loads a single instruction file rather than a directory, use the compact
self-contained version.

```bash
git clone https://github.com/OWNER/ilana.git ~/.ilana-src
mkdir -p .github
cp ~/.ilana-src/adapters/templates/ILANA.md .github/copilot-instructions.md
```

If you already have instructions, append it under its own heading rather than replacing them.

## What Copilot can and cannot do

| Ìlànà feature | Works in Copilot |
| --- | --- |
| Constitution and gates as behavioural rules | yes |
| The FLEET / TASK fork | yes, as a question it asks you |
| Phase routing and templates | yes, if you also commit `skill/` into the repository |
| Ledger in `.ilana/` | yes, Copilot can write files |
| Parallel agent fleet | no; sequential rotation only |
| Instruments (`metrics.py`, `gate_check.py`) | yes, run them yourself or via a task |

## Recommended for teams

Commit the whole skill into the repository so the templates are available:

```bash
git submodule add https://github.com/OWNER/ilana.git .ilana-src
```

Then point the instruction file at `.ilana-src/skill/` for anything beyond the compact rules.

## Pipeline enforcement

Copilot is a suggestion engine, not an enforcement surface. Put the real gates in CI:

```yaml
- name: Ilana gate G4
  run: python3 .ilana-src/skill/instruments/scripts/gate_check.py --gate G4 --rigour 3 --strict
```
