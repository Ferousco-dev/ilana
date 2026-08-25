# USING ÌLÀNÀ

Install takes a minute. This is the part that matters: what you actually say, what comes back, and
how to steer it.

---

## 1. Your first session

Open your coding agent in any project and say:

```
use ilana
```

You get this, and nothing else happens until you answer:

```
Ìlànà v1.0.0 online. Kernel loaded. Awaiting mode selection.

How should Ìlànà run this?

  [1] FLEET  a bundle of specialist agents running a full, gated lifecycle.
             Best for: a new feature, a new service, rescuing something broken,
             a full audit. Costs more. Produces a complete paper trail.

  [2] TASK   one specialist, one focused operation, one artifact.
             Best for: "write the test plan", "review this diff",
             "draw the activity diagram", "check my Git branching".

Other modes: AUDIT, TUTOR, DOCTOR, DRILL.
```

**Answer `2` the first time.** Fleet mode is real work and you should see the machinery on
something small before you commit a session to it.

Then it asks five to nine questions **in one batch**, and waits. Answer what you know. For anything
you do not, type `assume` and it will state its assumption out loud rather than hiding it.

That is the whole interaction model: it asks, you answer, it works, it shows you a verdict.

---

## 2. What to say

You do not need to memorise commands. Ìlànà is prose-triggered. But these are the phrasings that
land cleanly.

### Starting

| You say | You get |
| --- | --- |
| `use ilana` | the boot sequence and the fork question |
| `ilana: build a URL shortener` | boot, and it reads your intent as FLEET |
| `ilana: write me a test plan` | boot, and it reads your intent as TASK |
| `audit this repo with ilana` | AUDIT mode, read-only, scores all eleven phases |
| `ilana doctor mode: we keep missing deadlines` | DOCTOR mode, diagnoses the process |
| `ilana tutor: what is the difference between a walkthrough and an inspection` | TUTOR mode |
| `ilana drill: gauntlet` | 40 questions and a scorecard |

### Mid-run

| You say | Effect |
| --- | --- |
| `assume` | it states its assumptions as decision records and continues |
| `rigour 2` | drops the strictness; gates warn instead of blocking |
| `rigour 4, this handles payments` | raises it; gates enforce and overrides need justification |
| `override, demo is Friday` | accepts a failed gate, records your reason, moves on |
| `why did that gate fail` | it restates the unmet criteria and the evidence |
| `switch to task mode` | abandons the fleet, keeps the ledger |
| `rotate, do not spawn` | runs the fleet sequentially in one context instead of parallel agents |
| `skip the interface phase, this is a library` | records the skip with your reason |
| `stop` | halts cleanly; `.ilana/` holds your position for next time |

### Slash commands

Installed with the skill. Faster than prose once you know them.

| Command | Same as saying |
| --- | --- |
| `/ilana` | `use ilana` |
| `/ilana:task write a test plan` | `ilana: write me a test plan` |
| `/ilana:fleet a URL shortener` | `ilana: build a URL shortener, fleet mode` |
| `/ilana:audit` | `audit this repo with ilana` |
| `/ilana:review` | `ilana: review this diff` |
| `/ilana:ship` | `ilana: gate this before I ship` |
| `/ilana:gate G4` | `ilana: run gate G4` |
| `/ilana:doctor <symptom>` | `ilana doctor mode: <symptom>` |
| `/ilana:status` | `ilana: where am I` |
| `/ilana:rigour 2` | `rigour 2` |
| `/ilana:drill gauntlet` | `ilana drill: gauntlet` |
| `/ilana:tutor <concept>` | `ilana tutor: <concept>` |

`ilana commands` lists them with descriptions. They are a convenience layer, never a requirement:
every one has a prose equivalent, which matters because most agents have no slash-command
mechanism.

### From the shell, without an agent

Some things do not need a conversation.

```bash
ilana status              where this project is in the process
ilana gate G4             run one gate; reads rigour from .ilana/state.json
ilana gate G6 5           run a gate at an explicit rigour
ilana metrics             product, process and project metrics
ilana metrics --json      the same, machine readable
ilana trace               which requirements have no design, no test, no verification
ilana commands            list the slash commands
ilana doctor              verify the installation
```

These are wrappers over the instruments in `skill/instruments/scripts/`, which are plain Python 3
with no dependencies and can be called directly if you prefer.

### Resuming

Just say `use ilana` again in the same project. It reads `.ilana/` and tells you where you were:

```
Resuming. MODE=FLEET PHASE=05 GATE=G4 AGENT=verifier RIGOUR=3
Open: DEF-004 (severity high, unassigned), CR-002 (awaiting approval)
Last ledger entry: 2026-08-24 G4 passed, evidence tests/report.xml
```

