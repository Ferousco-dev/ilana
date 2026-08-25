# CONTRIBUTING

Pull requests are welcome and wanted. This project is deliberately open: it came out of a
university course, and it gets better when people who have shipped real systems argue with it.

---

## What is most wanted

In rough order of value:

1. **New host adapters.** If your coding agent is not in `adapters/`, add it. This is the highest
   value contribution and the easiest to review.
2. **Better gate criteria.** If a gate is missing a check that has actually caught something for
   you, add it, with the rigour level at which it should apply.
3. **Anti-patterns from real projects.** Every `antipatterns.md` entry should be something you have
   watched happen. Those are the most useful pages in the whole skill.
4. **Instrument improvements.** More metrics, better detection, more languages recognised.
5. **Assessment questions.** Especially scenario questions with marking notes.
6. **Translations.** The process is not language-specific; the wording is.
7. **Worked examples.** A real run on a real project, warts included.

## What will be declined

- Adding a phase without a strong case. Eleven is already a lot, and each one costs the reader.
- Removing a gate criterion because it is inconvenient. Argue that it is *wrong*, with an example.
- Making Ìlànà less strict in general. The rigour dial exists for that; use it.
- Vendor-specific content in the core. It belongs in `adapters/` or `references/tools-map.md`.
- Content that is not traceable to the source material, an established standard, or defensible
  engineering practice. Say which, in the pull request.

---

## Getting set up

```bash
git clone https://github.com/OWNER/ilana.git
cd ilana
make check          # validate, lint, style
./bin/ilana doctor  # verify the payload
```

---

## House style

These are enforced by `make check`. A pull request that fails it will not be reviewed until it
passes.

### Prose

- **No em dashes.** Anywhere. Use commas, colons, semicolons, parentheses or a new sentence. This
  is checked mechanically.
- **Direct and concrete.** "Every closed defect names its regression test" beats "it is generally
  advisable to consider ensuring adequate test coverage".
- **Second person for instructions**, third person for descriptions.
- **No filler openers.** Not "It is important to note that". Say the thing.
- **Tables over prose** wherever the content is a comparison or a lookup.
- **Every claim is checkable.** If a page says "this is the most common failure", it should be
  traceable to the source material or to defensible practice, and the pull request should say
  which.

### Structure

- Every phase directory has exactly: `PHASE.md`, `checklist.md`, `questions.md`, `antipatterns.md`,
  `gate.md`, `reference.md`, `templates/`.
- Every agent directory has `AGENT.md` with: charter, owns, inputs, outputs, operating rules,
  never does, refusals, handoff produced, questions this agent asks.
- Gate criteria carry a rigour threshold: `R1+`, `R3+`, `R5`.
- Line length in markdown: wrap at 100. Tables and URLs may exceed it.

### Code

- **Python**: standard library only. Python 3.8 compatible. No third-party dependencies, ever.
  The instruments must run on a machine with nothing installed.
- **Shell**: POSIX `sh`, not bash. `sh -n` must pass. `shellcheck -S warning` should pass.
- Every script degrades gracefully when a tool it wants is absent, and says so.

---

## Adding a host adapter

1. Create `adapters/<agent>.md`.
2. Cover: install command, where the agent looks for instructions, a working pointer or rule file,
   whether sub-agents are available, and what degrades if they are not.
3. Add a row to `adapters/README.md`.
4. If the agent has a standard install path, add it to `host_targets()` in `bin/ilana`.
5. Test it end to end. Say in the pull request which agent and version you tested on.

---

## Adding a gate criterion

Open a pull request that answers these four questions in its description:

1. **What does this catch?** A specific class of defect, with an example.
2. **At what rigour does it apply?** Justify the threshold. A criterion that applies at R1 must be
   nearly free to satisfy.
3. **What is the evidence?** A gate passes on artifacts, paths and numbers, never on assertion.
4. **Can it be automated?** If yes, add the check to `gate_check.py`. If no, mark it `MANUAL`, and
   never let it silently pass.

---

## Adding an assessment question

- Distractors must be plausible enough that a partially-informed person would pick one.
- Map it to exactly one phase.
- Scenario questions need a marking note stating what a strong answer contains.
- Never test trivia a practitioner would look up. Test the distinctions they must hold in their
  head.

---

## Commit messages

Ìlànà holds itself to Article 3. Every commit references what it serves.

```
<type>(<scope>): <what changed, imperative, one line>

<why it changed, and what would break without it>

Refs: #issue
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `phase`, `gate`, `agent`, `adapter`.

---

## Pull request checklist

- [ ] `make check` passes
- [ ] No em dashes
- [ ] New files follow the structure rules above
- [ ] `CHANGELOG.md` updated under `[Unreleased]`
- [ ] If you touched a gate, the rationale is in the description
- [ ] If you touched an adapter, you say which agent and version you tested on
- [ ] If you added content, you say what it is traceable to

---

## Attribution

Contributors are listed in `AUTHORS.md`. Add yourself in the same pull request as your first
contribution.

By contributing you agree that your contribution is licensed under the MIT License, and that you
have the right to license it.

---

## Governance

See `GOVERNANCE.md` for how decisions are made and how disagreements are resolved. In short: the
same way Ìlànà tells you to resolve them, which is by agreeing the criteria before evaluating the
options.

## Conduct

See `CODE_OF_CONDUCT.md`.
