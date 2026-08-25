# G4 - CONSTRUCTION COMPLETE

Owner: `constructor`. Closes: phase 04. Opens: phase 05 Verification.

## Criteria

| # | Criterion | Rigour | Evidence |
|---|---|---|---|
| 1 | A written coding standard exists for this project | R1+ | `docs/coding-standard.md` or a linter config |
| 2 | The standard is machine-enforced where possible | R2+ | linter and formatter in CI |
| 3 | Every module traces to a `DES` element | R1+ | traceability matrix, module column filled |
| 4 | No commented-out dead code, no unreferenced modules | R1+ | grep and dependency scan |
| 5 | Error handling exists and error messages are meaningful | R2+ | error path review |
| 6 | Internal documentation present at roughly one comment per three source lines in non-obvious code | R2+ | sampled |
| 7 | No hard-coded credentials, keys, tokens or connection strings | R2+ | secret scan output |
| 8 | Function length and complexity within the standard's limits | R3+ | complexity report |
| 9 | Peer code review completed for every change | R3+ | PR approvals, `CODEOWNERS` |
| 10 | Third-party dependency licences recorded and compatible | R4+ | `docs/dependencies.md` |
| 11 | Static analysis and security scanning clean or triaged | R4+ | scan report |
| 12 | Formal inspection of safety-related modules | R5 | inspection record |

## Coding guidelines from the source material

These are the specific guidelines SEN102/212 teaches. Treat them as defaults that a project's
own standard may override in writing, not as universal law.

- Line length at or below 80 characters.
- Spacing around operators and after commas for readability.
- At least one comment per three source lines on average.
- Function length ordinarily under about 10 source lines, because long functions do too many
  things and carry a disproportionate share of the defects.
- No `goto`; structured or modular programming only.
- Consistent naming convention for globals, locals and constants.
- Consistent error return convention and exception handling across the organisation.
- Rules limiting what may be declared global.

If a project deviates (many languages and codebases reasonably do on line length and function
length), the deviation is written into `docs/coding-standard.md` with a reason. Undocumented
deviation is the failure, not deviation itself.

## The secret scan

Non-negotiable from R2 up:

```bash
grep -rinE '(password|passwd|secret|api[_-]?key|token|bearer|private[_-]?key)\s*[:=]\s*["'\''][^"'\'']{6,}' \
  --include='*.*' . | grep -v -E '(test|spec|example|sample|\.md:)'
```

Any hit is a gate failure until it is moved to configuration or a secret store.
