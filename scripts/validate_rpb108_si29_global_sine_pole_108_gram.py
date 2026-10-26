#!/usr/bin/env python3
"""Exact rational global 108-source physical Gram certificate.

The ORIGINAL degree-zero odd sine generator in each SI10 cluster and
the ORIGINAL supported sinh(x/2) pole form a quantitative 108D Riesz
family. This is NOT the full 470D Gram or an Astar/Weil sign theorem.

External analytic input: Montgomery–Vaughan 1974 Hilbert's inequality,
Corollary 2, for separated real frequencies:
  integral_I |sum b_j exp(2*pi*i*nu_j*x)|^2 dx
     >= (length(I)-1/delta)*sum |b_j|^2.
Everything ELSE in the accepting scalar is exact Fraction arithmetic.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
from validate_rpb108_si06_negative_band import B, PI
from validate_rpb108_si10_complement_positivity import protected_inner_cover
from validate_rpb108_si08_multiband_rank import taylor_order

ROOT=Path(__file__).resolve().parents[1]
K=10**30
D=10**22

def floor(x,d):
    y=x*d
    return F(y.numerator//y.denominator,d)

def ceil(x,d):
    return -floor(-x,d)

def outward(a):
    return floor(a[0],D),ceil(a[1],D)

def add(a,b): return a[0]+b[0],a[1]+b[1]
def neg(a): return -a[1],-a[0]
def mul(a,b):
    z=[x*y for x in a for y in b]
    return min(z),max(z)
def inv_pos(a):
    assert a[0]>0
    return 1/a[1],1/a[0]

def hyper(x,odd,terms=25):
    assert 0<=x<=F(11,10)
    lo=sum((x**(2*k+int(odd))/factorial(2*k+int(odd))
            for k in range(terms)),F(0))
    p=2*terms+int(odd)
    first=x**p/factorial(p)
    ratio=x*x/F((p+1)*(p+2))
    return lo,lo+first/(1-ratio)

def trig(r,pi0):
    """Enclose sin/cos(2*pi*r) for |r|<=1/2 with exact rational series."""
    assert -F(1,2)<=r<=F(1,2)
    t=2*pi0*r
    sn=sum(((-1)**k*t**(2*k+1)/factorial(2*k+1)
            for k in range(25)),F(0))
    cs=sum(((-1)**k*t**(2*k)/factorial(2*k)
            for k in range(26)),F(0))
    phase_err=F(1,K)
    se=F(22,7)**51/factorial(51)+phase_err
    ce=F(22,7)**52/factorial(52)+phase_err
    assert se<F(1,10**28) and ce<F(1,10**28)
    return (sn-se,sn+se),(cs-ce,cs+ce)

def verify():
    assert B==F(11,10) and 3<PI[0]<PI[1]<4
    pi0=floor(PI[0],K)
    assert pi0<=PI[0]<PI[1]<pi0+F(1,K)
    clusters,_,_,_,_=protected_inner_cover()
    assert len(clusters)==107
    centers=[(l+r)/2 for l,r,_ in clusters]
    assert centers[0]==F(37,64)
    assert 1+sum(taylor_order(r-l,9)[0] for l,r,_ in clusters)==470
    reflected=sorted(centers+[-c for c in centers])
    delta=min(y-x for x,y in zip(reflected,reflected[1:]))
    assert delta==F(67,128)
    lam=(2*B-1/delta)/2
    assert lam==F(97,670)>0
    # Exactly original support norm: ||sinh(x/2)||^2 = sinh(B)-B.
    Slo=floor(hyper(B,True)[0]-B,D)
    Shi=ceil(hyper(B,True)[1]-B,D)
    sh=hyper(B/2,True)
    ch=hyper(B/2,False)
    q2=F(0)
    overlaps=[]
    for c in centers:
        t=c*B
        k=(t+F(1,2)).numerator//(t+F(1,2)).denominator
        sine,cosine=trig(t-k,pi0)
        omega=(2*PI[0]*c,2*PI[1]*c)
        # Direct analytic integration of supported sine x sinh:
        # q=2*(.5*cosh(B/2)*sin(omega*B)
        #   -omega*sinh(B/2)*cos(omega*B))/(omega^2+1/4).
        num=add(mul(ch,sine),neg(mul((2,2),mul(omega,mul(sh,cosine)))))
        den=(omega[0]**2+F(1,4),omega[1]**2+F(1,4))
        q=outward(mul(num,inv_pos(den)))
        overlaps.append(q)
        q2+=max(q[0]*q[0],q[1]*q[1])
    assert len(overlaps)==107 and overlaps[0][0]>F(14,100)
    assert q2<F(33,1000)
    # The 107D sine Gram H>=lam I by Montgomery–Vaughan.
    # S-q^T H^{-1}q >= Slo-||q||^2/lam, no 108D inverse.
    residual=Slo-q2/lam
    det=lam*Slo-q2
    lower=det/(lam+Shi)
    assert residual>F(1,100)
    assert det>F(1,1000)
    assert lower>F(1,200)
    # For all (x,t), quadratic >= lam||x||^2-2||q||||x||t+S t^2.
    # The least eigenvalue of this 2x2 lower bound is >= det/trace.
    result={
      "status":"EXACT_RATIONAL_GLOBAL_108_ORIGINAL_SINES_PLUS_POLE_PHYSICAL_GRAM",
      "original_SI10_positive_clusters":len(clusters),
      "original_full_J_source_dim":470,
      "original_reflected_frequency_gap":str(delta),
      "Montgomery_Vaughan_global_107_sine_lower":str(lam),
      "genuine_sinh_pole_norm_lower":str(Slo),
      "genuine_sinh_pole_norm_upper":str(Shi),
      "sum_107_exact_overlap_square_upper":str(q2),
      "genuine_pole_residual_after_all_107_sines_lower":str(residual),
      "complete_global_108_physical_Gram_lower":str(lower),
      "original_full_470_Gram":"OPEN",
      "SI29_full_14_source_Schur":"OPEN",
      "Astar_full_action_signed_odd_even_CC27_RH":"OPEN"}
    dest=ROOT/"artifacts/si29_global_108_sine_pole_exact_gram.json"
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(result,indent=2)+"\n")
    print("SI29 exact original sine-plus-pole 108D Gram:",
          "q2 upper",float(q2),"pole residual lower",float(residual),
          "full Gram lower",float(lower),flush=True)
    return result

if __name__=="__main__":
    verify()
