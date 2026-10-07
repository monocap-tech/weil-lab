#!/usr/bin/env python3
"""Rational algebra controls only; not an actual-zeta or analytic certification."""
from fractions import Fraction as F
import json

def main():
    scalar = collar = rates = 0
    for a in (F(1, 4), F(1, 2), F(1), F(2), F(3)):
        for b in (F(0), F(1, 3), F(1), F(3)):
            for s in (F(1, 2), F(1, 4), F(1, 8)):
                e, d = a*a*s*s, b*b*s*s
                bound = (2*a*a+a*b)*s*s
                for j in range(101):
                    q = F(j, 10)*s*s
                    if q*q <= e*(2*q+d):
                        assert q <= bound
                        scalar += 1
                # The quadratic's positive root cannot exceed bound.
                assert bound*bound >= e*(2*bound+d)
    for p in range(1, 13):
        for s in (F(1, 2), F(1, 4), F(1, 8)):
            lhs = s**(2*p+1)/F(2*p+1)
            rhs = s*s/F(2)*p*p*s**(2*p-1)/F(2*p-1)
            assert lhs <= rhs
            collar += 1
    table = []
    for n in (2, 4, 8, 16, 32):
        s = F(1, n*n)
        rough, smooth = s, s**3
        assert rough/(s*s) == n*n
        assert smooth/(s*s) == s
        table.append({'n': n, 'linear_over_s2': str(rough/(s*s)),
                      'cubic_over_s2': str(smooth/(s*s))})
        rates += 1
    print(json.dumps({'status': 'rational_controls_pass',
                      'scope': 'scalar and collar controls; no analytic or Lean certification',
                      'scalar_premise_cases': scalar, 'collar_cases': collar,
                      'rate_cases': rates, 'rate_table': table}, sort_keys=True))

if __name__ == '__main__':
    main()
