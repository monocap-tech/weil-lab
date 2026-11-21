#!/usr/bin/env python3
"""PI031: exact integer-interval quadrature: m=1 normalized smooth correlation.

All accepted sign enclosures use integer outward-rounded operations and an
explicit mean-value remainder for each midpoint integration cell.
No Lean, compiled kernel, interval package, or spectral sum.
"""
from fractions import Fraction as F
S=10**45

def C(num, den=1):
    q=F(num,den)
    return I(q.numerator*S//q.denominator, -(-q.numerator*S//q.denominator))

class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi):
        assert isinstance(lo,int) and isinstance(hi,int) and lo<=hi,(lo,hi)
        self.lo,self.hi=lo,hi
    def __repr__(self):return f'[{self.lo/S:.8g},{self.hi/S:.8g}]'
    def __add__(self,other):
        other=asI(other);return I(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,other):return self+-asI(other)
    def __rsub__(self,other):return asI(other)+-self
    def __mul__(self,other):
        other=asI(other)
        v=[self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi]
        lo,hi=min(v),max(v)
        return I(lo//S,-(-hi//S))
    __rmul__=__mul__
    def recip(self):
        assert self.lo>0,(self, 'not positive')
        return I(S*S//self.hi,-(-S*S//self.lo))
    def __truediv__(self,other):
        if isinstance(other,int) and other>0:
            return I(self.lo//other, -(-self.hi//other))
        return self*asI(other).recip()
    def __rtruediv__(self,other):return asI(other)*self.recip()
    def __pow__(self, k):
        assert isinstance(k,int) and k>=0
        out=asI(1); p=self
        while k:
            if k%2:out=out*p
            p=p*p;k//=2
        return out
    def absmax(self):return max(abs(self.lo),abs(self.hi))

def asI(x):return x if isinstance(x,I) else C(x)

def expneg_scalar(t):
    assert t>0
    k=0
    divisor=1
    while -(-t//divisor)>S:
        k+=1;divisor*=2
    z=I(t//divisor,-(-t//divisor))
    term=C(1); partial=C(1)
    upper=None
    for n in range(1,32):
        term=term*z/n
        partial= partial-term if n%2 else partial+term
        if n==30:upper=partial.hi
    result=I(partial.lo,upper)
    assert result.lo>0
    for _ in range(k):result=result*result
    return result

def expneg(T):
    assert T.lo>0
    low=expneg_scalar(T.hi)
    high=expneg_scalar(T.lo)
    return I(low.lo,high.hi)

ELL_SQUARED_OVER_FOUR = I(C(F(1, 4_000_000)).lo,C(F(1,3_240_000)).hi)
EPS=C(F(1,20))

def smooth_eval(y):
    assert y.lo>=EPS.lo and y.hi<= (C(1)-EPS).hi
    a=y*(1-y)
    c=1-2*y
    t=a.recip()
    em=expneg(t)
    t2=t*t;t3=t2*t;t4=t3*t;t5=t4*t
    c2=c*c;c3=c2*c;c4=c2*c2
    l1=c*t2
    l2=-2*t2-2*c2*t3
    l3=12*c*t3+6*c3*t4
    l4=-24*t3-72*c2*t4-24*c4*t5
    E=em*(l1**3+3*l1*l2+l3-ELL_SQUARED_OVER_FOUR*l1)
    Ep=em*(l1**4+6*l1*l1*l2+3*l2*l2+4*l1*l3+l4-ELL_SQUARED_OVER_FOUR*(l1*l1+l2))
    return E,Ep

def endpoint_eval(y):
    # Proved envelope for y in [0,1/20] U [19/20,1]:
    # t=1/[y(1-y)] >=20, and e^-20 < 1/10^8
    # via sum_{k=0}^{16}20^k/k! >10^8.
    return I(-S,S),I(-500*S,500*S)

def enclose(y):
    if y.hi<=EPS.lo or y.lo >= (C(1)-EPS).hi:
        return endpoint_eval(y)
    left=C(F(1,20));right=C(F(19,20))
    Evals=[]
    if y.lo<left.hi or y.hi>right.lo:Evals.append(endpoint_eval(y))
    innerlo=max(y.lo,left.lo)
    innerhi=min(y.hi,right.hi)
    if innerlo<=innerhi:Evals.append(smooth_eval(I(innerlo,innerhi)))
    assert Evals
    return tuple(I(min(v[p].lo for v in Evals),max(v[p].hi for v in Evals)) for p in (0,1))

def sign_test(tau,N):
    assert isinstance(tau,F) and 0<=tau<1 and N>0
    h=(F(1)-tau)/N
    hI=C(h)
    errorCoeff=C(h*h/F(4))
    isum=C(0)
    maxlocal=0
    for j in range(N):
        a=tau+h*j; b=a+h
        mid=(a+b)/2
        tmid=C(mid)
        em,_=enclose(tmid)
        fm,_=enclose(C(mid-tau))
        center=em*fm
        ea,epa=enclose(I(C(a).lo,C(b).hi))
        fa,fpa=enclose(I(C(a-tau).lo,C(b-tau).hi))
        m=(epa.absmax()*fa.absmax()+ea.absmax()*fpa.absmax()+S-1)//S
        maxlocal=max(maxlocal,m)
        # Exact integral inclusion via midpoint + derivative sup error.
        error=I(-m,-m)*errorCoeff + I(0,2*m)*errorCoeff
        isum=isum+center*hI+error
    return isum,maxlocal

def assert_endpoint_bounds():
    # If y<=1/20 or y>=19/20, T=1/[y(1-y)]>=20.
    # For k<=8, T^k*exp(-T) decreases on T>=20.
    term=F(1);partial=F(1)
    for k in range(1,17):
        term*=F(20,k)
        partial+=term
    assert partial > 100_000_000
    t=20
    delta=F(1,3_240_000)
    E_bound=t**6+6*t**5+12*t**4+12*t**3+delta*t*t
    Ep_bound=(t**8+12*t**7+48*t**6+96*t**5+84*t**4+
              24*t**3+delta*(t**4+2*t**3+2*t**2))
    assert E_bound < 100_000_000
    assert Ep_bound < 500*100_000_000

def main():
    assert_endpoint_bounds()
    assert F(3)/F(10,9)**2==F(243,100)>2
    assert F(3)*F(10,9)==F(10,3)<4
    # d=log(10/9) is in (1/10,1/9). The true ell²/4=d²/40000
    # is contained in [1/4000000,1/3240000].
    N=512
    out={}
    for tau in (F(0),F(1,4),F(3,5),F(3,4)):
        enclosure, max_lipschitz=sign_test(tau,N)
        out[tau]=enclosure
        print(f'PI031 tau={tau}: integral enclosure {enclosure}',flush=True)
    # Strict acceptance comparisons using only exact integers.
    assert out[F(0)].lo > C(17).hi
    assert out[F(0)].hi < C(21).lo
    assert out[F(1,4)].hi < C(-5).lo
    assert out[F(3,5)].lo > C(6).hi
    assert out[F(3,4)].hi < C(-3).lo
    # Combine this source-exact correlation certificate with PI030's
    # analytic B<J/450 and kappa3>1/3 (not derived by this script).
    u=F(3,2)
    mass_factor=1+u*u
    gamma_bound=mass_factor*F(21)/450
    central_prime_lower=F(1,3)*mass_factor*F(6)
    satellite_prime_lower=F(1,3)*u*F(6)
    assert gamma_bound < central_prime_lower
    assert gamma_bound < satellite_prime_lower
    print('PI031 exact root-sign budget: at least 3 central + 6 satellite = 9 live crossings: PASS')
    print('No derivative-at-root certificate, exact total root count, Lean or Actions.')

if __name__=='__main__':
    main()
