<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.png">
  <img src="assets/logo.png" alt="Ìlànà" width="190">
</picture>

# ÌLÀNÀ

### A software engineering process operating system for coding agents

**Ìlànà** _(Yoruba: process, method, procedure, the disciplined way a thing is done)_

[![validate](https://github.com/Ferousco-dev/ilana/actions/workflows/validate.yml/badge.svg)](https://github.com/Ferousco-dev/ilana/actions/workflows/validate.yml)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![version](https://img.shields.io/badge/version-1.0.0-informational.svg)](VERSION)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**11 phases · 9 gates · 13 agents · 13 protocols · 7 modes · 17 constitutional articles**

_Built from SEN102/212 Software Engineering Process, Obafemi Awolowo University, Ile-Ife._

[Install](#install) · [Usage guide](docs/USING.md) · [Architecture](docs/architecture.md) · [Worked example](docs/examples/library-management-system.md) · [FAQ](docs/faq.md) · [Adapters](adapters/) · [Contributing](CONTRIBUTING.md)

</div>

---

## Why this exists

I am a software engineering student at **Obafemi Awolowo University, Ile-Ife**. We took SEN102/212,
Software Engineering Process. Requirements engineering, design levels, coding standards, four
testing levels, configuration management, quality assurance, CMMI, ISO/IEC 12207, process modeling,
professional ethics, team dynamics.

Then I went back to my editor and watched my coding agent do none of it.

Ask an agent for a login form and you get a login form. No requirement written down. No acceptance
criterion. No thought about the locked-account path or the bounced reset email. No test for either.
No record of why the session timeout is thirty minutes. It works, it ships, and six months later
nobody can safely change it.

The gap is not capability. Modern models are extremely capable. **The gap is process.**

So I turned the course into one. Not a summary of the slides. A working process that an agent runs:
that asks before it assumes, refuses to skip stages, writes down what it did, measures what it
claims, and can tell you exactly which gate you overrode and who accepted the risk.

That is Ìlànà.

---

## What it actually does

<table>
<tr><td width="50%" valign="top">

**Without Ìlànà**

```
> build a library system

Sure! Here's a library system.

[writes 400 lines]

Done! Let me know if you'd like
me to add anything else.
```

</td><td width="50%" valign="top">

**With Ìlànà**

```
> use ilana

Ìlànà online. Kernel loaded.

How should Ìlànà run this?
 [1] FLEET  a bundle of specialist agents,
            full gated lifecycle
 [2] TASK   one specialist, one artifact

Other modes: AUDIT, TUTOR, DOCTOR, DRILL.
```

</td></tr>
</table>

And then, ten minutes later, this happens:

```
[conductor] G1 attempt 1  verdict: FAIL

Criterion 3: no unmeasurable adjectives in requirements.
  docs/srs.md:41  "the search should be fast"
  docs/srs.md:58  "the interface must be simple for librarians"
  docs/srs.md:72  "student records must be secure"

Criterion 4: every requirement independently testable.
  REQ-011 "the system should handle reservations well" cannot be tested.

Remediate.
```

```
[analyst] Rewritten and confirmed with the head librarian.

  NFR-002  Search returns results within 1 second at the 95th percentile,
           over a catalogue of up to 50,000 items.

REQ-011 split into four. REQ-022 did not exist before: nobody had considered
what happens to an unclaimed reservation.

That is what the testability criterion is for.
```

**A gate did not just catch three sloppy adjectives. Forcing one requirement to be testable
discovered a missing requirement.** That is the cheapest possible place to find it, and Ìlànà found
it before a single line of code existed.

[Read the full worked example](docs/examples/library-management-system.md), including the gate the
user overrode and how that override followed them to the release gate.

---

## Install

Three ways. Pick one.

### 1. Let your coding agent do it

Paste this to Claude Code, Codex, Cursor, or anything else that can run shell commands:

```
install this skill: https://github.com/Ferousco-dev/ilana
```

The repository has an [`AGENTS.md`](AGENTS.md) at its root written for exactly this. Your agent
reads it, runs the three commands, and shows you the verification output. It also knows what
*not* to do, like vendoring the skill loose into your source tree.

### 2. One command

```bash
curl -fsSL https://raw.githubusercontent.com/Ferousco-dev/ilana/main/install.sh | sh
```

### 3. By hand, if you would rather read it first (you should)

```bash
git clone https://github.com/Ferousco-dev/ilana.git ~/.ilana-src
~/.ilana-src/bin/ilana install --link --all
~/.ilana-src/bin/ilana doctor
```

All three do the same thing: symlink `skill/` into every coding-agent directory on your machine.
Because they are symlinks to one directory, **`git pull` updates every agent at once**. Nothing
diverges.

`ilana doctor` tells you whether it worked:

```
  hosts:
    linked  claude-code  ~/.claude/skills/ilana -> ~/.ilana-src/skill
    linked  codex        ~/.codex/skills/ilana  -> ~/.ilana-src/skill
    absent  opencode     ~/.config/opencode/skills/ilana
```

<details>
<summary><b>Per-agent paths, if <code>--all</code> missed yours</b></summary>

| Agent | Guide | Mechanism |
| --- | --- | --- |
| Claude Code | [claude-code.md](adapters/claude-code.md) | `~/.claude/skills/ilana/` |
| OpenAI Codex | [codex.md](adapters/codex.md) | `AGENTS.md` + `~/.codex/skills/` |
| Cursor | [cursor.md](adapters/cursor.md) | `.cursor/rules/ilana.mdc` |
| Windsurf | [windsurf.md](adapters/windsurf.md) | `.windsurf/rules/` |
| Gemini CLI | [gemini-cli.md](adapters/gemini-cli.md) | `GEMINI.md` |
| GitHub Copilot | [copilot.md](adapters/copilot.md) | `.github/copilot-instructions.md` |
| Continue | [continue.md](adapters/continue.md) | `.continue/rules/` |
| Aider | [aider.md](adapters/aider.md) | `CONVENTIONS.md` |
| OpenCode | [opencode.md](adapters/opencode.md) | `~/.config/opencode/skills/` |
| Anything else | [generic.md](adapters/generic.md) | paste [`ILANA.md`](adapters/templates/ILANA.md) |

No skill mechanism at all? [`adapters/templates/ILANA.md`](adapters/templates/ILANA.md) is a single
self-contained file carrying the boot sequence, the constitution, the gates and the routing table.
Paste it into any system prompt or chat window.

</details>

---

## Use it

Start a **new** session in any project and say:

```
use ilana
```

Nothing happens until you answer one question:

```
Ìlànà online. Kernel loaded.

How should Ìlànà run this?

  [1] FLEET  a bundle of specialist agents running a full, gated lifecycle
  [2] TASK   one specialist, one focused operation, one artifact

Other modes: AUDIT, TUTOR, DOCTOR, DRILL.
```

**Answer `2` the first time.** See the machinery on something small before you commit a session to
a full lifecycle.

Then it asks five to nine questions in one batch and waits. Answer what you know; type `assume` for
the rest and it states its assumptions rather than hiding them.

### The things people actually say

| You say | You get |
| --- | --- |
| `ilana: write me a test plan for this service` | TASK mode, one artifact, minutes |
| `ilana: I'm building a URL shortener. Fleet mode.` | the full gated lifecycle |
| `audit this repo with ilana` | read-only scoring of all eleven phases, ranked findings |
| `ilana: gate this before I ship` | release readiness check; finds the rollback you never tested |
| `ilana doctor mode: the same bugs keep coming back` | diagnoses the process, prescribes **one** fix |
| `ilana drill: gauntlet` | 40 questions and a scorecard by phase |
| `rigour 2` | mid-run, drops the strictness |
| `override, demo is Friday` | accepts a failed gate, records your reason, moves on |

### Or use the slash commands

Installed automatically. `ilana commands` lists them.

| Command | Does |
| --- | --- |
| `/ilana` | boot, ask the fork question |
| `/ilana:task <what>` | one specialist, one artifact |
| `/ilana:fleet <what>` | the full gated lifecycle |
| `/ilana:audit` | score this repo, read-only |
| `/ilana:review` | code review against the standard and G4 |
| `/ilana:ship` | release readiness, gate G6 |
| `/ilana:gate G4` | run one gate |
| `/ilana:doctor <symptom>` | diagnose the process |
| `/ilana:status` | where am I in the process |
| `/ilana:rigour 2` | set the strictness dial |
| `/ilana:drill gauntlet` | 40 questions and a scorecard |
| `/ilana:tutor <concept>` | learn something properly |

`/ilana:task` and `/ilana:review` are the two you will use most.

### And from the shell, without an agent

```bash
ilana status              where this project is in the process
ilana gate G4             run one gate; reads rigour from the ledger
ilana metrics             product, process and project metrics
ilana trace               requirement coverage gaps
ilana doctor              verify the installation
```

**If it feels heavy, you are at the wrong rigour.** Say `rigour 2` and it becomes a light
sanity-check that still writes things down.

**Full guide: [docs/USING.md](docs/USING.md)** covers reading gate verdicts, steering, overriding,
the ledger, team setup and troubleshooting.

---

## The architecture

Ìlànà is built as a small operating system, not a checklist. Checklists degrade under context
pressure: the model reads them, keeps the first three items, and the rest evaporate. An OS does not,
because each layer is loaded only when it is needed.

```
    SKILL.md          boot loader     always read, deliberately short
        |
    kernel/           mechanism       constitution, state machine, ledger, refusals
        |
    modes/            scheduler       FLEET · TASK · AUDIT · TUTOR · DOCTOR · DRILL
        |
    gates/            enforcement     G0..G8, the part that says no
        |
    +---------+---------+---------+---------+---------+
    |         |         |         |         |         |
 phases/  agents/  protocols/ instruments/ references/ interrogation/
 11 stages 13 roles 10 procs   metrics      standards   questions
        |
    .ilana/           your filesystem, your repository, the source of truth
```

Three properties fall out of this shape:

**Shardable.** No invocation reads the whole tree. Boot reads `SKILL.md`, the kernel and one mode.
A phase adds one guide and one template. The payload is 100,000 words; the context cost per
operation is a few thousand.

**Resumable.** State lives in `.ilana/`, not in the conversation. A session can end anywhere and
another agent, another model, or a human can pick it up from the ledger.

**Degradable.** No sub-agents? Rotate the agent cards sequentially, same artifacts. No filesystem?
Emit fenced blocks with intended paths. No Python? Every instrument documents a manual procedure.
Nothing is a hard dependency except reading, writing and talking to a human.

[Full design rationale](docs/architecture.md)

---

## The eleven phases

Nine sequential, two continuous, all derived from the course syllabus.

```
                              G0 INTAKE
                                  |
  01 REQUIREMENTS ──G1──> 02 DESIGN ──G2──> 03 INTERFACE ──G3──> 04 CONSTRUCTION
                                                                        |
                                                                       G4
                                                                        |
  08 ASSESSMENT <──G7── 07 QUALITY <──G6── 06 SCM <──G5── 05 VERIFICATION
        |
       G8 CLOSURE

  09 PROCESS MODELING ....... continuous, describes all of the above
  10 TOOLING ................ continuous, automates all of the above
  11 ETHICS AND TEAMS ....... continuous, constrains all of the above
```

| #   | Phase                        | Covers                                                                                                                                               | Emits                                  |
| --- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| 01  | **Requirements**             | elicitation (8 techniques), analysis, specification, validation, management; functional, non-functional and domain types; 6 challenges, 6 strategies | SRS (IEEE 830), traceability matrix    |
| 02  | **Architecture and design**  | three levels, six design objectives, NFR mechanisms, architecture decision records                                                                   | design description (IEEE 1016), ADRs   |
| 03  | **Interface design**         | text-based vs graphical, GUI characteristics, the five UI principles as tests you can fail                                                           | interface spec, error catalogue        |
| 04  | **Construction**             | three goals of coding, six standards, seven guidelines, language characteristics                                                                     | coding standard, code review records   |
| 05  | **Verification**             | four levels, integration strategies, test planning, automation, defect lifecycle                                                                     | test plan (IEEE 829), defect log       |
| 06  | **Configuration management** | version control, change management, build management, release management                                                                             | SCM plan, rollback plan, changelog     |
| 07  | **Quality assurance**        | five core activities, reviews vs walkthroughs vs inspections vs audits, three metric categories, seven quality attributes                            | quality management plan, scorecard     |
| 08  | **Process assessment**       | measurement, CMMI five levels, ISO/IEC 12207 three categories, optimization                                                                          | maturity assessment, SPI plan          |
| 09  | **Process modeling**         | UML activity diagrams, BPMN, documentation standards, workflows                                                                                      | process model, documentation plan      |
| 10  | **Tooling**                  | CASE tools (upper, lower, integrated), Jira, Trello, Jenkins, GitHub Actions                                                                         | toolchain decision record, CI pipeline |
| 11  | **Ethics and teams**         | five ethical issues, ACM/IEEE code, team dynamics, Agile, DevOps, plan-driven                                                                        | ethics register, RACI, process style   |

Every phase ships six files plus templates: a phase guide, a checklist, a question set,
**anti-patterns**, a gate summary, and a condensed reference from the course.

---

## The nine gates

A gate is a named checkpoint with explicit criteria, required evidence, and a permanent record.
This is the part of Ìlànà that says no.

| Gate   | Closes       | Sample criterion                                                                                      |
| ------ | ------------ | ----------------------------------------------------------------------------------------------------- |
| **G0** | intake       | rigour set and justified; harm and data exposure scanned                                              |
| **G1** | requirements | no unmeasurable adjectives; every NFR has a number and a unit                                         |
| **G2** | design       | every requirement maps to a design element **and back**; every NFR has a mechanism                    |
| **G3** | interface    | every destructive action has undo or confirmation; every error says what to do next                   |
| **G4** | construction | no secrets in the tree **or the history**; coding standard machine-enforced                           |
| **G5** | verification | test plan predates execution; every requirement has a test; all four levels present or the gap stated |
| **G6** | release      | built from a tag; **rollback rehearsed, with a date**                                                 |
| **G7** | quality      | quality plan predates construction; three metric categories; seven attributes with evidence           |
| **G8** | closure      | retrospective held; one concrete process change carried forward                                       |

### Rigour: the dial that makes it usable

The course is explicit that no single process fits all projects, and a process tool that ignores
that gets uninstalled by the second project. So every criterion carries a rigour threshold.

| Rigour | Project                                     | Gates                                                |
| ------ | ------------------------------------------- | ---------------------------------------------------- |
| **1**  | throwaway script, spike                     | advisory; ledger still written                       |
| **2**  | internal tool, portfolio site               | warn; one override each                              |
| **3**  | production software, real users             | enforce; overrides logged and counted                |
| **4**  | regulated: finance, health, government      | enforce; overrides need written justification        |
| **5**  | safety-critical: medical, avionics, control | **no overrides**; independent verification mandatory |

The phases never disappear. Even at rigour 1 you are asked what problem you are solving and whether
anyone gets hurt if it is wrong. What scales is the ceremony, not the thinking.

### Overrides are recorded, never silent

```
[conductor] G4 OVERRIDE ACCEPTED

Unmet: criterion 3, integration tests for every module boundary.
Consequence here: the payment/ledger boundary is where money is reconciled,
and it will ship unverified.
Your reason (recorded): "demo Friday, integration suite next sprint".
Recorded as OVERRIDE-002. Advancing to phase 05.
```

Ìlànà does not argue twice, does not lecture, and does not pretend the gate was met. It names the
specific consequence for _your_ project, records your reason, and carries the risk forward so it
appears again at the release gate, where it matters.

---

## The thirteen agents

Not for parallelism. For **separation of duties**.

The value of `verifier` is not that it tests faster. It is that it does not fix what it raised, so
the confirmation is independent. The value of `quality-auditor` is that it does not audit its own
work. The value of `ethics-officer` is that it can stop the run and `conductor` cannot overrule it.

| Agent                    | Course role           | Charter                                      | Never                                      |
| ------------------------ | --------------------- | -------------------------------------------- | ------------------------------------------ |
| `conductor`              | Project Manager       | gates, schedule, ledger, risks               | writes production code                     |
| `analyst`                | Business Analyst      | need into testable, traceable requirements   | resolves a stakeholder conflict alone      |
| `architect`              | Software Designer     | requirements into structure at three levels  | picks tech before naming the NFR it serves |
| `interaction-designer`   | UI/UX Designer        | structure into something a human can operate | ships an error with no next action         |
| `constructor`            | Software Developer    | design into code that obeys the standard     | signs its own acceptance                   |
| `verifier`               | Tester / QA Engineer  | breaks it at four levels, writes it down     | fixes what it raised                       |
| `configuration-engineer` | DevOps Engineer       | branches, changes, builds, releases          | approves its own change requests           |
| `quality-auditor`        | SQA Engineer          | reviews, inspections, audits, compliance     | audits work it produced                    |
| `metrologist`            | Metrics Analyst       | the numbers                                  | offers opinion where data exists           |
| `process-modeler`        | Process Engineer      | draws the process before anyone argues       | models the ideal instead of the real       |
| `documentarian`          | Technical Writer      | knowledge that survives departures           | writes docs at the end, from memory        |
| `ethics-officer`         | Professional Practice | **holds the veto**                           | negotiates on public interest              |
| `release-manager`        | Release Engineer      | go/no-go and the way back                    | releases without a rehearsed rollback      |

Every agent card carries a charter, what it owns, its refusal list, and a **handoff contract**:

```
HANDOFF
  from:     analyst
  to:       architect
  gate:     G1 PASSED
  produced: docs/srs.md, .ilana/traceability.csv
  ids:      REQ-001..REQ-024, NFR-001..NFR-009, DOM-001..DOM-003
  open:     REQ-017 conflicts with NFR-004. Stakeholder decision needed.
  assumed:  DEC-005 peak concurrency 5000, unconfirmed by operations.
  next:     decompose REQ-001..REQ-012; hold reporting until REQ-017 resolves.
```

The receiving agent **must** address or explicitly defer every open item. Silently inheriting an
open conflict is exactly how a requirements ambiguity becomes a production defect three phases
later, and the contract makes it impossible to do quietly.

---

## The constitution

Sixteen articles, **ordered by precedence**. That ordering is the whole point: when public interest
conflicts with the schedule, there is no weighing to do, because Article 1 already decided it. A
judgement call becomes a lookup, which is what you want under pressure.

<details>
<summary><b>All seventeen articles</b></summary>

1. **Public interest is supreme.** Where user or public interest conflicts with schedule, budget or
   convenience, the public interest wins.
2. **Truthful reporting.** No describing untested code as tested, no hiding a failing test, no
   softening a security finding.
3. **No requirement, no code.** Every unit of production work traces backwards to a requirement and
   forwards to a test.
4. **Ambiguity is a defect.** "User-friendly" has already failed.
5. **Prevention outranks detection.** Reviews before execution-based testing.
6. **Process adherence is an ethical duty.** Skipping testing to hit a date transfers risk onto
   people who did not consent to carry it.
7. **Confidentiality.** No credentials, personal data or proprietary source anywhere they do not
   belong.
8. **Respect ownership.** Licences honoured, attribution preserved.
9. **Competence.** Disclose when the work is beyond demonstrated skill; require domain review where
   being wrong hurts people.
10. **Measure before you claim.** No superlative without an instrument.
11. **Every change is a change request.** Impact analysis before approval, never after.
12. **Write it down.** If it is not in an artifact or the ledger, it did not happen.
13. **One process does not fit all projects.** That is what rigour is for.
14. **Teams are part of the system.** Role clarity and communication paths are engineering concerns.
15. **Continuous improvement.** Measure, Analyze, Improve, Repeat.
16. **The human is in command.** Ìlànà advises, gates and refuses. It does not overrule.
17. **Repository evidence outranks assertion.** Prompts, roadmaps and earlier reports lose to git, code,
    migrations and tests.

</details>

### What it refuses

Three categories, and **nothing else**:

1. **Control-defeating code.** Hidden credentials, backdoors, disabled audit logging, suppressed
   test results.
2. **Fabricated evidence.** Claiming a test passed without having seen it pass.
3. **Ownership violations.** Code whose licence forbids the use, a previous employer's proprietary
   source, real personal data in fixtures.

It does **not** refuse security tooling for authorised work, aggressive refactoring, deleting your
own code, shipping fast at rigour 1, or anything that merely sounds risky. Over-refusing is its own
failure, because it trains people to ignore refusals when they matter.

Refusals are one paragraph: what was asked, why not, and **the legitimate alternative**. No
lecture, no repetition.

---

## Seven modes

Every invocation begins by asking which. That question is not optional, because both failure modes
are real: under-serving (write some code, skip the process) and over-serving (a thirteen-agent
lifecycle for a one-page test plan).

| Mode       | Answers                              | Agents            |
| ---------- | ------------------------------------ | ----------------- |
| **FLEET**  | "Build this properly, end to end."   | up to 13          |
| **TASK**   | "Do this one thing, well."           | 1                 |
| **MAINTAIN** | "Change this existing repo safely, with the least paperwork." | 1 to 3 |
| **AUDIT**  | "How bad is what we already have?"   | 4 to 6, read-only |
| **TUTOR**  | "Teach me the process."              | 1                 |
| **DOCTOR** | "Our process is broken. Why?"        | 3                 |
| **DRILL**  | "Test whether I actually know this." | 1                 |

### MAINTAIN: for repositories that already exist

`FLEET` designs a system. `MAINTAIN` works inside one. It produces the minimum documentation the
risk level needs and the maximum verified repository evidence:

- **Repository map** of packages, entry points, import edges, migrations, tables, env vars, branch,
  recent commits and uncommitted work (`ilana map`).
- **Milestone checkpoint** (`handoff.json` rendered to `milestone-state.md`): completed, current step,
  verified, remaining, limitations, next action. Another agent resumes from it alone.
- **Ceremony levels** `light`, `standard`, `regulated`, so a small change does not pay for a
  regulated lifecycle.
- **Automatic evidence**: every command run is recorded with head commit and exit code; the final
  validation report is rendered from those records, not written.
- **Scope guard**: pre-existing uncommitted work is protected byte for byte; out-of-scope changes fail
  the guard (`ilana guard`).
- **Privacy checklist** generated from what the repository actually handles, plus log lines to review
  and marker tests that prove a secret never reached an output (`ilana privacy`).
- **Commit hygiene**: Conventional Commits, and no AI or co-author attribution, checked and hookable.
- **Stop boundary** so the next roadmap item is never started, and a **reality check** so the
  repository overrides stale prompts and reports (Article 17).

<details>
<summary><b>AUDIT mode output</b></summary>

```
| Phase                 | Score | Gap                                        |
| 01 Requirements       |   0   | requirements exist only in people's heads  |
| 05 Verification       |   1   | unit only, no integration level            |
| 06 Configuration mgmt |   1   | no tags, no changelog, no rollback         |
| 07 Quality assurance  |   0   | no reviews required, no metrics            |

Mean 1.0.  Indicative CMMI level 2 Managed (partial). Not a formal appraisal.

F-01 [critical]  No release tags.
     Evidence: `git tag` returns nothing across 847 commits.
     Cost of inaction: you cannot say what is in production, and you cannot
     roll back. This is the finding that will hurt you first.
     Fix: tag the production commit today.   Effort: 5 minutes.
```

Findings ranked by **cost of inaction**, not by distance from the textbook. And a mandatory
"what is already good" section, because an audit that only finds fault gets routed around.

[Full audit example](docs/examples/audit-run.md)

</details>

<details>
<summary><b>DOCTOR mode: symptom to root cause</b></summary>

| You say                                | Likely root cause                               | Phase |
| -------------------------------------- | ----------------------------------------------- | ----- |
| "We keep building the wrong thing"     | elicitation failure, no stakeholder validation  | 01    |
| "Requirements keep changing"           | no change control, not a requirements problem   | 06    |
| "The same bugs keep coming back"       | no regression suite, no root-cause analysis     | 05    |
| "Two developers built the same module" | role ambiguity, no RACI                         | 11    |
| "Deployments fail"                     | environments diverge, no infrastructure as code | 06    |
| "We are always late"                   | no measurement, estimating from optimism        | 08    |
| "Reviews are rubber stamps"            | walkthrough posing as inspection                | 07    |
| "We are Agile but nothing improves"    | retrospectives with no follow-through           | 08    |

**One prescription per diagnosis.** With a metric, a baseline, and a recheck date. Prescribing five
changes at once guarantees none of them are evaluated.

</details>

---

## Instruments

Article 10 says no superlative without a number. These are the numbers. Dependency-free Python 3,
standard library only, so they run anywhere.

```bash
python3 skill/instruments/scripts/metrics.py --repo .
python3 skill/instruments/scripts/gate_check.py --gate G4 --rigour 3
python3 skill/instruments/scripts/traceability.py --file .ilana/traceability.csv
python3 skill/instruments/scripts/ledger.py status
```

```
GATE G4   rigour 3

  [pass] R1+  coding standard or linter config present
  [FAIL] R1+  no plausible secrets in the working tree
  [pass] R2+  CI configuration present
  [MAN ] R1+  every module traces to a DES element
  [MAN ] R3+  peer review completed for every change
  [skip] R4+  dependency register exists

plausible secrets found:
  src/config/db.js:14
  move these to configuration or a secret store. if any reached the
  history, rotate the secret; deletion is cosmetic.

VERDICT: not ready. 1 automated criteria unmet.
```

Note `[MAN]`. Criteria requiring human judgement are reported as manual and **never silently
passed**. A tool that quietly marks a judgement call as green is worse than no tool.

Every instrument documents a manual procedure for when Python is unavailable.

---

## The ledger

Ìlànà writes its memory into `.ilana/` in **your** repository. Plain text. Diffable. Yours.

```
.ilana/
  state.json         MODE, PHASE, GATE, AGENT, RIGOUR, open items, overrides
  ledger.md          append-only narrative; corrections supersede, never overwrite
  traceability.csv   requirement -> design -> module -> test -> result
  defects.md         nine-field defect log with lifecycle states
  decisions.md       DEC-### decisions and every logged assumption
  changes.md         CR-### with impact analysis
  risks.md           RSK-### register
  ethics.md          ETH-### findings, halts, dispositions
  metrics.csv        MET-### time series, every value with a source
  gates/G0..G8.md    one evidence record per gate attempt
```

```markdown
## 2026-08-24 14:02 | G4 | verifier | GATE PASS

Evidence:

- tests/ contains 61 cases, TC-001..TC-061
- unit 44, integration 12, system 4, acceptance 1
- run: 61 passed, 0 failed, coverage 78% (build/coverage.xml)
  Traceability: 24/24 REQ have >= 1 TC. 9/9 NFR have >= 1 TC. Gap: none.
```

Commit it. **Process history is project history**, it is plain text, and it outlives any particular
tool, model or vendor. `ilana uninstall` never touches it.

---

## Updating

Ìlànà updates on **your** side, not only in this repository. That is the difference between a skill
you copied once and a skill you actually keep.

```bash
ilana check                       # compare local against upstream
ilana update                      # pull and refresh every install
ilana autoupdate --enable         # weekly, via launchd or systemd
ilana channel edge                # track main instead of tagged releases
ilana pin 1.2.0                   # hold a version across a project
ilana doctor                      # verify everything
```

If you installed with `--link` (the default), a single `git pull` in `~/.ilana-src` updates every
agent on the machine at once, because they all point at the same directory.

At boot, Ìlànà reads a local timestamp. If the last check was over a week ago it emits **one line**
and continues. It never blocks, and it never touches the network on its own. A process tool that
interrupts your work to talk about itself has misunderstood its job.

### Local rules that survive updates

Never edit the installed skill. Put house rules in overrides:

```bash
cat > ~/.config/ilana/overrides/gates/G4.append.md <<'RULES'
## House rules
- All SQL goes through the query builder. No string concatenation, ever.
- Every public function documents its error conditions.
RULES
```

Ìlànà reads these after the core file and treats them as additive. Your rules survive every update,
and the diff between your process and upstream stays visible.

---

## For students

If you are also taking SEN102/212, or an equivalent anywhere else:

```
ilana tutor: explain the difference between an audit and a review
ilana drill: phase 07
ilana drill: gauntlet
ilana drill: scenario
```

**TUTOR** teaches with the confusion pairs and worked examples. **DRILL** tests, marks honestly, and
tells you which phase your errors cluster in.

```
DRILL RESULT  |  GAUNTLET  |  40 questions

05 Verification         5/8   WEAK: confuses integration with system testing
07 Quality assurance    2/5   WEAK: review vs audit; walkthrough vs inspection
08 Process assessment   1/3   WEAK: CMMI level 3 vs level 4 boundary

Total 28/40 (70%)

Three things to fix, in order:
  1. phases/07-quality-assurance/reference.md, reviews and audits
  2. references/cmmi.md, the level 3 to 4 boundary
  3. re-run DRILL PHASE on 05
```

[Syllabus map](docs/syllabus-map.md) connects every course topic to its location in the skill. The
complete original lecture deck is in [`source/`](source/), so you can always check the primary text.

---

## Repository layout

```
ilana/
├── skill/                      the payload; this is what gets installed
│   ├── SKILL.md                boot loader and router
│   ├── kernel/                 constitution, state machine, ledger spec, refusals, glossary
│   ├── modes/                  FLEET, TASK, AUDIT, TUTOR, DOCTOR, DRILL
│   ├── gates/                  G0 through G8, criteria scaled by rigour
│   ├── phases/                 11 phases x (guide, checklist, questions,
│   │                             anti-patterns, gate, reference, templates)
│   ├── agents/                 13 role cards with charters and handoff contracts
│   ├── protocols/              10 cross-phase procedures
│   ├── instruments/            metrics, gate check, traceability, ledger (Python 3)
│   ├── references/             standards, CMMI, ethics, methodology, tools, reading list
│   ├── interrogation/          intake questions + 12 assessment banks
│   ├── assessments/            DRILL formats and marking rubrics
│   └── update/                 the self-update mechanism
├── adapters/                   10 host guides + self-contained single-file version
├── bin/ilana                   the CLI
├── AGENTS.md                   how an agent installs this, and how to contribute
├── docs/USING.md               the usage guide: what to say, how to read it, how to steer
├── docs/                       quickstart, architecture, FAQ, syllabus map, examples
├── source/                     the original SEN102/212 lecture deck
├── tests/validate.sh           structural validation, run by CI
└── install.sh                  one-command bootstrap
```

---

## Contributing

**Pull requests are genuinely wanted.** This came out of a course, and it gets better when people
who have shipped real systems argue with it.

Most valuable, in order:

1. **New host adapters.** If your agent is not in `adapters/`, add it. Easiest to review, highest
   value.
2. **Better gate criteria.** If a check has actually caught something for you, add it, with the
   rigour threshold at which it should apply.
3. **Anti-patterns from real projects.** Every entry should be something you watched happen. Those
   are the most useful pages in the whole skill.
4. **Instruments, assessment questions, translations, worked examples.**

House style is enforced by `make check`: **no em dashes anywhere**, direct and concrete prose,
tables over paragraphs for comparisons, standard-library-only Python, POSIX shell.

Ìlànà holds itself to Article 3: every pull request says what its change is traceable to, whether
the source material, a named standard, or a real failure you can describe.

```bash
git clone https://github.com/Ferousco-dev/ilana.git && cd ilana
make check
```

[CONTRIBUTING.md](CONTRIBUTING.md) · [GOVERNANCE.md](GOVERNANCE.md) ·
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) · [SECURITY.md](SECURITY.md)

---

## Attribution

The engineering content derives from **SEN102/212 Software Engineering Process**, Department of
Software Engineering, **Obafemi Awolowo University, Ile-Ife**. Lecturers whose material informs this
work: Dr (Mrs) Onifade M. T., F. C. Ugwu, and Ubochi Chibueze Nmamouh. Copyright in the original
lecture material remains with its authors and with the university; the complete deck is included in
[`source/`](source/) for reference and attribution.

Everything built on top of it, the kernel, the constitution, the gate system, the agent fleet, the
protocols, the instruments, the refusal protocol, the mode system and the tooling, is original work
under MIT.

Standards referenced descriptively: ISO/IEC 12207, ISO/IEC 25010, IEEE 830, IEEE 1016, IEEE 829,
CMMI, and the ACM/IEEE Software Engineering Code of Ethics. See [NOTICE](NOTICE).

---

<div align="center">

**MIT licensed. Built in Ile-Ife.**

_Ìlànà: the disciplined way a thing is done._

</div>
