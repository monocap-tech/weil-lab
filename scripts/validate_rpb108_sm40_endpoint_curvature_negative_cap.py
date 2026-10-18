#!/usr/bin/env python3
"""SM40: exact original signed seven-prime ENDPOINT CURVATURE cap.

RIGOROUS SCOPED OPERATOR result under inherited SI06/SI07/SM10
Fourier/domain premises; not original signed odd W_o positivity:
 For every one of the original 3892 SI10/SM39 negative-frequency
 rational subcells [a,b], SI06 prime_interval(a/b) encloses the
 ORIGINAL seven-prime signed p(xi) at both endpoints.
 p''(xi)=8*pi^2 sum_n w_n(log n)^2*cos(2*pi*xi*log n)
 (sign may vary), so D2=8*pi_up^2 sum w_hi*log(n)_hi^2
 bounds abs(p'') at EVERY real xi.
 Linear interpolation error gives
     p(xi)>=min(p_lo(a),p_lo(b))-D2*(b-a)^2/8
 for ALL xi in the entire closed subcell, not sampled nodes.
 SI07 original rational arch_lower_at(a) is separately a lower
 for the original arch on ALL xi>=a; thus
     m(xi)>=arch_lower_at(a)+min(endpoint p_lo)-D2*h^2/8.
 Taking pointwise min of SM39 verified upper and outward rounded
 (kappa-lower)_+ with original 1e-6 floor proves a NEW
 true entire original Kneg upper <= SM39 cap in operator Loewner.
 Same exact 107 source centers, 890 Taylor columns and full
 residual eta; entire rational moment covariances exact SPD.

Original 25 selected physical source/trial tests remain FLOAT,
NONCERTIFYING due incomplete Astar-positive high-log Fourier tail,
missing true original Astar inverse/strong residual, and incomplete
470 source generalized spectral test. Odd O1/O2, Weil/RH OPEN.
"""
import argparse
import json
from fractions import Fraction as F

import numpy as np
from scipy import linalg

from validate_rpb108_si06_negative_band import (
    PI, ACTIVE, WEIGHTS, SHIFTS, prime_interval, B
)
from validate_rpb108_si07_negative_support_cover import (
    DEN, ceil_fraction
)
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm10_explicit_odd_cap_moments import (
    BITS, TAU, exact_block
)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_sm39_rational_left_arch_cap import (
    arch_lower_at, new_original_arch_left_cap
)
from sm36_original_odd_numerical_pilot import (
    ROOT, THETA, geometry, select_sources, physical_columns,
    fourier_form, all_source_negative_cap, original_multiplier
)
from sm38_leafwise_original_odd_fourier_audit import (
    prepare_real_subcells, supported_odd_sine_transform,
    generalized_max
)

# Exact rational genuine all-seven-prime |p''| global ceiling.
# This is NOT the old global first derivative M=69: it is
# multiplied by the much smaller ORIGINAL subcell width^2/8.
D2=8*PI[1]*PI[1]*sum(
    (WEIGHTS[n][1]*SHIFTS[n][1]*SHIFTS[n][1] for n in ACTIVE), F(0)
)
FLOOR=F(1,DEN)


def endpoint_interpolation_adversarial():
    """Exact-rational sharpness test of the second-derivative error.

    On [a,b], q(x)=(D2/2)(x-a)(x-b) has endpoints ZERO but
    q(mid)=-D2*(b-a)^2/8. Endpoint minimum alone would be
    invalid, and the curvature payment is exactly necessary.
    """
    a,b=F(3,10),F(3,10)+F(1,256)
    mid=(a+b)/2
    def q(x): return D2*(x-a)*(x-b)/2
    assert q(a)==q(b)==0
    assert q(mid)==-D2*(b-a)**2/8
    assert q(mid)<0
    assert D2>F(600) and D2<F(900)
    return D2*(b-a)**2/8


