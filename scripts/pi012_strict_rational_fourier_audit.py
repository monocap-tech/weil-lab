#!/usr/bin/env python3
"""PI012 exact direct Lean source, binary and standard-axiom custody audit.

Run after actual lake builds and direct lake env lean source evaluations.
This does not prove the PI008 finite Gamma identification, the full inverse
Gamma transform, Masullo's global trace, or RH/GRH.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

MODS = {
    "PI012ComplexRationalIdentity": (
        "pi012Denominator_pos",
        "pi012ComplexShiftMinus_ne_zero",
        "pi012ComplexShiftPlus_ne_zero",
        "pi012ReciprocalPair",
        "pi012ImaginaryShift_sq",
        "pi012FourierReciprocalClosed",
    ),
    "PI012SourceFourierAtom": (
        "pi012SourceFractionsClosed",
        "pi012WholeLineFourierClosed",
    ),
}
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
LINE = re.compile(
    r"(?m)^(?P<decl>WeilDefect\.[A-Za-z_][A-Za-z_0-9']*) "
    r"(?:(?P<none>does not depend on any axioms)"
    r"|depends on axioms:\s*\[(?P<axioms>[^\]]*)\])\s*$"
)
UNFINISHED = re.compile(r"(?m)^\s*(?:axiom|opaque|sorry|admit)\b")


def blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def inspect(mod: str, theorems: tuple[str, ...], audit_dir: Path) -> dict:
    source=Path("WeilDefect/Arithmetic")/(mod+".lean")
    obj=Path(".lake/build/lib/lean/WeilDefect/Arithmetic")/(mod+".olean")
    log=audit_dir/(mod+"-axioms.log")
    for p in (source,obj,log):
        if not p.is_file() or p.stat().st_size==0:
            raise RuntimeError(f"Required source/object/log missing: {p}")
    raw=source.read_bytes()
    if UNFINISHED.search(raw.decode()):
        raise RuntimeError(f"Unaccepted declaration in {source}")
    output=log.read_text()
    if re.search(r"(?mi)(?:^error:|:\d+:\d+: error:)", output):
        raise RuntimeError(f"Direct Lean compiler error in {log}")
    found={}
    for m in LINE.finditer(output):
        name=m.group("decl")
        if name in found:
            raise RuntimeError(f"Duplicate axiom record: {name}")
        text=m.group("axioms")
        axioms=[] if text is None or not text.strip() else [x.strip() for x in text.split(",")]
        if set(axioms)-ALLOWED:
            raise RuntimeError(f"{name}: forbidden axioms {sorted(set(axioms)-ALLOWED)}")
        found[name]=axioms
    expected={f"WeilDefect.{v}" for v in theorems}
    if set(found)!=expected:
        raise RuntimeError(
            f"Bad {mod} axiom coverage: missing {sorted(expected-set(found))}; "
            f"unexpected {sorted(set(found)-expected)}"
        )
    return {
        "source":str(source),
        "source_git_blob_sha":blob_sha(raw),
        "olean":str(obj),
        "olean_size":obj.stat().st_size,
        "olean_sha256":hashlib.sha256(obj.read_bytes()).hexdigest(),
        "axiom_log":str(log),
        "declarations":found,
    }


def main() -> None:
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("--audit-dir",type=Path,default=Path("pi012-audit"))
    parser.add_argument("--receipt",type=Path,default=Path("pi012-audit/receipt.json"))
    args=parser.parse_args()

    if "leanprover/lean4:v4.34.0" not in Path("lean-toolchain").read_text():
        raise RuntimeError("Unexpected Lean toolchain")
    if 'rev = "v4.34.0"' not in Path("lakefile.toml").read_text():
        raise RuntimeError("Unexpected Mathlib pin")

    pi10=Path("WeilDefect/Arithmetic/PI010FourierHalflineAtom.lean")
    pi11=Path("WeilDefect/Arithmetic/PI011WholeLineFourierAtom.lean")
    for path in (pi10,pi11):
        if not path.is_file():
            raise RuntimeError(f"Missing transitive source {path}")
    for module in ("PI010FourierHalflineAtom","PI011WholeLineFourierAtom"):
        o=Path(".lake/build/lib/lean/WeilDefect/Arithmetic")/(module+".olean")
        if not o.is_file() or o.stat().st_size==0:
            raise RuntimeError(f"Missing transitive compiled object {o}")

    evidence={mod:inspect(mod,names,args.audit_dir) for mod,names in MODS.items()}
    receipt={
        "status":"PASS_PI012_EIGHT_LEAN_CANDIDATES_ONLY",
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),
        "checked_out_commit":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),
        "allowed_axioms":sorted(ALLOWED),
        "lean_toolchain":"v4.34.0",
        "mathlib":"v4.34.0",
        "pi010_source_blob":blob_sha(pi10.read_bytes()),
        "pi011_source_blob":blob_sha(pi11.read_bytes()),
        "modules":evidence,
        "NOT_certified":[
            "PI008 rational Gamma atom cast theorem in Lean",
            "finite Fourier transform / inverse Fourier normalization",
            "literal original IV011 signed Gamma transport",
            "Masullo operator trace and diagonal contact term",
            "global Weil positivity, RH or GRH",
        ],
    }
    args.receipt.parent.mkdir(parents=True,exist_ok=True)
    args.receipt.write_text(json.dumps(receipt,sort_keys=True,indent=2)+"\n")
    print("PI012 direct Lean object and eight-theorem standard-axiom audit: PASS")


if __name__=="__main__":
    main()
