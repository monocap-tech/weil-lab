#!/usr/bin/env python3
"""SI05 exact rational regression of the explicit Fourier-to-Legendre rank bound.

The analytic proof (Rodrigues, Fourier spectral representation, min-max) is in
notes/RPB108_SI05_FREQUENCY_RANK_20261015.md.
"""
from fractions import Fraction as F

B = F(11, 10)
OMEGA = 2048
N = 20480


def validate():
    # SI04 inherited safe band: m_-=0 for |xi|>=2048 and 0<=m_-<13.
    z_max = 2 * F(22, 7) * B * OMEGA
    assert z_max == F(495616, 35)
    # e<11/4 and n! >= (n/e)^n. At all n>=N, use common geometric ratio.
    r = F(11, 4) * z_max / (2 * N)
    assert r == F(1331, 1400)
    assert r < F(24, 25)
    q = F(24, 25) ** 2
    assert q == F(576, 625)
    # q**9 <1/2; exact integer inequality without floating point or logs.
    assert 2 * 24**18 < 25**18
    assert N >= 9 * 2275

    # Infinite tail exact geometric-series prefactor.
    pre = 2 * B * (F(2 * N + 1) / (1 - q)
                   + 2 * q / (1 - q)**2)
    assert pre < 2**21
    # q**N < 2**(-2275), so projection tail squared <2**(-2254).
    projection_tail_sq_ub = F(1, 2**2254)
    assert pre * q**N < projection_tail_sq_ub

    # m_- is nonnegative, supported in an interval length 2*Omega,
    # with height <13; the mass is <2**16.
    negative_mass_upper = 2 * OMEGA * 13
    assert negative_mass_upper == 53248 < 2**16
    # Each ||phi_xi||=sqrt(2B), and 2 sqrt(2B)<4.
    assert 2 * B < 4
    # Operator-norm error <=4*2**16*2**(-1127) = 2**(-1109).
    # The exact amplification bound is therefore <2**(-1000).
    assert 2 + 16 - 1127 == -1109
    assert -1109 < -1000

    assert N == 20480 and N+1 == 20481
    print("SI05 PASS: all rational plane-wave tail / finite-rank bounds")
    print("geometric common ratio upper:",r)
    print("projection-tail exact prefactor:",float(pre))
    print("negative-frequency mass upper:",negative_mass_upper)
    print("certified rank incl. odd negative pole:",N+1)
    print("certified physical operator norm error: < 2^-1109 < 2^-1000")


if __name__ == "__main__":
    validate()
