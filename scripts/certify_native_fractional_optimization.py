#!/usr/bin/env python3
"""Rational ceiling and exact-cube audits for fractional-rate optimization."""
from fractions import Fraction as F
import argparse,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args()
def pair(x):return [x.numerator,x.denominator]
rows=[]
for d in [F(1,2),F(1,4),F(1,8),F(1,16),F(1,32),F(3,4)]:
 s=(1-d)/2;U=4+16/d**2;A=1+s*U;D=96*U
 assert 0<s<F(1,2)
 assert U<=20/d**2 and A<=11/d**2 and D<=1920/d**2
 for S in [F(0),F(5),F(17)]:
  for C0 in [F(0),F(6),F(13)]:
   W=11*S+1920;E=C0/2+W+2;K=2*E+3
   B=A*S+D
   assert B<=W/d**2
   assert C0/2+B+1<=E/d**2
   assert K==C0+22*S+3847
   assert 2*(8/d+2)<=20/d
   assert 2*(E+1)+1==K
 rows.append({'d':pair(d),'s':pair(s),'U':pair(U),'A':pair(A),'D':pair(D)})
K=F(4096);samples=[]
for m in [2,4,8,16]:
 L=K*m**3;d=F(1,m);s=(1-d)/2
 assert L>=8*K and 0<d<=F(1,2) and F(1,4)<=s<F(1,2)
 loss=K/d**2+d*L
 assert loss==2*K*m*m
 assert (loss/2)**3==K*L**2
 assert -L+loss<=0
 samples.append({'cube_ratio_m':m,'L':pair(L),'d':pair(d),'s':pair(s),'loss':pair(loss)})
# Violating the threshold at L=K/8 yields d=2, hence a negative s.
wrong_d=F(2);wrong_L=K/8
control_rejected=wrong_d**3==K/wrong_L and not 0<wrong_d<1
assert control_rejected
out={'base_commit':'4ddee22f868164432dee3816e36c371d5108dd90','distance_checks':rows,
 'test_budget_K':pair(K),'test_budget_is_actual_aperture_budget':False,
 'exact_cube_scale_checks':samples,'negative_control_ignore_scale_threshold_rejected':control_rejected,
 'universal_proofs_mechanically_checked':False,'Lean_changed':False,
 'exact_exponent_one_established':False,'half_derivative_established':False,
 'exponential_gaussian_decay':False,'global_endpoint_exclusion':False,
 'F4':False,'FULL_TRANSPORT_CLOSED':False}
Path(args.output).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
print(json.dumps({'distances_checked':len(rows),'source_budget_cases':54,'exact_cube_scales':len(samples),'negative_control_rejected':control_rejected}))
