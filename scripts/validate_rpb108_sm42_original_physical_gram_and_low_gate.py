#!/usr/bin/env python3
"""SM42 exact ORIGINAL physical 25-odd-source Gram/pole and low-band gate.

CERTIFIED SCOPED:
  * All 25 genuine SI10 zero-extended odd source Gram inner products
    analytically via sin-sin, sin-xcos, xcos-xcos, sinh pole formulas.
  * Original rational SI06 pi interval; certified rational Taylor
    sine/cosine phase enclosures after EXACT rational period reduction;
    positive Taylor sinh/cosh rational enclosures.
  * Complete 25x25 interval Gram and pole cross; exact rational
    preconditioned Gershgorin proves whole original physical Gram SPD.
  * Rigorous, deliberately COARSE entire original 25x25 low-frequency
    Ao Loewner enclosure using kappa<=a_o<=17+ln Lambda, Parseval,
    and exact SI41 high-frequency L2 source tail. Non-smooth crossings
    m=kappa do not invalidate these true operator order bounds.
  * Crossing-safe softplus smoothing: 0<=a_eps-a_o<=eps/2 on every
    real frequency, so 0<=A_eps-Ao<=(eps/2)H for EVERY 25-vector.

NOT certified: numerical Gauss-integrated original weighted low-band
stiffness; its useful two-sided interval (beyond coarse Parseval
band enclosure); true original Astar inverse/strong residual;
all 470 odd sources, whole Wodd O1/O2, even, signed Weil, RH.

No floating trig, digamma, or quadrature values enter exact source
interval acceptance. Float numpy is used ONLY to choose a rational
preconditioner; final inequalities are exact integers/Fractions.
"""
import json
from fractions import Fraction as F
from math import factorial

import numpy as np

from validate_rpb108_si06_negative_band import PI, B, LN
from validate_rpb108_si10_complement_positivity import (
    protected_inner_cover,KAPPA
)
from sm36_original_odd_numerical_pilot import ROOT,geometry,select_sources
from validate_rpb108_sm41_original_positive_log_tail import (
    odd_pilot_tail_enclosure, mathematical_global_original_positive_multiplier_majorant
)

class I:
    __slots__=("l","h")
    def __init__(self,l,h=None):
        self.l=F(l);self.h=F(l if h is None else h)
        assert self.l<=self.h
    @staticmethod
    def get(a): return a if isinstance(a,I) else I(a)
    def __add__(self,b):
        b=I.get(b);return I(self.l+b.l,self.h+b.h)
    __radd__=__add__
    def __neg__(self):return I(-self.h,-self.l)
    def __sub__(self,b):return self+(-I.get(b))
    def __rsub__(self,b):return I.get(b)+(-self)
    def __mul__(self,b):
        b=I.get(b)
        a=[self.l*b.l,self.l*b.h,self.h*b.l,self.h*b.h]
        return I(min(a),max(a))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=I.get(b)
        assert b.l*b.h>0,"interval denominator crosses zero"
        return self*I(1/b.h,1/b.l)
    def __rtruediv__(self,b):return I.get(b)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I(1)
        if n==1:return self
        if n==2:
            vals=[self.l*self.l,self.h*self.h]
            return I(0 if self.l<=0<=self.h else min(vals),max(vals))
        q=I(1)
        for _ in range(n):q=q*self
        return q
    def mid(self):return (self.l+self.h)/2
    def width(self):return self.h-self.l

SCALE=10**18
TRIG_ERR=F(1,10**12)

def rational_round(t):
    # nearest integer with exact rational arithmetic
    v=t+F(1,2)
    return v.numerator//v.denominator

