# PHASE 02 CHECKLIST

## Architecture level
- [ ] Decomposition style chosen and named
- [ ] At least one alternative considered and rejected in writing
- [ ] Major components listed with a one-sentence responsibility each
- [ ] Communication mechanism between components stated
- [ ] State ownership is unambiguous: exactly one component owns each piece of data
- [ ] Every NFR has an architectural mechanism, not an intention

## High-level design
- [ ] Every module has exactly one stated responsibility
- [ ] Every module interface lists inputs, outputs and errors
- [ ] Dependency graph drawn, and every arrow's direction is justified
- [ ] No cyclic dependencies, or the cycle is explicitly accepted with a reason
- [ ] Data flow between modules documented

## Detailed design
- [ ] Data structures specified with their invariants
- [ ] Algorithms named with their complexity where it matters
- [ ] Error handling specified per module
- [ ] Concurrency assumptions stated, or "single-threaded" stated explicitly

## Traceability
- [ ] Every REQ maps to at least one DES
- [ ] Every DES maps back to at least one REQ or NFR
- [ ] Orphan check run in both directions

## Objectives
- [ ] Correctness assessed
- [ ] Completeness assessed
- [ ] Efficiency assessed
- [ ] Flexibility assessed
- [ ] Consistency assessed
- [ ] Maintainability assessed

## Collaboration
- [ ] Data and persistence owners reviewed the data model
- [ ] Operations reviewed the deployment shape
- [ ] Security reviewed the trust boundaries
- [ ] Reviewers are named and dated (RIGOUR 3+)
