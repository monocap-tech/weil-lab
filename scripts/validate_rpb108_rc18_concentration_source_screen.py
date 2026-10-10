"""RC18 exact concentration-tail and conditional source-residual budgets."""
from fractions import Fraction as F
from math import factorial
import json
checks=0
def check(v):
    global checks
    assert v, checks+1
    checks+=1
def eb(x,n=128):
    p=sum((x**j/F(factorial(j)) for j in range(n+1)),F(0))
    return p,p+x**(n+1)/F(factorial(n+1))/(1-x/F(n+2))
B=F(11,10); N=F(16); ell=F(24); theta=F(1,96)
tail_mass=theta+1/ell
tail_floor=1-N*tail_mass
check(tail_mass==F(5,96))
check(tail_floor==F(1,6)>0)
check(theta<1/N-1/ell)
beta=F(1,200); m=F(1,4000)
cost=beta**2/tail_floor
check(cost==F(3,20000))
check(m-cost==F(1,10000)>0)
check(beta**2<m*tail_floor)
rank_coefficient=4*B/theta
check(rank_coefficient==F(2112,5))
exp24_upper=eb(ell)[1]
check(exp24_upper<27000000000)
check(rank_coefficient*exp24_upper<12*10**12)
check(F(16000000)/ell==F(2000000,3))
# Generic full-remainder cross bound is insufficient at this coarse tail.
generic_cross_squared=21**2*tail_mass
check(generic_cross_squared/tail_floor>m)
# Hilbert--Schmidt column residual bounds dominate the operator norm.
for residuals in [[F(1,400),F(1,400)], [F(1,1000)]*10, [F(1,200)]]:
    check(sum(r*r for r in residuals)<=beta**2)
# Lower tail and positive head alone still permit a negative coupled block.
check(m*tail_floor-F(1,100)**2<0)
print(json.dumps({'milestone':'RC18','status':'PASS','exact_rational_checks':checks,
 'cap':'11/10','frequency_cutoff':'exp(24)','concentration_threshold':str(theta),
 'whole_tail_physical_mass_upper':str(tail_mass),'original_whole_tail_floor':str(tail_floor),
 'conditional_source_cross_norm_upper':str(beta),'conditional_head_floor':str(m),
 'conditional_schur_reserve':str(m-cost),'analytic_head_rank_upper':12000000000000,
 'concentration_eigenspace_constructed':False,'source_residual_certified':False,
 'actual_head_certified':False,'whole_centered_aperture_extended':False,
 'RH':False,'F4':False,'Lean':False},indent=2))
