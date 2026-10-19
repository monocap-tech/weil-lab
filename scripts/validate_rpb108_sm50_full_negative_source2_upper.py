#!/usr/bin/env python3
"""SM50: complete original negative-frequency upper on genuine SM49 odd source e2.

Original SI10 provides ALL actual signed-negative-frequency support on
[0,896] via exactly 973 dyadic leaves (107 physical cover clusters).
For every real xi in a genuine leaf [a,b], w(xi)=(kappa-m(xi))_+
is <= h_leaf+kappa by exact original SI06 seven-prime/digamma bound.
Outside this cover, w(xi)=0 on all positive xi, including xi>=896.
No continuous-frequency negative contribution is omitted.

For actual original zero-extended sine physical source g2:
   T_g(xi)=B*(sinc(2B(c-xi))-sinc(2B(c+xi)))
where c is the genuine selected original cluster source center.
The inherited SM43 source_window_support_envelopes on whole REAL cells
bounds |T_g(xi)|<=s_I. Thus
 <g2,Kneg,o g2> <= 2*sum_I (h_I+kappa)*(b-a)*s_I^2.
This is an UPPER of the entire actual original Knegative, not a
15-band lower witness or sampled finite Fourier cutoff.

SM49 gives a complete original positive LOW [0,4096] 25-source
certified lower; use its exact coordinate (2,2) with either the
full-25source Loewner fee (strong acceptance) or tighter independent
directional remainder. Original true sinh pole p2 is enclosed by
SM42 exact full physical interval Gram, so
  <g2,Wodd g2> >= ApositiveLOW_LB(g2)
                 - NEGATIVE_ENTIRE_UPPER(g2)
                 - 2*max(|pole_interval|)^2.
Nonnegative omitted original positive high frequencies improve the
true Wodd, not weaken this certificate.

This is at most ONE genuine 25-dimensional source direction, NOT
the 25x25 PSD/negative index nor all 470 source original Astar
resolvent/complement, even, signed Weil, CC27 or RH. Fail closed on
any claim of actual original e2 signed positivity unless exact
strict positive lower is proved.
"""
import argparse
import json
from fractions import Fraction as F

from validate_rpb108_si06_negative_band import B
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm10_explicit_odd_cap_moments import full_upper_leaves
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    original_full_25_physical_interval_gram
)
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT,original_source_centered_windows,source_window_support_envelopes,
    ceil_rat,floor_rat
)
from validate_rpb108_sm47_original_full_low_jensen import (
    full_original_rational_gram,build_original_positive_jensen,TAIL
)
from validate_rpb108_sm49_adaptive_positive_jensen import (
    original_adaptive_candidate_cells,
    original_additional_positive_source_matrix
)

FOCUS=2
DEN=10**12
def down(x):return floor_rat(x,DEN)
def up(x):return ceil_rat(x,DEN)


