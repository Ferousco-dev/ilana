# FAQ

**Can I just point my agent at the repo and say "install this"?**

Yes. That is the intended path:

```
install this skill: https://github.com/Ferousco-dev/ilana
```

There is an [`AGENTS.md`](../AGENTS.md) at the repository root written specifically for an agent
that has been handed the URL. It carries the exact commands, the fallback if symlinks are not
possible, the per-host paths, and a list of things not to do (do not vendor the skill loose into
the user's source tree; do not touch any `.ilana/` directory found).

If your agent cannot run shell commands it will say so rather than improvise, and point you at
[`adapters/templates/ILANA.md`](../adapters/templates/ILANA.md), the single-file version you can
paste into a system prompt.

---

**`ilana: command not found` right after installing.**

`ilana install` links the command into `~/.local/bin`, which is not on every system's PATH. The
installer detects this and prints the exact line for your shell. `ilana doctor` reports it too,
under `cli on PATH:`.

The skill itself is unaffected: it and the slash commands work without the CLI on PATH. Only
`ilana update`, `ilana doctor` and the shell shortcuts need the command, and those all work by full
path (`~/.ilana-src/bin/ilana doctor`).

Set `ILANA_BIN` to install the command somewhere already on your PATH, or pass `--no-cli` to skip
linking it at all.

---

**How do I know it installed correctly?**

```bash
ilana doctor
```

Look at the `hosts:` block. Every agent directory it knows about is listed as `linked`, `copied` or
`absent`. Then start a **new** session, because most agents load skills at session start, and say
`use ilana`. If it answers with the fork question, it is working.

---

**Is this only for students?**

No. It came out of a university course, and the course happens to cover the things working
engineers most often skip: requirements that can be tested, reviews before testing, metrics that
inform a decision, and a rollback that has actually been rehearsed. Students get a syllabus map;
engineers get gates.

---

**Will it slow me down?**

At rigour 1 and 2, barely. Gates collapse to a few sentences and most ceremony disappears.

At rigour 3 and above, yes, at the front. The trade is deliberate: time spent at G1 and G2 buys
back more time than it costs, because a requirements defect found in production costs many times
what it costs in a review. If your project genuinely does not need that trade, set rigour lower.
That is what the dial is for.

---

**Does it work with anything other than Claude Code?**

Yes. See `adapters/`. Codex, Cursor, Windsurf, Gemini CLI, Copilot, Continue, Aider, OpenCode, and
a generic fallback for anything else. The payload is one directory; the adapters just point at it
differently.

For an agent with no skill mechanism at all, `adapters/templates/ILANA.md` is a self-contained
single file you can paste anywhere.

---

**Does it need sub-agents?**

No. Fleet mode has two runtimes. With sub-agents it spawns specialists in parallel. Without them it
rotates the thirteen agent cards sequentially in one context. The artifacts and the gates are
identical; only the wall-clock differs.

---

**What if I disagree with a gate?**

Override it. At rigour 1 to 4, Ìlànà states which criteria are unmet, states the specific
consequence for your project, records your reason, and proceeds without arguing a second time.

At rigour 5 there are no overrides. Ìlànà says so and stops rather than pretending the gate was met.

---

**Can I change the process?**

Yes, in three ways.

- **Per project:** set the rigour and the process style at intake.
- **Permanently, locally:** put house rules in `~/.config/ilana/overrides/`. They survive updates.
- **For everyone:** open a pull request. See `CONTRIBUTING.md`.

---

**Why is it called Ìlànà?**

Ìlànà is Yoruba for *process, method, procedure, the disciplined way a thing is done*. The course
it came from is taught at Obafemi Awolowo University in Ile-Ife, which is Yoruba land. The name is
the subject.

---

**Does it phone home?**

No. Ìlànà never touches the network except when you run `ilana check` or `ilana update`. The boot
sequence reads a local timestamp file and, at most, prints one line suggesting you run an update
when convenient.

---

**What does it refuse to do?**

Three things, and nothing else:

1. Code whose purpose is to defeat a control: hidden credentials, backdoors, disabled audit
   logging, suppressed test results.
2. Fabricated evidence: claiming a test passed without having seen it pass.
3. Ownership violations: code whose licence forbids the use, a previous employer's proprietary
   source, real personal data in test fixtures.

It does **not** refuse security tooling for authorised work, aggressive refactoring, deleting your
own code, shipping fast at low rigour, or anything that merely sounds risky. Over-refusing is its
own failure, because it teaches people to ignore refusals when they matter.

---

**It asked me a question and I do not know the answer.**

Say "assume". Ìlànà will state its assumptions explicitly, log them as decision records, and
proceed. An assumption written down is engineering; an assumption unspoken is what kills projects.

---

**Can I use only part of it?**

Yes. `TASK` mode uses exactly one phase and one agent. Most days that is all you want: write the
test plan, review this diff, draw the activity diagram, check the branching strategy. Task mode is
first class, not a degraded fleet.

---

**How do I keep it updated?**

If you installed with `--link`, `git pull` in `~/.ilana-src` updates every agent on the machine at
once. Or `ilana update`. Or `ilana autoupdate --enable` for a weekly background check.

---

**What is the difference between this and a linter?**

A linter checks the code you wrote. Ìlànà checks whether you should have written it, whether anyone
asked for it, whether it can be tested, whether anyone reviewed it, whether you can get back if it
breaks, and whether the process that produced it is improving.

They are complementary. Ìlànà will happily insist you install a linter, because G4 wants the
standard machine-enforced.

---

**Is the course material reproduced verbatim?**

The phase `reference.md` files condense and restate the course content, with the definitions,
tables and worked examples preserved because those are the substance. Everything else in Ìlànà, the
gates, the agents, the protocols, the instruments and the refusal system, is original work built on
top of it. The complete original deck is in `source/` for anyone who wants the primary text.
