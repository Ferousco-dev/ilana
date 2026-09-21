# PROTOCOL: SCOPE GUARD

Keeps work inside its intended change set, protects other people's uncommitted work, enforces the
stop boundary, and enforces commit hygiene.

## Why

In an existing repository the working tree often holds changes that are not yours: a user's
half-finished edit, a generated file, another agent's work. Staging or modifying them silently is
a scope violation. Starting the next roadmap item because it looks easy is a boundary violation.
Both are process failures, not style issues.

## Working-tree scope guard

Before changing anything:

```
python3 repo_map.py snapshot --allow "internal/observability/**" "cmd/**" "docs/**"
```

This records every dirty path with a content hash (the protected set) and the allowed globs. The
glob `.ilana/**` is always allowed.

During and after the work:

```
python3 repo_map.py guard
```

| Result | Meaning | Action |
| --- | --- | --- |
| `VIOLATIONS` | a pre-existing dirty file was modified or removed | stop, restore it, report |
| `OUT-OF-SCOPE` | a new dirty path matches no allowed glob | justify it (add a glob and a `DEC`) or revert it |
| in scope | new path inside an allowed glob | expected |

`guard` exits 0 only when nothing needs a decision. Run it before every commit.

When staging, list files explicitly. Never `git add -A` in a tree that had pre-existing changes.

## Stop boundary

The stop boundary names what must not be started, for example the next roadmap version.

- Set it in intake: `evidence.py policy --stop "v0.24" "TLS work"`.
- It is copied into the handoff and every rendered state document.
- When finishing, report completion and stop. Offering the next step is allowed; starting it is
  not. Only the user starting a new task lifts the boundary.
- If the current task cannot be completed without touching something in the boundary, that is a
  blocker: report it and ask.

## Commit hygiene

Policy lives in `.ilana/policy.json` (`commit.conventional`, `commit.forbid_ai_attribution`,
`commit.header_max`).

```
python3 evidence.py commit-check .git/COMMIT_EDITMSG     # or pipe a message on stdin
python3 evidence.py hook                                 # install a commit-msg hook
```

Checks: Conventional Commit header (`type(scope): subject`), header length, and the absence of
AI or automated-tool attribution (co-author trailers, "Generated with" lines, tool names).

Rules that do not depend on the policy file:

- Never change the configured git identity.
- Never rewrite, squash or amend history the user did not ask to rewrite.
- Read the full commit message before committing and remove any attribution the host tool
  injects by default. A user's explicit instruction overrides tool defaults.
- Do not push unless asked.

## Security and privacy checklist

`privacy_scan.py scan` derives the checklist from the repository (credentials, tokens, personal
identifiers, and domain classes such as mail content, addresses, delivery diagnostics, signing
material, outbound destinations) and lists log or print lines that mention sensitive identifiers.
Each relevant row becomes a requirement with a marker test:

```
python3 privacy_scan.py check --markers "$API_KEY,PRIVATE-BODY" captured.log metrics.txt
```

A row is proven only by an evidence id from such a check, never by assertion.
