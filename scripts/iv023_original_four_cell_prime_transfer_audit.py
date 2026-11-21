#!/usr/bin/env python3
"""IV023 — actual ORIGINAL four-cell Schwartz partition and complete prime transfer.

Source obligations: two real Mathlib smooth cutoff/Schwartz modules, full
authentic original signed zeta van-Mangoldt prime term including surviving
NF600 n=9, exact four-cell 17/2000 source mass and one-sixteenth
candidate original Weil coercivity. No independent spectral equivalence,
no global Weil positivity, no RH.

The independent Fraction receipt checks the exact true four-cell
geometry, the cutoffs, rigorous log(2) shifted-overlap negative control,
and original n9 old-old overlap. It is not a Lean proof. Strict kernel
PASS requires BOTH compiled .olean objects, all 18 new theorem axiom
receipts and eight authentic upstream standard-only source anchors,
zero sorryAx, and SHA-bound source and toolchain.
"""
import argparse
import hashlib
import json
import re
from fractions import Fraction as Q
from pathlib import Path

from iv015_frozen_collar_exact_log_gap import log_bracket, abs_lower

ROOT=Path("WeilDefect/Arithmetic")
M1=ROOT/"ActualZetaPhaseIVOriginalFourCellSmoothSchwartzPartition.lean"
M2=ROOT/"ActualZetaPhaseIVOriginalFourCellPrimeTransferCoercivity.lean"
OLEANS=Path(".lake/build/lib/lean/WeilDefect/Arithmetic")
LOG1=Path("iv023-original-four-cell-schwartz-partition-axioms.log")
LOG2=Path("iv023-original-four-cell-prime-transfer-coercivity-axioms.log")
EXACT=Path("iv023-original-four-cell-prime-preservation-exact-rational.json")
AUDIT=Path("iv023-original-four-cell-prime-transfer-kernel-audit.json")
ALLOWED={"propext","Classical.choice","Quot.sound"}
SCHEMA="IV023-full-original-four-cell-prime-transfer-and-oneSixteenth-kernel-v1"
UP1=[
 "neutralIV021EveryThreeCellSchwartz_decomposes",
 "neutralIV022FourCell_volume",
]
NEW1=[
 "neutralIV023SecondCutoff_one",
 "neutralIV023SecondCutoff_base_zero",
 "neutralIV023SecondCutoff_hasTemperateGrowth",
 "neutralIV023SecondPart_apply",
 "neutralIV023FourCell_split_threePlusOne",
 "neutralIV023EveryFourCellSchwartz_decomposes",
]
UP2=[
 "neutralIV021EveryThreeCell_originalPrime_eq_old",
 "neutralIV020WideOldMass_le_expandedMass",
 "neutralIV022SecondFrozenTwoCollarActiveGap",
 "neutralIV022FirstSecondActiveGap",
 "neutralIV022SecondSelfActiveGap",
 "neutralIV022FourCell_oneSixteenth_of_originalPrime",
]
NEW2=[
 "neutralIV023BaseSecond_supportedFourCell",
 "neutralIV023BaseSecond_mass_add",
 "neutralIV023BaseMass_le_expandedMass",
 "neutralIV023BaseSecondCorrelation_eq_base_of_threeZeros",
 "neutralIV023ActiveSeparated_add",
 "neutralIV023ThreeCellSecond_activeSeparated",
 "neutralIV023ThreeCellSecond_activeCorrelation_eq",
 "neutralIV023ThreeCellSecond_originalPrime_eq",
 "neutralIV023EveryFourCell_originalPrime_eq_old",
 "neutralIV023OldMass_le_fourCellMass",
 "neutralIV023EveryFourCell_originalPrime_real_bound",
 "neutralIV023WholeFourCellOriginalWeil_oneSixteenth",
]
DEPS=[
 ROOT/"ActualZetaPhaseIVOriginalSecondNewCellPrimeGeometry.lean",
 ROOT/"ActualZetaPhaseIVOriginalFourCellSignedCapacity.lean",
 ROOT/"ActualZetaPhaseIVOriginalWholeThreeCellSchwartzPartition.lean",
 ROOT/"ActualZetaPhaseIVOriginalWiderThreeCellPrime9Coercivity.lean",
 ROOT/"ActualZetaPhaseIVOriginalWiderThreeCellSourceMeasure.lean",
 ROOT/"ActualZetaPhaseIVOriginalVariableWidthSignedBudget.lean",
 ROOT/"ActualZetaPhaseIVOriginalWiderPrimeFreeBump.lean",
 ROOT/"ActualZetaPhaseIVOriginalThreeCellSignedEnvelope.lean",
 ROOT/"ActualZetaPhaseIVOriginalThreeCellPrime9Transfer.lean",
 ROOT/"ActualZetaPhaseIVOriginalNarrowSignedGamma.lean",
 ROOT/"ActualZetaPhaseIVOriginalNarrowDiagonalCoercivity.lean",
 ROOT/"ActualZetaPhaseIVOriginalConcreteGapPrimeFreeDiagonal.lean",
 ROOT/"ActualZetaPhaseIVOriginalNonzeroPrimeFreeSchwartzBump.lean",
 ROOT/"ActualZetaPhaseIVOriginalTwoCollarPrimeFreeBump.lean",
 ROOT/"ActualZetaPhaseIVOriginalActivePrimeSupportGeometry.lean",
 ROOT/"ActualZetaPhaseIVOriginalCrossSupportPhaseCancellation.lean",
 ROOT/"ActualZetaPhaseIVOriginalCrossSupportArithmeticEnvelope.lean",
 ROOT/"ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean",
 ROOT/"ActualZetaPhaseIVOriginalCrossSupportExtension.lean",
 ROOT/"ActualZetaPhaseIVOriginalSchwartzPolarization.lean",
 ROOT/"ActualZetaPhaseIVOriginalMixedHermitian.lean",
 ROOT/"ActualZetaOriginalCollarPrimeBound.lean",
 ROOT/"ActualZetaOriginalCollarPrimeGeometry.lean",
 ROOT/"ActualZetaOriginalCollarFourierMass.lean",
 ROOT/"ActualZetaOriginalCollarGammaLower.lean",
 ROOT/"ActualZetaOriginalCollarArchLower.lean",
 ROOT/"ActualZetaOriginalCollarPoleBound.lean",
 ROOT/"ActualZetaOriginalCollarLiteralArch.lean",
 ROOT/"ActualZetaOriginalCollar242Correction.lean",
 Path("WeilDefect/External/Zeta23/Definitions/Def_Zeta23_ExplicitFormula.lean"),
 Path("scripts/iv015_frozen_collar_exact_log_gap.py"),
 Path("scripts/iv022_original_four_cell_prime_capacity_audit.py"),
 Path("lean-toolchain"),
 Path("lakefile.toml"),
 Path("lake-manifest.json"),
]

