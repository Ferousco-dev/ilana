# PHASE 09 - PROCESS MODELING AND DOCUMENTATION

Owner: `process-modeler`. Support: `documentarian`. Continuous: runs alongside every phase.

> Process modeling uses graphical notations and documentation techniques to represent how
> software-related activities are performed, who performs them, and the sequence in which they
> occur.

Software development involves many people, tasks, resources and procedures. A process that is
not modelled and documented exists only in the heads of the people currently doing it, which
means it disappears when they do.

---

## What this phase produces

| Artifact | Path | Template |
| --- | --- | --- |
| Process model | `docs/process-model.md` | `templates/activity-diagram.md`, `templates/bpmn-model.md` |
| Process documentation | `docs/processes/` | `templates/process-documentation.md` |
| Documentation plan | `docs/document-plan.md` | `templates/document-plan.md` |
| Workflow definitions | `docs/workflows.md` | `templates/workflow.md` |

---

## Process modeling

Process modeling is the representation of a process using diagrams, charts or formal notations
to describe activities, tasks, decisions, workflows and interactions within a system. It gives a
visual description of how work is performed from start to finish.

A **software process model** describes:
- activities performed during development,
- the order of execution,
- responsible individuals or teams,
- inputs and outputs,
- decision points.

### Objectives

1. Improve understanding of processes.
2. Facilitate communication among stakeholders.
3. Standardise software development activities.
4. Identify inefficiencies and bottlenecks.
5. Support process improvement.
6. Enable automation.
7. Provide documentation for training and maintenance.

### Importance

- **Improved communication.** A common language among developers, analysts, testers and
  managers. Developers understand requirements, managers monitor activities, users understand
  system operations.
- **Better process understanding.** Team members see how work flows.
- **Better process analysis.** Efficiency, redundant activities and missing activities become
  visible.
- **Risk reduction.** Problems are identified before implementation.
- **Documentation.** Permanent records of organisational processes.

### Characteristics of a good process model

| Attribute | Meaning |
| --- | --- |
| Simplicity | avoid unnecessary complexity |
| Accuracy | must represent actual operations, not the idealised version |
| Completeness | include all important activities |
| Consistency | use standard notation |
| Maintainability | easy to update when processes change |
| Traceability | should connect with requirements |

**Accuracy is the one that gets violated.** Most process diagrams describe how the team wishes
it worked. Model the real process first; model the desired one separately and label it as such.

---

## Notations

Common notations: UML activity diagrams, BPMN, flowcharts, Petri nets, data flow diagrams. This
phase focuses on the first two.

### UML activity diagrams

An activity diagram is a flowchart representing the flow of control among the activities in a
system. Flow can be sequential, branched or concurrent. It answers: how does the process flow
from start to finish?

It shows activities, sequence of actions, decisions, parallel processing and process flow. It is
useful for modelling both software systems and business operations.

**Why they matter:**
- Business process modelling: represent how system tasks flow.
- Understanding system logic: order, conditions, loops, parallel actions.
- Visualising complex workflows, especially where multiple roles interact.
- Designing backend logic: developers use them to understand how functions change state.
- Supporting testing: QA teams create scenario-based tests from them.

**Notation:**

| Element | Symbol | Meaning |
| --- | --- | --- |
| Start node | small filled black circle | the initial state before an activity takes place |
| Action / activity node | rectangle with rounded corners | a step, with a short description |
| Control flow | solid line with an arrow | direction of progressing activities |
| Decision | diamond, one input flow, two or more output flows | mutually exclusive paths |
| Condition | text next to a decision marker | under what condition a flow splits that way |
| Fork | bar splitting one flow into several | splits a single flow into concurrent activities |
| Join | bar combining several flows into one | combines concurrent activities back into a flow |
| Merge | diamond | two flows merge and only one activity flows forward |
| Signal sending | convex pentagon | the action of sending a signal to an accepting activity |
| Signal receipt | concave pentagon | a signal is received |
| Note | folded-corner rectangle | relevant comments on elements |
| Final flow node | circle with an X, or bullseye for activity final | the end of a specific process flow |

**Advantages:** easy to understand; standardised notation; supports process analysis; useful for
software design; shows parallel activities clearly.

**Limitations:** can become complex for large systems; less suitable for highly dynamic business
processes; requires UML knowledge.

### BPMN

Business Process Model and Notation is a standardised way to draw and understand how work gets
done in an organisation. It is a universal diagramming language: simple enough for business
users to follow, detailed enough for IT teams to build from.

Organisations use several methods to map processes: flowcharts, UML diagrams, swimlane diagrams,
Gantt charts, value stream mapping, SIPOC diagrams. BPMN has become the most widely adopted
because it combines clarity for people with precision for systems.

**Advantages:** industry standard; easy communication; supports automation; suitable for complex
workflows; supports organisational modelling.

