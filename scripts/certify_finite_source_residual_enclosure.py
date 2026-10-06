#!/usr/bin/env python3
"""Exact real rational comparison controls, not actual-zeta certificates."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json


def tr(a):
    return [list(v) for v in zip(*a)]


def mul(a, b):
    return [[sum((x*y for x, y in zip(row, col)), F(0))
             for col in zip(*b)] for row in a]


def add(a, b, factor=F(1)):
    return [[x+factor*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a, t):
    return [[t*x for x in row] for row in a]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def inv(a):
    n = len(a)
    v = [row[:] + e for row, e in zip(a, eye(n))]
    for j in range(n):
        p = next(i for i in range(j, n) if v[i][j])
        v[j], v[p] = v[p], v[j]
        v[j] = [x/v[j][j] for x in v[j]]
        for i in range(n):
            if i != j:
                t = v[i][j]
                v[i] = [x-t*y for x, y in zip(v[i], v[j])]
    return [row[n:] for row in v]


def psd(a):
    if a != tr(a):
        return False
    a = [row[:] for row in a]
    while a:
        if any(a[i][i] < 0 for i in range(len(a))):
            return False
        p = next((i for i in range(len(a)) if a[i][i] > 0), None)
        if p is None:
            return not any(x for row in a for x in row)
        keep = [i for i in range(len(a)) if i != p]
        a = [[a[i][j]-a[i][p]*a[p][j]/a[p][p]
              for j in keep] for i in keep]
    return True


def serial(a):
    return [[str(x) for x in row] for row in a]


def control(g, r, y, beta):
    assert psd(add(g, scale(eye(len(g)), beta), F(-1)))
    e = add(tr(r), mul(g, y), F(-1))
    ry = mul(r, y)
    v = add(add(ry, tr(ry)), mul(tr(y), mul(g, y)), F(-1))
    k = mul(tr(e), e)
    l = mul(r, mul(inv(g), tr(r)))
    gap = add(l, v, F(-1))
    exact_gap = mul(tr(e), mul(inv(g), e))
    assert gap == exact_gap
    assert psd(gap)
    assert psd(add(scale(k, 1/beta), gap, F(-1)))
    # Same trial vector: Q(Yu) = u*(I-V)u - ||RYu-u||^2.
    native_trial = add(mul(tr(y), mul(g, y)), mul(tr(ry), ry), F(-1))
    mismatch = add(ry, eye(len(r)), F(-1))
    rhs = add(add(eye(len(r)), v, F(-1)), mul(tr(mismatch), mismatch), F(-1))
    assert native_trial == rhs
    return {'beta': str(beta), 'G': serial(g), 'R': serial(r), 'Y': serial(y),
            'V': serial(v), 'K': serial(k), 'L': serial(l),
            'native_trial': serial(native_trial),
            'naive_RY_hermitian': ry == tr(ry)}


def main():
    cases = []
    for i in range(1, 7):
        for j in range(1, 5):
            beta = F(j, 7)
            b = [[F(1), F(i, 3), F(0)],
                 [F(0), F(1), F(j, 5)], [F(1, 2), F(0), F(1)]]
            g = add(mul(tr(b), b), scale(eye(3), beta))
            r = [[F(i, 4), F(1), F(-j, 3)],
                 [F(1), F(-i, 5), F(j, 2)]]
            y = [[F(j, 9), F(-i, 11)], [F(i, 13), F(1, 4)],
                 [F(-1, 3), F(j, 17)]]
            cases.append(control(g, r, y, beta))
    assert any(not c['naive_RY_hermitian'] for c in cases)
    # Exact Galerkin controls using one-dimensional physical trial spaces.
    galerkin = []
    g = [[F(2), F(1)], [F(1), F(2)]]
    r = [[F(1), F(2)], [F(3), F(-1)]]
    for j in range(1, 5):
        w = [[F(1)], [F(j, 3)]]
        y = mul(w, mul(inv(mul(tr(w), mul(g, w))), mul(tr(w), tr(r))))
        c = control(g, r, y, F(1))
        assert c['V'] == serial(mul(r, y))
        galerkin.append(c)
    k = [[F(1), F(1)], [F(1), F(1)]]
    assert not psd(add(eye(2), k, F(-1)))
    assert not psd(scale(k, F(-1)))
    # Omitting beta^(-1) fails for G=I/2, R=I, Y=0.
    assert not psd(add(eye(2), scale(eye(2), F(2)), F(-1)))
    data = {'base_commit': 'a8a2d86ddc7dfdb0e5f3bb4803ade15b75ae5e73',
            'scope': 'finite real rational comparison controls only; no actual zeta matrix evaluated',
            'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'general_controls': cases, 'galerkin_controls': galerkin,
            'negative_controls_rejected': ['drop cross correlations',
                 'reverse residual correction sign', 'omit inverse coercivity factor'],
            'analytic_universal_proof': 'see accompanying note; not mechanically or Lean verified'}
    target = Path(__file__).resolve().parents[1] / 'notes/data/RPB108_FINITE_SOURCE_RESIDUAL_CONTROLS_20261006.json'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'controls': len(cases)+len(galerkin),
                      'negative_controls_rejected': 3,
                      'sha256': hashlib.sha256(target.read_bytes()).hexdigest()}))


if __name__ == '__main__':
    main()
