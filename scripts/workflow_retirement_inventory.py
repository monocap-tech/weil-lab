#!/usr/bin/env python3
"""Read-only GitHub Actions trigger inventory and retirement custody check.

Static YAML-pattern inspection only. Not full YAML/Actions validation,
Lean compilation, or a certificate acceptance gate.
"""
import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

LEDGERS = (
    "docs/governance/NF453_NF474_MANUAL_ONLY_RETIREMENT_20261121.json",
    "docs/governance/NF475_NF505_PR_TRIGGER_RETIREMENT_20261121.json",
)
ROOT_EVENT = re.compile(r"^on[ \t]*:[ \t]*(.*)$", re.M)
EVENT_NAME = re.compile(r"^  ([A-Za-z_][A-Za-z0-9_-]*)[ \t]*:", re.M)
TOPLEVEL = re.compile(r"^[^\s#][^:\n]*\s*:", re.M)


def git_blob_sha(content: bytes) -> str:
    return hashlib.sha1(f"blob {len(content)}\0".encode() + content).hexdigest()


def trigger_events(text: str) -> dict[str, str]:
    """Extract conventional GitHub Actions on: entries without YAML coercion."""
    match = ROOT_EVENT.search(text)
    if not match:
        return {}
    inline = match.group(1).strip()
    if inline:
        if inline.startswith("[") and inline.endswith("]"):
            return {v.strip().strip("\"'"): "" for v in inline[1:-1].split(",") if v.strip()}
        return {inline.strip("\"'"): ""}
    end = TOPLEVEL.search(text, match.end())
    block = text[match.end():end.start()] if end else text[match.end():]
    hits = list(EVENT_NAME.finditer(block))
    return {
        hit.group(1): block[hit.end():(hits[i + 1].start() if i + 1 < len(hits) else len(block))]
        for i, hit in enumerate(hits)
    }


def classify(events: dict[str, str]) -> str:
    if "pull_request_target" in events:
        return "pull_request_target_review"
    if "pull_request" in events:
        body = events["pull_request"]
        if re.search(r"^    paths(?:-ignore)?\s*:", body, re.M):
            return "path_scoped_pull_request"
        if re.search(r"^    types\s*:", body, re.M):
            return "event_filtered_pull_request"
        return "unrestricted_pull_request"
    if set(events) == {"workflow_dispatch"}:
        return "manual_only"
    if not events:
        return "unknown_or_missing_on"
    return "other_triggers"


def audit(repo: Path, check: bool) -> dict:
    folder = repo / ".github/workflows"
    if not folder.is_dir():
        raise ValueError(f"workflow directory not found: {folder}")
    files = sorted([*folder.glob("*.yml"), *folder.glob("*.yaml")])
    entries = {}
    for path in files:
        content = path.read_bytes()
        events = trigger_events(content.decode("utf-8"))
        entries[path.relative_to(repo).as_posix()] = {
            "mode": classify(events), "events": sorted(events),
            "blob": git_blob_sha(content),
        }
    mode_counts = Counter(v["mode"] for v in entries.values())
    failures, checked = [], 0
    for ledger_path in LEDGERS:
        file_path = repo / ledger_path
        if not file_path.is_file():
            failures.append(f"missing ledger: {ledger_path}")
            continue
        ledger = json.loads(file_path.read_text(encoding="utf-8"))
        for record in ledger["workflows"]:
            path = record["path"]
            checked += 1
            actual = entries.get(path)
            expected = record.get("manual_only_git_blob_sha") or record.get("retained_git_blob_sha")
            if actual is None:
                failures.append(f"missing retained workflow: {path}")
            elif actual["blob"] != expected:
                failures.append(f"changed Git blob since custody ledger: {path}")
            elif "pull_request" in actual["events"] or "pull_request_target" in actual["events"]:
                failures.append(f"automatic PR trigger restored: {path}")
            elif "workflow_dispatch" not in actual["events"]:
                failures.append(f"manual dispatch missing: {path}")
    summary = {
        "workflow_count": len(entries),
        "trigger_modes": dict(sorted(mode_counts.items())),
        "unrestricted_pull_request": sorted(
            path for path, data in entries.items() if data["mode"] == "unrestricted_pull_request"
        ),
        "custody_records_checked": checked,
        "custody_errors": failures,
        "scope": "static source audit only, not YAML/Actions semantics or Lean certification",
    }
    if check and failures:
        raise ValueError("\n".join(failures))
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--check", action="store_true", help="fail if a retirement custody record drifts")
    parser.add_argument("--output", type=Path, help="optional JSON output path; otherwise print")
    args = parser.parse_args()
    report = audit(args.repo.resolve(), args.check)
    result = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(result, encoding="utf-8")
    else:
        print(result, end="")


if __name__ == "__main__":
    main()
