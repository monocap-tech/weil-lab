#!/usr/bin/env python3
"""SI04 exact rational regressions; analytic digamma and trace-class arguments in note."""
from fractions import Fraction as F
from math import factorial, isqrt

XI = 2048
B = F(11, 10)
A = F(1, 4)
ACTIVE = {2: 2, 3: 3, 4: 2, 5: 5, 7: 7, 8: 2, 9: 3}


def log_bounds(n, terms=60):
    t = F(n - 1, n + 1)
    power = t
    lo = F(0)
    for k in range(terms):
        lo += 2 * power / (2*k+1)
        power *= t*t
    return lo, lo + 2*power / ((2*terms+1)*(1-t*t))


def sqrt_bounds(n, digits=40):
    scale = 10**digits
    root = isqrt(n*scale*scale)
    return F(root, scale), F(root+1, scale)


def exp_lower(x, n):
    return sum((x**k / factorial(k) for k in range(n+1)), F(0))


def validate():
    log2lo, _ = log_bounds(2)
    assert log2lo > F(69, 100)
    assert exp_lower(F(11,10), 5) > 3  # log3 < 1.1
    assert exp_lower(F(7,10), 3) > 2   # log2 < .7
    assert exp_lower(F(6,5), 3) > F(22,7)  # log(pi) < 1.2
    # Euler's constant <= H_N - log N, with N=32.
    H32 = sum((F(1,k) for k in range(1,33)), F(0))
    assert H32 - 5*log2lo < F(3,5)

    two_C_upper = F(0)
    for n, prime in ACTIVE.items():
        _, upper_log = log_bounds(prime)
        lower_root, _ = sqrt_bounds(n)
        two_C_upper += 2*upper_log / lower_root
    assert two_C_upper < F(177,25)

    y_min = F(3*XI)  # pi > 3
    g0 = y_min**2/(A*(A*A+y_min**2))
    g1 = y_min**2/((A+1)*((A+1)**2+y_min**2))
    assert g0 > F(399,100)
    assert g1 > F(79,100)

    # Integral over k>=2 equals 1/2 log(1+(y/(9/4))**2);
    # the latter exceeds log(y/(9/4)).
    assert y_min/(A+2) == F(8192,3)  # 2**13 / 3
    log_band_lower = 13*F(69,100)-F(11,10)
    assert log_band_lower == F(787,100)

    quarter_constant_upper = F(3,5)+F(11,7)+3*F(7,10)+F(6,5)
    arch_lower = F(399,100)+F(79,100)+log_band_lower-quarter_constant_upper
    assert arch_lower == F(201,28)
    margin = arch_lower - F(177,25)
    assert margin == F(69,700)

    trace = 4*B*XI
    assert trace == F(45056,5)
    physical_negative_upper = quarter_constant_upper+F(177,25)
    assert physical_negative_upper < 13

    print("SI04 PASS: rational arch-prime high-frequency positivity certificate")
    print("original signed 2C upper:",float(two_C_upper))
    print("arch lower bound for |xi|>=2048:",float(arch_lower))
    print("combined signed multiplier strict lower bound:",float(margin))
    print("time-frequency concentration operator trace:",float(trace))


if __name__ == "__main__":
    validate()
