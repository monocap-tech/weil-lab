#!/usr/bin/env python3
"""
GERM-63 certificate helper for the single-scale multikappa parity chamber.

Scope:
    kappa < e <= lambda_ret = h-kappa.

Geometry is proved in notes/_recurrence63.md.  In this chamber the lower
defect has only the kappa-return, so generic orbit templates are exactly

    124, 186, 248, 310, 372.

This script instantiates one generic representative of each topology and
performs an outward interval LU determinant audit for both parity signs.

Certified coefficient inputs:
    1.5849625 < log(3)/log(2) < 1.5849626
    2.3219280 < log(5)/log(2) < 2.3219281
"""

import math
import numpy as np
import mpmath as mp

iv = mp.iv

# Geometry
r = math.log(3/2)
q = math.log(4/3)
s = math.log(5/4)
R = math.log(5/3)
j = math.log(9/8)
k = math.log(16/15)
h = math.log(81/80)
kappa = k - 5*h
lambda_ret = h - kappa

# Midpoint coefficients, only for topology and pivot ordering.
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
        return [
            (t, 1.0),
            (r+t, beta),
            (s+t, delta*gamma),
            (u-t, -parity*delta*gamma),
        ]
    if t > u+tol and t < v-tol:
        return [(t, 1.0), (r+t, beta)]
    if t > v+tol and t < q-tol:
        return [(t, 1.0)]
    if t > q+tol and t < w-tol:
        return [
            (t, 1.0),
            (t-q, beta*gamma),
            (w-t, -parity*beta*gamma),
        ]
    return []


def orbit_matrix(e, seed, parity, max_nodes=2000):
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
    if abs(value+1.0) < 1e-10:
        return -iv.mpf(1)

    c = beta*gamma
    d0 = delta*gamma

    if abs(value-beta) < 1e-8:
        return beta_iv
    if abs(value+beta) < 1e-8:
        return -beta_iv
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


def interval_det_sparse(A):
    n = A.shape[0]
    if A.shape[1] != n:
        raise ValueError("matrix is not square")

    rows = [{} for _ in range(n)]
    B = A.astype(float).copy()

    for i in range(n):
        for j0 in np.nonzero(A[i])[0]:
            rows[i][int(j0)] = interval_coeff(A[i, j0])

    sign = 1
    det = iv.mpf(1)

    for kk in range(n):
        p = kk + int(np.argmax(np.abs(B[kk:, kk])))
        if abs(B[p, kk]) < 1e-14:
            raise RuntimeError(f"numeric zero pivot at {kk}")

        if p != kk:
            B[[kk, p], :] = B[[p, kk], :]
            rows[kk], rows[p] = rows[p], rows[kk]
            sign *= -1

        pivot = rows[kk].get(kk, iv.mpf(0))
        lo, hi = bounds(pivot)
        if lo <= 0 <= hi:
            raise RuntimeError(
                f"interval pivot crosses zero at {kk}: [{lo}, {hi}]"
            )

        det *= pivot
        pivot_keys = [j0 for j0 in rows[kk] if j0 > kk]

        for i in range(kk+1, n):
            if kk not in rows[i]:
                continue

            fac_iv = rows[i][kk] / pivot
            fac_num = B[i, kk] / B[kk, kk]
            rows[i].pop(kk, None)
            B[i, kk] = 0.0

            for j0 in pivot_keys:
                rows[i][j0] = (
                    rows[i].get(j0, iv.mpf(0))
                    - fac_iv * rows[kk][j0]
                )
                B[i, j0] -= fac_num * B[kk, j0]

    if sign < 0:
        det = -det
    return bounds(det)


# One generic representative of every topology.
# (e/kappa, seed/kappa, expected dimension)
REPRESENTATIVES = [
    (1.20, 0.23, 124),
    (1.20, 0.07, 186),
    (2.20, 0.07, 248),
    (3.20, 0.07, 310),
    (4.10, 0.07, 372),
]

EXPECTED = {
    124: (139.5135, 139.5383),
    186: (-1620.66, -1620.24),
    248: (-18822.97, -18816.68),
    310: (218526.2, 218619.1),
    372: (2537815.2, 2539170.0),
}


def main():
    assert 4*kappa < lambda_ret < 5*kappa

    for parity in (+1, -1):
        print(f"parity={parity:+d}")
        for emult, smult, dim in REPRESENTATIVES:
            e = emult*kappa
            seed = smult*kappa
            assert kappa < e < lambda_ret

            A = orbit_matrix(e, seed, parity)
            assert A.shape == (dim, dim), (emult, smult, A.shape)

            lo, hi = interval_det_sparse(A)
            elo, ehi = EXPECTED[dim]
            assert lo > elo and hi < ehi
            assert not (lo <= 0 <= hi)

            print(
                f"  dim={dim:3d}: det in "
                f"[{lo:.12f}, {hi:.12f}]"
            )

    print("certificate: all five multikappa templates exclude zero")


if __name__ == "__main__":
    main()