---

## 3. Reading the output

Three things appear constantly. Once you can read them the whole system is legible.

### The agent prefix

```
[analyst] REQ-014 conflicts with NFR-004. Both cannot hold.
[architect] Accepted. Blocking the reporting subsystem until REQ-014 resolves.
[ethics-officer] No exposure concerns in this subsystem. No halt.
```

Thirteen specialists, one speaking at a time. You always know who. If `[ethics-officer]` speaks,
read it carefully; it is the only agent that can stop the run.

### The gate verdict

```
[conductor] G1 attempt 1  verdict: FAIL

| # | Criterion                      | Met | Evidence                    |
| 3 | no unmeasurable adjectives     | NO  | 3 hits                      |
| 4 | independently testable         | NO  | REQ-011                     |

Adjective scan:
  docs/srs.md:41   "the search should be fast"

Remediate.
```

Failure is normal and is the point. A gate that never fails is a gate nobody set correctly.

**Two failures on the same gate and it stops** and escalates instead of grinding, because a gate
failing twice means the problem is upstream.

### The handoff

```
HANDOFF
  from:     analyst
  to:       architect
  gate:     G1 PASSED
  produced: docs/srs.md, .ilana/traceability.csv
  ids:      REQ-001..REQ-024, NFR-001..NFR-009
  open:     REQ-017 conflicts with NFR-004. Stakeholder decision needed.
  assumed:  DEC-005 peak concurrency 5000, unconfirmed by operations.
  next:     decompose REQ-001..REQ-012 into design elements.
```

**Read the `open` and `assumed` lines.** That is where the honesty lives. If an assumption is wrong,
say so now; it is free here and expensive three phases later.

---

## 4. Rigour: the one dial that matters

Set at intake, changeable any time. It scales how hard every gate bites.

| Say | Rigour | For | Gates |
| --- | --- | --- | --- |
| `rigour 1` | 1 | throwaway script, spike, weekend experiment | advisory only |
| `rigour 2` | 2 | internal tool, portfolio project | warn, one override each |
| `rigour 3` | 3 | production software with real users | enforce, overrides logged |
| `rigour 4` | 4 | finance, health records, government, personal data at scale | enforce, overrides need written justification |
| `rigour 5` | 5 | medical devices, avionics, traffic control | **no overrides at all** |

**If Ìlànà feels heavy, you are at the wrong rigour.** Say `rigour 2` and it becomes a light
sanity-check that still writes things down. The phases never disappear, but the ceremony does.

If you set 5, it will refuse to override a gate. That is deliberate, and it will say so and stop
rather than pretending.

---

## 5. Recipes

The things people actually want, and what to say.

### "I want to start a new project properly"

```
ilana: I'm building <describe it>. Fleet mode.
```

Expect: intake questions, then a phase walk from requirements through to closure, with a gate
between each. Budget a real session. It will produce an SRS, a design document, a test plan and a
ledger.

### "I want one document, not a lifecycle"

```
ilana: write me a test plan for this service
ilana: draw me the activity diagram for the checkout flow
ilana: write the SRS for what this code already does
ilana: review this diff
ilana: check my branching strategy
ilana: write a rollback plan for this deploy
```

TASK mode. One specialist, one artifact, minutes not hours. This is the mode you will use most.

### "I inherited a codebase and I do not know how bad it is"

```
audit this repo with ilana
```

Read-only. Scores all eleven phases 0 to 4, gives an indicative maturity level, and produces
findings ranked by **cost of inaction** with a three-horizon remediation plan. Writes exactly one
file and changes nothing else.

### "Something about how we work is broken"

```
ilana doctor mode: the same bugs keep coming back
ilana doctor mode: our deployments keep failing
ilana doctor mode: we're always late
```

Diagnoses the process rather than the code. Gives you **one** prescription with a metric, a
baseline and a recheck date. One, deliberately, because five simultaneous changes cannot be
evaluated.

### "I am about to ship and I want a second opinion"

```
ilana: gate this before I ship
```

Runs G6 release readiness: built from a tag, changelog written, rollback rehearsed, monitoring
defined, every change traceable. It will find the rollback you have never actually tested.

### "I am revising for an exam"

```
ilana drill: gauntlet
ilana drill: phase 07
ilana tutor: explain CMMI level 3 versus level 4
```

Marks honestly and tells you which phase your errors cluster in.

### "I want to check my own work with the tools"

