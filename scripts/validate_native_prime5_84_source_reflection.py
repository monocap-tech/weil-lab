"""Compare exact reflection with the original rational binomial composition."""
import json
from math import factorial
from certify_native_legendre_small_window import F,bernoulli
from certify_native_endpoint_log_gram import shifted_legendre
from certify_native_prime3_source36 import compose,exact_reflect,regular_difference_factor
from certify_native_exact_polynomial import mul

d=F(81,50);N=90;K=100;B=bernoulli(202)
bp=[F(0)]*201;bp[0],bp[1]=F(1),d
for k in range(1,101):bp[2*k]=B[2*k]*(2*d)**(2*k)/factorial(2*k)
A=[c/2 for c in mul(bp,[(-d/2)**k/factorial(k) for k in range(91)])]
H=[F(0)]+[-c/k for k,c in enumerate(A) if k>0]
p=shifted_legendre(83)[83];left=[F(0)]*(len(p)+len(A)-1)
for j,c in enumerate(p):
    for k,b in enumerate(A):left[j+k]+=c*b*regular_difference_factor(j,k)
for polynomial in [p,H,left]:assert exact_reflect(polynomial)==compose(polynomial,F(1),F(-1))
print(json.dumps(dict(exact_reflection_checks=3,checked_polynomial_degrees=[len(x)-1 for x in [p,H,left]],original_binomial_composition_agreement=True),indent=2))
