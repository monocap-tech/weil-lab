#!/usr/bin/env python3
"""SM50A: original complete source2 negative UPPER, true 3892-cell Fourier integration.

Rechecks original SI10 973-leaf all-negative cover; each of 4 subcells
inherits the parent certified weight upper and gets its own SM39
original arch-left + SI06 seven-prime midpoint whole-real signed bound.
For genuine original sine source e2, its physical Fourier value and
first/second derivatives are certified by original SM42 F0/F1/F2.
Cellwide mean-square uses exactly integrated affine v+d*t and pays
whole-real second-derivative/Taylor remainder through exact Cauchy.
Every retained region of original negative-frequency support is paid.
This certifies only e2, not full 25source or complete W-ODD-NEG.
"""
import argparse,json
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import B,PI,prime_interval
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_si07_negative_support_cover import M
from validate_rpb108_sm10_explicit_odd_cap_moments import full_upper_leaves
from validate_rpb108_sm39_rational_left_arch_cap import arch_lower_at
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    I,F0,F1,F2,original_full_25_physical_interval_gram)
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT,original_source_centered_windows,source_window_support_envelopes,
    ceil_rat,floor_rat)
from validate_rpb108_sm44_physical_fourier_cell_gram import quantize,sqrt_upper
from validate_rpb108_sm47_original_full_low_jensen import (
    full_original_rational_gram,build_original_positive_jensen,TAIL)
from validate_rpb108_sm49_adaptive_positive_jensen import (
    original_adaptive_candidate_cells,original_additional_positive_source_matrix)

IDX=2
SUB=4
def up(x):return ceil_rat(x,10**12)
def down(x):return floor_rat(x,10**12)

