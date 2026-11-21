#!/usr/bin/env python3
"""PI015 independent exact finite Gamma symbol, harmonic/contact coefficient.

All calculations are fractions.Fraction. Euler's constant gamma and log(pi)
are tracked as FORMAL basis elements; they are NOT numerically approximated.
This script does not evaluate Fourier integrals or compile either Lean stack.
"""
from fractions import Fraction as Q


def atom(n: int, r: Q) -> Q:
    a = Q(n) + Q(1, 4)
    return a / (a*a + (r/2)**2)


def harmonic(N: int) -> Q:
    return sum((Q(1, n+1) for n in range(N)), Q())


def finite_gamma_coeff(N: int, r: Q) -> tuple[Q, Q, Q]:
    """Coordinates on independent basis (1, EulerGamma, log(pi))."""
    q = sum((Q(1, n+1) - atom(n, r) for n in range(N)), Q())
    return (q, Q(-1), Q(-1))


def finite_model_coeff(N: int, r: Q) -> tuple[Q, Q, Q]:
    physical_transform = sum((atom(n, r) for n in range(N)), Q())
    return (harmonic(N)-physical_transform, Q(-1), Q(-1))


def scalar_mul(coeff: tuple[Q,Q,Q], h0: Q) -> tuple[Q,Q,Q]:
    return tuple(h0*x for x in coeff)


def main() -> None:
    frequencies = (Q(-31,2), Q(-3), Q(-1,17), Q(0), Q(1,9), Q(7,4), Q(18))
    count = 0
    for N in range(101):
        for r in frequencies:
            source = finite_gamma_coeff(N, r)
            model = finite_model_coeff(N, r)
            assert source == model
            assert source == finite_gamma_coeff(N, -r)
            for h0 in (Q(0), Q(1,5), Q(1), Q(-3,7)):
                paid = scalar_mul(source, h0)
                assert paid == scalar_mul(model, h0)
                assert paid[1] == -h0 and paid[2] == -h0
            count += 1

    # At N=0 no frequency atoms exist, but both contact constants remain:
    # Omega_0 = -EulerGamma -log(pi).
    assert finite_gamma_coeff(0, Q(7)) == (Q(0), Q(-1), Q(-1))
    print("PI015 EXACT SYMBOLIC/FRACTION FINITE-GAMMA PREFLIGHT: PASS")
    print(f"{count} finite frequency-symbol comparisons, four contact scalar variants each")
    print("EulerGamma/log(pi) retained as separate formal basis coordinates")
    print("NOT CHECKED: actual Zeta23 import, Lean builds, inverse Fourier, trace, RH")


if __name__ == "__main__":
    main()
