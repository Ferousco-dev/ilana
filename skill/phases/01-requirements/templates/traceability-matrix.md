# Traceability Matrix

Machine form lives at `.ilana/traceability.csv`. This file explains it.

## Columns

| Column | Meaning | Filled by |
| --- | --- | --- |
| `req_id` | REQ / NFR / DOM identifier | `analyst` |
| `requirement` | one-line statement | `analyst` |
| `type` | functional / non-functional / domain | `analyst` |
| `priority` | must / should / could / wont | `analyst` |
| `source` | who asked, when | `analyst` |
| `design_id` | DES element implementing it | `architect` |
| `module` | file or package path | `constructor` |
| `test_ids` | semicolon-separated TC list | `verifier` |
| `result` | pass / fail / not run | `verifier` |
| `status` | draft / specified / designed / implemented / verified / withdrawn | current owner |

## The four queries this table has to answer

Run these at every gate. They are the whole reason the matrix exists.

1. **Which requirements have no design?** -> the system will not do what was asked.
2. **Which design elements have no requirement?** -> you are building unrequested work
   (Article 3).
3. **Which requirements have no test?** -> you cannot claim verification.
4. **Which tests trace to nothing?** -> either an undocumented requirement or a test that is
   protecting nothing.

```bash
# requirements with no test case
awk -F, 'NR>1 && $8=="" {print $1": "$2}' .ilana/traceability.csv

# requirements not yet verified
awk -F, 'NR>1 && $10!="verified" {print $1" ["$10"]"}' .ilana/traceability.csv
```

## Withdrawal

A requirement is never deleted. It is marked `withdrawn` with the change request that
withdrew it:

```csv
REQ-014,Bulk import from spreadsheet,functional,could,BA interview 2026-08-19,,,,,withdrawn by CR-003
```

Deleting rows destroys the ability to answer "why did we stop doing that", which is the
question someone always asks eighteen months later.
