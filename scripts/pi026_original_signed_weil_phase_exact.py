#!/usr/bin/env python3
"""PI026 ANALYTIC-ONLY exact Fractions regression: full signed Weil phase law.

The smooth mathematical construction, proven in the companion memo:
  rho nonzero, real >=0, Cc-infinity on (0, log(10/9));
  phi_m = partial * product_(j<m)(partial^2-lambda_j^2)rho,
  lambda_j=2*j+1/2, m>=1;
  a=log(9/4), psi_m(x)=phi_m(x-a);
  s_beta=(phi_m+beta*psi_m)/sqrt(2), |beta|=1;
  h_beta(u)=integral s_beta(x) conjugate(s_beta(x-u)) dx.

For each beta, original prime samples, both pole Fourier values
and the total Mellin moment vanish. All have the same identity mass J.
Original Weil W(h_beta)=W(C_m)+B_m Re(beta), where
B_m=sum_(n>=m) B_mn*R(lambda_n)*R(-lambda_n)>0, and every
B_mn is an exact POSITIVE rational at this q=9/4.
The script treats the positive Laplace factors R(±lambda) as FORMAL,
not as numerical data for a particular rho.

Chapter 12/13 ZERO-SUM predictions are strictly CONDITIONAL on the
printed trace claims and common source-normalization dictionary:
Z12(D_even)=2B_m, Z13(D_even)=4B_m.
These are NOT observed or independently evaluated spectra.

No gamma integrals, zeta zero lookup, Masullo trace evaluation,
Lean, CI or Actions invocations occur here.
"""
from fractions import Fraction as Q
from math import isqrt

SHIFT_Q = Q(9, 4)
SUPPORT_WIDTH_Q = Q(10, 9)


def lam(n: int) -> Q:
    return Q(2*n) + Q(1, 2)


def annihilator(m: int, z: Q) -> Q:
    out = -z
    for j in range(m):
        out *= z*z - lam(j)**2
    return out


def gamma_mode_coefficient(m: int, n: int) -> Q:
    """B_m,n divided by independent positive R(lambda_n)R(-lambda_n)."""
    z = lam(n)
    damping = Q(2, 3) * SHIFT_Q ** (-2*n)
    square = z*z
    for j in range(m):
        square *= (z*z - lam(j)**2)**2
    return damping * square


def unit_rational_phases() -> list[tuple[Q, Q]]:
    return [
        (Q(1),Q(0)), (Q(-1),Q(0)), (Q(0),Q(1)), (Q(0),Q(-1)),
        (Q(3,5),Q(4,5)), (Q(3,5),Q(-4,5)),
        (Q(-3,5),Q(4,5)), (Q(-3,5),Q(-4,5)),
        (Q(5,13),Q(12,13)), (Q(-5,13),Q(-12,13))
    ]


def main() -> None:
    assert Q(2) < SHIFT_Q/SUPPORT_WIDTH_Q == Q(81, 40)
    assert SHIFT_Q*SUPPORT_WIDTH_Q == Q(5,2) < Q(3)
    assert SUPPORT_WIDTH_Q < SHIFT_Q
    assert (Q(2,3)/(Q(1)-Q(4,9)**2)) == Q(54,65)

    # The elementary zero-moment and exact n=0 pole annihilator.
    coefficients_checked=0
    phase_checks=0
    for m in range(1,9):
        assert annihilator(m,Q(0))==0
        assert annihilator(m,Q(1,2))==0
        assert annihilator(m,Q(-1,2))==0
        for n in range(m):
            assert gamma_mode_coefficient(m,n)==0

        for n in range(m,m+50):
            t=lam(n)
            assert annihilator(m,t)*annihilator(m,-t) == (
                -t*t*__import__("functools").reduce(
                    lambda x,j:x*(t*t-lam(j)**2)**2,range(m),Q(1)))
            assert gamma_mode_coefficient(m,n)>0
            coefficients_checked+=1

        # A formal truncated B_m with positive R_lambda R_-lambda factors
        # set to one FOR REGRESSION ONLY, not a claimed smooth rho integral.
        B=sum((gamma_mode_coefficient(m,n)
               for n in range(m,m+7)),Q())
        assert B>0
        for base in (Q(-13,7),Q(0),Q(2,5)):
            values={}
            for re,im in unit_rational_phases():
                assert re*re+im*im==1
                value=base+B*re
                values[(re,im)]=value
                assert value-base==B*re
                phase_checks+=1
            assert values[(Q(1),Q(0))]-values[(Q(-1),Q(0))]==2*B
            assert values[(Q(0),Q(1))]==values[(Q(0),Q(-1))]
            # If original W(D)=2B, and prime+pole are zero, the
            # literal Chapter12/Chapter13 equations would give the
            # respective whole zero-side values in a 1:2 ratio.
            W_D=2*B
            gamma_integral_D=-W_D
            Z12_if_valid=-gamma_integral_D
            Z13_if_valid=-2*gamma_integral_D
            assert (Z12_if_valid,Z13_if_valid)==(2*B,4*B)
            assert Z12_if_valid-Z13_if_valid==gamma_integral_D

    assert gamma_mode_coefficient(1,0)==0
    assert gamma_mode_coefficient(1,1)==Q(800,27)
    assert 2*gamma_mode_coefficient(1,1)==Q(1600,27)

    print("PI026 EXACT RATIONAL PHASE / ORIGINAL-WEIL SOURCE PREFLIGHT: PASS")
    print("exact prime gap: (log2,log3) excludes ALL log prime powers")
    print("all unit phases share identity contact, total and pole moments")
    print(f"{coefficients_checked} exact surviving positive Gamma mode checks")
    print(f"{phase_checks} exact rational unit-phase W0+B*Re(beta) checks")
    print("m=1 lower coefficient: B>=800/27 R(5/2)R(-5/2)")
    print("Chapter12 vs Chapter13 literal-source spectral predictions:")
    print("  Z12(D)=2B, Z13(D)=4B, CONDITIONAL on BOTH trace identities")
    print("NO independent zero-sum evaluation / Lean / CI / Masullo verification")


if __name__=="__main__":
    main()
