#!/usr/bin/env python3
"""UOI005 fail-closed proposed source-scoped PR-trigger patch builder.

This stages a *preview*, never changes an input tree, never calls git, and
cannot dispatch Actions. Its complete safety proof is *not* supplied by a dry
run: it does not decide GitHub branch rules, push triggers or transitive deps.

Usage:
 python scripts/uoi_source_scope_patch.py --source-root /tmp/exact-NF768 \
   --plan research/unified/repairs/UOI005_nf768_four_source_scopes.json
 python scripts/uoi_source_scope_patch.py --source-root /tmp/exact-NF768 \
   --plan ... --preview-dir /tmp/separate-preview > repair-review.json
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
from pathlib import Path
import re
import sys

HEX40 = re.compile(r"[a-f0-9]{40}\Z")
PATH = re.compile(r"[A-Za-z0-9._/+\-]+\Z")
EVENT = b"on:\n  pull_request:\n  workflow_dispatch:\n"
STANDING = "source-verified-dry-run-proposal-NOT-APPLIED"


class RepairError(ValueError):
    pass


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\x00" + data).hexdigest()


def _path(s: str, *, workflow: bool = False) -> Path:
    if (not isinstance(s, str) or not PATH.fullmatch(s) or s.startswith("/")
            or any(x in ("", ".", "..") for x in s.split("/"))):
        raise RepairError(f"unsafe plan path {s!r}")
    path = Path(s)
    if workflow and (not s.startswith(".github/workflows/") or path.suffix not in (".yml", ".yaml")):
        raise RepairError("workflow outside .github/workflows")
    return path


def check_plan(plan: dict) -> None:
    if not isinstance(plan, dict) or plan.get("schema") != "UOI005-proposed-NF768-scoped-PR-repair-v1":
        raise RepairError("unsupported plan schema")
    if (plan.get("status") != STANDING or plan.get("approved_for_push") is not False
            or plan.get("approved_for_pr") is not False
            or plan.get("dispatch_authorized") is not False
            or plan.get("accepted_theorems_modified") is not False):
        raise RepairError("proposed repair must preserve all NO-GO guards")
    if plan.get("research_branch_sha") != "b477d9a8eb6c33781a8eee7c1208de93c705f307":
        raise RepairError("NF768 original source baseline changed; review before proceeding")
    rows = plan.get("workflows")
    if not isinstance(rows, list) or len(rows) != 4:
        raise RepairError("expected four narrow repair proposals")
    seen = set()
    for row in rows:
        if not isinstance(row, dict):
            raise RepairError("bad repair row")
        name = str(_path(row.get("workflow"), workflow=True))
        if name in seen:
            raise RepairError("duplicate workflow")
        seen.add(name)
        if not isinstance(row.get("git_blob_sha"), str) or not HEX40.fullmatch(row["git_blob_sha"]):
            raise RepairError("invalid workflow blob sha")
        deps = row.get("source_blobs")
        paths = row.get("pr_paths")
        if not isinstance(deps, dict) or not deps or not isinstance(paths, list):
            raise RepairError("missing source blobs / PR paths")
        if paths != [name] + list(deps):
            raise RepairError("path list must enumerate own workflow then every pinned direct input")
        if len(set(paths)) != len(paths):
            raise RepairError("duplicate filter path")
        for path, sha in deps.items():
            _path(path)
            if not isinstance(sha, str) or not HEX40.fullmatch(sha):
                raise RepairError("missing pinned direct dependency blob sha")
            if path.startswith(".github/workflows/"):
                raise RepairError("nested workflow path is not a direct data/script input")


def verify_source(source_root: Path, name: str, expected_sha: str) -> bytes:
    relative = _path(name)
    root = source_root.resolve(strict=True)
    p = (root / relative).resolve(strict=True)
    if not p.is_relative_to(root):
        raise RepairError("source symlink escaped root: " + name)
    data = p.read_bytes()
    if git_blob_sha(data) != expected_sha:
        raise RepairError("source blob mismatch: " + name)
    return data


def patch_yaml(source: bytes, paths: list[str]) -> bytes:
    # Exact original syntax, not a general-purpose YAML rewriting tool.
    if source.count(EVENT) != 1 or source.count(b"\njobs:\n") != 1:
        raise RepairError("workflow does not have the frozen bare-PR/manual event format")
    for unsafe in (b"pull_request_target:", b"workflow_run:", b"repository_dispatch:", b"push:"):
        if unsafe in source.split(b"\njobs:\n")[0]:
            raise RepairError("unexpected event: " + unsafe.decode())
    filters = b"    paths:\n" + b"".join(
        b"      - '" + str(_path(p)).encode("ascii") + b"'\n" for p in paths)
    patched = source.replace(EVENT, b"on:\n  pull_request:\n" + filters + b"  workflow_dispatch:\n")
    assert patched.count(b"  workflow_dispatch:\n") == 1
    assert patched.split(b"\njobs:\n", 1)[1] == source.split(b"\njobs:\n", 1)[1]
    return patched


def preview(source_root: Path, plan: dict) -> list[dict]:
    check_plan(plan)
    rows = []
    for row in plan["workflows"]:
        name = row["workflow"]
        original = verify_source(source_root, name, row["git_blob_sha"])
        for dep, sha in row["source_blobs"].items():
            verify_source(source_root, dep, sha)
        changed = patch_yaml(original, row["pr_paths"])
        if changed == original:
            raise RepairError(name + ": patch had no effect")
        diff = "".join(difflib.unified_diff(
            original.decode("utf-8").splitlines(keepends=True),
            changed.decode("utf-8").splitlines(keepends=True),
            fromfile="a/" + name, tofile="b/" + name))
        rows.append({"workflow": name, "original_git_blob_sha": row["git_blob_sha"],
                     "proposed_git_blob_sha": git_blob_sha(changed),
                     "source_dependency_count": len(row["source_blobs"]),
                     "filter_path_count": len(row["pr_paths"]),
                     "manual_dispatch_preserved": True,
                     "job_body_byte_identical": True,
                     "diff": diff,
                     "_content": changed})
    return rows


def run(source_root: Path, plan: dict, preview_dir: Path | None = None) -> dict:
    source_root = source_root.resolve(strict=True)
    rows = preview(source_root, plan)
    if preview_dir is not None:
        dest = preview_dir.resolve()
        if dest == source_root or dest.is_relative_to(source_root) or source_root.is_relative_to(dest):
            raise RepairError("preview directory must be separate from source tree")
        for row in rows:
            target = dest / row["workflow"]
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                raise RepairError("refusing to overwrite staged file: " + str(target))
            target.write_bytes(row["_content"])
    public = [{k: v for k, v in row.items() if k != "_content"} for row in rows]
    return {"classification": "proposal_only_not_applied_to_source", "source_branch_sha": plan["research_branch_sha"],
            "files": public, "preview_dir": str(preview_dir) if preview_dir else None,
            "jobs_modified": False, "workflow_dispatch_preserved": True,
            "dispatch_authorized": False, "pr_authorized": False,
            "push_authorized": False, "required_checks_verified": False,
            "entire_workflow_tree_audited": False,
            "mathematical_promotion_authorized": False}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source-root", type=Path, required=True)
    p.add_argument("--plan", type=Path, required=True)
    p.add_argument("--preview-dir", type=Path)
    args = p.parse_args()
    try:
        result = run(args.source_root, json.loads(args.plan.read_text()), args.preview_dir)
        print(json.dumps(result, indent=2))
        return 0
    except (OSError, UnicodeError, ValueError) as e:
        print("UOI005 PATCH PREVIEW FAILED CLOSED:", str(e), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
