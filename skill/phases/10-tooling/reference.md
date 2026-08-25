# PHASE 10 REFERENCE

## Software process support tools

Software development involves requirements gathering, system analysis and design, coding,
testing, deployment and maintenance. Managing these activities manually can be difficult,
time-consuming and error-prone, so organisations use software tools to automate, monitor and
improve the development process.

**Definition.** Software process support tools are software applications that assist developers,
testers, project managers and stakeholders in planning, developing, testing, deploying and
maintaining software systems.

**Benefits:** improved productivity; better collaboration among team members; enhanced software
quality; reduced development time; automated repetitive tasks; improved project visibility and
tracking; faster delivery of software products.

## CASE tools

CASE stands for Computer Aided Software Engineering: development and maintenance of software
projects with the help of various automated software tools.

CASE tools are a set of software application programs used to automate SDLC activities. They are
used by software project managers, analysts and engineers. A number of CASE tools exist to
simplify various stages of the SDLC, including analysis tools, design tools, project management
tools, database management tools and documentation tools.

Use of CASE tools accelerates the development of a project to produce the desired result and
helps uncover flaws before moving ahead with the next stage in software development.

### Components

**Central repository.** CASE tools require a central repository which serves as a source of
common, integrated and consistent information. The central repository is a central place of
storage where product specifications, requirement documents, related reports and diagrams, and
other useful management information are stored. The central repository also serves as a data
dictionary.

**Upper CASE tools.** Used in the planning, analysis and design stages of the SDLC. Their primary
goal is to improve system quality, reduce development errors, and provide clear documentation
during the planning and design stages.

Example: requirements analysis involves identifying, gathering, documenting and validating the
needs of users and stakeholders. For instance, a bank wants to develop an online banking system.
Using an upper CASE tool, analysts can document requirements such as: customers can transfer
funds; customers can view account balances; the system must operate 24/7; transactions must be
secure. The tool stores and organises all these requirements for future reference.

System design converts requirements into a detailed blueprint for developers. Modeling is the
process of creating graphical representations of the system to improve understanding.

**Lower CASE tools.** Software tools that support the later phases of the SDLC. These phases occur
after system analysis and design have been completed and focus on implementation, testing,
deployment and maintenance. Lower CASE tools help developers write code efficiently, identify and
fix errors, test applications automatically, and maintain software throughout its lifecycle.

Stages supported: coding, testing, maintenance.
Major functions: code generation, debugging, automated testing.
Common tools: Selenium, Eclipse IDE, Visual Studio.

| Tool | Primary use | Key features |
| --- | --- | --- |
| Selenium | Automated testing | Browser automation, regression testing |
| Eclipse IDE | Coding and debugging | Code editing, compilation, plugins |
| Visual Studio | Coding, debugging and testing | Full-featured IDE, testing, deployment tools |

Advantages of lower CASE tools: increase developer productivity; reduce coding errors; automate
repetitive tasks; improve software quality; accelerate testing processes; simplify debugging;
support software maintenance; reduce development costs; enhance collaboration among development
teams; improve reliability of software products.

**Integrated CASE tools.** Support the entire SDLC, from planning and requirements gathering to
design, coding, testing, deployment and maintenance. They combine the functions of upper CASE and
lower CASE tools into a single environment, allowing all project activities to be connected and
managed consistently.

1. **IBM Rational Suite** provides tools for requirements management, UML modeling, software
   design, testing and quality assurance, and configuration management. It helps teams
   collaborate efficiently and maintain traceability between requirements, design, code and tests.
2. **Oracle Designer** is used for system analysis, database design, process modeling and
   application generation. It supports developers in creating enterprise applications with strong
   database integration.
3. **SAP PowerDesigner** offers business process modeling, data modeling, enterprise architecture
   design, impact analysis and documentation generation. It is widely used in large organisations
   to manage complex information systems.

**Features of CASE tools:** diagramming and modeling; documentation generation; code generation;
version control support; requirement management; testing support; reverse engineering.

**Advantages of CASE tools:** improved software quality; better documentation; faster
development; increased consistency; easier maintenance.

**Limitations of CASE tools:** high acquisition cost; training requirements; complexity;
resistance to adoption by team members.

## Project management tools

**Definition.** Project management tools are software applications that help software development
teams plan, organise, monitor and control project activities throughout the SDLC. They enable
project managers and team members to coordinate tasks, track progress, manage resources,
communicate effectively, and ensure projects are completed on time, within budget, and according
to requirements and quality standards.

Without project management tools, large software projects can become difficult to control due to
missed deadlines, poor communication, resource conflicts and unclear responsibilities.

**Examples:** Microsoft Project, Jira, Asana, Trello, Monday.com.

**Functions:** task assignment; schedule tracking; resource management; progress monitoring; team
collaboration; risk management; reporting.

Task assignment involves distributing project work among team members according to their skills,
experience and responsibilities. For example, requirements analysis is assigned to the business
analyst and UI design to the designer.

Progress monitoring surfaces issues early. A dashboard may show completed tasks, tasks in
progress and overdue items, so managers can quickly determine whether the project is on track.

Team collaboration matters because software projects require constant communication among team
members, within a shared project workspace.

Risk management includes recording risks and mitigation measures such as assigning backup
personnel.

**Advantages:** clearer responsibility; visible progress; earlier detection of problems; better
communication.

**Limitations:** advanced tools may require expensive licences and subscriptions; team members
may need training to use the software effectively; incorrect updates can lead to misleading
reports and decisions.

## Jira

Jira is based on three concepts: **project**, **issue** and **workflow**. It integrates with many
version control systems and development tools.

**Key features:**
- **Issue tracking:** tracks bugs, tasks, stories and epics.
- **Agile support:** supports Scrum and Kanban boards, backlogs, and sprint progress tracking.
- **Workflow management:** custom workflows can be created to match organisational processes, for
  example `To Do -> In Progress -> Testing -> Done`.
- **Reporting:** provides charts and dashboards.

**Benefits:** strong traceability; wide integration; configurable.
**Limitations:** complexity; administrative overhead; cost.

## Trello

Trello is a visual, board-based project management tool.

**Structure:**
- **Board.** Represents an entire project, department or workflow. Example: "E-commerce Website
  Project" contains all tasks needed to build an online shopping platform. Boards provide a clear
  overview.
- **Lists.** Represent stages of work within a board.
- **Cards.** Represent individual work items. Example: "Develop Payment Module".

**Information stored in cards:** description, checklist, due date, attachments, assigned members,
labels, comments.

**Features:** team members can comment, attach files and assign work; supports management
activities; integrates with other tools.

**Benefits:** easy to learn and use; projects can be created within minutes; works exceptionally
well for small teams and simple workflows; can manage various types of projects.

**Limitations:** limited reporting; weaker for complex workflows and large programmes.

## Continuous integration tools

Continuous Integration automatically builds and tests software whenever code changes are
committed.

**Benefits:** early bug detection; faster development; improved software quality.
**Tools:** Jenkins, GitHub Actions, GitLab CI/CD.

## DevOps tool mapping

| Tool | Primary function |
| --- | --- |
| Git | version control |
| Jenkins | CI/CD automation |
| Docker | containerisation |
| Kubernetes | container orchestration |
| Selenium | automated testing |
| Ansible | configuration management and deployment automation |
