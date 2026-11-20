#!/usr/bin/env python3
"""NF730 exact pure Fin242 four-quad half-cover source and kernel axiom audit.

The statements are logical implications from four range hypotheses, not
original HD/A numerical gate certifications.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path
ALLOWED={"propext","Classical.choice","Quot.sound"}
ROOT=Path("WeilDefect/Arithmetic")

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def source(side):
    assert side in ("Left","Right")
    path=ROOT/f"ActualZetaOriginalPhysicalEightQuad{side}Cover.lean"
    s=path.read_text()
    name=f"neutralNF730{side}OfFourQuads"
    assert s.startswith("import Mathlib.Tactic\n")
    assert re.findall(r"^theorem (neutralNF730\w+)",s,re.M)==[name]
    assert not re.search(r"\b(sorry|admit|axiom|unsafe)\b",s)
    parts=(0,4,8,12) if side=="Left" else (16,20,24,28)
    for b in parts:
        hi=min((b+4)*8,242)
        wanted=f"(h{b:03d} : ∀ i : Fin 242, {b*8} ≤ i.val → i.val < {hi} → P i)"
        assert wanted in s,(side,b)
        assert f"exact h{b:03d} i (by omega)" in s,(side,b)
    assert f"#print axioms {name}" in s
    print(f"NF730 pure four-quad {side} Fin242 structural preflight PASS; Lean kernel acceptance separate")
    return name,path

def verify(side):
    name,path=source(side)
    log=Path(f"nf730-pure-{side.lower()}-axioms.log").read_text()
    mx=re.findall(rf"'WeilDefect\.{name}' depends on axioms: \[([^\]]*)\]",log)
    no=re.findall(rf"'WeilDefect\.{name}' does not depend on any axioms",log)
    assert len(mx)+len(no)==1,(name,mx,no)
    found=[x.strip() for x in mx[0].split(",") if x.strip()] if mx else []
    assert set(found)<=ALLOWED,(name,found)
    assert "error:" not in log.lower()
    receipt={
        "schema":"NF730-4-quad-pure-logic-Lean-source-kernel-audit-v1",
        "side":side,
        "theorem":name,
        "source_sha256":sha(path),
        "axioms":found,
        "range":[0,128] if side=="Left" else [128,242],
        "original_numeric_gate_truth_asserted":False,
        "status":"Lean kernel PASS; strict standard axiom audit PASS"
    }
    Path(f"nf730-pure-{side.lower()}-audit.json").write_text(
        json.dumps(receipt,indent=2,sort_keys=True)+"\n")
    print(f"NF730 {side}: independent four-original-coordinate-quad pure logical Lean proof PASS; original numerical half proof NOT YET supplied")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("source","verify"))
    p.add_argument("--side",choices=("Left","Right"),required=True)
    a=p.parse_args()
    source(a.side) if a.stage=="source" else verify(a.side)
