# TOOLS MAP

Which tool does what. Being able to state this correctly is a basic professional competence, and
it is a recurring assessment question.

## The canonical mapping

| Tool | Primary function |
| --- | --- |
| **Git** | version control |
| **GitHub, GitLab** | repository hosting and collaboration |
| **SVN** | centralized version control |
| **Jenkins** | CI/CD automation |
| **GitHub Actions** | CI/CD automation, hosted with the repository |
| **GitLab CI/CD** | CI/CD automation, integrated with GitLab |
| **Docker** | containerisation |
| **Kubernetes** | container orchestration across multiple computing nodes |
| **Ansible** | configuration management and deployment automation |
| **Terraform** | infrastructure as code |
| **Selenium** | automated browser-based functional testing |
| **Cypress** | frontend testing |
| **JUnit** | unit testing, Java |
| **NUnit** | unit testing, .NET |
| **PyTest** | unit testing, Python |
| **TestNG** | Java testing framework |
| **Appium** | mobile application testing |
| **Maven** | build management, Java projects |
| **Gradle** | build automation |
| **Ant** | Java builds |
| **Make** | C and C++ projects |
| **Jira** | issue tracking and project management |
| **Bugzilla** | defect tracking |
| **Redmine** | defect tracking and project management |
| **MantisBT** | defect tracking |
| **Azure DevOps** | defect tracking and lifecycle management |
| **Trello** | visual board-based project management |
| **Asana, Monday.com** | project management |
| **Microsoft Project** | project scheduling |
| **Eclipse IDE** | coding and debugging |
| **Visual Studio** | coding, debugging and testing |
| **Doxygen, DrExplain, Adobe RoboHelp** | documentation generation |

## CASE tool categories

| Category | Supports | Examples |
| --- | --- | --- |
| **Upper CASE** | planning, analysis, design | requirements and modeling tools |
| **Lower CASE** | coding, testing, maintenance | Selenium, Eclipse IDE, Visual Studio |
| **Integrated CASE** | the whole lifecycle | IBM Rational Suite, Oracle Designer, SAP PowerDesigner |

All CASE tools depend on a **central repository**, which also serves as the data dictionary.

| Integrated tool | Provides |
| --- | --- |
| IBM Rational Suite | requirements management, UML modeling, design, testing and QA, configuration management, traceability between requirements, design, code and tests |
| Oracle Designer | system analysis, database design, process modeling, application generation |
| SAP PowerDesigner | business process modeling, data modeling, enterprise architecture, impact analysis, documentation generation |

## Project management tool structures

**Jira** is built on three concepts: **project**, **issue**, **workflow**. Custom workflows match
organisational processes, for example `To Do -> In Progress -> Testing -> Done`.

**Trello** is built on three structures: **board** (an entire project, department or workflow),
**list** (a stage), **card** (an individual work item). A card may contain a description,
checklist, due date, attachments, assigned members, labels and comments.

## Selecting

| Need | Choose |
| --- | --- |
| Small team, simple flow, board is the whole process | Trello |
| Traceability, reporting, complex workflows, integration with development tools | Jira |
| Self-hosted CI with maximum extensibility | Jenkins |
| CI hosted with the repository, minimal operations | GitHub Actions or GitLab CI/CD |
| Reproducible environments | Docker plus infrastructure as code |
| Scale containers across nodes | Kubernetes |

The most common mistake is adopting a heavyweight tool and configuring it into something nobody
updates. A stale board produces misleading reports and misleading decisions, which is worse than
no board.
