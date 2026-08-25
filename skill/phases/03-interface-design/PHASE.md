# PHASE 03 - INTERFACE DESIGN

Owner: `interaction-designer`. Entry gate: G2. Exit gate: G3.

> The user interface is the visual part of an application or operating system through which a
> client interacts with a computer or software. It determines how commands are given and how
> data is displayed.

Applies to every surface a human touches: graphical interfaces, command line interfaces, API
surfaces consumed by other engineers, report layouts, error messages, log output. A CLI is a
user interface and receives the same gate.

---

## What this phase produces

| Artifact | Path | Template |
| --- | --- | --- |
| Interface specification | `docs/ui-spec.md` | `templates/interface-spec.md` |
| Error catalogue | `docs/error-catalogue.md` | `templates/error-catalogue.md` |
| Usability review record | `docs/reviews/usability-<date>.md` | `templates/usability-review.md` |

---

## Choosing the interface type

Two main types, and the choice is a design decision with consequences, not a default.

### Text-based / command line
Relies primarily on the keyboard. UNIX is the canonical example.

| Advantages | Disadvantages |
| --- | --- |
| Many and easier customisation options | Relies on recall rather than recognition |
| Typically capable of more powerful composition | Navigation is often more difficult |

Choose it when: the user is expert, the task is repeated, the operation must be scriptable and
composable, or the environment has no display.

### Graphical
Relies much more heavily on the pointer. Windows is the canonical example.

| Advantages | Disadvantages |
| --- | --- |
| Less expert knowledge required | Typically fewer options exposed |
| Easier navigation, quick exploration of structures | Usually less customisable |
| Fast task switching, several applications at once | One control rarely covers many variations |

Choose it when: the user is occasional, the task is exploratory, spatial relationships carry
meaning, or discoverability matters more than throughput.

**Both is a legitimate answer.** Many good systems expose a GUI for discovery and a CLI for
repetition. If you choose both, the two must agree on vocabulary and on what an operation does.

### GUI characteristics

The five defining elements, and what each buys you:

| Characteristic | What it is | Design consequence |
| --- | --- | --- |
| Windows | multiple windows allow different information to be displayed simultaneously | decide what a user needs side by side, and what must never be |
| Icons | represent files on some systems, processes on others | an icon without a label is a memory test |
| Menus | commands selected rather than typed | menu depth is the cost of every command |
| Pointing | a pointing device selects choices and indicates items of interest | target size and distance determine effort |
| Graphics | graphical elements can be mixed with text in the same display | graphics that do not carry information are noise |

---

## The five principles, as tests you can fail

These are the core of the phase. Each one is written here as a check, not as advice.

### Structure
Organise the interface purposefully, meaningfully and usefully, based on clear and consistent
models that are apparent and recognisable to users. Put related things together, separate
unrelated things, differentiate dissimilar things, and make similar things resemble one
another. This principle concerns the overall interface architecture.

**Test:** show a user two screens. Can they predict where a given control lives on the third?

### Simplicity
Make the common task easy. Communicate clearly and directly in the user's language. Provide
good shortcuts that are meaningfully related to the longer procedures.

**Test:** can a first-time user complete the primary task without documentation? Time it.
**Test:** does every shortcut have a discoverable long form that it is visibly related to?

### Visibility
Make all options and materials needed for a given task visible, without distracting the user
with extraneous or redundant information.

**Test:** for the current task, list every visible element. How many are needed? Elements that
are neither needed nor removable are a finding.

### Feedback
Keep users informed of actions, interpretations, changes of state or condition, and errors or
exceptions, through clear, concise and unambiguous language familiar to the user.

**Test:** after every action, can the user tell what happened without checking a log?
**Test:** does every action taking more than one second show progress?
**Test:** is every error message written in the user's vocabulary, and does it say what to do
next?

### Tolerance
Be flexible and tolerant. Reduce the cost of mistakes and misuse by allowing undo and redo.
Prevent errors where possible by tolerating varied inputs and sequences and interpreting all
reasonable actions.

**Test:** name every destructive action. Each one must have undo, or confirmation, or both.
**Test:** does the date field accept `2026-08-25`, `25/08/2026`, and `25 Aug 2026`? If not,
why is the user doing parsing work the machine could do?

---

## Error messages are interface design

The single highest-leverage interface work in most systems, and the most neglected. Every error
message has four jobs:

1. Say what happened, in the user's words, not the system's.
2. Say why, if the user could have caused it or could avoid it.
3. Say what to do next, concretely.
4. Preserve the user's work.

```
Bad:   Error 500: null pointer exception in OrderService.validate()
Bad:   Something went wrong. Please try again.
Good:  We could not process your payment because the card expiry date is in the past.
       Your basket is saved. Update the card details and try again.
```

The error catalogue in `templates/error-catalogue.md` forces this discipline by making every
error a row with all four columns.

---

## Accessibility

At `RIGOUR` 3 and above this is a gate criterion, not a nicety. Minimum sweep:

- Colour is never the only carrier of meaning.
- Contrast is sufficient for text at its rendered size.
- Every interactive element is reachable and operable by keyboard alone.
- Every control has an accessible name.
- Focus order follows reading order and focus is always visible.
- Motion can be reduced.
- The CLI equivalent: output is parseable without colour, and `--help` is complete.

---

## Exit

Run `checklist.md`, attempt G3. Handoff goes to `constructor` with the interface specification
and the error catalogue.
