"""RC8 exact rational bounds for signed native log9 cross interactions."""
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
# Narrow packets: active atoms, support cap, continuous bound.
check(eb(F(1099,500))[0]>9)
check(eb(F(11,5))[1]<10)
check(eb(F(1))[1]<3)
check(eb(F(2))[1]<9)
check(eb(F(11,5))[0]>9)
check(eb(F(1,500))[1]<F(9,8))
check(eb(F(1,500))[1]<F(11,9))
check(F(11,5)+F(1,500)<F(12,5))
check(eb(F(6,5))[1]<4)
check(eb(F(1))[0]>2)
check(F(1,2)/(1-F(1,16))<1)
eps=F(1,1000)
narrow_cross_upper=-F(1,3)+6*2*eps
narrow_correction_upper=2*narrow_cross_upper
check(narrow_correction_upper==F(-241,375)<0)
# Wider packet: all possible atom overlaps, including 8 and 11.
wide=F(1,8)
check(eb(F(11,5))[0]>9)
check(F(11,10)+wide<F(123,100))
check(eb(F(123,50))[1]<12)
check(eb(F(1,4))[1]<F(9,7))
check(eb(F(1,4))[0]>F(9,8))
check(eb(F(1,4))[0]>F(11,9))
check(eb(F(1,10))[1]<F(9,8))
check(eb(F(1,5))[1]<F(11,9))
check(eb(F(3,5))[1]<2)
check(F(3,5)>2*wide)
check(eb(F(11,10))[0]>3)
check(eb(F(7,10))[0]>2)
check(F(14,5)**2<8)
check(eb(F(12,5))[0]>11)
check(F(33,10)**2<11)
# Entire cross-distance interval: j(d)<1/2.
check(eb(F(43,20))[1]<9)
check(eb(F(19,20))[0]>F(5,2))
check(eb(F(19,5))[0]>40)
check(F(2,5)/(1-F(1,40))<F(1,2))
overlap8_upper=1-F(1,10)/(2*wide)
overlap11_upper=1-F(1,5)/(2*wide)
check(overlap8_upper==F(3,5))
check(overlap11_upper==F(1,5))
c8_upper=F(7,10)/F(14,5)
c9_upper=F(11,10)/3
c11_upper=F(12,5)/F(33,10)
pole_lower=F(10,3)*(2*wide)
arch_upper=F(1,2)*(2*wide)
wide_cross_lower=pole_lower-arch_upper-c8_upper*overlap8_upper-c9_upper-c11_upper*overlap11_upper
check(wide_cross_lower==F(61,1320)>0)
check(2*wide_cross_lower==F(61,660))
# Exact log9 kernel and pole-only necessary threshold.
check(F(10,3)-F(27,80)==F(719,240))
check(F(1,3)/F(10,3)==F(1,10))
print(json.dumps({'milestone':'RC8','status':'PASS','exact_rational_checks':checks,
 'narrow_correction_upper':str(narrow_correction_upper),
 'wide_correction_lower':str(2*wide_cross_lower),
 'wide_nonzero_prime_cross_terms':[8,9,11],
 'scope':'analytic smooth-packet cross-sign bounds; no critical-mode evaluation',
 'original_negative_vector_claimed':False,'new_positive_aperture':False,
 'RH':False,'F4':False,'Lean':False},indent=2))
