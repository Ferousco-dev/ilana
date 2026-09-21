#!/usr/bin/env python3
"""Ilana repository map and change-scope guard.

Gives a coding agent the state of an EXISTING repository in one short document,
and proves that work stayed inside its scope. Stdlib only. Python 3.8+.

Usage:
    python3 repo_map.py map      [--repo .] [--out .ilana/repo-map.md] [--stdout]
    python3 repo_map.py snapshot [--repo .] [--allow GLOB ...]
    python3 repo_map.py guard    [--repo .] [--json]

`map` writes a compact summary: branch, recent commits, uncommitted work, languages,
entry points, packages and their import edges, data ownership (migrations, tables) and
environment variables read by the code.

`snapshot` records every currently dirty path with a content hash, plus the allowed
scope globs. `guard` compares the tree to that baseline and exits 1 if a file that was
already dirty was modified or reverted, because that is somebody else's work.
"""

import argparse
import fnmatch
import hashlib
import json
import os
import re
import subprocess
import sys

BASELINE = os.path.join(".ilana", "scope-baseline.json")
ALWAYS_ALLOWED = [".ilana/**"]
SKIP_DIRS = {".git", "node_modules", "vendor", "dist", "build", "__pycache__", ".venv", "venv", "data"}
LANG = {".go": "Go", ".py": "Python", ".js": "JavaScript", ".ts": "TypeScript", ".tsx": "TypeScript",
        ".java": "Java", ".kt": "Kotlin", ".rs": "Rust", ".rb": "Ruby", ".php": "PHP", ".cs": "C#",
        ".swift": "Swift", ".dart": "Dart", ".sql": "SQL", ".sh": "Shell"}
CONTAINER_DIRS = ("internal", "pkg", "src", "app", "apps", "lib", "cmd", "services", "packages")


