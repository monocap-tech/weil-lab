#!/usr/bin/env python3
"""PI008 independent exact-Fraction digamma frequency/physical truncation checks.

Confirms finite algebraic coefficient bounds and representative finite tails.
Does NOT prove infinite-series comparisons, Fourier inversion, integration
bounds, Zeta23 source binding, a Lean build, or Masullo's global trace theorem.
"""
from fractions import Fraction as Q
from math import isqrt


def d(n: int, r: Q) -> Q:
    assert n >= 0
    a = Q(n) + Q(1, 4)
    t = r / 2
    return Q(1, n + 1) - a / (a*a + t*t)


def d_decomposition(n: int, r: Q) -> Q:
    a = Q(n) + Q(1, 4)
    t = r / 2
    return -Q(3, 4) / ((n + 1)*a) + (t*t) / (a * (a*a+t*t))


def atom_bound(n: int, r: Q) -> Q:
    return Q(3, (n+1)**2) + 16*r*r / (n+1)**3


def tail_bound(N: int, r: Q) -> Q:
    assert N >= 1
    return Q(3, N) + 8*r*r / (N*N)


def check_fraction_digamma() -> None:
    # Test exact decomposition and positive majorant at rational points.
    for n in range(101):
        for r in (Q(0), Q(1,3), Q(-2,7), Q(3,2), Q(-7), Q(100,11)):
            term = d(n, r)
            assert term == d_decomposition(n, r)
            assert abs(term) <= atom_bound(n, r)
            assert d(n, r) == d(n, -r)

    # Finite slices of the infinite tail must each obey the same
    # rigorous upper bound; infinite tail proof is analytic, not sampling.
    for r in (Q(0), Q(1,3), Q(-2,7), Q(3,2), Q(-7)):
        for N in (1, 2, 3, 4, 10, 20, 40):
            partial_tail = sum((d(n, r) for n in range(N, 128)), Q())
            assert abs(partial_tail) <= tail_bound(N, r)
            assert Q(3, N) >= 0 and Q(8)*r*r/N**2 >= 0


def check_physical_kernel() -> None:
    # At u=log q for perfect square q, the physical kernel and every
    # finite exponential sum are rational exactly.
    for q in (4, 9, 16, 25, 36, 49):
        root = isqrt(q)
        assert root*root == q
        K = Q(1, root) / (1-Q(1, q*q))
        for N in (0, 1, 2, 3, 4, 6, 10):
            KN = sum((Q(1, root*q**(2*n)) for n in range(N)), Q())
            assert K-KN == K/Q(q**(2*N))
    assert Q(27, 80) - Q(1, 3) == Q(1, 240)


def check_contact_linear_algebra() -> None:
    # Exact finite-source identity: for h=g+h0 eta with g(0)=0,
    # (c_N h0 - I_N(h))=h0(c_N-I_N(eta))-I_N(g).
    for h0 in (Q(0), Q(1), Q(-3, 7)):
        for cN in (Q(0), Q(1, 6), Q(19, 10)):
            for Ig in (Q(-1, 3), Q(0), Q(13, 5)):
                for Ieta in (Q(1, 2), Q(-2, 3)):
                    Ih=Ig+h0*Ieta
                    assert cN*h0-Ih == h0*(cN-Ieta)-Ig


def main() -> None:
    check_fraction_digamma()
    check_physical_kernel()
    check_contact_linear_algebra()
    print("PI008 INDEPENDENT EXACT-RATIONAL PREFLIGHT: PASS")
    print("Finite digamma atom decomposition, evenness and polynomial majorant: verified")
    print("Rational finite slices of O(1/N) frequency tail: verified")
    print("Physical finite-kernel geometric tails at 6 square norms: verified")
    print("Finite contact compensation algebra: verified")
    print("NOT checked: full infinite sum, Fourier atom integral, Lean compilation/axioms, Masullo trace")


if __name__ == "__main__":
    main()
