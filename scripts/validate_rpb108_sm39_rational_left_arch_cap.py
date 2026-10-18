#!/usr/bin/env python3
"""SM39: original signed 7-prime cap with RATIONAL subcell-left arch lower.

Entire ORIGINAL signed real-frequency proof, conditional on the
inherited SI06/SI07/SM10 original Fourier/form-domain identification:
- 973 true unresolved original negative source leaves remain
  covered on both signed frequency halves by 3892 rational subcells.
- SI07 arch_lower_cell(j) originally uses integer floor j,
  even for real xi far along [j,j+1].
- SI07 exact positive digamma series lower can be evaluated at
  ANY rational a>=0 (left original subcell endpoint), by monotonicity
  of the genuine Re psi(1/4+i*pi*xi)-log pi at xi>=0:
      arch_true(xi)>=arch_lower_at(a) for xi>=a.
- SI06 all-seven-prime rigorous midpoint interval and M=69
  derivative bound cover ALL real xi in original subcell [a,b]:
      m_true(xi)>=arch_lower_at(a)+prime_interval((a+b)/2).low
                    -69*(b-a)/2.
- Whole-cell nonnegative kappa-m upper is min of SM37 original
  certified subcell weight, plus outward round-up of new lower with
  positive 1e-6 floor. Hence 0<=Kneg<=Kcap_SM39<=Kcap_SM37
  for ENTIRE original physical odd operator on all signed frequency,
  with identical 107 original moment blocks and 890 physical Taylor
  source columns, and exact new eta for 24-bit residual.
- Exact rational moment integrations with all 890 strict LDL pivots.
- SAME SM38 25 genuine original source selected numerical Galerkin
  and analytically supported odd sine Fourier reference compare
  direct negative vs SM37 envelope and SM39 envelope/cap;
  Gauss/physical transforms and positive Astar trial are FLOAT,
  NONCERTIFYING and do not establish full original O1/O2 or RH.
"""
import argparse
import json
from functools import lru_cache
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from scipy import linalg

from validate_rpb108_si06_negative_band import (
    YFAC, CONST_UP, log_rational_bounds, prime_interval, B
)
from validate_rpb108_si07_negative_support_cover import (
    K as ARCH_K, M, DEN, ceil_fraction, arch_lower_cell
)
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm10_explicit_odd_cap_moments import (
    exact_block, BITS, TAU
)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_sm37_refined_original_negative_cap import (
    refined_signed_original_cap, FLOOR
)
from sm36_original_odd_numerical_pilot import (
    ROOT, geometry, select_sources, physical_columns, fourier_form,
    all_source_negative_cap, THETA
)
from sm38_leafwise_original_odd_fourier_audit import (
    prepare_real_subcells, supported_odd_sine_transform,
    generalized_max
)


@lru_cache(maxsize=None)
def arch_lower_at(left):
    """TRUE original arch lower for EVERY xi>=rational left>=0.

    This is literally the SI07 rational lower formula with j
    replaced by an arbitrary real-frequency rational left.

    Proof obligation: positive digamma expansion for t=pi*xi
      Re psi(1/4+i t)-log(pi)
       =-gamma-1/(1/4)+sum_{k>=1} [...]
    contributes increasing [t² / ((k+a)((k+a)²+t²))] and
    increasing integral-tail lower; SI07 lower rational YFAC<=pi
    and CONST_UP are unchanged. Thus the SI07 bound valid at
    integer j is valid at every rational left. No sampled
    multiplier signs are used to certify this assertion.
    """
    left=F(left)
    assert left>=0
    y=YFAC*left
    q=F(1,4)
    head=sum((y*y/((k+q)*((k+q)**2+y*y))
              for k in range(ARCH_K)),F(0))
    tail=log_rational_bounds(1+(y/(ARCH_K+q))**2)[0]/2
    return head+tail-CONST_UP


