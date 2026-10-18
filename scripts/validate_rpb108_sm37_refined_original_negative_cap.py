#!/usr/bin/env python3
"""SM37: rigorously refine the ORIGINAL signed-negative seven-prime CAP,
and test its original SM36 25-source trial response numerically.

CERTIFIED, subject to inherited SI06/07/10/SM10 interval and original
Fourier identification:
 - Split each of ALL 973 original dyadic unresolved sign-safe leaves
   into 4 subcells; retain same ORIGINAL true 107 cluster boundaries.
 - Each subcell lower-bounds the ORIGINAL signed seven-prime m(xi)
   at EVERY real point by SI07 monotone original arch lower at floor(l)
   plus SI06 exact signed 7-prime midpoint interval minus M*width/2.
 - Refined nonnegative weight wsub>=max(0,kappa-m) on each whole subcell,
   outward rounded upward in exact rationals; 1e-6 floor makes every
   moment block strictly SPD. Also wsub<=wold on that subcell.
 - Thus a NEW genuine original full operator cap:
       0<=Kneg <= (1+tau) U Dnew U* + eta_new I
                <= (1+tau) U Dold U* + eta_old I
   using SAME all 107 physical Taylor source blocks, 890 columns,
   SAME full negative source frequency support, and exactly recomputed
   eta_new for the true 24-bit remainder and new total weight mass.
   Entries and strict SPD of ALL true 107 moment blocks exact Fraction.
 - Pilot: compare new/old block-cap generalized largest eigenvalues
   on SAME 25 SM36 selected original physical source trial and
   SAME direct sampled negative response at fixed (N,pad).

Crucial: pilot Fourier m and physical quadrature are float64 and omit
the complete positive digamma high-frequency tail; the pilot
eigenvalues are NOT original whole operator spectral certificates.
No full 470 source pole-conditioned resolvent or strong residual.
Even exact Kneg cap SPD does NOT prove W_odd>=0, Weil positivity/RH.
"""
import argparse
import json
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy import linalg

from validate_rpb108_si06_negative_band import prime_interval,B
from validate_rpb108_si07_negative_support_cover import (
    arch_lower_cell,M,DEN,ceil_fraction
)
from validate_rpb108_sm10_explicit_odd_cap_moments import (
    full_upper_leaves,exact_block,BITS,TAU
)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm17_compact_spectral_gate import ETA_UP
from sm36_original_odd_numerical_pilot import (
    geometry,select_sources,physical_columns,fourier_form,
    all_source_negative_cap,original_multiplier,THETA
)

ROOT=Path(__file__).resolve().parents[1]
FLOOR=F(1,DEN)
SUBCELLS=4


