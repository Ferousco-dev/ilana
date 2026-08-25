# PHASE 01 REFERENCE

Condensed source material for requirements engineering, as taught in SEN102/212.

## Definition

Requirement Engineering is a systematic process of identifying, documenting and managing
requirements within the framework of the engineering design process. It covers detection,
analysis, definition and confirmation of requirements and stakeholder expectations, and
monitoring and controlling them.

Properly implemented, it decreases project risk, keeps scope in check, lowers cost, and
delivers the agreed vision. Improperly defined, projects face difficulties leading to failure:
resources expended, needs unmet.

## Objectives and goals

1. **Identify and capture requirements** from customers, users and their regulators.
2. **Ensure requirement clarity and understanding** so that everyone contributing knows them,
   accurately communicated, refined, free of ambiguity.
3. **Prioritise requirements** by significance and emergent status.
4. **Validate requirements** so they are achievable, verifiable, meet project needs and respect
   the constraints of the activity.
5. **Manage changes to requirements** through the project lifecycle, so that every change is
   documented and examined.

## Historical evolution

Requirements were once handled ad hoc and communicated by word of mouth, which produced
misconceptions and project disasters.

- **1960s and 1970s.** Focus was on software only; requirements were a supplement. The
  emergence of the SDLC model made the need for structure around requirements visible.
- **1980s.** Formal methods entered routine use.
- Subsequent decades produced structured techniques, dedicated tooling, and the recognition of
  requirements engineering as a discipline in its own right.

## The three types

### Functional requirements
Depict what the system must perform: the functions to be designed and the features to be
traced, encompassing relations between the system and its surroundings, including inputs,
activities and outputs.

Examples: user authentication; order processing (place, edit, cancel); report generation
(monthly sales); data entry (customer name, address, contact); email notification on
registration completion.

**Role in system design:**
- Define scope: what the system can and cannot do.
- Guide development: a checklist ensuring all points are incorporated.
- Facilitate testing: the basis for test cases.
- Improve communication: shared understanding among stakeholders.

### Non-functional requirements
Specify how a system performs a function rather than what is expected of it. Centred on
efficiency, flexibility, dependability and protection.

Examples: transaction time under 2 seconds; usability with minimal training; 99.9% monthly
availability; crucial information secured in transfer and at rest; capacity for at least ten
thousand concurrent users without loss of efficiency.

**Importance:** ensure user satisfaction, enhance system quality, support future growth,
mitigate risk.

### Domain requirements
Derived from the industry or field of intended use. Specialised requirements, norms and
policies within which the system must operate.

Examples: healthcare privacy and security of patient information; finance multi-currency
operations and global accounting standards; education enrolment, progression, grading and
attendance; e-commerce payment gateway integration and PCI-DSS; manufacturing ERP integration
with inventory control and production planning.

## The five-stage process

The process is cyclical. Expect to revisit.

1. **Elicitation** - interviews, questionnaires, workshops, brainstorming, observation,
   document analysis, use cases and scenarios, prototyping.
2. **Analysis** - prioritisation, cost-benefit analysis, risk analysis, feasibility study,
   modeling (data flow diagrams, entity-relationship diagrams).
3. **Specification** - writing effective requirements, standard formats and templates,
   specification languages (UML, SysML), avoiding common pitfalls.
4. **Validation** - reviews and inspections, prototyping, model validation, deriving test cases.
5. **Management** - version control and traceability, change management, impact analysis,
   communication, tooling.

## Six challenges

1. **Ambiguous requirements.** Vague or multi-meaning. "The system should be user-friendly"
   means different things to different users.
2. **Incomplete requirements.** Gaps in functionality. A transaction system with no error
   handling requirement can lose data.
3. **Changing requirements.** Business needs, market shifts, preference changes. A desktop
   application that must become mobile mid-project.
4. **Conflicting requirements.** One stakeholder wants richer reporting, another wants
   throughput; both compete for the same resources.
5. **Stakeholder communication issues.** Domain vocabulary the development team does not
   fully share.
6. **Technical constraints.** Legacy databases and hardware that cannot support what was
   specified.

## Six strategies

1. **Clear and detailed documentation** with standard formats, templates, examples, diagrams.
2. **Regular stakeholder engagement**: periodic sessions, participation in review and validation.
3. **Change management processes**: change request forms, impact analysis, prioritisation by
   business importance, controlled implementation.
4. **Conflict resolution mechanisms**: facilitated workshops, negotiation, decision models,
   consensus.
5. **Effective communication techniques**: mockups and prototypes to prevent miscommunication.
6. **Modern tools**: Jira, Trello, or specialised requirements management tools for creation,
   tracking and traceability.

## Case studies

**Healthcare management system.** Functional: patient registration, appointment scheduling,
electronic health records. Non-functional: data secured to the applicable privacy regime,
99.9% availability, ease of use for clinicians. Domain: healthcare guidelines followed,
compatible with existing medical devices and structures.

**E-commerce platform.** Functional: product catalogue, shopping cart, order processing.
Non-functional: page load performance, PCI-DSS-compliant payment processing, scalability for
sale-event traffic. Domain: multiple payment gateway integration, consumer protection law.
