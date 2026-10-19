#!/usr/bin/env python3
"""SM51 direct signed-frequency physical source2 certificate (scoped).

Unlike SM47-50A's separate Apositive LOWER - Knegative UPPER,
on CORE=[13,16] integrate TRUE original signed m(xi) directly,
using original SI06 all-seven-prime midpoint/endpoint rational
bounds and original SM39 monotone archimedean rational lower.

For every real cell I, certify m>=mlo. If mlo>=0, Jensen's
frequency-AVERAGED actual source2 Fourier transform gives a lower
bound on its true L2 mass. If mlo<0, exact physical F0/F1/F2
affine-square with curvature pays the entire source L2 from ABOVE.
This preserves the *sign* of the contribution.

Outside core, original SI10 973 exhaustive true signed-negative
leaves (3892 SM39 subcells) bound the remaining negative from
ABOVE, while 17 original SM12 and 32 new SM49 sign-positive
windows outside core give Jensen positive contributions from BELOW.
Original SM42 true physical sinh pole square upper is paid once.

The result lower-bounds the TRUE original odd signed W quadratic
ON ONE original supported source e2 only. A nonpositive lower
proves no negativity; neither one source nor an isolated positive
Rayleigh scalar proves full source-space/470/odd O1/O2/Weil/RH.
"""
import argparse,json
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import B,PI,prime_interval
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_si07_negative_support_cover import M
from validate_rpb108_sm10_explicit_odd_cap_moments import full_upper_leaves
from validate_rpb108_sm39_rational_left_arch_cap import arch_lower_at
from validate_rpb108_sm40_endpoint_curvature_negative_cap import D2
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    I,F0,F1,F2,original_full_25_physical_interval_gram)
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT,original_source_centered_windows,source_window_support_envelopes,
    ceil_rat,floor_rat)
from validate_rpb108_sm44_physical_fourier_cell_gram import quantize,sqrt_upper
from validate_rpb108_sm12_positive_reference_33 import (
    CENTERS as OLD_POS,RADIUS as OLD_R)
from validate_rpb108_sm49_adaptive_positive_jensen import (
    original_adaptive_candidate_cells)
CORE_A=F(13)
CORE_B=F(16)
NCORE=768
IDX=2
DEN=10**12
def up(x):return ceil_rat(x,DEN)
def down(x):return floor_rat(x,DEN)

def source_data(centers,sources,lo,hi):
    """TRUE original odd supported source2 physical Fourier cell integrals.

    Exact source-transform value, first derivative, second derivative
    (all outward interval), plus global true original third spatial
    moment provide whole-real affine-square UPPER and frequency
    Jensen L2 LOWER independently. Every quantity is Fraction.
    """
    assert lo<hi
    typ,j,k=sources[IDX]
    assert typ=="cluster" and k==0
    c=centers[j]
    r=(hi-lo)/2;mid=(lo+hi)/2
    pi=I(PI[0],PI[1])
    Kglob=4*PI[1]**2*2*B**3/3
    M3=(2*PI[1])**3*B**4/2
    val=(F0(c-mid)-F0(c+mid))/2
    deriv=pi*(F1(c-mid)+F1(c+mid))
    second=2*pi*pi*(F2(c+mid)-F2(c-mid))
    v=quantize(val.mid())
    d=quantize(deriv.mid())
    e0=ceil_rat(max(abs(val.l-v),abs(val.h-v)),10**9)
    e1=ceil_rat(max(abs(deriv.l-d),abs(deriv.h-d)),10**9)
    K=min(Kglob,max(abs(second.l),abs(second.h))+M3*r)
    assert 0<=K<=Kglob
    # |T(xi)-v-d*(xi-mid)| <= e0+e1*r+K*r²/2.
    rem=e0+e1*r+K*r*r/2
    affine_energy=v*v+d*d*r*r/3
    upper_sq=affine_energy+2*rem*sqrt_upper(affine_energy)+rem*rem
    sinc=source_window_support_envelopes(lo,hi,centers,sources)[IDX]
    upper_sq=min(upper_sq,sinc*sinc)
    # For true frequency average u, T' mean zero, second T''/6.
    mean_e=e0+K*r*r/6
    mean_lower=max(F(0),abs(v)-mean_e)
    lower_sq=mean_lower*mean_lower
    assert 0<=lower_sq<=upper_sq
    return lower_sq,upper_sq,int(K<Kglob)

