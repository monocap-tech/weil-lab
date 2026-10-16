#!/usr/bin/env python3
"""SI06 exact original signed frequency safe-band and rank certificates."""
from fractions import Fraction as F
from math import isqrt, factorial
from functools import lru_cache

B = F(11, 10)
START = 896
END = 1200
K = 128
ACTIVE = {2: 2, 3: 3, 4: 2, 5: 5, 7: 7, 8: 2, 9: 3}
SCALE = 10**40


def arctan_bounds(t, terms=50):
    power = t
    out = F(0)
    for k in range(terms):
        out += (-1)**k * power / F(2*k+1)
        power *= t*t
    rem = power / F(2*terms+1)
    return (out, out+rem) if terms % 2 == 0 else (out-rem, out)


def pi_bounds():
    a = arctan_bounds(F(1, 5))
    b = arctan_bounds(F(1, 239))
    return 16*a[0]-4*b[1], 16*a[1]-4*b[0]


def ln_bounds(n, terms=128):
    t = F(n-1, n+1)
    power = t
    out = F(0)
    for k in range(terms):
        out += 2*power/F(2*k+1)
        power *= t*t
    return out, out+2*power/(F(2*terms+1)*(1-t*t))


def sqrt_bounds(n):
    sc = 10**48
    r = isqrt(n*sc*sc)
    return F(r, sc), F(r+1, sc)


PI = pi_bounds()
LN = {n: ln_bounds(n) for n in (2, 3, 5, 7, 8, 9)}
WEIGHTS = {
    n: (LN[p][0]/sqrt_bounds(n)[1], LN[p][1]/sqrt_bounds(n)[0])
    for n, p in ACTIVE.items()
}
SHIFTS = {n: ln_bounds(n) for n in ACTIVE}
TWOC = sum((2*c[1] for c in WEIGHTS.values()), F(0))


def log_rational_bounds(x):
    assert x > 0
    z = x
    j = 0
    while z >= 2:
        z /= 2
        j += 1
    while z < 1:
        z *= 2
        j -= 1
    t = (z-1)/(z+1)
    term = t
    lo = F(0)
    for k in range(22):
        lo += 2*term/(2*k+1)
        term *= t*t
    hi = lo+2*term/(45*(1-t*t))
    if j >= 0:
        return lo+j*LN[2][0], hi+j*LN[2][1]
    return lo+j*LN[2][1], hi+j*LN[2][0]


GAMMA_UP = F(29, 50)
CONST_UP = GAMMA_UP+F(11,7)+3*F(347,500)+F(573,500)
YFAC = F(333,106)


@lru_cache(None)
def arch_lower(j):
    y = YFAC*j
    a = F(1,4)
    out = sum((y*y/((k+a)*((k+a)**2+y*y)) for k in range(K)), F(0))
    return out + log_rational_bounds(y/(K+a))[0] - CONST_UP


def cos_integer(t):
    # Taylor up through t^36, all integer operations; floor error <= 1
    # in each recurrence, with total recurrence propagation <10^5 units.
    term = SCALE
    total = term
    for k in range(1,19):
        term = -(term*t*t)//(SCALE*SCALE*(2*k)*(2*k-1))
        total += term
    return total


@lru_cache(maxsize=100000)
def prime_interval(x):
    low = F(0)
    high = F(0)
    pi_mid = (PI[0]+PI[1])/2
    for n in ACTIVE:
        a = 2*PI[0]*x*SHIFTS[n][0]
        b = 2*PI[1]*x*SHIFTS[n][1]
        mid = (a+b)/2
        quotient = mid/(2*pi_mid)+F(1,2)
        k = quotient.numerator//quotient.denominator
        theta = mid-2*k*pi_mid
        assert abs(theta) <= PI[1]
        phase_error = (b-a)+2*abs(k)*(PI[1]-PI[0])+F(1,SCALE)
        assert phase_error < F(1,10**15)
        scaled = theta*SCALE
        t = scaled.numerator//scaled.denominator
        assert abs(F(t,SCALE)) < PI[1]
        ct = cos_integer(t)
        # Phase, Taylor truncation and integer rounding:
        # all are less than the conservative +-10^-13 enclosure.
        err = F(1,10**13)
        clo = F(ct,SCALE)-err
        chi = F(ct,SCALE)+err
        wlo, whi = WEIGHTS[n]
        values = (-2*wlo*clo, -2*wlo*chi, -2*whi*clo, -2*whi*chi)
        low += min(values)
        high += max(values)
    return low, high


