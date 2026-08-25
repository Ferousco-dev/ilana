# SYLLABUS MAP

Where each part of SEN102/212 lives in Ìlànà. For students revising, and for anyone who wants to
check that nothing was dropped.

---

## Course content, as stated

> **Requirements Process.** Requirements elicitation, analysis, specification, validation;
> traceability; role of process in managing requirements.
>
> **Software Design and Development Process.** Design process activities; architectural design;
> interface and component design; coding standards and best practices.
>
> **Software Testing Process.** Testing levels (unit, integration, system, acceptance); test
> planning; test automation; defect tracking and reporting.
>
> **Software Configuration Management.** Version control systems (Git), change management, build
> management, release management.

Plus the three additional lecture modules delivered in the same course: process modeling and
documentation with tooling; software quality assurance; software process assessment and
improvement; and process ethics, team dynamics and industry practices.

---

## Mapping

| Course topic | Ìlànà location |
| --- | --- |
| **Requirements engineering** | |
| Definition, objectives, historical evolution | `phases/01-requirements/reference.md` |
| Functional, non-functional, domain requirements | same, plus `templates/srs.md` |
| Elicitation, analysis, specification, validation, management | `phases/01-requirements/PHASE.md`, `protocols/elicitation.md` |
| Traceability | `phases/01-requirements/templates/traceability-matrix.md`, `instruments/scripts/traceability.py` |
| Six challenges and six strategies | `phases/01-requirements/reference.md`, `antipatterns.md` |
| Case studies (healthcare, e-commerce) | `phases/01-requirements/reference.md` |
| **Software design** | |
| Definition, objectives | `phases/02-architecture-design/reference.md` |
| Three levels: architecture, high-level, detailed | `phases/02-architecture-design/PHASE.md` |
| Six design objectives | `checklist.md`, `templates/design-description.md` |
| **User interface design** | |
| Text-based and graphical, advantages and disadvantages | `phases/03-interface-design/reference.md` |
| GUI characteristics | same |
| Five UI design principles | `phases/03-interface-design/PHASE.md`, restated as tests |
| **Coding** | |
| Goals of coding | `phases/04-construction/reference.md` |
| Characteristics of programming languages | same |
| Coding standards | `phases/04-construction/PHASE.md`, `templates/coding-standard.md` |
| Coding guidelines | same, with modern adaptation guidance |
| **Software testing** | |
| Definition, objectives, importance | `phases/05-verification/reference.md` |
| Testing process (seven stages) | `phases/05-verification/PHASE.md` |
| Four levels and the testing pyramid | same |
| Integration strategies | same |
| Test planning and plan components | `templates/test-plan.md` |
| Test automation, tools, benefits, challenges | `templates/automation-strategy.md` |
| Defect tracking, life cycle, report fields | `templates/defect-report.md`, `protocols/defect-lifecycle.md` |
| **Software configuration management** | |
| Definition, objectives, artifacts | `phases/06-configuration-management/reference.md` |
| Version control, centralized and distributed, Git | same, plus `templates/scm-plan.md` |
| Change management and change types | `protocols/change-control.md` |
| Build management and tools | `phases/06-configuration-management/PHASE.md` |
| Continuous integration | same, plus `phases/10-tooling/templates/ci-pipeline.md` |
| Release management and release types | `templates/release-plan.md`, `protocols/release.md` |
| Relationship between testing and SCM | `phases/06-configuration-management/reference.md` |
| **Software quality assurance** | |
| Definition, concept of quality, objectives | `phases/07-quality-assurance/reference.md` |
| SQA as a continuous process | same |
| Five core activities | `phases/07-quality-assurance/PHASE.md` |
| Reviews, walkthroughs, inspections, audits | `protocols/review-inspection.md`, `templates/inspection-record.md` |
| Product, process and project metrics | `instruments/metrics.md`, `templates/metrics-report.md` |
| Seven quality attributes | `instruments/quality-attributes.md`, `templates/quality-scorecard.md` |
| **Process assessment and improvement** | |
| Assessment, SPI, process measurement | `phases/08-process-assessment/reference.md` |
| CMMI five levels | `references/cmmi.md`, `instruments/cmmi-probe.md` |
| ISO/IEC 12207 three categories | `references/standards.md`, `templates/process-map-12207.md` |
| Process optimization techniques | `phases/08-process-assessment/PHASE.md` |
| Measure, Analyze, Improve, Repeat | `templates/spi-plan.md` |
| **Process modeling and documentation** | |
| Process modeling, objectives, characteristics | `phases/09-process-modeling/reference.md` |
| UML activity diagrams and notation | `templates/activity-diagram.md` |
| BPMN and the comparison | `templates/bpmn-model.md` |
| Documentation types and standards | `templates/document-plan.md`, `references/standards.md` |
| Process workflows and components | `templates/workflow.md` |
| **Tools supporting software processes** | |
| CASE tools: upper, lower, integrated | `phases/10-tooling/reference.md` |
| Central repository and data dictionary | same |
| Project management tools, Jira, Trello | same, plus `templates/board-setup.md` |
| CI tools: Jenkins, GitHub Actions | `templates/ci-pipeline.md` |
| **Ethics, teams and industry practice** | |
| Software engineering ethics, five key issues | `phases/11-ethics-and-teams/reference.md` |
| Ethics in process adherence | same, plus `kernel/constitution.md` Article 6 |
| ACM/IEEE code, four principles | `references/acm-ieee-ethics.md` |
| Team dynamics, five characteristics | `phases/11-ethics-and-teams/PHASE.md` |
| Role of team dynamics per phase | same |
| Five team roles | `agents/FLEET.md` |
| Agile, Scrum, Kanban | `references/agile-devops-plan-driven.md` |
| DevOps, CI, CD, automation | same |
| Plan-driven approaches | same |
| Four lessons from industry | same, plus `templates/process-style.md` |

---

## Revising with Ìlànà

```
ilana tutor: explain the difference between an audit and a review
ilana drill: phase 07
ilana drill: gauntlet
ilana drill: scenario
```

`TUTOR` mode teaches with the confusion pairs and worked examples. `DRILL` mode tests, marks
honestly, and tells you which phase your errors cluster in.

The full original deck is in `source/`, so you can always go back to the primary text.

---

## The exam-critical distinctions

The ones that carry the most marks and are most often confused. Full list in `modes/tutor.md`.

| Pair | The test |
| --- | --- |
| Verification vs validation | building it right vs building the right thing |
| SQA vs testing | process-oriented prevention vs product-oriented detection |
| Review vs audit | technical content vs process compliance |
| Walkthrough vs inspection | author-led and informal vs Moderator, Reader, Recorder |
| Integration vs system testing | interfaces between components vs the whole against the SRS |
| Alpha vs beta | at the developer site vs real users in a real environment |
| CI vs CD | integrate and test on commit vs release after validation |
| Scrum vs Kanban | fixed-length sprints vs continuous flow with WIP limits |
| Product vs process vs project metric | the artifact vs the activity vs the endeavour |
| CMMI 3 vs 4 | standardised and documented vs quantitatively controlled |
| Primary vs supporting vs organizational | building it vs enabling it vs governing it |
| Severity vs priority | technical impact vs business urgency |
