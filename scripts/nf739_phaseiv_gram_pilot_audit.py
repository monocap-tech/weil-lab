#!/usr/bin/env python3
"""NF739: strictly distinguish generic exact Gram algebra from actual Weil EF.

Two independent, Mathlib-only Lean modules:
1. full complex Hermitian 2x2 quadratic-form PSD from |m|^2 <= ab,
   written with real/imag coordinates to fix orientation exactly;
2. 3x3 real countermodel: each 2-coordinate restriction PSD but
   full three-coordinate span has negative energy.

No numerical original data or zeta Weil diagonal/offdiagonal facts are
inserted. Source preflight is not equivalent to kernel acceptance.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT=Path("WeilDefect/Arithmetic")
SOURCES={
    "complex":ROOT/"ActualZetaPhaseIVHermitianTwoBlockPSD.lean",
    "three":ROOT/"ActualZetaPhaseIVThreeSupportObstruction.lean",
}
NAMES={
    "complex":[
      "neutralNF739HermitianTwoBlockPSD",
      "neutralNF739HermitianTwoBlockExactSquares",
    ],
    "three":[
      "neutralNF739ThreeSupport_pair01_nonnegative",
      "neutralNF739ThreeSupport_pair02_nonnegative",
      "neutralNF739ThreeSupport_pair12_nonnegative",
      "neutralNF739ThreeSupport_all_ones_negative",
      "neutralNF739PairwisePSD_not_fullPSD",
    ],
}
ALLOWED={"propext","Classical.choice","Quot.sound"}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def source(stage):
    assert stage in SOURCES
    path=SOURCES[stage]
    text=path.read_text()
    assert text.startswith("import Mathlib.Tactic\n")
    assert re.findall(r"^theorem (neutralNF739\w+)",text,re.M)==NAMES[stage]
    assert not re.search(r"^\s*(?:sorry|admit|axiom|unsafe)\b",text,re.M)
    assert all("#print axioms "+n in text for n in NAMES[stage])
    assert "Zeta23.EF" not in text
    assert "neutralNF598SmoothWeil" not in text
    if stage=="complex":
        assert "neutralNF739HermitianTwoBlockEnergy" in text
        assert "(hdet : p^2 + q^2 ≤ a*b)" in text
        assert "neutralNF739HermitianTwoBlockExactSquares" in text
        assert "a*b - p^2 - q^2" in text
        assert "by_cases hzero : a = 0" in text
        assert "by_contra hn" in text
    else:
        assert "neutralNF739ThreeSupportCrossModel" in text
        assert "(v : Fin 3 → ℝ)" in text
        assert "neutralNF739ThreeSupport_all_ones_negative" in text
        assert "neutralNF739PairwisePSD_not_fullPSD" in text
        assert all(f"neutralNF739ThreeSupport_pair{s}_nonnegative" in text
                   for s in ("01","02","12"))
    print(f"NF739 {stage}: SOURCE/PREFLIGHT PASS: {len(NAMES[stage])} pure Mathlib exact mixed Gram theorem candidates; no actual original Weil mixed entry, global EF or RH certified")


def parse(log,names):
    got={}
    for name,raw in re.findall(
       r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",log
    ):
        if name in names:
            assert name not in got
            got[name]=[v.strip() for v in raw.split(",") if v.strip()]
    for name in re.findall(
       r"'WeilDefect\.(\w+)' does not depend on any axioms",log
    ):
        if name in names:
            assert name not in got
            got[name]=[]
    assert set(got)==set(names),set(names)-set(got)
    assert all(set(v)<=ALLOWED for v in got.values()),got
    assert not re.search(r"\berror:|\b(?:sorryAx|axiom#)",log,re.I)
    return got


def verify(stage):
    source(stage)
    src=SOURCES[stage]
    obj=Path(".lake/build/lib/lean")/src.with_suffix(".olean")
    assert obj.is_file() and obj.stat().st_size>1024,obj
    log=Path(f"nf739-{stage}-axioms.log").read_text()
    got=parse(log,NAMES[stage])
    r={
      "schema":"NF739-mixed-gram-source-independent-mathlib-lean-v1",
      "stage":stage,
      "source_sha256":sha(src),
      "olean_sha256":sha(obj),
      "theorems":NAMES[stage],
      "standard_axioms":got,
      "all_theorems_Learn_kernel_pass":True,
      "asserts_original_zeta_Weil_form":False,
      "asserts_actual_mixed_prime_pole_archimedean_bounds":False,
      "asserts_global_Weil_positivity":False,
      "asserts_Riemann_Hypothesis":False,
      "scope":(
        "Pure complex-Hermitian 2x2 coefficient-form sufficient PSD under determinant bound; no actual Weil off-diagonal bound"
        if stage=="complex" else
        "Pure real 3x3 countermodel: three pairwise PSD coordinate planes coexist with a negative full 3-vector"
      ),
      "status":"LEAN PASS under standard axioms; no source-specific global Weil theorem"
    }
    Path(f"nf739-{stage}-lean-audit.json").write_text(
      json.dumps(r,indent=2,sort_keys=True)+"\n")
    print(f"NF739 {stage}: {len(NAMES[stage])} actual pure Mathlib Lean theorem kernel PASS under standard axioms, no zeta Weil global positivity or RH")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("complex","three"))
    p.add_argument("action",choices=("source","verify"))
    a=p.parse_args()
    source(a.stage) if a.action=="source" else verify(a.stage)