def refined_original_endpoint_curvature():
    prev37,prev39,orders,s39=new_original_arch_left_cap()
    assert len(prev39)==107 and sum(orders)==890
    assert s39["signed_rational_subcells"]==3892
    endpoint_interpolation_adversarial()

    refined=[];mass_new=F(0);improved=0;floor_cells=0
    max_curve=F(0);weight_reduction=F(0);all_sub=0
    significant=0
    for cluster in prev39:
        out=[]
        for a,b,h_prev in cluster:
            assert F(0)<=a<b and (b-a)<=F(1,256)
            prev_weight=h_prev+KAPPA
            assert prev_weight>=FLOOR
            # Exact SI06 original full seven-prime cosine-phase
            # enclosures at both endpoints, including each log p
            # coefficient, prime powers n=4,8,9 and pi bounds.
            pa=prime_interval(a)[0]
            pb=prime_interval(b)[0]
            curve=D2*(b-a)**2/8
            max_curve=max(max_curve,curve)
            low=arch_lower_at(a)+min(pa,pb)-curve
            true_need=max(F(0),KAPPA-low)
            outward=F(ceil_fraction(true_need*DEN),DEN)
            candidate=max(FLOOR,outward)
            w=min(prev_weight,candidate)
            assert FLOOR<=w<=prev_weight
            # Both inherited previous true whole-cell upper and
            # current endpoint-curvature upper independently pay
            # actual original real frequency signed-negative.
            assert w>=true_need or w==prev_weight
            if w<prev_weight:
                improved+=1
                delta=prev_weight-w
                weight_reduction+=2*(b-a)*delta
                if delta>F(1,100):significant+=1
            if w==FLOOR:floor_cells+=1
            out.append((a,b,w-KAPPA))
            mass_new+=2*(b-a)*w
            all_sub+=1
        assert len(out)==len(cluster)
        assert all(out[i][:2]==cluster[i][:2] for i in range(len(out)))
        assert all(out[i][1]==out[i+1][0] for i in range(len(out)-1))
        refined.append(out)
    assert all_sub==3892 and len(refined)==107
    oldmass=s39["SM39_full_signed_envelope_mass"]
    assert mass_new<=oldmass
    assert weight_reduction==oldmass-mass_new
    assert improved>0 and mass_new>0

    pivots=0
    for cluster,p in zip(refined,orders):
        assert p==taylor_order(cluster[-1][1]-cluster[0][0],BITS)[0]
        mat,c,ds=exact_block(cluster,p)
        assert len(ds)==p and all(d>0 for d in ds)
        assert mat[0][0]>0
        pivots+=p
    assert pivots==890
    eta=(1+1/TAU)*2*B*mass_new*F(1,2**(2*BITS))
    assert eta>0 and eta<=s39["SM39_full_eta"]

    return prev39,refined,orders,{
      "original_signed_negative_parent_leaves":973,
      "all_original_signed_subcells":3892,
      "original_complete_clusters":107,
      "unchanged_original_taylor_columns":890,
      "original_exact_SPD_pivots":pivots,
      "original_prime_second_derivative_bound":D2,
      "max_original_real_cell_interpolation_error":max_curve,
      "old_SM39_signed_envelope_mass":oldmass,
      "new_SM40_signed_envelope_mass":mass_new,
      "exact_original_mass_saved":oldmass-mass_new,
      "new_over_old_signed_mass_ratio":mass_new/oldmass,
      "strictly_improved_subcells":improved,
      "subcells_with_weight_gain_over_0_01":significant,
      "original_positive_floor_subcells":floor_cells,
      "old_SM39_full_Taylor_eta":s39["SM39_full_eta"],
      "new_SM40_full_Taylor_eta":eta,
      "adversarial_endpoint_curvature_test":"PASSED"
    }


