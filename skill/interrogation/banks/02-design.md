# ASSESSMENT BANK: DESIGN

## Recall

1. Name the three levels of software design and what each produces.
2. Name the six objectives of software design.
3. What does "conceptual integrity" mean, and which design level provides it?
4. What is recorded in a module specification document?

## Multiple choice

**Q1.** Which design level presents a less abstract view of subsystems and modules and illustrates
how they interact with one another?
A. architecture design  B. high-level design  C. detailed design  D. interface design
*Answer: B*

**Q2.** At which level is every module thoroughly examined to determine the data structures and
algorithms to be employed?
A. architecture  B. high-level  C. detailed  D. acceptance
*Answer: C*

**Q3.** Which software engineering artifact is most likely produced through collaborative design
activities?
A. source code repository  B. software architecture and design specification
C. deployment script  D. user authentication database
*Answer: B*

**Q4.** Failure of software architects, developers and database engineers to collaborate during
system design is most likely to result in:
A. improved cohesion  B. architectural inconsistencies and integration problems
C. automatic scalability  D. reduced software complexity
*Answer: B*

**Q5.** During system architecture design, developers disagree about microservices versus a
monolithic architecture. Which team practice best supports arriving at the optimal decision?
A. seniority-based decision without discussion
B. technical evaluation supported by collaborative design reviews
C. ignoring non-functional requirements
D. selecting the first proposed architecture
*Answer: B*

**Q6.** Which design objective is concerned with the design having all components including data
structures, modules and external interfaces?
A. correctness  B. completeness  C. consistency  D. flexibility
*Answer: B*

## Scenario

**S1.** Your SRS contains eight non-functional requirements. Your design document mentions none of
them. Explain why this fails G2 and what specifically must be added.

**S2.** A design review produces a diagram with twelve services. Three of them correspond to no
requirement. What do you do, and which constitutional article applies?

**S3.** You are asked to choose between two architectures. Describe the procedure you would follow
so the decision is defensible in six months when nobody remembers the discussion.

## Marking notes

- S1 must produce an NFR mechanism table: each NFR mapped to a specific structural mechanism in a
  named component.
- S2 must apply the orphan check in the design-to-requirement direction, and Article 3.
- S3 must include: criteria agreed before evaluating options, both options scored, an ADR recording
  the alternatives and the reason for rejection, and a revisit trigger.
