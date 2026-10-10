"""RC10 exact budgets: four-copy anchor probe and three-packet log9 gluing."""
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
eps=F(1,1000)
# Four anchor copies at centers (-3/2,-1/2,1/2,3/2)*log2.
check(eb(F(3,5))[1]<2)
check(eb(F(7,10))[0]>2)
check(F(3,2)*F(7,10)+eps<F(53,50))
check(F(3,5)>2*eps)
check(F(3,2)**2>2)
check(3**2>8)
check(F(3,5)-2*eps>F(1,2))
check(F(7,10)+2*eps<1)
check(eb(F(1,2))[1]<F(5,3))
check(eb(F(1))[0]>2)
check(2*F(3,5)-2*eps>1)
check(3*F(7,10)+2*eps<F(53,25))
check(eb(F(53,50))[1]<3)
check(eb(F(1,2))[0]>F(3,2))
check(eb(F(2))[0]>4)
check(F(2,3)/(1-F(1,4))<1)
for ratio in [F(3,2),F(4,3),F(5,4),F(8,7),F(9,8)]:
    check(eb(2*eps)[1]<ratio)
c2_lower=F(2,5)
c4_lower=F(3,10)
c8_lower=F(1,5)
pair_continuous_bound=5*2*eps
self_floor=(2*(3*c2_lower+2*c4_lower+c8_lower)-12*pair_continuous_bound)/4
check(self_floor==F(97,100))
# Target chain centers -log9,0,log9; arbitrary independent profiles.
check(eb(F(2))[1]<9)
check(eb(F(11,5))[0]>9)
check(F(11,5)+eps<F(221,100))
check(eb(F(11,10))[0]>3)
check(F(11,5)+2*eps<F(12,5))
check(eb(F(6,5))[1]<4)
check(F(1,2)/(1-F(1,16))<1)
check(eb(F(1))[0]>2)
check(2*F(11,5)+2*eps<F(23,5))
check(eb(F(23,10))[1]<10)
for ratio in [F(9,8),F(10,9),F(81,80),F(82,81)]:
    check(eb(2*eps)[1]<ratio)
adjacent=F(11,30)+6*2*eps
outer=F(11,90)+12*2*eps
check(adjacent==F(142,375))
check(outer==F(329,2250))
check(outer<adjacent)
row_bound=2*adjacent
theta=row_bound/self_floor
reserve=1-theta
guard=self_floor-row_bound
check(row_bound==F(284,375)<self_floor)
check(theta==F(1136,1455)<1)
check(reserve==F(319,1455)>0)
check(guard==F(319,1500)>0)
check(reserve*self_floor==guard)
# Algebra controls only; universal square identities appear in the report.
for a,b,c in [(F(1),F(1),F(1)),(F(2),F(1),F(0)),(F(1,3),F(7,5),F(9,4))]:
    loss=2*adjacent*(a*b+b*c)+2*outer*a*c
    rows=(adjacent+outer)*(a*a+c*c)+2*adjacent*b*b
    check(rows-loss==adjacent*((a-b)**2+(b-c)**2)+outer*(a-c)**2>=0)
    check(row_bound*(a*a+b*b+c*c)-rows==(adjacent-outer)*(a*a+c*c)>=0)
print(json.dumps({'milestone':'RC10','status':'PASS','exact_rational_checks':checks,
 'anchor_copy_count':4,'local_physical_floor':str(self_floor),
 'target_packet_count':3,'target_nonzero_cross_prime_powers':[9,81],
 'collective_mass_cost':str(row_bound),'relative_loss_upper':str(theta),
 'relative_energy_reserve':str(reserve),'three_interval_physical_guard':str(guard),
 'profiles':'arbitrary independent complex smooth profiles of radius <=1/1000',
 'whole_centered_aperture_extended':False,'critical_mode_evaluated':False,
 'RH':False,'F4':False,'Lean':False},indent=2))
