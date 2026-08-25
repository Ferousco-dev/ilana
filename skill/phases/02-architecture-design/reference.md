# PHASE 02 REFERENCE

## What software design is

Software design is the process of constructing software methods, functions, objects, the
overall structure and interaction of code, so that the functionality produced satisfies user
needs. There are many methods for designing software, and different developers prefer
different design levels either up front or during execution.

The overall design should be carefully considered and reviewed before coding starts. Early in
the development cycle it is simpler to test various designs and identify issues than to make a
large design change after the majority of the code has been written.

Software design transforms user requirements into a suitable form that helps the programmer in
coding and implementation. It represents the client's requirement, as described in the SRS
document, in a form easily implementable in a programming language.

The design phase is the first step in the lifecycle that moves concentration from the problem
domain to the solution domain. The system is considered to be a set of components or modules
with clearly defined behaviours and boundaries.

## The six objectives of software design

| Objective | Statement |
| --- | --- |
| Correctness | The design should be correct as per requirement. |
| Completeness | The design should have all components: data structures, modules, external interfaces. |
| Efficiency | Resources should be used efficiently by the program. |
| Flexibility | Able to modify on changing needs. |
| Consistency | There should not be any inconsistency in the design. |
| Maintainability | The design should be simple enough to be easily maintainable by other designers. |

## The three design levels

### Architecture design
An architecture is the overall structure of a system and how that structure provides
conceptual integrity to the system. Under architectural design the software is a system made
up of many interrelated parts. At this point the designers obtain a broad understanding of the
domain of the suggested solution.

### High-level design
By breaking down the architectural design's "single entity, multiple component" concept, the
high-level design presents a less abstract view of subsystems and modules and illustrates how
they interact with one another. Implementing the system and its components as modules is the
focus. It acknowledges each subsystem's modular design in addition to their connections and
interactions.

### Detailed design
Following the completion of high-level design, the detailed design process starts. Every
module is thoroughly examined to determine the data structures and algorithms to be employed.
The stage's results are recorded in a module specification document, which outlines each
module's interface with other modules as well as its logical structure.

## Design in the collaboration context

The design phase is where collaboration matters most. Developers, system analysts and
designers must work together to decide how the software should be structured. Failure to
collaborate effectively produces poor or inconsistent design decisions that affect software
quality. The specific documented failure mode is architecture designed without consulting
database engineers, producing massive data type mismatches across structural components.

Where two architects disagree, the correct first step is to evaluate both alternatives
objectively using agreed technical criteria, not seniority and not deadline pressure.

## Relationship to standards

- **IEEE 1016** Software Design Description gives the document structure.
- **ISO/IEC 12207** places design among the primary processes.
- **ISO/IEC 25010** supplies the quality model that the NFR mechanisms serve.
