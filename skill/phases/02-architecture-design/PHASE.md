# PHASE 02 - ARCHITECTURE AND DESIGN

Owner: `architect`. Entry gate: G1. Exit gate: G2.

> Software design is a mechanism to transform user requirements into a form that helps the
> programmer in coding and implementation. It moves concentration from the problem domain to
> the solution domain.

Design is where the SRS stops being a wish list and becomes a structure. The system is treated
as a set of components or modules with clearly defined behaviours and boundaries.

---

## What this phase produces

| Artifact | Path | Template |
| --- | --- | --- |
| Design description | `docs/design.md` | `templates/design-description.md` |
| Architecture decision records | `docs/adr/ADR-###.md` | `templates/adr.md` |
| Module specifications | `docs/modules/` | `templates/module-spec.md` |
| Data model | `docs/data-model.md` | inline in design description |

---

## The three levels

Design happens at three levels, in this order. Skipping a level does not save time; it moves
the cost later.

### Level 1: Architecture design

The overall structure of the system and how that structure provides **conceptual integrity**.
The software is a system made of many interrelated parts. At this level the designer obtains a
broad understanding of the domain of the proposed solution.

Decide here:
- the decomposition style (layered, client-server, microservices, monolith, event-driven,
  pipe-and-filter),
- the major components and what each is responsible for,
- how components communicate,
- where state lives and who owns it,
- which non-functional requirements are satisfied structurally rather than by effort.

The last point matters most. Latency, availability, security and scalability are architectural
properties. You cannot add them later by working harder.

### Level 2: High-level design

Breaks the architecture's "single entity, multiple component" concept into a less abstract
view of subsystems and modules, and shows how they interact. Implementing the system and its
components as modules is the focus. It acknowledges each subsystem's modular design as well as
their connections and interactions.

Produce here:
- the module list with one-sentence responsibilities,
- the interface of each module: inputs, outputs, errors, preconditions, postconditions,
- the dependency graph, with the direction of every arrow justified,
- the data flow between modules.

### Level 3: Detailed design

Every module is thoroughly examined to determine the data structures and algorithms that will
be employed. Results are recorded in a module specification document that outlines each
module's interface with other modules as well as its logical structure.

Produce here, per module:
- data structures with their invariants,
- algorithms with their complexity,
- error handling and failure behaviour,
- concurrency assumptions, if any,
- the specific `REQ` and `NFR` identifiers it satisfies.

---

## The six design objectives

Assess every design against all six. One paragraph each in the design description. These come
straight from the course material and they are a genuinely good review lens.

| Objective | The question | How it fails |
| --- | --- | --- |
| **Correctness** | Does the design satisfy the requirements? | a requirement with no design element |
| **Completeness** | Are all components present: data structures, modules, external interfaces? | the "and then a miracle occurs" box |
| **Efficiency** | Are resources used well? | an architecture that cannot meet its own latency NFR |
| **Flexibility** | Can it absorb the changes we expect? | every new feature requires touching every module |
| **Consistency** | Is there any internal contradiction? | two modules that disagree about who owns a record |
| **Maintainability** | Can another designer maintain this? | a design only its author can read |

---

## Where designs actually fail

The source material is blunt about this, and it is worth repeating: a major failure mode is
architecture designed without consulting the database engineers, producing data type mismatches
across structural components. That is a **collaboration** failure that shows up as a
**technical** defect.

Ìlànà response: before G2, the design must be reviewed by whoever owns each system it touches.
At `RIGOUR` 3 and above, that review is dated and named.

---

## Design and non-functional requirements

Every `NFR` needs an architectural mechanism, not an intention. Map them explicitly:

| NFR | Mechanism | Where |
| --- | --- | --- |
| NFR-002 95th percentile under 2s | read-through cache with a 60s TTL on the catalogue | DES-019 |
| NFR-005 99.9% monthly availability | stateless app tier, two zones, health-checked | DES-004, DES-005 |
| NFR-007 encryption of records at rest | field-level encryption in the persistence layer | DES-022 |
| NFR-009 10,000 concurrent users | connection pooling, horizontal scale, no session affinity | DES-004 |

An NFR with an empty mechanism column is a G2 failure.

---

## Exit

Run `checklist.md`, attempt G2. Handoff goes to `interaction-designer` with the module list and
every interface that a human will touch.
