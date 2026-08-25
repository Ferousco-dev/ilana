#!/usr/bin/env python3
"""Ilana metrics engine.

Computes the three metric categories from a repository and an .ilana ledger.
No third-party dependencies. Python 3.8+.

Usage:
    python3 metrics.py --repo . [--out .ilana/metrics.csv] [--json]

Every value it emits carries a source. Values it cannot compute are reported as
UNVERIFIED rather than guessed, per Constitution Article 2.
"""

import argparse
import csv
import json
import os
import re
import subprocess
import sys
from datetime import date

SOURCE_EXT = {
    ".py", ".js", ".ts", ".tsx", ".jsx", ".java", ".kt", ".go", ".rs", ".rb",
    ".c", ".h", ".cc", ".cpp", ".hpp", ".cs", ".swift", ".php", ".scala",
    ".dart", ".m", ".sh", ".sql",
}
SKIP_DIRS = {
    ".git", "node_modules", "vendor", "dist", "build", "target", ".venv",
    "venv", "__pycache__", ".tox", ".mypy_cache", ".next", "coverage",
    ".gradle", ".idea", ".ilana",
}
TEST_HINT = re.compile(r"(^|[/_.-])(tests?|spec|__tests__)([/_.-]|$)", re.I)
COMMENT_PREFIX = ("#", "//", "/*", "*", "*/", "--", '"""', "'''")


