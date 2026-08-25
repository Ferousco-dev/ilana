# Documentation Plan

| Field | Value |
| --- | --- |
| Project | |
| Owner | documentarian |
| Standard(s) followed | IEEE 830 / 1016 / 829, ISO/IEC 12207, organisational |

## 1. Document inventory

| Type | Document | Standard | Audience | Owner | Updated at | Location |
| --- | --- | --- | --- | --- | --- | --- |
| Requirements | SRS | IEEE 830 | all | analyst | every CR | `docs/srs.md` |
| Requirements | User stories | | delivery team | analyst | per story | `docs/stories/` |
| Design | Software design description | IEEE 1016 | engineers | architect | G2, then per CR | `docs/design.md` |
| Design | Architecture decision records | | engineers | architect | per decision | `docs/adr/` |
| Design | Data model | | engineers, data owners | architect | per schema change | `docs/data-model.md` |
| Technical | API reference | | integrators | constructor | per interface change | |
| Technical | Configuration guide | | operators | configuration-engineer | per config change | |
| Technical | Runbook | | on-call | release-manager | per incident learning | `docs/runbook.md` |
| User | User manual | | end users | documentarian | per release | |
| User | Installation guide | | operators, users | documentarian | per release | |
| Testing | Test plan | IEEE 829 | quality, delivery | verifier | before execution | `docs/test-plan.md` |
| Testing | Test report | IEEE 829 | quality, stakeholders | verifier | per cycle | `docs/test-report.md` |
| Testing | Defect reports | | delivery team | verifier | continuous | `.ilana/defects.md` |
| Process | Process model | UML or BPMN | all | process-modeler | on process change | `docs/process-model.md` |
| Process | Quality management plan | | quality | quality-auditor | before construction | `docs/quality-plan.md` |
| Process | SCM plan | | delivery, operations | configuration-engineer | on strategy change | `docs/scm-plan.md` |

## 2. Documentation quality criteria

| Criterion | How it is checked |
| --- | --- |
| Accuracy | reviewed against the system at each gate |
| Completeness | template sections all present |
| Clarity | read by someone outside the authoring role |
| Consistency | shared glossary applied |
| Maintainability | plain text, in the repository, diffable |
| Accessibility | in the repository, linked from the README |

## 3. Update triggers

| Trigger | Documents to update |
| --- | --- |
| Requirement change (CR) | SRS, traceability, test plan, user documentation |
| Design change | SDD, ADR, data model |
| Interface change | UI spec, API reference, user manual |
| New dependency | dependency register, toolchain decision record |
| Release | changelog, user documentation, runbook |
| Incident | runbook, process model, retrospective |
| Process change | process model, relevant plan |

Documentation that is not updated by a trigger is documentation that will be wrong.

## 4. The onboarding test

The single best measure of documentation quality: give the documentation to someone who has
never seen the system and ask them to build, run, test and deploy it. Record where they got
stuck. Every place they got stuck is a documentation defect.

| Date | Newcomer | Got stuck at | Fixed in |
| --- | --- | --- | --- |