def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def frac(q):return f"{q.numerator}/{q.denominator}"

def exact_source_receipt():
    second=Q(-1,5)
    plateau=Q(1,20)
    outer=Q(1,10)
    r2=Q(1,4000)
    secondlo=second-r2
    secondhi=second+r2
    firstlo=Q(99,500)
    firsthi=Q(101,500)
    leftmax=Q(-11,10)+Q(1,500)
    rightmin=Q(11,10)-Q(1,500)
    assert secondhi<firstlo
    assert r2<plateau<outer
    assert second-leftmax>outer
    assert firstlo-second>outer
    assert rightmin-second>outer
    assert secondlo>Q(-11,10)
    assert secondhi<Q(11,10)
    assert firstlo-second==Q(199,500)
    assert second-leftmax==Q(449,500)

    old=Q(1,250)
    first=Q(1,250)
    fourth=2*r2
    width=old+first+fourth
    gamma=Q(11,10)-Q(67,10)*(10*width)
    pole=8*width
    analytic=gamma-pole
    retained_n9=Q(2,5)
    margin=analytic-retained_n9
    assert width==Q(17,2000)
    assert gamma==Q(1061,2000)
    assert pole==Q(17,250)
    assert analytic==Q(37,80)
    assert margin==Q(1,16)

    # Genuine old-old n=9 overlap survives. The full original
    # arithmetic P is NOT zero on arbitrary four-cell tests.
    lo9,hi9=log_bracket(9)
    oldshift=Q(1099,1000)-(-Q(1099,1000))
    overlap9=abs_lower(oldshift-hi9,oldshift-lo9)-Q(2,1000)
    assert overlap9<0,("old n9 incorrectly declared prime-free",overlap9)

    # The same transfer law is NOT true for an arbitrary invented
    # fourth cell: a new support centered at first+693/1000 has
    # genuine n=2 shifted overlap with the first new interval.
    shift=Q(693,1000)
    lo2,hi2=log_bracket(2)
    collision2=abs_lower(shift-hi2,shift-lo2) - (Q(1,500)+r2)
    assert collision2<0,("log2 collision counterexample must fail",collision2)

    # This demonstrates why the full original four-cell transfer is
    # a falsifiable geometry-dependent identity, not a universal
    # invariance law or an arithmetic/spectral isomorphism.
    data={
      "schema":"IV023-full-original-four-cell-arithmetic-compatibility-exact-rational-v1",
      "original_frozen_two_collar_total_measure":frac(old),
      "first_new_physical_interval":"[99/500,101/500]",
      "second_new_physical_interval":[frac(secondlo),frac(secondhi)],
      "second_smooth_cutoff_center":frac(second),
      "second_smooth_cutoff_rIn":frac(plateau),
      "second_smooth_cutoff_rOut":frac(outer),
      "first_to_second_distance_at_nearest_end":frac(firstlo-second),
      "original_left_to_second_distance_at_nearest_end":frac(second-leftmax),
      "second_interval_fits_inner_plateau":True,
      "all_original_three_cells_outside_second_smooth_cutoff":True,
      "total_real_physical_width":frac(width),
      "true_signed_Gamma_lower":frac(gamma),
      "two_original_poles_loss":frac(pole),
      "pole_plus_Gamma_remainder_lower":frac(analytic),
      "surviving_original_n9_prime_allowance":frac(retained_n9),
      "target_whole_four_cell_signed_margin":frac(margin),
      "original_old_n9_prime_shift_overlap_retained":True,
      "negative_control_fake_log2_spaced_fourth_cell_collision_rejected":True,
      "original_prime_preservation_beyond_this_support_NOT_ASSUMED":True,
      "whole_four_cell_Schwartz_partition_Lean_kernel_passed":False,
      "whole_four_cell_original_prime_transfer_Lean_kernel_passed":False,
      "whole_four_cell_original_Weil_coercivity_Lean_kernel_passed":False,
      "independent_arithmetic_or_spectral_equivalence_proved":False,
      "global_Weil_positivity_proved":False,
      "RH_proved":False,
    }
    EXACT.write_text(json.dumps(data,sort_keys=True,indent=2)+"\n")
    print("IV023 EXACT original source geometry PASS: 2 smooth plateau cells, 17/2000 total support, genuine old n9 survivor, log2 collision negative control; signed 1/16 exact rational margin. NOT LEAN.")
    return data

