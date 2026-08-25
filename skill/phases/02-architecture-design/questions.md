# PHASE 02 QUESTIONS

Maximum five, one batch.

1. What is the expected lifetime of this system, and what is the most likely change it will be
   asked to absorb in year two? (This is the flexibility requirement in disguise.)
2. What does the team already know how to operate? An architecture the team cannot run is a
   worse architecture than a boring one they can.
3. What existing systems must this integrate with, who owns them, and can they change?
4. Where is the data of record, and who is allowed to write to it?
5. Which single component, if it fails at 3am, must not take the rest of the system with it?

## Ask when it is a distributed or high-scale system

6. What is acceptable behaviour under partial failure: fail closed, fail open, or degrade?
7. Is eventual consistency acceptable anywhere, and where is it explicitly not?

## Ask when replacing something

8. What must remain compatible during the transition, and for how long?
9. What is the rollback story if the new system is worse?

## Never ask

- "Monolith or microservices?" as an opening question. Derive it from the NFRs, team size and
  operational capability, then propose it with reasons.
