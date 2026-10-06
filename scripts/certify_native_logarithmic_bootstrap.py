#!/usr/bin/env python3
"""Integer/rational audits for analytic logarithmic-bootstrap constants."""
import argparse,json,math
from fractions import Fraction as F
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args()
rows=[]
for k in range(13):
 moments=[2**(j+2)*math.factorial(j+1) for j in range(k+1)]
 assert moments[0]==4
 assert all(moments[j]==2*(j+1)*moments[j-1] for j in range(1,k+1))
 U=2**(k+1)+4*sum(math.comb(k,j)*moments[j] for j in range(k+1))
 # Independent Horner construction of the integral of v(1+v)^k exp(-v/2).
 coeff=[0]+[math.comb(k,j) for j in range(k+1)]
 acc=coeff[-1]
 for j in range(k, -1, -1): acc=coeff[j]+2*(j+1)*acc
 assert 2*acc==sum(math.comb(k,j)*moments[j] for j in range(k+1))
 A=1 if k==0 else 1+k*rows[-1]['U']
 pole=sum(math.comb(2*k,j)*2**(2*k-j)*math.factorial(j) for j in range(2*k+1))
 # Integration by parts: integral (2+t)^n exp(-t) = 2^n+n*previous.
 rec=1
 for n in range(1,2*k+1):rec=2**n+n*rec
 assert pole==rec
 rows.append({'k':k,'U':U,'A':A,'D':96*U,'pole_tail_moment':pole})
checks={'small_derivative_budget':4*(16+2)==72,
 'global_small_derivative_budget':72*2==144,
 'large_derivative_budget':F(1,3)+2<3,
 'commutator_pi_budget':F(144,3)==48,
 'two_sign_schur_budget':2*48==96,
 'pole_fourier_tail_budget':F(2,4*3**2)==F(1,18),
 'exp_one_exceeds_two':1+1+F(1,2)>2}
assert all(checks.values())
# Since 2*sinh(v/2)<=exp(v/2), J_0 >= 2*integral_0^inf v exp(-v/2)dv=8.
# Dropping the tail would produce the insufficient ceiling 2.
control_rejected=2<8<=rows[0]['U']
assert control_rejected
out={'base_commit':'a7d14ef13f2b83ddfbd21dcc32939a84202318f4','orders':rows,
 'checks':checks,'negative_control_drop_schur_tail_rejected':control_rejected,
 'universal_operator_proofs_mechanically_checked':False,'Lean_changed':False,
 'exponential_gaussian_decay':False,'global_endpoint_exclusion':False,
 'F4':False,'FULL_TRANSPORT_CLOSED':False}
Path(args.output).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
print(json.dumps({'orders_checked':len(rows),'budget_checks':len(checks),'negative_control_rejected':control_rejected}))
