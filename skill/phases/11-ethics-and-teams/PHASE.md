# PHASE 11 - ETHICS, TEAM DYNAMICS AND INDUSTRY PRACTICE

Owner: `ethics-officer`. Support: `conductor`. Continuous: constrains every other phase.

> Software engineers build systems that affect people's lives every day. They have a
> responsibility not only to produce working software, but to produce software that is safe,
> trustworthy and beneficial to society.

This phase holds the veto. Article 1 lives here.

---

## What this phase produces

| Artifact | Path | Template |
| --- | --- | --- |
| Ethics register | `.ilana/ethics.md` | `templates/ethics-review.md` |
| Roles and responsibility matrix | `docs/raci.md` | `templates/raci.md` |
| Communication plan | `docs/communication-plan.md` | `templates/communication-plan.md` |
| Process style decision | `docs/process-style.md` | `templates/process-style.md` |

---

# PART A: PROCESS ETHICS

## What software engineering ethics is

The moral principles and professional standards that guide software engineers in developing and
maintaining software responsibly. In plain terms: doing the right thing while designing,
developing, testing and maintaining software systems.

An ethical software engineer develops software that is:

| Property | Meaning |
| --- | --- |
| **Safe** | it does not put users at risk |
| **Reliable** | it works correctly and consistently |
| **Secure** | it protects users' data from unauthorised access |
| **Fair** | it treats all users equally without discrimination or bias |

What happens when ethical standards are ignored: system failures where software stops working or
produces incorrect results; data breaches exposing sensitive information; loss of public trust;
legal consequences including lawsuits and fines.

Two examples that make it concrete:

- You build software for a hospital. Doctors use it to diagnose patients and prescribe
  medication. If you are careless and it calculates the wrong drug dosage, a patient receives the
  wrong treatment.
- You build software for a bank and intentionally leave a hidden backdoor so you can access
  customer accounts later. That is not a programming mistake. It is a criminal offence.

## Why ethics runs through the whole process

Ethics is not something that becomes relevant after the software is finished. It applies from the
moment a project begins until the software is deployed and maintained. **Ethics is not separate
from the software process; it is part of every stage.**

Ethical practice:
- **protects users and stakeholders** by ensuring the software does not cause unnecessary harm,
- **ensures honesty and transparency** by communicating truthfully about capabilities and
  limitations,
- **promotes accountability** by making developers take responsibility for the quality and impact
  of what they build,
- **maintains professional integrity** by following professional standards.

## The five key ethical issues

### 1. Honesty and integrity
- Provide accurate information about system capabilities. Communicate clearly what the software
  can and cannot do, without exaggeration.
- Avoid misleading stakeholders. Clients, users and management receive truthful, transparent
  information.
- Report issues truthfully. Disclose bugs, risks and project challenges honestly, without
  concealing problems.

### 2. Confidentiality
- Protect user information. Safeguard sensitive personal and organisational data.
- Avoid unauthorised disclosure. Never share confidential information without proper permission.
- Follow data protection policies. Comply with organisational and legal requirements.

### 3. Quality and safety
- Software meets required standards.
- Systems are safe for users, not exposing them to unnecessary risk or harm.
- Risks are properly addressed: identified, evaluated and mitigated during development.
- **Neglecting quality for speed or cost is unethical.**

### 4. Intellectual property rights
- Respect copyright laws.
- Use and distribute software according to its licence terms.
- Acknowledge and respect the rightful ownership of code, designs and innovations.

### 5. Professional responsibility
- Follow established processes and approved development methods.
- Adhere to professional, organisational and industry standards.
- Take responsibility for the quality, reliability and consequences of the software produced.

## Ethics in process adherence

Some people think development processes are guidelines that can be ignored under pressure. That
is not the case. **Following a defined software process is not just a technical requirement; it
is an ethical responsibility.**

Three examples the course gives explicitly:

- A team **skips testing** to meet a deadline. The software ships on time. If it contains serious
  bugs affecting users, that is unethical, because the team knowingly released software that had
  not been properly tested.
