"""V10B39d: exact finite projection budget (no infinite expansion).
Conditional on literal degree-63 Taylor reproduction and the coefficient
ratio/envelope; does not certify these analytic attachments.
"""
from fractions import Fraction as Q
from math import factorial,prod

n=64
# e^u >= 1+u >= 7/8 on [-1/8,1/8].
# Rodrigues beta leading coefficient = 31/(8^15 * 31!!).
den_lower=Q(7,8)*Q(31,8**15*prod(range(1,32,2)))
eps=Q(n+1,8**n*factorial(n)*n)
norm=sum((2*j+1)*16**j for j in range(n))
coarse=n*(2*n+1)*16**n
assert norm<=coarse
projection=eps*(1+coarse)/den_lower
rho=Q(1,65000)
outer=4**35*rho**10/(1-16*rho)
assert projection<Q(1,10**36)
assert outer<Q(1,10**27)
# Independent finite weighted Taylor coefficient error from V10B37c.
def B(j,m):
    return Q(factorial(j)*factorial(2*m)*factorial(j+m),
             factorial(m)*factorial(2*j+2*m+1))
def s(j,n):
    return Q(2*j+1,4**j*factorial(j))*sum(
        (B(j,m)/(8**(2*m)*factorial(2*m)) for m in range(n)),Q(0))
for k in (16,17):
    e=Q(2*k+1,8**(2*k)*factorial(2*k)*2*k)
    inner=2*e/(1-e)*sum((4**j*s(j,k)/s(15,k) for j in range(15,34,2)),Q(0))
    total=projection+outer+inner
    assert total<Q(1,10**25)
    print(k, 'retained terms: finite projection',float(projection),
          'outer',float(outer),'inner',float(inner),'total',float(total),'PASS')