def new_original_arch_left_cap():
    prev,orders,prev_stats=refined_signed_original_cap(4)
    assert len(prev)==107 and sum(orders)==890
    assert M==69 and DEN==10**6
    # Recheck SAME original parent-source signed 3892 cells.
    new=[]
    mass_new=F(0);n_improved=0
    mass_from_arch=F(0);improvements=[]
    arch_gains=[]
    minprime=0
    n_sub=0;zero_floor=0
    for cluster,oldorder in zip(prev,orders):
        out=[]
        for a,b,hh_prev in cluster:
            j=a.numerator//a.denominator
            assert F(j)<=a and b<=j+1
            oldw=hh_prev+KAPPA
            assert oldw>=FLOOR
            arch_r=arch_lower_at(a)
            arch_j=arch_lower_cell(j)
            assert arch_r>=arch_j,(
                "SI07 rational arch monotonicity failed",a,j)
            ach=arch_r-arch_j
            arch_gains.append(ach)
            midpoint=(a+b)/2
            lowm=arch_r+prime_interval(midpoint)[0]-M*(b-a)/2
            want=max(F(0),KAPPA-lowm)
            up=F(ceil_fraction(want*DEN),DEN)
            neww=min(oldw,max(FLOOR,up))
            assert FLOOR<=neww<=oldw
            assert neww>=want or neww==oldw # inherited old cap
            if neww<oldw:
                n_improved+=1
                mass_from_arch+=2*(b-a)*(oldw-neww)
                improvements.append((a,b,oldw-neww))
            if neww==FLOOR:
                zero_floor+=1
            out.append((a,b,neww-KAPPA))
            mass_new+=2*(b-a)*neww
            n_sub+=1
        assert out[0][0]==cluster[0][0]
        assert out[-1][1]==cluster[-1][1]
        assert all(out[k][1]==out[k+1][0] for k in range(len(out)-1))
        new.append(out)
    assert n_sub==3892
    assert all(u>=0 for u in arch_gains)
    assert n_improved>0 and mass_from_arch>0
    assert mass_from_arch==prev_stats["new_total_cap_mass"]-mass_new
    assert mass_new>0
    assert mass_new<prev_stats["new_total_cap_mass"]
    # Actual observed SM39 full ORIGINAL exact-Fraction improvements
    # become hard certificate assertions, not float pilot claims.
    assert mass_new*10<prev_stats["new_total_cap_mass"]*7
    assert mass_from_arch>F(8)
    assert n_improved>2700

    # EXACT full 107 original source covariances; all cross
    # entries integrated rationally (not diagonal samples).
    n_pivots=0
    for cluster,p in zip(new,orders):
        assert p==taylor_order(cluster[-1][1]-cluster[0][0],BITS)[0]
        cov,c,pivots=exact_block(cluster,p)
        assert cov[0][0]>0 and len(pivots)==p
        assert all(x>0 for x in pivots)
        n_pivots+=p
    assert n_pivots==890
    eta=(1+1/TAU)*2*B*mass_new*F(1,2**(2*BITS))
    prev_eta=prev_stats["eta_new"]
    assert 0<eta<prev_eta
    # By pointwise w39<=w37, each full moment covariance
    # matrix is smaller in LOEWNER order, not merely entrywise.
    return prev,new,orders,{
        "original_parent_negative_leaves":973,
        "signed_rational_subcells":3892,
        "original_signed_covariance_blocks":107,
        "original_odd_negative_columns":n_pivots,
        "subcells_with_strict_weight_gain":n_improved,
        "subcells_at_strict_positive_floor":zero_floor,
        "old_SM37_full_signed_envelope_mass":prev_stats["new_total_cap_mass"],
        "SM39_full_signed_envelope_mass":mass_new,
        "exact_signed_mass_saved":mass_from_arch,
        "mass_ratio_SM39_over_SM37":mass_new/prev_stats["new_total_cap_mass"],
        "old_SM37_full_eta":prev_eta,
        "SM39_full_eta":eta,
        "max_exact_arch_left_over_integer_gain":max(arch_gains),
        "nonzero_arch_gain_subcells":sum(x>0 for x in arch_gains),
        "certified_full_moment_SPD_pivots":n_pivots,
        "max_source_weight_saved":max(v[2] for v in improvements)
    }


