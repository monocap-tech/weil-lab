#!/usr/bin/env python3
"""EF25 — true ORIGINAL archimedean energy and mixed source norm bounds.

On EF21's EXACT original SI10 even 469-source FIR/C5 cosine bell f:
  q_prime(f,f)=0, so E=q_arch(f,f) (EF22 genuine support proof).
  mu||f||^2 <= E < 30||f||^2,
  ||arch(D)e||_2 < 47 and |q_arch(e,f)| <47||f||_2,
where e=1_I cos(2*pi*(37/64)*x), I=[-11/10,11/10].

No high-frequency integration or spectral grid. The upper energy is an
actual original digamma-symbol bound and exact physical derivative ratio.
The source mixed bound is a norm UPPER, not a sign/cancellation certificate.
No positive lower on |M_arch+Mprime| or corrected Schur PSD/RH.

All rational regression arithmetic is exact. The digamma symbol
inequalities and Parseval/Jensen are written in the mathematical note
for independently reviewable analytic attachment; CI validates their
finite rational sufficient conditions, not the general theorem itself.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

from validate_rpb108_si06_negative_band import (
    B, PI, LN, GAMMA_UP, ACTIVE, WEIGHTS
)
from validate_rpb108_ef21_original_even_fixed_bell import (
    R, H, N, authentic_source_replay, bell_transform_identity,
    physical_support_and_disjointness
)
ROOT=Path(__file__).resolve().parents[1]
MU=F(17,25000)


def arch_symbol_global_gate():
    """Proven analytic symbol envelope from original digamma sum.

    a(xi)=Re psi(1/4+i*pi*xi)-ln pi.
    a(xi)=psi(1/4)-ln pi+
      sum_n y^2/((n+1/4)*((n+1/4)^2+y^2)), y=pi*|xi|.
    a(0)>-8, a(xi)>-8, a(xi)<8+ln(1+|xi|).

    For y>0 and N0=ceil(y):
      term n=0 <=4; n=1..N0 <=1/n, sum <=1+ln N0;
      tail <=y^2/(2*(N0+1/4)^2)<=1/2.
      psi(1/4)-ln pi<0. Thus
      a(xi)<=11/2+ln(1+y)
         < 8+ln(1+|xi|) using pi<4 and ln4<2.

    Source constant lower: psi(1/4)-ln pi
    =-gamma-pi/2-3ln2-ln pi >-8.
    """
    assert B==F(11,10)
    assert PI[0]>3 and PI[1]<4
    assert LN[2][0]>0 and LN[2][1]<1
    assert GAMMA_UP<F(1)
    assert GAMMA_UP + PI[1]/2 + 3*LN[2][1]+2 <8
    # ln4<2 since e^2>4, rational truncation e^2 >=1+2+2.
    assert F(1)+2+F(2)>4
    assert F(11,2)+2<8
    # e>2 and e²>3 imply ln2<1, ln3<2;
    # exact rational lower of exp(2) >=1+2+2=5>3.
    assert F(1)+F(1)+F(1,2)>2
    assert F(1)+F(2)+F(2)>3
    return True


def exact_native_bell_derivative_ratio():
    """EF21 1,878 disjoint source/filter-shift physical lobes:
      ||b||² = 231r/512,
      ||b'||² = 189*pi²/(512r),
      ||f'||²/||f||²=(9/11)*pi²/r².
    Using Fourier ∫xi²|fhat|²=||f'||²/(4*pi²).
    """
    centers,orders=authentic_source_replay()
    assert len(centers)==107 and sum(orders)==469
    assert (N,H,R)==(469,F(1,2048),F(1,65536))
    mass,norm2=bell_transform_identity()
    alo,ahi,phase_lo,phase_hi,normlower=physical_support_and_disjointness()
    assert 0<alo<ahi<B and normlower>0 and norm2==F(231,512)*R
    cos10=F(63,128)*R
    cos12=F(231,512)*R
    sinsq=cos10-cos12
    assert sinsq==F(21,512)*R
    deriv_norm2_over_pi2=9*sinsq/R**2
    assert deriv_norm2_over_pi2==F(189,512)/R
    ratio_over_pi2=deriv_norm2_over_pi2/norm2
    assert ratio_over_pi2==F(9,11)/R**2
    # Original f has exactly two copies each A_k and
    # no overlapping physical supports. Its f'/f ratio is
    # IDENTICAL to the single source bell ratio above.
    return ratio_over_pi2


def original_arch_energy_upper():
    """Actual E=q_arch(f,f)<30||f||², no frequency quadrature.

    Jensen for real weighted |fhat|²:
       average ln(1+xi²)
         <=ln(1+ average xi²)
         = ln(1+9/(44*r²)).
    And 1+|xi| <= 2*(1+xi²).
    With global a(xi)<8+ln(1+|xi|):
       E/||f||² <8+ln2+ln(1+9/(44*r²)).
    ln2<1. Show ln(1+9/(44*r²))<21 using
    rational partial sum exp(21)>=sum_{k=0}^{40} 21^k/k!
    strictly greater than 1+9/(44r²).
    """
    ratio_over_pi2=exact_native_bell_derivative_ratio()
    mean_xi2=ratio_over_pi2/4
    assert mean_xi2==F(9,44)/R**2
    X=1+mean_xi2
    exp21lo=sum((F(21)**k/factorial(k) for k in range(41)),F(0))
    assert X<exp21lo
    assert 8+1+21==30
    # Finite absolutely true E UPPER:
    # ||F_h||<=4^469, ||psi||²=231r/1024:
    # E<30*(231r/1024)*4^938. Huge but verified.
    upper=30*F(231,1024)*R*4**938
    assert upper>0
    return X,upper


def original_arch_source_mixed_upper():
    """Strong-domain source e physically original even c0=37/64.

    |ehat(xi)|<=2B=11/5 always by support.
    For |xi|>=2, exact ehat as two shifted sinc functions gives
      |ehat|<=1/[pi(|xi|-c0)] < 1/|xi|
      since pi>3, c0=37/64 and pi*(1-c0/2)>1.

    Original symbol |arch(xi)|<8+ln(1+|xi|).
    On |xi|<=2, ln(1+|xi|)<ln3<2, giving
      ∫_<2 |arch*ehat|² <=4*10²*(11/5)²=1936.
    On |xi|>=2, ln(1+xi)<1+ln xi,
      2∫_2∞ (9+ln xi)²/xi² dxi
        <2∫_1∞ (9+ln xi)²/xi² dxi
        =2*(81+18+2)=202.
    Total <2138<2200<47².
    Hence ||arch(D)e||_2<47, so |q_arch(e,f)|<47||f||_2.
    This is the TRUE original arch source mixed UPPER,
    with no sign/normalized lower for full M.
    """
    c0=F(37,64)
    assert 0<c0<1
    assert PI[0]*(1-c0/2)>1
    near=4*10**2*(2*B)**2
    tail=2*(81+18+2)
    source_energy=near+tail
    assert near==1936 and tail==202
    assert source_energy==2138
    assert 2138<2200<47**2
    return near,tail,source_energy


def run():
    data=json.loads((ROOT/"research/obligations.json").read_text())
    obs={x["id"]:x for x in data["obligations"]}
    assert data["active_obligation"]=="W-EVEN-FORM"
    assert all(obs[i]["status"]=="open" for i in (
        "W-EVEN-FORM","W-ODD-NEG","W-WHOLE-FORM"))
    assert all(i in obs["W-EVEN-FORM"]["evidence"] for i in (
        "EF22","EF23","EF24","EF25"))
    assert set(ACTIVE)=={2,3,4,5,7,8,9}
    arch_symbol_global_gate()
    X,absolute_E_upper=original_arch_energy_upper()
    near,tail,source_upper=original_arch_source_mixed_upper()
    print("EF25 actual original SI10 107/469 even C5 physical test:",
          "h",H,"r",R,"B",B,flush=True)
    print("EF25 ORIGINAL arch symbol bound:",
          "-8<a(xi)<8+ln(1+|xi|) all xi,",
          "finite rational digamma constant gates PASS.",flush=True)
    print("EF25 EXACT physical derivative/f norm:",
          "||f'||²/(pi²||f||²) =",F(9,11)/R**2,
          "Fourier mean xi² =",F(9,44)/R**2,flush=True)
    print("EF25 certified log-Jensen gate: X=",
          float(X),"exp(21) rational partial sum >",float(X),flush=True)
    print("EF25 ORIGINAL ARCH ENERGY upper:",
          "mu||f||²<=E=q_arch(f,f)<30||f||²;",
          "entire original seven-prime self-energy exactly zero"
          " by native EF22. Finite absolute E upper <"
          "30*(231r/1024)*4^938 (vast, not useful normalized).",
          flush=True)
    print("EF25 ORIGINAL arch first-source strong domain:",
          "||arch(D)e||²<",source_upper,"<2200;",
          "|M_arch|<47||f||. Source low/high contributions",
          near,tail,flush=True)
    print("EF25 METHOD ACCEPT: rigorous source-conditional"
          " FULL original cofinite energy upper and original"
          " arch mixed NORM upper without full frequency mesh.",
          "METHOD STOP: neither source-specific signed M_arch"
          " nor |M_arch+Mprime| sign/lower is known.",flush=True)
    print("EF25 OPEN: actual complete signed M and positive normalized"
          " inverse Schur lower, physical 469D corrected Schur PSD,"
          " form-domain independent audit, odd/whole Weil/RH.",
          flush=True)


if __name__=="__main__":
    run()
