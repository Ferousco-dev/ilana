#!/usr/bin/env python3
"""Ilana gate checker.

Runs the mechanically checkable criteria for a gate against the repository and
the .ilana ledger, at a given rigour. Criteria that require human judgement are
reported as MANUAL, never silently passed.

Usage:
    python3 gate_check.py --gate G4 --rigour 3 [--repo .] [--strict]
"""

import argparse
import os
import re
import subprocess
import sys

SKIP_DIRS = {
    ".git", "node_modules", "vendor", "dist", "build", "target", ".venv",
    "venv", "__pycache__", ".tox", ".next", "coverage", ".gradle",
}

SECRET = re.compile(
    r"(password|passwd|secret|api[_-]?key|apikey|token|bearer|private[_-]?key)"
    r"\s*[:=]\s*[\"'][^\"']{8,}[\"']", re.I)
SECRET_ALLOW = re.compile(r"(test|spec|example|sample|fixture|mock|dummy|\.md$|\.lock$)", re.I)

ADJECTIVES = re.compile(
    r"\b(fast|quick|easy|simple|user[- ]friendly|intuitive|secure|scalable|robust|"
    r"efficient|reliable|flexible|modern|seamless)\b", re.I)

TEST_DIR = re.compile(r"(^|/)(tests?|spec|__tests__)(/|$)", re.I)


