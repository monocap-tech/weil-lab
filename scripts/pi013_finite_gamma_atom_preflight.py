#!/usr/bin/env python3
"""PI013 independent exact arithmetic: source Gamma atom and finite Fourier sums.

Uses fractions.Fraction only. Checks algebraic Fourier coefficients from
PI012 and PI008, and physical kernel values at log(9). It does NOT
evaluate improper integrals, compile Lean or certify Masullo's trace.
"""
from fractions import Fraction as Q


FREQUENCIES = (
    Q(-17, 3), Q(-2), Q(-1, 7), Q(0), Q(1, 9), Q(5, 4), Q(13)
)


def damping(n: int) -> Q:
    assert n >= 0
    return 2 * (Q(n) + Q(1, 4))


def fourier_atom(n: int, r: Q) -> Q:
    alpha = damping(n)
    assert alpha > 0
    return 2 * alpha / (alpha * alpha + r * r)


def gamma_atom(n: int, r: Q) -> Q:
    a = Q(n) + Q(1, 4)
    return a / (a * a + (r / 2) ** 2)


def main() -> None:
    atoms = 0
    finite = 0

    for n in range(256):
        a = damping(n)
        assert a == 2 * Q(n) + Q(1, 2)
        for r in FREQUENCIES:
            actual = fourier_atom(n, r)
            assert actual == gamma_atom(n, r)
            assert actual == fourier_atom(n, -r)
            assert actual > 0
            if r == 0:
                assert actual == Q(2) / a
            atoms += 1

    for N in (0, 1, 2, 3, 8, 16, 32, 64):
        for r in FREQUENCIES:
            true_source = sum((fourier_atom(n, r) for n in range(N)), Q())
            gamma_source = sum((gamma_atom(n, r) for n in range(N)), Q())
            assert true_source == gamma_source
            finite += 1

    # Distinct physical-space finite kernel anchor, where exp(u)=9.
    for N in range(50):
        value = sum((Q(1, 3 * 9 ** (2*n)) for n in range(N)), Q())
        assert value == Q(27, 80) * (1 - Q(1, 9 ** (2*N)))

    print("PI013 INDEPENDENT EXACT FRACTION PREFLIGHT: PASS")
    print(f"Verified {atoms} source Fourier/Gamma atom identities")
    print(f"Verified {finite} finite Fourier-sum/Gamma-sum identities")
    print("Checked 50 exact physical kernel stages at u=log(9)")
    print("No floating-point frequency fitting or invented 2*pi normalization")
    print("NOT CERTIFIED: improper integrals, Lean, original IV011, Masullo, RH")


if __name__ == "__main__":
    main()
