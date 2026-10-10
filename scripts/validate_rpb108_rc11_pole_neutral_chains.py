"""RC11 exact budgets for pole-neutral log9 chains of arbitrary finite length.

Finite controls below accompany the universal analytic argument in the report.
They do not evaluate original critical modes or prove all-N by sampling.
"""
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
# Refine RC10's four-copy anchor lower bounds, retaining all six pairs.
check(eb(F(69,100))[1]<2)
check(F(23,16)**2>2)
check(F(23,8)**2>8)
check(F(69,100)/F(23,16)==F(12,25))
check(F(69,100)/2>F(17,50))
check(F(69,100)/F(23,8)==F(6,25))
check(eb(F(7,10))[0]>2)
check(F(3,2)*F(7,10)+eps_cap<F(53,50))
check(F(69,100)-2*eps_cap>F(1,2))
check(F(7,10)+2*eps_cap<1)
check(eb(F(1,2))[1]<F(5,3))
check(eb(F(1))[0]>2)
check(2*F(69,100)-2*eps_cap>1)
check(3*F(7,10)+2*eps_cap<F(53,25))
check(eb(F(53,50))[1]<3)
check(eb(F(1,2))[0]>F(3,2))
check(eb(F(2))[0]>4)
check(F(2,3)/(1-F(1,4))<1)
for ratio in [F(3,2),F(4,3),F(5,4),F(8,7),F(9,8)]:
    check(eb(2*eps_cap)[1]<ratio)
self_floor=(2*(3*F(12,25)+2*F(17,50)+F(6,25))-120*eps_cap)/4
check(self_floor==F(23,20))
# Pole moments are cancelled globally; local signed poles are still paid.
check(eb(eps_cap)[1]<F(5,4))
check(eb(4*eps_cap)[1]<2)
local_pole_allowance=4*eps_cap*F(5,4)
check(local_pole_allowance==F(1,200))
check(F(5,4)/(1-F(2,81))==F(405,316)<F(3,2))
check(eb(F(11,10))[0]>3)
coefficient=F(11,10)+3*eps_cap
check(coefficient==F(1103,1000))
check(2*F(1,3)/(1-F(1,3))==1)
row_cost=coefficient
total_loss=row_cost+local_pole_allowance
theta=total_loss/self_floor
reserve=1-theta
guard=self_floor-total_loss
check(total_loss==F(277,250))
check(theta==F(554,575)<1)
check(reserve==F(21,575)>0)
check(guard==F(21,500)>0)
check(reserve*self_floor==guard)
# Sample exact controls for the analytic integer-isolation and row-sum laws.
for count in [1,2,3,4,8,16]:
    maximum_n=9**(count-1)
    epsilon=F(1,1000*maximum_n)
    check(epsilon<=eps_cap)
    exp_upper=1/(1-2*epsilon) # exp(x)<=sum x^j=1/(1-x)
    check(exp_upper<1+F(1,maximum_n))
    check((maximum_n+1)*(500*maximum_n-1)-500*maximum_n**2==499*maximum_n-1>0)
    for gap in range(1,count):
        n=9**gap
        check(exp_upper<F(n+1,n))
        check(exp_upper<F(n,n-1))
    for i in range(count):
        row=sum((coefficient/F(3**abs(i-j)) for j in range(count) if i!=j),F(0))
        check(row<row_cost)
# A genuine nonzero pole-null coefficient vector for three common profiles.
centers_exp=[F(1,3),F(1),F(3)]
amplitudes=[F(1),F(-10,3),F(1)]
check(sum((a*z for a,z in zip(amplitudes,centers_exp)),F(0))==0)
check(sum((a/z for a,z in zip(amplitudes,centers_exp)),F(0))==0)
check(sum((a*a for a in amplitudes),F(0))==F(118,9)>0)
print(json.dumps({'milestone':'RC11','status':'PASS','exact_rational_checks':checks,
 'local_physical_floor':str(self_floor),'local_pole_allowance':str(local_pole_allowance),
 'all_count_row_cost':str(row_cost),'relative_loss_upper':str(theta),
 'relative_energy_reserve':str(reserve),'physical_guard':str(guard),
 'packet_count':'arbitrary finite N; analytic proof, finite controls only in script',
 'half_width_condition':'epsilon <= 1/(1000*9**(N-1))',
 'global_pole_moments':'both zero',
 'whole_centered_aperture_extended':False,'critical_mode_evaluated':False,
 'RH':False,'F4':False,'Lean':False},indent=2))
