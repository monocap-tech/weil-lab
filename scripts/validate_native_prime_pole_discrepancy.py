"""Exact finite arithmetic checks; not a Weil positivity certificate."""
from fractions import Fraction as F
from math import isqrt
import json
from certify_native_drive_cusp_geometry import log_interval

def sqrt_interval(n):
    den = 10**40
    k = isqrt(n*den*den)
    return F(k,den), F(k+1,den)

def run():
    powers = {2:2,3:3,4:2,5:5,7:7,8:2}
    # Verify that the dictionary contains all prime powers in this finite range.
    actual = {}
    for p in [2,3,5,7]:
        n = p
        while n <= 8:
            actual[n] = p
            n *= p
    assert powers == actual
    lo = hi = F(0)
    bounds = {}
    for n,p in powers.items():
        ll,lu = log_interval(p)
        sl,su = sqrt_interval(n)
        assert sl*sl <= n <= su*su
        lo += ll/su
        hi += lu/sl
        vl,vu = lo-2*(su-1), hi-2*(sl-1)
        assert vl < vu < -F(1,4)
        grid = 10**12
        lower = F((vl*grid).numerator//(vl*grid).denominator,grid)
        upper = F(-((-vu*grid).numerator//(-vu*grid).denominator),grid)
        assert lower <= vl < vu <= upper < -F(1,4)
        bounds[str(n)] = {'lower': str(lower), 'upper': str(upper)}
    a,d,eps = F(1,4),F(1,8),F(1,64)
    assert d+eps < a
    assert 2*eps < d
    assert 2*a < log_interval(2)[0]
    # Pole splitting minus the original prime budget preserves the signed total.
    for prime,growing,decaying in [(F(7,3),F(5,2),F(4,7)),(F(0),F(9,5),F(2))]:
        original = -2*prime+2*growing+2*decaying
        discrepancy = -2*(prime-growing)
        assert original == 2*decaying+discrepancy
        mu,mass = F(3,11),F(5,7)
        assert original-mu*mass == 2*decaying+discrepancy-mu*mass
    return {'actual_prime_power_jumps':6,'jump_upper_bound':'-1/4',
            'passed':True,'jump_enclosures':bounds,
            'scope':'finite arithmetic and form algebra; no positivity or gain certificate'}

if __name__ == '__main__':
    print(json.dumps(run(),indent=2))
