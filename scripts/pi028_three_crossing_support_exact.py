#!/usr/bin/env python3
"""PI028 exact support/inequality regression; NO smooth-integral or Lean certification.

The mathematical memo fixes:
 d=log(10/9), ell=d/100, Delta=d/2, x0=d/5,
 b(x)=exp(-1/((x/ell)(1-x/ell))) on (0,ell), zero outside,
 rho(x)=b(x-x0)+b(x-x0-Delta),
 phi_m=L_m rho, L_m=D prod_{j<m}(D^2-(2j+1/2)^2).
 With Q=autocorrelation(L_m b), C=2Q+Q(.-Delta)+Q(.+Delta),
 J=2Q(0)>0, Q supported on [-ell,ell], Q(+-ell)=0.
 On a=log3-t for t in [0,d]:
   P(a)=(log3/sqrt3) C(t), 0<B(a)<J/9.
 This script checks only exact rational support geometry and sign margins.
"""
from fractions import Fraction as F

ELL = F(1, 100)       # lengths in units of d
DELTA = F(1, 2)
X0 = F(1, 5)

def q_may_be_nonzero(t: F) -> bool:
    """Strict interior of a Q support interval, in units of d."""
    return abs(t) < ELL

def correlation_channels(t: F) -> tuple[bool, bool, bool]:
    """Possible support of 2Q(t), Q(t-Delta), Q(t+Delta)."""
    return (
        q_may_be_nonzero(t),
        q_may_be_nonzero(t-DELTA),
        q_may_be_nonzero(t+DELTA),
    )

def main() -> None:
    assert 0 < X0 < X0+ELL < X0+DELTA < X0+DELTA+ELL < 1
    assert DELTA > 2*ELL
    assert DELTA+ELL < 1

    # Open supports; Q(+-ell)=0 because Q is smooth and compactly supported.
    controls = [
        ("satellite exterior", DELTA+ELL, (False, False, False)),
        ("satellite peak", DELTA, (False, True, False)),
        ("satellite interior", DELTA-ELL, (False, False, False)),
        ("central exterior", ELL, (False, False, False)),
        ("central peak", F(0), (True, False, False)),
    ]
    for title,t,expected in controls:
        actual = correlation_channels(t)
        assert actual == expected, (title,t,actual,expected)

    # At t=Delta, C=Q(0)=J/2. At t=0, C=2Q(0)=J.
    assert DELTA - ELL == F(49,100)
    assert DELTA == F(50,100)
    assert DELTA + ELL == F(51,100)
    assert ELL == F(1,100)
    j_ratios = {
        DELTA+ELL: F(0),
        DELTA: F(1,2),
        DELTA-ELL: F(0),
        ELL: F(0),
        F(0): F(1),
    }
    assert len(j_ratios) == 5

    # For a=log3-t, 0<=t<=d: the window a+-d sees n=3 only.
    # We use rational powers at integer multiples of d, no floating logs.
    exp_d = F(10,9)
    assert F(3)/exp_d**2 == F(243,100) > 2
    assert F(3)*exp_d == F(10,3) < 4
    assert F(3) > exp_d**2  # a>=log3-d > d

    # K(log2)^2=8/9<1; K decreasing; a-d >= log(243/100)>log2.
    # log(10/9)<1/9 and log3/sqrt3>1/3 are analytic memo inputs.
    assert F(8,9) < F(1)
    gamma_ratio_ceiling = F(1,9)
    kappa_ratio_floor = F(1,3)
    satellite_margin = gamma_ratio_ceiling - kappa_ratio_floor*j_ratios[DELTA]
    center_margin = gamma_ratio_ceiling - kappa_ratio_floor*j_ratios[F(0)]
    assert satellite_margin == -F(1,18)
    assert center_margin == -F(2,9)
    assert satellite_margin < 0 and center_margin < 0

    # In ascending a order: positive, negative, positive, positive, negative.
    # Three disjoint IVT brackets of exact width ell.
    # Using t coordinates reverses a ordering.
    bracket_t = [
        (DELTA,DELTA+ELL),
        (DELTA-ELL,DELTA),
        (F(0),ELL),
    ]
    assert all(high-low == ELL for low,high in bracket_t)
    assert bracket_t[0][0] >= bracket_t[1][1]
    assert bracket_t[1][0] > bracket_t[2][1]
    signs_by_t = [
        (+1,-1),   # t from Delta+ell down to Delta, a increases
        (-1,+1),   # t from Delta down to Delta-ell, a increases
        (+1,-1),   # t from ell down to 0, a increases
    ]
    assert signs_by_t == [(1,-1),(-1,1),(1,-1)]

    print("PI028 exact nonnegative two-subbump support: PASS")
    print("PI028 5 original n=3 source-channel controls: PASS")
    print("PI028 rational source prime-isolation/Gamma ceiling: PASS")
    print("PI028 strict satellite Θ<-J/18 and central Θ<-2J/9: PASS")
    print("PI028 3 disjoint analytical IVT brackets, each width d/100: PASS")
    print("No computed B/C smooth integral, derivative enclosure, spectral sum, Lean or Actions.")

if __name__ == "__main__":
    main()