- A team **ignores documentation standards**. Other team members later struggle to understand,
  maintain or improve the software. That is unethical because it creates unnecessary problems for
  others.
- A team **bypasses code or design reviews** to save time. Reviews exist to identify errors,
  improve quality and reduce risk before release.

Process adherence is directly linked to ethical responsibility. A responsible engineer follows
established processes not because the organisation requires it, but because it is the right thing
to do for users, the organisation and society.

## Professional codes of ethics

Software engineers do not simply decide for themselves what is right. Professional bodies develop
rules and standards.

- **ACM**: Association for Computing Machinery.
- **IEEE**: Institute of Electrical and Electronics Engineers.

Both are internationally recognised professional bodies that establish standards and publish
guidelines, including codes of ethics.

The **ACM/IEEE Software Engineering Code of Ethics** is the most widely recognised. Four
principles it emphasises:

| Principle | Requirement |
| --- | --- |
| **Public interest** | Act in ways that benefit and protect the public. Do not knowingly release unsafe software. Always consider how the work affects users and society. |
| **Client and employer responsibilities** | Be honest, trustworthy and loyal. Do not hide important problems in a system or misuse company resources for personal gain. |
| **Product quality** | Ensure the software meets acceptable quality standards. Carry out proper testing. Avoid releasing software with known defects or serious faults. |
| **Professional competence** | Possess the knowledge and skills to perform duties effectively. Continue learning. Avoid accepting tasks beyond your level of competence. |

When employer instruction conflicts with public safety, **public interest takes precedence.**

---

# PART B: TEAM DYNAMICS

## What team dynamics are

Software development is rarely a one-person job. A typical team includes software developers,
system analysts, UI/UX designers, testers, database administrators and project managers, all
working towards a common goal.

**Team dynamics** are the patterns of interaction, communication and collaboration among team
members. In plain terms: how well team members work together.

**Benefits of effective team dynamics:**
- **Higher productivity**, because members work efficiently and complete tasks on time.
- **Better quality software**, because collaboration helps identify and correct errors.
- **Reduced conflicts**, because members communicate openly, respect one another's opinions and
  resolve disagreements professionally.

Technical skills alone are not enough. The ability to work effectively with others is equally
important.

## The five characteristics of effective teams

### 1. Clear roles and responsibilities
Every member knows their tasks, understands the duties they are accountable for, and recognises
how their work supports the project's overall success.

### 2. Effective communication
Produces clear understanding of requirements, proper coordination of tasks, and quick resolution
of issues.

### 3. Collaboration and cooperation
Work together towards common goals; share knowledge and ideas; support each other.

### 4. Trust and respect
Trust strengthens teamwork by creating a united, cooperative environment. Respect encourages
honest and transparent communication. Mutual trust motivates people to work together.

### 5. Conflict management
Open discussion to identify the root cause; negotiation to find fair compromises; respectful
resolution that maintains positive working relationships.

## How team dynamics affect each phase

| Phase | What good dynamics produce | What poor dynamics produce |
| --- | --- | --- |
| **Requirements gathering** | clear communication with stakeholders, correct understanding of user needs | incorrect or incomplete requirements, affecting the entire project |
| **Design decisions** | developers, analysts and designers collaborate on structure | poor or inconsistent design decisions that damage quality |
| **Testing** | testers provide accurate information, developers fix quickly | defects remain unresolved, low-quality software |
| **Deployment** | developers, testers and operations work in sync | deployment failures, system downtime, unstable software |

Poor team dynamics lead to misunderstood requirements, project delays and low-quality software.

## Team roles

| Role | Responsibility |
| --- | --- |
| **Project Manager** | Plans, coordinates and monitors the project to ensure it is completed on time, within budget and according to requirements. |
| **Software Developer** | Designs, writes, tests and maintains the application based on project specifications. |
| **Tester / QA Engineer** | Verifies that the software functions correctly by identifying defects and ensuring quality standards are met. |
| **Business Analyst** | Gathers, analyses and documents business requirements so the software meets user and organisational needs. |
| **DevOps Engineer** | Automates deployment, manages infrastructure, and ensures CI/CD processes run efficiently. |