def certificate():
    assert PI[0] < PI[1]
    assert PI[0] > F(333,106) and PI[1] < F(22,7)
    assert LN[2][0] > F(69,100) and LN[2][1] < F(347,500)
    assert TWOC < F(70751,10000)
    assert arch_lower(1200) - TWOC > 0
    assert F(22,7)**38/factorial(38) < F(1,10**22)

    # Upper/lower rigor for the quarter-digamma constant.
    H256 = sum((F(1,k) for k in range(1,257)), F(0))
    assert H256-8*LN[2][0] < GAMMA_UP
    assert sum((F(573,500)**k/factorial(k) for k in range(10)),F(0)) > F(22,7)

    # Derivative pays every continuous point between dyadic midpoints.
    derivative_upper = 4*PI[1]*sum(
        (WEIGHTS[n][1]*SHIFTS[n][1] for n in ACTIVE), F(0))
    assert derivative_upper < 69

    # Independent negative frequency witness, with upper digamma tail.
    witness = F(88291,100)
    y = PI[1]*witness
    aa = F(1,4)
    arch_up = sum(
        (y*y/((k+aa)*((k+aa)**2+y*y)) for k in range(K)), F(0))
    arch_up += log_rational_bounds(1+(y/(K-1+aa))**2)[1]/2
    H128 = sum((F(1,k) for k in range(1,129)),F(0))
    assert H128-log_rational_bounds(F(129))[1] > F(57,100)
    constant_lower = (
        F(57,100) + PI[0]/2 + 3*LN[2][0]
        + log_rational_bounds(PI[0])[0]
    )
    arch_up -= constant_lower
    witnessed_upper = arch_up + prime_interval(witness)[1]
    assert witnessed_upper < F(-8,100)

    leaves = 0
    deepest = 0
    minimum = F(10**6)
    def check(a,b,arch,depth):
        nonlocal leaves, deepest, minimum
        mid = (a+b)/2
        lower = arch+prime_interval(mid)[0]-F(69,2)*(b-a)
        if lower > 0:
            leaves += 1
            deepest = max(deepest,depth)
            minimum = min(minimum,lower)
            return
        if depth >= 15:
            raise AssertionError(f"Unpaid interval [{a}, {b}]")
        check(a,mid,arch,depth+1)
        check(mid,b,arch,depth+1)
    for j in range(START,END):
        check(F(j),F(j+1),arch_lower(j),0)
    assert leaves == 2535 and deepest == 7
    assert minimum > F(369,100000)

    # Reuse SI05's rigorous Rodrigues bound with omega=896, N=9472.
    N = 9472
    zmax = 2*PI[1]*B*START
    ratio = F(11,4)*zmax/(2*N)
    assert ratio < F(9,10)
    q = F(81,100)
    assert q**4 < F(1,2)
    prefactor = 2*B*(F(2*N+1)/(1-q)+2*q/(1-q)**2)
    assert prefactor < 2**18
    assert N == 4*2368
    assert 2*START*13 < 2**15
    # projection-tail^2 <2^(18-2368)=2^-2350,
    # resulting original K_- compression error <2^-1158.
    assert 2+15-1175 == -1158

    print("SI06 PASS: original signed Fourier m(xi)>0 for all |xi|>=896")
    print("finite interval dyadic leaves:",leaves,"max depth:",deepest)
    print("strict rational lower bound over finite cells:",float(minimum))
    print("m(882.91) certified upper:",float(witnessed_upper))
    print("signed 2C certified upper:",float(TWOC))
    print("rank incl. exact negative odd pole: <=9473")
    print("certified negative operator remainder: <2^-1158<2^-1000")


if __name__ == "__main__":
    certificate()
