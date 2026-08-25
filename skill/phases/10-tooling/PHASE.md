# PHASE 10 - TOOLING

Owner: `configuration-engineer`. Support: `conductor`. Continuous: runs alongside every phase.

> Managing software activities manually is difficult, time-consuming and error-prone.
> Organisations use tools to automate, monitor and improve the software development process.

Tools do not create process. They enforce a process that already exists, or they impose one
nobody chose. This phase is about choosing deliberately.

---

## What this phase produces

| Artifact | Path | Template |
| --- | --- | --- |
| Toolchain decision record | `docs/toolchain.md` | `templates/toolchain-decision.md` |
| CI pipeline definition | `.github/workflows/` or equivalent | `templates/ci-pipeline.md` |
| Board configuration | documented in the toolchain record | `templates/board-setup.md` |

---

## Software process support tools

Software process support tools are applications that assist developers, testers, project managers
and stakeholders in planning, developing, testing, deploying and maintaining software systems.

**Benefits:** improved productivity; better collaboration; enhanced software quality; reduced
development time; automated repetitive tasks; improved project visibility and tracking; faster
delivery.

---

## CASE tools

CASE stands for Computer Aided Software Engineering: development and maintenance of software
projects with the help of automated software tools.

CASE tools are software application programs used to automate SDLC activities. They are used by
project managers, analysts and engineers. Categories available include analysis tools, design
tools, project management tools, database management tools and documentation tools. Their use
accelerates development and helps uncover flaws before moving to the next stage.

### Components

**Central repository.** CASE tools require a central repository serving as a source of common,
integrated and consistent information: product specifications, requirement documents, related
reports and diagrams, and management information. It also serves as a data dictionary.

**Upper CASE tools.** Used in the planning, analysis and design stages. Their primary goal is to
improve system quality, reduce development errors, and provide clear documentation during
planning and design.

Example: a bank developing an online banking system. Using an upper CASE tool, analysts document
requirements such as customers can transfer funds, customers can view account balances, the
system must operate 24/7, transactions must be secure. The tool stores and organises these for
future reference. It also supports system design (converting requirements into a blueprint) and
modeling (graphical representations that improve understanding).

**Lower CASE tools.** Support the later phases: implementation, testing, deployment and
maintenance, after analysis and design are complete. They help developers write code
efficiently, identify and fix errors, test applications automatically, and maintain software.

Stages supported: coding, testing, maintenance.
Major functions: code generation, debugging, automated testing.

| Tool | Primary use | Key features |
| --- | --- | --- |
| Selenium | automated testing | browser automation, regression testing |
| Eclipse IDE | coding and debugging | code editing, compilation, plugins |
| Visual Studio | coding, debugging and testing | full-featured IDE, testing, deployment tools |

Advantages: increase developer productivity; reduce coding errors; automate repetitive tasks;
improve software quality; accelerate testing; simplify debugging; support maintenance; reduce
development costs; enhance collaboration; improve reliability.

**Integrated CASE tools.** Support the entire SDLC, from planning and requirements gathering to
design, coding, testing, deployment and maintenance. They combine upper and lower CASE functions
in a single environment, so all project activities are connected and managed consistently.

| Tool | Provides |
| --- | --- |
| IBM Rational Suite | requirements management, UML modeling, software design, testing and quality assurance, configuration management; maintains traceability between requirements, design, code and tests |
| Oracle Designer | system analysis, database design, process modeling, application generation |
| SAP PowerDesigner | business process modeling, data modeling, enterprise architecture design, impact analysis, documentation generation |

### Features, advantages, limitations

**Features:** diagramming and modeling; documentation generation; code generation; version
control support; requirement management; testing support; reverse engineering.

**Advantages:** improved software quality; better documentation; faster development; increased
consistency; easier maintenance.

**Limitations:** high acquisition cost; training requirements; complexity; resistance to
adoption by team members.

---

## Project management tools

Applications that help teams plan, organise, monitor and control project activities across the
SDLC, so projects are completed on time, within budget, and to requirements and quality
standards.

Without them, large projects become difficult to control because of missed deadlines, poor
communication, resource conflicts and unclear responsibilities.

Examples: Microsoft Project, Jira, Asana, Trello, Monday.com.

### Functions

1. **Task assignment.** Distributing work according to skills, experience and responsibilities.
   Example: requirements analysis to the business analyst, UI design to the designer.
2. **Schedule tracking.** Timelines, milestones and dependencies.
3. **Resource management.** People, tools and budget.
4. **Progress monitoring.** Dashboards that show status and surface issues early. A dashboard
   might show completed tasks, tasks in progress and overdue items, so managers can quickly
   determine whether the project is on track.
