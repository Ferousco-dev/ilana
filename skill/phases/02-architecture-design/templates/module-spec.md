# Module Specification: <name> (DES-###)

| Field | Value |
| --- | --- |
| Design level | detailed |
| Owner | |
| Requirements satisfied | REQ-..., NFR-... |
| Depends on | DES-... |
| Depended on by | DES-... |

## 1. Responsibility
One sentence. If it needs "and", consider splitting the module.

## 2. Public interface

| Operation | Inputs | Outputs | Errors raised | Preconditions | Postconditions |
| --- | --- | --- | --- | --- | --- |

## 3. Data structures

| Structure | Fields | Invariants | Lifetime |
| --- | --- | --- | --- |

Invariants are the statements that must be true before and after every public operation. They
are also the best source of test cases.

## 4. Algorithms

| Operation | Approach | Time | Space | Why this and not the obvious alternative |
| --- | --- | --- | --- | --- |

## 5. Error handling
| Condition | Detection | Response | Propagated as | Logged as |
| --- | --- | --- | --- | --- |

## 6. Concurrency
Thread safety, reentrancy, shared state, locking order. If none: state "single-threaded, not
safe for concurrent use" explicitly. Silence here becomes a production defect.

## 7. Test hooks
What must be injectable or observable for this module to be unit tested. If the answer is
"nothing", the module is not testable and the design is not finished.

## 8. Verification
| Requirement | Test case |
| --- | --- |