def same_original_25_source_pilot(prev,new,orders,stats,n,pad,gauss=16):
    # ONLY NUMERICAL diagnostics: actual original selected
    # positive Astar trial uses unbounded-arch FFT with no
    # complete true positive-frequency tail certificate.
    infos,old,oldorders,mass,width,oldtotal=geometry()
    assert orders==oldorders
    source=select_sources(infos)
    assert len(source)==25
    x,dx,v=physical_columns(n,infos,source)
    H=v.T@v*dx
    A0,_,_,_=fourier_form(v,dx,pad)
    pole=v.T@np.sinh(x/2)*dx
    As=A0-2*np.outer(pole,pole)
    As=(As+As.T)/2
    sol=linalg.solve(As,H,assume_a="pos")
    G=sol.T@As@sol
    G=(G+G.T)/2
    prevcap,oldmeta=all_source_negative_cap(
        v,x,dx,prev,orders,sol,H,mass,float(stats["old_SM37_full_signed_envelope_mass"]))
    newcap,newmeta=all_source_negative_cap(
        v,x,dx,new,orders,sol,H,mass,float(stats["SM39_full_signed_envelope_mass"]))
    # The frequency nodes of the ORIGINAL 3892 cells are unchanged.
    cs,hw,w39,wold,floors=prepare_real_subcells(new,old)
    ps,ph,w37,ow,fprev=prepare_real_subcells(prev,old)
    assert np.max(np.abs(cs-ps))==0 and np.max(np.abs(hw-ph))==0
    assert len(cs)==3892
    assert np.all(w39<=w37+1e-13)
    nodes,weights=np.polynomial.legendre.leggauss(gauss)
    xi=(cs[:,None]+hw[:,None]*nodes[None,:]).ravel()
    dw=(hw[:,None]*np.broadcast_to(weights,(
        len(cs),gauss))).ravel()
    Tx=supported_odd_sine_transform(xi,infos,source)@sol
    Fw=Tx.T
    def weighted(w):
        z=2*dw*np.repeat(w,gauss)
        A=Fw@(Tx*z[:,None])
        return (A+A.T)/2
    envelope37=weighted(w37)
    envelope39=weighted(w39)
    vals={
       "SM37_envelope_only":generalized_max(envelope37,G),
       "SM39_envelope_only":generalized_max(envelope39,G),
       "SM37_moment_cap":generalized_max(prevcap,G),
       "SM39_moment_cap":generalized_max(newcap,G)
    }
    a=vals["SM39_envelope_only"]
    b=vals["SM37_envelope_only"]
    c=vals["SM39_moment_cap"]
    d=vals["SM37_moment_cap"]
    # Floating sanity tests ONLY, inherited exact signed pointwise
    # envelope dominance independently proves operator order.
    assert a<=b+1e-8*max(b,1)
    assert c<=d+1e-8*max(d,1)
    # Observed sampled pilot spectral contraction -- NOT a theorem
    # about the original full signed odd operator.
    assert a/b<0.12 and c/d<0.12
    assert c>THETA # scoped original selected trial not yet below gate
    return {
      "physical_grid":n,"FFT_positive_padding":pad,
      "source_count":len(source),"gauss_order":gauss,
      "rigorous":False,"certifies_entire_W_odd":False,
      "same_source_trial_spectral_maxima":vals,
      "SM39_to_SM37_envelope_max_ratio":a/b,
      "SM39_to_SM37_moment_max_ratio":c/d,
      "new_full_moment_minus_envelope_num_min_eigenvalue":float(
          np.linalg.eigvalsh((newcap-envelope39+
                              (newcap-envelope39).T)/2)[0]),
      "original_signed_moment_columns":newmeta["columns"],
      "original_covariance_blocks":newmeta["blocks"]
    }


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm39_original_rational_left_arch_cap.json")
    p.add_argument("--quick",action="store_true")
    args=p.parse_args()
    m=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in m["obligations"] if x["id"]=="W-ODD-NEG")
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]=="open" and odd["status"]=="open"
    assert m["governance"]["no_automatic_promotion"] is True
    assert "O1/O2" in odd["acceptance"]
    assert all(z in m["evidence"] and z in odd["evidence"]
               for z in ("SM37","SM38","SM39"))
    assert "sm39_original_rational_left_arch" in m["governance"]
    prev,new,orders,stat=new_original_arch_left_cap()
    print("SM39 EXACT ORIGINAL signed 7-prime 3892 rational cells:"
          " arch at LEFT, all 107 original covariance clusters"
          " and 890 strict positive fraction LDL pivots.",flush=True)
    print("SM39 EXACT original SM37 signed total mass",
          float(stat["old_SM37_full_signed_envelope_mass"]),
          "new SM39",float(stat["SM39_full_signed_envelope_mass"]),
          "saved",float(stat["exact_signed_mass_saved"]),
          "ratio",float(stat["mass_ratio_SM39_over_SM37"]),
          "strictly improved cells",
          stat["subcells_with_strict_weight_gain"],flush=True)
    print("SM39 EXACT FULL original negative cap infinite eta"
          " prev",float(stat["old_SM37_full_eta"]),
          "new",float(stat["SM39_full_eta"]),flush=True)
    cases=[]
    for n,pad in ([(4096,4)] if args.quick else [(4096,4),(8192,8)]):
        q=same_original_25_source_pilot(
            prev,new,orders,stat,n,pad)
        print("SM39 NUMERICAL original source benchmark"
              " NONCERTIFYING",json.dumps(q,sort_keys=True),flush=True)
        cases.append(q)
    out={
        "status":"EXACT_ORIGINAL_SUBCELL_LOEWER_CERTIFICATE_AND_NONCERTIFYING_25D_RITZ",
        "canonical_odd_O1_O2":"open",
        "proof_scope":"ORIGINAL_TRUE_WHOLE_NEGATIVE_KNEG_UPPER_ONLY",
        "original_exact_Fraction_enclosure":{
            k:(str(v) if isinstance(v,F) else v)
            for k,v in stat.items()
        },
        "same_source_numerical_pilot":cases,
        "still_missing":[
          "complete original positive archimedean logarithmic frequency tail",
          "full original 470 source Astar resolvent/strong residual",
          "rigorous original frequency quadrature interval matrix",
          "complete original 470 generalized theta 51/56 or corrected Schur",
          "independent original SI06/SI07/SM10 Fourier/domain audit"
        ]
    }
    dest=ROOT/args.output
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+"\n")
    print("SM39 SCOPED: FULL original signed Kneg upper cap"
          " improved via exact rational left-arch frequency"
          " intervals and entire 890 source Loewner reduction."
          " No original complete signed Wodd O1/O2,"
          " even E1-E4, Weil, CC27 or RH promotion.",flush=True)


if __name__=="__main__":
    main()