def sin_cos_period(q):
    """Certified sine/cos(2pi*q) interval, q exact rational.

    EXACT q reduction by nearest integer makes |q-k|<=1/2.
    Real pi lies in original SI06 rational interval.
    Taylor through sin^35 / cos^34, at |t|<4:
      next sin term <4^37/37! <1e-18
      next cos term <4^36/36! <1e-18.
    Quantize midpoint phase to 1e-18: phase error <=
    1e-18 + (PI_hi-PI_lo), which is <1e-13 under SI06.
    Both sine/cosine are 1-Lipschitz. Outward 1e-12 pays ALL.
    """
    q=F(q)
    k=rational_round(q)
    u=q-k
    assert -F(1,2)<=u<=F(1,2)
    theta_mid=2*(PI[0]+PI[1])/2*u
    t=F((theta_mid*SCALE).__floor__(),SCALE)
    phase_err=abs(theta_mid-t)+(PI[1]-PI[0])
    assert phase_err < F(1,10**13)
    assert abs(t)<4
    assert F(4)**36/factorial(36)<F(1,10**18)
    assert F(4)**37/factorial(37)<F(1,10**18)
    sn=sum(((-1)**j*t**(2*j+1)/factorial(2*j+1) for j in range(18)),F(0))
    cs=sum(((-1)**j*t**(2*j)/factorial(2*j) for j in range(18)),F(0))
    assert phase_err+F(1,10**18)<TRIG_ERR
    return I(sn-TRIG_ERR,sn+TRIG_ERR),I(cs-TRIG_ERR,cs+TRIG_ERR)


def hyperbolic_interval(x,kind):
    """Entire exact positive power series with rigorous geometric tail."""
    x=F(x);assert 0<=x<=B
    assert kind in ("sinh","cosh")
    s=F(0)
    start=1 if kind=="sinh" else 0
    for k in range(17):
        v=2*k+start
        s+=x**v/factorial(v)
    nextdegree=2*17+start
    first=x**nextdegree/factorial(nextdegree)
    ratio=x*x/F((nextdegree+1)*(nextdegree+2))
    assert ratio<F(1,100)
    return I(s,s+first/(1-ratio))


def omega(q):return 2*I(PI[0],PI[1])*F(q)

def F0(q):
    if q==0:return I(2*B)
    sn,_=sin_cos_period(B*q)
    return 2*sn/omega(q)

def F1(q):
    if q==0:return I(0)
    w=omega(q);sn,cs=sin_cos_period(B*q)
    return 2*(sn-B*w*cs)/(w*w)

def F2(q):
    if q==0:return I(2*B**3/3)
    w=omega(q);sn,cs=sin_cos_period(B*q)
    return 2*(B*B*sn/w+2*B*cs/(w*w)-2*sn/(w*w*w))


def pole_sin(c,sh,ch):
    w=omega(c);sn,cs=sin_cos_period(B*c)
    a=F(1,2)
    numerator=2*(a*ch*sn-w*sh*cs)
    return numerator/(I(a*a)+w*w)

def pole_xcos(c,sh,ch):
    w=omega(c);sn,cs=sin_cos_period(B*c)
    a=F(1,2);D=I(a*a)+w*w
    N=2*(a*ch*sn-w*sh*cs)
    Np=2*(a*ch*B*cs-sh*cs+w*sh*B*sn)
    return (Np*D-2*w*N)/(D*D)


def original_full_25_physical_interval_gram():
    infos,*_=geometry()
    src=select_sources(infos)
    clusters,_,_,_,_=protected_inner_cover()
    centers=[(a+b)/2 for a,b,_ in clusters]
    assert len(src)==25 and src[-1][0]=="pole"
    sh=hyperbolic_interval(B/2,"sinh")
    ch=hyperbolic_interval(B/2,"cosh")
    pole_norm=hyperbolic_interval(B,"sinh")-B
    assert pole_norm.l>0
    n=len(src)
    g=[[I(0) for _ in range(n)] for _ in range(n)]
    for i,(ti,ji,ki) in enumerate(src):
        ci=centers[ji] if ji>=0 else None
        for j in range(i,n):
            tj,jj,kj=src[j]
            cj=centers[jj] if jj>=0 else None
            if ti=="pole" and tj=="pole": val=pole_norm
            elif ti=="pole":
                val=pole_sin(cj,sh,ch) if kj==0 else pole_xcos(cj,sh,ch)
            elif tj=="pole":
                val=pole_sin(ci,sh,ch) if ki==0 else pole_xcos(ci,sh,ch)
            elif ki==0 and kj==0:
                val=(F0(ci-cj)-F0(ci+cj))/2
            elif ki==1 and kj==1:
                val=(F2(ci-cj)+F2(ci+cj))/2
            else:
                # Mixed sin(ci*x) and x*cos(cj*x).
                csine,ccos=(ci,cj) if ki==0 else (cj,ci)
                val=(F1(csine+ccos)+F1(csine-ccos))/2
            g[i][j]=g[j][i]=val
    # Cross-check exact analytic odd pole norm and Cauchy for all
    # original source columns. Not a sample/trapezoid calculation.
    for i in range(n):
        assert g[i][i].l>0
        assert g[i][-1].l*g[i][-1].l <= \
               g[i][i].h*pole_norm.h or g[i][-1].l<=0
        assert g[i][-1].h*g[i][-1].h <= \
               g[i][i].h*pole_norm.h or g[i][-1].h>=0
    return g,src,pole_norm


