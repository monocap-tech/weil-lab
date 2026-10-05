"""Independent high-degree identities and constructor controls for prime 5."""
import json
from math import comb
from certify_native_legendre_small_window import F,legendre,certificate
from certify_native_prime3_source36 import regular_difference_factor,compute
from certify_native_exact_polynomial import correlation
from certify_native_prime5_matrix84_081 import integer_correlation
count=0
for j in range(84):
    for k in range(291):
        old=sum((F((-1)**r*comb(j,r),k+r) for r in range(1,j+1)),F(0))
        assert regular_difference_factor(j,k)==old,(j,k)
        count+=1
p=legendre(83)
for i,j in [(0,83),(80,83),(83,83)]:assert correlation(p[i],p[j])==integer_correlation(p[i],p[j])
for a,degree in [(F(81,100),51),(F(4,5),83),(F(81,100),47)]:
    try:certificate(a,True,degree)
    except ValueError:pass
    else:raise AssertionError('Unsupported native constructor accepted')
    try:compute(degree,a)
    except ValueError:pass
    else:raise AssertionError('Unsupported source constructor accepted')
print(json.dumps(dict(regular_factor_count=count,new_degree_correlation_checks=3,constructor_controls_rejected=True),indent=2))