def complete_original_negative_source2_upper(centers,sources):
    """Entire original NEGATIVE frequency support, original SI10 dyadic cap.

    With reflected factor 2 as in SM47, no factor of two is missing.
    Entire high |xi|>=896 is truly negative-free by SI06.
    """
    assert len(sources)==25
    typ,j,k=sources[FOCUS]
    assert typ=="cluster" and k==0 and j>=0
    clusters,W,Mneg,mass=full_upper_leaves()
    assert len(clusters)==107 and W==F(973,32)
    leaves=[(a,b,h) for cluster in clusters for a,b,h in cluster]
    assert len(leaves)==973
    total=F(0)
    mass_check=F(0)
    near=F(0)
    max_source=F(0)
    for a,b,h in leaves:
        # The original SI10 all-real leaf theorem:
        # true (kappa-m)_+ <= h + kappa.
        weight=h+KAPPA
        assert weight>0
        whole_source_caps=source_window_support_envelopes(
            a,b,centers,sources)
        s=whole_source_caps[FOCUS]
        assert s>=0
        contribution=2*(b-a)*weight*s*s
        total+=contribution
        mass_check+=2*(b-a)*weight
        max_source=max(max_source,s)
        if a<=centers[j]<=b:
            near+=contribution
    assert mass_check==mass
    # A uniform source transform ceiling |T|<=2B also holds,
    # so trace-style full-negative upper is clearly looser.
    trivial=mass*(2*B)**2
    assert total<trivial
    return total,trivial,max_source,near,len(leaves),len(clusters),mass


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",
        default="artifacts/sm50_original_complete_negative_upper_source2.json")
    args=parser.parse_args()
    m=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in m["obligations"] if x["id"]=="W-ODD-NEG")
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]==odd["status"]=="open"
    assert m["governance"]["no_automatic_promotion"] is True
    assert "SM49" in m["evidence"] and "SM49" in odd["evidence"]
    centers,sources,_=original_source_centered_windows()
    gram,actual_source_list,pole=original_full_25_physical_interval_gram()
    assert sources==actual_source_list
    Hq,epsH=full_original_rational_gram(gram)
    P47,epsP47,improved,rad,bands,signed=build_original_positive_jensen(
        centers,sources)
    chosen,available,rejected,focus_center=original_adaptive_candidate_cells(
        centers,sources)
    P49,epsP49,eps49_dir,improved49,extra_bands=(
        original_additional_positive_source_matrix(centers,sources,chosen))
    epsH=up(epsH);epsP47=up(epsP47)
    pos_full=KAPPA*Hq[FOCUS][FOCUS]+P47[FOCUS][FOCUS]+P49[FOCUS][FOCUS] - (
        KAPPA*(TAIL+epsH)+epsP47+epsP49)
    pos_direction=KAPPA*Hq[FOCUS][FOCUS]+P47[FOCUS][FOCUS]+P49[FOCUS][FOCUS] - (
        KAPPA*(TAIL+epsH)+epsP47+eps49_dir)
    assert pos_direction>=pos_full>0
    original_negative,rough_source_upper,maxcap,near,nleaf,ncluster,mass=(
        complete_original_negative_source2_upper(centers,sources))
    neg_upper=up(original_negative)
    pole_interval=gram[FOCUS][24]
    pole_cross_upper=max(abs(pole_interval.l),abs(pole_interval.h))
    pole_penalty_upper=up(2*pole_cross_upper**2)
    signed_full=pos_full-neg_upper-pole_penalty_upper
    signed_dir=pos_direction-neg_upper-pole_penalty_upper
    assert signed_dir>=signed_full
    # A signed-positive conclusion is conditional on the ACTUAL
    # full original NEGATIVE upper, not the SM48 15-band lower.
    actual_signed_certificate=signed_full>0
    result={
      "status":"SCOPED_TRUE_ORIGINAL_FULL_NEGATIVE_973LEAF_SOURCE2_UPPER",
      "canonical_W_ODD_NEG":"OPEN",
      "actual_original_odd_source_dimension":25,
      "original_genuine_sine_source_index":FOCUS,
      "genuine_original_sine_frequency_center":str(focus_center),
      "original_signed_negative_entire_real_positive_half_support":"[0,896] certified cover",
      "true_original_negative_frequency_leaves":nleaf,
      "original_negative_cover_clusters":ncluster,
      "total_original_negative_weight_rational_cap_mass_up":str(up(mass)),
      "true_original_whole_negative_frequency_source2_form_upper":str(neg_upper),
      "true_original_whole_negative_frequency_unrounded_up":str(
          up(original_negative)),
      "independent_crude_original_negative_source_upper":str(
          up(rough_source_upper)),
      "negative_upper_max_source_transform_envelope":str(up(maxcap)),
      "near_sine_center_negative_upper_part":str(up(near)),
      "SM49_baseline_plus_adaptive_positiveLOW_true_full25error_source2_lower":str(
          down(pos_full)),
      "SM49_baseline_plus_adaptive_positiveLOW_directionalerror_source2_lower":str(
          down(pos_direction)),
      "true_original_physical_sinh_pole_rankone_source2_penalty_upper":str(
          pole_penalty_upper),
      "full25error_entire_original_signed_odd_source2_Rayleigh_lower":str(
          down(signed_full)),
      "directionalerror_entire_original_signed_odd_source2_Rayleigh_lower":str(
          down(signed_dir)),
      "full25error_actual_original_signed_source2_positive_certified":
          actual_signed_certificate,
      "source2_actual_signed_positive_claim_requires_strict_certified_lower":True,
      "complete_true_original_negative_upper_on_same_source":True,
      "original_high_positive_tail_discarded_only_nonnegative":True,
      "all_25_source_coupled_signed_operator_PSD_certified":False,
      "original_complete_470_Astar_inverse_strong_residual_certified":False,
      "original_entire_odd_O1_O2_even_Weil_CC27_RH_certified":False,
      "external_original_Fourier_closed_domain_audit":"OPEN",
      "interpretation":"The entire original signed-negative frequency upper on source e2 is paid, alongside true original positive LOW full25 error and genuine signed sinh pole. A positive scalar lower implies TRUE original Wodd positivity only along source e2, never entire source space or Weil/RH."
    }
    dest=ROOT/args.output;dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(result,indent=2)+"\n")
    print("SM50 ACTUAL original whole-negative source2 comparison:",json.dumps({
       "full_negative_source2_upper":result[
           "true_original_whole_negative_frequency_source2_form_upper"],
       "full25source_positive_lower":result[
           "SM49_baseline_plus_adaptive_positiveLOW_true_full25error_source2_lower"],
       "source2_sinh_pole_penalty_upper":result[
           "true_original_physical_sinh_pole_rankone_source2_penalty_upper"],
       "actual_original_signed_lower":result[
           "full25error_entire_original_signed_odd_source2_Rayleigh_lower"],
       "actual_sign_certified":actual_signed_certificate,
       "neg_leaves":nleaf
    }),flush=True)
    print("SM50 entire original negative source2 UPPER scoped; full 25source/470source O1/O2/even Weil CC27 RH OPEN.",flush=True)

if __name__=="__main__":
    main()
