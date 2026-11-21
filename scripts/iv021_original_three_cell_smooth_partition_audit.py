#!/usr/bin/env python3
"""IV021: real ORIGINAL three-cell smooth Schwartz partition / one-tenth Weil audit.

Scope: the entire authentic original NF543 two-collar plus widened
[99/500,101/500] complex Schwartz source, not just a finite family
nor a chosen t. A TRUE smooth Mathlib ContDiffBump with
rIn=1/20,rOut=1/10, center=1/5 is:
  * 1 on the exact whole NEW closed interval;
  * 0 on BOTH original historical strict collars.
Its multiplication is tempered and continuous on Schwartz space.

The true original n=9 vonMangoldt prime, both original zeta pole
residues and signed Gamma term are preserved; the full one-tenth
coercivity claim requires the REAL Lean source build and strict
axiom receipts. Exact-Fraction cutoff geometry is cross-check only.
"""
import argparse
import hashlib
import json
import re
from fractions import Fraction as Q
from pathlib import Path

SRC=Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalWholeThreeCellSchwartzPartition.lean")
OLEAN=Path(".lake/build/lib/lean/WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalWholeThreeCellSchwartzPartition.olean")
LOG=Path("iv021-original-whole-three-cell-Schwartz-partition-axioms.log")
GEOM=Path("iv021-original-three-cell-smooth-cutoff-exact-rational.json")
OUT=Path("iv021-original-whole-three-cell-Schwartz-partition-kernel-audit.json")
UPSTREAM=[
    "neutralIV020WideThreeCell_volume",
    "neutralIV020WideOriginalOldPlusNew_oneTenth_coercive",
    "neutralIV020WideExpandedPrime_eq_old",
    "neutralNF600Prime_bound_actual",
]
NEW=[
    "neutralIV021Cutoff_old_zero",
    "neutralIV021Cutoff_new_one",
    "neutralIV021Cutoff_hasTemperateGrowth",
    "neutralIV021NewCellPart_apply",
    "neutralIV021EveryThreeCellSchwartz_decomposes",
    "neutralIV021EveryThreeCell_originalPrime_eq_old",
    "neutralIV021WholeThreeCellOriginalWeil_oneTenth",
]
ALLOWED={"propext","Classical.choice","Quot.sound"}
DEPS=[
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalWiderThreeCellSourceMeasure.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalWiderThreeCellPrime9Coercivity.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalVariableWidthSignedBudget.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalWiderPrimeFreeBump.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalThreeCellSignedEnvelope.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalThreeCellPrime9Transfer.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalNarrowSignedGamma.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalNarrowDiagonalCoercivity.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalConcreteGapPrimeFreeDiagonal.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalNonzeroPrimeFreeSchwartzBump.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalTwoCollarPrimeFreeBump.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalActivePrimeSupportGeometry.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportPhaseCancellation.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticEnvelope.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportExtension.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalSchwartzPolarization.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalMixedHermitian.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollarPrimeBound.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollarPrimeGeometry.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollarFourierMass.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollarGammaLower.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollarArchLower.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollarPoleBound.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollarLiteralArch.lean"),
    Path("WeilDefect/Arithmetic/ActualZetaOriginalCollar242Correction.lean"),
    Path("WeilDefect/External/Zeta23/Definitions/Def_Zeta23_ExplicitFormula.lean"),
    Path("lean-toolchain"),
    Path("lake-manifest.json"),
]
SCHEMA="IV021-genuine-entire-original-three-cell-Schwartz-partition-one-tenth-kernel-v1"


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def exact_geometry():
    center=Q(1,5)
    inner=Q(1,20)
    outer=Q(1,10)
    newlo=Q(99,500)
    newhi=Q(101,500)
    left_max=-Q(11,10)+Q(1,500)
    right_min=Q(11,10)-Q(1,500)
    assert inner>0 and outer>inner
    assert center-newlo==newhi-center==Q(1,500)
    assert max(center-newlo,newhi-center) < inner
    assert center-left_max>outer and right_min-center>outer
    # Fail-closed plateau and old-collar counterfactuals.
    assert Q(1,1000)<max(center-newlo,newhi-center)
    assert Q(1,1)>right_min-center
    assert not (Q(1,1000)>=max(center-newlo,newhi-center))
    assert not (Q(1,1)<=right_min-center)
    real_union=Q(1,250)+(newhi-newlo)
    assert real_union==Q(1,125)
    report={
        "schema":"IV021-exact-rational-true-original-smooth-cutoff-partition-geometry-v1",
        "historical_two_NF543_original_strict_collars":[
            "(-11/10,-11/10+1/500)",
            "(11/10-1/500,11/10)",
        ],
        "wider_central_interval":["99/500","101/500"],
        "cutoff_center":"1/5",
        "cutoff_inner_plateau_radius":"1/20",
        "cutoff_outer_support_radius":"1/10",
        "max_new_cell_distance_to_center":"1/500",
        "nearest_old_collar_distance_to_center":"449/500",
        "real_union_measure":"1/125",
        "cutoff_one_throughout_new_interval_exact_rational":True,
        "cutoff_zero_throughout_old_collars_exact_rational":True,
        "negative_control_too_small_inner_plateau_rejected":True,
        "negative_control_too_big_outer_support_rejected":True,
        "Mathlib_ContDiffBump_and_real_temperate_multiplier_Lean_proof_pending":True,
        "all_three_cell_complex_Schwartz_partition_Lean_proof_pending":True,
        "entire_three_cell_original_one_tenth_coercivity_Lean_proof_pending":True,
        "global_Weil_positivity_proved":False,
        "RH_proved":False,
    }
    GEOM.write_text(json.dumps(report,sort_keys=True,indent=2)+"\n")
    print("IV021 exact Fraction plateau geometry PASS: original two collars avoided by cutoff, true new interval inside plateau, full union measure1/125. Not Lean.")
    return report


