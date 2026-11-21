#!/usr/bin/env python3
"""IV030 exact rational witness for the failure of graph+mass-only prime reconstruction.

The underlying genuine Schwartz construction is a nonzero nonnegative real
C-infinity bump phi in a rational subinterval A of the original left NF543
collar, and its log(9) translate psi(x)=phi(x-log(9)) in the right collar.
For f_beta=phi+beta psi, beta in {1,-1,i}, the authentic ORIGINAL
von-Mangoldt prime sum is P(f_beta,f_beta)=2*(log(3)/3)*J*Re(beta), where
J=integral phi(x)^2 dx>0 is the same for every beta; Mass(f_beta)=2J.
The program rigorously checks the log bounds, active-prime separation and
phase identities; it does NOT construct phi in Lean, compute J, or prove RH.
"""
from __future__ import annotations
import json
from fractions import Fraction as Q
from pathlib import Path

OUT = Path("iv030-original-old-n9-phase-no-go-exact-rational-NONKERNEL.json")
TERMS = 96

def log_bracket(n: int) -> tuple[Q,Q]:
    assert isinstance(n,int) and n>=1
    y=Q(n-1,n+1)
    s=sum((2*y**(2*k+1)/Q(2*k+1) for k in range(TERMS)),Q(0))
    tail=2*y**(2*TERMS+1)/Q(2*TERMS+1)/(1-y*y)
    return s,s+tail

def abs_lower(lo: Q,hi: Q)->Q:
    assert lo<=hi
    if lo>0:return lo
    if hi<0:return -hi
    return Q(0)

def frac(v:Q)->str:return f"{v.numerator}/{v.denominator}"

# Arbitrary real nonnegative bump strictly supported inside this closed
# rational subinterval, not an indicator itself. The Schwartz bump
# construction is external mathematics, not a formalized Lean proof.
A_LO=Q(-1099,1000)
A_HI=Q(-5494,5000)
OLD_L_LO=-Q(11,10)
OLD_L_HI=-Q(549,500)
OLD_R_LO=Q(549,500)
OLD_R_HI=Q(11,10)
ACTIVE=(2,3,4,5,7,8,9)

# Tiny exact Gaussian-rational complex representation for evaluating
# phase coefficients; J and kappa stay SYMBOLIC positive scalars.
class CQ:
    def __init__(self,re,im=0): self.re,self.im=Q(re),Q(im)
    def conj(self):return CQ(self.re,-self.im)
    def __mul__(self,z):return CQ(self.re*z.re-self.im*z.im,self.re*z.im+self.im*z.re)
    def __add__(self,z):return CQ(self.re+z.re,self.im+z.im)
    def sqabs(self):return self.re**2+self.im**2
    def __eq__(self,z):return isinstance(z,CQ) and (self.re,self.im)==(z.re,z.im)

