"""RC7 rational enclosures for an actual native cross-packet loss."""
from fractions import Fraction as F
from math import factorial
import json
checks=0
def check(v):
    global checks
    if not v: raise AssertionError(checks+1)
    checks+=1
def eb(x,n=20):
    p=sum((x**j/F(factorial(j)) for j in range(n+1)),F(0))
    return p,p+x**(n+1)/F(factorial(n+1))/(1-x/F(n+2))
check(eb(F(3,5))[1]<2) # log 2 > .6
check(eb(F(7,10))[0]>2) # log 2 < .7
check(eb(F(1))[1]<3) # log 3 > 1
check(eb(F(1))[0]>2) # e > 2
check(eb(F(1,2))[1]<F(5,3))
check(F(3,2)**2>2)
epsilon=F(1,1000)
check(F(3,5)-2*epsilon>F(1,2))
check(F(7,10)+2*epsilon<1)
prime_coefficient_lower=F(3,5)/F(3,2)
check(prime_coefficient_lower==F(2,5))
# For distances in [.5,1], |2cosh(d/2)-j(d)| < 3+2=5.
continuous_cross_upper=5*(2*epsilon)
correction_upper=-2*prime_coefficient_lower+2*continuous_cross_upper
check(correction_upper==F(-39,50)<0)
eta=F(1,10**37)
check(-correction_upper>2*eta)
# Prime 9 first enters beyond the certified tile diameter.
check(eb(F(53,25))[1]<9)
check(eb(F(11,5))[0]>9)
# Exact partition loss retains signs and mixed terms.
# At two packet supports the partition vectors are (1,0), (0,1).
cx,cy=(F(1),F(0)),(F(0),F(1))
delta=1-sum(x*y for x,y in zip(cx,cy))
check(delta==sum((x-y)**2 for x,y in zip(cx,cy))/2==1)
for kernel in [F(-2),F(3),F(-1,4)]:
    for cross in [F(1),F(-1),F(2,3)]:
        global_cross=2*kernel*cross
        local_cross=2*kernel*cross*sum(x*y for x,y in zip(cx,cy))
        correction=2*kernel*cross*delta
        check(global_cross==local_cross+correction)
print(json.dumps({'milestone':'RC7','status':'PASS','exact_rational_checks':checks,
 'packet_half_width':str(epsilon),'native_localization_correction_upper':str(correction_upper),
 'scope':'rational bounds for analytic smooth-packet localization control',
 'actual_critical_vector_evaluated':False,'original_negative_vector_claimed':False,
 'RH':False,'F4':False,'Lean':False},indent=2))
