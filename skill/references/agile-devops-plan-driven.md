# AGILE, DEVOPS AND PLAN-DRIVEN

No single process fits all projects. This card is for choosing, not for advocacy.

---

## Agile

Developing software in small iterations, receiving continuous feedback, releasing frequently.

**Characteristics:** iterative development, continuous feedback, frequent releases.

### Scrum

Work is organised into short, fixed time periods called sprints, usually two to four weeks. During
each sprint the team focuses on a specific set of tasks; at the end, a working portion of the
software is delivered.

**Roles**

| Role | Responsibility |
| --- | --- |
| Product Owner | determines what should be built; maximises product value by managing and prioritising the Product Backlog |
| Scrum Master | ensures Scrum practices are followed correctly and removes impediments affecting the development team |
| Development Team | builds the software |

**Events**

| Event | Cadence | Purpose |
| --- | --- | --- |
| Sprint Planning | per sprint | define the Sprint Goal and select Product Backlog items |
| Daily Scrum | daily | synchronise activities and identify impediments |
| Sprint Review | per sprint | evaluate the completed increment with stakeholders |
| Sprint Retrospective | per sprint | analyse what went well and what should be improved |

**Artifacts**

| Artifact | Contains |
| --- | --- |
| Product Backlog | all desired features, enhancements, bug fixes and technical improvements planned for future development |
| Sprint Backlog | the items committed for the current sprint |
| Increment | the working software delivered |

**Common failures:** committing significantly more backlog items than can reasonably be completed
(a violation of sustainable sprint commitment); repeated sprint failure from beginning
implementation before requirements are sufficiently clarified, which is addressed through backlog
refinement, collaborative estimation, retrospectives and historical velocity analysis.

### Kanban

Focuses on visualising and managing work as it progresses. Tasks are displayed on a board and move
through stages such as To Do, In Progress and Done.

Unlike Scrum, Kanban does not use fixed time periods; work flows continuously. It emphasises
limiting Work in Progress to avoid overload, reduce bottlenecks and improve workflow efficiency.

**The distinguishing feature is the WIP limit.** A board without WIP limits is a to-do list with
columns.

---

## DevOps

A modern approach integrating development and operations activities into a unified process. In
traditional environments developers write and build software while operations teams handle
deployment and maintenance. DevOps brings the two together across the entire lifecycle, improving
efficiency and reducing delays.

| Practice | Meaning |
| --- | --- |
| **Continuous Integration** | code changes are frequently integrated into a shared repository where they are automatically built and tested, so errors are detected early and the software remains stable |
| **Continuous Deployment** | software is automatically released once it has passed all necessary tests, enabling faster and more reliable delivery |
| **Automation** | building, testing and deployment performed automatically by specialised tools, reducing manual effort, minimising human error and accelerating development |

**CI versus CD:** CI focuses on automated code integration and testing. CD automates release after
successful validation. CI comes first.

**Infrastructure as code** is the DevOps practice that most directly prevents deployment failures
caused by configuration differences between environments.

---

## Plan-driven approaches

Software development methods where everything is carefully planned in advance before development
begins. Requirements are fully specified, design is documented, processes are recorded. Nothing is
left unclear or informal. The process must be followed exactly as planned; each stage must be
completed before moving to the next. Changes are not easily allowed and work is closely monitored.

**Used in:** government projects; safety-critical systems such as medical and aviation systems,
because these require high reliability and strict control.

**Characteristics:** detailed documentation; strict process control.

**Why uncontrolled change is discouraged:** it compromises traceability, planning, verification and
project predictability.

**The critical artifact:** a comprehensive Software Requirements Specification. It is the baseline
for design, and traceability management is the practice that supports it.

---

## Choosing

| Project characteristic | Points towards |
| --- | --- |
| Rapidly evolving customer requirements | Agile |
| Continuous customer availability | Agile |
| Stable regulatory requirements | plan-driven |
| Safety-critical operation | plan-driven, high rigour |
| Complete traceability required from requirements through deployment | plan-driven governance |
| Frequent deployment desired | DevOps emphasis |
| Large, complex, many teams | more structure |
| Small, simple, few requirements | Agile |

Examples that settle the question:
- Startup mobile application with continuously evolving requirements: Scrum.
- Government tax administration system with extensive regulatory compliance: plan-driven.
- Aircraft navigation software requiring extensive documentation before implementation: plan-driven.
- National electronic voting system: plan-driven governance, even with DevOps automation.
- Experimental social media prototype changing weekly: Agile.

---

## Hybrid, which is what most real projects are

Two recurring patterns, and both are mature positions rather than compromises.

**Plan-driven governance with Agile development.** A healthcare project that must satisfy stringent
regulatory documentation while incorporating periodic customer feedback. Governance artifacts are
plan-driven; construction and verification run in iterations.

**DevOps inside controlled process.** A financial institution adopting Git for version control,
Jenkins for CI, Docker for containerisation and Kubernetes for orchestration, while maintaining
formal documentation and regulatory approval procedures. This is integrating modern DevOps
practices within a controlled software engineering process.

For regulated financial software specifically: Agile development supported by formal
documentation, compliance reviews and controlled change management.

---

## The four lessons

1. No single process fits all projects.
2. Process selection depends on project type.
3. Flexibility is important.
4. Continuous improvement is essential.

Effective software engineering requires selecting, tailoring and continuously improving development
processes according to project objectives, risk, regulatory requirements, stakeholder needs and
organisational context.
