# Software Design Description: <SYSTEM>

Structure follows IEEE 1016.

| Field | Value |
| --- | --- |
| Document ID | SDD-<project>-v<n> |
| Baselined SRS | SRS-<project>-v<n> |
| Author | |
| Reviewers (named, RIGOUR 3+) | |
| Date | |

---

## 1. Introduction
Purpose, scope, definitions, references.

## 2. Architecture design (level 1)

### 2.1 Decomposition style
Chosen style and why. Alternatives rejected are in `docs/adr/`.

### 2.2 Component view
| Component | Responsibility (one sentence) | Owns which data | Talks to |
| --- | --- | --- | --- |

### 2.3 Conceptual integrity
What single idea holds this system together. If you cannot state it in two sentences, the
architecture is not finished.

### 2.4 Non-functional mechanisms
| NFR | Mechanism | Component | Verified by |
| --- | --- | --- | --- |

Empty mechanism cells fail G2.

### 2.5 Trust boundaries
Where does untrusted input cross into trusted code, and what validates it there.

### 2.6 Failure behaviour
| Dependency | If it is unavailable | User-visible effect |
| --- | --- | --- |

## 3. High-level design (level 2)

### 3.1 Module list
| Module ID | Name | Responsibility | Requirements satisfied |
| --- | --- | --- | --- |

### 3.2 Interfaces
| Module | Operation | Inputs | Outputs | Errors | Preconditions | Postconditions |
| --- | --- | --- | --- | --- | --- | --- |

### 3.3 Dependency graph
Direction of every arrow, and the reason it points that way.

### 3.4 Data flow
How information moves through the system for the two or three most important operations.

## 4. Detailed design (level 3)

One subsection per module, or a separate file under `docs/modules/`.

### 4.x <Module name> (DES-###)
- Requirements satisfied:
- Data structures and their invariants:
- Algorithms and complexity:
- Error handling:
- Concurrency assumptions:
- Test hooks:

## 5. Data model
Entities, relationships, ownership, retention, and who is permitted to write.

## 6. Design objective assessment
| Objective | Assessment | Evidence |
| --- | --- | --- |
| Correctness | | |
| Completeness | | |
| Efficiency | | |
| Flexibility | | |
| Consistency | | |
| Maintainability | | |

## 7. Traceability
| REQ / NFR / DOM | DES | Module | Notes |
| --- | --- | --- | --- |
