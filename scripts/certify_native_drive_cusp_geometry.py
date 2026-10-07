#!/usr/bin/env python3
"""Exact support/exponent checks for the analytic actual-drive cusp control.

No numerical h, eigenvector, actual-null certificate or Lean proof is produced.
"""
from fractions import Fraction as F
import json


def log_interval(n, terms=120):
    z = F(n-1, n+1)
    value = 2*sum((z**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    tail = 2*z**(2*terms+1)/F(2*terms+1)/(1-z*z)
    return value, value+tail


def disjoint(x, y):
    return x[1] < y[0] or y[1] < x[0]


def check():
    a, eps, delta = F(97,100), F(1,1000), F(1,10000)
    logs = {n: log_interval(n) for n in [2,3,4,5,7]}
    assert all(logs[n][1] < 2*a for n in [2,3,4,5])
    assert logs[7][0] > 2*a
    right = {n: (a-hi, a-lo) for n,(lo,hi) in logs.items() if n != 7}
    left = {n: (-a+lo, -a+hi) for n,(lo,hi) in logs.items() if n != 7}
    supports = {
        'endpoint_cusp': (a-delta, a),
        'interior_cusp': (right[2][0], right[2][1]+delta),
        'right_bump': (a-2*eps, a-eps),
        'left_bump': (-a+eps, -a+2*eps),
    }
    comparisons = 0
    for label,point_set in [('right',right),('left',left)]:
        for n,(lo,hi) in point_set.items():
            collar = lo-delta, hi+delta
            for name,support in supports.items():
                if label == 'right' and n == 2 and name == 'interior_cusp':
                    # x0+u and x0-v are treated with their exact correlated center.
                    continue
                assert disjoint(collar,support), (label,n,name)
                comparisons += 1
    assert disjoint(supports['endpoint_cusp'], supports['right_bump'])
    assert disjoint(supports['interior_cusp'], supports['endpoint_cusp'])
    diagonal_lower = 2*(1/(8*eps)-4)
    off_diagonal_upper = F(12)
    assert diagonal_lower == 242
    assert diagonal_lower-off_diagonal_upper == 230
    assert 1 < 2*a-2*eps < 2*a-eps < 2
    alpha = F(1,4)
    assert 2*alpha-1 == F(-1,2)  # critical collar integral, logarithms integrable
    assert 2*alpha-F(3,2) == -1  # supercritical flux logarithm diverges
    assert 2*alpha-2 == F(-3,2)  # physical derivative square diverges
    # A deliberately incorrect prime-2 exterior omission is rejected by support.
    assert not disjoint((right[2][0],right[2][1]+delta/2),supports['interior_cusp'])
    return {
        'scope': 'rational support/matrix/exponent checks only; analytic theorem not certified',
        'aperture_reused': '97/100',
        'active_prime_powers': [2,3,4,5],
        'support_interval_checks': comparisons,
        'correlated_prime2_inside_outside': 'exact x0-v versus x0+u',
        'compatibility_matrix_eigenvalue_lower_strict': '230',
        'derivative_L2': False,
        'actual_null_claimed': False,
        'new_aperture_certificate': False,
        'lean_certified': False,
        'omitted_prime2_control_rejected': True,
    }


if __name__ == '__main__':
    print(json.dumps(check(), indent=2, sort_keys=True))