5. **Team collaboration.** Constant communication among team members within a shared project
   workspace.
6. **Risk management.** Recording risks, likelihood, impact and mitigation, including measures
   such as assigning backup personnel.
7. **Reporting.** Status reports for stakeholders.

**Importance:** helps organisations plan realistically, coordinate work, see status, and deliver
predictably.

**Advantages:** clearer responsibility; visible progress; earlier detection of problems; better
communication; historical data for future estimation.

**Limitations:** advanced tools may require expensive licences and subscriptions; team members
may need training; incorrect updates can lead to misleading reports and decisions.

That last limitation is the important one. **A project board is only as truthful as the people
updating it.** A board that is out of date is worse than no board, because decisions are made
from it.

### Jira

Jira is based on three concepts: **project**, **issue** and **workflow**. It integrates with many
version control and development tools.

Key features:
- **Issue tracking.** Tracks bugs, tasks, stories and epics.
- **Agile support.** Supports Scrum and Kanban boards, backlogs and sprint progress tracking.
- **Workflow management.** Custom workflows matching organisational processes, for example
  `To Do -> In Progress -> Testing -> Done`.
- **Reporting.** Burndown charts, velocity, dashboards.

Benefits: strong traceability, mature integrations, configurable to the real process.
Limitations: complexity, administration overhead, cost, and a strong tendency towards
over-configuration.

### Trello

A visual, board-based tool built on three structures:

| Structure | Meaning | Example |
| --- | --- | --- |
| **Board** | an entire project, department or workflow | "E-commerce Website Project" |
| **List** | a stage of work within the board | To Do, Doing, Done |
| **Card** | an individual work item | "Develop payment module" |

A card may contain a description, checklist, due date, attachments, assigned members, labels and
comments.

Features: team members can comment, attach and assign; supports management activities; integrates
with other tools.
Benefits: easy to learn; projects can be created in minutes; works well for small teams and
simple workflows; flexible across project types.
Limitations: limited reporting; weaker for complex workflows and large programmes; no built-in
estimation or velocity.

**Choosing between them:** Trello for small teams and simple flows where the board is the whole
process. Jira where traceability, reporting and complex workflows are genuinely needed. The
common failure is adopting Jira and configuring it into something nobody updates.

---

## Continuous integration tools

CI automatically builds and tests software whenever code changes are committed.

| Tool | Nature |
| --- | --- |
| Jenkins | self-hosted, extremely extensible, plugin ecosystem, you operate it |
| GitHub Actions | hosted with the repository, YAML workflows, strong ecosystem |
| GitLab CI/CD | integrated with GitLab, single-file pipeline definition |

Benefits: early bug detection, faster development, improved software quality.

### What a pipeline must do

At minimum, and in this order, so the cheapest check fails first:

```
lint -> build -> unit tests -> integration tests -> static analysis
     -> security scan -> package -> deploy to staging -> smoke test
```

At `RIGOUR` 3 and above, the pipeline is the gate. A merge that has not passed it does not enter
the main branch.

---

## The DevOps toolchain

The reference mapping. Being able to state which tool does what is a basic professional
competence.

| Category | Tools | Purpose |
| --- | --- | --- |
| Version control | Git, GitHub, GitLab | track and manage source changes |
| CI/CD | Jenkins, GitHub Actions, GitLab CI/CD | automate build, test and deployment |
| Testing | Selenium, JUnit, Cypress, TestNG, Appium | automated verification |
| Containerisation | Docker | package an application with its environment |
| Orchestration | Kubernetes | run and scale containers across nodes |
| Configuration and deployment | Ansible, Terraform | reproducible infrastructure and configuration |
| Build | Maven, Gradle, Ant, Make | compile and package |
| Defect tracking | Jira, Bugzilla, Redmine, MantisBT | manage the defect lifecycle |
| Documentation | Doxygen, DrExplain, Adobe RoboHelp | generate technical and user documentation |

---

## Ìlànà's position on tools

1. **Process first, tool second.** A tool adopted before the process is defined imposes its
   defaults on you, and its defaults were designed for someone else.
2. **Every tool is a dependency.** Cost, licence, lock-in, operational burden and a migration
   path all belong in the decision record.
3. **A tool nobody updates is worse than no tool**, because people make decisions from stale data.
4. **Automate the repetitive, keep humans on the judgemental.** Regression testing, builds and
   deployments should be automatic. Requirements elicitation, design trade-offs, exploratory
   testing and ethical judgement should not.
5. **The pipeline is the enforcement surface.** Whatever the standards say, what CI blocks is
   what actually holds.