def refined_signed_original_cap(subcells=SUBCELLS):
    assert subcells>=2 and subcells<=16 and subcells&(subcells-1)==0
    old,W,mneg,total_old=full_upper_leaves()
    assert len(old)==107 and W==F(973,32)
    assert F(0)<KAPPA and FLOOR<KAPPA
    refined=[]
    mass_old_check=F(0)
    mass_new=F(0)
    protected_sub=0
    improved_sub=0
    upper_gap_sum=F(0)
    n_refined=0
    for cluster in old:
        out=[]
        for left,right,h_old in cluster:
            old_weight=h_old+KAPPA
            assert h_old>=0 and old_weight>=KAPPA
            j=left.numerator//left.denominator
            low_arch=arch_lower_cell(j)
            mass_old_check+=2*(right-left)*old_weight
            assert 0<=j<896 and left<right<=j+1
            for i in range(subcells):
                a=left+(right-left)*F(i,subcells)
                b=left+(right-left)*F(i+1,subcells)
                midpoint=(a+b)/2
                # Arch lower at integer j valid through [j,j+1];
                # genuine seven-prime midpoint rigorous interval plus
                # true prime derivative 69 pays the entire subcell.
                m_lower=low_arch+prime_interval(midpoint)[0]-M*(b-a)/2
                assert M==69 and a>=j and b<=j+1
                needed=max(F(0),KAPPA-m_lower)
                rounded=F(ceil_fraction(needed*DEN),DEN)
                assert rounded>=needed
                weight=min(old_weight,max(FLOOR,rounded))
                assert FLOOR<=weight<=old_weight
                assert weight>=max(F(0),KAPPA-m_lower) or (
                    # If old weight is smaller, its independently
                    # proven whole ORIGINAL old-leaf upper applies.
                    weight==old_weight)
                if m_lower>KAPPA:protected_sub+=1
                if weight<old_weight:improved_sub+=1
                upper_gap_sum+=(old_weight-weight)*(b-a)*2
                # Original SM10 exact_block stores leaf's h with
                # actual weight w=h+kappa. Negative h is allowed
                # here: w strictly >0 and old≥new pointwise.
                out.append((a,b,weight-KAPPA))
                mass_new+=2*(b-a)*weight
                n_refined+=1
        assert out[0][0]==cluster[0][0]
        assert out[-1][1]==cluster[-1][1]
        assert all(out[k][1]==out[k+1][0] for k in range(len(out)-1))
        refined.append(out)
    assert n_refined==973*subcells and len(refined)==107
    assert mass_old_check==total_old
    assert mass_new<total_old
    # ACTUAL ORIGINAL strict whole-cap mass improvement, exact
    # rather than a float64 comparison or selected Ritz sign:
    assert mass_new*4<total_old*3
    assert total_old-mass_new>F(10)
    assert upper_gap_sum==total_old-mass_new
    orders=[taylor_order(c[-1][1]-c[0][0],BITS)[0]
            for c in refined]
    assert len(orders)==107 and sum(orders)==890

    # Exact positive moment for ALL 890 original Taylor columns
    # across every one of 107 source blocks, preserving the
    # ORIGINAL finite/infinite remainder and same Taylor centers.
    spd_pivots=0
    for cluster,order in zip(refined,orders):
        mat,center,pivots=exact_block(cluster,order)
        assert mat[0][0]>0 and len(pivots)==order
        assert all(p>0 for p in pivots)
        spd_pivots+=len(pivots)
    assert spd_pivots==890
    eta_old=(1+1/TAU)*2*B*total_old*F(1,2**(2*BITS))
    eta_new=(1+1/TAU)*2*B*mass_new*F(1,2**(2*BITS))
    assert F(0)<eta_new<eta_old<ETA_UP
    # Pointwise wnew<=wold proves WHOLE-operator cap order,
    # not merely an entrywise/diagonal inequality.
    return refined,orders,{
        "subcells":subcells,
        "original_leaves":973,"new_subcells":n_refined,
        "clusters":107,"source_columns":sum(orders),
        "positive_subcells":protected_sub,
        "strictly_improved_subcells":improved_sub,
        "old_total_cap_mass":total_old,
        "new_total_cap_mass":mass_new,
        "mass_saved":total_old-mass_new,
        "mass_ratio":mass_new/total_old,
        "eta_old":eta_old,"eta_new":eta_new,
        "exact_spd_pivots":spd_pivots,
    }


