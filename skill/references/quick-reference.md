# QUICK REFERENCE

The whole of SEN102/212 in a form you can scan.

---

## Requirements

**Five stages:** Elicitation, Analysis, Specification, Validation, Management. Cyclical.

**Eight elicitation techniques:** interviews, questionnaires, workshops, brainstorming,
observation, document analysis, use cases and scenarios, prototyping.

**Three types:**
| Type | Asks | Example |
| --- | --- | --- |
| Functional | what must it do | place, edit and cancel an order |
| Non-functional | how well | transaction time under 2 seconds |
| Domain | what the field requires | PCI-DSS for payment handling |

**Six challenges:** ambiguity, incompleteness, change, conflict, communication issues, technical
constraints.

**Six strategies:** clear documentation, regular stakeholder engagement, change management,
conflict resolution mechanisms, effective communication techniques, modern tools.

---

## Design

**Three levels:** architecture (conceptual integrity of the whole), high-level (subsystems and
modules and their interaction), detailed (data structures and algorithms per module).

**Six objectives:** correctness, completeness, efficiency, flexibility, consistency,
maintainability.

---

## Interface

**Two types:** text-based (keyboard, recall-based, harder navigation, more customisable) and
graphical (pointer, recognition-based, easier navigation, fewer options).

**GUI characteristics:** windows, icons, menus, pointing, graphics.

**Five principles:** structure, simplicity, visibility, feedback, tolerance.

---

## Construction

**Three goals of coding:** translate design into executable form; reduce the cost of later
phases; make the program readable.

**Standards:** indentation, inline comments, limits on globals, structured programming (no
`goto`), naming conventions, error return and exception conventions.

**Guidelines:** line length at or below 80; spacing; one comment per three source lines;
function length under about 10 lines; no `goto`; inline comments; meaningful error messages.

---

## Verification

**Process:** requirement analysis, test planning, test case design, environment setup,
execution, defect reporting, test closure.

**Four levels:**
| Level | Tests | By | Finds |
| --- | --- | --- | --- |
| Unit | individual components | developers | logic errors |
| Integration | module interfaces | developers, testers | interface and data flow errors |
| System | the whole against the SRS | independent testers | system-wide defects |
| Acceptance | against business need | users, clients | fitness for purpose |

**Integration strategies:** top-down, bottom-up, big bang.
**Acceptance types:** UAT, alpha (developer site), beta (real users, real environment).
**System testing types:** functional, performance, security, usability, stress.

**Test plan components:** objectives, scope, strategy, environment, roles and responsibilities,
risk analysis, schedule, deliverables, exit criteria.

**Defect life cycle:** New, Assigned, Open, Fixed, Retest, Verified, Closed.
Alternatives: Reopened, Deferred, Rejected.

**Defect report fields:** ID, Title, Description, Severity, Priority, Steps to Reproduce,
Expected Result, Actual Result, Status.

**Automation suits:** regression, repetitive, load, smoke.
**Automation challenges:** high initial cost, maintenance complexity, skilled personnel, tool
compatibility.

---

## Configuration management

**Four pillars:** version control, change management, build management, release management.

**VCS types:** centralized (SVN, one central repository), distributed (Git, full local repository
per developer).

**Git commands:** `init`, `clone`, `add`, `commit`, `push`, `pull`, `branch`, `merge`.

**Change process:** submit, evaluate (impact analysis), approve or reject, implement, test,
document.
**Change types:** corrective, adaptive, perfective, preventive.

**Build tools:** Maven (Java), Gradle, Ant, Make (C/C++).

**Release types:** major, minor, patch, emergency.

---

## Quality assurance

**SQA is process-oriented and prevention-focused. Testing is product-oriented and
detection-focused.**

**Five core activities:** quality planning, reviews, audits, software metrics, testing.

**Quality planning output:** the Quality Management Plan.

**Four review activities:**
| Activity | Led by | Formality | Roles |
| --- | --- | --- | --- |
| Peer review | a peer | low | none |
| Walkthrough | the author | informal | none |
| Inspection | a Moderator | formal | Moderator, Reader, Recorder |
| Audit | independent personnel | formal | auditor |

**Three metric categories:**
| Category | Measures | Examples |
| --- | --- | --- |
| Product | the artifact | lines of code, complexity, defect density |
| Process | the activity | defect rate, time to fix, process cycle time |
| Project | the endeavour | cost variance, schedule adherence |

**Defect density** = defects / KLOC. 10 bugs in 5,000 lines = 2 per KLOC.
**Cost variance** = planned minus actual. Actual above planned is negative: over budget.
**Schedule adherence**: planned 10 days, completed in 10 days, is high.

**Seven quality attributes:** correctness, reliability, efficiency, usability, maintainability,
portability, security.

---

## Process assessment and improvement

**SPI activities:** identify weaknesses, introduce improvements, monitor impact.
**The cycle:** Measure -> Analyze -> Improve -> Repeat.

**CMMI five levels:** 1 Initial (chaotic), 2 Managed (planned and tracked), 3 Defined
(standardised across the organisation), 4 Quantitatively Managed (statistical control),
5 Optimizing (continuous refinement, prevention).

**ISO/IEC 12207 three categories:**
| Category | Contains |
| --- | --- |
| Primary | requirements analysis, design, implementation, testing, maintenance |
| Supporting | documentation, configuration management, quality assurance, verification and validation |
| Organizational | process improvement, training, infrastructure management |

**Process optimization techniques:** automation of tasks, adoption of best practices, continuous
monitoring and feedback, use of metrics for decision-making.

---

## Process modeling

**Notations:** UML activity diagrams, BPMN, flowcharts, Petri nets, data flow diagrams.

**Activity diagram elements:** start node, action nodes, control flow, decision, condition, fork,
join, merge, signal send, signal receipt, note, final flow node.

**Good process model:** simplicity, accuracy, completeness, consistency, maintainability,
traceability.

**Good documentation:** accuracy, completeness, clarity, consistency, maintainability,
accessibility.

**Five documentation types:** requirements, design, technical, user, testing.

**Process document sections:** purpose, scope, inputs, activities, outputs, roles.

**Workflow components:** activities, roles, inputs, outputs, decision points.

---

## Tooling

**CASE tools:** upper (planning, analysis, design), lower (coding, testing, maintenance),
integrated (whole lifecycle). All share a central repository that also serves as a data
dictionary.

**Trello structure:** board, list, card.
**Jira concepts:** project, issue, workflow.

---

## Ethics and teams

**Ethical software is:** safe, reliable, secure, fair.

**Five ethical issues:** honesty and integrity, confidentiality, quality and safety, intellectual
property rights, professional responsibility.

**ACM/IEEE four principles:** public interest, client and employer responsibilities, product
quality, professional competence.

**Five characteristics of effective teams:** clear roles and responsibilities, effective
communication, collaboration and cooperation, trust and respect, conflict management.

**Five team roles:** Project Manager, Software Developer, Tester/QA Engineer, Business Analyst,
DevOps Engineer.

**Scrum roles:** Product Owner, Scrum Master, Development Team.
**Scrum events:** sprint planning, daily scrum, sprint review, sprint retrospective.
**Kanban:** continuous flow, visual board, WIP limits.
**DevOps:** CI, CD, automation.
**Plan-driven:** full specification in advance, strict control, detailed documentation.

**Four lessons from industry:** no single process fits all projects; process selection depends on
project type; flexibility is important; continuous improvement is essential.