def preflight():
    lo9,hi9=log_bracket(9)
    lo3,hi3=log_bracket(3)
    assert OLD_L_LO<A_LO<A_HI<OLD_L_HI
    assert OLD_R_LO<A_LO+lo9
    assert A_HI+hi9<OLD_R_HI
    assert lo9>0 and lo3>0 and hi3<Q(6,5)
    w=A_HI-A_LO
    assert w==Q(1,5000)
    assert lo9>w
    min_non9=None
    prime_separation={}
    # Actual left/right bump supports are A and A+log9. For original
    # tau=±log n, a different n cannot couple these 2 cells.
    for n in ACTIVE:
        lo,hi=log_bracket(n)
        if n==9:
            prime_separation[n]="retained_both_signed_orientations"
            continue
        # The right-left gap at +log n is log9-logn. The opposite
        # orientation requires log9+logn. Both are > bump width.
        lower=abs_lower(lo9-hi,hi9-lo)
        assert lower>w,("unexpected new translated correlation",n)
        assert lo9+lo>w
        assert lo>w  # same-cell self-overlap is excluded too.
        min_non9=lower-w if min_non9 is None else min(min_non9,lower-w)
        prime_separation[n]="no_bump_overlap_at_either_sign"
    assert min_non9>0

    # Four actual complex test families f_beta=phi+beta*translate(phi).
    # Their supports agree, and their physical L2 Mass = 2*J.
    # Because the authentic first slot is antilinear, the source
    # correlations at ±log9 equal beta*conj(1)*J and conj(beta)*J.
    # Their two-sign prime sum has phase coefficient 2*Re(beta)*J.
    betas={"positive":CQ(1),"negative":CQ(-1),"zero":CQ(0,1)}
    phases={}
    for name,beta in betas.items():
        cplus=beta*CQ(1).conj()
        cminus=CQ(1)*beta.conj()
        assert cminus==cplus.conj()
        assert cplus.im+cminus.im==0
        assert CQ(1).sqabs()+beta.sqabs()==2
        phases[name]={
            "beta":f"{frac(beta.re)}+({frac(beta.im)})i",
            "C_plus_over_J":f"{frac(cplus.re)}+({frac(cplus.im)})i",
            "C_minus_over_J":f"{frac(cminus.re)}+({frac(cminus.im)})i",
            "full_prime_P_over_(kappa_J)":frac(cplus.re+cminus.re),
            "Mass_over_J":"2",
            "prime_over_Mass_over_kappa":frac((cplus.re+cminus.re)/2),
            "physical_support_unchanged":True,
        }
    assert [Q(phases[n]["full_prime_P_over_(kappa_J)"]) for n in ("positive","negative","zero")]==[2,-2,0]
    assert [Q(phases[n]["prime_over_Mass_over_kappa"]) for n in ("positive","negative","zero")]==[1,-1,0]

    # The true source coefficient kappa=Lambda(9)/sqrt9=log3/3 is
    # positive and smaller than NF600's coarse 2/5 allowance.
    assert Q(0)<lo3/Q(3)
    assert hi3/Q(3)<Q(2,5)
    receipt={
      "schema":"IV030-original-prime-phase-fidelity-graph-mass-no-go-v1",
      "true_NF543_original_left_open_interval":[frac(OLD_L_LO),frac(OLD_L_HI)],
      "true_NF543_original_right_open_interval":[frac(OLD_R_LO),frac(OLD_R_HI)],
      "rational_left_smooth_bump_support_inside":[frac(A_LO),frac(A_HI)],
      "right_smooth_bump_is_exact_log9_translate_of_left":True,
      "translated_bump_support_strictly_inside_original_right":True,
      "positive_real_smooth_compact_bump_phi_exists_mathematically_not_Lean":True,
      "log9_rigorous_rational_bracket_terms":TERMS,
      "min_other_prime_strict_overlap_clearance_lower_1e6":frac(Q((min_non9*10**6).numerator//(min_non9*10**6).denominator,10**6)),
      "actual_original_active_prime_powers_below10":list(ACTIVE),
      "shift_classification":prime_separation,
      "authentic_original_n9_coefficient":"kappa=vonMangoldt(9)/sqrt(9)=log(3)/3>0",
      "nf600_original_kappa_strictly_less_than_twoFifths":True,
      "same_support_and_same_mass_phase_families":phases,
      "symbolic_J":"J=integral(phi(x)^2)dx>0 for real smooth nonzero phi",
      "exact_prime_pairing_law":"P(f_beta,f_beta)=2*kappa*J*Re(beta)",
      "exact_mass_law":"Mass(f_beta)=2*J for beta in {1,-1,i}",
      "conclusion":"NO universal reconstruction of original prime quadratic P from just support overlap graph and physical L2 mass; missing relative complex phase/mixed pairing values",
      "graph_and_mass_do_not_determine_prime_value":True,
      "this_does_NOT_show_full_original_Weil_form_negative":True,
      "formal_Lean_Schwartz_bump_and_prime_identity_certified":False,
      "independent_spectral_equivalence_proved":False,
      "global_Weil_positivity_proved":False,
      "RH_proved":False,
    }
    OUT.write_text(json.dumps(receipt,sort_keys=True,indent=2)+"\n")
    print("IV030 exact-rational PHASE OBSTRUCTION PASS: same source support and Mass=2J, true original P/(kappa*J) in {+2,-2,0}; other active n excluded, correct original ±log9; NOT Lean or RH.")
    return receipt

if __name__=='__main__': preflight()
