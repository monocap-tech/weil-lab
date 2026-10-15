#!/usr/bin/env python3
"""Run RPB108 checkpoint custody checks or an exact stored-certificate replay.

The validator's --replay compares against the committed JSON and checks its
inherited Git-blob pins; this harness neither regenerates ancestors nor
asserts any RH/Stage-I theorem.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import traceback

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_RE = re.compile(r"validate_rpb108_rc([0-9]+)_[a-z0-9_]+\.py$")
REQUIRED_DIRS = ("scripts", "certificates", "notes")


def select_checkpoint(value: str) -> tuple[int, dict[str, Path]]:
    if value != "latest" and not re.fullmatch(r"[0-9]{1,4}", value):
        raise ValueError("checkpoint must be 'latest' or a 1–4 digit RC number")

    numbered: dict[int, list[Path]] = {}
    for script in (ROOT / "scripts").glob("validate_rpb108_rc*.py"):
        match = SCRIPT_RE.fullmatch(script.name)
        if match:
            numbered.setdefault(int(match.group(1)), []).append(script)
    if not numbered:
        raise ValueError("no RPB108 RC validator scripts found")

    number = max(numbered) if value == "latest" else int(value)
    scripts = numbered.get(number, [])
    candidates = {
        "script": scripts,
        "certificate": list((ROOT / "certificates").glob(
            f"rpb108_rc{number}_*.json")),
        "note": list((ROOT / "notes").glob(
            f"RPB108_RC{number}_*.md")),
    }
    for kind, matches in candidates.items():
        if len(matches) != 1:
            raise ValueError(
                f"RC{number}: expected exactly one {kind}, found {len(matches)}: "
                + ", ".join(str(x.relative_to(ROOT)) for x in matches))
    return number, {kind: files[0] for kind, files in candidates.items()}


def git_blob_sha(path: Path) -> str:
    content = path.read_bytes()
    return hashlib.sha1(
        b"blob " + str(len(content)).encode("ascii") + b"\0" + content
    ).hexdigest()


def custody(number: int, paths: dict[str, Path]) -> dict:
    certificate = json.loads(paths["certificate"].read_text(encoding="utf-8"))
    if not isinstance(certificate, dict):
        raise ValueError("certificate root must be a JSON object")
    ast.parse(paths["script"].read_text(encoding="utf-8"),
              filename=str(paths["script"]))
    note = paths["note"].read_text(encoding="utf-8")
    if not re.search(r"\bRC" + str(number) + r"\b", note):
        raise ValueError("note does not identify its checkpoint")
    result = {
        "checkpoint": f"RC{number}",
        "certificate_keys": len(certificate),
        "files": {
            name: {
                "path": str(path.relative_to(ROOT)),
                "git_blob_sha1": git_blob_sha(path),
            }
            for name, path in paths.items()
        },
    }
    # This is a structural/custody check, not a proof validation.
    print(f"RC{number}: custody OK (note, JSON, and parseable validator)")
    return result


def replay(paths: dict[str, Path]) -> None:
    # RC validators read their saved --output file when --replay is set.
    # Use the COMMITTED artifact, not an empty temporary destination.
    certificate = paths["certificate"]
    before = hashlib.sha256(certificate.read_bytes()).hexdigest()
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONUNBUFFERED="1")
    command = [
        sys.executable,
        str(paths["script"].relative_to(ROOT)),
        "--output",
        str(certificate.relative_to(ROOT)),
        "--replay",
    ]
    print("Exact checkpoint replay:", " ".join(command), flush=True)
    completed = subprocess.run(command, cwd=ROOT, env=env, check=False)
    if completed.returncode:
        raise RuntimeError(f"validator replay failed: exit {completed.returncode}")
    after = hashlib.sha256(certificate.read_bytes()).hexdigest()
    if before != after:
        raise RuntimeError("validator modified the committed certificate")
    print("Exact stored-certificate replay PASSED", flush=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", default="latest")
    parser.add_argument("--mode", choices=("custody", "replay"),
                        default="custody")
    parser.add_argument("--report", default="rpb108-actions-report.json")
    args = parser.parse_args()

    start = time.monotonic()
    result = {
        "requested_checkpoint": args.checkpoint,
        "mode": args.mode,
        "git_sha": os.environ.get("GITHUB_SHA", ""),
        "status": "failed",
    }
    try:
        number, paths = select_checkpoint(args.checkpoint)
        result.update(custody(number, paths))
        if args.mode == "replay":
            replay(paths)
        result["status"] = "passed"
        return 0
    except Exception as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"
        traceback.print_exc()
        return 1
    finally:
        result["elapsed_seconds"] = round(time.monotonic() - start, 3)
        report = ROOT / args.report
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8")
        print(f"Report: {report.relative_to(ROOT)} ({result['status']})",
              flush=True)
        summary = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary:
            with open(summary, "a", encoding="utf-8") as stream:
                stream.write(
                    f"### RPB108 {args.mode}: {result['status']}\n\n"
                    f"Checkpoint: {result.get('checkpoint', args.checkpoint)}  \n"
                    "This run checks certificate reproducibility, not Stage I "
                    "closure or RH.\n"
                )


if __name__ == "__main__":
    sys.exit(main())
