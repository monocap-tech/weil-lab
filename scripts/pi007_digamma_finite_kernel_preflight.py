#!/usr/bin/env python3
"""PI007 exact rational partial-fraction and finite-kernel preflight.

An independent rational sanity check for the analytical identities in
PI007_DIGAMMA_FINITE_KERNEL_AND_TAIL.md.

NOT a Lean compiler run; NOT a proof of Fourier inversion, the digamma
partial-fraction theorem, Masullo's operator trace or RH/GRH.
"""
from fractions import Fraction as Q
from math import isqrt


def test_finite_gamma_kernel() -> None:
    # At u=log(q) with q a positive perfect square, all exponentials in
    # K_N(u) = sum_{n<N} exp(-(2n+1/2)|u|) become rational exactly.
    for q in (4, 9, 16, 25, 36, 49, 64, 81):
        root = isqrt(q)
        assert root * root == q and q > 1
        K = Q(1, root) / (1 - Q(1, q * q))
        for N in range(21):
            partial = sum((Q(1, root * q ** (2*n)) for n in range(N)), Q())
            tail = K - partial
            assert partial == K * (1 - Q(1, q ** (2*N)))
            assert tail == K * Q(1, q ** (2*N))
            assert partial >= 0 and tail > 0
    assert Q(1, 3) / (1 - Q(1, 81)) == Q(27, 80)
    assert Q(27, 80) - Q(1, 3) == Q(1, 240)


def real_part_reciprocal(x: Q, y: Q) -> Q:
    assert x*x + y*y != 0
    return x / (x*x + y*y)


def test_complex_digamma_telescope_real_parts() -> None:
    # Exact real part of the complex finite telescope
    #  T_N(z) - S_N(z) = -1/z + 1/(N+z).
    # S_N uses 1/(n+1+z), as in Zeta23's proved partial fraction.
    # T_N uses 1/(n+z), as in the PI007 finite symbol.
    for a, b in ((Q(1, 4), Q(1, 3)),
                 (Q(5, 6), Q(0)),
                 (Q(3, 4), Q(1, 7))):
        for N in range(1, 31):
            shifted = sum((
                Q(1, n + 1) - real_part_reciprocal(n + 1 + a, b)
                for n in range(N)), Q())
            desired = sum((
                Q(1, n + 1) - real_part_reciprocal(n + a, b)
                for n in range(N)), Q())
            expected = (-real_part_reciprocal(a, b)
                        + real_part_reciprocal(N + a, b))
            assert desired - shifted == expected


def test_explicit_tail_coefficients() -> None:
    # For smooth h(0)=0 with ||h'||_infty <= L:
    # |Integral h (K-K_N)| <= L * (1/alpha + 2/alpha^2),
    # alpha = 2*N+1/2. Test exact rational algebra/monotonicity
    # at sample rational L and finite levels; NOT an integration proof.
    for L in (Q(0), Q(1, 9), Q(1), Q(17, 4)):
        previous = None
        for N in range(1, 100):
            alpha = Q(4*N+1, 2)
            upper = L * (1/alpha + 2/(alpha*alpha))
            assert upper >= 0
            if previous is not None:
                assert upper <= previous
            previous = upper


def main() -> None:
    test_finite_gamma_kernel()
    test_complex_digamma_telescope_real_parts()
    test_explicit_tail_coefficients()
    print("PI007 exact rational finite-kernel preflight: PASS")
    print("Eight square-norm checkpoints x N=0..20; exact geometric tails")
    print("Complex digamma finite telescope: rational real-parts checked")
    print("At +/-log9: K=27/80, K_1=1/3, remaining tail=1/240")
    print("C1 derivative-tail bound: rational algebra/monotonicity checked")
    print("NOT checked: Fourier inversion, source Lean build/axioms, trace/RH")


if __name__ == "__main__":
    main()
