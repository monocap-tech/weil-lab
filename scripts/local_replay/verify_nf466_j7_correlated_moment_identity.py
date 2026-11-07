#!/usr/bin/env python3
"""Exact-rational NF466 algebraic and panel geometry tests; NOT a source-integral verifier."""
from fractions import Fraction as F
import json
B=F(11,10); a=F(26,25); b=F(53,50); L=b-a
assert L==F(1,50)
assert B-a==F(3,50) and B-b==F(1,25)
# Finite exact-rational quadrature identity, valid for arbitrary p,z arrays
# with equal-weight sample quadrature; the continuous proof is identical.
p=[F(1,3),F(2,5),F(3,7),F(4,9),F(5,11)]
z=[F(1,13),F(-2,17),F(3,19),F(-4,23),F(5,29)]
n=len(p); pm=sum(p)/n; zm=sum(z)/n
direct=sum(4*x*y+2*y*y for x,y in zip(p,z))/n
split=4*pm*zm+2*zm*zm+4*sum((x-pm)*(y-zm) for x,y in zip(p,z))/n+2*sum((y-zm)**2 for y in z)/n
assert direct==split
# F1(d)=d(C+.5*log(B/d)+.5), dF1/dd=q(d).
# p' = v/(2(B-x)) <0 for v<0, oscillation = |v|/2 log(3/2).
assert (B-a)/(B-b)==F(3,2)
print(json.dumps({"pass":"NF466","standing":"algebraic exact-rational identity only","panel":["26/25","53/50"],"length":"1/50","d_endpoints":["3/50","1/25"],"principal_oscillation_over_abs_v":"(1/2)log(3/2)","signed_source_panel_integral":"OPEN","mean_covariance_variance_identity":"PASS","exact_original_source_evaluation":"NOT PERFORMED"},indent=2))