def signed_core(centers,sources):
    """All of core covered EXACTLY by 768 rational real-frequency cells.

    True original m_lower on each whole cell is max of two
    separately rigorous original lower certificates:
    - SI39 rational arch-left + SI06 midpoint prime -69*r
    - SI39 arch-left + SI06 endpoint-min prime -D2*h²/8.
    """
    step=(CORE_B-CORE_A)/NCORE
    assert step==F(1,256)
    signed=F(0)
    neg=F(0);pos=F(0)
    positive_cells=0;negative_cells=0;source_improved=0
    sign_lower_min=None;sign_lower_max=None
    for n in range(NCORE):
        a=CORE_A+n*step;b=a+step
        mid=(a+b)/2
        arch=arch_lower_at(a)
        prime_lo=prime_interval(mid)[0]-M*step/2
        endpoint_lo=min(prime_interval(a)[0],prime_interval(b)[0])-D2*step*step/8
        mlo=arch+max(prime_lo,endpoint_lo)
        sign_lower_min=mlo if sign_lower_min is None else min(mlo,sign_lower_min)
        sign_lower_max=mlo if sign_lower_max is None else max(mlo,sign_lower_max)
        lb,ub,improved=source_data(centers,sources,a,b)
        source_improved+=improved
        if mlo>=0:
            positive_cells+=1
            contribution=2*step*mlo*lb
            pos+=contribution
        else:
            negative_cells+=1
            contribution=2*step*mlo*ub
            neg-=contribution
        signed+=contribution
    assert positive_cells+negative_cells==NCORE
    assert signed==pos-neg
    return signed,{
        "original_core_left":str(CORE_A),
        "original_core_right":str(CORE_B),
        "certified_whole_real_signed_core_cells":NCORE,
        "core_exact_positive_m_lower_cells":positive_cells,
        "core_exact_negative_m_lower_cells":negative_cells,
        "core_source_local_curvature_strict_improvements":source_improved,
        "signed_core_positive_lower_component":str(down(pos)),
        "signed_core_negative_upper_component":str(up(neg)),
        "signed_core_full_original_m_source2_lower":str(down(signed)),
        "core_min_multiplier_signed_lower":str(down(sign_lower_min)),
        "core_max_multiplier_signed_lower":str(down(sign_lower_max))
    }

def outside_negative(centers,sources):
    """Entire true negative outside core, no double counting.

    Full original 973 SI10 parent signed-negative support leaves.
    Refined 3892 rational original SM39 signed upper cells are aligned
    with integer core endpoints [13,16]. On every excluded subcell,
    min of genuine parent and SM39 true signed upper plus original
    true physical source2 affine-square upper proves form ceiling.
    """
    original,W,Mneg,mass=full_upper_leaves()
    leaves=[(a,b,h) for cluster in original for a,b,h in cluster]
    assert len(original)==107 and len(leaves)==973 and W==F(973,32)
    value=F(0);n=0;inside=0;outside=0;zero=0;aff=0;improved=0
    for a,b,h in leaves:
        wp=h+KAPPA
        for t in range(4):
            l=a+(b-a)*F(t,4)
            r=a+(b-a)*F(t+1,4)
            n+=1
            assert not (l<CORE_A<r or l<CORE_B<r)
            if CORE_A<=l and r<=CORE_B:
                inside+=1
                continue
            outside+=1
            mlo=arch_lower_at(l)+prime_interval((l+r)/2)[0]-M*(r-l)/2
            need=max(F(0),KAPPA-mlo)
            w=min(wp,ceil_rat(need,10**6))
            assert w>=need or w==wp
            assert 0<=w<=wp
            if w==0:
                zero+=1
                continue
            _,upper,local=source_data(centers,sources,l,r)
            improved+=local
            # source_data upper is min affine integral and genuine
            # entire real sinc bound; all subcells accounted.
            value+=2*(r-l)*w*upper
    assert n==3892 and inside>0 and outside>0
    return value,{
        "original_total_negative_leaves":973,
        "whole_original_negative_subcells":3892,
        "original_negative_subcells_inside_direct_signed_core":inside,
        "original_negative_subcells_outside_core_upper_paid":outside,
        "original_negative_subcells_zero_weight_outside":zero,
        "outside_original_negative_local_curvature_improvements":improved,
        "entire_original_negative_outside_core_upper":str(up(value))
    }

