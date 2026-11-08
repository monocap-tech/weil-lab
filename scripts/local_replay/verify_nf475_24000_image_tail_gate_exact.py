#!/usr/bin/env python3
"""NF475 exact rational source-independent near-B image/Cauchy/branch entry gates."""
from fractions import Fraction as F
from math import factorial
B=F(11,10); center=F(217,200); h=F(1,200); R=F(1,100); M=24000;N=1600
assert center-h==F(27,25) and center+h==F(109,100)
assert R>h and center+R==F(219,200)
assert B-(center+h)==F(1,100)
assert B-center==F(3,200) and h/(B-center)==F(1,3)
# log 9 = 2*atanh(4/5); the positive 10-term rational partial is a strict lower bound.
L=sum((2*F(4,5)**(2*k+1)/F(2*k+1) for k in range(10)),F(0))
assert L>F(439,200)==B+center+R
# Elementary exp(5)>110, proved by rational 7-term Taylor partial.
assert sum((F(5)**k/F(factorial(k)) for k in range(7)),F(0))>110
def tail(m):
    return F(100*10**160,m)*F(3,8)**(m//50)
assert tail(23000)>F(1,10**40)
assert tail(M)<F(1,10**40)
assert all(tail(i)>=F(1,10**40) for i in range(1000,24000,1000))
assert F(10**350)*F(1,2)**N/(1-F(1,2))<F(1,10**120)
assert F(117,10**13)*F(1,3)**260/(2*260*(1-F(1,3)))<F(1,10**116)
print("NF475 exact original J7 [1.08,1.09] near-B analytic/image tail gate PASS")
print("m=23000 absolute envelope remains >1e-40; m=24000 first 1000-grid passing cutoff")
print("Original source-native signed panel and full J7 still distinct obligations")
