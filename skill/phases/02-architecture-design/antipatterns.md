# PHASE 02 ANTI-PATTERNS

## Resume-Driven Architecture
The technology is chosen because it is interesting, then requirements are retrofitted to
justify it.
**Test:** can you name the specific NFR that this technology exists to satisfy? If not, it is
decoration.

## The Missing Middle
Architecture diagram exists, code exists, nothing in between. Nobody wrote the module
interfaces, so every integration is discovered at merge time.
**Fix:** high-level design is a level, not a formality.

## Design Without the Database People
The classic collaboration failure named in the source material: structural components end up
with mismatched data types because the people who own persistence were never in the room.
**Fix:** G2 criterion 10. Named reviewers from every system the design touches.

## The Untraceable Component
A service appears in the diagram that no requirement asked for. Usually "we'll need it later".
**Fix:** Article 3, applied in both directions at the orphan check.

## The Non-Functional Afterthought
Security, performance and availability appear in the SRS and nowhere in the design, on the
assumption that they can be added during construction. They cannot; they are structural.
**Fix:** the NFR mechanism table. Empty cells fail G2.

## Conceptual Disintegration
Three modules solve the same problem three different ways because three people designed them
independently. The system has no conceptual integrity, which is the thing architecture is
specifically for.
**Fix:** one architect owns the architecture document. Others contribute, one integrates.

## Premature Distribution
A network boundary is introduced between two components that will always deploy together and
always change together. Now every call can fail, and every deploy is a coordination problem.
**Fix:** distribute along axes of independent change and independent scale, and be able to say
which axis this boundary is on.

## The Undocumented Rejection
The chosen option is recorded. The three rejected options are not. Eighteen months later
someone proposes a rejected option again, and nobody can remember why it was rejected.
**Fix:** ADRs record alternatives and the reason for rejection, not just the decision.
