# MODES

Ìlànà runs in exactly one mode at a time. The mode is chosen at boot (SKILL.md Step 0.4) and
recorded in the `MODE` register. Switching modes mid-run is legal and is logged as a `DEC-###`.

| Mode | Question it answers | Agents | Typical duration | File |
| --- | --- | --- | --- | --- |
| `FLEET` | "Build this properly, end to end." | up to 13 | hours to days | `fleet.md` |
| `TASK` | "Do this one thing, well." | 1 | minutes | `task.md` |
| `AUDIT` | "How bad is what we already have?" | 4 to 6 | 30 to 90 minutes | `audit.md` |
| `TUTOR` | "Teach me the process." | 1 (`conductor`) | open ended | `tutor.md` |
| `DOCTOR` | "Our process is broken. Why?" | 3 (`metrologist`, `quality-auditor`, `conductor`) | 30 minutes | `doctor.md` |
| `DRILL` | "Test whether I actually know this." | 1 | 10 to 40 minutes | `drill.md` |
| `MEMO` | degraded: no filesystem | 1 to 13 | any | see `kernel/KERNEL.md` section 6 |

## Choosing for the user

If the user will not pick, choose using this decision list, top down, and say which rule fired:

1. The user described a *system to build or rescue* -> `FLEET`.
2. The user named *one artifact* ("SRS", "test plan", "activity diagram", "defect report",
   "branching strategy") -> `TASK`.
3. The user pointed at *existing code and asked how it is* -> `AUDIT`.
4. The user described *symptoms* ("we keep missing deadlines", "the same bugs keep coming
   back", "releases break") -> `DOCTOR`.
5. The user asked *what something means* or *how something works* -> `TUTOR`.
6. The user has an *exam, interview, or assessment* -> `DRILL`.
7. Nothing matches -> ask once more, with two concrete options phrased in their own words.

## Mode contracts

Every mode obeys these regardless of which one is active:

- The boot sequence ran. The fork question was asked or explicitly resolved.
- At least one file is written to the user's repository (except `TUTOR`, `DRILL`, `MEMO`).
- The ledger is appended to.
- Constitution articles 1, 2, 7 and 8 apply without exception in every mode.
