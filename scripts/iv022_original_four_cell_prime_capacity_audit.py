#!/usr/bin/env python3
"""IV022 — exact rational FOUR-cell original signed-zeta interface audit.

EXACT source geometry:
  true historical NF543 strict collars, center +-1099/1000,
    original radius 1/1000 each;
  first central Schwartz cell center +1/5 radius 1/500;
  second independent cell center -1/5 radius 1/4000.

Source arithmetic uses full original von-Mangoldt series, actual
±log(n), all active prime powers, the unchanged original window
[-11/10,11/10], both poles and signed Gamma bracket.

The SECOND cell adds 1/2000 support measure, yielding 17/2000 total.
With the GENUINE ORIGINAL prime allowance <=2/5 Mass, not yet
shown on the whole FOUR-cell class, the signed budget is 1/16 Mass.
An original prime-transfer theorem for all FOUR cells is a separately
falsifiable OPEN obligation. A green rational preflight is not a
Lean kernel certificate and must not be reported as one.
"""
import argparse
import hashlib
import json
import re
from fractions import Fraction as Q
from pathlib import Path

from iv015_frozen_collar_exact_log_gap import log_bracket, abs_lower

ROOT=Path("WeilDefect/Arithmetic")
MODULE1=ROOT/"ActualZetaPhaseIVOriginalSecondNewCellPrimeGeometry.lean"
MODULE2=ROOT/"ActualZetaPhaseIVOriginalFourCellSignedCapacity.lean"
OLEAN_ROOT=Path(".lake/build/lib/lean/WeilDefect/Arithmetic")
LOG1=Path("iv022-original-second-cell-prime-geometry-axioms.log")
LOG2=Path("iv022-original-four-cell-signed-capacity-axioms.log")
EXACT=Path("iv022-original-four-cell-prime-geometry-exact-rational.json")
AUDIT=Path("iv022-original-four-cell-conditional-capacity-kernel-audit.json")
ALLOWED={"propext","Classical.choice","Quot.sound"}

UP1=[
 "neutralIV016FrozenFourSignedGaps_of_band",
 "neutralIV019WideFrozenConcrete_allIntegerGap",
 "neutralIV014ActiveSeparated_of_intervalGap",
 "neutralIV015ExistsComplexSchwartzBump",
]
NEW1=[
 "neutralIV022SecondCenter_outside",
 "neutralIV022ActiveOriginalLog_gtHalf",
 "neutralIV022SecondFourGap_of_band",
 "neutralIV022SecondFrozenTwoCollarActiveGap",
 "neutralIV022FirstSecondActiveGap",
 "neutralIV022SecondSelfActiveGap",
 "neutralIV022ExistsIndependentSecondPrimeFreeSchwartz",
]
UP2=[
 "neutralIV020WideThreeCell_volume",
 "neutralIV019OriginalSignedWeil_massBudget_of_prime",
 "neutralIV021WholeThreeCellOriginalWeil_oneTenth",
 "neutralIV022SecondFrozenTwoCollarActiveGap",
]
NEW2=[
 "neutralIV022FourthCell_volume",
 "neutralIV022FourCell_disjoint",
 "neutralIV022FourCell_volume",
 "neutralIV022FourCell_supported_window",
 "neutralIV022FourCell_L1_bound",
 "neutralIV022FourCell_L1_sq",
 "neutralIV022FourCell_oneSixteenth_of_originalPrime",
 "neutralIV022AdditionalCell_radiusMargin_iff",
 "neutralIV022FourthCell_exactMargin",
]
DEPS=[
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
 Path("scripts/iv019_original_width_capacity_kernel_audit.py"),
 Path("scripts/iv021_original_three_cell_smooth_partition_audit.py"),
 Path("lean-toolchain"),
 Path("lake-manifest.json"),
]
SCHEMA="IV022-original-four-physical-cells-prime-gap-and-conditional-oneSixteenth-kernel-v1"

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rat(q):return f"{q.numerator}/{q.denominator}"

CELLS={
 "original_left":(-Q(1099,1000),Q(1,1000)),
 "original_right":(Q(1099,1000),Q(1,1000)),
 "first_new":(Q(1,5),Q(1,500)),
 "second_new":(-Q(1,5),Q(1,4000)),
}
PAIRS=[
 ("original_left","first_new"),
 ("original_right","first_new"),
 ("original_left","second_new"),
 ("original_right","second_new"),
 ("first_new","second_new"),
]

