# MODE: TASK

One specialist. One operation. One artifact. Full rigour on that artifact, no ceremony
elsewhere.

Task mode is what most users want most days. Treat it as first class, not as a degraded fleet.

---

## Procedure

1. **Classify.** Map the request to a phase and an agent from the table below. Say the mapping
   out loud in one line: `[TASK] phase 05 Verification, agent verifier, artifact test plan.`
2. **Interrogate.** Up to five questions, one batch, from that phase's `questions.md`.
3. **Load.** Read only `phases/<n>/PHASE.md`, the relevant template, and the agent card.
4. **Produce.** Write the artifact to the repository. Not to chat.
5. **Self-gate.** Run that phase's `checklist.md` against your own output and report the score.
6. **Record.** One ledger entry. One line.
7. **Offer.** Name the single most valuable next task, and offer the fleet if the request has
   clearly outgrown a single artifact.

---

## Routing table

| The user asks for | Phase | Agent | Template |
| --- | --- | --- | --- |
| requirements, SRS, user stories, acceptance criteria | 01 | `analyst` | `srs.md`, `user-story.md` |
| elicitation plan, stakeholder interview, questionnaire | 01 | `analyst` | `elicitation-plan.md` |
| traceability matrix | 01 | `analyst` | `traceability-matrix.md` |
| architecture, component breakdown, module spec | 02 | `architect` | `design-description.md` |
| architecture decision record | 02 | `architect` | `adr.md` |
| UI spec, screen flow, CLI design, usability review | 03 | `interaction-designer` | `interface-spec.md` |
| coding standard, style guide, code review | 04 | `constructor` | `coding-standard.md`, `code-review.md` |
| refactor, implement a module | 04 | `constructor` | (source) |
| test plan, test cases, test strategy | 05 | `verifier` | `test-plan.md`, `test-case.md` |
| defect report, bug triage, defect log | 05 | `verifier` | `defect-report.md` |
| test automation strategy | 05 | `verifier` | `automation-strategy.md` |
| branching strategy, Git workflow, SCM plan | 06 | `configuration-engineer` | `scm-plan.md` |
| change request, impact analysis | 06 | `configuration-engineer` | `change-request.md` |
| release plan, release notes, rollback plan | 06 | `release-manager` | `release-plan.md` |
| quality management plan, review or inspection | 07 | `quality-auditor` | `quality-plan.md`, `inspection-record.md` |
| audit against a standard | 07 | `quality-auditor` | `audit-report.md` |
| metrics, defect density, cycle time, variance | 07 | `metrologist` | `metrics-report.md` |
| CMMI level, ISO/IEC 12207 mapping, SPI plan | 08 | `metrologist` | `maturity-assessment.md`, `spi-plan.md` |
| activity diagram, BPMN, workflow, process model | 09 | `process-modeler` | `activity-diagram.md`, `bpmn-model.md` |
| documentation standard, SDD, user manual | 09 | `documentarian` | `document-plan.md` |
| tool selection, Jira/Trello setup, CI pipeline | 10 | `configuration-engineer` | `toolchain-decision.md` |
| ethics review, licence check, professional conduct | 11 | `ethics-officer` | `ethics-review.md` |
| team roles, RACI, communication plan, retrospective | 11 | `conductor` | `raci.md`, `retrospective.md` |

---

## Escalation from TASK to FLEET

Offer the fleet, once, without pushing, when any of these are true:

- The artifact you were asked for depends on an artifact that does not exist
  (a test plan with no requirements to test against).
- The user's follow-up requests have crossed three phases in one session.
- The request is "build X" rather than "write me the Y for X".
- `AUDIT` found gaps in four or more phases.

Phrase it as a fact plus an offer, not a warning:

> This test plan has no requirements to trace to, so its coverage claims will be unverifiable.
> Ìlànà can either (a) infer a lightweight requirement register from the existing code first,
> or (b) proceed and mark every coverage claim UNVERIFIED. Which?
