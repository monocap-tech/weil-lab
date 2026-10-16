#!/usr/bin/env python3
"""SI11: exact-rational Birman-Schwinger accuracy gate for the original
signed Weil form. Reconstructs the SI10 entire protected-frequency cover;
does NOT assert positivity of the finite inverse-response matrix.

Mathematical matrix identities / compressed inverse warning in SI11 note.
"""
from fractions import Fraction as F
from validate_rpb108_si10_complement_positivity import (
    KAPPA, protected_outer_band, protected_inner_cover,
)
from validate_rpb108_si08_multiband_rank import B, taylor_order

BITS = (9, 10, 12, 16, 20, 21, 24, 32)
CODIM_SI10 = {9:939, 10:1003, 12:1121, 16:1367,
              20:1561, 21:1631, 24:1781, 32:2151}


def validate():
    leaves, amin = protected_outer_band()
    assert leaves == 2535 and amin > KAPPA
    groups, W, M, unresolved, protected = protected_inner_cover()
    assert unresolved == 973 and protected == 9261
    assert len(groups) == 107
    assert W == F(973, 32)
    assert M == F(1203060883, 32000000)

    # The original complete form is A-K, with positive *supported*
    # A >= kappa I and positive compact K supported in the uncertain
    # frequency cover, whose multiplier r=(kappa-m)_+ satisfies
    # integral r <= R = M + kappa*W. The signed odd pole is a rank one
    # inside each reference subspace and adds no residual.
    R = M + KAPPA*W
    assert R == F(1204033883, 32000000)
    assert R < 38
    factor = 4*B*R
    assert factor < 166

    print("SI11 PASS: original signed inverse-response criterion exact rational gate")
    print("certified protected U full width:", float(W))
    print("certified true negative m_- mass upper:", float(M))
    print("certified shifted negative r=(kappa-m)_+ mass upper:", float(R))
    print("original positive base lower floor kappa:", float(KAPPA))

    for bits in BITS:
        eps = F(1, 2**bits)
        n = 2*sum(taylor_order(right-left,bits)[0]
                  for left,right,mass in groups)+1
        # Positive K, original signed pole exactly inside span:
        # ||K-PKP|| <=4 B R eps, and ||(1-P)K(1-P)||<=2 B R eps².
        eta = factor*eps
        relative = eta/KAPPA
        high_loss = 2*B*R*eps**2
        assert KAPPA-high_loss > 0
        if bits in CODIM_SI10:
            assert n == CODIM_SI10[bits]
        if bits == 9:
            assert relative > 300  # SI10 939-dimensional gate cannot use this crude perturbative inverse margin.
        if bits == 16:
            assert relative > 2    # Even the 1367-dimensional gate insufficient for eta<kappa.
        if bits == 20:
            assert relative < F(1, 6) and relative > F(15,100)
        if bits == 21:
            assert relative < F(8,100) and n < 2151
        if bits == 24:
            assert relative < F(1,100)
        if bits == 32:
            assert relative < F(1,25000)
        print("bits:",bits, "supported feature rank <=",n,
              "||K-PKP|| upper:",float(eta),
              "Birman-Schwinger relative error upper:",float(relative),
              "certified complement margin lower:",float(KAPPA-high_loss))

    # Inverse response residual has the *correct positive remainder sign*:
    # <u,A^-1 u>=2<u,y>-<y,Ay>+<u-Ay,A^-1(u-Ay)>.
    # Scalar 2x2-free rational regression: A=2, u=3, y=1, kappa=1.
    a, u, y, k = F(2), F(3), F(1), F(1)
    residual = u-a*y
    exact_inv = u*u/a
    decomposition = 2*u*y-a*y*y+residual*residual/a
    conservative_upper = 2*u*y-a*y*y+residual*residual/k
    assert exact_inv == decomposition < conservative_upper

    # Compression and inversion do not commute. For A=[[2,1],[1,2]]
    # and P projecting onto coordinate 1, 1/(PAP)=1/2 while
    # P A^-1 P=2/3. Using full-line inverse as equality is invalid.
    assert F(1,2) < F(2,3)
    print("SI11: inverse response must be the inverse of the physically supported positive operator")
    print("SI11: no finite BS eigenvalue or full Weil positivity certificate has been established.")


if __name__=="__main__":
    validate()
