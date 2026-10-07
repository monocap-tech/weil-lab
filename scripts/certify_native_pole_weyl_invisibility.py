"""Exact weighted isoweyl controls; not a continuum or zeta null model."""
from fractions import Fraction as F
import json


def inverse(a):
    n = len(a)
    m = [row[:] + [F(i == j) for j in range(n)] for i, row in enumerate(a)]
    for j in range(n):
        k = next(i for i in range(j, n) if m[i][j])
        m[j], m[k] = m[k], m[j]
        t = m[j][j]
        m[j] = [x/t for x in m[j]]
        for i in range(n):
            if i != j:
                t = m[i][j]
                m[i] = [x-t*y for x, y in zip(m[i], m[j])]
    return [row[n:] for row in m]


def rank(a):
    m = [row[:] for row in a]
    k = 0
    for j in range(len(m[0])):
        p = next((i for i in range(k, len(m)) if m[i][j]), None)
        if p is None:
            continue
        m[k], m[p] = m[p], m[k]
        t = m[k][j]
        m[k] = [x/t for x in m[k]]
        for i in range(len(m)):
            if i != k:
                t = m[i][j]
                m[i] = [x-t*y for x, y in zip(m[i], m[k])]
        k += 1
    return k


def apply(a, v):
    return [sum((x*y for x, y in zip(row, v)), F(0)) for row in a]


def inner(w, u, v):
    return sum((p*x*y for p, x, y in zip(w, u, v)), F(0))


def main():
    models = [([F(1, 2), F(2)], [F(1), F(1)]),
              ([F(2, 3), F(3, 2), F(1, 3), F(3)],
               [F(25, 33), F(25, 33), F(8, 33), F(8, 33)])]
    count = 0
    outputs = []
    for t, w in models:
        n = len(t)
        c = [(p+1/p)/2 for p in t]
        s = [(p-1/p)/2 for p in t]
        P = [[2*(c[i]*c[j]-s[i]*s[j])*w[j] for j in range(n)] for i in range(n)]
        H = [[-p for p in row] for row in P]
        assert sum(w) == 2
        assert inner(w, c, c) == F(25, 8)
        assert inner(w, s, s) == F(9, 8)
        assert inner(w, c, s) == 0
        assert rank(H) == 2
        assert apply(H, c) == [-F(25, 4)*p for p in c]
        assert apply(H, s) == [F(9, 4)*p for p in s]
        count += 7
        for i in range(n):
            for j in range(n):
                assert P[i][j] == (t[i]/t[j]+t[j]/t[i])*w[j]
                assert w[i]*H[i][j] == w[j]*H[j][i]
                assert -H[i][j] > 0
                count += 3
        for z in (F(-10), F(-5), F(-1), -F(1, 10), F(1, 10), F(1), F(2), F(3), F(10)):
            R = inverse([[H[i][j]-z*F(i == j) for j in range(n)] for i in range(n)])
            assert inner(w, c, apply(R, c)) == F(25, 8)/(-F(25, 4)-z)
            assert inner(w, s, apply(R, s)) == F(9, 8)/(F(9, 4)-z)
            assert inner(w, c, apply(R, s)) == 0
            assert inner(w, s, apply(R, c)) == 0
            count += 4
        if n == 4:
            for v in ([F(160), F(160), -F(325), -F(325)],
                      [-F(128), F(128), F(125), -F(125)]):
                assert inner(w, c, v) == 0
                assert inner(w, s, v) == 0
                assert apply(H, v) == [F(0)]*n
                count += 3
        for mu in (F(1, 10), F(1), F(10)):
            Hmu = [[H[i][j]+mu*F(i == j) for j in range(n)] for i in range(n)]
            A = [[Hmu[i][j]+P[i][j] for j in range(n)] for i in range(n)]
            assert A == [[mu*F(i == j) for j in range(n)] for i in range(n)]
            count += 1
        outputs.append({'dimension': n, 'base_nullity': n-2, 'native_comparison_nullity': n})
    print(json.dumps({'passed_assertions': count, 'models': outputs,
                      'scope': 'exact isoweyl positive-jump controls; no actual continuum/source-range proof'}, indent=2))


if __name__ == '__main__':
    main()
