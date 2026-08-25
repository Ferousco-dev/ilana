# Interface Specification: <SYSTEM>

| Field | Value |
| --- | --- |
| Interface type | text-based / graphical / both |
| Primary user | |
| Frequency of use | |
| Environment | |
| Baselined design | SDD-<project>-v<n> |

## 1. Vocabulary

The controlled vocabulary for this interface. Every term is used consistently everywhere, and
nothing outside this list appears in user-facing text.

| Term | Means | Never call it |
| --- | --- | --- |
| Item | a single borrowable physical object | book, copy, record |
| Borrow | transfer custody to a member for a loan period | check out, take, issue |

## 2. Structure

### 2.1 Information architecture
The map. Screens, or commands and subcommands.

### 2.2 Layout model
The consistent skeleton every screen inherits. For a CLI: the consistent shape of output.

### 2.3 Grouping rules
What lives together and why.

## 3. Task flows

For each primary task:

```
UI-001  <task name>
Frequency: <daily / weekly / rare>
Entry point:
Steps:
  1.
  2.
Success state (what the user sees):
Failure states:
Undo path:
Satisfies: REQ-###
```

## 4. Controls

| UI ID | Element | Type | Purpose | States | Keyboard | Satisfies |
| --- | --- | --- | --- | --- | --- | --- |

States must include at minimum: default, hover or focus, active, disabled, loading, error,
empty. Missing states are where interfaces break in production.

## 5. Feedback policy

| Duration | Treatment |
| --- | --- |
| under 100ms | no indicator needed |
| 100ms to 1s | immediate visual acknowledgement of the action |
| 1s to 10s | progress indicator, action remains cancellable |
| over 10s | progress with estimate, and the user may leave and return |

## 6. Tolerance register

| Destructive action | Confirmation | Undo window | Recovery if undo missed |
| --- | --- | --- | --- |

## 7. Accessibility

| Check | Status | Evidence |
| --- | --- | --- |
| Colour not sole carrier of meaning | | |
| Contrast sufficient | | |
| Keyboard reachable and operable | | |
| Accessible names present | | |
| Focus visible and ordered | | |
| Reduced motion respected | | |

## 8. Principle assessment

| Principle | How this design satisfies it | Weakest point |
| --- | --- | --- |
| Structure | | |
| Simplicity | | |
| Visibility | | |
| Feedback | | |
| Tolerance | | |

## 9. Traceability

| REQ | UI element | Test case |
| --- | --- | --- |
