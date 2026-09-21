# MODE: MAINTAIN

The mode for a coding agent working inside an EXISTING repository: adding a feature, finishing a
milestone, fixing a defect, or resuming after an interruption.

`FLEET` assumes you are designing a system. `MAINTAIN` assumes the system already exists, the
repository already knows most of what a requirements phase would ask, and the risk is breaking
or contradicting what is there. The goal is:

> The minimum process documentation the risk level demands, and the maximum verified repository
> evidence.

Every artifact in this mode is either a fact captured by an instrument or a decision a human
would otherwise have to guess. Nothing is written twice.

---

## When it applies

Choose `MAINTAIN` when all of these hold:

- the working directory is a git repository with history;
- the user asks to add, change, fix, continue or resume, not to build from scratch or rescue;
- the change fits inside one milestone or one change request.

Use `FLEET` for a new system, `AUDIT` to assess a repository without changing it.

---

## Intake (three questions, only if `.ilana/policy.json` is absent)

Ask once, in one batch. "Assume defaults" is legal and must print what was assumed.

1. **Ceremony:** `light`, `standard` or `regulated`? Default `standard`. See `protocols/ceremony.md`.
2. **Stop boundary:** what must NOT be started (the next roadmap item, a named refactor)?
3. **Commit policy:** Conventional Commits and no AI or co-author attribution? Default yes to both.

Record the answers with `evidence.py policy --ceremony standard --stop "v0.24"`.

---

## Procedure

Announce each step in one line. Do not narrate.

1. **Orient.** `repo_map.py map`, then read `.ilana/handoff.json` and `.ilana/milestone-state.md`
   if they exist. Do not read the whole `.ilana/` directory. Resuming from the handoff is enough.
2. **Reality check (Article 17).** Compare the prompt, roadmap and earlier reports with the
   repository: `git status`, `git log`, the code, migrations and tests. Where they disagree,
   the repository wins. Record each disagreement with
   `evidence.py handoff --add disagreement="..."` and continue from the truth.
3. **Guard scope.** `repo_map.py snapshot --allow "<globs for this task>"`. From now on, files that
   were already dirty belong to someone else and stay byte-identical. See `protocols/scope-guard.md`.
4. **Derive the checklist.** `privacy_scan.py scan` produces the security and privacy checklist for
   what this repository actually handles. Carry the relevant rows into the requirements table.
5. **Specify at the ceremony level.** `light`: one sentence of intent in the handoff.
   `standard`: a requirements-to-tests table (see below). `regulated`: a full SRS per `FLEET`.
6. **Implement.** Smallest change that satisfies the specification. Read only what the change
   needs. No opportunistic refactors. A bug outside scope is reported, not fixed, unless the
   milestone cannot be completed without it (then a `CR` records why).
7. **Verify with evidence.** Run every check through `evidence.py run --label NAME -- CMD`.
   Never paste results into prose; refer to the `EV-###` id.
8. **Re-check scope and privacy.** `repo_map.py guard` must exit 0. Marker tests use
   `privacy_scan.py check`.
9. **Update Ilana.** `evidence.py handoff` with completed, verified, remaining and limitation
   items. Add a `DEC` only for a real decision. Update the architecture facts that changed.
10. **Commit with hygiene.** `evidence.py commit-check` on the message. Stage only intended files.
11. **Report and stop.** `evidence.py report`. Do not begin anything in the stop boundary.

---

## The compact artifact set (standard ceremony)

| Artifact | Owns | Written by |
| --- | --- | --- |
| `.ilana/handoff.json` | current milestone state, single source | `evidence.py handoff` |
| `.ilana/milestone-state.md` | rendered view of the handoff | generated |
| `.ilana/traceability.csv` | requirements (statement) mapped to tests | analyst role |
| `.ilana/decisions.md` | real decisions and why | any role, sparingly |
| `.ilana/evidence.jsonl` | every command run, with head commit and exit code | `evidence.py run` |
| `.ilana/repo-map.md`, `privacy-checklist.md` | generated facts | instruments |

The requirements-to-tests table is the requirements document. Its rows carry the statement, the
test ids and the evidence id. A separate SRS at `standard` ceremony is duplication.

The final validation report is `evidence.py report`. It is rendered from evidence, not written.

---

## Completion criteria

A milestone is COMPLETE only when: the implementation is done; required tests pass with evidence
ids; `repo_map.py guard` exits 0; the privacy checklist rows relevant to the change are proven;
Ilana is updated; the commit message passed `commit-check`; and the stop boundary was respected.
The completion report states `Ilana updated: YES` and what knowledge changed.

If any item is unmet, say NOT COMPLETE and name it. Article 2 applies.

---

## Token discipline

- Read the handoff and the map, not the whole ledger.
- Reference evidence by id. Never restate a fact that an instrument already recorded.
- One line per ledger event. No summary of a summary.
- Do not spawn sub-agents for work a few commands can do.
- Update the affected row or section, never rewrite a file.
