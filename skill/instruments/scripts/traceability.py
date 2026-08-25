#!/usr/bin/env python3
"""Ilana traceability checker.

Answers the four questions the matrix exists to answer:
  1. Which requirements have no design element?     -> the system will not do what was asked
  2. Which design elements have no requirement?     -> unrequested work (Article 3)
  3. Which requirements have no test case?          -> verification cannot be claimed
  4. Which requirements are not yet verified?       -> the honest status

Usage:
    python3 traceability.py [--file .ilana/traceability.csv] [--strict]

--strict exits non-zero when any gap exists, so it can gate a pipeline.
"""

import argparse
import csv
import os
import sys

STATUSES = ["draft", "specified", "designed", "implemented", "verified", "withdrawn"]


def load(path):
    if not os.path.exists(path):
        sys.stderr.write("no traceability matrix at " + path + "\n")
        sys.stderr.write("this absence is itself a G1 finding\n")
        return None
    with open(path, newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle))


def val(row, key):
    return (row.get(key) or "").strip()


def report(rows):
    active = [r for r in rows if val(r, "status").lower() != "withdrawn"]
    withdrawn = [r for r in rows if val(r, "status").lower() == "withdrawn"]

    no_design = [r for r in active if not val(r, "design_id")]
    no_module = [r for r in active if not val(r, "module") and val(r, "type") != "non-functional"]
    no_test = [r for r in active if not val(r, "test_ids")]
    not_verified = [r for r in active if val(r, "status").lower() != "verified"]
    bad_status = [
        r for r in rows
        if val(r, "status") and val(r, "status").lower() not in STATUSES
    ]

    by_type = {}
    for r in active:
        key = val(r, "type") or "unclassified"
        by_type[key] = by_type.get(key, 0) + 1

    return {
        "total": len(rows),
        "active": len(active),
        "withdrawn": len(withdrawn),
        "by_type": by_type,
        "no_design": no_design,
        "no_module": no_module,
        "no_test": no_test,
        "not_verified": not_verified,
        "bad_status": bad_status,
    }


def show(name, rows, limit=25):
    print("\n" + name + ": " + str(len(rows)))
    for row in rows[:limit]:
        print("  " + val(row, "req_id") + "  " + val(row, "requirement")[:70])
    if len(rows) > limit:
        print("  ... and " + str(len(rows) - limit) + " more")


def main():
    parser = argparse.ArgumentParser(description="Ilana traceability checker")
    parser.add_argument("--file", default=".ilana/traceability.csv")
    parser.add_argument("--strict", action="store_true",
                        help="exit non-zero if any gap exists")
    args = parser.parse_args()

    rows = load(args.file)
    if rows is None:
        return 2
    if not rows:
        print("matrix is empty")
        return 2 if args.strict else 0

    r = report(rows)

    print("TRACEABILITY  " + args.file)
    print("  requirements: %d active, %d withdrawn" % (r["active"], r["withdrawn"]))
    for key in sorted(r["by_type"]):
        print("    %-16s %d" % (key, r["by_type"][key]))

    print("\nCOVERAGE")
    if r["active"]:
        print("  design coverage:  %5.1f%%" % (100.0 * (r["active"] - len(r["no_design"])) / r["active"]))
        print("  test coverage:    %5.1f%%" % (100.0 * (r["active"] - len(r["no_test"])) / r["active"]))
        print("  verified:         %5.1f%%" % (100.0 * (r["active"] - len(r["not_verified"])) / r["active"]))

    gaps = 0
    if r["no_design"]:
        show("GAP 1  requirements with no design element", r["no_design"])
        gaps += 1
    if r["no_test"]:
        show("GAP 3  requirements with no test case", r["no_test"])
        gaps += 1
    if r["not_verified"]:
        show("OPEN   requirements not yet verified", r["not_verified"])
    if r["bad_status"]:
        show("ERROR  rows with an invalid status", r["bad_status"])
        gaps += 1

    print("\nNOTE  gap 2 (design elements with no requirement) cannot be computed from this")
    print("      file alone. Compare the DES ids in docs/design.md against the design_id")
    print("      column. Design that traces to no requirement is unrequested work.")

    if gaps == 0:
        print("\nno structural gaps")
    if args.strict and gaps:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
