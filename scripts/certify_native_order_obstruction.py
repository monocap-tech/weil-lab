"""Exact arithmetic checks for the smooth full-native cross-pair witness."""
from fractions import Fraction as F
import json


def log_interval(n, terms=120):
    z = F(n-1, n+1)
    lower = 2*sum((z**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    tail = 2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
    return lower, lower+tail


def main():
    l2, u2 = log_interval(2)
    l3, u3 = log_interval(3)
    checks = {
        'prime_2_below_separation': u2 < F(49, 50),
        'all_n_ge_3_above_separation': l3 > F(51, 50),
        'lower_pair_separation': F(49, 100)-F(-49, 100) == F(49, 50),
        'upper_pair_separation': F(51, 100)-F(-51, 100) == F(51, 50),
        'exp_lower_budget': 1+2*F(49, 50) == F(74, 25),
        'jump_upper_budget': 1/(1-F(25, 74)) == F(74, 49),
        'positive_cross_margin': 2-F(74, 49) == F(24, 49),
        'modulus_polarization_factor': 2-(-2) == 4,
    }
    assert all(checks.values()), checks
    print(json.dumps({'checks': checks, 'passed': len(checks),
                      'scope': 'rational witness arithmetic; analytic heat/resolvent/index proofs in note'}, indent=2))


if __name__ == '__main__':
    main()
