"""Exact finite pole-resonance controls; no actual spectral values computed."""
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


def quadratic(a, v):
    return sum((v[i]*a[i][j]*v[j] for i in range(len(v)) for j in range(len(v))), F(0))


def main():
    count = 0
    for gamma in (F(1), F(2), F(3, 2)):
        for b in (F(0), F(1), F(2, 3)):
            for B in (F(1), F(3), F(5, 2)):
                p = b*b/B
                for margin in (-F(1, 4), F(0), F(1, 3), F(2)):
                    d = gamma*gamma/(p+F(1, 2)+margin)
                    E = -gamma*gamma/d+p
                    sigma = -d+2*gamma*gamma/(1+2*p)
                    assert (sigma >= 0) == (E <= -F(1, 2))
                    assert (sigma == 0) == (E == -F(1, 2))
                    # Determinant after positive rank-one restoration.
                    det = (-d+2*gamma*gamma)*(B+2*b*b)-(2*gamma*b)**2
                    assert det == (B+2*b*b)*sigma
                    count += 3
                for delta in (F(0), F(1), F(2, 3)):
                    d = F(3)
                    det = (-d+2*gamma*gamma)*(2*delta*delta)-(2*gamma*delta)**2
                    assert det == -2*d*delta*delta
                    assert (det >= 0) == (delta == 0)
                    count += 2
    for s in (F(1), F(3, 4), F(2)):
        for O in (F(1, 4), F(1, 2), F(3, 4)):
            B = s*s/O
            assert (B-2*s*s >= 0) == (O <= F(1, 2))
            assert (B-2*s*s == 0) == (O == F(1, 2))
            count += 2
    c = [F(5, 4), F(5, 4)]
    s = [-F(3, 4), F(3, 4)]
    P = [[2*c[i]*c[j]-2*s[i]*s[j] for j in range(2)] for i in range(2)]
    H = [[-x for x in row] for row in P]
    assert P == [[F(2), F(17, 4)], [F(17, 4), F(2)]]
    assert quadratic(inverse(H), c) == -F(1, 2)
    assert quadratic(inverse(H), s) == F(1, 2)
    assert H[0][0]+H[0][1] == -F(25, 4)
    assert H[0][0]-H[0][1] == F(9, 4)
    rate = F(17, 4)
    mass = -F(25, 4)
    assert H == [[rate+mass, -rate], [-rate, rate+mass]]
    assert rate > 0
    count += 7
    for mu in (F(1, 10), F(1), F(10)):
        Hmu = [[H[i][j]+mu*F(i == j) for j in range(2)] for i in range(2)]
        A = [[Hmu[i][j]+P[i][j] for j in range(2)] for i in range(2)]
        assert A == [[mu, F(0)], [F(0), mu]]
        recovered = [[Hmu[i][j]-mu*F(i == j) for j in range(2)] for i in range(2)]
        assert recovered == H
        count += 2
    print(json.dumps({'passed_assertions': count,
                      'scope': 'finite singular-coupling/Schur algebra and two-point positive-jump control; not actual continuum nullity'}, indent=2))


if __name__ == '__main__':
    main()
