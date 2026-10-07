"""Finite exact algebra of the actual pole moments on a derivative chain.

No actual null vector, spectral computation or analytic certification is supplied.
"""
from fractions import Fraction as F
import json


def rank(matrix, columns):
    a = [row[:] for row in matrix]
    k = 0
    for col in range(columns):
        pivot = next((i for i in range(k, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        t = a[k][col]
        a[k] = [x/t for x in a[k]]
        for i in range(len(a)):
            if i != k:
                t = a[i][col]
                a[i] = [x-t*y for x, y in zip(a[i], a[k])]
        k += 1
    return k


def main():
    count = 0
    cases = []
    for r in range(1, 17):
        for parity in (0, 1):
            for active in (False, True):
                moments = [[F(0) for _ in range(r)] for _ in range(2)]
                for j in range(r):
                    moments[(parity+j) % 2][j] = (-F(1, 2))**j if active else F(0)
                for j in range(1, r):
                    assert moments[0][j] == -moments[1][j-1]/2
                    assert moments[1][j] == -moments[0][j-1]/2
                    count += 2
                mr = rank(moments, r)
                assert mr == (min(2, r) if active else 0)
                count += 1
                n = max(r-2, 0)
                stripping = [[F(0) for _ in range(n)] for _ in range(r)]
                for j in range(n):
                    stripping[j][j] = -F(1, 4)
                    stripping[j+2][j] = F(1)
                assert rank(stripping, n) == n
                count += 1
                for row in moments:
                    for j in range(n):
                        assert sum((row[i]*stripping[i][j] for i in range(r)), F(0)) == 0
                        count += 1
                if active and r >= 3:
                    assert r-mr == n
                    count += 1
                if r >= 3:
                    assert stripping[-1][-1] == 1
                    assert all(stripping[-1][j] == 0 for j in range(n-1))
                    count += 2
                cases.append({'r': r, 'parity': parity, 'active': active,
                              'moment_rank': mr, 'Z_dimension': r-mr,
                              'stripping_image_dimension': n})
    print(json.dumps({'passed_assertions': count, 'cases': len(cases),
                      'scope': 'exact chain algebra; no actual spectrum or source-range assertion'}, indent=2))


if __name__ == '__main__':
    main()