def git(repo, *args):
    try:
        out = subprocess.run(["git", "-C", repo] + list(args), capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return None
    return out.stdout if out.returncode == 0 else None


def tracked(repo):
    out = git(repo, "ls-files")
    return [p for p in out.splitlines() if p] if out else []


def dirty(repo):
    """Return {path: status} for modified, added, deleted and untracked files."""
    out = git(repo, "status", "--porcelain", "-uall")
    result = {}
    for line in (out or "").splitlines():
        if len(line) < 4:
            continue
        status, path = line[:2].strip() or "?", line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        result[path.strip('"')] = status
    return result


def content_hash(repo, path):
    full = os.path.join(repo, path)
    if not os.path.exists(full):
        return "MISSING"
    if os.path.isdir(full):
        return "DIR"
    h = hashlib.sha1()
    with open(full, "rb") as fh:
        h.update(fh.read())
    return h.hexdigest()


def glob_to_regex(pattern):
    out, i = "", 0
    while i < len(pattern):
        c = pattern[i]
        if pattern[i:i + 3] == "**/":
            out += "(?:.*/)?"
            i += 3
            continue
        if pattern[i:i + 2] == "**":
            out += ".*"
            i += 2
            continue
        out += "[^/]*" if c == "*" else ("[^/]" if c == "?" else re.escape(c))
        i += 1
    return re.compile("^" + out + "$")


def matches(path, patterns):
    return any(glob_to_regex(p).match(path) for p in patterns)


# ------------------------------------------------------------------- map ----

def read_text(repo, path, limit=400_000):
    try:
        with open(os.path.join(repo, path), "r", encoding="utf-8", errors="ignore") as fh:
            return fh.read(limit)
    except OSError:
        return ""


def build_map(repo):
    files = tracked(repo)
    if not files:
        return "# Repository map\n\nNot a git repository, or no tracked files.\n"
    lines = ["# Repository map", ""]
    branch = (git(repo, "branch", "--show-current") or "").strip() or "(detached)"
    head = (git(repo, "rev-parse", "--short", "HEAD") or "").strip() or "(no commits)"
    upstream = (git(repo, "rev-parse", "--abbrev-ref", "@{upstream}") or "").strip()
    ahead = ""
    if upstream:
        counts = (git(repo, "rev-list", "--left-right", "--count", "HEAD...@{upstream}") or "").split()
        if len(counts) == 2:
            ahead = " (ahead %s, behind %s)" % (counts[0], counts[1])
    lines.append("- branch: `%s` at `%s`%s%s" % (branch, head, " tracking `%s`" % upstream if upstream else "", ahead))
    total = (git(repo, "rev-list", "--count", "HEAD") or "?").strip()
    lines.append("- commits: %s" % total)
    lines += ["", "## Recent commits"]
    for row in (git(repo, "log", "-8", "--format=%h %s") or "").splitlines():
        lines.append("- " + row)

    changes = dirty(repo)
    lines += ["", "## Uncommitted work (%d paths)" % len(changes)]
    if changes:
        groups = {}
        for path, status in sorted(changes.items()):
            top = path.split("/")[0] + ("/" if "/" in path else "")
            groups.setdefault(top, []).append(status)
        for top, statuses in sorted(groups.items()):
            lines.append("- `%s` %d (%s)" % (top, len(statuses), ",".join(sorted(set(statuses)))))
    else:
        lines.append("- none (clean working tree)")

    counts = {}
    for path in files:
        lang = LANG.get(os.path.splitext(path)[1])
        if lang:
            counts[lang] = counts.get(lang, 0) + 1
    lines += ["", "## Languages (tracked files)"]
    lines.append(", ".join("%s %d" % kv for kv in sorted(counts.items(), key=lambda kv: -kv[1])[:6]) or "none detected")

    lines += ["", "## Entry points"]
    entries = []
    for path in files:
        base = os.path.basename(path)
        if base in ("main.go", "__main__.py", "manage.py", "Dockerfile", "compose.yaml", "docker-compose.yml", "Makefile"):
            entries.append(path)
        elif path.endswith("package.json") and "node_modules" not in path:
            entries.append(path)
    lines.append(", ".join("`%s`" % e for e in entries[:14]) or "none detected")

    lines += ["", "## Packages and import edges"]
    module = ""
    if "go.mod" in files:
        match = re.search(r"^module\s+(\S+)", read_text(repo, "go.mod"), re.M)
        module = match.group(1) if match else ""
    packages = {}
    for path in files:
        parts = path.split("/")
        if len(parts) >= 3 and parts[0] in CONTAINER_DIRS:
            packages.setdefault("/".join(parts[:2]), []).append(path)
        elif len(parts) == 2 and parts[0] in CONTAINER_DIRS:
            packages.setdefault(parts[0], []).append(path)
    for name, members in sorted(packages.items()):
        code = [m for m in members if os.path.splitext(m)[1] in LANG and "_test" not in m and "/test" not in m]
        if not code:
            continue
        deps = set()
        if module:
            for member in code:
                if member.endswith(".go"):
                    for imp in re.findall(r'"%s/([^"]+)"' % re.escape(module), read_text(repo, member)):
                        dep = "/".join(imp.split("/")[:2]) if imp.split("/")[0] != "cmd" else imp
                        if dep != name:
                            deps.add(dep)
        tail = " -> " + ", ".join(sorted(deps)) if deps else ""
        lines.append("- `%s` (%d files)%s" % (name, len(code), tail))
    if not any(os.path.splitext(m)[1] in LANG for ms in packages.values() for m in ms):
        lines.append("- no conventional package directories found")

    lines += ["", "## Data ownership"]
    sql = sorted(p for p in files if p.endswith(".sql") and "migration" in p.lower())
    ups = [p for p in sql if not p.endswith(".down.sql")]
    tables = []
    for path in ups:
        tables += re.findall(r"CREATE TABLE(?: IF NOT EXISTS)?\s+([A-Za-z0-9_\.\"]+)", read_text(repo, path), re.I)
    if ups:
        lines.append("- migrations: %d, latest `%s`" % (len(ups), os.path.basename(ups[-1])))
        lines.append("- tables: " + ", ".join(sorted(set(t.strip('"') for t in tables))))
    else:
        lines.append("- no SQL migrations found")

    env = set()
    for path in files:
        if os.path.splitext(path)[1] in (".go", ".py", ".js", ".ts") and "_test" not in path:
            text = read_text(repo, path)
            env.update(re.findall(r'(?:Getenv|LookupEnv)\("([A-Z][A-Z0-9_]+)"\)', text))
            env.update(re.findall(r'os\.environ(?:\.get)?[\[\(]"([A-Z][A-Z0-9_]+)"', text))
            env.update(re.findall(r"process\.env\.([A-Z][A-Z0-9_]+)", text))
    lines += ["", "## Environment variables read by code", ", ".join(sorted(env)) or "none detected"]
    lines += ["", "Generated by `repo_map.py map`. Facts only; regenerate instead of editing."]
    return "\n".join(lines) + "\n"


def cmd_map(args):
    text = build_map(args.repo)
    if args.stdout:
        sys.stdout.write(text)
        return 0
    out = os.path.join(args.repo, args.out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(text)
    print("wrote %s (%d lines)" % (args.out, text.count("\n")))
    return 0


# ----------------------------------------------------------------- guard ----

def cmd_snapshot(args):
    changes = dirty(args.repo)
    head = (git(args.repo, "rev-parse", "HEAD") or "").strip()
    baseline = {
        "head": head,
        "allow": ALWAYS_ALLOWED + list(args.allow or []),
        "preexisting": {p: {"status": s, "hash": content_hash(args.repo, p)} for p, s in changes.items()},
    }
    out = os.path.join(args.repo, BASELINE)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(baseline, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print("scope baseline: %d pre-existing dirty path(s) protected, %d allow glob(s)" %
          (len(baseline["preexisting"]), len(baseline["allow"])))
    return 0


def guard(repo):
    path = os.path.join(repo, BASELINE)
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        base = json.load(fh)
    now = dirty(repo)
    pre = base["preexisting"]
    report = {"violations": [], "out_of_scope": [], "in_scope": [], "protected_untouched": 0}
    for p, info in sorted(pre.items()):
        current = content_hash(repo, p)
        if current == info["hash"]:
            report["protected_untouched"] += 1
        elif current == "MISSING":
            report["violations"].append("%s: pre-existing change was removed or deleted" % p)
        else:
            report["violations"].append("%s: pre-existing change was modified" % p)
    for p in sorted(now):
        if p in pre:
            continue
        (report["in_scope"] if matches(p, base["allow"]) else report["out_of_scope"]).append(p)
    return report


def cmd_guard(args):
    report = guard(args.repo)
    if report is None:
        print("no baseline: run `repo_map.py snapshot` before starting work", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print("protected untouched: %d" % report["protected_untouched"])
        print("in scope: %d, out of scope: %d, violations: %d" %
              (len(report["in_scope"]), len(report["out_of_scope"]), len(report["violations"])))
        for label in ("violations", "out_of_scope"):
            for item in report[label]:
                print("  %s  %s" % (label.upper().replace("_", "-"), item))
    return 1 if report["violations"] or report["out_of_scope"] else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    m = sub.add_parser("map")
    m.add_argument("--repo", default=".")
    m.add_argument("--out", default=os.path.join(".ilana", "repo-map.md"))
    m.add_argument("--stdout", action="store_true")
    s = sub.add_parser("snapshot")
    s.add_argument("--repo", default=".")
    s.add_argument("--allow", nargs="*", default=[])
    g = sub.add_parser("guard")
    g.add_argument("--repo", default=".")
    g.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    return {"map": cmd_map, "snapshot": cmd_snapshot, "guard": cmd_guard}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