def walk(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            yield os.path.join(dirpath, name)


def exists(root, *rel):
    return any(os.path.exists(os.path.join(root, r)) for r in rel)


def git_ok(root):
    return os.path.isdir(os.path.join(root, ".git"))


def git(root, *args):
    try:
        out = subprocess.run(["git", "-C", root, *args], capture_output=True,
                             text=True, timeout=20, check=False)
        return out.stdout.strip() if out.returncode == 0 else None
    except (OSError, subprocess.SubprocessError):
        return None


def scan_secrets(root):
    hits = []
    for path in walk(root):
        if SECRET_ALLOW.search(path):
            continue
        if os.path.getsize(path) > 2_000_000:
            continue
        try:
            with open(path, encoding="utf-8", errors="ignore") as handle:
                for n, line in enumerate(handle, 1):
                    if SECRET.search(line):
                        hits.append("%s:%d" % (os.path.relpath(path, root), n))
                        if len(hits) > 20:
                            return hits
        except OSError:
            continue
    return hits


def scan_adjectives(root):
    hits = []
    for rel in ("docs/srs.md", "docs/requirements.md", ".ilana/requirements.md"):
        path = os.path.join(root, rel)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8", errors="ignore") as handle:
            for n, line in enumerate(handle, 1):
                for m in ADJECTIVES.finditer(line):
                    hits.append("%s:%d  %s" % (rel, n, m.group(0)))
    return hits


def has_tests(root):
    for path in walk(root):
        rel = os.path.relpath(path, root).replace(os.sep, "/")
        if TEST_DIR.search(rel) or re.search(r"(^|/)(test_|.*_test\.|.*\.test\.|.*\.spec\.)", rel):
            return True
    return False


def has_ci(root):
    return (os.path.isdir(os.path.join(root, ".github", "workflows"))
            or exists(root, ".gitlab-ci.yml", "Jenkinsfile", ".circleci/config.yml",
                      "azure-pipelines.yml", ".drone.yml"))


def regression_in_ci(root):
    """A regression suite cannot be running if no tests exist.

    Checking only for a CI config passes this criterion on a pipeline that does
    nothing but a syntax check. A gate that passes when it should not is worse
    than no gate, because it manufactures confidence.
    """
    return has_tests(root) and has_ci(root)


def has_linter(root):
    return exists(root, ".eslintrc", ".eslintrc.json", ".eslintrc.js", "eslint.config.js",
                  ".flake8", "setup.cfg", "ruff.toml", ".ruff.toml", "pyproject.toml",
                  ".rubocop.yml", "checkstyle.xml", ".golangci.yml", "clippy.toml",
                  ".editorconfig", "Makefile")


CHECKS = {
    "G0": [
        (1, "ledger initialised", lambda r: exists(r, ".ilana/state.json")),
        (1, "MANUAL problem stated in one sentence", None),
        (1, "MANUAL stakeholders named", None),
        (3, "MANUAL domain and regulatory exposure identified", None),
    ],
    "G1": [
        (1, "requirements artifact exists",
         lambda r: exists(r, "docs/srs.md", ".ilana/requirements.md", "docs/requirements.md")),
        (1, "traceability matrix exists", lambda r: exists(r, ".ilana/traceability.csv")),
        (1, "no unmeasurable adjectives in requirements",
         lambda r: not scan_adjectives(r)),
        (1, "MANUAL every requirement is independently testable", None),
        (2, "MANUAL out of scope is written down", None),
        (3, "MANUAL every NFR carries a number and a unit", None),
        (3, "MANUAL requirements validated with a stakeholder, dated", None),
        (5, "MANUAL formal inspection with Moderator, Reader, Recorder", None),
    ],
    "G2": [
        (1, "design artifact exists",
         lambda r: exists(r, "docs/design.md", "ARCHITECTURE.md", "docs/architecture.md")),
        (1, "MANUAL every REQ maps to a DES element", None),
        (1, "MANUAL every DES maps back to a REQ", None),
        (3, "architecture decision records exist", lambda r: os.path.isdir(os.path.join(r, "docs", "adr"))),
        (3, "MANUAL every NFR has an architectural mechanism", None),
        (4, "MANUAL independent design review, named and dated", None),
    ],
    "G3": [
        (1, "interface specification exists",
         lambda r: exists(r, "docs/ui-spec.md", "docs/interface-spec.md")),
        (1, "MANUAL five UI principles assessed", None),
        (2, "error catalogue exists", lambda r: exists(r, "docs/error-catalogue.md")),
        (2, "MANUAL every destructive action has undo or confirmation", None),
        (3, "MANUAL accessibility checked", None),
    ],
    "G4": [
        (1, "coding standard or linter config present",
         lambda r: exists(r, "docs/coding-standard.md") or has_linter(r)),
        (1, "no plausible secrets in the working tree", lambda r: not scan_secrets(r)),
        (2, "CI configuration present", has_ci),
        (1, "MANUAL every module traces to a DES element", None),
        (2, "MANUAL no commented-out dead code", None),
        (3, "MANUAL peer review completed for every change", None),
        (4, "dependency register exists", lambda r: exists(r, "docs/dependencies.md")),
    ],
    "G5": [
        (1, "tests exist", has_tests),
        (1, "test plan exists", lambda r: exists(r, "docs/test-plan.md")),
        (2, "defect log exists", lambda r: exists(r, ".ilana/defects.md")),
        (1, "MANUAL every REQ and NFR maps to at least one TC", None),
        (2, "MANUAL exit criteria met or shortfall explicit", None),
        (3, "regression suite runs in CI", regression_in_ci),
        (3, "MANUAL acceptance signed by a user or client, not a developer", None),
        (5, "MANUAL no open defects of severity high or critical", None),
    ],
    "G6": [
        (1, "is a git repository", git_ok),
        (1, "working tree is clean",
         lambda r: git_ok(r) and (git(r, "status", "--porcelain") == "")),
        (1, "at least one release tag exists",
         lambda r: bool(git(r, "tag"))),
        (1, "changelog exists", lambda r: exists(r, "CHANGELOG.md")),
        (2, "rollback plan exists", lambda r: exists(r, "docs/rollback.md")),
        (2, "MANUAL rollback has been rehearsed, with a date", None),
        (2, "SCM plan exists", lambda r: exists(r, "docs/scm-plan.md")),
        (3, "CI configuration present", has_ci),
        (3, "MANUAL environments reproducible from source", None),
    ],
    "G7": [
        (2, "quality management plan exists", lambda r: exists(r, "docs/quality-plan.md")),
        (2, "review records exist", lambda r: os.path.isdir(os.path.join(r, "docs", "reviews"))),
        (3, "metrics recorded", lambda r: exists(r, ".ilana/metrics.csv")),
        (2, "MANUAL quality plan predates construction", None),
        (3, "MANUAL independent audit performed", None),
        (2, "MANUAL seven quality attributes assessed with evidence", None),
    ],
    "G8": [
        (1, "gate records exist", lambda r: os.path.isdir(os.path.join(r, ".ilana", "gates"))),
        (2, "retrospective exists", lambda r: exists(r, "docs/retrospective.md")),
        (3, "maturity assessment exists", lambda r: exists(r, "docs/maturity-assessment.md")),
        (1, "MANUAL open items closed, deferred with an owner, or withdrawn", None),
        (2, "MANUAL one concrete process change carried forward", None),
        (3, "MANUAL onboarding test: a newcomer can operate this from the docs", None),
    ],
}


def main():
    parser = argparse.ArgumentParser(description="Ilana gate checker")
    parser.add_argument("--gate", required=True)
    parser.add_argument("--rigour", type=int, default=3, choices=[1, 2, 3, 4, 5])
    parser.add_argument("--repo", default=".")
    parser.add_argument("--strict", action="store_true",
                        help="exit non-zero if any automatable criterion fails")
    args = parser.parse_args()

    gate = args.gate.upper()
    if gate not in CHECKS:
        print("unknown gate " + gate + ". known: " + ", ".join(sorted(CHECKS)))
        return 2

    root = args.repo
    print("GATE %s   rigour %d   repo %s" % (gate, args.rigour, os.path.abspath(root)))
    print()
    failed = manual = passed = skipped = 0

    for min_rigour, label, fn in CHECKS[gate]:
        if min_rigour > args.rigour:
            print("  [skip] R%d+  %s" % (min_rigour, label.replace("MANUAL ", "")))
            skipped += 1
            continue
        if fn is None:
            print("  [MAN ] R%d+  %s" % (min_rigour, label.replace("MANUAL ", "")))
            manual += 1
            continue
        try:
            ok = bool(fn(root))
        except Exception as exc:  # a check that errors is a failed check
            ok = False
            label = label + "  (check errored: " + str(exc) + ")"
        print("  [%s] R%d+  %s" % ("pass" if ok else "FAIL", min_rigour, label))
        if ok:
            passed += 1
        else:
            failed += 1

    print()
    print("automated: %d passed, %d failed   manual: %d   not applicable at this rigour: %d"
          % (passed, failed, manual, skipped))

    if gate == "G1":
        hits = scan_adjectives(root)
        if hits:
            print("\nunmeasurable adjectives found:")
            for h in hits[:20]:
                print("  " + h)
            print("  each must be rewritten with a number and a unit, or moved out of")
            print("  the requirements section and called a goal.")

    if gate == "G4":
        hits = scan_secrets(root)
        if hits:
            print("\nplausible secrets found:")
            for h in hits[:20]:
                print("  " + h)
            print("  move these to configuration or a secret store. if any reached the")
            print("  history, rotate the secret; deletion is cosmetic.")

    print()
    if failed:
        print("VERDICT: not ready. %d automated criteria unmet." % failed)
    elif manual:
        print("VERDICT: automated criteria met. %d criteria require human judgement." % manual)
        print("A gate is not passed until the manual criteria are assessed and recorded.")
    else:
        print("VERDICT: all applicable criteria met.")

    return 1 if (args.strict and failed) else 0


if __name__ == "__main__":
    sys.exit(main())
