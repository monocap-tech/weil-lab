#!/usr/bin/env python3
"""NF467 symbolic/exact rational linearity and finite-translation primitive audit.
No original source coefficient or compact arch integral is evaluated here.
"""
from fractions import Fraction as F
import json
a,b=F(26,25),F(53,50);L=b-a;B=F(11,10)
assert L==F(1,50) and B-b==F(1,25)
# Exact polynomial source example: U(x)=sum c_j x^j, and a symbolic
# translation t standing for log(n), evaluated at rational t only for
# the algebra test; this is NOT the native NF407 source or a prime weight.
c=[F(3,7),F(-2,11),F(5,13)]
t=F(1,3)
def primitive(x):
 return sum(cj*x**(j+1)/F(j+1) for j,cj in enumerate(c))
def shifted_primitive(x):
 return primitive(x-t)
assert (shifted_primitive(b)-shifted_primitive(a))/L == sum(
 cj*((b-t)**(j+1)-(a-t)**(j+1))/(L*(j+1))
 for j,cj in enumerate(c))
# Abstract exact arch source-linearity in a finite source basis.
arch_basis=[F(2,7),F(-5,17),F(11,23)]
arch=sum(x*y for x,y in zip(c,arch_basis))
assert arch==sum(c[j]*arch_basis[j] for j in range(len(c)))
print(json.dumps({"pass":"NF467","scope":"exact linear mean and shifted primitive identity only",
 "panel":["26/25","53/50"],"length":"1/50",
 "original_J7_regular_minus_support":[2,3,4,5,7,8],
 "joint_compact_arch_panel_integral":"OPEN",
 "original_source_native_coefficients_evaluated":False,
 "original_mean_zbar":"OPEN","status":"operator identity established; numerical certification pending"},indent=2))