def original_same_25_source_probe(previous,new,orders,stats,n,pad,gauss=16):
    """Exact SAME actual selected 25 original physical odd sources.

    Positive sampled Astar trial is NUMERICAL only; all selected
    generalized spectral maxima are NONCERTIFYING.
    """
    infos,old,oldorders,mass,width,oldtotal=geometry()
    assert oldorders==orders
    sources=select_sources(infos)
    assert len(sources)==25
    x,dx,v=physical_columns(n,infos,sources)
    H=(v.T@v)*dx
    A0,_,_,_=fourier_form(v,dx,pad)
    pole=(v.T@np.sinh(x/2))*dx
    Astar=A0-2*np.outer(pole,pole)
    Astar=(Astar+Astar.T)/2
    z=linalg.solve(Astar,H,assume_a="pos")
    G=z.T@Astar@z
    G=(G+G.T)/2

    oldcap,_=all_source_negative_cap(
        v,x,dx,previous,orders,z,H,mass,
        float(stats["old_SM39_signed_envelope_mass"]))
    newcap,newmeta=all_source_negative_cap(
        v,x,dx,new,orders,z,H,mass,
        float(stats["new_SM40_signed_envelope_mass"]))
    cs,hw,wn,wo,floor=prepare_real_subcells(new,old)
    pc,ph,wp,_,_=prepare_real_subcells(previous,old)
    assert np.array_equal(cs,pc) and np.array_equal(hw,ph)
    assert np.all(wn<=wp+1e-12)
    nodes,weights=np.polynomial.legendre.leggauss(gauss)
    xi=(cs[:,None]+hw[:,None]*nodes[None,:]).reshape(-1)
    q=(hw[:,None]*np.broadcast_to(weights,(3892,gauss))).reshape(-1)
    Tx=supported_odd_sine_transform(xi,infos,sources)@z
    actual_w=np.maximum(0.,float(KAPPA)-original_multiplier(xi))
    def integral(w):
        ww=2*q*w
        result=Tx.T@(Tx*ww[:,None])
        return (result+result.T)/2
    direct=integral(actual_w)
    prev_e=integral(np.repeat(wp,gauss))
    new_e=integral(np.repeat(wn,gauss))
    values={
      "same_original_leafwise_direct":generalized_max(direct,G),
      "SM39_envelope_only":generalized_max(prev_e,G),
      "SM40_envelope_only":generalized_max(new_e,G),
      "SM39_full_890_moment_cap":generalized_max(oldcap,G),
      "SM40_full_890_moment_cap":generalized_max(newcap,G)
    }
    assert values["SM40_envelope_only"]<=values["SM39_envelope_only"]+1e-7
    assert values["SM40_full_890_moment_cap"]<=values["SM39_full_890_moment_cap"]+1e-7
    assert newmeta["columns"]==890 and newmeta["blocks"]==107
    return {
      "physical_grid":n,"FFT_positive_padding":pad,
      "selected_actual_original_source_count":25,
      "signed_frequency_gauss_order":gauss,
      "numerical_only":True,"certifies_original_odd_O1_O2":False,
      "same_original_source_selected_generalized_maxima":values,
      "new_moment_to_SM39_ratio":
        values["SM40_full_890_moment_cap"]/values["SM39_full_890_moment_cap"],
      "SM40_full_cap_over_direct_ratio":
        values["SM40_full_890_moment_cap"]/max(values["same_original_leafwise_direct"],1e-30),
      "new_envelope_minus_true_sampled_weight_max_violation":float(
        np.max(actual_w-np.repeat(wn,gauss))),
      "original_890_moment_source_columns":newmeta["columns"]
    }


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--quick",action="store_true")
    p.add_argument("--output",default="artifacts/sm40_endpoint_curvature_original_cap.json")
    args=p.parse_args()
    m=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(v for v in m["obligations"] if v["id"]=="W-ODD-NEG")
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]=="open" and odd["status"]=="open"
    assert m["governance"]["no_automatic_promotion"] is True
    assert all(z in m["evidence"] and z in odd["evidence"]
               for z in ("SM38","SM39","SM40"))
    assert "sm40_original_endpoint_curvature_negative_cap" in m["governance"]
    previous,new,orders,stats=refined_original_endpoint_curvature()
    print("SM40 exact original REAL seven-prime endpoint curvature:"
          " D2",float(D2),"max subcell interpolation remainder",
          float(stats["max_original_real_cell_interpolation_error"]),
          "all 3892 original signed subcells, same 107/890 source",
          " pivots",stats["original_exact_SPD_pivots"],flush=True)
    print("SM40 exact original full Kneg signed mass SM39",
          float(stats["old_SM39_signed_envelope_mass"]),
          "SM40",float(stats["new_SM40_signed_envelope_mass"]),
          "saved",float(stats["exact_original_mass_saved"]),
          "ratio",float(stats["new_over_old_signed_mass_ratio"]),
          "improved cells",stats["strictly_improved_subcells"],flush=True)
    assert stats["original_exact_SPD_pivots"]==890
    cases=[]
    for n,pad in ([(4096,4)] if args.quick else [(4096,4),(8192,8)]):
        r=original_same_25_source_probe(previous,new,orders,stats,n,pad)
        cases.append(r)
        print("SM40 NONCERTIFYING original 25-source Gauss diagnostic",
              json.dumps(r,sort_keys=True),flush=True)
    out={
      "status":"EXACT_ORIGINAL_ENDPOINT_CURVATURE_FULL_KNEG_UPPER_PLUS_NUMERICAL_DIAGNOSTIC",
      "canonical_original_W_ODD_NEG":"OPEN",
      "exact_original_complete_negative_operator_cap":{
          k:(str(v) if isinstance(v,F) else v)
          for k,v in stats.items()
      },
      "numerical_same_actual_original_25_source_pilot":cases,
      "not_proved":[
          "original complete odd signed W_o=Astar-Kneg >=0 O1/O2",
          "original true positive arch digamma logarithmic high frequency form tail",
          "original full 470 source Astar inverse / strong resolvent residual",
          "complete 470 source generalized 51/56 Loewner or exact Schur",
          "even E1-E4 whole signed Weil CC27 transfer and RH"
      ]
    }
    dest=ROOT/args.output
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+"\n")
    print("SM40 SCOPED PASS: exact original whole-real signed"
          " seven-prime negative Kneg upper SMALLER by Loewner"
          " than SM39 with same 107 exact moment blocks / 890"
          " SPD source pivots; original signed odd Wodd O1/O2,"
          " even E1-E4 full Weil CC27 and RH OPEN.",flush=True)


if __name__=="__main__":
    main()