def source_preflight():
    for mod,up,new in ((M1,UP1,NEW1),(M2,UP2,NEW2)):
        source=mod.read_text()
        names=re.findall(r"^theorem (neutralIV023\w+)",source,re.M)
        prints=re.findall(r"^#print axioms (\w+)$",source,re.M)
        assert names==new,(str(mod),"theorem inventory mismatch",names)
        assert prints==up+new,(str(mod),"audit inventory mismatch",prints)
        assert not re.search(r"^\s*(?:axiom|sorry|admit|unsafe)\b",source,re.M),mod
        assert not re.search(r"\bsorryAx\b",source),mod
    a=M1.read_text()
    b=M2.read_text()
    for marker in (
      "ContDiffBump",
      "neutralIV023SecondCutoff_one",
      "neutralIV023SecondCutoff_base_zero",
      "hasCompactSupport.hasTemperateGrowth",
      "SchwartzMap.smulLeftCLM",
      "neutralIV021EveryThreeCellSchwartz_decomposes",
      "neutralIV023EveryFourCellSchwartz_decomposes",
    ):
        assert marker in a,("missing smooth genuine source",marker)
    for marker in (
      "ArithmeticFunction.vonMangoldt",
      "neutralIV011MixedCorrelation_eq_schwartzIntegral",
      "neutralIV011OriginalMixedPrime_eq_finite",
      "neutralIV022SecondFrozenTwoCollarActiveGap",
      "neutralIV022FirstSecondActiveGap",
      "neutralIV022SecondSelfActiveGap",
      "neutralIV021EveryThreeCell_originalPrime_eq_old",
      "neutralNF600Prime_bound_actual",
      "neutralIV022FourCell_oneSixteenth_of_originalPrime",
      "neutralIV023WholeFourCellOriginalWeil_oneSixteenth",
    ):
        assert marker in b,("missing real source prime/coercivity",marker)
    for p in DEPS:assert p.is_file(),("real original upstream source absent",str(p))
    exact_source_receipt()
    print("IV023 ORIGINAL source preflight: 18 new original Schwartz/primes/coercivity Lean theorem CANDIDATES +8 upstream strict axiom anchors, no kernel receipt yet.")

