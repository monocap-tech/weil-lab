#!/usr/bin/env python3
"""PI016 fail-closed common-graph Zeta23 source and Lean kernel custody.

Do not call this before an actual successful source-exact local Lean 4.34
compilation of upstream Zeta23.Defs plus both PI016 modules. This is
NOT evidence that the upstream's native Lean 4.33 objects are interchangeable
with 4.34 objects; it tests a new unchanged-source compilation in 4.34.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

UPSTREAM_ROOT = "16a5ce41304fcdaea4e0be7c132e1c361dc26da5"
UPSTREAM_DEFS_GIT_BLOB = "8024700cbfefb54d763b487afa84c03fef58a550"
UPSTREAM_TOOLCHAIN = "leanprover/lean4:v4.33.0-rc2"
UPSTREAM_MATHLIB_SHA = "51e6992efd06126df61a496bebf8f49482a4e129"
LOCAL_TOOLCHAIN = "leanprover/lean4:v4.34.0"
LOCAL_MATHLIB_SHA = "5ed2965256430c3649e86755f9576b54eca72435"
EXPECTED = {
    "PI016ImportedPaperFTCore": {
        "WeilDefect.pi016ImportedPaperFT_pi007_unfold",
        "WeilDefect.pi016ImportedPaperFT_pi007_complex",
    },
    "PI016ImportedFiniteGamma": {
        "WeilDefect.pi016ImportedPaperFT_eq_localModel",
        "WeilDefect.pi016ImportedPaperFT_finiteGammaSum",
        "WeilDefect.pi016FiniteGammaSymbol_eq_importedPaperFT",
    },
}
TRANSITIVE = [
    "PI007FiniteGammaKernel",
    "PI008FiniteDigammaSymbol",
    "PI010FourierHalflineAtom",
    "PI011WholeLineFourierAtom",
    "PI012ComplexRationalIdentity",
    "PI012SourceFourierAtom",
    "PI013GammaAtomCast",
    "PI013FiniteFourierSum",
    "PI014KernelCharacterBridge",
    "PI015FiniteGammaSymbolBridge",
]
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
AXIOM_LINE = re.compile(
    r"(?m)^(?P<name>WeilDefect\.[A-Za-z_][A-Za-z_0-9']*) "
    r"(?:(?P<none>does not depend on any axioms)"
    r"|depends on axioms:\s*\[(?P<axioms>[^\]]*)\])\s*$"
)
UNSAFE = re.compile(r"(?m)^\s*(?:axiom|opaque|sorry|admit)\b")
LITERAL_FT = (
    "def paperFT (f : ℝ → ℂ) (z : ℂ) : ℂ := "
    "∫ u : ℝ, f u * Complex.exp (Complex.I * z * (u : ℂ))"
)


def git_head(path: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(path), "rev-parse", "HEAD"], text=True
    ).strip()


def git_blob(raw: bytes) -> str:
    return hashlib.sha1(
        b"blob " + str(len(raw)).encode() + b"\0" + raw
    ).hexdigest()


def require_file(path: Path) -> bytes:
    if not path.is_file() or path.stat().st_size == 0:
        raise RuntimeError(f"Required nonempty source or compiled object absent: {path}")
    return path.read_bytes()


def object_record(path: Path) -> dict:
    data = require_file(path)
    return {"path": str(path), "size": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def axiom_record(path: Path, required: set[str]) -> dict:
    log = require_file(path).decode("utf-8")
    if re.search(r"(?mi)(?:^error:|:\d+:\d+: error:)", log):
        raise RuntimeError(f"Lean errors in source axiom log: {path}")
    found = {}
    for m in AXIOM_LINE.finditer(log):
        name = m.group("name")
        if name in found:
            raise RuntimeError(f"Duplicated axiom receipt: {name}")
        raw = m.group("axioms")
        axioms = [] if raw is None or not raw.strip() else [
            t.strip() for t in raw.split(",")
        ]
        if set(axioms) - ALLOWED:
            raise RuntimeError(f"Nonstandard axioms on {name}: {axioms}")
        found[name] = axioms
    if set(found) != required:
        raise RuntimeError(
            f"{path}: missing {sorted(required - set(found))}; "
            f"extra {sorted(set(found) - required)}"
        )
    return found


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--upstream", type=Path, default=Path("pi016-upstream"))
    p.add_argument("--logs", type=Path, default=Path("pi016-audit"))
    p.add_argument("--out", type=Path, default=Path("pi016-audit/receipt.json"))
    p.add_argument("--stage", choices=("core", "full"), default="full")
    args = p.parse_args()

    if Path("lean-toolchain").read_text().strip() != LOCAL_TOOLCHAIN:
        raise RuntimeError("Wrong Weil-Lab local Lean toolchain")
    if 'rev = "v4.34.0"' not in Path("lakefile.toml").read_text():
        raise RuntimeError("Wrong Weil-Lab Mathlib tag")
    local_mathlib = Path(".lake/packages/mathlib")
    if not local_mathlib.is_dir() or git_head(local_mathlib) != LOCAL_MATHLIB_SHA:
        raise RuntimeError("Actual local Mathlib checkout differs from v4.34.0")
    if git_head(args.upstream) != UPSTREAM_ROOT:
        raise RuntimeError("External upstream root commit SHA differs")
    upstream_toolchain = args.upstream / "zeta23/lean-toolchain"
    if require_file(upstream_toolchain).decode().strip() != UPSTREAM_TOOLCHAIN:
        raise RuntimeError("Original upstream toolchain pin differs")
    upstream_lake = args.upstream / "zeta23/lakefile.toml"
    if UPSTREAM_MATHLIB_SHA not in require_file(upstream_lake).decode():
        raise RuntimeError("Original upstream Mathlib source rev differs")
    upstream_defs = args.upstream / "zeta23/Zeta23/Defs.lean"
    raw_defs = require_file(upstream_defs)
    if git_blob(raw_defs) != UPSTREAM_DEFS_GIT_BLOB:
        raise RuntimeError("Original external Zeta23/Defs source bytes changed")
    if LITERAL_FT not in raw_defs.decode():
        raise RuntimeError("Literal imported paperFT is not the original +iru formula")

    build_root = Path(".lake/build/lib/lean")
    defs_obj = build_root / "Zeta23/Defs.olean"
    core_obj = build_root / "WeilDefect/Arithmetic/PI016ImportedPaperFTCore.olean"
    full_obj = build_root / "WeilDefect/Arithmetic/PI016ImportedFiniteGamma.olean"
    compiled = {
        "source_original_upstream_Defs_under_local_lean": object_record(defs_obj),
        "PI016_imported_core": object_record(core_obj),
    }
    if args.stage == "full":
        compiled["PI016_complete_finite_dictionary"] = object_record(full_obj)

    dependencies = {}
    for module in (TRANSITIVE if args.stage == "full" else ["PI007FiniteGammaKernel"]):
        path = build_root / f"WeilDefect/Arithmetic/{module}.olean"
        dependencies[module] = object_record(path)

    source_info = {}
    axiom_info = {}
    for module, required in EXPECTED.items():
        if args.stage == "core" and module != "PI016ImportedPaperFTCore":
            continue
        source = Path("WeilDefect/Arithmetic") / f"{module}.lean"
        raw = require_file(source)
        if UNSAFE.search(raw.decode()):
            raise RuntimeError(f"Untrusted unfinished source: {source}")
        if "import Zeta23.Defs" not in raw.decode() and module == "PI016ImportedPaperFTCore":
            raise RuntimeError("Direct original Zeta23.Defs import is missing")
        source_info[module] = {"path": str(source), "git_blob": git_blob(raw)}
        log_path = args.logs / f"{module}-axioms.log"
        axiom_info[module] = axiom_record(log_path, required)

    report = {
        "status": f"PASS_PI016_{args.stage.upper()}_UNCHANGED_UPSTREAM_SOURCE_IN_LOCAL_LEAN_ONLY",
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "current_weil_lab_commit": git_head(Path(".")),
        "upstream_root_commit": UPSTREAM_ROOT,
        "upstream_defs_git_blob": UPSTREAM_DEFS_GIT_BLOB,
        "upstream_native_lean": UPSTREAM_TOOLCHAIN,
        "upstream_native_mathlib": UPSTREAM_MATHLIB_SHA,
        "common_compiler_lean": LOCAL_TOOLCHAIN,
        "common_compiler_mathlib": LOCAL_MATHLIB_SHA,
        "actual_compiled_objects": compiled,
        "transitive_compiled_lean_objects": dependencies,
        "source_git_blobs": source_info,
        "strict_axiom_records": axiom_info,
        "allowed_axioms": sorted(ALLOWED),
        "explicit_scope": (
            "This checks unchanged Zeta23/Defs.lean compiled under the local "
            "4.34.0 toolchain, NOT reuse of 4.33.0-rc2 olean files."
        ),
        "NOT_certified": [
            "full upstream Zeta23 ExplicitFormula.lean under Lean 4.34.0",
            "actual IV011 neutralIV011OriginalMixedArch Lean source import",
            "inverse Fourier finite pairing and harmonic contact in Lean",
            "source-bound Gamma infinite limit on h(0)=0 in Lean",
            "Masullo independent trace operator, diagonal contact, RH or GRH",
        ],
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print("PI016 DIRECT ONE-TOOLCHAIN SOURCE/LEAN/AXIOM AUDIT: PASS")
    print(f"Source certificate stage: {args.stage}")
    print("The authentic unchanged upstream Zeta23.Defs source was compiled")
    print("in the SAME local 4.34.0 environment as the literal PI007/PI008/PI014 terms.")


if __name__ == "__main__":
    main()
