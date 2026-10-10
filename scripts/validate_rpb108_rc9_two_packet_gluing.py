"""RC9 rational certificate budgets for arbitrary narrow two-packet gluing."""
from fractions import Fraction as F
from math import factorial
import json
checks=0
def check(v):
    global checks
    if not v: raise AssertionError(checks+1)
    checks+=1
def eb(x,n=24):
    p=sum((x**j/F(factorial(j)) for j in range(n+1)),F(0))
    return p,p+x**(n+1)/F(factorial(n+1))/(1-x/F(n+2))
eps=F(1,1000)
# Anchor probe: two copies at separation log2.
check(eb(F(3,5))[1]<2)
check(eb(F(7,10))[0]>2)
check(eb(F(1))[1]<3)
check(F(3,2)**2>2)
check(F(7,20)+eps<F(53,50))
check(F(3,5)>2*eps)
check(F(3,5)-2*eps>F(1,2))
check(F(7,10)+2*eps<1)
check(eb(F(1,2))[1]<F(5,3))
check(eb(F(1))[0]>2)
check(F(5,3)+1<3)
check(1/(1-F(1,2))==2)
check(1>F(7,10)+2*eps) # excludes every n>=3 atom
c2_lower=F(3,5)/F(3,2)
anchor_continuous_allowance=5*2*eps
self_floor=c2_lower-anchor_continuous_allowance
check(self_floor==F(39,100))
# Log9 target probe, with two independent profiles and all active atoms.
check(eb(F(1099,500))[0]>9)
check(eb(F(11,5))[1]<10)
check(eb(F(2))[1]<9)
check(eb(F(11,5))[0]>9)
check(eb(F(1,500))[1]<F(9,8))
check(eb(F(1,500))[1]<F(11,9))
check(F(11,5)+2*eps<F(12,5))
check(eb(F(6,5))[1]<4)
check(F(1,2)/(1-F(1,16))<1)
check(eb(F(11,10))[0]>3)
c9_upper=F(11,30)
cross_norm_bound=c9_upper+6*2*eps
theta=cross_norm_bound/self_floor
relative_reserve=1-theta
physical_guard=self_floor-cross_norm_bound
check(cross_norm_bound==F(142,375))
check(theta==F(568,585)<1)
check(relative_reserve==F(17,585)>0)
check(physical_guard==F(17,1500)>0)
check(relative_reserve*self_floor==physical_guard)
# Finite rational controls illustrate, but do not prove, the universal
# algebraic inequalities (x-y)^2>=0 used in the analytic report.
for x,y in [(F(1),F(1)),(F(2),F(1)),(F(0),F(3)),(F(7,3),F(5,4))]:
    check(x*x+y*y-2*x*y==(x-y)**2>=0)
    worst=self_floor*(x*x+y*y)-2*cross_norm_bound*x*y
    check(worst-physical_guard*(x*x+y*y)==cross_norm_bound*(x-y)**2>=0)
print(json.dumps({'milestone':'RC9','status':'PASS','exact_rational_checks':checks,
 'local_physical_floor':str(self_floor),'mixed_mass_coefficient':str(cross_norm_bound),
 'relative_loss_upper':str(theta),'relative_energy_reserve':str(relative_reserve),
 'two_interval_physical_guard':str(physical_guard),
 'profiles':'arbitrary independent complex smooth profiles, radius <=1/1000',
 'whole_centered_aperture_extended':False,'critical_mode_evaluated':False,
 'RH':False,'F4':False,'Lean':False},indent=2))