def gap(c1,r1,c2,r2,n):
    lo,hi=log_bracket(n)
    delta=c2-c1
    margins=[]
    for sign in (-1,+1):
        a,b=(delta-hi,delta-lo) if sign==-1 else (delta+lo,delta+hi)
        margins.append(abs_lower(a,b)-(r1+r2))
    return min(margins)

def exact_preflight():
    results={}
    for left,right in PAIRS:
        c1,r1=CELLS[left]
        c2,r2=CELLS[right]
        q=min(gap(c1,r1,c2,r2,n) for n in range(10))
        assert q>0,(left,right,rat(q))
        results[f"{left}_to_{right}"]=rat(q)
    for name in ("first_new","second_new"):
        c,r=CELLS[name]
        q=min(gap(c,r,c,r,n) for n in range(2,10))
        assert q>0,(name,rat(q))
        results[f"{name}_self_active_n2_to_9"]=rat(q)
    ln10lo,_=log_bracket(10)
    assert ln10lo>Q(11,5)

    # The historical original-old PRIME POWER n=9 is genuinely
    # active and its translated physical overlap MUST be retained.
    a,ra=CELLS["original_left"]
    b,rb=CELLS["original_right"]
    original_n9=gap(a,ra,b,rb,9)
    assert original_n9<0,("old n9 genuine prime translation was accidentally removed",rat(original_n9))

    old=Q(1,250)
    first=Q(1,250)
    second=Q(1,2000)
    total=old+first+second
    low_mass=10*total
    gamma=Q(11,10)-Q(67,10)*low_mass
    poles=8*total
    analytic=gamma-poles
    old_prime=Q(2,5)
    margin=analytic-old_prime
    assert total==Q(17,2000)
    assert low_mass==Q(17,200)
    assert gamma==Q(1061,2000)
    assert poles==Q(17,250)
    assert analytic==Q(37,80)
    assert margin==Q(1,16)
    assert margin==Q(1,10)-150*Q(1,4000)
    threshold=Q(1,1500)
    assert Q(1,4000)<threshold
    assert Q(1,10)-150*threshold==0
    assert Q(1,10)-150*Q(1,1000)<0

    # A fabricated proposed new interval exactly log(2) away
    # from the first new interval MUST overlap at the true n=2
    # prime frequency. The checker uses rational enclosure log2.
    log2lo,log2hi=log_bracket(2)
    # The entire valid log2 interval is covered by the interval
    # of source differences if center is set to rational 693/1000.
    bad_gap=gap(Q(1,5),Q(1,500),
      Q(1,5)+Q(693,1000),Q(1,4000),2)
    assert bad_gap<0,("n2 prime-collision negative control was not rejected",rat(bad_gap))

    receipt={
      "schema":"IV022-exact-Fraction-true-four-cell-original-prime-overlap-and-capacity-v1",
      "cells":{k:{"center":rat(v[0]),"radius":rat(v[1])} for k,v in CELLS.items()},
      "all_0_to_9_original_two_collars_to_both_new_cells_plus_new_new_signed_log_gaps_certified":True,
      "two_new_cell_self_active_2_to_9_signed_log_gaps_certified":True,
      "all_pair_minimum_exact_certified_margins":results,
      "true_original_n9_old_collar_overlap_negative_margin":rat(original_n9),
      "true_original_n10_cutoff_gap":rat(ln10lo-Q(11,5)),
      "historical_two_strict_collar_measure":rat(old),
      "first_new_physical_measure":rat(first),
      "second_new_physical_measure":rat(second),
      "four_cell_physical_measure":rat(total),
      "low_frequency_mass_bound_fraction":rat(low_mass),
      "true_signed_Gamma_lower_fraction":rat(gamma),
      "both_original_pole_loss_fraction":rat(poles),
      "true_pole_plus_Gamma_lower_fraction":rat(analytic),
      "surviving_historical_n9_prime_cost_fraction":rat(old_prime),
      "CONDITIONAL_signed_four_cell_Weil_margin":rat(margin),
      "additional_second_radius_positive_threshold":rat(threshold),
      "counterfactual_oversized_second_radius_rejected_by_budget":True,
      "counterfactual_prime2_translated_cell_collision_rejected":True,
      "original_n9_prime_must_NOT_be_discarded":True,
      "complete_four_cell_original_prime_transfer_Lean_proved":False,
      "unconditional_four_cell_Weil_coercivity_Lean_proved":False,
      "kernel_proof_from_rational_preflight":False,
      "global_Weil_positivity":False,
      "RH":False,
    }
    EXACT.write_text(json.dumps(receipt,sort_keys=True,indent=2)+"\n")
    print("IV022 independent EXACT original four-cell rational gaps PASS; old n9 prime overlap retained; total real measure 17/2000, signed original Gamma1061/2000, poles17/250, candidate conditional original margin 1/16; Lean still PENDING")
    return receipt

