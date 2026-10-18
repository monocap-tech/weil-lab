#!/usr/bin/env python3
"""SM33 TRUE original ODD full negative-frequency mixed coupling.

Original signed 7-prime SI10 protected cover (973 original leaves,
107 source clusters), odd parity E9<=470:
  M_j = 2 sum_{leaves in J_j} h_leaf * leaf_length,
  e_j = (pi_up B width_j)^p_j / p_j! < 2^-9.
For Q = physical odd orthogonal projection away from E9:
  0 <= Q Kneg Q <= eps_neg I,
  eps_neg = 2B sum_j M_j e_j^2.
Globally 0<=Kneg <= H_neg I, H_neg=2B sum M_j.
Thus ||Q Kneg P||^2 <= H_neg eps_neg = gamma_neg2.
True original FULL positive infinite D=Q Wo Q >=mu I, mu=17/25000,
gives NEGATIVE-ONLY correction
  0 <= (Q Kneg P)^* D^-1(Q Kneg P)
      <= (gamma_neg2/mu) I.
The actual full cross is C=C_plus-C_minus; C_plus from the
ORIGINAL unbounded positive multiplier is NOT estimated. The exact
source pole and scalar kappa both have zero Q-to-P coupling, since
s is contained in E9 and P,Q physically orthogonal.

This certificate cannot promote the full original <=470D Schur
or W-ODD-NEG O1/O2. All proof theory external to arithmetic needs
independent functional-analytic and Fourier-domain audit.
"""
from fractions import Fraction as F
from pathlib import Path
import json

from validate_rpb108_si10_complement_positivity import (
    protected_inner_cover, protected_outer_band, KAPPA, B
)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_sm32_parity_cofinite_odd_schur import MU, BITS

ROOT=Path(__file__).resolve().parents[1]
COMMON_REMAINDER=F(1,2**BITS)
CROSS2_MAX=F(27,1000)
NEG_CORRECTION_MAX=F(40)


def full_original_clusterwise_negative_mixed():
    leaves_high,min_positive=protected_outer_band()
    clusters,width,mass,nleaves,naccepted=protected_inner_cover()
    assert leaves_high==2535 and min_positive>KAPPA
    assert nleaves==973 and naccepted==9261
    assert len(clusters)==107
    assert width==F(973,32) and F(0)<mass<F(38)
    assert B==F(11,10) and KAPPA==F(1,1000) and BITS==9

    mass_check=F(0)
    weighted_squared=F(0)
    norm_source_count=0
    max_rem=F(0)
    e2_max_weight=F(0)
    errors=[]
    masses=[]
    strict_improvements=0
    nontrivial=0
    for l,r,mj in clusters:
        assert l<r and mj>=0
        p,ej=taylor_order(r-l,BITS)
        assert p>=1 and F(0)<ej<COMMON_REMAINDER
        mass_check+=mj
        weighted_squared+=mj*ej*ej
        norm_source_count+=p
        max_rem=max(max_rem,ej)
        if mj>0:
            nontrivial+=1
            strict_improvements+=int(ej<COMMON_REMAINDER)
        errors.append(ej)
        masses.append(mj)

    assert mass_check==mass
    assert len(errors)==len(masses)==107
    assert norm_source_count==469
    assert norm_source_count+1==470
    assert nontrivial>0 and strict_improvements==nontrivial
    assert max_rem<COMMON_REMAINDER

    # Full ORIGINAL signed negative multiplier integral weight mass,
    # including BOTH +/- mirrored frequency halves. Odd sine packet
    # physical Taylor residual in each cluster bounds Q Kneg Q.
    leakage=2*B*weighted_squared
    worst_leak=2*B*mass*COMMON_REMAINDER**2
    assert 0<leakage<worst_leak
    # Strict source-specific original negative-frequency leakage
    # improvement from the full 107 weighted Taylor cluster errors.
    assert leakage<F(1,15000)
    # The positive frequency Kneg is globally bounded from true
    # physical support, without any 470-source orthonormalization.
    H=2*B*mass
    gamma2=H*leakage
    rough_gamma2=H*worst_leak
    assert 0<gamma2<rough_gamma2
    assert H<F(83) and rough_gamma2<F(27,1000)
    assert gamma2<CROSS2_MAX
    assert gamma2<F(11,2000) # STRICT original measured mixed² upper

    # Complete original D=Q Wodd Q >=mu I, so 0<=D^-1<=mu^-1 I.
    # This controls *only* Cminus*D^-1 Cminus, never full signed C.
    correction=gamma2/MU
    assert MU==F(17,25000)
    assert correction<NEG_CORRECTION_MAX
    assert correction<F(81,10) # exact measured original negative-only D^-1 response

    # Uniform true original SI10 complete SIGNED complement has
    # original full protected-positive multiplier and all negative
    # leaves, hence an actual finite-codimension physical coercivity.
    eps2=COMMON_REMAINDER**2
    actual_mu=KAPPA*(1-2*B*width*eps2)-2*B*mass*eps2
    assert actual_mu>MU
    return {
        "clusters":len(clusters),"leaves":nleaves,
        "accepted":naccepted,"source_count":norm_source_count+1,
        "mass":mass,"max_e":max_rem,"leak":leakage,
        "coarse_leak":worst_leak,
        "neg_global_norm":H,
        "cross2":gamma2,"cross2_coarse":rough_gamma2,
        "negative_only_schur_correction":correction,
        "original_complement_floor":actual_mu,
        "weighted_error_mass":weighted_squared,
        "nonzero_mass_clusters":nontrivial,
    }


