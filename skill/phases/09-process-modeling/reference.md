# PHASE 09 REFERENCE

## Why process modeling exists

Software development is a complex activity involving many people, tasks, resources and
procedures. To ensure software is developed efficiently and consistently, organisations define
and document their software processes.

A software process must be clearly communicated to developers, testers, managers, clients and
other stakeholders. One of the most effective ways to achieve this is through process modeling,
which uses graphical notations and documentation techniques to represent how software-related
activities are performed, who performs them, and the sequence in which they occur.

## Process modeling

**Definition.** Process modeling is the representation of a process using diagrams, charts or
formal notations to describe activities, tasks, decisions, workflows and interactions within a
system. It provides a visual description of how work is performed from start to finish.

**A software process model describes:** activities performed during software development; order
of execution; responsible individuals or teams; inputs and outputs; decision points.

**Worked example, ATM withdrawal:**
```
Insert Card -> Enter PIN -> PIN correct?
                              /        \
                            Yes         No
                             |           |
                       Select Amount   Retry
                             |
                       Dispense Cash
                             |
                            End
```

**Objectives:** improve understanding of processes; facilitate communication among stakeholders;
standardise development activities; identify inefficiencies and bottlenecks; support process
improvement; enable automation; provide documentation for training and maintenance.

**Importance:** improved communication (a common language among developers, analysts, testers
and managers); better process understanding; better process analysis (efficiency, redundant
activities, missing activities); risk reduction (problems identified before implementation);
documentation (permanent records of organisational processes).

**Characteristics of good process models:** simplicity, accuracy, completeness, consistency,
maintainability, traceability.

## Process documentation

Documentation in a software project starts prior to the software process, goes through all
phases of the SDLC, and continues after project completion.

Documentation tools generate documents for technical users and end users. Technical users are
mostly in-house professionals of the development team who refer to system manuals, reference
manuals, training manuals and installation manuals. End user documents describe the functioning
and how-to of the system, such as the user manual. Tools include Doxygen, DrExplain and Adobe
RoboHelp.

**Definition.** Process documentation refers to the recording of procedures, activities,
workflows, standards and guidelines used during software development. It serves as a reference
for understanding, executing and improving software processes.

**Importance:** knowledge preservation; consistency; training; compliance; quality assurance.

**Characteristics of good documentation:** accuracy, completeness, clarity, consistency,
maintainability, accessibility.

**Typical sections of a process document:** purpose, scope, inputs, activities, outputs, roles.

**Worked example, course registration process:**
Purpose: register students for courses.
Inputs: student details, course catalog.
Activities: login, course selection, validation, approval.
Outputs: registration slip.

## Process modeling notations

A notation is a standardised graphical language used to represent processes. Common notations:
UML activity diagrams, BPMN, flowcharts, Petri nets, data flow diagrams.

## UML activity diagrams

**Definition.** An activity diagram is a flowchart representing the flow of control among the
activities in a system. The flow of operation can be sequential, branched or concurrent. It
answers: how does the process flow from start to finish?

It shows activities, sequence of actions, decisions, parallel processing and process flow.
Activity diagrams are useful for modelling both software systems and business operations.

**Why they matter.** Business process modelling (representing how system tasks flow);
understanding system logic (order, conditions, loops, parallel actions); visualising complex
workflows, especially where multiple roles interact; designing backend logic (developers use
them to understand how functions change states); supporting testing (QA teams create
scenario-based tests from them).

**Notations used:**
- **Start node.** The small filled black circle is the standard notation for an initial state
  before an activity takes place.
- **Action / activity nodes.** The building blocks, usually with a short description of the
  activity they represent, often drawn as rectangles with rounded corners.
- **Control flow.** A solid line with an arrow representing the direction of the activities. The
  arrow points in the direction of progressing activities.
- **Decision symbol.** A diamond shape, with two paths coming out of a decision, and condition
  text indicating which options are mutually exclusive. One input flow, two or more output flows.
- **Join node.** Combines two concurrent activities back into a flow.
- **Fork node.** Splits a single activity flow into two concurrent activities.
- **Condition.** Condition text placed next to a decision marker, indicating under what condition
  an activity flow should split off in that direction.
