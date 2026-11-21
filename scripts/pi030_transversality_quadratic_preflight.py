#!/usr/bin/env python3
"""PI030 exact Fraction regression: two-channel amplitudes, margins, root derivatives.

This is arithmetic/preflight ONLY, not a computation of Q_m, G_m, H_m,
an execution of Sard's theorem, a Lean build, or a certified spectral sum.

For PI027 original d=log(10/9), ell=d/100, Delta=d/2:
 rho_u=b(x-d/5)+u*b(x-7d/10), phi=L_m rho_u.
 Q=autocorrelation(L_m b), q=Q(0)>0, support(Q) within [-ell,ell].
 C_u(t)=(1+u²)Q(t)+uQ(t-Delta)+uQ(t+Delta).
 B_u(a)=(1+u²)G(a)+2uH(a), G,H>0.
 On a=log3-t, 0<=t<=d, P_u(a)=(log3/sqrt3)*C_u(t).
 At a cancellation, the exact parameter derivatives are
   central:   dTheta/du = 2H*(1-u²)/(1+u²);
   satellite: dTheta/du = G*(u-1/u).
 For all u in [1/2,2], all orders m>=1, the three crossing
 sign controls are strict, using B/J<1/450 and log3/sqrt3>1/3.
"""
from fractions import Fraction as F
from functools import reduce


def source_channels(t: F, Delta: F, ell: F) -> tuple[bool, bool, bool]:
    return (abs(t) < ell, abs(t-Delta) < ell, abs(t+Delta) < ell)


def nu(n: int) -> F:
    return 2 * F(n) + F(1, 2)


def gamma_polynomial(m: int, n: int) -> F:
    v = nu(n)
    return v*v*reduce(lambda s,j: s*(v*v-nu(j)**2)**2, range(m), F(1))


def central_theta(u: F, G: F, H: F, kQ: F) -> F:
    return (1+u*u)*(G-kQ)+2*u*H


def satellite_theta(u: F, G: F, H: F, kQ: F) -> F:
    return (1+u*u)*G+u*(2*H-kQ)


def check_derivative_on_zero(u: F, G: F, H: F) -> None:
    assert u > 0 and G > 0 and H > 0
    # Values of kappa*Q chosen algebraically to satisfy the root equation.
    kQ_c = G + 2*u*H/(1+u*u)
    assert central_theta(u,G,H,kQ_c) == 0
    d_c = 2*u*(G-kQ_c)+2*H
    expected_c = 2*H*(1-u*u)/(1+u*u)
    assert d_c == expected_c
    assert (d_c == 0) == (u == 1)

    kQ_s = 2*H+(u+1/u)*G
    assert satellite_theta(u,G,H,kQ_s) == 0
    d_s = 2*u*G+2*H-kQ_s
    expected_s = G*(u-1/u)
    assert d_s == expected_s
    assert (d_s == 0) == (u == 1)


def main() -> None:
    ell, Delta, x0 = F(1,100), F(1,2), F(1,5)
    assert 0 < x0 < x0+ell < x0+Delta < x0+Delta+ell < 1
    assert Delta > 2*ell
    assert source_channels(F(0), Delta, ell) == (True,False,False)
    assert source_channels(Delta, Delta, ell) == (False,True,False)
    for t in (ell, Delta-ell, Delta+ell):
        assert source_channels(t, Delta, ell) == (False,False,False)

    # Only n=3 original prime sample in whole first prime window.
    assert F(3)/F(10,9)**2 == F(243,100) > 2
    assert F(3)*F(10,9) == F(10,3) < 4
    assert F(8,9) < 1                   # K(log2)^2<1
    # 2*ell*d < d/50 < 1/450; uses analytic log(10/9)<1/9.
    assert F(1,50) * F(1,9) == F(1,450)

    # Test the exact source Gamma-mode algebra with rational weights,
    # not the full Laplace integrals (those are analytic inputs).
    count = 0
    for m in range(1,13):
        for j in range(m):
            assert gamma_polynomial(m,j) == 0
        for n in range(m,m+30):
            assert gamma_polynomial(m,n)>0
            count += 1
    assert count == 360

    # Finite dense rational test grid; uniform u claim is analytically
    # proved by interval endpoint bounds, not by these samples.
    u_values = sorted({F(k,40) for k in range(20,81)} |
                      {F(1,2),F(3,4),F(1),F(5,4),F(2)})
    assert u_values[0] == F(1,2) and u_values[-1] == 2
    for u in u_values:
        q = F(1)
        J = (1+u*u)*q
        central_b_upper = J/F(450)
        central_p_lower = J/F(3)
        assert central_b_upper-central_p_lower == -F(149,450)*J
        satellite_b_upper = J/F(450)
        satellite_p_lower = u*q/F(3)
        assert satellite_b_upper <= F(1,90)*q
        assert satellite_p_lower >= F(1,6)*q
        assert satellite_b_upper-satellite_p_lower <= -F(7,45)*q

    for u in u_values:
        for G,H in ((F(1,19),F(3,17)),(F(1,3),F(1,5)),(F(17,5),F(111,7))):
            check_derivative_on_zero(u,G,H)

    assert F(2)*F(1,2)/(1+F(1,2)**2) == F(4,5)
    assert F(2)*F(2)/(1+F(2)**2) == F(4,5)  # r(u)=r(1/u)
    assert F(1,2)+1/F(1,2) == F(2)+1/F(2)   # s(u)=s(1/u)
    print("PI030 exact support and sole-n=3 arithmetic controls: PASS")
    print(f"PI030 {count} finite positive Gamma coefficient controls: PASS")
    print(f"PI030 {len(u_values)} rational amplitude sign-budget checks: PASS")
    print(f"PI030 {3*len(u_values)} central/satellite root derivative identities: PASS")
    print("PI030 Sard/transversality and all-m generalization: mathematical proof only")
    print("No exact smooth-integral evaluation, named rational generic u, Lean, trace, or Actions.")


if __name__ == "__main__":
    main()