**Limitations:** can be difficult for beginners; large diagrams become complex; requires training
for effective use.

### Choosing between them

| Feature | UML activity diagram | BPMN |
| --- | --- | --- |
| Origin | UML | BPMN standard |
| Main purpose | software workflow modelling | business process modelling |
| Audience | software engineers | business and technical users |
| Complexity | moderate | high |
| Swimlanes | limited | extensive |
| Process automation | limited | strong |
| Business process support | moderate | excellent |

Rule of thumb: modelling what the **code** does, use an activity diagram. Modelling what the
**organisation** does across roles and systems, use BPMN.

---

## Process documentation

Documentation starts before the software process, continues through all phases of the SDLC, and
persists after project completion.

Documentation tools generate documents for technical users and end users. Technical users are
in-house professionals who refer to system manuals, reference manuals, training manuals and
installation manuals. End user documents describe the functioning and how-to of the system, such
as the user manual. Examples of tools: Doxygen, DrExplain, Adobe RoboHelp.

**Definition.** Process documentation is the recording of procedures, activities, workflows,
standards and guidelines used during software development. It serves as a reference for
understanding, executing and improving software processes.

**Importance:**
- Knowledge preservation: prevents loss of organisational knowledge.
- Consistency: activities are performed uniformly.
- Training: new employees understand procedures.
- Compliance: supports adherence to standards and regulations.
- Quality assurance: provides evidence of proper process execution.

**Characteristics of good documentation:** accuracy, completeness, clarity, consistency,
maintainability, accessibility.

**Typical sections of a software process document:** purpose (reason for the process), scope
(boundaries), inputs (resources required), activities (tasks performed), outputs (deliverables),
roles (responsible personnel).

---

## Types of software documentation

| Type | Describes | Examples | Contents |
| --- | --- | --- | --- |
| **Requirements** | what the system should do | SRS, user requirements document, functional requirements document | project overview, functional requirements, non-functional requirements, constraints, assumptions |
| **Design** | how the software will be developed | system architecture documents, UML diagrams, database design documents | system architecture, data models, interface designs, component descriptions |
| **Technical** | for developers and maintenance teams | source code documentation, API documentation, configuration guides | benefits: easier maintenance, faster troubleshooting, improved knowledge transfer |
| **User** | for end users | user manuals, installation guides, help documentation, tutorials | helps users understand and operate the software |
| **Testing** | testing activities and results | test plans, test cases, test reports, defect reports | ensures software quality and traceability |

---

## Documentation standards

Established guidelines, rules, formats and best practices used to create, organise, maintain and
manage documentation consistently. They ensure documents are accurate, complete, consistent,
easy to understand and easy to maintain.

### IEEE

| Standard | Covers |
| --- | --- |
| IEEE 830 | Software Requirements Specification |
| IEEE 1016 | Software Design Description |
| IEEE 829 | Software Testing Documentation |

Benefits: standardised structure, improved quality, better communication.

### ISO

| Standard | Covers |
| --- | --- |
| ISO/IEC 12207 | Software Life Cycle Processes |
| ISO/IEC 25010 | Software Quality Model |

**Benefits of documentation standards:** improved communication; better software quality, because
accurate documentation reduces errors; easier maintenance; knowledge preservation when team
members leave; regulatory compliance, supporting auditing and industry requirements.

---

## Process workflows

A process workflow is a sequence of activities, tasks, decisions and responsibilities defining
how work moves from initiation to completion. In software engineering, workflows provide a
structured approach to performing development activities.

Workflows ensure that tasks are completed in the correct order, responsibilities are clearly
defined, quality standards are maintained, and progress can be monitored.

**Importance:** improve productivity; reduce errors; increase consistency; enhance collaboration;
improve project visibility; ensure compliance with development processes.

**Components:**

| Component | Meaning | Example |
| --- | --- | --- |
| Activities | tasks that must be performed | write code, review code, execute tests |
| Roles | people responsible for tasks | developer, tester, project manager |
| Inputs | information required to begin a task | requirements document, design specification |
| Outputs | results produced by a task | source code, test report |
| Decision points | points where alternative paths may be taken | test passed? yes: deploy. no: fix defects |

**The canonical software development workflow:**

```
Requirements -> Analysis -> Design -> Implementation -> Testing -> Deployment -> Maintenance
```

- **Requirements:** gather user needs and business objectives.
- **Analysis:** study requirements and assess feasibility.
- **Design:** create system architecture and detailed designs.
- **Implementation:** develop source code.
- **Testing:** verify software correctness.
- **Deployment:** release software to users.
- **Maintenance:** fix defects and implement improvements.

---

## Exit

This phase is continuous. Its artifacts are updated at every gate rather than produced once. At
G8, the check is: could a new engineer operate this system from the documentation alone?
