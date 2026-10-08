"""Finite rational budgets for the analytic NF57 prime-smearing theorem."""
from fractions import Fraction as F
from math import isqrt
from certify_native_drive_cusp_geometry import log_interval
import json

def sqrt_lower(n):
    den=10**40
    return F(isqrt(n*den*den),den)

def run():
    powers={2:2,3:3,4:2,5:5,7:7,8:2}
    actual={}
    for p in [2,3,5,7]:
        n=p
        while n<=8:
            actual[n]=p
            n*=p
    assert powers==actual
    budget=F(0)
    for n,p in powers.items():
        l,u=log_interval(p)
        sl=sqrt_lower(n)
        assert sl*sl<=n
        budget+=2*u/sl
        if n==7:
            assert budget<6
            one=budget
    assert budget<F(13,2)
    l2,u2=log_interval(2)
    assert l2>F(2,3)
    assert u2<1<log_interval(3)[0]
    assert log_interval(7)[1]<2<3*l2
    # Low-frequency constant: L exp(-L)<1/4 implies (32/3)*L*delta<4.
    assert F(32,3)*F(1,4)<4
    for k in [6,145,157,1000]:
        assert k*l2>4
        assert 4*one/(k*l2)<F(36,k)
        assert 4*budget/(k*l2)<F(39,k)
    k=36*10**34+1
    margin=F(2,10**34)
    assert F(36,k)<margin/2
    return {'passed':True,'aperture_one_prime_budget_upper':'6',
      'prime_8_threshold_budget_upper':'13/2',
      'dyadic_error_upper_bounds':['36/k','39/k'],
      'half_margin_sufficient_k':str(k),
      'scope':'exact finite budgets; analytic norm bound and lower limit not mechanically certified'}

if __name__=='__main__':
    print(json.dumps(run(),indent=2))