def original_pilot_comparison(refined,orders,newtotal,n,pad):
    infos,old,oldorders,mass,width,oldtotal=geometry()
    assert orders==oldorders and len(old)==len(refined)==107
    sources=select_sources(infos)
    x,dx,v=physical_columns(n,infos,sources)
    H=(v.T@v)*dx;H=(H+H.T)/2
    a0,kneg,gramfft,ff=fourier_form(v,dx,pad)
    b=(v.T@np.sinh(x/2))*dx
    astar=a0-2*np.outer(b,b)
    astar=(astar+astar.T)/2
    c=linalg.solve(astar,H,assume_a="pos")
    G0=c.T@astar@c;G0=(G0+G0.T)/2
    oldcap,oldmeta=all_source_negative_cap(
        v,x,dx,old,orders,c,H,mass,oldtotal)
    newcap,newmeta=all_source_negative_cap(
        v,x,dx,refined,orders,c,H,mass,float(newtotal))
    direct=c.T@kneg@c;direct=(direct+direct.T)/2
    oldmax=float(linalg.eigh(oldcap,G0,eigvals_only=True)[-1])
    newmax=float(linalg.eigh(newcap,G0,eigvals_only=True)[-1])
    directmax=float(linalg.eigh(direct,G0,eigvals_only=True)[-1])
    # Numerically the refined original cap must be <= prior cap
    # in the whole 25-source matrix, as rigorously proved by
    # positive difference of entire pointwise frequency weights.
    residual=oldcap-newcap
    mineig=float(np.linalg.eigvalsh((residual+residual.T)/2)[0])
    denom=max(float(np.linalg.norm(oldcap)),1e-30)
    assert mineig>=-1e-8*denom,(
        "Pilot numeric cap ordering inconsistent; check moments",mineig,denom)
    assert newmax<=oldmax+1e-8*max(oldmax,1)
    assert abs(oldmeta["eta"]-float(
        (1+1/TAU)*2*B*F(str(oldtotal))*F(1,2**(2*BITS))))<1e-10
    return {
        "physical_grid":n,"fourier_padding":pad,
        "pilot_sources":len(sources),
        "original_negative_107_blocks":newmeta["blocks"],
        "original_negative_890_columns":newmeta["columns"],
        "sampled_original_direct_negative_generalized_max":directmax,
        "original_SM10_cap_generalized_max":oldmax,
        "SM37_refined_cap_generalized_max":newmax,
        "new_cap_to_direct_ratio":newmax/max(directmax,1e-30),
        "old_cap_to_direct_ratio":oldmax/max(directmax,1e-30),
        "refined_to_original_cap_ratio":newmax/oldmax,
        "original_theta_51_over_56":THETA,
        "cap_difference_min_eigenvalue_float":mineig,
        "old_eta_float":oldmeta["eta"],
        "new_eta_float":newmeta["eta"],
        "sampled_pole_denominator":float(1-2*b@linalg.solve(
            a0,b,assume_a="pos")),
        "sampled_fft_frequency_step":ff["freq_step"],
        "math_certifying":False,
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--subcells",type=int,default=SUBCELLS)
    parser.add_argument("--output",default="artifacts/sm37_refined_original_negative_cap.json")
    parser.add_argument("--quick",action="store_true")
    args=parser.parse_args()
    # No ACCEPTANCE from sampled frequency or sampled eigenvalues.
    d=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in d["obligations"] if x["id"]=="W-ODD-NEG")
    assert d["active_obligation"]=="W-ODD-NEG" and d["objective"]["status"]=="open"
    assert d["governance"]["no_automatic_promotion"] is True
    assert odd["status"]=="open" and "O1/O2" in odd["acceptance"]
    assert "SM37" in odd["evidence"] and "SM37" in d["evidence"]
    assert "sm37_refined_original_cap" in d["governance"]
    refined,orders,stats=refined_signed_original_cap(args.subcells)
    print("SM37 CERTIFIED ORIGINAL whole-real signed seven-prime"
          " refined negative multiplier upper 973->",
          stats["new_subcells"],"subcells in SAME 107 clusters"
          " and 890 source columns",flush=True)
    print("SM37 CERTIFIED exact rational old cap mass",
          float(stats["old_total_cap_mass"]),
          "NEW original cap mass",float(stats["new_total_cap_mass"]),
          "ratio",float(stats["mass_ratio"]),
          "saved",float(stats["mass_saved"]),flush=True)
    print("SM37 CERTIFIED old/new entire infinite original"
          " 24-bit Taylor eta",float(stats["eta_old"]),
          float(stats["eta_new"]),flush=True)
    assert stats["exact_spd_pivots"]==890
    print("SM37 CERTIFIED new source block 890 exact SPD pivots"
          " and WHOLE original operator cap K<=Knew<=Kold",
          flush=True)
    cases=[]
    for n,pad in ([(4096,4)] if args.quick else [
                    (4096,4),(8192,4),(8192,8)]):
        res=original_pilot_comparison(
            refined,orders,stats["new_total_cap_mass"],n,pad)
        print("SM37 NUMERICAL PILOT NONCERTIFYING",
              json.dumps(res,sort_keys=True),flush=True)
        cases.append(res)
    out={
        "status":"SCOPED_CERTIFIED_CAP_ENCLOSURE_WITH_NONCERTIFYING_RITZ",
        "canonical_odd_O1_O2":"open",
        "refined_exact_rational_cap":{
            k:(str(v) if isinstance(v,F) else v)
            for k,v in stats.items()
        },
        "original_pilot_comparisons":cases,
        "missing_whole_operator_certificates":[
            "Original full 470 odd positive pole-conditioned Astar inverse",
            "Original high positive archimedean log-frequency tail",
            "Original rigorously enclosed Galerkin strong residual",
            "Original all-470-source full matrix 51/56 or exact Feshbach sign",
            "Independent SI06/SM10 signed Fourier physical-domain analytic audit"
        ]
    }
    path=ROOT/args.output
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2,allow_nan=False)+"\n")
    print("SM37 SCOPED PASS: actual original whole-real negative"
          " CAP sharpened with 890 EXACT SPD pivots/107"
          " covariance blocks and full new eta."
          " Numerically sampled selected-source 25D trial is"
          " NONCERTIFYING. Full W-ODD-NEG O1/O2, original"
          " even E1-E4, full signed Weil, CC27, RH OPEN.",
          flush=True)


if __name__=="__main__":
    main()
