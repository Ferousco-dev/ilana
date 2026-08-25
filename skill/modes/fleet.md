# MODE: FLEET

Full lifecycle. Up to thirteen specialist agents. Nine gates. A complete paper trail.

Use when the deliverable is a system, not a snippet.

---

## Before you spawn anything

Print the plan and get a yes. Fleet mode is expensive; surprising the user with it is rude.

```
FLEET PLAN
  project:       Library Management System
  process style: hybrid (Agile construction, plan-driven governance)
  rigour:        3 of 5
  phases:        01 02 03 04 05 06 07 08 (09, 10, 11 continuous)
  agents:        conductor, analyst, architect, interaction-designer, constructor,
                 verifier, configuration-engineer, quality-auditor, metrologist,
                 documentarian, ethics-officer, release-manager   (12 of 13)
  gates:         G0..G8
  artifacts:     docs/srs.md, docs/design.md, docs/ui-spec.md, docs/test-plan.md,
                 docs/scm-plan.md, docs/quality-plan.md, docs/process-model.md,
                 docs/maturity-assessment.md, .ilana/*
  estimate:      ~12 agent turns, one long session or several short ones
Proceed?  [yes / trim / switch to TASK]
```

`trim` is a real option. Offer the trimmed variant for `RIGOUR` 1 to 2:
phases 01, 02, 04, 05, 06 only; agents `analyst`, `architect`, `constructor`, `verifier`,
`configuration-engineer`; gates G1, G4, G5.

---

## Execution: two runtimes, one behaviour

### Runtime A: real sub-agents

Host supports parallel agents (Claude Code `Agent`, or equivalent). Then:

- **Wave 1 (parallel):** `analyst` elicits; `process-modeler` drafts the process model;
  `ethics-officer` scans the domain for regulatory and safety exposure.
  Barrier at `G1`, because architecture must see the whole requirement set.
- **Wave 2 (parallel):** `architect` decomposes; `interaction-designer` specifies the
  interface; `documentarian` starts the SRS-to-design traceability.
  Barrier at `G3`.
- **Wave 3 (pipeline, no barrier):** each design element flows independently through
  `constructor` -> `verifier`. A module that is done testing does not wait for its siblings.
- **Wave 4 (parallel):** `configuration-engineer` prepares the release train;
  `quality-auditor` runs the inspection; `metrologist` computes the metric set.
  Barrier at `G6`.
- **Wave 5 (sequential):** `release-manager` go/no-go, then `conductor` closes at `G8`.

`ethics-officer` is not a wave. It is resident and may interrupt any wave.

### Runtime B: no sub-agents (role rotation)

Identical artifacts, one context. Adopt one agent card at a time:

```
[analyst] ... work ... HANDOFF -> architect
[architect] ... work ... HANDOFF -> interaction-designer
```

Between rotations, write the artifact to disk and append to the ledger, then drop the previous
agent's working detail from active reasoning. The ledger is what carries state, not memory.

This runtime is the default. Never assume the host has sub-agents.

---

## Phase walk

| Gate | Phase entered | Lead | Exit artifact |
| --- | --- | --- | --- |
| G0 | 01 Requirements | `analyst` | `docs/srs.md`, `.ilana/traceability.csv` |
| G1 | 02 Architecture | `architect` | `docs/design.md` |
| G2 | 03 Interface | `interaction-designer` | `docs/ui-spec.md` |
| G3 | 04 Construction | `constructor` | source + `docs/coding-standard.md` |
| G4 | 05 Verification | `verifier` | `docs/test-plan.md`, `.ilana/defects.md` |
| G5 | 06 Configuration Mgmt | `configuration-engineer` | `docs/scm-plan.md` |
| G6 | 07 Quality Assurance | `quality-auditor` | `docs/quality-plan.md` |
| G7 | 08 Process Assessment | `metrologist` | `docs/maturity-assessment.md` |
| G8 | closure | `conductor` | `docs/retrospective.md` |

Phases 09 (process modeling), 10 (tooling) and 11 (ethics and teams) are continuous. Their
artifacts are updated at every gate rather than produced once.

---

## Fleet rules

1. **One writer per artifact.** Two agents never edit the same file in the same wave.
2. **Handoffs are explicit.** Use the block in `kernel/KERNEL.md` section 4. No handoff, no advance.
3. **Open items travel.** A receiving agent must address or explicitly defer every open item.
4. **Ethics is resident.** `ethics-officer` reads every handoff. Its veto stops the wave.
5. **Metrics at every gate.** `metrologist` records at least one `MET-###` per gate, even if
   the value is "not measurable yet, and here is why".
6. **The conductor never writes production code.** It owns gates, schedule and ledger only.
   This mirrors the Project Manager role in the course material.
7. **Announce every agent switch.** The user must always know who is speaking.

---

## Failure handling

| Failure | Response |
| --- | --- |
| Gate fails once | Name the exact missing evidence. Remediate. Retry. |
| Gate fails twice | `protocols/escalation.md`. Stop and present options to the user. |
| Two agents disagree | `protocols/conflict-resolution.md`: objective technical criteria, agreed in advance, applied by `conductor`. |
| Requirement conflicts with requirement | `analyst` runs a facilitated resolution with the user. Never resolve a stakeholder conflict unilaterally. |
| Ethics veto | Halt. Present `ETH-###`. Wait for the human. |
| Scope grows | `CR-###`. Impact analysis before implementation, never after. |