```bash
python3 ~/.ilana-src/skill/instruments/scripts/gate_check.py --gate G4 --rigour 3
python3 ~/.ilana-src/skill/instruments/scripts/metrics.py --repo .
python3 ~/.ilana-src/skill/instruments/scripts/traceability.py
```

No agent needed. These run standalone.

---

## 6. What it writes to your repository

Ìlànà creates `.ilana/` in your project. Plain text, diffable, yours.

```
.ilana/
  state.json         where the run is: mode, phase, gate, rigour, open items
  ledger.md          append-only narrative of everything that happened
  traceability.csv   requirement -> design -> module -> test -> result
  defects.md         defect log
  decisions.md       decisions and every assumption it made
  gates/G0..G8.md    one evidence record per gate attempt, including overrides
```

**Commit it.** Process history is project history. It survives Ìlànà, your agent, and your vendor.

You can also create it yourself without an agent:

```bash
ilana init --project my-service --rigour 3
```

`ilana uninstall` never touches `.ilana/`.

---

## 7. Steering, overriding and disagreeing

Ìlànà is strict, not stubborn. Article 16 says the human is in command.

**A gate fails and you disagree.** Say why, and override:

```
override: this is a CLI with no destructive commands, G3 does not apply here
```

It records the reason and moves on. It does not argue twice.

**It asks too many questions.** Say `assume` once. It will state its assumptions and stop asking.

**It is too heavy.** Say `rigour 1`.

**It refused something.** It refuses exactly three things: code that defeats a control, fabricated
evidence, and licence or confidentiality violations. If your case is legitimate (an authorised
pentest, a CTF, a fixture with synthetic data), say so plainly and it proceeds. It takes reframing
at face value.

**You want your own house rules permanently.** Do not edit the installed skill; it gets replaced on
update. Use overrides instead:

```bash
mkdir -p ~/.config/ilana/overrides/gates
cat > ~/.config/ilana/overrides/gates/G4.append.md <<'RULES'
## House rules
- All SQL goes through the query builder. No string concatenation, ever.
- Every public function documents its error conditions.
RULES
```

These are read after the core file and survive every update. `ilana doctor` lists which are active.

---

## 8. Working as a team

Pin the process definition to a commit so everyone runs the same one:

```bash
git submodule add https://github.com/Ferousco-dev/ilana.git .ilana-src
mkdir -p .claude/skills && ln -s ../../.ilana-src/skill .claude/skills/ilana
```

Then put the project's posture in your repository's `AGENTS.md` so every session starts the same:

```markdown
## Process

This project follows Ìlànà. Rigour 3. Hybrid style. Ledger in `.ilana/`.
Definition: `.ilana-src/skill/SKILL.md`.

No merge to main without G4. No release without a rehearsed rollback.
```

Commit `.ilana/` too. Gate records in a pull request are how a reviewer sees that the process
actually ran.

---

## 9. Troubleshooting

**"My agent does not know what ilana is."**

```bash
ilana doctor
```

Look at the `hosts:` block. It shows every agent directory it knows and whether Ìlànà is `linked`,
`copied` or `absent`. If yours says `absent`, find your agent in `adapters/` and follow that guide.
Then start a **new** session; most agents load skills at session start.

**"`ilana: command not found`."** The CLI is not on your PATH. Either use the full path
`~/.ilana-src/bin/ilana`, or:

```bash
mkdir -p ~/.local/bin && ln -sf ~/.ilana-src/bin/ilana ~/.local/bin/ilana
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && exec zsh
```

**"It skipped the fork question."** It should never do that. If your request already clearly named
a mode ("write me a test plan") it will state its reading and let you correct it. If it genuinely
skipped, say `restart the boot sequence`.

**"It is not writing files."** Either your agent lacks filesystem access, or you are in a read-only
mode. Ìlànà will say `MEMO mode` when it cannot write, and emit artifacts as code blocks with their
intended paths instead.

**"The instruments do not run."** They need Python 3. `ilana doctor` reports whether it found it.
Without Python, every instrument has a documented manual procedure in its `.md` file.

**"I want to start over."**

```bash
rm -rf .ilana        # only if you genuinely want to discard the process history
```

---

## 10. What good use looks like

After a week you should be doing roughly this:

- **Most days:** TASK mode, one artifact. A test plan, a code review, a rollback plan, an activity
  diagram.
- **Starting something new:** FLEET at rigour 2 or 3.
- **Inheriting something:** AUDIT first, always. It takes half an hour and it changes what you do
  next.
- **When something feels wrong about how the team works:** DOCTOR, and actually do the one thing it
  prescribes.
- **Before every release:** `gate this before I ship`.

You are not meant to run the full fleet every day. You are meant to have a process available the
moment the work deserves one.
