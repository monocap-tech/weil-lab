#!/usr/bin/env python3
"""EF26 — authentic original signed arch mixed via positive Laplace/FIR series.

On the original physical source e=1_I cos(omega*x), omega=2*pi*(37/64),
and the exact SI10 b9 469-even-source FIR complement test f=F_h psi:

 m_arch(xi)=psi(1/4)-ln pi +
    int_0^infty [e^(-t/4)/(1-e^-t)]*(1-cos(pi*xi*t))dt.

Original <e,f>=0 exactly, so parity and the true compact cutoff
convert q_arch(e,f) into a positive-measure translation integral
and a real half-integer Laplace series:

 M_arch = 2 Re[e^(i*omega*B) *
     sum_{m>=0} exp(-lambda_m*B)*
     Lambda_h(lambda_m)*cosh(lambda_m*a)*J_r(lambda_m)
     /(lambda_m-i*omega)], lambda_m=2*m+1/2.

 Lambda_h(lambda)=prod_j
   [2*cosh(lambda*h)-2*cos(2*pi*h*c_j)]^pj >0
 J_r(lambda)=integral_-r^r cos^6(pi*x/(2*r))*exp(lambda*x)dx >0.

Every factor is the ORIGINAL SI10 source (107 c_j, 469 orders), with no
surrogate cap, periodization or ignored prime term.

The sign of the mth summand is exactly the sign of
 lambda_m*cos(omega*B) - omega*sin(omega*B).
Authentic source trig gives m0,m1 positive and ALL m>=2 negative.
If a finite outward interval sum m=0..K is negative, the entire
ORIGINAL infinite series is rigorously negative without tail quadrature.
This script checks a source-pinned finite partial sum by 340-digit
OUTWARD integer arithmetic and reports if this sufficient condition
succeeds. It does NOT claim a sign if the finite test is inconclusive.

Even if M_arch<0 and Mprime<0 imply full original M<0, this is
only a single cofinite Schur test, NOT full even Schur PSD/RH.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json, math

from validate_rpb108_si06_negative_band import (
    B, ln_bounds
)
from validate_rpb108_ef21_original_even_fixed_bell import (
    R,H,N,authentic_source_replay,
    physical_support_and_disjointness
)
from validate_rpb108_ef24_original_even_edge_intervals import (
    I,S,PI,D,trig_pi,as_i
)

ROOT=Path(__file__).resolve().parents[1]
C0=F(37,64)
OMEGA=2*PI*C0
KMAX=12


def epos(x):
    """Fully outward exp(x) for 0<=x<=40, by 2^-6 scaling.

    exp(y), y=x/64<=5/8, evaluated with 220 positive Taylor terms.
    Tail <=2/(221!) (since 0<=y<1), then raised to 64
    by six outward squarings. Every op uses I integer intervals.
    """
    x=as_i(x)
    assert x.lo>=0 and x.hi<=40*S
    z=x/64
    assert 0<=z.lo<=z.hi<S
    term=I(S)
    total=term
    for j in range(1,221):
        term=term*z/j
        total=total+term
    tail=I.rational_bounds(0,F(2,factorial(221)))
    y=total+tail
    for _ in range(6):
        y=y*y
    assert y.lo>0
    return y


def eneg(x):
    return I(S)/epos(x)


def cosh_i(x):
    t=epos(x)
    return (t+I(S)/t)/2


def sinh_i(x):
    t=epos(x)
    return (t-I(S)/t)/2


def actual_source():
    centers,orders=authentic_source_replay()
    assert len(centers)==107 and sum(orders)==469
    logs=ln_bounds(2,terms=450)
    aa=I.rational(B+N*H)-I.rational_bounds(*logs)
    assert aa.lo>0 and aa.hi<I.rational(B).lo
    coss=[]
    for c in centers:
        cos,_=trig_pi(2*H*c)
        coss.append(cos)
    cB,sB=trig_pi(2*B*C0)
    assert cB.hi<0 and sB.hi<0
    def sign_factor(lam):
        v=lam*cB-OMEGA*sB
        return v
    assert sign_factor(F(1,2)).lo>0
    assert sign_factor(F(5,2)).lo>0
    assert sign_factor(F(9,2)).hi<0
    return aa,coss,orders,cB,sB


def laplace_bell(lam):
    """Exact EF21 bell Fourier at imaginary frequency, no integral."""
    x=lam*R
    y=x/PI
    denom=I(S)
    for k in (1,2,3):
        denom=denom*(y*y+k*k)
    out=F(45,2)*sinh_i(x)/(lam*denom)
    assert out.lo>0
    return out


def actual_laplace_filter(lam,sourcecos,orders):
    t=2*cosh_i(lam*H)
    out=I(S)
    for u,p in zip(sourcecos,orders):
        factor=100*(t-2*u)
        assert factor.lo>0
        for _ in range(p):
            out=out*factor
    # Positive common normalization of EVERY original Laplace term:
    # out = 100^469 * Lambda_h(lambda), exactly. Original unscaled
    # filter can be <<10^-340 at small lambda and must not be
    # mistaken for the zero mathematical object.
    return out


def exact_arch_term(m,a,sourcecos,orders,cB,sB):
    lam=F(2*m,1)+F(1,2)
    lam_i=I.rational(lam)
    L=actual_laplace_filter(lam_i,sourcecos,orders)
    fac=eneg(lam_i*B)*L*cosh_i(lam_i*a)*laplace_bell(lam_i)
    real=(lam_i*cB-OMEGA*sB)/(lam_i*lam_i+OMEGA*OMEGA)
    val=2*fac*real
    assert (val.lo>0 if m<2 else val.hi<0),("source sign",m)
    return val,fac,real


def noncertifying_double_log_pilot():
    """For understanding dynamic range only; NEVER acceptance proof."""
    centers,orders=authentic_source_replay()
    a=float(B)-math.log(2)+N*float(H)
    theta=2*math.pi*float(C0)*float(B)
    omega=2*math.pi*float(C0)
    pilot=[]
    for m in range(KMAX+1):
        lam=2*m+.5
        lg=sum(p*math.log10(2*math.cosh(lam*float(H))-2*math.cos(2*math.pi*float(H)*float(c)))
               for c,p in zip(centers,orders))
        sign=(lam*math.cos(theta)-omega*math.sin(theta))
        pilot.append((m,round(lg,4),"+" if sign>0 else "-"))
    print("EF26 NONCERTIFYING original source double-log Lambda pilot:",pilot,flush=True)
    print("EF26 exact common positive source scaling 100^469;",
          "ALL displayed interval Laplace terms and partial sums are",
          "100^469 times actual M_arch, preserving exact sign.",flush=True)



def certified_complete_original_variational_lower():
    """First original even mixed e/F source, not whole 469D Schur.

    EF26 finite outward + uniform sign tail => M_arch<0;
    independently rerun authentic EF24 SI06 original Mprime bound:
    Mprime<-10^184. So M=M_arch+Mprime<-10^184.
    Original EF25 E=q_arch(f,f)<30||f||².
    Original EF21 exact ||psi||²=231r/1024, and the TRUE
    bounded source-filter operator norm ||F_h||<=4^469.
    Hence E<30*(231r/1024)*4^938 <10^561.
    Variational true pole-free inverse correction >10^-193.
    Requires mathematical source Laplace/form-domain audit.
    """
    from validate_rpb108_ef24_original_even_edge_intervals import (
        recurrence_211_native, original_bell_hat_at_c0,
        original_edge_interval
    )
    from validate_rpb108_ef22_original_even_prime_energy_vanish import (
        exact_original_n2_signed_mixed_lower
    )
    coeff=recurrence_211_native()
    hat=original_bell_hat_at_c0()
    m5,_,_=original_edge_interval(5,coeff,hat)
    m7,_,_=original_edge_interval(7,coeff,hat)
    n2lo,n2hi,_=exact_original_n2_signed_mixed_lower()
    mprime=I.rational_bounds(n2lo,n2hi)+m5+m7
    assert mprime.hi< -10**184*S, ("original arithmetic lower",mprime.scaled())
    eupper=30*F(231,1024)*R*4**938
    assert eupper<F(10**561)
    lower=F(10**368)/eupper
    assert lower>F(1,10**193)
    print("EF26 COMPLETE ORIGINAL SOURCE INVERSE-SCHUR NONZERO:",
          "M_arch<0 from true half-integer source tail;",
          "Mprime<-10^184 native SI06 340-digit source;",
          "M=M_arch+Mprime<-10^184. E<10^561;",
          "|M|²/E > 10^-193.",
          "This is a microscopic one-source inverse correction,"
          " NOT 469D Schur PSD or RH.",flush=True)



def run():
    data=json.loads((ROOT/"research/obligations.json").read_text())
    obs={x["id"]:x for x in data["obligations"]}
    assert data["active_obligation"]=="W-EVEN-FORM"
    assert all(obs[k]["status"]=="open" for k in (
        "W-EVEN-FORM","W-ODD-NEG","W-WHOLE-FORM"))
    assert "EF26" in obs["W-EVEN-FORM"]["evidence"]
    alo,ahi,phase_lo,phase_hi,normlo=physical_support_and_disjointness()
    a,coss,orders,cB,sB=actual_source()
    noncertifying_double_log_pilot()
    partial=I(0)
    certified_sign=False
    for m in range(KMAX+1):
        term,fac,real=exact_arch_term(m,a,coss,orders,cB,sB)
        partial=partial+term
        print("EF26 RESCALED (100^469) ORIGINAL arch Laplace term",m,
              "sign",term.sign(),"value",term.scaled(),
              "partial",partial.scaled(),flush=True)
        if m>=2 and partial.hi<0:
            print("EF26 CERTIFIED TRUE ORIGINAL M_arch STRICTLY NEGATIVE"
                  " by finite outward partial+uniform negative infinite"
                  " tail; m=",m,"all m'>m negative",
                  "full mixed M=Mprime+M_arch<0 by EF24.",
                  flush=True)
            certified_sign=True
            break
    else:
        print("EF26 INCONCLUSIVE: finite source-pinned"
              " outward partial not negative; no tail sign"
              " of complete M_arch established from this test.",
              flush=True)
    assert certified_sign, ("EF26 source finite partial did not certify"
                            " original arch signed mixing")
    certified_complete_original_variational_lower()
    print("EF26 OPEN: full finite even 469D corrected Schur PSD and"
          " original source/domain independent audit, odd/whole Weil/RH.",
          flush=True)


if __name__=="__main__":
    run()
