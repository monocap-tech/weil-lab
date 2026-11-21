#!/usr/bin/env python3
"""PI017 pure exact arithmetic sanity: TWO Fourier inverse obligations.

This does NOT prove either Fourier inversion law. It checks that, IF
one has the zero-frequency inversion and even-K_N Fourier pairing, the
PI016 finite-symbol identity yields the precise h(0) contact coefficient,
with EulerGamma and log(pi) tracked as independent formal basis elements.

The stronger theorem candidate is PI017FiniteContactObligations.lean.
No complex integration or Lean compiler claim is made by this script.
"""
from fractions import Fraction as F


def formal_multiplier(N: int, r: F) -> tuple[F, F, F]:
    harmonic = sum((F(1, n+1) for n in range(N)), F())
    atoms = sum(
        ((F(n)+F(1,4)) /
         ((F(n)+F(1,4))**2 + (r/2)**2)
         for n in range(N)), F()
    )
    # Coordinates: (rational, EulerGamma, log(pi))
    return (harmonic-atoms, F(-1), F(-1))


def check() -> int:
    freqs = [F(-5), F(-1,7), F(0), F(3,5), F(11,3)]
    h0_values = [F(0), F(1), F(-3,7), F(7,2)]
    kernel_pair_values = [F(0), F(4,9), F(-5,3)]
    checks = 0
    for N in range(25):
        harmonic = sum((F(1,n+1) for n in range(N)), F())
        for r in freqs:
            atom_sum = sum(
                ((F(n)+F(1,4)) /
                 ((F(n)+F(1,4))**2 + (r/2)**2)
                 for n in range(N)), F()
            )
            omega = formal_multiplier(N,r)
            for h0 in h0_values:
                for J in kernel_pair_values:
                    from_symbol = (
                        omega[0]*h0-J,omega[1]*h0,omega[2]*h0)
                    from_two_inversions = (
                        (harmonic-atom_sum)*h0-J,-h0,-h0)
                    assert from_symbol == from_two_inversions
                    if h0:
                        assert from_symbol[1] == -h0
                        assert from_symbol[2] == -h0
                    checks += 1
    assert checks == 1500
    assert formal_multiplier(0,F(7)) == (F(0),F(-1),F(-1))
    return checks


if __name__ == "__main__":
    count = check()
    print("PI017 CONDITIONAL FINITE CONTACT ARITHMETIC: PASS")
    print(f"{count} exact symbolic rational/contact cases")
    print("EulerGamma and log(pi) retained as separate basis symbols")
    print("NOT proved: either Fourier inversion law, Lean, IV011, Masullo, RH")
