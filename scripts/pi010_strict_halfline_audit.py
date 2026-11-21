#!/usr/bin/env python3
"""PI010 strict compiled Lean half-line module + axiom audit (fail closed).

This script MUST be run only after both direct lake build and direct source
lean invocation succeed. A source file or job status alone is insufficient.
It certifies ONLY the five named half-line lemmas, NOT the full real-line atom,
the original IV011 Gamma bridge, Masullo's operator trace, RH or GRH.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
from pathlib import Path

MODULE="PI010FourierHalflineAtom"
DECLS={
    "WeilDefect.pi010PositiveExponent_re",
    "WeilDefect.pi010NegativeExponent_re",
    "WeilDefect.pi010PositiveHalflineIntegral",
    "WeilDefect.pi010NegativeHalflineIntegral",
    "WeilDefect.pi010HalflineIntegralPair",
}
ACCEPTED={"propext","Classical.choice","Quot.sound"}
PRINT = re.compile(
    r"(?m)^(?P<name>WeilDefect\.[A-Za-z_][A-Za-z_0-9']*) "
    r"(?:(?P<none>does not depend on any axioms)"
    r"|depends on axioms:\s*\[(?P<axioms>[^\]]*)\])\s*$"
)
UNTRUSTED = re.compile(r"(?m)^\s*(?:axiom|sorry|admit|opaque)\b")


def sha256(p:Path)->str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def git_blob(p:Path)->str:
    b=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--log",type=Path,default=Path("pi010-audit/PI010FourierHalflineAtom-axioms.log"))
    ap.add_argument("--receipt",type=Path,default=Path("pi010-audit/receipt.json"))
    args=ap.parse_args()

    src=Path("WeilDefect/Arithmetic")/(MODULE+".lean")
    obj=Path(".lake/build/lib/lean/WeilDefect/Arithmetic")/(MODULE+".olean")
    if not src.is_file() or not obj.is_file() or obj.stat().st_size==0:
        raise RuntimeError("Missing Lean source or nonempty actual .olean")
    if not args.log.is_file() or args.log.stat().st_size==0:
        raise RuntimeError("Missing actual direct Lean axiom log")
    if 'rev = "v4.34.0"' not in Path("lakefile.toml").read_text():
        raise RuntimeError("Pinned mathlib version drift")
    if "leanprover/lean4:v4.34.0" not in Path("lean-toolchain").read_text():
        raise RuntimeError("Pinned Lean toolchain drift")
    if UNTRUSTED.search(src.read_text()):
        raise RuntimeError("Project axiom, opaque or unfinished proof")
    log=args.log.read_text()
    if re.search(r"(?mi)(?:^error:|:\d+:\d+: error:)",log):
        raise RuntimeError("Lean source compiler log has an error")
    found={}
    for m in PRINT.finditer(log):
        name=m.group("name")
        if name in found:
            raise RuntimeError("Duplicate axiom entry for "+name)
        raw=m.group("axioms")
        axs=[] if raw is None or not raw.strip() else [v.strip() for v in raw.split(",")]
        if not set(axs).issubset(ACCEPTED):
            raise RuntimeError("Unaccepted Lean axiom(s): "+name+" "+str(axs))
        found[name]=axs
    if set(found)!=DECLS:
        raise RuntimeError("Missing/extra declarations: "+
                           str(sorted(DECLS-set(found)))+" / "+str(sorted(set(found)-DECLS)))
    commit=subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip()
    receipt={
        "status":"PASS_DIRECT_PI010_HALFLINE_LEAN_ONLY",
        "commit_sha":commit,
        "source_blob":git_blob(src),
        "source":str(src),
        "olean":str(obj),
        "olean_sha256":sha256(obj),
        "olean_size":obj.stat().st_size,
        "axiom_log":str(args.log),
        "theorems":found,
        "accepted_axioms":sorted(ACCEPTED),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),
        "NOT_certified":["whole-real-line Fourier exponential atom",
                         "literal IV011 Gamma inverse transform",
                         "Masullo nuclear operator trace and diagonal extension",
                         "global Weil positivity, RH and GRH"],
    }
    args.receipt.parent.mkdir(parents=True,exist_ok=True)
    args.receipt.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print("PI010 SOURCE/LEAN/AXIOM AUDIT: PASS (five half-line lemmas only)")


if __name__=="__main__":
    main()
