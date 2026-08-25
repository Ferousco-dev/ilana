# Process Style Decision

No single process fits all projects. Choose deliberately, record the reason, and revisit when
the project characteristics change.

| Field | Value |
| --- | --- |
| Project | |
| Style chosen | agile (Scrum) / agile (Kanban) / plan-driven / hybrid / devops-centred |
| Decided by | |
| Date | |
| Decision ID | DEC-### |

## 1. Project characteristics

Score each. The pattern of scores, not any single row, chooses the style.

| Characteristic | Value | Points towards |
| --- | --- | --- |
| Requirement stability | volatile / moderate / fixed | volatile -> Agile, fixed -> plan-driven |
| Regulatory obligation | none / some / heavy | heavy -> plan-driven governance |
| Safety criticality | none / moderate / life-critical | life-critical -> plan-driven, RIGOUR 5 |
| Customer availability | continuous / periodic / rare | continuous -> Agile, rare -> plan-driven |
| Team size | small / medium / large | large -> more structure |
| Team distribution | co-located / distributed / asynchronous | distributed -> more written process |
| Project size and complexity | small / medium / large | large -> more structure |
| Deployment frequency | continuous / periodic / rare | continuous -> DevOps emphasis |
| Cost of a production failure | low / moderate / severe | severe -> heavier gates |
| Time constraint | flexible / firm / fixed by law or contract | fixed -> plan the scope, not the date |

## 2. The choice

**Style:** ___

**Reason:** the specific characteristics above that drove it. Not "the team prefers Agile".

## 3. What that means concretely here

| Aspect | This project |
| --- | --- |
| Iteration length | |
| Requirements handling | full SRS up front / progressively elaborated backlog / hybrid |
| Documentation depth | |
| Change handling | frozen after baseline / continuous re-prioritisation with impact analysis |
| Roles used | Product Owner, Scrum Master, Development Team / PM, BA, Dev, QA, DevOps |
| Ceremonies | sprint planning, daily scrum, review, retrospective / stage gates |
| Verification cadence | continuous / phase-end |
| Release cadence | |

## 4. The hybrid case

Most real projects are hybrid, and saying so honestly beats pretending to be pure.

The two patterns that recur:

**Plan-driven governance plus Agile development.** A regulated healthcare or financial system that
must satisfy stringent documentation, traceability and approval requirements, while still
incorporating periodic customer feedback during development. Governance artifacts (SRS,
traceability, formal approvals) are plan-driven; construction and verification run in iterations.

**Agile delivery inside controlled process.** An organisation adopting Git, Jenkins, Docker and
Kubernetes with automated CI/CD, while maintaining formal documentation and regulatory approval
procedures. This is integrating modern DevOps practice within a controlled software engineering
process, and it is a mature position rather than a contradiction.

## 5. Anti-pattern check

- [ ] Not chosen by habit ("this is how we do things")
- [ ] Not chosen by fashion ("everyone is Agile")
- [ ] Ceremonies chosen serve a purpose that can be named
- [ ] If Agile: the customer is genuinely available for feedback
- [ ] If Agile: retrospectives actually change the process
- [ ] If plan-driven: the requirements are genuinely stable enough to freeze
- [ ] If hybrid: which parts are which is written down, not improvised

## 6. Revisit trigger

The observable condition that should reopen this decision. Examples: requirement volatility
changes materially; a regulator enters the picture; the team doubles; the system moves from
internal to public.
