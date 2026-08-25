# PHASE 01 - REQUIREMENTS

Owner: `analyst`. Entry gate: G0. Exit gate: G1.

> Requirements engineering is the systematic process of identifying, documenting and managing
> requirements. It is the basis for every other phase. When it is done badly, resources are
> expended and needs are still unmet.

This phase is where projects are actually won or lost. Everything downstream inherits its
defects.

---

## What this phase produces

| Artifact | Path | Template |
| --- | --- | --- |
| Software Requirements Specification | `docs/srs.md` | `templates/srs.md` |
| Traceability matrix | `.ilana/traceability.csv` | `templates/traceability-matrix.md` |
| Elicitation plan | `docs/elicitation-plan.md` | `templates/elicitation-plan.md` |
| User stories (Agile style) | `docs/stories/` | `templates/user-story.md` |
| Requirements register | `.ilana/requirements.md` | inline |

At `RIGOUR` 1 to 2, the SRS may collapse to a single page. It may not disappear.

---

## The five stages

Run them in order. The process is cyclical: expect to return to elicitation after analysis
exposes a gap.

### 1. Elicitation

Identify requirements from the people involved. Eight techniques, and the choice matters:

| Technique | Use when | Weakness |
| --- | --- | --- |
| Interviews | you need depth and the *why* behind a request | small sample, interviewer bias |
| Questionnaires | you need breadth across many users | shallow, no follow-up |
| Workshops | stakeholders disagree and need to hear each other | dominated by the loudest voice |
| Brainstorming | the solution space is genuinely open | generates volume, not priority |
| Observation | users cannot articulate what they actually do | expensive, observer effect |
| Document analysis | replacing or integrating with an existing system | documents describe the past |
| Use cases and scenarios | behaviour is conditional and multi-step | can miss non-functional needs |
| Prototyping | the user cannot judge a description but can judge a thing | prototype gets mistaken for the product |

Ìlànà default: interviews plus document analysis plus one prototype or scenario pass. Add
observation whenever the user says "it's hard to explain, you'd have to see it".

Protocol: `protocols/elicitation.md`.

### 2. Analysis

Scrutinise what was collected for clarity, completeness and feasibility. Find contradictions,
overlaps and duplication.

- **Prioritisation.** Rank by importance and impact. MoSCoW or numeric, but ranked.
- **Cost-benefit analysis.** Money, time and effort against value.
- **Risk analysis.** Which requirements are likely to become problems.
- **Feasibility study.** Technical and economic.
- **Modeling.** Data flow diagrams, entity-relationship diagrams, use case models.

### 3. Specification

Write it down precisely, concisely and in a fixed structure.

- Each requirement expresses exactly one meaning.
- Standard formats and templates, consistently applied.
- Where useful, formal notations: UML, SysML.
- Follow IEEE 830 shape (see `references/standards.md`).

### 4. Validation

Confirm the requirements still reflect what users need and can actually be fulfilled.

- Reviews and inspections of the requirements document.
- Prototyping to confirm with users.
- Model validation against the analysis models.
- Deriving test cases from requirements, which double as a completeness check: a requirement
  from which you cannot derive a test case is not yet a requirement.

### 5. Management

Manage change across the whole lifecycle.

- Version control and traceability, including the origin of each requirement.
- A change control procedure. See `protocols/change-control.md`.
- Impact analysis on scope, schedule and cost before approval.
- Communication of every accepted change to everyone affected.
- Tooling: Jira, Trello, or dedicated requirements management tools.

---

## The three types

Every system needs all three considered, even if one comes back empty.

**Functional** - what the system must do. Inputs, activities, outputs.
Example: the system must allow a user to place, edit and cancel an order.

**Non-functional** - how well it does it. Performance, usability, reliability, security,
scalability.
Example: transaction time must not exceed 2 seconds.
Example: availability must be 99.9% per month.

**Domain** - what the industry, regulator or field demands.
Example (healthcare): patient information handling must satisfy the applicable privacy regime.
Example (finance): multi-currency operation and conformance to accounting standards.
Example (e-commerce): payment handling must satisfy PCI-DSS.
Example (manufacturing): must integrate with the established ERP and support inventory control.

Ìlànà rule: if `DOM` comes back empty, say out loud which regulator or standard you checked
and found not to apply. Empty because unexamined is a G1 failure.

---

## Requirement writing form

```
REQ-007  [functional] [priority: must] [source: interview, Head of Circulation, 2026-08-19]
The system shall allow a librarian to record the return of a borrowed item and, where the
return is late, calculate the fine using the fine schedule in DOM-002.

Rationale: fines are the library's only enforcement mechanism for late returns.
Acceptance: given an item borrowed on day 0 with a 14-day loan period, when returned on
day 20, the system records a fine of 6 units per the DOM-002 schedule.
Verified by: TC-018, TC-019
Depends on: REQ-004 (item borrowing), DOM-002 (fine schedule)
```

Every field earns its place. `source` is what lets you go back and ask when the requirement
turns out to be wrong. `rationale` is what stops a future team deleting something load-bearing.

---

## Challenges, and what Ìlànà does about each

| Challenge | Symptom | Ìlànà response |
| --- | --- | --- |
| Ambiguity | "user-friendly", "fast", "secure" | run the adjective grep at G1, rewrite with numbers |
| Incompleteness | no error handling requirement anywhere | force an explicit failure-path pass over every functional requirement |
| Volatility | requirements change weekly | change control, not resistance. Every change is a `CR` |
| Conflict | two stakeholders want incompatible things | facilitated resolution, `protocols/conflict-resolution.md`. Never resolve unilaterally |
| Communication breakdown | the team builds what it thought it heard | write it, read it back, get it confirmed, date it |
| Technical constraint | legacy database cannot support the feature | record the constraint as a requirement of its own, do not silently descope |

---

## Exit

Run `checklist.md`, then attempt `gate.md` (G1).
Handoff goes to `architect` with the full ID range and every open item named.
