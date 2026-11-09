#!/usr/bin/env python3
"""NF488: SOURCE-PINNED ORIGINAL J8 terminal 4-moment remainder decision gate.

This computes a rigorously enclosed *explicit* baseline A of the ORIGINAL
terminal physical signed integral, after the source-exact NF487 whole-z
logarithmic cusp is removed:
 z(B-d) = Z + alpha*d*log(B/d) + R(d), alpha=-U'(B)/2.
 D_terminal = A + (4vC+4Z)*M0 + 2v*M1 + 4alpha*M2 + 2M3,
 M0=int R, M1=int L R, M2=int d L R, M3=int R^2.

A is an exact analytic moment of REAL ORIGINAL source endpoint data.
The M0..M3 are NOT computed here. No RH / full J8 upper claim.

Pure exact Fraction rational arithmetic and independently sourced
NF411/NF450/NF479/NF482 original JSON custody, no floating point
needed for verification or source bounds.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib, json, re, sys
from decimal import Decimal, localcontext

if hasattr(sys, "set_int_max_str_digits"): sys.set_int_max_str_digits(0)
B=F(11,10)
DELTA=F(1,500)
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
WEIGHTS=(2,3,4,5,7,8,9)

def load(path):
    p=Path(path)
    b=p.read_bytes()
    return json.loads(b),hashlib.sha256(b).hexdigest()

class Iv:
    def __init__(self,lo,hi=None):
        self.lo=F(lo)
        self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def _as(self,o): return o if isinstance(o,Iv) else Iv(o)
    def __add__(self,o):
        o=self._as(o);return Iv(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return Iv(-self.hi,-self.lo)
    def __sub__(self,o):return self+(-self._as(o))
    def __rsub__(self,o):return self._as(o)+(-self)
    def __mul__(self,o):
        o=self._as(o)
        t=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
        return Iv(min(t),max(t))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=self._as(o)
        assert o.lo*o.hi>0, "division through zero interval"
        return self*Iv(1/o.hi,1/o.lo)
    def __pow__(self,k):
        assert isinstance(k,int) and k>=0
        if k==0: return Iv(1)
        if k%2==1:
            return Iv(self.lo**k,self.hi**k)
        lo=F(0) if self.lo<=0<=self.hi else min(self.lo**k,self.hi**k)
        return Iv(lo,max(self.lo**k,self.hi**k))
    def raw(self):return [str(self.lo),str(self.hi)]
    def decimal(self,places=45):return [dec(self.lo,places),dec(self.hi,places)]
    def width(self):return self.hi-self.lo

def dec(q,places=45):
    with localcontext() as c:
        c.prec=places
        return str(Decimal(q.numerator)/Decimal(q.denominator))

def arb_ball(s):
    m=re.fullmatch(r"\[([+-]?[0-9]+(?:\.[0-9]+)?e[+-]?[0-9]+) \+/- ([0-9]+(?:\.[0-9]+)?e[+-]?[0-9]+)\]",s)
    assert m,"METHOD STOP: immutable native source Arb carrier format changed"
    x,rad=map(F,m.groups())
    assert rad>=0
    return Iv(x-rad,x+rad)

def positive_log_series(q,N=140):
    """2 atanh(q), 0<q<1, with exact positive rational remainder."""
    assert F(0)<q<F(1)
    lo=2*sum((q**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
    tail=2*q**(2*N+1)/F((2*N+1)) / (1-q*q)
    assert tail>0
    return Iv(lo,lo+tail)

def log550():
    # EXACT original NF483 factorization:
    # (11/10)*(5/4)^3*2^8=550.
    assert F(11,10)*F(5,4)**3*F(2)**8==550
    return positive_log_series(F(1,21))+3*positive_log_series(F(1,9))+8*positive_log_series(F(1,3))

def analytic_log_moment(j,k,h):
    """Exact improper integral int_0^delta d^j log(B/d)^k dd."""
    assert j>=0 and k>=0
    out=Iv(0)
    for l in range(k+1):
        out+=F(comb(k,l)*factorial(l), (j+1)**l)*h**(k-l)
    return F(DELTA**(j+1),j+1)*out

def analytic_log_moment_rational(j,k,h):
    return (DELTA**(j+1)/F(j+1))*sum(
        (F(comb(k,l)*factorial(l),(j+1)**l)*h**(k-l)
         for l in range(k+1)),F(0))

def compute_baseline(v,Z,alpha,C,h):
    t00=analytic_log_moment(0,0,h)
    t01=analytic_log_moment(0,1,h)
    t11=analytic_log_moment(1,1,h)
    t12=analytic_log_moment(1,2,h)
    t22=analytic_log_moment(2,2,h)
    return (4*v*Z*(C*t00+F(1,2)*t01)
        +2*Z**2*t00
        +4*v*alpha*(C*t11+F(1,2)*t12)
        +4*Z*alpha*t11
        +2*alpha**2*t22)

def direct_signed_polynomial(v,Z,alpha,C,h,r):
    """Independent polynomial×log coefficient multiplication over Q."""
    pp={(0,0):v*C,(0,1):v/F(2)}
    zz={(0,0):Z,(1,1):alpha}
    for k,a in enumerate(r,1):
        zz[(k,0)]=zz.get((k,0),F(0))+a
    total=F(0)
    for (i,j),pi in pp.items():
        for (k,l),zk in zz.items():
            total+=4*pi*zk*analytic_log_moment_rational(i+k,j+l,h)
    for (i,j),zi in zz.items():
        for (k,l),zk in zz.items():
            total+=2*zi*zk*analytic_log_moment_rational(i+k,j+l,h)
    return total

def four_moment_formula(v,Z,alpha,C,h,r):
    v,Z,alpha,C,h=map(Iv,(v,Z,alpha,C,h))
    A=compute_baseline(v,Z,alpha,C,h)
    M0=M1=M2=M3=F(0)
    for k,a in enumerate(r,1):
        M0+=a*analytic_log_moment_rational(k,0,F(h.lo))
        M1+=a*analytic_log_moment_rational(k,1,F(h.lo))
        M2+=a*analytic_log_moment_rational(k+1,1,F(h.lo))
        for l,b in enumerate(r,1):
            M3+=a*b*DELTA**(k+l+1)/F(k+l+1)
    assert A.lo==A.hi
    return A.lo+(4*v.lo*C.lo+4*Z.lo)*M0+2*v.lo*M1+4*alpha.lo*M2+2*M3

def exact_algebra_controls():
    tests=[
      (F(-1,11),F(-3,17),F(7,23),F(5,4),F(1),[]),
      (F(-1,11),F(-3,17),F(7,23),F(5,4),F(7),[F(0)]),
      (F(1,19),F(-2,31),F(-3,29),F(8,7),F(5),[F(1,3)]),
      (F(-1,29),F(0),F(3,17),F(0),F(13,2),[F(1),F(-1)]),
      (F(0),F(13,11),F(0),F(12,7),F(3),[F(-2),F(5),F(-11)]),
      (F(13,17),F(-11,7),F(19,43),F(37,23),F(9),[F(0),F(-1,7),F(0),F(8,19)]),
      (F(-101,103),F(107,109),F(-113,127),F(131,137),F(2),[F(1,10**30),F(-1,10**25)]),
      (F(-1,10**19),F(-2,10**17),F(3,10**15),F(17,5),F(6),[F(0)]*3+[F(19,31)]),
      (F(0),F(0),F(0),F(0),F(1),[F(0)]*5),
      (F(-2,7),F(3,11),F(5,13),F(7,17),F(13,3),[F((-1)**k*k,3*k+1) for k in range(1,8)]),
      (F(11,41),F(-13,43),F(17,47),F(19,53),F(3),[F(0),F(0),F(5,1009)]),
      (F(-5,97),F(7,101),F(-11,103),F(13,107),F(4),[F((-1)**k,10**k) for k in range(1,7)])
    ]
    for v,Z,alpha,C,h,r in tests:
        a=direct_signed_polynomial(v,Z,alpha,C,h,r)
        b=four_moment_formula(v,Z,alpha,C,h,r)
        assert a==b,(a,b)
    return len(tests)

def main():
    jet,jetsha=load("notes/data/provisional/NF411_original_source_boundary_jet.json")
    zreceipt,zsha=load("notes/data/provisional/NF450_original_B_complete_Laplace_native_sign_custody_index.json")
    nf479,p479=load("notes/data/provisional/NF479_original_full_J8_forced_positive_NF404_transfer_custody.json")
    nf482,p482=load("notes/data/provisional/NF482_original_first_J8_irrational_n9_source_signed_custody.json")
    assert jet["pass"]=="NF411" and zreceipt["pass"]=="NF450" and nf479["pass"]=="NF479" and nf482["pass"]=="NF482"
    assert jet["nf407_source_sha256"]==zreceipt["source_SHA256"]==nf479["original_nf407_source_sha256"]==nf482["original_nf407_source_sha256"]==SRC
    assert nf479["original_nf406_seams_sha256"]==nf482["original_nf406_seams_sha256"]==SEAM
    assert jet["source_derivative_strict_negative"] and zreceipt["complete_z_B_strictly_negative"]
    assert zreceipt["original_source_radius_paid"]
    # The original NF411 4096-bit source numeric balls are midpoint balls.
    # Add an explicit safe 10^-100 overcharge for original NF407 dyadic
    # input uncertainties (reported S0<10^-700 and source-native linear
    # amplification <10^20), not merely native Arb precision.
    input_fee=F(1,10**100)
    assert F(jet["native_source_derivative_uncertainty_exact_upper"])<input_fee
    v=arb_ball(jet["original_original_source_value_at_B_arb"])+Iv(-input_fee,input_fee)
    alpha=(-arb_ball(jet["original_original_source_derivative_at_B_arb"]))/2+Iv(-input_fee,input_fee)
    z0,z1=map(F,zreceipt["complete_z_B_outward_24_decimal"])
    Z=Iv(z0,z1)
    assert v.hi<0 and Z.hi<0 and alpha.lo>0
    assert F(0)<alpha.lo<=alpha.hi<F(1,10**6)
    assert F(-1,10**9)<Z.lo<Z.hi<0
    assert v.lo>F(-1,10**8)
    assert len(jet["all_seven_original_prime_seam_derivative_identities"])==7
    cw={}
    for row in jet["all_seven_original_prime_seam_derivative_identities"]:
        n=row["prime_power"]
        assert n in WEIGHTS and n not in cw
        cw[n]=Iv(*map(F,row["c_n_positive_outward"]))
        assert F(0)<cw[n].lo<=cw[n].hi<1
    assert tuple(sorted(cw))==WEIGHTS
    C=sum((cw[n] for n in WEIGHTS),Iv(0))
    h=log550()
    assert F(6)<h.lo<=h.hi<F(7)
    assert h.width()<F(1,10**90)
    A=compute_baseline(v,Z,alpha,C,h)
    assert A.lo>0 and A.hi>A.lo
    # Unnormalized original D8 = D_A + A + remainder four moments.
    # Use source-confirmed strict conservative NF479 threshold rounding,
    # not an unjustified equality to printed approximate numbers.
    D8_lower=F("1.628791413591084997382e-22")
    nf404_sufficient_cap=F("1.629122471432905958157e-22")
    nf404_definite_failure_lower=F("1.656776807914060395598e-22")
    assert D8_lower<F(nf479["original_full_J8_signed_D8_strict_lower_approx"])
    assert nf404_sufficient_cap<F(nf479["original_J8_signed_sufficient_upper_for_NF404_approx"])
    assert nf404_definite_failure_lower>F(nf479["original_J8_signed_failure_lower_for_NF404_approx"])
    DAlo,DAhi=map(F,nf482["original_source_native_signed_D_I_outward_coarse"])
    assert F(0)<DAlo<DAhi
    # This four-moment residual is SOURCE-INFERRED bounded below but NOT
    # directly computed; its needed small upper is the NF404 suff gate.
    remainder_forced_lower=D8_lower-DAhi-A.hi
    sufficient_remainder_upper=nf404_sufficient_cap-DAhi-A.hi
    definite_failure_remainder_lower=nf404_definite_failure_lower-DAlo-A.lo
    assert remainder_forced_lower<sufficient_remainder_upper<definite_failure_remainder_lower
    assert sufficient_remainder_upper<0
    assert exact_algebra_controls()==12
    out={
      "pass":"NF488",
      "standing":"ORIGINAL source-exact explicit endpoint+cusp baseline and exact four-moment physical remainder gate ONLY; actual four source R moments and full J8 D8 UPPER OPEN",
      "original_nf407_source_sha256":SRC,
      "original_nf406_seam_sha256":SEAM,
      "original_nf411_source_jet_receipt_sha256":jetsha,
      "original_nf450_true_endpoint_receipt_sha256":zsha,
      "original_nf479_global_bessel_receipt_sha256":p479,
      "original_nf482_irrational_n9_first_panel_receipt_sha256":p482,
      "original_source_246_generators_273_groups_and_m0_pole_unchanged":True,
      "original_seven_prime_power_weights":list(WEIGHTS),
      "original_source_input_dyadic_explicit_extra_overcharge":str(input_fee),
      "v_U_B_interval":v.raw(),
      "true_z_B_interval":Z.raw(),
      "alpha_minus_U_prime_B_over_2_interval":alpha.raw(),
      "genuine_original_C8_seven_prime_weight_interval":C.raw(),
      "log_B_over_terminal_delta_equals_log550_interval":h.raw(),
      "original_true_terminal_d_interval":["0","1/500"],
      "baseline_exact_formula":"A=4vZ[C8 I00+I01/2]+2 Z^2 I00+4v alpha[C8 I11+I12/2]+4Z alpha I11+2alpha^2 I22; Ijk=int_0^delta d^j log(B/d)^k dd",
      "original_true_full_J8_terminal_explicit_Z_plus_cusp_signed_A_outward_exact":A.raw(),
      "original_true_full_J8_terminal_explicit_Z_plus_cusp_signed_A_decimal":A.decimal(48),
      "explicit_baseline_interval_width_decimal":dec(A.width()),
      "exact_original_remaining_four_moment_identity":"D_T=A+(4vC8+4Z)M0+2v M1+4alpha M2+2M3; M0=int R, M1=int L R, M2=int dL R, M3=int R^2; z(B-d)=Z+alpha dL+R",
      "source_inferred_four_moment_residual_strict_lower":str(remainder_forced_lower),
      "source_inferred_four_moment_residual_strict_lower_decimal":dec(remainder_forced_lower,48),
      "NF404_conservative_sufficient_four_moment_residual_upper":str(sufficient_remainder_upper),
      "NF404_conservative_sufficient_four_moment_residual_upper_decimal":dec(sufficient_remainder_upper,48),
      "NF404_definite_failure_if_four_moment_residual_above":str(definite_failure_remainder_lower),
      "NF404_definite_failure_if_four_moment_residual_above_decimal":dec(definite_failure_remainder_lower,48),
      "genuine_original_first_n9_panel_coarse_bounds":[str(DAlo),str(DAhi)],
      "independent_exact_rational_four_moment_signed_algebra_controls":12,
      "original_four_R_moments_numerically_source_integrated":False,
      "original_complete_terminal_D8_signed_UPPER":"OPEN",
      "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
      "next_bold":"NF489 compute actual original NF446 joint compact-source R(d) weighted first three moments and square on the full J8 terminal, with certified physical integration and source-coupled cancellation; compare R to newly narrowed exact NF404 gate"
    }
    p=Path("nf488-original-J8-terminal-four-moment-source-exact-gate.json")
    p.write_text(json.dumps(out,indent=2)+"\n")
    print("NF488 accepted original source explicit terminal baseline + 4-moment gate algebra PASS")
    print("Original source-explicit Z+alpha*dL baseline A",A.decimal())
    print("Source-forced four-moment residual lower",dec(remainder_forced_lower))
    print("NF404 sufficient four-moment residual upper",dec(sufficient_remainder_upper))
    print("NF404 definite-failure four-moment residual lower",dec(definite_failure_remainder_lower))
    print("Four genuine original source R moments, complete D8 upper, NF404, W-ODD-NEG, RH OPEN")
if __name__=="__main__":main()