def exact_verified_preconditioned_gram(g):
    """Numerical preconditioner is NEVER trusted as a proof.

    Approximate exact interval centers H0 with fixed integer
    denominator, rational Q approximating inverse Cholesky, then
    exact rational Gershgorin + rigorous entire interval error.
    """
    n=len(g);hs=10**11;qs=10**6
    hn=[[rational_round(a.mid()*hs) for a in row] for row in g]
    em=max((max(abs(a.l-F(hn[i][j],hs)),
                abs(a.h-F(hn[i][j],hs)))
            for i,row in enumerate(g) for j,a in enumerate(row)))
    hnum=np.array([[float(F(x,hs)) for x in row] for row in hn])
    assert np.linalg.norm(hnum-hnum.T)<1e-12
    chol=np.linalg.cholesky(hnum)
    Q=np.linalg.inv(chol.T)
    qn=[[int(np.rint(Q[i,j]*qs)) for j in range(n)] for i in range(n)]
    # Exact integers, all 25x25 transformations and all source cross.
    hq=[[sum(hn[i][k]*qn[k][j] for k in range(n))
         for j in range(n)] for i in range(n)]
    mat=[[sum(qn[k][i]*hq[k][j] for k in range(n))
          for j in range(n)] for i in range(n)]
    assert all(mat[i][j]==mat[j][i] for i in range(n) for j in range(n))
    # Bound Q^T E Q entrywise by max entry E times absolute column
    # sums; Gershgorin row error = em*c_i*sum(c_j).
    c=[sum(abs(qn[k][j]) for k in range(n)) for j in range(n)]
    total=sum(c)
    margins=[F(mat[i][i]-sum(abs(mat[i][j]) for j in range(n) if i!=j),hs)
             -em*c[i]*total for i in range(n)]
    assert min(margins)>0,("verified Gram SPD FAILED",float(min(margins)))
    # Matrix congruence by Q is valid, invertibility: Q^THQ
    # positive definite implies Q must be full rank.
    # Export short outward decimal RATIONAL enclosures, not gigantic
    # thousands-of-digit exact intermediate fractions. Original
    # Fraction proof runs to completion BEFORE rounding summaries.
    S=10**12
    def up(q):return F(-(-q.numerator*S//q.denominator),S)
    def down(q):return F(q.numerator*S//q.denominator,S)
    rawmargin=min(margins)/qs**2
    pole_lo=down(g[-1][-1].l)
    pole_hi=up(g[-1][-1].h)
    assert up(em)>=em and down(rawmargin)<=rawmargin
    assert down(rawmargin)>0 and pole_hi>=g[-1][-1].h
    return {
       "certified_entire_original_25x25_physical_gram_SPD":True,
       "outward_max_entry_interval_error_upper":str(up(em)),
       "outward_preconditioned_gershgorin_lower":
           str(down(rawmargin)),
       "min_preconditioned_gershgorin_margin_float":
           float(rawmargin),
       "preconditioner_quantization":str(F(1,qs)),
       "original_source_dimension":n,
       "original_pole_norm_exact_formula":"sinh(11/10)-11/10",
       "original_pole_norm_outward_interval":
           [str(pole_lo),str(pole_hi)],
       "certifying_method":"exact rational whole 25x25 interval Gram and rational-preconditioned strict Gershgorin; outward decimal summary rounded only after proof"
    }


def original_crossing_safe_low_band_gate():
    """Exact operator comparison valid ACROSS every m=kappa crossing.

    Given a_o=max(kappa,m), a_eps(xi)=kappa+
        (x+sqrt(x*x+eps*eps))/2, x=m-kappa:
      0<=a_eps-a_o<=eps/2 everywhere by sqrt(x²+eps²)<=
      |x|+eps. All original source frequency crosses INCLUDED.
    For cutoff L>=1, arch monotone + SM41 bound at L
      kappa<=a_o(xi)<=17+ln L for 0<=xi<=L.
    Thus kappa P_L<=A_low<=(17+lnL)P_L. The physical Gram
    H=P_{all} source Gram, and selected source raw L2 tail
    <=2E/L I. So the *rigorous* coarse Loewner source sandwich:
      kappa(H-2E/L I)<=A_low<=(17+lnL)H.
    This is a true whole original low-band but intentionally
    too coarse to certify spectral sign or recover Gauss matrix.
    """
    epsilon=F(1,2**20);L=4096;E=F(202,25)
    ln_upper=12*F(347,500)
    assert LN[2][1]<F(347,500)
    Htail=2*E/L
    err_soft=epsilon/2
    assert err_soft<F(1,10**6)
    assert Htail<F(1,200)
    return {
       "crossing_method":"exact global softplus operator sandwich; no need to isolate m=kappa roots",
       "softplus_epsilon_exact":str(epsilon),
       "a_epsilon_minus_true_Ao_whole_operator_upper_multiple_H":
           str(err_soft),
       "entire_original_low_band_cutoff":L,
       "original_25_source_raw_L2_high_tail_upper_I":str(Htail),
       "certified_original_low_band_lower":"kappa*(H - (2E/Lambda)*I_25) <= A_low",
       "certified_original_low_band_upper":"A_low <= (17+ln Lambda)*H",
       "exact_upward_log_cutoff":str(ln_upper),
       "full_low_frequency_quad_error_certified":False,
       "true_original_Astar_resolvent_certified":False
    }


def main():
    import argparse
    a=argparse.ArgumentParser()
    a.add_argument("--output",default="artifacts/sm42_exact_original_25_source_gram_and_low_gate.json")
    args=a.parse_args()
    m=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in m["obligations"] if x["id"]=="W-ODD-NEG")
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]=="open" and odd["status"]=="open"
    assert m["governance"]["no_automatic_promotion"] is True
    assert all(x in odd["evidence"] and x in m["evidence"] for x in ("SM40","SM41","SM42"))
    assert "sm42_true_original_physical_gram_crossing_safe_low_gate" in m["governance"]
    mathematical_global_original_positive_multiplier_majorant()
    g,src,pole=original_full_25_physical_interval_gram()
    gram=exact_verified_preconditioned_gram(g)
    crossing=original_crossing_safe_low_band_gate()
    print("SM42 ORIGINAL EXACT ENTIRE 25x25 PHYSICAL GRAM",
          json.dumps(gram,sort_keys=True),flush=True)
    print("SM42 ORIGINAL EXACT m=kappa CROSSING-SAFE COARSE"
          " low-band operator Loewner sandwich",
          json.dumps(crossing,sort_keys=True),flush=True)
    data={
       "status":"CERTIFIED_EXACT_ORIGINAL_25_PHYSICAL_GRAM_AND_COARSE_CROSSING_SAFE_LOW_OPERATOR",
       "canonical_W_ODD_NEG":"OPEN",
       "real_original_source_count":25,
       "actual_original_25_source_gram":gram,
       "actual_original_odd_pole_norm":gram["original_pole_norm_outward_interval"],
       "original_positive_low_band_coarse_operator_gate":crossing,
       "missing_original_complete_odd_acceptance":[
         "useful tight low-band positive digamma-seven-prime 25x25 interval Gauss remainder",
         "complete original 470 source higher-degree physical Gram and sharp positive high tail",
         "genuine original Astar pole-conditioned all-470 inverse and strong residual",
         "entire original 470 coupled negative generalized <=51/56 or true corrected Schur",
         "independent complete original signed Fourier and closed-form-domain audit",
         "whole original Wodd O1/O2, even E1-E4, signed Weil, native CC27 and RH"
       ]
    }
    out=ROOT/args.output
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(data,indent=2)+"\n")
    print("SM42 SCOPED PASS: certified original actual 25x25"
          " zero-extended odd physical source Gram and true odd"
          " pole norm with ALL source cross via exact rational"
          " interval trig/hyperbolic, rational-preconditioned"
          " Gershgorin, plus exact whole m=kappa crossing-safe"
          " low-band coarse Loewner and softplus. Tight LOW"
          " quadrature, original full 470 Astar resolvent,"
          " whole O1/O2, even, Weil, CC27 and RH OPEN.",flush=True)


if __name__=="__main__":
    main()