def exterior_positive(centers,sources,chosen):
    """Source2 Jensen contributions OUTSIDE signed core, disjoint windows.

    All genuine SM12 17 positive whole-real windows and selected
    32 SM49 sign-positive windows are disjoint pairwise. We do not
    count any band touching or overlapping direct signed core.
    Any discarded bands merely weaken the lower inequality.
    """
    bands=[(c-OLD_R,c+OLD_R,F(2),"SM12") for c in OLD_POS]
    for row in chosen:
        bands.append((row["a"],row["b"],row["delta"],"SM49"))
    bands.sort()
    for i in range(len(bands)-1):
        assert bands[i][1]<=bands[i+1][0]
    gain=F(0);count=0;overlap=0
    from_old=0;from_new=0
    for a,b,delta,label in bands:
        if not(b<=CORE_A or a>=CORE_B):
            overlap+=1
            continue
        assert delta>0
        lo,hi,_=source_data(centers,sources,a,b)
        g=2*(b-a)*delta*lo
        assert g>=0
        gain+=g
        count+=1
        if label=="SM12":from_old+=1
        else:from_new+=1
    assert len(bands)==49 and count+overlap==49
    return gain,{
        "original_SM12_SM49_disjoint_signed_positive_total":49,
        "positive_bands_outside_direct_core_used":count,
        "SM12_windows_used":from_old,
        "SM49_windows_used":from_new,
        "positive_bands_overlapping_core_discarded":overlap,
        "certified_original_exterior_positive_Jensen_lower":str(down(gain))
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm51_true_original_signed_source2_direct_core.json")
    a=p.parse_args()
    manifest=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in manifest["obligations"] if x["id"]=="W-ODD-NEG")
    assert manifest["active_obligation"]=="W-ODD-NEG"
    assert manifest["objective"]["status"]==odd["status"]=="open"
    assert manifest["governance"]["no_automatic_promotion"] is True
    assert all(x in odd["evidence"] for x in ("SM49","SM50","SM50A"))
    centers,sources,_=original_source_centered_windows()
    assert len(sources)==25 and sources[IDX][0]=="cluster" and sources[IDX][2]==0
    assert centers[sources[IDX][1]]==F(1845,128)
    H,src,pole=original_full_25_physical_interval_gram()
    assert src==sources
    chosen,available,rejected,c=original_adaptive_candidate_cells(centers,sources)
    assert len(chosen)==32 and c==F(1845,128)
    core,corestats=signed_core(centers,sources)
    outside,outstats=outside_negative(centers,sources)
    positive,posstats=exterior_positive(centers,sources,chosen)
    pole_c=H[IDX][24]
    polefee=up(2*max(abs(pole_c.l),abs(pole_c.h))**2)
    # Entire true odd signed W form (for this physical source):
    # signed m on core + signed m >= -negative outside core
    # + extra genuine positive windows (disjoint with core)
    # - true physical sinh pole rank-one penalty.
    total=core-outside+positive-polefee
    validpositive=total>0
    result={
      "status":"SCOPED_TRUE_ORIGINAL_DIRECT_SIGNED_CORE_COMPLETE_OUTER_NEGATIVE_ONE_SOURCE",
      "canonical_W_ODD_NEG":"OPEN",
      "original_physical_odd_carrier_source_count":25,
      "original_signed_target_source_index":IDX,
      "original_signed_target_source_center":"1845/128",
      **corestats,**outstats,**posstats,
      "true_original_signed_sinh_pole_outer_penalty":str(polefee),
      "true_original_direct_signed_source2_Rayleigh_lower":str(down(total)),
      "true_original_one_source_signed_positive_certified":validpositive,
      "whole_signed_frequency_outside_core_covered":"SI10 973 all-real negative leaves, nonnegative elsewhere, original SM12/SM49 disjoint exterior positive Jensen bands",
      "true_signed_m_original_on_core_not_pos_minus_neg":True,
      "whole_true_original_25x25_signed_PSD_certified":False,
      "complete_original_470_source_odd_O1O2_even_Weil_CC27_RH_certified":False,
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "interpretation":"Full original true signed m core, full exhaustive exterior negative UPPER and disjoint exterior positive Jensen LOWER, true pole paid. Valid original odd signed lower for ONE supported source only; its sign if bound nonpositive is inconclusive."
    }
    target=ROOT/a.output;target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(result,indent=2)+"\n")
    print("SM51 original direct signed physical source2:",json.dumps({
        "core_signed_lower":result["signed_core_full_original_m_source2_lower"],
        "outside_negative_upper":result["entire_original_negative_outside_core_upper"],
        "outside_positive_lower":result["certified_original_exterior_positive_Jensen_lower"],
        "pole_upper":result["true_original_signed_sinh_pole_outer_penalty"],
        "whole_signed_source2_lower":result["true_original_direct_signed_source2_Rayleigh_lower"],
        "signed_e2_certified":validpositive,
        "core_signpositive":corestats["core_exact_positive_m_lower_cells"],
        "core_signnegative":corestats["core_exact_negative_m_lower_cells"],
        "even_Weil_RH":"OPEN"
    }),flush=True)
if __name__=="__main__":main()
