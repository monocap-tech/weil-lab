#!/usr/bin/env python3
"""EF21: fixed real-even physical cosine-bell F469 test and Fourier reduction.

AUTHENTIC original SI10 seven-prime parity-even source family: 107
distinct rational frequencies c_j, orders p_j summing to 469.
Actual fixed original even physical test:
  h=1/2048, r=1/65536, a=B-ln2+469h
  b_r(x)=cos(pi*x/(2r))**6, |x|<r, else 0
  psi(x)=(b_r(x-a)+b_r(x+a))/2
  f=prod_j(T_h+T_-h-2cos(2*pi*h*c_j))**p_j psi.

f is C^5 compact, even, exactly source-orthogonal, hence a genuine
original pole-free signed form/strong-domain test. The 939 shifts of
each bell are all mutually disjoint, giving EXACT physical norm
||f||^2=(231*r/1024) sum_{k=-469}^{469} A_k^2, A_{+-469}=1.

Full original pole-free signed mixed numerator and cofinite energy
are exactly TWO convergent scalar Fourier integrals in the authentic
signed multiplier m(xi), with known analytic ehat, bellhat, and FIR
symbol. A new cancellation-free rational-sine bell Fourier formula
has O(|xi|^-7) tail. This DOES NOT evaluate those integrals,
certify their sign, or supply a normalized Schur lower.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import math

from validate_rpb108_si10_complement_positivity import (
    protected_inner_cover, protected_outer_band, KAPPA, B,
)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_si06_negative_band import SHIFTS, ACTIVE
from validate_rpb108_ef20_original_even_finite_shift import H, N

ROOT=Path(__file__).resolve().parents[1]
R=F(1,65536)
MU=F(17,25000)


def multiply(p,q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            out[i+j]+=a*b
    return out


def bell_transform_identity():
    # cos^6(theta)=(10+15*cos(2theta)+6*cos(4theta)+cos(6theta))/32
    # H_r(xi)=r sum_{k=-3}^3 w_k sinc(2*r*xi-k).
    # w_0=20/32, w_{+-1}=15/32, w_{+-2}=6/32, w_{+-3}=1/32.
    weights={0:F(20,32),1:F(15,32),2:F(6,32),3:F(1,32)}
    assert weights[0]==F(5,8)
    assert weights[0]+2*sum(weights[k] for k in (1,2,3))==2

    # Grouping sin(pi*(q+-k))=(-1)^k sin(pi*q) yields
    # H_r(xi)=r*sin(pi*q)/pi * rational(q)
    # rational(q)=-45/[2*q*(q^2-1)*(q^2-4)*(q^2-9)], q=2*r*xi.
    # Prove rational function numerator is a CONSTANT -45/2
    # by an exact polynomial identity in t=q^2 (not sampling).
    factors={k:[F(-k*k),F(1)] for k in (1,2,3)}
    whole=[F(1)]
    for k in (1,2,3):
        whole=multiply(whole,factors[k])
    num=[weights[0]*v for v in whole]
    for k in (1,2,3):
        prod=[F(1)]
        for j in (1,2,3):
            if j!=k:
                prod=multiply(prod,factors[j])
        piece=[F(0)]+[2*weights[k]*((-1)**k)*v for v in prod]
        for j,v in enumerate(piece):
            num[j]+=v
    assert num==[F(-45,2),F(0),F(0),F(0)],num

    # Fourier transform at xi=0 via sinc:
    # integral bell = 5r/8. Its exact squared L2 norm is
    # ∫_-r^r cos^12(pi*x/(2r)) dx =231r/512.
    bell_mass=F(5,8)*R
    bell_norm2=F(231,512)*R
    assert 0<bell_norm2<bell_mass
    # For |q|>=4, |q^2-k^2| >= q^2*(1-k^2/16).
    # with pi>3, 45*4096/(2*1260*3)<25:
    # |H_r(xi)| <=25r/|2*r*xi|^7.
    assert F(45*4096,2*1260*3)<25
    return bell_mass,bell_norm2


def physical_support_and_disjointness():
    lo,hi=SHIFTS[2]
    a_lo=B-hi+N*H
    a_hi=B-lo+N*H
    assert 0<a_lo<a_hi<B
    # The full FIR support of BOTH bells stays in original [-B,B].
    assert a_hi+N*H+R<B
    assert a_lo-N*H-R>0
    assert 2*R<H
    # Even distinct shifted lobes cannot overlap. Same lobe
    # centers spaced h. Opposite lobe centers separated by
    # abs(2*a+(k-j)h), k,j in [-469,469]. Exact ln2
    # interval gives fractional phase 2*a/h in (2604.25,2604.75).
    two_a_h_lo=2*a_lo/H
    two_a_h_hi=2*a_hi/H
    assert F(10417,4)<two_a_h_lo<two_a_h_hi<F(10419,4)
    # Above are 2604.25 and 2604.75.
    assert H/4>2*R
    # Thus every one of 1878 total translated bell supports is
    # disjoint, despite the potentially huge FIR coefficients.
    # True exact physical norm:
    # ||f||^2=(bell_norm^2/2)*sum_{k=-N}^{N} A_k^2.
    # FIR extreme coefficients A_{-N}=A_N=1, yielding
    # a RIGOROUS physical norm squared lower 231r/512.
    bell_norm2=F(231,512)*R
    norm2_lower=bell_norm2
    assert norm2_lower==F(231,512*65536)
    assert norm2_lower>0
    return (a_lo,a_hi,two_a_h_lo,two_a_h_hi,norm2_lower)


def authentic_source_replay():
    outer,minval=protected_outer_band()
    clusters,w,m,leaves,accepted=protected_inner_cover()
    assert outer==2535 and minval>KAPPA
    assert (len(clusters),leaves,accepted)==(107,973,9261)
    assert w==F(973,32)
    centers=[(l+r)/2 for l,r,_ in clusters]
    degrees=[taylor_order(r-l,9)[0] for l,r,_ in clusters]
    assert len(set(centers))==107
    assert sum(degrees)==N==469
    assert centers[0]==F(37,64)
    # For every original c_j the FIR symbol
    # S_h(xi)=prod_j [2cos(2pi h xi)-2cos(2pi h c_j)]^p_j
    # vanishes to order >=p_j at BOTH signed original c_j,
    # because sin(2pi h c_j)!=0 for 0<c_j*h<1/2.
    assert 2*max(centers)*H<1
    return centers,degrees



def noncertifying_filter_conditioning_pilot(centers,degrees):
    """Fast source-specific double precision LOG amplitude pilot ONLY.

    This is NOT a signed M/E quadrature, mathematical interval,
    or proved FIR ill-conditioning STOP. It prevents unnormalized
    amplitude underflow from being misread as a source zero.
    """
    frequencies=(F(0),F(1),F(100),F(500),F(1000),F(1800),F(2048))
    totals=[]
    for xi in frequencies:
        x=float(xi)
        val=2*math.cos(2*math.pi*float(H)*x)
        logabs=0.0
        for cj,pj in zip(centers,degrees):
            factor=val-2*math.cos(2*math.pi*float(H)*float(cj))
            if factor==0.0:
                logabs=float("-inf")
                break
            logabs+=pj*math.log10(abs(factor))
        totals.append((str(xi),logabs))
    print("EF21 NONCERTIFYING double-log spectral symbol samples",totals,
          "no M/E integration, not acceptance evidence",flush=True)
    return totals



def fixed_step_localization_method_stop():
    """Exact dimensionless scaling constants; analytic boundedness audit.

    Fix h and its original 469-source FIR F_h. The original signed
    physical gradient g=P_I m(D)e has finitely many translated jumps;
    its FIR translate G=F_h g has locally bounded one-sided values
    at +/-a by original log-arch pseudolocality. Let |G|<=C on the
    shrinking supports (the value of C is NOT calculated).
    For the positive cosine-six bells:
      ||psi_r||_1=5r/8,
      ||F_h psi_r||_2^2>=(231/512)r,
      |q0(e,F_h psi_r)| <= C*(5/8)r.
    Since original cofinite q0>=mu||.||², the actual normalized
    variational Schur trial obeys
       |q0(e,f_r)|²/q0(f_r,f_r)
           <= (200/231)*(C²/mu)*r ->0.
    This is a METHOD STOP for r->0 at FIXED h; no claim about
    the explicit r=1/65536 sign, positive cofinite Schur, or C.
    """
    mass_factor=F(5,8)
    physical_floor=F(231,512)
    coefficient=mass_factor**2/physical_floor
    assert coefficient==F(200,231)
    return coefficient



def run():
    custody=json.loads((ROOT/"research/obligations.json").read_text())
    obligations={ob["id"]:ob for ob in custody["obligations"]}
    assert custody["active_obligation"]=="W-EVEN-FORM"
    assert all(obligations[k]["status"]=="open"
               for k in ("W-EVEN-FORM","W-ODD-NEG","W-WHOLE-FORM"))
    assert all(k in obligations["W-EVEN-FORM"]["evidence"]
               for k in ("EF19","EF20","EF21"))
    centers,degrees=authentic_source_replay()
    pilot=noncertifying_filter_conditioning_pilot(centers,degrees)
    mass,norm=bell_transform_identity()
    scaled_bound=fixed_step_localization_method_stop()
    a,b,phase_lo,phase_hi,normlower=physical_support_and_disjointness()
    print("EF21 native ORIGINAL SI10 clusters:",len(centers),
          "even b9 generators",sum(degrees),"step",H,
          "explicit bell radius",R,flush=True)
    print("EF21 actual original shifted arithmetic jump-centered bell:",
          "a in",float(a),float(b),"2a/h in",
          float(phase_lo),float(phase_hi),flush=True)
    print("EF21 EXACT real even physical disjoint shifted-bell L2 bound:",
          "||F_h psi||^2 >= ",float(normlower),
          "and equality formula (231r/1024)*sum(A_k^2).",flush=True)
    print("EF21 EXACT compact cos^6 bell Fourier rational-sine identity:",
          "H_r(xi)= -45r sin(pi q)/[2pi q(q²-1)(q²-4)(q²-9)]",
          "q=2rxi, removable at q=0,±1,±2,±3.",flush=True)
    print("EF21 EXACT physical bell zerofrequency mass:",float(mass),
          "squared L2 norm:",float(norm),flush=True)
    print("EF21 original signed scalar quadrature gates:",
          "M=integral_R m(xi) ehat(xi) H_r(xi) cos(2pi a xi)",
          "*S_h(xi) dxi;",
          "E=integral_R m(xi) |H_r(xi)cos(2pi a xi)S_h(xi)|² dxi.",
          "S_h ORIGINAL 469-factor signed cosine product.",flush=True)
    print("EF21 fixed-h shrinking-bell normalized Schur METHOD STOP:",
          "R_r<= (",scaled_bound,")*(C²/mu)*r ->0 as r->0,"
          " C is unmeasured actual locally bounded signed gradient."
          " No fixed-r sign or numeric Schur lower.",flush=True)
    print("EF21 OPEN: actual original signed numerical M and E",
          "are NOT evaluated or interval-certified. E>=mu||f||²",
          "conditionally on original cofinite analytic proof.",
          "No normalized Schur floor, corrected even PSD or RH.",flush=True)


if __name__=="__main__":
    run()
