#!/usr/bin/env python3
"""SI02 exact Fraction regressions. The all-degree proof is the SI02 note."""
from fractions import Fraction as F


def add(a, b, scale=F(1)):
    out = [F(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += scale * x
    return out


def shift_x(a):
    return [F(0)] + a


def derivative(a):
    return [i * a[i] for i in range(1, len(a))]


def inner(a, b):
    return sum(
        (F(2, i + j + 1) * x * y
         for i, x in enumerate(a) for j, y in enumerate(b)
         if (i + j) % 2 == 0),
        F(0),
    )


def legendre(top):
    p = [[F(1)], [F(0), F(1)]]
    for n in range(1, top):
        num = add([(2*n+1)*x for x in shift_x(p[n])], p[n-1], -F(n))
        p.append([x / F(n+1) for x in num])
    return p[:top+1]


def H(n):
    return sum((F(1, k) for k in range(1, n+1)), F(0))


def endpoint(n, d):
    return F(2*(2*d-1)*(2*n+1),
             (n-d)*(n+d+1)*(n-d+2)*(n+d-1))


def validate():
    B = F(11, 10)
    s = F(3, 2)  # Rational regression point, not Weil's claimed exact shift.
    p = legendre(19)
    for d in range(2, 19, 2):
        f = add(p[d], p[d-2], -F(1))
        df = derivative(f)
        assert sum(f) == 0
        assert sum(x * (-1)**i for i, x in enumerate(f)) == 0
        expected = [(2*d-1)*x for x in p[d-1]]
        assert add(df, expected, -F(1)) == [F(0)] * len(df)
        assert inner(df, df) == 2*(2*d-1)
        assert inner(f, f) == F(2, 2*d+1)+F(2, 2*d-3)
        for e in range(2, d, 2):
            earlier = add(p[e], p[e-2], -F(1))
            assert inner(df, derivative(earlier)) == 0
        n = d+2
        neighbor = F(1, 4) - F(2, 4*d*d+8*d+3)
        assert endpoint(n, d) == neighbor
        assert F(27, 140) <= neighbor < F(1, 4)
        for n in range(2*d, 3*d+9, 2):
            assert 0 < endpoint(n, d) <= F(48*d, n**3)

    c = [F(3, 2), -F(7, 3), F(2, 5), F(5, 6)]
    N = len(c)
    q = [F(0)]
    for k, ck in enumerate(c, 1):
        q = add(q, add(p[2*k], p[2*k-2], -F(1)), ck)
    gradient_left = inner(derivative(q), derivative(q)) / B
    gradient_right = sum(
        (F(2*(4*k-1), 1) / B * c[k-1]**2
         for k in range(1, N+1)), F(0))
    assert gradient_left == gradient_right

    def a(j):
        return (2*B / F(4*j+1)) * (H(2*j)+s)

    original_coords = [-c[0]] + [c[j-1]-c[j] for j in range(1, N)] + [c[-1]]
    direct_D = sum((a(j)*v*v for j, v in enumerate(original_coords)), F(0))
    pad = [F(0)] + c + [F(0)]
    difference_D = sum(
        (a(j)*(pad[j]-pad[j+1])**2 for j in range(N+1)), F(0))
    assert 0 < direct_D == difference_D
    print("SI02 PASS: exact Legendre derivative, endpoint, D-Gram, near/far checks")
    print("D norm squared:", direct_D)
    print("H1 derivative norm squared:", gradient_left)


if __name__ == "__main__":
    validate()