def parse_log(path,names):
    source=path.read_text()
    assert not re.search(r"(?:^|\n).*?(?:error:|##\[error\]|declaration uses `sorry`|sorryAx)",source,re.I),path
    results={}
    for name in names:
        full="'WeilDefect."+name+"'"
        yes=re.findall(re.escape(full)+r" depends on axioms: \[([^\]]*)\]",source,re.S)
        no=re.findall(re.escape(full)+r" does not depend on any axioms",source,re.S)
        assert len(yes)+len(no)==1,(path,name,len(yes),len(no))
        axioms=[] if no else [i.strip() for i in yes[0].split(",") if i.strip()]
        assert set(axioms)<=ALLOWED,(name,axioms)
        results[name]=axioms
    return results

def verify():
    source_preflight()
    objs=[OLEANS/(p.stem+".olean") for p in (M1,M2)]
    for p in objs:
        assert p.is_file() and p.stat().st_size>0,("real compiled .olean REQUIRED",str(p))
    one=parse_log(LOG1,UP1+NEW1)
    two=parse_log(LOG2,UP2+NEW2)
    report={
        "schema":SCHEMA,
        "scope":"EVERY genuine complex Schwartz function supported in the ORIGINAL frozen strict two collars plus first wide [99/500,101/500] and second [-801/4000,-799/4000] new cells: actual smooth three-component partition, genuine complete original prime = old n9 only, signed original Weil 1/16 coercivity.",
        "source_sha256":{str(p):h(p) for p in [M1,M2]+DEPS},
        "compiled_original_Lean_olean_sha256":{str(p):h(p) for p in objs},
        "independent_exact_Fraction_receipt_sha256":h(EXACT),
        "new_original_Lean_proved_theorems":NEW1+NEW2,
        "upstream_original_axiom_anchors":UP1+UP2,
        "standard_only_actual_Lean_axiom_receipts":{**one,**two},
        "every_four_cell_complex_Schwartz_partition_Lean_PASS":True,
        "complete_original_prime_preservation_at_every_four_cell_Schwartz_Lean_PASS":True,
        "true_original_signed_oneSixteenth_whole_four_cell_coercivity_Lean_PASS":True,
        "global_Weil_positivity":False,
        "RH":False,
        "external_spectral_equivalence":False,
    }
    AUDIT.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print("IV023 REAL ORIGINAL SOURCE LEAN KERNEL PASS: two true compiled sources, 18 new +8 upstream standard axioms, actual whole four-cell 1/16 signed Weil restricted coercivity; NOT global Weil/RH.")

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("stage",choices=("preflight","verify"))
    if parser.parse_args().stage=="preflight":source_preflight()
    else:verify()