- **Merge node.** Two activities are merged with a condition and only one activity flows forward.
- **Note.** Used to add relevant comments to elements.
- **Signal sending.** Used to represent the action of sending a signal to an accepting activity.
- **Signal receipt.** Used to represent that a signal is received.
- **Final flow node.** Represents the end of a specific process flow.

**Advantages:** easy to understand; standardised notation; supports process analysis; useful for
software design; shows parallel activities clearly.

**Limitations:** can become complex for large systems; less suitable for highly dynamic business
processes; requires UML knowledge.

## BPMN

Business Process Model and Notation is a standardised way to draw and understand how work gets
done in an organisation. Think of it as a universal diagramming language: simple enough for
business users to follow, yet detailed enough for IT teams to build from.

Organisations use different methods to map or model processes: flowcharts, UML diagrams,
swimlane diagrams, Gantt charts, value stream mapping, SIPOC diagrams. Each has strengths, but
BPMN has become the most widely adopted because it combines clarity for people with precision
for systems.

**Advantages:** industry standard; easy communication; supports automation; suitable for complex
workflows; supports organisational modelling.

**Limitations:** can be difficult for beginners; large diagrams become complex; requires training
for effective use.

## UML activity diagrams versus BPMN

| Feature | UML Activity Diagram | BPMN |
| --- | --- | --- |
| Origin | UML | BPMN Standard |
| Main purpose | Software workflow modelling | Business process modelling |
| Audience | Software engineers | Business and technical users |
| Complexity | Moderate | High |
| Swimlanes | Limited | Extensive |
| Process automation | Limited | Strong |
| Business process support | Moderate | Excellent |

## Documentation standards

**Definition.** Documentation standards are established guidelines, rules, formats and best
practices used to create, organise, maintain and manage software documentation consistently
throughout a project. They ensure that all project documents are accurate, complete, consistent,
easy to understand and easy to maintain.

### Types of software documentation

1. **Requirements documentation.** Describes what the software system should do. Examples: SRS,
   user requirements document, functional requirements document. Contents: project overview,
   functional requirements, non-functional requirements, constraints, assumptions.
2. **Design documentation.** Describes how the software will be developed. Examples: system
   architecture documents, UML diagrams, database design documents. Contents: system
   architecture, data models, interface designs, component descriptions.
3. **Technical documentation.** Used by developers and maintenance teams. Examples: source code
   documentation, API documentation, configuration guides. Benefits: easier maintenance, faster
   troubleshooting, improved knowledge transfer.
4. **User documentation.** Created for end users. Examples: user manuals, installation guides,
   help documentation, tutorials. Purpose: helps users understand and operate the software
   effectively.
5. **Testing documentation.** Records testing activities and results. Examples: test plans, test
   cases, test reports, defect reports. Purpose: ensures software quality and traceability.

### Common documentation standards

**IEEE.** Internationally recognised standards for software documentation.
Examples: IEEE 830 (Software Requirements Specification), IEEE 1016 (Software Design
Description), IEEE 829 (Software Testing Documentation).
Benefits: standardised structure, improved quality, better communication.

**ISO.** Standards related to software quality and documentation.
Examples: ISO/IEC 12207 (Software Life Cycle Processes), ISO/IEC 25010 (Software Quality Model).

**Benefits of documentation standards:** improved communication; better software quality;
easier maintenance; knowledge preservation even when team members leave; regulatory compliance
supporting auditing and industry requirements.

## Process workflows

**Definition.** A process workflow is a sequence of activities, tasks, decisions and
responsibilities that define how work moves from initiation to completion. In software
engineering, workflows provide a structured approach to performing development activities.

Workflows ensure tasks are completed in the correct order, responsibilities are clearly defined,
quality standards are maintained, and progress can be monitored.

**Importance:** improve productivity; reduce errors; increase consistency; enhance
collaboration; improve project visibility; ensure compliance with development processes.

**Components:** activities (tasks that must be performed); roles (people responsible for tasks);
inputs (information required to begin a task); outputs (results produced by a task); decision
points (points where alternative paths may be taken).

**Software development workflow:**
Requirements -> Analysis -> Design -> Implementation -> Testing -> Deployment -> Maintenance.

Requirements: gather user needs and business objectives. Analysis: study requirements and assess
feasibility. Design: create system architecture and detailed designs. Implementation: develop
source code. Testing: verify software correctness. Deployment: release software to users.
Maintenance: fix defects and implement improvements.
