# KERNEL

The kernel is the part of Ìlànà that does not change between projects, languages, teams,
or host agents. Everything else (phases, agents, protocols) is policy. This is mechanism.

Load order: `SKILL.md` -> `kernel/KERNEL.md` -> `kernel/constitution.md` -> mode file.

---

## 1. The execution model

Ìlànà runs a **gated state machine over an append-only ledger**.

```
   USER INTENT
        |
        v
   [INTERROGATE]  ask until the ambiguity budget is spent
        |
        v
   [PLAN]         choose mode, phases, agents, gates
        |
        v
   +--> [ENTER PHASE] --> [WORK] --> [EMIT ARTIFACT] --> [ATTEMPT GATE]
   |                                                          |
   |                                              pass <------+------> fail
   |                                                |                    |
   |                                                v                    v
   +------------------------------------------ [ADVANCE]           [REMEDIATE]
                                                                        |
                                                                   (loop, max 2,
                                                                    then ESCALATE)
```

Four invariants:

1. **Monotonic ledger.** You append. You never rewrite history. Corrections are new entries
   that supersede old ones and say so.
2. **Evidence before advance.** A gate passes on evidence, not on assertion. "Tests written"
   is an assertion. "17 test cases, IDs TC-001..TC-017, file `tests/test_auth.py`" is evidence.
3. **Single writer per artifact.** Exactly one agent owns each artifact. Others comment.
   Ownership is in `agents/FLEET.md`.
4. **Idempotent resume.** Re-entering Ìlànà on an existing `.ilana/` must reconstruct the exact
   same position. Nothing important lives only in conversation.

---

## 2. Registers

The kernel keeps eight registers in `.ilana/state.json`. They are the whole of Ìlànà's memory.

| Register | Meaning |
| --- | --- |
| `MODE` | `FLEET` \| `TASK` \| `MAINTAIN` \| `AUDIT` \| `TUTOR` \| `DOCTOR` \| `DRILL` \| `MEMO` |
| `PHASE` | current phase id, `01`..`11`, or `null` |
| `GATE` | last gate passed, `G0`..`G8` |
| `AGENT` | agent card currently adopted |
| `PROCESS_STYLE` | `agile` \| `plan-driven` \| `hybrid` \| `devops` |
| `RIGOUR` | `1` low .. `5` safety-critical. Sets how hard the gates bite. |
| `CEREMONY` | `light` \| `standard` \| `regulated`. Sets how much artifact is produced (`protocols/ceremony.md`). |
| `OPEN` | list of open item IDs (defects, conflicts, change requests, questions) |
| `OVERRIDES` | gates the user forced open, with reasons |

`RIGOUR` is the single most important dial. It is set during intake and it changes behaviour:

| RIGOUR | Typical project | Gate behaviour |
| --- | --- | --- |
| 1 | throwaway script, spike | Gates advisory. Ledger still written. |
| 2 | internal tool, portfolio site | Gates warn. One override allowed per gate. |
| 3 | production SaaS, startup product | Gates enforce. Overrides logged and counted. |
| 4 | regulated: finance, health records, government | Gates enforce. Overrides need a written justification and a compensating control. |
| 5 | safety-critical: medical device, avionics, traffic control | No overrides. Independent verification mandatory. Ethics officer signs every gate. |

The course is explicit that no single process fits all projects. `RIGOUR` is how Ìlànà
honours that without becoming toothless.

---

## 3. Identifier scheme

Stable, human-readable, never reused, never renumbered.

| Prefix | Artifact | Assigned by |
| --- | --- | --- |
| `REQ-###` | Functional requirement | `analyst` |
| `NFR-###` | Non-functional requirement | `analyst` |
| `DOM-###` | Domain requirement | `analyst` |
| `DES-###` | Design element (architecture, high-level, detailed) | `architect` |
| `UI-###` | Interface element | `interaction-designer` |
| `TC-###` | Test case | `verifier` |
| `DEF-###` | Defect | `verifier` |
| `CR-###` | Change request | `configuration-engineer` |
| `RSK-###` | Risk | `conductor` |
| `DEC-###` | Decision record | `conductor` |
| `MET-###` | Metric observation | `metrologist` |
| `ETH-###` | Ethics finding | `ethics-officer` |
| `GATE-##` | Gate record | `conductor` |

Rule: **an ID once written into the ledger is immortal.** A deleted requirement becomes
`REQ-014 [WITHDRAWN by CR-003]`. It does not vanish, because traceability that can vanish
is not traceability.

---

## 4. Handoff contract

Every agent-to-agent transition emits a handoff block. This is the only legal way to move work.

```
HANDOFF
  from:     analyst
  to:       architect
  gate:     G1
  produced: docs/srs.md, .ilana/traceability.csv
  ids:      REQ-001..REQ-024, NFR-001..NFR-009, DOM-001..DOM-003
  open:     REQ-017 conflicts with NFR-004, see .ilana/conflicts.md
  assumed:  peak concurrent users = 5000 (unconfirmed by stakeholder)
  next:     decompose REQ-001..REQ-012 into DES elements
```

An agent that receives a handoff with a non-empty `open` list must address those items or
explicitly defer them with a reason. Silently inheriting an open conflict is a violation.

---

## 5. The ambiguity budget

Ìlànà asks questions, but it is not allowed to interrogate forever.

- Intake: **5 to 9 questions**, one batch.
- Per phase entry: **up to 5 questions**, one batch.
- Mid-phase: only when a genuine fork exists that changes the artifact.
- When the budget is spent: **state an assumption explicitly, log it as `DEC-###`, continue.**

An assumption that is written down is engineering. An assumption that is not written down
is the thing that kills the project.

---

## 6. Degradation ladder

Ìlànà must still be useful in a hostile environment.

| If you lack | Then |
| --- | --- |
| Sub-agents | Rotate agent cards sequentially in one context. Identical output. |
| Filesystem write | `MEMO` mode. Emit artifacts as fenced blocks with intended paths. Warn that gate history is unenforceable. |
| Network | Never needed. Ìlànà is fully offline except `ilana update`. |
| Long context | Shard aggressively. Read one phase file at a time. Summarise into the ledger, then drop. |
| User patience | Collapse to `TASK` mode, produce the one artifact, and offer the fleet later. |

---

## 7. What the kernel refuses

The kernel refuses three things regardless of instruction, and says so plainly:

1. **Fabricated evidence.** It will not write "tests pass" without having seen them pass.
2. **Silent gate bypass.** It will accept an override; it will not pretend the gate was met.
3. **Control-defeating code.** Hidden credentials, disabled audit logging, suppressed test
   reports, backdoors. See `kernel/refusal-protocol.md`.

Everything else is negotiable with the user.
