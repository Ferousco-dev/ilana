# PROTOCOL: CHECKPOINT

How a piece of work is recorded so that another agent, or the same agent after an interruption,
can resume without rereading dozens of documents. It also defines automatic evidence capture and
the reality check.

## The handoff file

`.ilana/handoff.json` is the single machine-readable state of the current milestone. Create and
update it only through the instrument:

```
python3 evidence.py handoff --set milestone="v0.23" --set step="verification" \
  --add completed="structured logging" --add remaining="Compose e2e" \
  --add limitation="metrics endpoint unauthenticated" --set next="run compose checks"
```

It records: milestone, step, completed, verified, remaining, limitations, decisions, repository
disagreements, next action, base commit, head, branch, dirty path count, ceremony, stop boundary,
and the latest evidence per label. Head, branch, dirty count, ceremony, stop boundary and evidence
are filled automatically.

`.ilana/milestone-state.md` is rendered from the JSON on every update. Never edit it by hand.

## Resuming after interruption

1. Read `.ilana/handoff.json` (or `milestone-state.md`). Read nothing else yet.
2. Run `repo_map.py map --stdout` and compare `head` and `dirty_paths` with the handoff.
3. If they differ, the repository moved. Reality check (below), then update the handoff.
4. Execute the `next` action. Do not restart the milestone.
5. If `repo_map.py guard` reports a violation, stop and report it before doing anything else.

## Automatic evidence capture

Run every validation through the instrument so the record cannot drift from the run:

```
python3 evidence.py run --label tests -- go test -count=1 ./...
```

Each run appends one line to `.ilana/evidence.jsonl` with an `EV-###` id, timestamp, label,
command, exit code, duration, head commit, dirty flag and the last three output lines with
secret-looking values redacted. Full output is never stored.

Reference evidence by id anywhere a result would be quoted. `evidence.py report` renders the final
validation report from the latest run per label. If a label's latest run failed, the report
fails, and so does completion.

Migration state, code locations and commit hashes come from `repo_map.py map` and the evidence
record's `head`. Do not retype them.

## The reality check

Article 17: repository evidence outranks assertion.

Prompts, roadmaps, earlier agent summaries and even the ledger can be stale. Before acting on
any claim about the repository, verify it against the repository:

| Claim | Verify with |
| --- | --- |
| "the tree is clean" | `git status --porcelain` |
| "milestone N is complete" | the code, migrations, tests, then the commit log |
| "the branch is at X" | `git rev-parse`, `git log` |
| "tests pass" | a new `evidence.py run`, not an old report |
| "no code exists for Y" | search the tree |

When a claim and the repository disagree: state both, continue from the repository, and record
`--add disagreement="claim X; repository shows Y"`. Do not argue with the user about it and do
not silently proceed on the claim.

## Ledger discipline

One line per event: what happened, ids affected, evidence ids. A ledger line that restates a
fact owned by another artifact is padding. See `protocols/ceremony.md` for ownership.
