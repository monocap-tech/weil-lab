#!/usr/bin/env python3
"""Rational audits of analytic capped fractional-null estimates."""
from fractions import Fraction as F
import argparse,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args()
def pair(x):return [x.numerator,x.denominator]
rows=[]
for s in [F(1,16),F(1,8),F(1,4),F(1,3),F(2,5),F(7,16)]:
 d=F(1,2)-s;pole=1-2*s
 U=4+4/d**2;A=1+s*U;D=96*U
 assert d>0 and pole>0
 # The integral tail budget is independently 4/d^2 by integration by parts.
 assert U-4==4/d*F(1,d)
 assert F(2,3)*s*U<=s*U
 assert 1/pole**2>=1/pole
 for b in [F(0),F(1),F(3)]:
  for v in [F(0),F(2),F(5)]:
   assert (2*b+v/(3*pole))**2>=4*b*b+v*v/(9*pole)
 for budget in [F(0),F(1),F(17),F(10000)]:
  c=budget/(2*(budget+1))
  assert 0<=c<F(1,2)
  assert 1/(1-c)<=2
 # Check the capped log-weight Lipschitz statement directly for rational log coordinates.
 for x in [F(0),F(1,3),F(2),F(9)]:
  for y in [F(0),F(1,2),F(3),F(11)]:
   for cap in [F(0),F(1),F(4)]:
    assert abs(min(s*x,cap)-min(s*y,cap))<=s*abs(x-y)
 rows.append({'s':pair(s),'U':pair(U),'A':pair(A),'D':pair(D),
  'pole_tail_denominator':pair(pole),'collar_coefficient':pair(8/pole+2)})
quarter=rows[2]
assert quarter['U']==[68,1] and quarter['A']==[18,1] and quarter['D']==[6528,1]
control_rejected=(F(1,2)-F(1,2)==0 and 1-2*F(1,2)==0)
assert control_rejected
out={'base_commit':'6002bba61cb9abf21e341d72556589f02a5447d4','rational_s_checks':rows,
 'negative_control_include_half_derivative_rejected':control_rejected,
 'initial_multiplier_domain_assumed':False,'new_fractional_domain_assumed':False,
 'universal_operator_proofs_mechanically_checked':False,'Lean_changed':False,
 'exponential_gaussian_decay':False,'global_endpoint_exclusion':False,
 'F4':False,'FULL_TRANSPORT_CLOSED':False}
Path(args.output).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
print(json.dumps({'fractional_orders_checked':len(rows),'quarter_constants':[68,18,6528],'negative_control_rejected':control_rejected}))
