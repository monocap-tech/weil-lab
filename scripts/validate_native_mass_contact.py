#!/usr/bin/env python3
"""Exact algebra controls; no actual arithmetic eigenvalues are computed."""
from fractions import Fraction as F
import json

def main():
    cases = 0
    for mu in (F(1), F(2), F(3)):
        for nu in (F(1), F(2), F(3)):
            for r in (F(1), F(2), F(3)):
                for beta in (F(1, 4), F(1, 2), F(3, 4)):
                    # Actual-structure control matrix Q=[[mu,beta],[beta,mu+nu]].
                    # Endpoint compression is mu. Subtract mu times mass.
                    assert mu*(mu+nu)-beta*beta > 0
                    det = r*r*nu-beta*beta
                    assert det > 0  # G=[[r*r,beta],[beta,nu]] coercive.
                    x = -beta/nu
                    assert 2*beta*x+nu*x*x == -beta*beta/nu < 0
                    # Residual of unchanged endpoint h=(1,0) is (0,beta).
                    e = beta*beta*r*r/det
                    response = r*r*nu/det
                    assert r*r*(response-1) == e > 0
                    v1, v2 = -beta*beta/det, r*r*beta/det
                    assert r*r*v1+beta*v2 == 0
                    assert beta*v1+nu*v2 == beta
                    assert beta*v2 == e
                    trial1, trial2 = 1-v1, -v2
                    q_trial = 2*beta*trial1*trial2+nu*trial2*trial2
                    assert q_trial == -e-r*r*v1*v1 < 0
                    cases += 1
    print(json.dumps({'status': 'rational_controls_pass', 'cases': cases,
                      'scope': 'scalar-shift and residual algebra only; no actual zeta contact or Lean certification'},
                     sort_keys=True))

if __name__ == '__main__':
    main()
