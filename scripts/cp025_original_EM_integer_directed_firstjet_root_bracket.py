#!/usr/bin/env python3
"""CP025 original M=6,N=256 finite Euler–Maclaurin, integer-directed intervals.

NOT LEAN.  Arithmetic uses ONLY Python integers/Fraction; not mpmath,
float, approximate complex number objects, decimal string roundoff,
an unverified numerical library, or numerical Gamma/ζ oracles.

Source:
  original Zeta.EulerMaclaurin.Continuation.zetaApproximant,
  original Zeta.Zeros.HardyZ.abs_riemannSiegelTheta_sub_approximant_two_le,
  original Zeta.Gamma.LogGammaStirling.logGammaStirling_two,
  original Zeta.Gram.Averaging.hasDerivAt_riemannSiegelTheta,
  original Zeta.Gamma.DigammaStirling.norm_digamma_sub_log_le',
  original Zeta.EulerMaclaurin.ErrorBound.norm_zetaRemainder_le.

The user-visible narrow sign and Z'(149.5)>2.4 enclosures require
mathematically justified original M6N256 value bound R<=3e-13 and the
source-derived θ'<=9/5, R'<=12e-13 error budget; these latter original
fully quantified complex bounds are NOT YET Lean-kernel accepted.
Everything numerical is enclosed by integer floors/ceilings,
rational atanh/arctan Taylor majorants, rational Machin pi and real
Taylor sin/cos with explicit Lagrange remainder.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as Q
from math import comb, factorial, isqrt
from pathlib import Path

S=10**55

class I:
    __slots__=("l","h")
    def __init__(self,l,h=None):
        self.l=int(l);self.h=int(h if h is not None else l)
        assert self.l<=self.h
    @staticmethod
    def q(q):
        q=Q(q)
        return I(q.numerator*S//q.denominator,
                 -(-q.numerator*S//q.denominator))
    @staticmethod
    def cv(x):
        return x if isinstance(x,I) else I.q(x)
    def __add__(a,b):
        b=I.cv(b);return I(a.l+b.l,a.h+b.h)
    __radd__=__add__
    def __neg__(a):return I(-a.h,-a.l)
    def __sub__(a,b):return a+(-I.cv(b))
    def __rsub__(a,b):return I.cv(b)-a
    def __mul__(a,b):
        b=I.cv(b)
        p=(a.l*b.l,a.l*b.h,a.h*b.l,a.h*b.h)
        return I(min(p)//S,-(-max(p)//S))
    __rmul__=__mul__
    def inv(a):
        if a.l<=0<=a.h:raise ZeroDivisionError
        return I(S*S//a.h,-(-S*S//a.l))
    def __truediv__(a,b):return a*I.cv(b).inv()
    def __rtruediv__(a,b):return I.cv(b)/a
    def __pow__(a,n):
        assert isinstance(n,int) and n>=0
        v=a;ans=I.q(1)
        while n:
            if n&1:ans=ans*v
            v=v*v;n//=2
        return ans
    def lo(a):return Q(a.l,S)
    def hi(a):return Q(a.h,S)
    def absup(a):return Q(max(abs(a.l),abs(a.h)),S)

class C:
    __slots__=("r","i")
    def __init__(self,r=0,i=0):
        self.r=I.cv(r);self.i=I.cv(i)
    @staticmethod
    def cv(x):return x if isinstance(x,C) else C(x)
    def __add__(a,b):
        b=C.cv(b);return C(a.r+b.r,a.i+b.i)
    __radd__=__add__
    def __neg__(a):return C(-a.r,-a.i)
    def __sub__(a,b):return a+(-C.cv(b))
    def __rsub__(a,b):return C.cv(b)-a
    def __mul__(a,b):
        b=C.cv(b)
        return C(a.r*b.r-a.i*b.i,a.r*b.i+a.i*b.r)
    __rmul__=__mul__
    def inv(a):
        d=a.r*a.r+a.i*a.i
        return C(a.r/d,-a.i/d)
    def __truediv__(a,b):return a*C.cv(b).inv()
    def __rtruediv__(a,b):return C.cv(b)/a
    def normup(a):
        x=a.r.absup();y=a.i.absup()
        v=(x*x+y*y)*S*S
        p=isqrt(v.numerator//v.denominator)
        if Q(p*p)<v:p+=1
        return Q(p,S)

def atan_inv(n,steps=64):
    x=Q(1,n);v=Q(0)
    for k in range(steps):
        v+=(-1)**k*x**(2*k+1)/(2*k+1)
    e=x**(2*steps+1)/(2*steps+1)
    return I(I.q(v-e).l,I.q(v+e).h)

# The Machin pi identity is exact; arctan alternating tails are
# bounded by the magnitude of the first omitted term.
PI=16*atan_inv(5)-4*atan_inv(239)
LOGCACHE={}

def log2(steps=115):
    y=Q(1,3);v=I.q(0)
    for k in range(steps):
        v+=I.q(2*y**(2*k+1)/(2*k+1))
    e=2*y**(2*steps+1)/((2*steps+1)*(1-y*y))
    return I(v.l,v.h+I.q(e).h)

LOG2=log2()

def lnq(x,steps=115):
    x=Q(x)
    if x<=0:raise ValueError("positive log argument required")
    if x==1:return I.q(0)
    if x in LOGCACHE:return LOGCACHE[x]
    k=0;u=x
    while u>=2:u/=2;k+=1
    while u<1:u*=2;k-=1
    y=(u-1)/(u+1);v=I.q(0)
    for j in range(steps):
        v+=I.q(2*y**(2*j+1)/(2*j+1))
    e=2*y**(2*steps+1)/((2*steps+1)*(1-y*y))
    v=I(v.l,v.h+I.q(e).h)+k*LOG2
    LOGCACHE[x]=v
    return v

def lni(v):
    v=I.cv(v)
    if v.l<=0:raise ValueError("positive interval for logarithm required")
    low=lnq(Q(v.l,S));high=lnq(Q(v.h,S))
    return I(low.l,high.h)

def invsqrt(n):
    p=isqrt(S*S//n)
    return I(p,p if p*p*n==S*S else p+1)

# Taylor truncation at 2m for sin, at 2m-1 for cos;
# derivatives of real sin/cos are ≤1 in absolute value.
def sincos(x,m=50):
    x=I.cv(x)
    if max(abs(x.l),abs(x.h))>4*S:
        raise ValueError("trig argument must be reduced to [-4,4]")
    xx=x*x;si=I.q(0);co=I.q(0)
    ts=x;tc=I.q(1)
    for j in range(m):
        si+=ts;co+=tc
        ts=-(ts*xx)/((2*j+2)*(2*j+3))
        tc=-(tc*xx)/((2*j+1)*(2*j+2))
    se=I.q(Q(4**(2*m+1),factorial(2*m+1)))
    ce=I.q(Q(4**(2*m),factorial(2*m)))
    return si+I(-se.h,se.h),co+I(-ce.h,ce.h)

def trig(x):
    x=I.cv(x)
    # Float chooses ONLY an integer phase-reduction multiple; its
    # magnitude is rigorously rechecked before evaluating Taylor.
    k=round(float(x.lo()/(2*PI.lo())))
    return sincos(x-2*k*PI)

def atan_small(x,m=14):
    x=Q(x)
    if not (0<=x<=Q(1,100)):raise ValueError("small arctan domain")
    v=Q(0)
    for j in range(m):
        v+=(-1)**j*x**(2*j+1)/(2*j+1)
    e=x**(2*m+1)/(2*m+1)
    return I(I.q(v-e).l,I.q(v+e).h)

LOGPI=lni(PI)
LOG256=lnq(256)
B=[Q(1,6),-Q(1,30),Q(1,42),-Q(1,30),Q(5,66),-Q(691,2730)]

def original_A_and_Ds(t):
    t=Q(t);s=C(Q(1,2),t)
    a=C();da=C()
    # Genuine original Finset.Ico 1 256, exactly 255 terms.
    for n in range(1,256):
        ln=lnq(n)
        si,co=trig(t*ln)
        term=C(co*invsqrt(n),-si*invsqrt(n))
        a+=term;da+=term*(-ln)
    si,co=trig(t*LOG256)
    base=C(co*Q(1,16),-si*Q(1,16))  # 256^(-s)
    pole=base*256/(s-1)               # 256^(1-s)/(s-1)
    a+=pole+base/2
    da+=pole*(-LOG256)-(base*256)/((s-1)*(s-1))+base*(-LOG256)/2
    p=C(1);dp=C(0)
    # Ascending Pochhammer polynomials (s)_(2k-1) and their
    # COMPLEX derivatives, no finite-difference derivatives.
    for j in range(11):
        dp,p=dp*(s+j)+p,p*(s+j)
        if j%2==0:
            k=(j+2)//2
            q=B[k-1]/factorial(2*k)/256**(2*k-1)
            a+=p*base*q
            da+=(dp-p*LOG256)*base*q
    return a,da

def original_theta_stirling2_and_prime0(t):
    t=Q(t);w=C(Q(1,4),t/2)
    # log|w|=log(t/2)+1/2 log(1+1/(4t^2)).
    lnabs=lnq(t/2)+lni(1+I.q(Q(1,4*t*t)))/2
    inv=w.inv()
    # Exact imaginary part of original logGammaStirling_two at
    # w=1/4+it/2, minus (t/2) log pi.
    th=I.q(t/2)*(lnabs-LOGPI-I.q(1))
    th+=-PI/8+atan_small(Q(1,2*t))/4+inv.i/12-(w*w*w).inv().i/360
    # From original theta'= (Re digamma(w)-log pi)/2 and
    # source ψ=Log w-(2w)^-1+H(w):
    approxPrime=(lnabs-LOGPI-inv.r/2)/2
    return th,approxPrime

def enclosure(t,with_prime=False):
    t=Q(t);a,da=original_A_and_Ds(t)
    th,thp=original_theta_stirling2_and_prime0(t)
    si,co=trig(th);ph=C(co,si)
    val=(ph*a).r
    # ORIGINAL published HardyZ.lean:
    # |theta(t)-Stirling2_0(t)|<=12/t^4.
    phase_err=Q(12,t**4)
    # Genuine original Borwein complex bound; CP020–21 local Lean
    # proof of uniform 3e-13 is SOURCE CANDIDATE, not kernel accepted.
    zerr=a.normup()*phase_err+Q(3,10**13)
    zlo=val.lo()-zerr;zhi=val.hi()+zerr
    out={
      "t":str(t),
      "A_phase_rotated_finite_lo":str(val.lo()),
      "A_phase_rotated_finite_hi":str(val.hi()),
      "published_theta_error":str(phase_err),
      "original_zeta_remainder_value_cap_source_candidate":"3/10^13",
      "original_Z_lower":str(zlo),
      "original_Z_upper":str(zhi),
    }
    if with_prime:
        # Exact analytic phase first jet, evaluated at Stirling
        # theta approximant and first-order digamma approximant.
        vp=-(ph*(a*thp+da)).i
        # From original published digamma-Stirling error:
        # |Re H(w)|/2 <= 1/10000 for |w|>=74.
        pd=Q(1,10000)
        # First phase perturbation, then theta' perturbation,
        # then source-based (not yet Lean-accepted) R' Hardy budget.
        e=phase_err*((thp.absup()+pd)*a.normup()+da.normup())
        e+=pd*a.normup()+Q(87,5*10**13)
        out.update(
          A_finite_first_derivative_lo=str(vp.lo()),
          A_finite_first_derivative_hi=str(vp.hi()),
          first_derivative_total_error=str(e),
          original_Zprime_lower=str(vp.lo()-e),
          original_Zprime_upper=str(vp.hi()+e),
        )
    return out

ZETA_COMMIT="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
PINS={
 "Zeta/EulerMaclaurin/Continuation.lean":"1bb01e946fa7e344497eaf7694fbecff0a714d09",
 "Zeta/EulerMaclaurin/ErrorBound.lean":"01184af0dbfd1369e14725e02e990b016bedfe6f",
 "Zeta/Zeros/HardyZ.lean":"9975442b0c14011c35f4624197d0bf26169c7665",
 "Zeta/Gamma/LogGammaStirling.lean":"50b98a2a3dfef8cb4e6d77de82d33ac52c8ecaca",
 "Zeta/Gamma/DigammaStirling.lean":"9b5a21dfefe6c778411b03fc7e0cf8e8c5bcfac8",
 "Zeta/Gram/Averaging.lean":"6a30171433903a57736de2ab83b120ef660e08bd",
}
SIGNATURES={
 "Zeta/EulerMaclaurin/Continuation.lean":["noncomputable abbrev zetaApproximant"],
 "Zeta/EulerMaclaurin/ErrorBound.lean":["theorem norm_zetaRemainder_le"],
 "Zeta/Zeros/HardyZ.lean":["theorem abs_riemannSiegelTheta_sub_approximant_two_le"],
 "Zeta/Gamma/LogGammaStirling.lean":["theorem logGammaStirling_two"],
 "Zeta/Gamma/DigammaStirling.lean":["theorem norm_digamma_sub_log_le'"],
 "Zeta/Gram/Averaging.lean":["theorem hasDerivAt_riemannSiegelTheta"],
}
def sha_file(f):
    h=hashlib.sha1(b"blob "+str(f.stat().st_size).encode()+b"\0")
    with f.open('rb') as fp:
        for chunk in iter(lambda:fp.read(1<<20),b''):
            h.update(chunk)
    return h.hexdigest()
def original_source_gate(root):
    for name,sha in PINS.items():
        f=root/name
        if sha_file(f)!=sha:
            raise ValueError("genuine original source SHA mismatch "+name)
        body=f.read_text("utf-8")
        for signature in SIGNATURES[name]:
            if signature not in body:
                raise ValueError("frozen source theorem changed "+name+": "+signature)
    print("CP025 SIX ORIGINAL A/PHASE SOURCE GIT SHA+THEOREM GATES: 6/6 PASS NOT LEAN")

def bernoulli(n):
    v=[Q(1)]
    for k in range(1,n+1):
        v.append(Q(1)-sum(Q(comb(k,i),k-i+1)*v[i] for i in range(k)))
    return (-1)**n*v[n]
def arithmetic_controls():
    assert 3<PI.lo()<PI.hi()<4
    assert Q("3.14159265358979323846264338327950288419716939937510")<PI.lo()
    assert Q("3.14159265358979323846264338327950288419716939937511")>PI.hi()
    assert Q("0.6931471805599453094172321214581765680755")<lnq(2).lo()
    assert Q("0.6931471805599453094172321214581765680756")>lnq(2).hi()
    assert [bernoulli(2*k) for k in range(1,7)]==B
    for n in [1,2,3,8,17,55,128,255]:
        v=invsqrt(n)
        assert v.lo()**2*n<=1<=v.hi()**2*n
        assert lnq(n).lo()<=lnq(n).hi()
    for p in [Q(1,3),Q(-2,7),Q(2),Q(-5)]:
        x=I.q(p)
        assert x.lo()<=p<=x.hi()
        assert (x*x).lo()<=p*p<=(x*x).hi()
        assert (I.q(1)/x).lo()<=1/p<=(I.q(1)/x).hi()
        for q in [Q(-2,7),Q(1,5)]:
            assert (x*I.q(q)).lo()<=p*q<=(x*I.q(q)).hi()
    assert Q(12,Q(299,2)**4)<Q(1,10**7)
    assert Q(87,5*10**13)==Q("0.00000000000174")
    print("CP025 INTEGER-DIRECTED PI/LOG/SIN/BERNOULLI/COMPLEX INTERVAL CONTROLS: PASS NOT LEAN")

def certificate():
    a=enclosure(Q(299,2),True)
    l=enclosure(Q("150.05352"))
    r=enclosure(Q("150.05353"))
    assert Q(a["original_Zprime_lower"])>Q("2.4426")>Q(12,5)
    assert Q(a["original_Zprime_upper"])<Q("2.4429")
    assert Q("-0.000000682")<Q(l["original_Z_lower"])
    assert Q(l["original_Z_upper"])<Q("-0.000000681")<0
    assert Q("0.000015519")<Q(r["original_Z_lower"])
    assert Q(r["original_Z_upper"])<Q("0.000015520")
    print("CP025 ORIGINAL M6N256 INTEGER DIRECTED FIRST-JET + NARROW BRACKET: PASS NOT LEAN")
    print("  2.4426 < original Z'(149.5) < 2.4429")
    print("  -0.000000682 < original Z(150.05352) < -0.000000681")
    print("  0.000015519 < original Z(150.05353) < 0.000015520")
    return {
      "status":"CP025_EXTERNAL_INTEGER_DIRECTED_ORIGINAL_M6N256_INTERVAL_PASS_NOT_LEAN",
      "original_frozen_Zeta_git_commit":ZETA_COMMIT,
      "original_six_frozen_source_SHA":PINS,
      "arithmetic":"fixed 10^55 integer floor/ceil, rational Machin pi, positive-log atanh and alternating atan tails, sine/cosine Taylor Lagrange errors; no mpmath or floating oracle needed for enclosures",
      "mathematical_hypotheses":["published exact original zeta=A6,256+R6,256",
        "published original Hardy theta-Stirling order-two error <=12/t^4",
        "published original digamma-Stirling H bound <=1/5000 at |w|>=74",
        "source-derived original Borwein |R|<=3e-13 (NEW LEAN PROOF PENDING)",
        "source-derived thetaPrime<=9/5 and |R'|<=12e-13 (NEW LEAN PROOF PENDING)"],
      "outside_Lean_original_first_derivative_anchor_gt_2_4":True,
      "outside_Lean_original_narrow_HardyZ_sign_change":True,
      "numeric_anchor_interval":["2.4426","2.4429"],
      "numeric_left_endpoint_interval":["-0.000000682","-0.000000681"],
      "numeric_right_endpoint_interval":["0.000015519","0.000015520"],
      "actual_new_Lean_v435_kernel_receipt":False,
      "source_original_zero53_ordinal_attachment_kernel_certified":False,
      "original_whole_interval_HardyZ_curvature_le4":False,
      "original_signed_Weil_spectral_matrix_equivalence":False,
      "global_Weil_positivity_or_RH":False,
      "exact_point_intervals":{"149.5":a,"150.05352":l,"150.05353":r},
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--original-zeta",type=Path)
    p.add_argument("--receipt",type=Path)
    args=p.parse_args()
    if not args.self_test and not args.original_zeta:
        p.print_help();return
    if args.self_test:
        arithmetic_controls()
        cert=certificate()
    if args.original_zeta:original_source_gate(args.original_zeta)
    if args.receipt:
        if not (args.self_test and args.original_zeta):
            raise ValueError("NOT_READY: requires exact arithmetic AND six frozen source SHA")
        args.receipt.write_text(json.dumps(cert,indent=2)+"\n",encoding="utf8")
        print(cert["status"])
if __name__=="__main__":
    try:main()
    except (AssertionError,ValueError,OSError,ZeroDivisionError) as exc:
        raise SystemExit("CP025 FAIL-CLOSED: "+repr(exc))
