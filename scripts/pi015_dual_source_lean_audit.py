#!/usr/bin/env python3
"""PI015 fail-closed TWO-TOOLCHAIN source/object/axiom audit.

Weil-Lab local mathlib: Lean v4.34.0 / Mathlib v4.34.0.
Actual upstream Zeta23: Lean v4.33.0-rc2 / Mathlib v4.33.0-rc2.

This script NEVER equates the two compiled Lean environments. Each
--mode verifies only its own named source statements. A cross-project
Lean import theorem remains an additional proof+toolchain obligation.

Usage after SUCCESSFUL relevant lake build/direct lake env lean:
  python scripts/pi015_dual_source_lean_audit.py --mode local \
     --log pi015-audit/local-axioms.log --olean \
     .lake/build/lib/lean/WeilDefect/Arithmetic/PI015FiniteGammaSymbolBridge.olean
  python scripts/pi015_dual_source_lean_audit.py --mode upstream \
     --upstream pi015-upstream --log pi015-audit/upstream-axioms.log \
     --olean pi015-audit/PI015ExternalPaperFT.olean
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

LOCK = Path("docs/PI015_DUAL_SOURCE_LOCK.json")
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
NAMES = {
    "local": {
        "WeilDefect.pi015FiniteHarmonic_zero",
        "WeilDefect.pi015FiniteHarmonic_succ",
        "WeilDefect.pi015FiniteSymbol_split",
        "WeilDefect.pi015FiniteSymbol_eq_localFourier",
        "WeilDefect.pi015FiniteSymbol_scalar",
    },
    "upstream": {
        "pi015ImportedZeta23PaperFT_unfold",
        "pi015ImportedZeta23PaperFT_real",
    },
}
AXIOM_RECORD = re.compile(
    r"(?m)^(?P<name>[A-Za-z_][A-Za-z_0-9'.]*) "
    r"(?:(?P<none>does not depend on any axioms)"
    r"|depends on axioms:\s*\[(?P<axioms>[^\]]*)\])\s*$"
)
UNFINISHED = re.compile(r"(?m)^\s*(?:sorry|admit|axiom|opaque)\b")


def blob_sha(raw: bytes) -> str:
    return hashlib.sha1(
        b"blob " + str(len(raw)).encode() + b"\0" + raw
    ).hexdigest()


def check_blob(path: Path, expected: str) -> dict:
    if not path.is_file() or not expected:
        raise RuntimeError(f"Required source blob missing: {path}")
    raw = path.read_bytes()
    actual = blob_sha(raw)
    if actual != expected:
        raise RuntimeError(
            f"Wrong Git blob for {path}: {actual}; expected {expected}"
        )
    return {
        "source_path": str(path),
        "source_git_blob": actual,
        "source_sha256": hashlib.sha256(raw).hexdigest(),
    }


def git_head(path: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(path), "rev-parse", "HEAD"], text=True
    ).strip()


def check_axioms(log_path: Path, required: set[str]) -> dict:
    if not log_path.is_file() or log_path.stat().st_size == 0:
        raise RuntimeError(f"No direct Lean axiom log: {log_path}")
    log = log_path.read_text("utf-8")
    if re.search(r"(?mi)(?:^error:|:\d+:\d+: error:)", log):
        raise RuntimeError("Actual Lean compiler errors in printed axiom log")
    parsed = {}
    for m in AXIOM_RECORD.finditer(log):
        name = m.group("name")
        if name in parsed:
            raise RuntimeError(f"Repeated theorem axiom record {name}")
        raw = m.group("axioms")
        axioms = [] if not raw or not raw.strip() else [
            item.strip() for item in raw.split(",")
        ]
        unexpected = set(axioms) - ALLOWED
        if unexpected:
            raise RuntimeError(f"Nonstandard axioms in {name}: {unexpected}")
        parsed[name] = axioms
    if set(parsed) != required:
        raise RuntimeError(
            f"Missing {sorted(required-set(parsed))}; "
            f"unexpected {sorted(set(parsed)-required)}"
        )
    return parsed


def source_check(lock: dict, upstream_dir: Path, mode: str) -> dict:
    # Local pins and all permanently frozen local imported-source blobs.
    local = lock["local"]
    if Path("lean-toolchain").read_text().strip() != local["lean_toolchain"]:
        raise RuntimeError("Local Lean toolchain changed")
    lfile = Path("lakefile.toml").read_text()
    if f'rev = "{local["mathlib_ref"]}"' not in lfile:
        raise RuntimeError("Local Mathlib pin changed")
    local_files = {
        name: check_blob(Path(name), sha)
        for name, sha in local["source_blobs"].items()
    }

    resolved_local = Path(".lake/packages/mathlib")
    if not resolved_local.is_dir():
        raise RuntimeError("Local actual Mathlib checkout missing")
    local_sha = git_head(resolved_local)
    if local_sha != local["mathlib_tag_commit"]:
        raise RuntimeError(
            f"Local actual Mathlib revision mismatched: {local_sha}"
        )

    result = {
        "local_sources": local_files,
        "local_resolved_mathlib_sha": local_sha,
    }

    if mode == "upstream":
        upstream = lock["upstream"]
        if git_head(upstream_dir) != upstream["commit"]:
            raise RuntimeError("Upstream parent repository commit changed")
        up_toolchain = upstream_dir / "zeta23" / "lean-toolchain"
        if up_toolchain.read_text().strip() != upstream["lean_toolchain"]:
            raise RuntimeError("Upstream Lean toolchain changed")
        up_lake = (upstream_dir / "zeta23" / "lakefile.toml").read_text()
        if f'rev = "{upstream["mathlib_commit"]}"' not in up_lake:
            raise RuntimeError("Upstream Mathlib lake pin changed")
        upstream_files = {
            name: check_blob(upstream_dir / name, sha)
            for name, sha in upstream["source_blobs"].items()
        }
        defs = (upstream_dir / "zeta23/Zeta23/Defs.lean").read_text()
        if ("def paperFT (f : ℝ → ℂ) (z : ℂ) : ℂ := "
                "∫ u : ℝ, f u * Complex.exp "
                "(Complex.I * z * (u : ℂ))") not in defs:
            raise RuntimeError("Literal upstream Fourier source changed")

        # This is the real resolved commit in the UPSTREAM package's Lake
        # working graph, not merely a textual rev in lakefile.toml.
        resolved = upstream_dir / "zeta23/.lake/packages/mathlib"
        if not resolved.is_dir():
            raise RuntimeError("Upstream Mathlib checkout missing")
        actual = git_head(resolved)
        if actual != upstream["mathlib_commit"]:
            raise RuntimeError(
                f"Upstream resolved Mathlib SHA differs: {actual}"
            )
        result.update({
            "upstream_head": upstream["commit"],
            "upstream_sources": upstream_files,
            "upstream_resolved_mathlib_sha": actual,
        })
    return result


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=("local", "upstream"), required=True)
    p.add_argument("--upstream", type=Path, default=Path("pi015-upstream"))
    p.add_argument("--log", type=Path, required=True)
    p.add_argument("--olean", type=Path, required=True)
    p.add_argument("--out", type=Path, default=Path("pi015-audit/receipt.json"))
    args = p.parse_args()
    lock = json.loads(LOCK.read_text())
    if lock["schema"] != "weil-lab/pi015-dual-source-lock/v1":
        raise RuntimeError("Unknown source-lock schema")
    if lock["local"]["mathlib_tag_commit"] == lock["upstream"]["mathlib_commit"]:
        raise RuntimeError("Source lock now claims same Mathlib SHA unexpectedly")
    sources = source_check(lock, args.upstream, args.mode)

    src = (Path("WeilDefect/Arithmetic/PI015FiniteGammaSymbolBridge.lean")
           if args.mode == "local" else
           Path("compat/pi015/PI015ExternalPaperFT.lean"))
    if not src.is_file():
        raise RuntimeError(f"Missing candidate source: {src}")
    if UNFINISHED.search(src.read_text()):
        raise RuntimeError(f"Untrusted/unfinished declaration in {src}")
    if not args.olean.is_file() or args.olean.stat().st_size == 0:
        raise RuntimeError(f"Missing compiled .olean: {args.olean}")
    axioms = check_axioms(args.log, NAMES[args.mode])

    report = {
        "status": f"PASS_PI015_{args.mode.upper()}_ONLY",
        "local_pi_commit": git_head(Path(".")),
        "mode": args.mode,
        "source_lock": sources,
        "candidate_source_sha": blob_sha(src.read_bytes()),
        "compiled_olean_sha256": hashlib.sha256(
            args.olean.read_bytes()
        ).hexdigest(),
        "compiled_olean_size": args.olean.stat().st_size,
        "axiom_records": axioms,
        "allowed_axioms": sorted(ALLOWED),
        "NOT_certified": [
            "both local and upstream toolchains have a common imported environment",
            "literal Weil-Lab PI007 kernel is a term in the upstream Zeta23 compiled module",
            "source-bound original IV011 Gamma inverse transform",
            "Masullo operator trace or diagonal contact extension",
            "Weil positivity, RH or GRH",
        ],
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"PI015 strict {args.mode} source/object/axiom audit: PASS")
    print(f"Receipt: {args.out}")


if __name__ == "__main__":
    main()
