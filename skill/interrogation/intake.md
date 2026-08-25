# INTAKE INTERROGATION

Runs at boot, in every mode, after the user has chosen FLEET or TASK. One batch. Five to nine
questions. Never one at a time.

## The batch

Adapt the wording; keep the substance.

```
Before Ìlànà starts, a short intake. Answer what you can. Say "assume" for anything
you would rather Ìlànà decided, and it will state its assumptions explicitly.

1. In one sentence, what problem is this solving, and for whom?
2. Who uses it, how often, and under what conditions?
3. Does it hold personal, health, or financial data, or affect anyone's safety or money?
4. What must it explicitly NOT do?
5. What already exists: code, docs, tickets, a previous attempt?
6. What is the deadline, and what happens if it is missed?
7. Three months after launch, what number tells you this worked?
```

Questions 3 and 6 together set `RIGOUR`, which is the most consequential register in the whole
system. Do not skip them.

## Mandatory regardless of anything

These two are asked in every mode, at every rigour, even when the user is impatient:

- **Who is harmed if this software is wrong?**
- **What data does this hold, and what happens to a person if it leaks?**

If the user declines, assume the worst plausible case for both, say so explicitly, and set rigour
accordingly.

## Deriving the registers

### RIGOUR

| Signals | Rigour |
| --- | --- |
| Throwaway, spike, personal experiment, nobody else will run it | 1 |
| Internal tool, portfolio project, small user base, low blast radius | 2 |
| Production software with real users, revenue, or reputation attached | 3 |
| Regulated: finance, health records, government, personal data at scale, legal obligation | 4 |
| Safety-critical: medical device, avionics, traffic, industrial control, anything that can injure | 5 |

Say the rigour out loud with its reason:

> Rigour 4. This holds patient records, so a privacy regime applies and the gates enforce
> traceability and independent review. Say if that is heavier than you want.

### PROCESS_STYLE

| Signals | Style |
| --- | --- |
| Requirements volatile, customer available continuously, frequent release | `agile` |
| Requirements stable, heavy regulatory documentation, staged approval | `plan-driven` |
| Regulatory obligation plus evolving product | `hybrid` |
| Deployment frequency is the dominant concern | `devops` |

### MODE

Already chosen at the fork. Confirm it is still right after the answers arrive; a request that
sounded like TASK often turns out to be FLEET, and saying so is helpful rather than pushy.

## Existing-project intake

When there is already code, ask fewer questions and read more. Before asking anything, check:

```bash
ls; cat README.md 2>/dev/null | head -50
ls docs 2>/dev/null; ls .github/workflows 2>/dev/null
git log --oneline -20 2>/dev/null; git tag 2>/dev/null | tail -5
find . -type d -name 'test*' -not -path './node_modules/*' 2>/dev/null | head
```

Then ask only what the repository cannot tell you:

1. What hurts most about this codebase right now?
2. What is the next thing that must ship, and by when?
3. What part is nobody willing to touch, and why?
4. Who else works on this?

## Handling "just build it"

Legitimate and common. Response:

1. Ask the two mandatory ethics questions only.
2. Assume everything else, from the strongest evidence available.
3. **Print the assumptions**, numbered, as `DEC-###` entries.
4. Proceed.

```
Proceeding on these assumptions. Correct any of them and Ìlànà will adjust.
  DEC-001  Rigour 2. No personal or financial data, internal users only.
  DEC-002  Process style: agile. Requirements will evolve.
  DEC-003  Single-tenant. No multi-tenancy in the data model.
  DEC-004  English only. No localisation.
  DEC-005  Target platform: Linux server, modern browsers.
```

An assumption written down is engineering. An assumption unspoken is what kills the project.

## What never appears in intake

- Technology stack questions. That is phase 02, and asking now invites a solution before the
  problem is stated.
- Anything answerable by reading the repository.
- More than nine questions. Users leave.