def compute_negative(centers,sources):
    typ,j,degree=sources[IDX]
    assert typ=="cluster" and degree==0
    c=centers[j]
    clusters,W,_,total=full_upper_leaves()
    leaves=[(a,b,h) for cluster in clusters for a,b,h in cluster]
    assert len(leaves)==973 and len(clusters)==107 and W==F(973,32)
    pi=I(PI[0],PI[1])
    Kglobal=4*PI[1]**2*2*B**3/3
    Kthird=(2*PI[1])**3*B**4/2
    baseline=F(0);weightonly=F(0);integrated=F(0)
    mass=F(0);new_mass=F(0)
    selected_aff=0;improved_weights=0;second_improved=0
    for a,b,h in leaves:
        wp=h+KAPPA
        assert wp>=0
        parentcap=source_window_support_envelopes(a,b,centers,sources)[IDX]
        baseline+=2*(b-a)*wp*parentcap**2
        mass+=2*(b-a)*wp
        for t in range(SUB):
            lo=a+(b-a)*F(t,SUB)
            hi=a+(b-a)*F(t+1,SUB)
            radius=(hi-lo)/2;mid=(lo+hi)/2
            lower=arch_lower_at(lo)+prime_interval(mid)[0]-M*radius
            needed=max(F(0),KAPPA-lower)
            w=min(wp,ceil_rat(needed,10**6))
            assert w>=needed or w==wp
            assert 0<=w<=wp
            improved_weights+=w<wp
            new_mass+=2*(hi-lo)*w
            if not w:continue
            sc=source_window_support_envelopes(lo,hi,centers,sources)[IDX]
            sup2=sc*sc
            weightonly+=2*(hi-lo)*w*sup2
            val=(F0(c-mid)-F0(c+mid))/2
            deriv=pi*(F1(c-mid)+F1(c+mid))
            second=2*pi*pi*(F2(c+mid)-F2(c-mid))
            v=quantize(val.mid());d=quantize(deriv.mid())
            e0=ceil_rat(max(abs(val.l-v),abs(val.h-v)),10**9)
            e1=ceil_rat(max(abs(deriv.l-d),abs(deriv.h-d)),10**9)
            K=min(Kglobal,max(abs(second.l),abs(second.h))+Kthird*radius)
            assert 0<=K<=Kglobal
            second_improved+=K<Kglobal
            R=e0+e1*radius+K*radius**2/2
            moment=v*v+d*d*radius*radius/3
            affine2=moment+2*R*sqrt_upper(moment)+R*R
            selected_aff+=affine2<sup2
            integrated+=2*(hi-lo)*w*min(affine2,sup2)
    assert mass==total
    assert 0<=new_mass<=mass
    assert 0<=integrated<=weightonly<=baseline
    assert improved_weights>0 and integrated<baseline
    return {
       "parent_true_original_negative_leaves":973,
       "refined_true_original_negative_subcells":973*SUB,
       "all_107_original_negative_clusters_retained":True,
       "original_weight_improved_subcells":improved_weights,
       "source_frequency_affine_integration_cells_selected":selected_aff,
       "source_second_derivative_strict_improvements":second_improved,
       "original_negative_weight_mass_parent_upper":str(up(mass)),
       "original_negative_weight_mass_refined_upper":str(up(new_mass)),
       "original_full_negative_973parent_sinc_upper":str(up(baseline)),
       "original_full_negative_refined_weight_only_sinc_upper":str(up(weightonly)),
       "original_full_negative_refined_fourier_integrated_upper":str(up(integrated)),
       "exact_rational_refinement_strict":integrated<baseline,
       "refined_to_parent_ratio_float":float(integrated/baseline)
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm50a_original_refined_negative_source2.json")
    args=p.parse_args()
    manifest=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in manifest["obligations"] if x["id"]=="W-ODD-NEG")
    assert manifest["active_obligation"]=="W-ODD-NEG"
    assert manifest["objective"]["status"]==odd["status"]=="open"
    assert "SM50" in odd["evidence"] and "SM49" in odd["evidence"]
    centers,sources,_=original_source_centered_windows()
    gram,src,pole=original_full_25_physical_interval_gram()
    assert sources==src
    Hq,eH=full_original_rational_gram(gram)
    Pbase,eP,_,_,_,_=build_original_positive_jensen(centers,sources)
    candidates,_,_,source_center=original_adaptive_candidate_cells(centers,sources)
    Padd,eAdd,eDir,_,_=original_additional_positive_source_matrix(
        centers,sources,candidates)
    assert source_center==F(1845,128)
    eOld=KAPPA*(TAIL+up(eH))+up(eP)
    positive=KAPPA*Hq[IDX][IDX]+Pbase[IDX][IDX]+Padd[IDX][IDX]-eOld-eAdd
    assert positive>0
    neg=compute_negative(centers,sources)
    negative_upper=F(neg["original_full_negative_refined_fourier_integrated_upper"])
    oldnegative=F(neg["original_full_negative_973parent_sinc_upper"])
    p2=gram[IDX][24]
    poleupper=up(2*max(abs(p2.l),abs(p2.h))**2)
    margin=positive-negative_upper-poleupper
    oldmargin=positive-oldnegative-poleupper
    assert margin>oldmargin
    certified=margin>0
    neg.update({
      "status":"SCOPED_TRUE_ORIGINAL_3892SUBCELL_COMPLETE_NEGATIVE_SOURCE2_UPPER",
      "canonical_W_ODD_NEG":"OPEN",
      "original_physical_odd_source_index":IDX,
      "original_sine_source_center":str(source_center),
      "full25error_original_positiveLOW_source2_lower":str(down(positive)),
      "true_original_complete_negative_source2_upper":str(up(negative_upper)),
      "true_original_sinh_pole_source2_penalty_upper":str(poleupper),
      "old_entire_negative_parent_upper_signed_Rayleigh_lower":str(down(oldmargin)),
      "refined_entire_original_signed_source2_Rayleigh_lower":str(down(margin)),
      "true_original_source2_signed_positivity_certified":certified,
      "whole_original_negative_frequency_upper_not_15band_lower":True,
      "whole_true_25x25_odd_signed_PSD_certified":False,
      "original_470_Astar_resolvent_O1O2_even_Weil_CC27_RH_certified":False,
      "independent_physical_Fourier_and_form_domain_audit":"OPEN"
    })
    dest=ROOT/args.output
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(neg,indent=2)+"\n")
    print("SM50A original complete signed source2 refined upper:",json.dumps({
      "parent":neg["original_full_negative_973parent_sinc_upper"],
      "refined_weight_only":neg["original_full_negative_refined_weight_only_sinc_upper"],
      "refined_affine":neg["true_original_complete_negative_source2_upper"],
      "ratio":neg["refined_to_parent_ratio_float"],
      "positive_lower":neg["full25error_original_positiveLOW_source2_lower"],
      "pole_penalty":neg["true_original_sinh_pole_source2_penalty_upper"],
      "signed_lower":neg["refined_entire_original_signed_source2_Rayleigh_lower"],
      "certified":certified,
      "even_Weil_RH":"OPEN"
    }),flush=True)
if __name__=="__main__": main()
