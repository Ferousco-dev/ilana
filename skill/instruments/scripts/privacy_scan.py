#!/usr/bin/env python3
"""Ilana privacy checklist generator and marker checker.

Derives a security and privacy checklist from what the repository actually handles,
instead of a generic list. Stdlib only. Python 3.8+.

Usage:
    python3 privacy_scan.py scan  [--repo .] [--out .ilana/privacy-checklist.md] [--stdout]
    python3 privacy_scan.py check --markers M1,M2 FILE...      (use - for stdin)

`scan` finds which sensitive data classes appear in tracked source (identifiers, columns,
environment names), adds domain classes only when the domain is detected (mail, webhook),
and lists log or print lines that mention a sensitive identifier for human review.
`check` fails if any marker string appears in captured logs, metrics or responses, which
is how a test proves a secret never reached an output.
"""

import argparse
import os
import re
import subprocess
import sys

TEXT_EXT = {".go", ".py", ".js", ".ts", ".tsx", ".java", ".kt", ".rs", ".rb", ".php", ".cs", ".sql", ".yaml",
            ".yml", ".json", ".env", ".sh", ".swift", ".dart"}

# name, domain ("all" or a detected domain), regex, what must never happen
CLASSES = [
    ("credentials", "all", r"password|passwd|secret|api[_-]?key|apikey|bearer|authorization|private[_-]?key|master[_-]?key|credential",
     "never logged, returned after creation, used as a metric label, or stored unhashed/unencrypted"),
    ("tokens and sessions", "all", r"\btoken\b|cookie|jwt|session[_-]?token",
     "never logged or exposed in URLs, errors, or metrics"),
    ("personal identifiers", "all", r"e-?mail|phone|\bssn\b|\bdob\b|passport",
     "never logged, used as a metric label, or echoed in errors unless the requirement says so"),
    ("recipient and sender addresses", "mail", r"recipient|rcpt|mail_?from|reply[_-]?to|\bbcc\b",
     "never logged; Bcc never appears in headers or responses"),
    ("message content", "mail", r"\bbody\b|raw[_-]?mime|\bmime\b|attachment|subject|text_body|html_body",
     "never logged, exposed in metrics, or included in health and error responses"),
    ("delivery diagnostics", "mail", r"\bdsn\b|bounce|remote[_-]?message|smtp[_-]?response|enhanced[_-]?status",
     "remote text is untrusted and may contain addresses; never log or label with it"),
    ("signing material", "webhook", r"signature|hmac|whsec|signing",
     "never logged; verify in constant time; secrets stored encrypted and recoverable only where required"),
    ("outbound destinations", "webhook", r"webhook[_-]?url|\bendpoint\b|callback[_-]?url",
     "validate at connect time (SSRF and DNS rebinding); never log full URLs"),
]
DOMAIN_DETECT = {"mail": r"smtp|mime|\bdsn\b|imap|rfc ?5321", "webhook": r"webhook"}
LOG_CALL = re.compile(r"\b(?:log|logger|slog|logging|console)\.\w+\(|fmt\.(?:Print|Fprint|Sprint)\w*\(|\bprint\(|\bprintf\(|\bPrintln\(|\.(?:Info|Warn|Error|Debug)\(")
MAX_BYTES = 300_000


def tracked(repo):
    try:
        out = subprocess.run(["git", "-C", repo, "ls-files"], capture_output=True, text=True, timeout=60)
        files = out.stdout.split("\n") if out.returncode == 0 else []
    except (OSError, subprocess.SubprocessError):
        files = []
    if not any(files):
        for base, dirs, names in os.walk(repo):
            dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "vendor", ".venv", "__pycache__")]
            files += [os.path.relpath(os.path.join(base, n), repo) for n in names]
    return [f for f in files if f and os.path.splitext(f)[1] in TEXT_EXT]


def is_test(path):
    low = path.lower()
    return "_test." in low or "/test" in low or low.startswith("test") or ".test." in low or "/fixtures/" in low