def walk_sources(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for name in filenames:
            if os.path.splitext(name)[1] in SOURCE_EXT:
                yield os.path.join(dirpath, name)


def count_lines(path):
    """Return (total, code, comment, blank)."""
    total = code = comment = blank = 0
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as handle:
            for raw in handle:
                total += 1
                line = raw.strip()
                if not line:
                    blank += 1
                elif line.startswith(COMMENT_PREFIX):
                    comment += 1
                else:
                    code += 1
    except OSError:
        pass
    return total, code, comment, blank


def size_metrics(root):
    files = list(walk_sources(root))
    prod = [f for f in files if not TEST_HINT.search(f)]
    tests = [f for f in files if TEST_HINT.search(f)]
    totals = {"code": 0, "comment": 0, "blank": 0, "total": 0}
    for path in prod:
        t, c, cm, b = count_lines(path)
        totals["total"] += t
        totals["code"] += c
        totals["comment"] += cm
        totals["blank"] += b
    test_code = sum(count_lines(f)[1] for f in tests)
    return {
        "source_files": len(prod),
        "test_files": len(tests),
        "loc_total": totals["total"],
        "loc_code": totals["code"],
        "loc_comment": totals["comment"],
        "loc_blank": totals["blank"],
        "kloc": round(totals["code"] / 1000.0, 3) if totals["code"] else 0.0,
        "test_loc": test_code,
        "comment_ratio": (
            round(totals["comment"] / totals["code"], 3) if totals["code"] else None
        ),
        "test_to_source_ratio": (
            round(test_code / totals["code"], 3) if totals["code"] else None
        ),
    }


def parse_defects(ledger_dir):
    """Read .ilana/defects.md. Counts DEF-### occurrences and their severities."""
    path = os.path.join(ledger_dir, "defects.md")
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        text = handle.read()
    ids = set(re.findall(r"\bDEF-(\d+)\b", text))
    severities = {}
    for match in re.finditer(
        r"Severity:\s*(critical|high|medium|low)", text, re.I
    ):
        key = match.group(1).lower()
        severities[key] = severities.get(key, 0) + 1
    statuses = {}
    for match in re.finditer(
        r"Status:\s*(New|Assigned|Open|Fixed|Retest|Verified|Closed|Reopened|Deferred|Rejected)",
        text,
        re.I,
    ):
        key = match.group(1).lower()
        statuses[key] = statuses.get(key, 0) + 1
    return {"count": len(ids), "severity": severities, "status": statuses}


def git(root, *args):
    try:
        out = subprocess.run(
            ["git", "-C", root, *args],
            capture_output=True, text=True, timeout=20, check=False,
        )
        return out.stdout.strip() if out.returncode == 0 else None
    except (OSError, subprocess.SubprocessError):
        return None


def process_metrics(root):
    metrics = {}
    commits = git(root, "rev-list", "--count", "HEAD")
    metrics["commits"] = int(commits) if commits and commits.isdigit() else None
    authors = git(root, "shortlog", "-sn", "--all", "--no-merges")
    metrics["contributors"] = len(authors.splitlines()) if authors else None
    tags = git(root, "tag")
    metrics["tags"] = len(tags.splitlines()) if tags else 0
    subjects = git(root, "log", "--format=%s", "-500")
    if subjects:
        lines = subjects.splitlines()
        conventional = sum(
            1 for line in lines
            if re.match(r"^(feat|fix|docs|chore|refactor|test|perf|build|ci)(\(.+\))?!?:", line)
        )
        traced = sum(1 for line in lines if re.search(r"\b(REQ|CR|DEF|NFR|DOM)-\d+", line))
        metrics["commit_sample"] = len(lines)
        metrics["conventional_commit_ratio"] = round(conventional / len(lines), 3)
        metrics["traced_commit_ratio"] = round(traced / len(lines), 3)
    return metrics


def traceability_metrics(ledger_dir):
    path = os.path.join(ledger_dir, "traceability.csv")
    if not os.path.exists(path):
        return None
    rows = []
    with open(path, newline="", encoding="utf-8", errors="replace") as handle:
        for row in csv.DictReader(handle):
            rows.append(row)
    if not rows:
        return {"requirements": 0}
    def filled(row, *keys):
        return any((row.get(k) or "").strip() for k in keys)
    total = len(rows)
    with_design = sum(1 for r in rows if filled(r, "design_id"))
    with_tests = sum(1 for r in rows if filled(r, "test_ids"))
    verified = sum(
        1 for r in rows if (r.get("status") or "").strip().lower() == "verified"
    )
    return {
        "requirements": total,
        "with_design": with_design,
        "with_tests": with_tests,
        "verified": verified,
        "design_coverage": round(with_design / total, 3),
        "test_coverage": round(with_tests / total, 3),
        "verified_ratio": round(verified / total, 3),
    }


def defect_density(size, defects):
    if not defects or not size.get("kloc"):
        return None
    return round(defects["count"] / size["kloc"], 3)


def build_report(root, ledger_dir):
    size = size_metrics(root)
    defects = parse_defects(ledger_dir)
    process = process_metrics(root)
    trace = traceability_metrics(ledger_dir)
    return {
        "generated": date.today().isoformat(),
        "repo": os.path.abspath(root),
        "product": {
            **size,
            "defect_density_per_kloc": defect_density(size, defects),
            "defects": defects,
        },
        "process": process,
        "project": {
            "cost_variance": "UNVERIFIED: supply planned and actual cost",
            "schedule_adherence": "UNVERIFIED: supply planned and actual dates",
        },
        "traceability": trace,
    }


def unverified_notes(report):
    notes = []
    if report["product"]["defects"] is None:
        notes.append("defect data: no .ilana/defects.md; defect density UNVERIFIED")
    if report["traceability"] is None:
        notes.append("traceability: no .ilana/traceability.csv; requirement coverage UNVERIFIED")
    if report["process"].get("commits") is None:
        notes.append("process: not a git repository or git unavailable")
    if report["product"]["test_files"] == 0:
        notes.append("verification: no test files detected; this is a G5 finding")
    notes.append("project metrics require planned versus actual cost and schedule input")
    return notes


def flatten(report):
    rows = []
    stamp = report["generated"]

    def add(metric, category, value, unit, source):
        if value is None:
            return
        rows.append([stamp, metric, category, value, unit, source])

    p = report["product"]
    add("loc_code", "product", p["loc_code"], "lines", "source scan")
    add("kloc", "product", p["kloc"], "kloc", "source scan")
    add("source_files", "product", p["source_files"], "files", "source scan")
    add("test_files", "product", p["test_files"], "files", "source scan")
    add("comment_ratio", "product", p["comment_ratio"], "ratio", "source scan")
    add("test_to_source_ratio", "product", p["test_to_source_ratio"], "ratio", "source scan")
    add("defect_density", "product", p["defect_density_per_kloc"], "defects_per_kloc",
        ".ilana/defects.md + source scan")
    if p["defects"]:
        add("defect_count", "product", p["defects"]["count"], "defects", ".ilana/defects.md")

    pr = report["process"]
    add("commits", "process", pr.get("commits"), "commits", "git rev-list")
    add("contributors", "process", pr.get("contributors"), "people", "git shortlog")
    add("tags", "process", pr.get("tags"), "tags", "git tag")
    add("conventional_commit_ratio", "process", pr.get("conventional_commit_ratio"),
        "ratio", "git log sample")
    add("traced_commit_ratio", "process", pr.get("traced_commit_ratio"),
        "ratio", "git log sample")

    t = report.get("traceability")
    if t and t.get("requirements"):
        add("requirements", "project", t["requirements"], "count", ".ilana/traceability.csv")
        add("design_coverage", "project", t["design_coverage"], "ratio",
            ".ilana/traceability.csv")
        add("requirement_test_coverage", "project", t["test_coverage"], "ratio",
            ".ilana/traceability.csv")
        add("verified_ratio", "project", t["verified_ratio"], "ratio",
            ".ilana/traceability.csv")
    return rows


def main():
    parser = argparse.ArgumentParser(description="Ilana metrics engine")
    parser.add_argument("--repo", default=".", help="repository root")
    parser.add_argument("--ledger", default=None, help="ledger directory (default <repo>/.ilana)")
    parser.add_argument("--out", default=None, help="append results to this CSV")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of a table")
    args = parser.parse_args()

    root = args.repo
    ledger_dir = args.ledger or os.path.join(root, ".ilana")
    report = build_report(root, ledger_dir)
    notes = unverified_notes(report)

    if args.json:
        report["unverified"] = notes
        print(json.dumps(report, indent=2))
    else:
        print("ILANA METRICS  " + report["generated"])
        print("repo: " + report["repo"])
        print()
        rows = flatten(report)
        if rows:
            width = max(len(r[1]) for r in rows)
            current = None
            for stamp, metric, category, value, unit, source in rows:
                if category != current:
                    print("[" + category + "]")
                    current = category
                print("  {0:<{1}}  {2}  {3}   ({4})".format(
                    metric, width, value, unit, source))
        print()
        print("[UNVERIFIED]")
        for note in notes:
            print("  - " + note)

    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        exists = os.path.exists(args.out)
        with open(args.out, "a", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            if not exists:
                writer.writerow(["date", "metric", "category", "value", "unit", "source"])
            for row in flatten(report):
                writer.writerow(row)
        print("\nappended to " + args.out, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
