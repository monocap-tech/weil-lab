#!/usr/bin/env python3
"""PI018 ANALYTIC-ONLY exact-contact anchor regression.

No Lean imports, no build, no workflow creation, no approximate quadrature.
All exponentials are integrated symbolically:
  integral_R exp(-b*|u|) du = 2/b for rational b>0.
The script verifies exact finite H_N cancellation at eta_*(u)=exp(-3|u|/2),
the uniqueness witness at N=1, and exact changes of compensation gauge.

It does not prove Fourier inversion, the digamma series, the Masullo trace,
the source IV011 theorem, or global Weil positivity / RH.
"""
from fractions import Fraction as Q


ANCHOR = Q(3, 2)


def harmonic(N: int) -> Q:
    assert N >= 0
    return sum((Q(1, n + 1) for n in range(N)), Q())


def gamma_kernel_pairing(N: int, anchor: Q) -> Q:
    """Exact integral_R exp(-anchor*|u|) K_N(u)du."""
    assert N >= 0 and anchor > 0
    return sum(
        (Q(2) / (anchor + 2*Q(n) + Q(1, 2)) for n in range(N)), Q()
    )


def contact_rational_remainder(N: int, anchor: Q) -> Q:
    """C_{a,N} = (-gamma-log pi) + this RATIONAL remainder."""
    return harmonic(N) - gamma_kernel_pairing(N, anchor)


def check() -> None:
    count = 0
    for N in range(257):
        H = harmonic(N)
        anchor_integral = gamma_kernel_pairing(N, ANCHOR)
        assert anchor_integral == H
        assert contact_rational_remainder(N, ANCHOR) == 0
        count += 1

    # One positive truncation (N=1) forces a=3/2 uniquely:
    # integral eta_a K_1 = 2/(a+1/2) = 1 iff a=3/2.
    assert gamma_kernel_pairing(1, ANCHOR) == 1
    for a in (Q(1, 10), Q(1, 2), Q(1), Q(2), Q(7, 2), Q(10)):
        assert gamma_kernel_pairing(1, a) != 1
        assert (gamma_kernel_pairing(1,a)<1) == (a>ANCHOR)

    # For eta_{1/2}, the exact half-integer harmonic identity gives
    # integral eta_{1/2} K_N = 2 H_{2N} - H_N.
    for N in range(101):
        expected = 2*harmonic(2*N) - harmonic(N)
        assert gamma_kernel_pairing(N, Q(1, 2)) == expected

    # For eta_{7/2}, z = 2, contact shift = 1 - 1/(N+1).
    for N in range(101):
        expected = 1 - Q(1, N+1)
        assert contact_rational_remainder(N,Q(7,2)) == expected

    # The contact offset moves with the compensation gauge.
    # c_a,N - c_b,N = integral_R (eta_b - eta_a) K_N.
    # This finite identity is literal algebra, not a conjecture.
    anchor_pairs = (
        (Q(1, 5), Q(1, 2)),
        (Q(1, 2), Q(3, 2)),
        (Q(3, 2), Q(7, 2)),
        (Q(7, 2), Q(9, 2)),
    )
    for a, b in anchor_pairs:
        for N in (0,1,2,5,10,30,100):
            lhs = (contact_rational_remainder(N,a)
                   - contact_rational_remainder(N,b))
            rhs = (gamma_kernel_pairing(N,b)
                   - gamma_kernel_pairing(N,a))
            assert lhs == rhs

    # At finite N the correctly compensated pairing is gauge invariant,
    # even on a diagonal h(0) != 0. The physical integral of h*K_N
    # cancels algebraically, so an arbitrary formal rational value is used.
    for N in range(20):
        for h0 in (Q(0), Q(1), Q(-3,7)):
            for physical_h_kernel in (Q(0), Q(2,3), Q(-5,4)):
                canonical = (harmonic(N)*h0 - physical_h_kernel)
                for a in (Q(1,2), Q(3,2), Q(7,2)):
                    compensated = (
                        contact_rational_remainder(N,a)*h0
                        - (physical_h_kernel
                           - h0*gamma_kernel_pairing(N,a))
                    )
                    assert compensated == canonical

    # Every modification T_c(h)=T_source(h)+c*h(0) is invisible
    # on h(0)=0 tests, but differs for a nonzero diagonal.
    for c in (Q(-9),Q(1,3),Q(3)):
        for source_pair in (Q(0),Q(5,7)):
            assert source_pair + c*Q(0) == source_pair
            assert source_pair + c*Q(1) != source_pair

    print("PI018 ANALYTIC-ONLY EXACT RATIONAL PREFLIGHT: PASS")
    print(f"{count} finite anchor levels with exact H_N cancellation")
    print("101 half-integer and 101 z=2 alternative-anchor checks")
    print(f"{len(anchor_pairs)*7} finite compensation gauge transitions")
    print("540 finite diagonal gauge-independence checks")
    print("3 nonzero contact offsets invisible on h(0)=0")
    print("NO Lean, Actions, numerical quadrature, Masullo trace or RH claims")


if __name__ == "__main__":
    check()
