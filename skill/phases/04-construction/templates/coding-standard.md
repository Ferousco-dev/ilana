# Coding Standard: <PROJECT>

| Field | Value |
| --- | --- |
| Applies to | languages, directories |
| Enforced by | formatter, linter, CI job names |
| Owner | |
| Last reviewed | |

## 1. Layout

| Rule | This project | Course default | Reason for deviation |
| --- | --- | --- | --- |
| Indentation | | consistent, emphasising control-structure bodies, conditional bodies and new scope blocks | |
| Line length | | 80 characters | |
| Spacing around operators | | required | |
| Brace or block style | | | |
| File organisation | | | |

## 2. Naming

| Kind | Convention | Example |
| --- | --- | --- |
| Global | | |
| Local | | |
| Constant | | |
| Type | | |
| Function | | |
| File | | |
| Test | | |

## 3. Structure

| Rule | This project | Course default | Reason for deviation |
| --- | --- | --- | --- |
| Function length | | at or below about 10 source lines | |
| Cyclomatic complexity ceiling | | not specified | |
| Unstructured jumps (`goto` and equivalents) | prohibited | prohibited | |
| Nesting depth | | | |
| Module size | | | |

## 4. Global data

What may be declared global, what may not, and who approves an exception.

## 5. Errors and exceptions

| Situation | Convention |
| --- | --- |
| Recoverable failure | |
| Unrecoverable failure | |
| Error return value convention | |
| Exception types used | |
| What must never be caught | |
| Logging requirement per error | |
| Silently swallowing an error | prohibited without a written comment stating why |

## 6. Comments and documentation

- Comment the **why**, not the **what**.
- Public interfaces carry documentation comments stating inputs, outputs, errors and
  preconditions.
- Density target: <state it>. Course rule of thumb is one comment line per three source lines;
  state your project's target and the reason if it differs.
- Every `TODO` carries an owner and a ticket ID, or it is not merged.

## 7. Security rules

- No credentials, keys, tokens or connection strings in source.
- Validate untrusted input at the boundary named in the design.
- Encode output for its sink.
- Never log secrets or personal data.
- Dependencies must have a recorded licence.

## 8. Enforcement

| Rule | Automated | Tool | Blocking |
| --- | --- | --- | --- |

Rules that are not automated are enforced at review. Rules enforced neither automatically nor at
review are decoration; delete them from this document.

## 9. Deviation procedure

How to propose a change to this standard, who decides, and where the decision is recorded.