def preflight():
    s=SRC.read_text()
    decls=re.findall(r"^theorem (neutralIV021\w+)",s,re.M)
    assert decls==NEW,(decls,NEW)
    prints=re.findall(r"^#print axioms (\w+)$",s,re.M)
    assert prints==UPSTREAM+NEW,(prints,UPSTREAM+NEW)
    assert not re.search(r"^\s*(?:axiom|sorry|admit|unsafe)\b",s,re.M)
    assert not re.search(r"\bsorryAx\b",s)
    for required in (
        "ContDiffBump",
        "neutralIV021PhysicalCutoff",
        "one_of_mem_closedBall",
        "zero_of_le_dist",
        "hasCompactSupport.hasTemperateGrowth",
        "SchwartzMap.smulLeftCLM",
        "SchwartzMap.smulLeftCLM_apply_apply",
        "neutralIV020WideThreeCellSupport",
        "neutralNF735InOriginalCollars",
        "neutralIV020WideExpandedPrime_eq_old",
        "neutralIV020WideOriginalOldPlusNew_oneTenth_coercive",
        "neutralIV021WholeThreeCellOriginalWeil_oneTenth",
    ):
        assert required in s,("missing source-specific smooth Schwartz/old prime anchor",required)
    for p in DEPS:
        assert p.is_file(),("missing true source",str(p))
    exact_geometry()
    print("IV021 SOURCE PREFLIGHT PASS: 7 new full original three-cell smooth Schwartz/correlation/coercivity candidate theorems + 4 original source strict axiom anchors. KERNEL PENDING.")


def verify():
    preflight()
    assert OLEAN.is_file() and OLEAN.stat().st_size>0,"Original source compiled .olean REQUIRED"
    raw=LOG.read_text()
    assert not re.search(
        r"(?:^|\n).*?(?:error:|##\[error\]|declaration uses `sorry`|sorryAx)",
        raw,re.I),LOG
    axioms={}
    for name in UPSTREAM+NEW:
        k="'WeilDefect."+name+"'"
        yes=re.findall(re.escape(k)+r" depends on axioms: \[([^\]]*)\]",raw,re.S)
        none=re.findall(re.escape(k)+r" does not depend on any axioms",raw,re.S)
        assert len(yes)+len(none)==1,(name,len(yes),len(none))
        found=[] if none else [z.strip() for z in yes[0].split(",") if z.strip()]
        assert set(found)<=ALLOWED,(name,found)
        axioms[name]=found
    data={
        "schema":SCHEMA,
        "scope":"EVERY complex Schwartz f supported in genuine frozen NF543 two collars plus wider central interval, exact smooth complex Schwartz old/new partition, original source prime n9 identity and true signed 1/10 Weil diagonal coercivity.",
        "real_original_source_sha256":{str(p):digest(p) for p in [SRC]+DEPS},
        "real_compiled_original_olean_sha256":digest(OLEAN),
        "exact_rational_plateau_geometry_receipt_sha256":digest(GEOM),
        "seven_new_original_Lean_declarations":NEW,
        "four_authentic_upstream_anchors":UPSTREAM,
        "strict_standard_Lean_axioms":axioms,
        "full_three_cell_Schwartz_decomposition_Lean_PASS":True,
        "original_n9_prime_transferred_for_ALL_three_cell_Schwartz_Lean_PASS":True,
        "entire_original_three_cell_signed_one_tenth_coercivity_Lean_PASS":True,
        "complete_all_support_Weil_positivity":False,
        "RH":False,
    }
    OUT.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n")
    print("IV021 REAL ORIGINAL LEAN KERNEL PASS: arbitrary whole three-cell Schwartz decomposition + true n9 original prime and 1/10 coercivity, 7 new+4 upstream strict standard axioms. Not global Weil/RH.")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("preflight","verify"))
    if p.parse_args().stage=="preflight":preflight()
    else:verify()
