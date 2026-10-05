"""Independent exact-factor, correlation and constructor controls for degree 51."""
import json
from math import comb
from fractions import Fraction as F
from certify_native_prime3_source36 import regular_difference_factor
from certify_native_legendre_small_window import legendre,certificate
from certify_native_exact_polynomial import correlation
from certify_native_prime4_matrix52_080 import integer_correlation
count=0
for j in range(52):
 for k in range(165):
  original=sum((F((-1)**r*comb(j,r),k+r) for r in range(1,j+1)),F(0))
  assert regular_difference_factor(j,k)==original,(j,k)
  count+=1
p=legendre(51)
for i,j in [(0,51),(48,51),(51,51)]:assert correlation(p[i],p[j])==integer_correlation(p[i],p[j])
for a,degree in [(F(4,5),47),(F(3,4),51),(F(4,5),35)]:
 try:certificate(a,True,degree)
 except ValueError:pass
 else:raise AssertionError('Unsupported constructor accepted')
from certify_native_prime3_source36 import compute
for a,degree in [(F(4,5),47),(F(3,4),51),(F(4,5),35)]:
 try:compute(degree,a)
 except ValueError:pass
 else:raise AssertionError('Unsupported source constructor accepted')
print(json.dumps(dict(regular_factor_count=count,new_degree_correlation_checks=3,constructor_controls_rejected=True),indent=2))