def preflight():
    for mod,up,new in ((MODULE1,UP1,NEW1),(MODULE2,UP2,NEW2)):
        s=mod.read_text()
        assert re.findall(r"^theorem (neutralIV022\w+)",s,re.M)==new,(mod,"declarations mismatch")
        assert re.findall(r"^#print axioms (\w+)$",s,re.M)==up+new,(mod,"axiom audit mismatch")
        assert not re.search(r"^\s*(?:axiom|sorry|admit|unsafe)\b",s,re.M),mod
        assert not re.search(r"\bsorryAx\b",s),mod
    s=MODULE1.read_text()
    for name in ("neutralIV016FrozenFourSignedGaps_of_band",
       "neutralIV015FrozenTwoCollarActiveGap",
       "ArithmeticFunction.vonMangoldt_ne_zero_iff",
       "neutralIV014ActiveSeparated_of_intervalGap",
       "neutralIV022ExistsIndependentSecondPrimeFreeSchwartz"):
        assert name in s,("source geometry missing",name)
    s=MODULE2.read_text()
    for name in ("neutralIV020WideThreeCellSupport",
       "neutralIV022FourthCellInterval",
       "measure_union",
       "neutralIV020WideThreeCell_volume",
       "integral_mul_norm_le_Lp_mul_Lq",
       "neutralIV019OriginalSignedWeil_massBudget_of_prime",
       "neutralIV022FourCell_oneSixteenth_of_originalPrime"):
        assert name in s,("source signed capacity missing",name)
    for path in DEPS:assert path.is_file(),("missing source dependency",str(path))
    exact_preflight()
    print("IV022 SOURCE-ONLY PREFLIGHT PASS: 16 new authentic original source candidates and eight upstream axiom anchors. Real Lean KERNEL PENDING.")

def check_log(logpath,names):
    raw=logpath.read_text()
    assert not re.search(r"(?:^|\n).*?(?:error:|##\[error\]|declaration uses `sorry`|sorryAx)",raw,re.I),logpath
    result={}
    for name in names:
        full="'WeilDefect."+name+"'"
        positive=re.findall(re.escape(full)+r" depends on axioms: \[([^\]]*)\]",raw,re.S)
        none=re.findall(re.escape(full)+r" does not depend on any axioms",raw,re.S)
        assert len(positive)+len(none)==1,(name,len(positive),len(none))
        found=[] if none else [x.strip() for x in positive[0].split(",") if x.strip()]
        assert set(found)<=ALLOWED,(name,found)
        result[name]=found
    return result

def verify():
    preflight()
    objs=[OLEAN_ROOT/(mod.stem+".olean") for mod in (MODULE1,MODULE2)]
    for p in objs:assert p.is_file() and p.stat().st_size>0,("compiled original Lean object missing",str(p))
    a=check_log(LOG1,UP1+NEW1)
    b=check_log(LOG2,UP2+NEW2)
    report={
      "schema":SCHEMA,
      "scope":"Authentic unchanged original signed zeta four physical cells; second complex Schwartz direction independent of original plus first source; strict original ±log active prime gaps; exact physical measure; conditional original 1/16 Weil margin.",
      "source_sha256":{str(p):sha(p) for p in [MODULE1,MODULE2]+DEPS},
      "real_olean_sha256":{str(p):sha(p) for p in objs},
      "exact_rational_receipt_sha256":sha(EXACT),
      "new_compiled_source_Lean_theorems":NEW1+NEW2,
      "upstream_actual_source_axiom_anchors":UP1+UP2,
      "strict_standard_axioms":{**a,**b},
      "genuine_second_independent_complex_Schwartz_direction_Lean_PASS":True,
      "second_prime_separation_from_old_and_first_new_and_self_Lean_PASS":True,
      "true_four_cell_L1_mass_certificate_Lean_PASS":True,
      "conditional_original_four_cell_oneSixteenth_capacity_Lean_PASS":True,
      "four_cell_complete_prime_transfer_PROVED":False,
      "unconditional_original_four_cell_Weil_coercivity_PROVED":False,
      "global_Weil_positivity":False,
      "RH":False,
    }
    AUDIT.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print("IV022 ACTUAL LEAN KERNEL PASS: second original prime-compatible Schwartz cell and conditional four-cell signed 1/16 width bound; 16 new+8 upstream standard axioms. Four-cell prime transfer STILL OPEN.")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("stage",choices=("preflight","verify"))
    if p.parse_args().stage=="preflight":preflight()
    else:verify()
