#!/usr/bin/env python3
"""Exact rational replay of the NF617 retained pole Gram pilot.

No floating point or Arb. Matches the NF591 rectangular multiplication
and directed-rounding recurrence. Lean checker acceptance is separate.
"""
from fractions import Fraction as F
from math import floor, ceil, factorial

Q = 10**40
N = 48
zero = (F(0), F(0))
one = (F(1), F(0))

def add(a, b):
    return a[0]+b[0], a[1]+b[1]

def neg(a):
    return -a[0], a[1]

def rnd(a):
    return F(floor(a[0]*Q), Q), F(ceil(a[1]*Q)+1, Q)

def exact(q):
    return (q, F(0)) if (q*Q).denominator == 1 else rnd((q, F(0)))

def mul(a, b):
    m, r = a
    n, s = b
    return rnd((m*n, abs(m)*s+abs(n)*r+r*s))

def div(a, d):
    return rnd((a[0]/d, a[1]/d))

def zadd(a, b):
    return add(a[0], b[0]), add(a[1], b[1])

def zmul(a, b):
    return (add(mul(a[0], b[0]), neg(mul(a[1], b[1]))),
            add(mul(a[0], b[1]), mul(a[1], b[0])))

def small(h):
    z = (exact(h), zero)
    s = (zero, zero)
    t = (one, zero)
    for n in range(N):
        s = zadd(s, t)
        u = zmul(t, z)
        t = (div(u[0], n+1), div(u[1], n+1))
    return tuple((m, r+F(1, Q)) for m, r in s)

def main():
    p = small(F(11, 20))
    m = small(F(-11, 20))
    h = add(div(add(zmul(p, p)[0], neg(zmul(m, m)[0])), 2),
            exact(F(-11, 10)))
    mid = F(2356474701241767793847805235787, 10**31)
    rad = F(1, 10**30)
    assert 2*Q <= factorial(N)
    assert h == (F(2356474701241767793847805235786784358332, Q), F(231, Q))
    assert abs(h[0]-mid)+h[1] <= rad
    print("NF617 exact rational replay PASS")
    print("center integer:", h[0]*Q, "radius integer:", h[1]*Q)
    print("target:", mid, rad)

if __name__ == "__main__":
    main()
