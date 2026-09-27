#!/usr/bin/env python3
"""
GERM-62 certificate helper for the first-return-free parity chamber.

Scope:
    0 < e <= kappa = log[(16/15)(80/81)^5].

The chamber proof in notes/_recurrence62.md reduces every generic L2 orbit
to one 124 x 124 constant coefficient template, up to coordinate relabeling.
This script builds that template at one generic representative and performs
an outward interval LU determinant audit for both parity signs.

Certified input intervals reuse the rational logarithmic enclosures from the
earlier scattering audits:
    1.5849625 < log(3)/log(2) < 1.5849626
    2.3219280 < log(5)/log(2) < 2.3219281

Only the coefficient audit is numerical/interval. Geometry is handled in the
companion note.
"""

import math
import numpy as np
import mpmath as mp

iv = mp.iv

# Geometry.
r = math.log(3/2)
q = math.log(4/3)
s = math.log(5/4)
R = math.log(5/3)
j = math.log(9/8)
k = math.log(16/15)
h = math.log(81/80)
kappa = k - 5*h

# Point coefficients, for topology construction only.
beta = (math.log(3)/math.sqrt(3))/(math.log(2)/math.sqrt(2))
gamma = 1/math.sqrt(2)
delta = (math.log(5)/math.sqrt(5))/(math.log(2)/math.sqrt(2))

# Certified coefficient intervals.
r3 = iv.mpf([1.5849625, 1.5849626])
r5 = iv.mpf([2.3219280, 2.3219281])
beta_iv = r3 * iv.sqrt(2) / iv.sqrt(3)
c_iv = r3 / iv.sqrt(3)       # beta*gamma
d0_iv = r5 / iv.sqrt(5)      # delta*gamma


def params(e):
    u = k + e
    w = R + u
    v = q - j + e
    return u, w, v


def equation(t, e, parity, tol=1e-11):
    u, w, v = params(e)
    if t <= tol or t >= w-tol:
        return []
    if t < u-tol:
        return [(t, 1.0),
                (r+t, beta),
                (s+t, delta*gamma),
                (u-t, -parity*delta*gamma)]
    if t > u+tol and t < v-tol:
        return [(t, 1.0), (r+t, beta)]
    if t > v+tol and t < q-tol:
        return [(t, 1.0)]
    if t > q+tol and t < w-tol:
        return [(t, 1.0),
                (t-q, beta*gamma),
                (w-t, -parity*beta*gamma)]
    return []


def orbit_matrix(e, seed, parity, max_nodes=1000):
    def key(x):
        return round(x, 13)

    nodes = {}
    queue = [seed]
    rows = []
    seen = set()

    while queue and len(nodes) < max_nodes:
        t = queue.pop()
        kt = key(t)
        if kt in seen:
            continue
        seen.add(kt)
        nodes[kt] = t
        row = equation(t, e, parity)
        if row:
            rows.append(row)
            for x, _ in row:
                if 0 < x < params(e)[1]:
                    kx = key(x)
                    nodes.setdefault(kx, x)
                    if kx not in seen:
                        queue.append(x)

    keys = sorted(nodes)
    index = {k_: i for i, k_ in enumerate(keys)}
    A = np.zeros((len(rows), len(keys)))

    for i, row in enumerate(rows):
        for x, coeff in row:
            A[i, index[key(x)]] += coeff

    return A


def interval_coeff(value):
    if abs(value-1.0) < 1e-10:
        return iv.mpf(1)
    if abs(value-beta) < 1e-8:
        return beta_iv
    if abs(value+beta) < 1e-8:
        return -beta_iv
    c = beta*gamma
    d0 = delta*gamma
    if abs(value-c) < 1e-8:
        return c_iv
    if abs(value+c) < 1e-8:
        return -c_iv
    if abs(value-d0) < 1e-8:
        return d0_iv
    if abs(value+d0) < 1e-8:
        return -d0_iv
    raise ValueError(f"unrecognized coefficient {value}")


def bounds(x):
    return float(x.a), float(x.b)


def interval_det(A):
    n = A.shape[0]
    if A.shape[1] != n:
        raise ValueError("matrix is not square")

    M = [[iv.mpf(0) for _ in range(n)] for _ in range(n)]
    B = A.astype(float).copy()

    for i in range(n):
        for j_ in np.nonzero(A[i])[0]:
            M[i][j_] = interval_coeff(A[i, j_])

    sign = 1
    det = iv.mpf(1)

    for k_ in range(n):
        p = k_ + int(np.argmax(np.abs(B[k_:, k_])))
        if abs(B[p, k_]) < 1e-14:
            raise RuntimeError(f"numeric zero pivot at {k_}")
        if p != k_:
            B[[k_, p], :] = B[[p, k_], :]
            M[k_], M[p] = M[p], M[k_]
            sign *= -1

        pivot = M[k_][k_]
        lo, hi = bounds(pivot)
        if lo <= 0 <= hi:
            raise RuntimeError(f"interval pivot crosses zero at {k_}: {lo}, {hi}")

        det *= pivot

        for i in range(k_+1, n):
            mlo, mhi = bounds(M[i][k_])
            if abs(B[i, k_]) < 1e-18 and mlo == 0.0 and mhi == 0.0:
                continue

            fac_num = B[i, k_] / B[k_, k_]
            fac_iv = M[i][k_] / pivot
            B[i, k_] = 0.0
            M[i][k_] = iv.mpf(0)

            for j_ in range(k_+1, n):
                plo, phi = bounds(M[k_][j_])
                if B[k_, j_] != 0.0 or plo != 0.0 or phi != 0.0:
                    B[i, j_] -= fac_num * B[k_, j_]
                    M[i][j_] -= fac_iv * M[k_][j_]

    if sign < 0:
        det = -det
    return bounds(det)


def main():
    # Generic representative inside 0<e<kappa.
    e = 0.001
    seed = 0.000137

    for parity in (+1, -1):
        A = orbit_matrix(e, seed, parity)
        assert A.shape == (124, 124), A.shape
        lo, hi = interval_det(A)
        print(f"parity={parity:+d}: det in [{lo:.12f}, {hi:.12f}]")
        assert lo > 139.51
        assert hi < 139.54

    print("certificate: both parity templates exclude zero determinant")


if __name__ == "__main__":
    main()
