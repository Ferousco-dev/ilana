# PHASE 04 CHECKLIST

## Standard
- [ ] `docs/coding-standard.md` exists for this project
- [ ] Indentation, naming, error-return and exception conventions are stated
- [ ] Rules on global data are stated
- [ ] Deviations from the course guidelines are recorded with reasons
- [ ] The standard is machine-enforced where possible (formatter and linter in CI)

## Code
- [ ] Every module traces to a `DES` element
- [ ] No `goto` or equivalent unstructured control flow
- [ ] Function length and complexity within the project's stated limits
- [ ] Comments explain why, not what
- [ ] No commented-out dead code
- [ ] No unreferenced modules or functions
- [ ] Consistent naming throughout

## Errors
- [ ] Every failure path is handled or deliberately propagated
- [ ] No silently swallowed exceptions
- [ ] Error messages are meaningful and match the error catalogue from phase 03
- [ ] Errors carry enough context to diagnose from a log alone

## Security
- [ ] No hard-coded credentials, keys, tokens or connection strings
- [ ] Untrusted input is validated at the trust boundary named in the design
- [ ] No secrets in commit history, not only in the working tree
- [ ] Output encoding appropriate to the sink (HTML, SQL, shell, log)

## Dependencies
- [ ] Every dependency is recorded with its version and licence
- [ ] Licences are compatible with the project's own licence and intended use
- [ ] No copied source whose licence forbids this use
- [ ] Dependency count is justified: each one earns its place

## Review
- [ ] Peer review completed for every change (RIGOUR 3+)
- [ ] Review comments resolved, not just marked resolved
- [ ] Reviewer is not the author
