#!/usr/bin/env python3
"""PS01: exact-rational physical shift/difference-energy original P0/P1 audit.

Archimedean term is an INDEPENDENT exponential-integral series,
not RC46's regular-kernel approximation. The original RC315 certificate
is imported only for its independently pinned comparison and shared
outward-rational elementary constant routines.

Scope: calibration on two vectors, NOT full Weil positivity, Schur or RH.
"""
from fractions import Fraction as F
from math import factorial
import validate_rpb108_rc315_low_mode_sign as old

IV = old.IV
B = F(11, 10)
R = 2 * B
PRIMES = ((2, 2), (3, 3), (4, 2), (5, 5), (7, 7), (8, 2), (9, 3))
N_TERMS = 512

def exp_minus(x):
    """Rational e^(-x) enclosure.

    For x<10: alternating Taylor on x/2^h<=1, then integer powers.
    For x>=10: e>2 and monotonicity give e^(-x)<=2^(-floor x);
    after floor x=128, cap the bound to avoid enormous denominators.
    """
    assert isinstance(x, F) and x > 0
    if x >= 10:
        return IV(0, F(1, 2 ** min(128, x.numerator // x.denominator)))
    y = x
    h = 0
    while y > 1:
        y /= 2
        h += 1
    m = 16
    even = sum(((-y) ** j / factorial(j) for j in range(2 * m + 1)), F(0))
    odd = even - y ** (2 * m + 1) / factorial(2 * m + 1)
    assert 0 < odd < even < 1
    return IV(odd ** (2 ** h), even ** (2 ** h))

def laplace_piece(n, j):
    """Whole [0,infinity) integral of e^(-a_j u) D_nn(u).

    All support overlap and exterior tail are included analytically.
    """
    assert n in (0, 1) and j >= 0
    a = F(4 * j + 1, 2)
    x = a * R
    e = exp_minus(x)
    if n == 0:
        return F(2) / (R * a * a) * (1 - e)
    base = F(6) / (R * a * a) - F(24) / (R ** 3 * a ** 4)
    positive_coefficient = 6 * R * (x + 2) ** 2 / x ** 4
    return IV(base) + positive_coefficient * e

def arch_difference(n):
    """Exact outward bound for sum_j Laplace(D_nn), j>=0.

    Integral comparison for decreasing (2j+1/2)^-p:
      int_N^inf f <= sum_{j=N}^inf f(j)
                      <= f(N)+int_N^inf f.
    For the remote exponential terms use e^(-a_N R)<2^-128.
    """
    total = sum((laplace_piece(n, j) for j in range(N_TERMS)), IV(0))
    a = F(4 * N_TERMS + 1, 2)
    assert a * R > 128
    s2_lo = 1 / (2 * a)
    s2_hi = s2_lo + 1 / a ** 2
    if n == 0:
        tail_lo = F(2) / R * (1 - F(1, 2 ** 128)) * s2_lo
        tail_hi = F(2) / R * s2_hi
    else:
        s4_hi = 1 / a ** 4 + 1 / (6 * a ** 3)
        tail_lo = F(6) / R * s2_lo - F(24) / R ** 3 * s4_hi
        tail_hi = (F(6) / R * s2_hi
                   * (1 + F(1, 2 ** 128) * (1 + F(2) / (a * R)) ** 2))
    assert tail_lo > 0 and tail_lo <= tail_hi
    ans = total + IV(tail_lo, tail_hi)
    assert F(0) < ans.lo <= ans.hi
    assert ans.hi - ans.lo < F(1, 100000)
    return ans

def autocorrelation(n, shift):
    """Original normalized zero-extension autocorrelation at shift log(m)."""
    assert shift.lo > 0 and shift.hi < R
    y = shift / R
    if n == 0:
        return 1 - y
    return 1 - 3 * y + 2 * y ** 3

def prime_difference(n):
    """Compute prime terms as -2 sum(w) + sum(w ||g-T_log(n)g||^2)."""
    q = IV(0)
    for m, p in PRIMES:
        ell = old.log_i(F(m))
        coefficient = old.log_i(F(p)) / old.sqrt_i(m)
        corr = autocorrelation(n, ell)
        difference = 2 * (1 - corr)
        q += -2 * coefficient + coefficient * difference
    return q

def full_signed_diagonal(n):
    """Same signed CC27/SI10 form, new arch coordinate system."""
    pi = old.pi_iv()
    # digamma(1/4)=-gamma-pi/2-3*log(2), with original -log(pi).
    arch_constant = (-old.gamma_iv() - pi / 2 - 3 * old.log_i(F(2))
                     - old.log_i(pi))
    arch = arch_difference(n)
    prime = prime_difference(n)
    pole = old.pole_diagonal(n)
    return arch_constant + arch + prime + pole, arch, prime, pole

def run():
    # RC315 checks original CC27/RC313 model, RC46/RC314 Git blob pins.
    earlier = old.run()
    assert earlier["original_CC27_native_source_from_RC313"]
    assert earlier["reg_source_verified"]
    assert earlier["offdiagonal_P0_P1_exactly_zero_by_parity"]
    assert len(earlier["original_low_diagonals"]) == 2

    for n in (0, 1):
        entry = next(row for row in earlier["original_low_diagonals"]
                     if row["n"] == n)
        previous_lo, previous_hi = map(F, entry[
            "physically_normalized_original_Weil_diagonal_interval"])
        assert previous_lo > 0 and previous_lo <= previous_hi
        q, arch, prime, pole = full_signed_diagonal(n)
        old_prime_lo, old_prime_hi = map(F, entry["prime"])
        old_pole_lo, old_pole_hi = map(F, entry["pole"])
        assert prime.lo <= old_prime_hi and old_prime_lo <= prime.hi
        assert pole.lo <= old_pole_hi and old_pole_lo <= pole.hi
        # Two independently enclosed forms of the SAME signed diagonal
        # must INTERSECT. Both must still prove the prior strict sign.
        assert q.lo <= previous_hi and previous_lo <= q.hi, (
            "original signed PS01/RC315 diagonal enclosures disagree", n)
        assert q.lo > 0 and q.hi - q.lo < F(1, 1000)
        print("PS01 signed original P%d physical-difference Q interval" % n,
              tuple(map(str, q.bounds())), flush=True)
        print("PS01 P%d independent arch difference integral" % n,
              tuple(map(str, arch.bounds())), flush=True)
        print("PS01 P%d original signed prime-shift term" % n,
              tuple(map(str, prime.bounds())), flush=True)
    print("PS01 PASS SCOPED: full original signed P0/P1 reproduced by"
          " physical difference-energy arch integral and prime shifts;"
          " RC315 pins confirmed. W-ODD-NEG, W-EVEN-FORM, Schur, RH OPEN.",
          flush=True)

if __name__ == "__main__":
    run()
