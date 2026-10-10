"""RC12 exact signed-pole budgets; universal argument is in the report."""
from fractions import Fraction as F
from math import factorial
import json
checks=0
def check(v):
    global checks
    if not v: raise AssertionError(checks+1)
    checks+=1
def eb(x,n=28):
    p=sum((x**j/F(factorial(j)) for j in range(n+1)),F(0))
    return p,p+x**(n+1)/F(factorial(n+1))/(1-x/F(n+2))
eps_cap=F(1,1000)
check(eb(eps_cap)[1]<F(5,4))
# RC11 budgets, inherited without imposing its global moment constraint.
self_floor=F(23,20)
local_pole_cost=F(1,200)
background_cross_cost=F(1103,1000)
background_guard=self_floor-local_pole_cost-background_cross_cost
check(background_guard==F(21,500))
global_negative_pole_cost=F(2)*eps_cap*F(5,4)*F(9,8)
check(global_negative_pole_cost==F(9,3200))
total_loss=local_pole_cost+background_cross_cost+global_negative_pole_cost
theta=total_loss/self_floor
reserve=1-theta
guard=self_floor-total_loss
check(total_loss==F(17773,16000))
check(theta==F(17773,18400)<1)
check(reserve==F(627,18400)>0)
check(guard==F(627,16000)>0)
check(reserve*self_floor==guard)
check(background_guard-global_negative_pole_cost==guard)
# Exact integral enclosures at selected N; the all-N geometric proof is analytic.
for count in [1,2,3,4,8,16]:
    maximum_n=9**(count-1)
    epsilon=F(1,1000*maximum_n)
    weights=[F(3)**(2*i-(count-1)) for i in range(count)]
    weight_sum=sum(weights,F(0))
    check(weight_sum==F(9**count-1,8*3**(count-1)))
    check(weight_sum<F(9,8)*3**(count-1))
    exp_lower,exp_upper=eb(epsilon)
    integral_upper=(exp_upper-1/exp_upper)*weight_sum
    support_length=2*count*epsilon
    coarse_upper=2*epsilon*F(5,4)*weight_sum
    decay_upper=global_negative_pole_cost/F(3**(count-1))
    check(exp_upper<F(5,4))
    check(integral_upper<coarse_upper<decay_upper)
    check(decay_upper<=global_negative_pole_cost)
    check(integral_upper>=support_length)
    # Integral cosh - length is the exact norm squared of the odd moment functional.
    check(integral_upper-support_length<decay_upper)
    check(background_guard-decay_upper>=guard)
# Rational moment identities with nonzero moments and both pole signs.
weights=[F(1,3),F(1),F(3)]
for real,imag in [([F(1),F(1),F(1)],[F(0)]*3),
                  ([F(1),F(0),F(-1)],[F(0)]*3),
                  ([F(1),F(-2),F(3)],[F(2),F(1),F(-1)])]:
    plus_r=sum((a*w for a,w in zip(real,weights)),F(0))
    minus_r=sum((a/w for a,w in zip(real,weights)),F(0))
    plus_i=sum((a*w for a,w in zip(imag,weights)),F(0))
    minus_i=sum((a/w for a,w in zip(imag,weights)),F(0))
    pole=2*(plus_r*minus_r+plus_i*minus_i)
    even_sq=((plus_r+minus_r)**2+(plus_i+minus_i)**2)/2
    odd_sq=((plus_r-minus_r)**2+(plus_i-minus_i)**2)/2
    check(pole==even_sq-odd_sq)
    check(pole>=-odd_sq)
check(2*(F(1,3)-3)*(3-F(1,3))==F(-128,9)<0)
print(json.dumps({'milestone':'RC12','status':'PASS','exact_rational_checks':checks,
 'global_negative_pole_allowance':str(global_negative_pole_cost),
 'relative_loss_upper':str(theta),'relative_energy_reserve':str(reserve),
 'physical_guard':str(guard),'packet_count':'arbitrary finite N; analytic proof',
 'half_width_condition':'epsilon <= 1/(1000*9**(N-1))',
 'global_moment_constraints':'none; signed poles explicitly retained',
 'scope':'arbitrary complex profiles on the sparse log9 chain support',
 'whole_centered_aperture_extended':False,'critical_mode_evaluated':False,
 'RH':False,'F4':False,'Lean':False},indent=2))
