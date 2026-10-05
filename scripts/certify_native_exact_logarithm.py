"""Same rational logarithm series, summed over one integer denominator."""
from math import lcm
from functools import lru_cache
from certify_native_legendre_small_window import F,I

@lru_cache(maxsize=None)
def odd_denominator(terms):return lcm(*range(1,2*terms,2))

def log_rational(x,terms=100):
    assert x>0
    def unit(y):
        z=(y-1)/(y+1);p=z.numerator;q=z.denominator
        common=odd_denominator(terms);p2=p*p;q2=q*q
        numerator=common//(2*terms-1);qpower=1
        for k in range(terms-2,-1,-1):
            qpower*=q2
            numerator=numerator*p2+(common//(2*k+1))*qpower
        s=F(2*p*numerator,common*q**(2*terms-1))
        e=2*abs(z)**(2*terms+1)/((2*terms+1)*(1-z*z))
        return I(s-e,s+e)
    power=0
    while x>=2:x/=2;power+=1
    while x<1:x*=2;power-=1
    return unit(x)+power*unit(F(2))
