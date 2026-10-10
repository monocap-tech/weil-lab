"""RC19 native digamma lower-envelope and concentration-screen budgets."""
from fractions import Fraction as F
from math import factorial
import json
checks=0
def check(v):
    global checks
    assert v, checks+1
    checks+=1
def eb(x,n=96):
    p=sum((x**j/F(factorial(j)) for j in range(n+1)),F(0))
    return p,p+x**(n+1)/F(factorial(n+1))/(1-x/F(n+2))
B=F(11,10)
check(eb(F(6,5))[0]>F(22,7)) # log(pi)<6/5 using inherited pi<22/7
check(2<eb(F(1))[0]<eb(F(1))[1]<3)
check(eb(F(10))[1]<22100)
prime=F(12093,3740)+F(11,30)
negative_pole=F(179,310)
check(2*prime+negative_pole<8)
arch_low=-F(1)-4-F(6,5)
check(arch_low==-F(31,5))
alpha=F(1,10); ell=F(10)
# High-frequency lower envelope after subtracting all nonarch negative cost.
check((1-alpha)*ell-8-(1+3*alpha)/2>0)
penalty=alpha*11-arch_low+8
check(penalty==F(153,10))
theta=F(1,306)
tail_floor=alpha-penalty*theta
check(tail_floor==F(1,20)>0)
rank_coefficient=4*B/theta
check(rank_coefficient==F(6732,5))
check(rank_coefficient*eb(F(10))[1]<30000000)
m=F(1,4000); beta=F(1,400)
cost=beta**2/tail_floor
check(cost==F(1,8000))
check(m-cost==F(1,8000)>0)
check(F(12000000000000)/30000000==400000)
# Rational algebra behind the Euler-sum variation estimate, a=1/4.
a=F(1,4)
for y in [a,F(1),F(2),F(100)]:
    f0=a/(a*a+y*y)
    fmax=y/(y*y+y*y)
    variation=2*fmax-f0
    check(fmax==1/(2*y))
    check(0<variation<=1/y)
    # Each Euler-series real-part increment from y=0 is nonnegative.
    for n in [0,1,7]:
        u=n+a
        check(1/u-u/(u*u+y*y)==y*y/(u*(u*u+y*y))>0)
# Blockwise positivity is still unsafe without actual source control.
check(m*tail_floor-F(1,100)**2<0)
print(json.dumps({'milestone':'RC19','status':'PASS','exact_rational_checks':checks,
 'cap':'11/10','frequency_cutoff':'exp(10)','concentration_threshold':str(theta),
 'native_arch_global_lower':str(arch_low),'nonarch_negative_allowance':8,
 'canonical_principal_floor':str(alpha),'low_band_penalty':str(penalty),
 'original_whole_tail_floor':str(tail_floor),'analytic_head_rank_upper':30000000,
 'conditional_actual_head_floor':str(m),'conditional_source_cross_norm_upper':str(beta),
 'conditional_schur_reserve':str(m-cost),'head_constructed':False,
 'actual_head_certified':False,'source_residual_certified':False,
 'whole_centered_aperture_extended':False,'RH':False,'F4':False,'Lean':False},indent=2))
