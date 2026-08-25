# INSTRUMENTS

Article 10: no superlative without a number. These are the numbers.

| Instrument | Answers | File |
| --- | --- | --- |
| Metrics engine | what are the product, process and project numbers | `metrics.md`, `scripts/metrics.py` |
| Quality scorecard | are the seven attributes actually met | `quality-attributes.md` |
| CMMI probe | what maturity level does the evidence support | `cmmi-probe.md` |
| Gate checker | does the current state satisfy this gate | `scripts/gate_check.py` |
| Traceability checker | which requirements have no design, code or test | `scripts/traceability.py` |
| Ledger tool | read, append to and validate `.ilana/` | `scripts/ledger.py` |

## Rules of measurement

1. **Every value has a source.** A path, a command, or a document. No source means no number.
2. **State the unit.** "2.4" is meaningless. "2.4 defects per KLOC" is a measurement.
3. **Two points is not a trend.** Say "changed from X to Y", not "improving".
4. **Estimates are labelled.** Presenting an estimate as a measurement violates Article 2.
5. **Absence is a finding.** "No process metrics exist" is often the most important sentence in a
   report.
6. **Every metric names the decision it informs.** A metric informing no decision is deleted, and
   collecting it stops.
7. **Never attach a metric to individual performance evaluation.** Do it once with defect counts
   and defect reporting stops being honest, which costs more than any performance question is
   worth.

## Running them

The scripts are dependency-free Python 3 and read only the repository and `.ilana/`.

```bash
python3 skill/instruments/scripts/metrics.py --repo . --out .ilana/metrics.csv
python3 skill/instruments/scripts/traceability.py --file .ilana/traceability.csv
python3 skill/instruments/scripts/gate_check.py --gate G5 --rigour 3
python3 skill/instruments/scripts/ledger.py init --project "library-system" --rigour 3
```

If Python is unavailable, every instrument has a stated manual procedure in its `.md` file. Ìlànà
never requires a runtime it cannot degrade without.
