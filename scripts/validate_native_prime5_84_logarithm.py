"""Check accelerated logarithm endpoints against the original rational series."""
import json
from certify_native_legendre_small_window import F,I,log_rational as original
from certify_native_exact_logarithm import log_rational as accelerated
I.grid=10**400;count=0
for terms in [1,2,20,100,220]:
    for x in [F(1),F(2),F(3),F(5),F(81,25),F(100),F(3141592653589793238462643383279,10**30)]:
        a=original(x,terms);b=accelerated(x,terms)
        assert (a.lo,a.hi)==(b.lo,b.hi)
        count+=1
x=F(3141592653589793238462643383279*10**370+1,10**400)
a=original(x,220);b=accelerated(x,220)
assert (a.lo,a.hi)==(b.lo,b.hi);count+=1
print(json.dumps(dict(exact_logarithm_endpoint_comparisons=count,high_denominator_digits=400,original_series_interval_equality=True),indent=2))
