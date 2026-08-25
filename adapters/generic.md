# Any other agent

Ìlànà assumes almost nothing. If your agent can read files, write files and talk to a human, it can
run the process.

## Three installation shapes, in order of preference

### 1. Directory the agent can read

Best. Full fidelity: phases, templates, protocols, instruments, question banks.

```bash
git clone https://github.com/OWNER/ilana.git ~/.ilana-src
```

Then, in whatever instruction file your agent reads:

```
Read ~/.ilana-src/skill/SKILL.md and run its boot sequence before non-trivial work.
```

### 2. Single instruction file

For agents that accept one system prompt or one rules file.

```bash
cp ~/.ilana-src/adapters/templates/ILANA.md <wherever your agent reads>
```

`ILANA.md` is self-contained: boot sequence, constitution, gates, routing table, and the
FLEET/TASK fork. It loses the templates and question banks, and keeps everything else.

### 3. Paste into the conversation

Works anywhere, including a plain chat interface with no file access.

Paste `ILANA.md`, then say: "run the boot sequence".

In this mode Ìlànà runs in `MEMO` degradation: it emits every artifact as a fenced code block with
its intended path, and tells you it cannot enforce gate history because it has no ledger.

## What degrades, and how

| Missing | Effect |
| --- | --- |
| Sub-agents | fleet mode rotates agent cards sequentially in one context; identical artifacts |
| Filesystem write | `MEMO` mode; artifacts as fenced blocks; no enforceable gate history |
| Python 3 | instruments fall back to the manual procedures documented in each `.md` |
| Network | no effect; Ìlànà is fully offline except `ilana update` |
| Long context | shard: read one phase file at a time, summarise into the ledger, drop |

## Minimum viable Ìlànà

If you can carry only one paragraph into your agent, carry this one:

> Before writing code, ask: what requirement is this satisfying, and how will we know it works?
> Before shipping, ask: which gate have we skipped, and who accepted that risk?
> Never claim a test passed without having seen it pass.