Each role performs specialised responsibilities that collectively ensure successful development
and delivery.

---

# PART C: INDUSTRY PRACTICES

## Agile

Many companies develop software in small iterations with continuous feedback and frequent
releases.

**Scrum.** Work is organised into short, fixed time periods called sprints, usually two to four
weeks. Each sprint focuses on a specific set of tasks, and at the end a working portion of the
software is delivered.

| Role | Responsibility |
| --- | --- |
| Product Owner | determines what should be built; manages and prioritises the Product Backlog by business value |
| Scrum Master | ensures Scrum practices are followed and removes impediments affecting the team |
| Development Team | builds the software |

| Event | Purpose |
| --- | --- |
| Sprint Planning | define the Sprint Goal and select Product Backlog items |
| Daily Scrum | synchronise activities and identify impediments, daily |
| Sprint Review | evaluate the completed increment with stakeholders |
| Sprint Retrospective | analyse what went well and what should improve |

| Artifact | Contains |
| --- | --- |
| Product Backlog | all desired features, enhancements, bug fixes and technical improvements planned |
| Sprint Backlog | the items selected for the current sprint |
| Increment | the working software delivered |

**Kanban.** Focuses on visualising and managing work as it progresses. Tasks are displayed on a
board and move through stages such as To Do, In Progress and Done. Unlike Scrum, Kanban does not
use fixed time periods; work flows continuously. It emphasises limiting Work in Progress to avoid
overload, reduce bottlenecks and improve workflow efficiency.

**Agile characteristics:** iterative development, continuous feedback, frequent releases.

## DevOps

A modern approach integrating development and operations activities into a unified process. In
traditional environments developers write and build software while operations teams handle
deployment and maintenance. DevOps brings these groups together to work collaboratively across
the entire lifecycle, improving efficiency and reducing delays.

- **Continuous Integration (CI):** frequently integrating code changes into a shared repository
  where they are automatically built and tested, so errors are detected early and the software
  remains stable.
- **Continuous Deployment (CD):** software is automatically released to users once it has passed
  all necessary tests, enabling faster and more reliable delivery.
- **Automation:** building, testing and deployment performed automatically using specialised
  tools. Version control (Git, GitHub, GitLab); CI/CD (Jenkins, GitHub Actions, GitLab CI/CD);
  testing (Selenium, JUnit); configuration and deployment (Docker, Kubernetes, Ansible). This
  reduces manual effort, minimises human error and accelerates development.

## Plan-driven approaches

Development methods where everything is carefully planned in advance. Requirements are fully
specified, design is documented, processes are recorded. Nothing is left unclear or informal. The
process must be followed exactly as planned, each stage completed before moving to the next.
Changes are not easily allowed and work is closely monitored.

**Used in:** government projects; safety-critical systems such as medical and aviation systems,
because these require high reliability and strict control.

**Characteristics:** detailed documentation; strict process control.

## Lessons from industry practice

No single software development process is suitable for all projects. The choice depends on the
type of project, flexibility is required to adapt to changes, and continuous improvement is
necessary.

Small projects with few requirements can use flexible methods like Agile. Large, complex projects
may require a more structured and detailed approach such as a plan-driven model. Safety-critical
systems such as medical or aviation software, where errors can be dangerous, require strict
processes, detailed documentation and careful control. Mobile applications and websites that
change frequently require flexible, adaptive methods.

Projects also differ in time constraints, budget, team size and customer involvement. A single
process cannot effectively address all project needs.

**The four lessons:**
1. No single process fits all projects.
2. Process selection depends on project type.
3. Flexibility is important.
4. Continuous improvement is essential.

**Hybrid is often the right answer.** A regulated healthcare project that must satisfy stringent
documentation requirements while also incorporating periodic customer feedback is best served by
combining plan-driven governance with Agile development practice. A financial institution using
Git, Jenkins, Docker and Kubernetes while maintaining formal documentation and regulatory
approval procedures is integrating modern DevOps inside a controlled process, and that is a
mature position, not a contradiction.

---

## Exit

This phase is continuous. Its register is reviewed at G8, where every `ETH-###` must be
dispositioned.
