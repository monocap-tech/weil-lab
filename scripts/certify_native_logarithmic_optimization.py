#!/usr/bin/env python3
"""Exact constant/envelope audits and rational log interval order controls."""
from fractions import Fraction as F
import argparse,json,math
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args()
def log_unit(x,N=80):
 z=(x-1)/(x+1)
 lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
 tail=2*z**(2*N+1)/(F(2*N+1)*(1-z*z))
 return lo,lo+tail
L2=log_unit(F(2))
def log_interval(x):
 x=F(x);q=0
 while x>2:x/=2;q+=1
 lo,hi=log_unit(x)
 return q*L2[0]+lo,q*L2[1]+hi
rows=[];Z=4096;B=1;prod=1
for k in range(65):
 U=2**(k+1)+16*sum(math.comb(k,j)*2**j*math.factorial(j+1) for j in range(k+1))
 cap=34*2**k*math.factorial(k+1)
 assert U<=cap
 A=1 if k==0 else 1+k*rows[-1]['U']
 assert A<=35*2**k*math.factorial(k+1)
 assert 96*U<=3264*2**k*math.factorial(k+1)
 pole=sum(math.comb(2*k,j)*2**(2*k-j)*math.factorial(j) for j in range(2*k+1))
 assert pole<9*math.factorial(2*k)
 assert math.factorial(2*k)<=4**k*math.factorial(k)**2
 if k: B*=Z*2**(k-1)*math.factorial(k);prod*=math.factorial(k)
 assert B==Z**k*2**(k*(k-1)//2)*prod
 rows.append({'k':k,'U':U,'factorial_U_ceiling':cap})
Zlo,Zhi=log_interval(Z);samples=[]
for t in [128,256,512,1024]:
 lo,hi=log_interval(t+2)
 kl=F(t)/(8*hi);kh=F(t)/(8*lo)
 k=kl.numerator//kl.denominator
 assert k==kh.numerator//kh.denominator
 assert t>=4*Zhi and k>=F(t)/(16*lo)
 lklo,lkhi=log_interval(2*k)
 exponent_hi=2*k*Zhi+2*k*k*lkhi-2*k*t
 target_lo=-F(t*t)/(16*lo)
 assert exponent_hi<=target_lo
 samples.append({'t':t,'k':k,'threshold_satisfied':True,'exponent_comparison_passed':True})
# Deliberately violate the aperture-budget threshold; the bound's exponent becomes positive.
wronglo,wronghi=log_interval(2**512);t=128;k=samples[0]['k']
control_rejected=2*k*(wronglo-t)>0 and t<4*wronglo
assert control_rejected
out={'base_commit':'cc9302665923e060a5d5b56c032dd5990727eabf',
 'integer_orders':rows,'test_budget_Z':Z,'floor_and_exponent_samples':samples,
 'negative_control_ignore_budget_threshold_rejected':control_rejected,
 'log_intervals':'80-term rational atanh series with geometric tail; powers-of-two reduction',
 'universal_proofs_mechanically_checked':False,'Lean_changed':False,
 'exponential_gaussian_decay_in_R':False,'global_endpoint_exclusion':False,
 'F4':False,'FULL_TRANSPORT_CLOSED':False}
Path(args.output).write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
print(json.dumps({'orders_checked':len(rows),'rational_log_samples':len(samples),'negative_control_rejected':control_rejected}))