def read_lines(repo, path):
    try:
        if os.path.getsize(os.path.join(repo, path)) > MAX_BYTES:
            return []
        with open(os.path.join(repo, path), encoding="utf-8", errors="ignore") as fh:
            return fh.read().splitlines()
    except OSError:
        return []


def scan(repo):
    files = tracked(repo)
    corpus = {f: read_lines(repo, f) for f in files}
    domains = {"all"}
    for name, pattern in DOMAIN_DETECT.items():
        hits = sum(1 for f, ls in corpus.items() if not is_test(f) for ln in ls if re.search(pattern, ln, re.I))
        if hits >= 3:
            domains.add(name)
    rows, leaks = [], []
    for name, domain, pattern, rule in CLASSES:
        if domain not in domains:
            continue
        rx = re.compile(pattern, re.I)
        where = {}
        for f, ls in corpus.items():
            if is_test(f):
                continue
            for i, ln in enumerate(ls, 1):
                if rx.search(ln):
                    where.setdefault(f, []).append(i)
                    if LOG_CALL.search(ln) and not ln.strip().startswith(("//", "#")):
                        leaks.append((name, f, i, ln.strip()[:110]))
        examples = ["%s:%d" % (f, ls[0]) for f, ls in sorted(where.items(), key=lambda kv: -len(kv[1]))[:4]]
        rows.append((name, domain, len(where), examples, rule))
    return sorted(domains), rows, leaks


def render(repo):
    domains, rows, leaks = scan(repo)
    out = ["# Privacy and security checklist", "",
           "Domains detected: %s. Generated by `privacy_scan.py scan`; regenerate rather than edit. "
           "Mark each row in the ledger with the evidence id that proves it, never with prose." % ", ".join(domains), "",
           "| Class | Files | Where (examples) | Must hold | Status |", "| --- | --- | --- | --- | --- |"]
    for name, domain, count, examples, rule in rows:
        out.append("| %s | %d | %s | %s | unchecked |" % (name, count, ", ".join("`%s`" % e for e in examples) or "-", rule))
    out += ["", "## Output paths to verify with marker tests",
            "Logs, metrics labels, health and error bodies, panic recovery, and API responses. "
            "Prove each with `privacy_scan.py check --markers ...` against captured output."]
    out += ["", "## Log or print lines mentioning a sensitive identifier (review each, %d found)" % len(leaks)]
    for name, f, i, text in leaks[:25]:
        out.append("- `%s:%d` (%s): `%s`" % (f, i, name, text.replace("`", "'")))
    if len(leaks) > 25:
        out.append("- ... %d more" % (len(leaks) - 25))
    if not leaks:
        out.append("- none found")
    return "\n".join(out) + "\n"


def cmd_scan(args):
    text = render(args.repo)
    if args.stdout:
        sys.stdout.write(text)
        return 0
    out = os.path.join(args.repo, args.out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(text)
    print("wrote %s (%d classes, %d log lines to review)" % (args.out, text.count("\n| ") - 1, text.count("\n- `")))
    return 0


def cmd_check(args):
    markers = [m for m in args.markers.split(",") if m]
    if not markers:
        print("no markers given", file=sys.stderr)
        return 2
    bad = 0
    for name in args.files:
        text = sys.stdin.read() if name == "-" else open(name, encoding="utf-8", errors="ignore").read()
        for marker in markers:
            count = text.count(marker)
            if count:
                bad += count
                print("LEAK  %s appears %d time(s) in %s" % (marker[:4] + "***", count, "stdin" if name == "-" else name))
    print("markers checked: %d, occurrences found: %d" % (len(markers), bad))
    return 1 if bad else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    s = sub.add_parser("scan")
    s.add_argument("--repo", default=".")
    s.add_argument("--out", default=os.path.join(".ilana", "privacy-checklist.md"))
    s.add_argument("--stdout", action="store_true")
    c = sub.add_parser("check")
    c.add_argument("--markers", required=True)
    c.add_argument("files", nargs="+")
    args = parser.parse_args(argv)
    return {"scan": cmd_scan, "check": cmd_check}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
