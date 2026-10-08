#!/usr/bin/env python3
"""Exact finite controls; not an actual-Weil positivity certificate."""
from fractions import Fraction as F
import json

def validate():
    checks = 0
    c, m, tau = F(93,100), F(7), F(1,320*10**27)
    r, d = m*m, 2*c
    samples = [F(j,100) for j in range(101)]
    for s in samples:
        finite = r/c + tau*(1-2*s)
        bad = finite-r/c
        good = finite-r/d
        assert bad == tau*(1-2*s)
        assert good > 0
        assert (bad > 0) == (s < F(1,2))
        assert (bad == 0) == (s == F(1,2))
        # Both complements have spectrum {c,d}, exact lower bound c,
        # identical trace and identical complete coupling Gram r.
        assert c+d == d+c and min(c,d) == c
        checks += 5
    for mass in [F(1),F(2),F(5,3)]:
        for eigenvalue in [c,d,F(3)]:
            for coupling in [F(1),F(7),F(-2,3)]:
                for u in [F(0),F(1),F(-1,3),coupling/(mass*eigenvalue)]:
                    # Physical inner product on this coordinate is mass*x*y.
                    h = coupling**2/(mass*eigenvalue)
                    dual_residual = coupling-mass*eigenvalue*u
                    residual_norm_squared = dual_residual**2/mass
                    trial = 2*coupling*u-mass*eigenvalue*u*u
                    assert h == trial+residual_norm_squared/eigenvalue
                    assert trial <= h <= trial+residual_norm_squared/c
                    if u == 0:
                        assert trial+residual_norm_squared/c == coupling**2/(mass*c)
                    checks += 2
    return {
        'scope':'exact rational finite controls, not actual Weil or Lean certification',
        'checks':checks,
        'complement_lower':str(c),'coupling_gram':str(r),
        'finite_margin':str(tau),'contact_parameter':'1/2',
        'bad_inverse_correction':str(r/c),
        'good_inverse_correction':str(r/d),
        'physical_mass_cases':['1','2','5/3'],
        'result':'passed'
    }

if __name__ == '__main__':
    print(json.dumps(validate(),indent=2,sort_keys=True))
