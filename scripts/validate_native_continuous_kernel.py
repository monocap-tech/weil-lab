"""Exact finite identity and synthetic relative-error controls, not a zeta certificate."""
from fractions import Fraction as F
import json


def integrate(coeffs, lo, hi):
    return sum((c * (hi**(j+1)-lo**(j+1))/F(j+1)
                for j, c in enumerate(coeffs)), F(0))


def multiply(p, q):
    r = [F(0)]*(len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i+j] += x*y
    return r


def run():
    checks = 0
    def check(value):
        nonlocal checks
        assert value
        checks += 1
    # h(x)=1-x^2 on [-1,1] lies in H0^1. For 0<=s<=2:
    # C_h(s)=16/15-4s^2/3+2s^3/3-s^5/30,
    # C_h'(s) is not used as an extra regularity assumption.
    c = [F(16,15), F(0), F(-4,3), F(2,3), F(0), F(-1,30)]
    cu = [F(8,3), F(-4), F(0), F(2,3)]
    value = lambda p, s: sum((v*s**j for j,v in enumerate(p)),F(0))
    for s in [F(j,8) for j in range(17)]:
        direct_c = integrate(multiply([F(1),F(0),F(-1)],
                                      [1-s*s,-2*s,F(-1)]), F(-1),1-s)
        direct_cu = integrate(multiply([F(0),F(-2)],[-2*s,F(-2)]),
                              F(-1),1-s)
        check(direct_c == value(c,s))
        check(direct_cu == value(cu,s))
        check(2*integrate(multiply([-s,F(1)],cu),s,F(2)) == -2*direct_c)
    check(value(c,F(2)) == 0)
    check(-integrate([F(0)]+cu,F(0),F(2)) == value(c,F(0)))
    # k_pole=-8(cosh(t/2)-1): -k_pole''=2cosh(t/2).
    check(-F(-8)*F(1,2)**2 == F(2))
    mu = F(3,2)
    harmonic = F(0)
    controls = []
    previous_error = None
    for n in range(1,129):
        harmonic += F(1,n)
        ell = mu+harmonic-1
        check(ell >= mu)
        if n in (1,2,4,8,16,32,64,128):
            mass = F(1,n*n)
            original = ell*mass
            error = -(ell+1)*mass
            check((original+error)/mass == -1)
            check(original/mass == ell > 0)
            if n == 1:
                check(original-mu*mass == 0)
            if previous_error is not None:
                check(abs(error) < previous_error)
            previous_error = abs(error)
            controls.append({'n':n,'relative_level_after_error':'-1',
                             'absolute_error':str(abs(error))})
    return {'passed':True,'finite_checks':checks,'controls':controls,
            'scope':'exact H0^1 polynomial identities and synthetic finite controls only',
            'actual_source_gain_established':False,'lean_certified':False}


if __name__ == '__main__':
    print(json.dumps(run(),indent=2))
