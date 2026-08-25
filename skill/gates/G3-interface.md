# G3 - INTERFACE BASELINE

Owner: `interaction-designer`. Closes: phase 03. Opens: phase 04 Construction.

Applies to every interface a human touches: GUI, CLI, API surface, report format.
A command line interface is a user interface and gets the same gate.

## Criteria

| # | Criterion | Rigour | Evidence |
|---|---|---|---|
| 1 | Interface type chosen and justified: text-based, graphical, or both | R1+ | `docs/ui-spec.md` |
| 2 | Every user-facing `REQ` maps to a `UI-###` element | R1+ | traceability |
| 3 | Five UI principles assessed: structure, simplicity, visibility, feedback, tolerance | R1+ | one paragraph each, with the specific screen or command |
| 4 | Every error state has a message and a recovery path | R2+ | error catalogue |
| 5 | Undo, redo, or confirmation exists for every destructive action | R2+ | tolerance principle, enumerated |
| 6 | Primary task flows documented end to end | R3+ | flow diagrams or numbered steps |
| 7 | Accessibility considered: contrast, keyboard reachability, screen reader labels | R3+ | checklist result |
| 8 | Feedback latency budget stated (what happens if an action takes over 1s) | R3+ | spinner, progress, optimistic update policy |
| 9 | Interface reviewed with a representative user | R4+ | dated session note |
| 10 | Safety-critical actions require deliberate confirmation and are logged | R5 | control list |

## The five principles as tests

Straight from the source material, turned into checks you can actually fail:

| Principle | Test |
| --- | --- |
| Structure | Are related things grouped and unrelated things separated, consistently across screens? |
| Simplicity | Can the most common task be completed without reading documentation? |
| Visibility | Is every option needed for the current task visible, and nothing else? |
| Feedback | After every action, does the user know what happened, in their own language? |
| Tolerance | Can every mistake be undone, and are unreasonable inputs handled rather than rejected? |

## Common failures

- Treating a CLI as exempt. Recall and navigation are exactly why text interfaces are harder;
  the principles apply more, not less.
- Feedback that exists in the log but not on the screen.
- No tolerance: a destructive action with no confirmation and no undo.