def signed_schur_adversarial_regression():
    # An original-style strictly positive infinite D and
    # positive uncorrected finite block A do not entail total
    # signed form PSD, even if the negative cross Cminus is zero.
    mu=MU
    A=F(1)
    cminus=F(0)
    cplus=F(1)
    C=cplus-cminus
    corrected=A-C*C/mu
    assert A>0 and mu>0 and corrected<0
    # A small Cminus can fail to repair unbounded Cplus:
    small=F(1,10000)
    assert small**2<CROSS2_MAX
    corrected2=A-(cplus-small)**2/mu
    assert corrected2<0
    # Conversely a real PLUS cross may cancel minus cross,
    # so the separate negative-only inverse cannot substitute
    # for the full operator's signed mixed correction.
    cplus2=small
    cminus2=small
    corrected3=A-(cplus2-cminus2)**2/mu
    assert corrected3==A
    # Exact conditional triangle norm test, no original Cplus bound.
    gam_minus=F(1,10)
    gam_plus=F(1,100)
    triangle2=(gam_minus+gam_plus)**2
    assert triangle2>gam_minus**2
    assert A-triangle2/mu<0
    return corrected,corrected2,corrected3


def run():
    m=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in m["obligations"] if x["id"]=="W-ODD-NEG")
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]=="open"
    assert m["governance"]["no_automatic_promotion"] is True
    assert odd["status"]=="open" and "O1/O2" in odd["acceptance"]
    assert "SM32" in m["evidence"] and "SM33" in m["evidence"]
    assert "SM32" in odd["evidence"] and "SM33" in odd["evidence"]
    assert "full_original_odd_negative_mixed_acceptance" in m["governance"]

    r=full_original_clusterwise_negative_mixed()
    bad1,bad2,good=signed_schur_adversarial_regression()
    print("SM33 original full signed seven-prime cover",
          r["leaves"],"leaves",r["clusters"],"clusters",
          r["accepted"],"protected cells",flush=True)
    print("SM33 TRUE original odd exceptional physical source count",
          r["source_count"],"including negative odd pole",flush=True)
    print("SM33 all original negative leaf scalar mass",
          float(r["mass"]),"global operator norm bound",
          float(r["neg_global_norm"]),flush=True)
    print("SM33 107 true original cluster-specific b9 Taylor"
          " remainder maximum",float(r["max_e"]),
          "vs coarse",float(COMMON_REMAINDER),flush=True)
    print("SM33 TRUE original entire odd complementary"
          " Kneg leakage operator norm upper",float(r["leak"]),
          "coarse",float(r["coarse_leak"]),flush=True)
    print("SM33 TRUE original entire negative signed physical"
          " 470-vs-infinite mixed operator squared norm upper",
          float(r["cross2"]),"coarse",float(r["cross2_coarse"]),
          "<27/1000",flush=True)
    print("SM33 TRUE original infinite D inverse, NEGATIVE-ONLY"
          " complete Schur correction upper",
          float(r["negative_only_schur_correction"]),
          "<40 (deliberately conservative)",flush=True)
    print("SM33 true full signed original QWoddQ physical floor",
          float(r["original_complement_floor"]),">17/25000",flush=True)
    print("SM33 original whole signed C = Cplus - Cminus;"
          " both original odd-pole and kappa scalar cross vanish"
          " on P/Q, but Cplus full original continuum UNMEASURED.",
          flush=True)
    print("SM33 exact finite rational full Schur adversarial"
          " negative determinants, cancellation mode:",
          float(bad1),float(bad2),float(good),flush=True)
    print("SM33 PASS SCOPED ORIGINAL: ALL 973 real original"
          " seven-prime negative leaves and 107 cluster-specific"
          " errors give a TRUE finite-vs-infinite original odd"
          " NEGATIVE-FREQUENCY cross bound and a complete"
          " negative-only D^-1 correction ceiling. This does"
          " NOT certify Cplus, the true full signed C,"
          " corrected original exceptional 470D spectral PSD,"
          " O1/O2 full odd, even E1-E4, whole Weil,"
          " CC27 D-Riesz or RH. Analytic original form audit"
          " remains independent.",flush=True)


if __name__=="__main__":
    run()
