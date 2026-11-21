#!/usr/bin/env python3
"""PI014 strict locally compiled Lean theorem and dependency source audit.

Certifies only three named local PI014 theorem candidates AFTER a real direct
lake build and direct lake env lean axiom dump. This cannot certify the
external Zeta23.paperFT definition because Zeta23 is not an import on the
PI-only Lake graph.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess
import os

NAME="PI014KernelCharacterBridge"
PREVIOUS=("PI007FiniteGammaKernel","PI008FiniteDigammaSymbol",
          "PI010FourierHalflineAtom","PI011WholeLineFourierAtom",
          "PI012ComplexRationalIdentity","PI012SourceFourierAtom",
          "PI013GammaAtomCast","PI013FiniteFourierSum")
DECLARATIONS={
    "WeilDefect.pi014PhysicalAtom_factor",
    "WeilDefect.pi014FiniteDamped_eq_kernelCharacter",
    "WeilDefect.pi014PaperFTModel_finite",
}
ALLOWED={"propext","Classical.choice","Quot.sound"}
AXIOM=re.compile(
    r"(?m)^(?P<name>WeilDefect\.[A-Za-z_][A-Za-z_0-9']*) "
    r"(?:(?P<none>does not depend on any axioms)"
    r"|depends on axioms:\s*\[(?P<axioms>[^\]]*)\])\s*$"
)
UNSAFE=re.compile(r"(?m)^\s*(?:axiom|sorry|admit|opaque)\b")


def path_for(mod: str,extension:str) -> Path:
    if extension=="lean":
        return Path("WeilDefect/Arithmetic")/(mod+".lean")
    return Path(".lake/build/lib/lean/WeilDefect/Arithmetic")/(mod+".olean")


def source_blob(raw:bytes) -> str:
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def main() -> None:
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument("--logs",type=Path,default=Path("pi014-audit/PI014KernelCharacterBridge-axioms.log"))
    p.add_argument("--out",type=Path,default=Path("pi014-audit/receipt.json"))
    a=p.parse_args()

    if "leanprover/lean4:v4.34.0" not in Path("lean-toolchain").read_text():
        raise RuntimeError("Wrong Lean pin")
    if 'rev = "v4.34.0"' not in Path("lakefile.toml").read_text():
        raise RuntimeError("Wrong local Mathlib pin")
    data={}
    for mod in (*PREVIOUS,NAME):
        src=path_for(mod,"lean")
        obj=path_for(mod,"olean")
        if any(not t.is_file() or t.stat().st_size==0 for t in (src,obj)):
            raise RuntimeError(f"Missing source or true compiled olean for {mod}")
        raw=src.read_bytes()
        if UNSAFE.search(raw.decode("utf-8")):
            raise RuntimeError(f"Untrusted project declaration in {mod}")
        data[mod]={
            "source_git_blob":source_blob(raw),
            "olean_sha256":hashlib.sha256(obj.read_bytes()).hexdigest(),
            "olean_size":obj.stat().st_size,
        }

    if not a.logs.is_file() or a.logs.stat().st_size==0:
        raise RuntimeError("Missing direct PI014 source axiom log")
    log=a.logs.read_text()
    if re.search(r"(?mi)(?:^error:|:\d+:\d+: error:)",log):
        raise RuntimeError("PI014 source Lean error")
    found={}
    for m in AXIOM.finditer(log):
        name=m.group("name")
        if name in found:
            raise RuntimeError("Duplicate theorem axiom record")
        raw=m.group("axioms")
        axioms=[] if not raw or not raw.strip() else [s.strip() for s in raw.split(",")]
        if set(axioms)-ALLOWED:
            raise RuntimeError(f"Nonstandard axiom in {name}: {axioms}")
        found[name]=axioms
    if set(found)!=DECLARATIONS:
        raise RuntimeError(
            f"Missing PI014 axiom records: {sorted(DECLARATIONS-set(found))}, "
            f"unexpected: {sorted(set(found)-DECLARATIONS)}"
        )
    report={
        "status":"PASS_PI014_THREE_LOCAL_THEOREMS_ONLY",
        "checked_out_commit":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),
        "axioms":found,
        "modules":data,
        "external_Zeta23_import":"NOT_PRESENT_NOT_CERTIFIED",
        "NOT_certified":[
          "actual imported Zeta23.paperFT theorem",
          "compatible external Mathlib dependency",
          "finite Gamma inverse pairing with 1/(2*pi) and contact",
          "IV011 original source import and infinite limit",
          "Masullo operator diagonal extension, Weil positivity or RH"
        ],
    }
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print("PI014 direct local Lean kernel source and standard-axiom audit: PASS")


if __name__=="__main__":
    main()
