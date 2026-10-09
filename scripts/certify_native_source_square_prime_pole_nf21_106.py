#!/usr/bin/env python3
"""Exact prime-plus-signed-pole physical source-square Gram on e0/e1.
The original archimedean source is OMITTED. This is not the full Weil
source Gram or the finite native Q matrix. All intervals are rational.
"""
from fractions import Fraction as F
from math import isqrt
import json, hashlib
G=10**44
class I:
 def __init__(self,lo,hi=None):
  if isinstance(lo,I):self.l,self.h=lo.l,lo.h;return
  lo=F(lo);hi=F(lo if hi is None else hi);assert lo<=hi
  self.l=F((lo*G).__floor__(),G);self.h=F((hi*G).__ceil__(),G)
 def __add__(self,b):
  b=I(b);return I(self.l+b.l,self.h+b.h)
 __radd__=__add__
 def __neg__(self):return I(-self.h,-self.l)
 def __sub__(self,b):return self+-I(b)
 def __rsub__(self,b):return I(b)+-self
 def __mul__(self,b):
  b=I(b);z=[x*y for x in (self.l,self.h) for y in (b.l,b.h)]
  return I(min(z),max(z))
 __rmul__=__mul__
 def __truediv__(self,b):
  b=I(b);assert b.l>0 or b.h<0
  return self*I(1/b.h,1/b.l)
 def __pow__(self,k):
  assert k>=0 and isinstance(k,int)
  if k==0:return I(1)
  if k==1:return I(self)
  if k%2==0:
   q=self**(k//2);return q*q
  return self*(self**(k-1))
 def asstr(self):return [str(self.l),str(self.h)]

def log(n,terms=125):
 n=F(n);power=0
 while n>=2:n/=2;power+=1
 while n<1:n*=2;power-=1
 def unit(x):
  z=(x-1)/(x+1);p=z;v=F(0)
  for k in range(terms):v+=2*p/F(2*k+1);p*=z*z
  e=2*abs(p)/(F(2*terms+1)*(1-z*z))
  return I(v-e,v+e)
 return unit(n)+power*unit(F(2))

def sqrt(n):
 q=10**58;k=isqrt((n*q*q).__floor__())
 return I(F(k,q),F(k+1,q))

def extrema(op,v):
 return I(max(x.l for x in v),max(x.h for x in v)) if op=='max' else I(min(x.l for x in v),min(x.h for x in v))

def integrate(line, t, u):
 # integrated product (x+t)(x+u) dx over line=[L,U]
 L,U=line
 return (U**3-L**3)/3+(t+u)*(U**2-L**2)/2+t*u*(U-L)

def expi(x):
 x=I(x);bound=max(abs(x.l),abs(x.h))
 assert bound<F(11,10)
 terms=145;p=I(1);v=I(1)
 from math import factorial
 for k in range(1,terms):
  p=p*x;v+=p/F(factorial(k))
 rem=F(4)*bound**terms/factorial(terms)
 return v+I(-rem,rem)

def sinh(x):return (expi(x)-expi(-I(x)))/2

def cosh(x):return (expi(x)+expi(-I(x)))/2

def certificate():
 a=F(53,50);powers=(2,3,4,5,7,8)
 logs={n:log(n) for n in powers};weight={n:(logs[2] if n in (4,8) else logs[n])/sqrt(F(n)) for n in powers}
 assert logs[8].h<2*a<log(9).l
 panels=[]
 for n in powers:
  for sign in (1,-1):
   t=sign*logs[n]
   lower=extrema('max',[I(-a),I(-a)-t]);upper=extrema('min',[I(a),I(a)-t])
   assert upper.l>lower.h
   panels.append((n,sign,t,lower,upper))
 even=I(0);odd=I(0);overlaps=0
 for ni,si,ti,li,ui in panels:
  for nj,sj,tj,lj,uj in panels:
   lower=extrema('max',[li,lj]);upper=extrema('min',[ui,uj])
   if upper.h<lower.l: continue
   assert upper.l>lower.h, (ni,si,nj,sj,'ambiguous support overlap')
   overlap=(upper-lower)
   c=weight[ni]*weight[nj]
   even+=c*overlap
   odd+=c*integrate((lower,upper),ti,tj)
   overlaps+=1
 even=even/(2*a);odd=3*odd/(2*a**3)
 assert 0<even.l<even.h and 0<odd.l<odd.h
 # Exact original signed-pole SOURCE, NOT its native quadratic form.
 # L_pole(p)=exp(x/2)*m_minus(p)+exp(-x/2)*m_plus(p).
 sh=sinh(I(a)/2);ch=cosh(I(a)/2)
 m0=4*sh/sqrt(F(2*a))
 m1=sqrt(F(3)/(2*a))*(4*ch-8*sh/a)
 pole0=4*m0*m0*(sinh(I(a))+a)
 pole1=4*m1*m1*(sinh(I(a))-a)
 cross0=I(0);cross1=I(0)
 for n,sign,t,L,U in panels:
  c=weight[n]
  int_cosh=2*(sinh(U/2)-sinh(L/2))
  cross0+=2*(I(-1)/sqrt(F(2*a)))*(2*m0)*c*int_cosh
  def primitive(x):return 2*(x+t)*cosh(x/2)-4*sinh(x/2)
  int_linear_sinh=primitive(U)-primitive(L)
  cross1+=4*sqrt(F(3)/(2*a))/a*m1*c*int_linear_sinh
 combined0=even+pole0+cross0
 combined1=odd+pole1+cross1
 assert pole0.l>0 and pole1.l>0
 assert combined0.l>0 and combined1.l>0
 # physical reflection proves the offdiagonal e0/e1 pairing vanishes exactly.
 return dict(aperture='53/50',active_prime_powers=list(powers),orientations=12,
   overlapping_ordered_source_shift_pairs=overlaps,
   prime_only_source_square_gram_00=even.asstr(),
   prime_only_source_square_gram_11=odd.asstr(),
   prime_only_source_square_gram_01=['0','0'],
   pole_only_source_square_gram_00=pole0.asstr(),
   pole_only_source_square_gram_11=pole1.asstr(),
   prime_pole_source_cross_00=cross0.asstr(),
   prime_pole_source_cross_11=cross1.asstr(),
   prime_plus_pole_source_square_gram_00=combined0.asstr(),
   prime_plus_pole_source_square_gram_11=combined1.asstr(),
   complete_prime_plus_pole_source_gram_01=['0','0'],
   guaranteed_signs='strict positive diagonal, zero cross by reflection',
   native_pole_form_00=(2*m0*m0).asstr(),
   native_pole_form_11=(-2*m1*m1).asstr(),
   full_source_Gram=False,archimedean_source_included=False,pole_source_included=True,
   full_residual_P2_built=False,whole_aperture_positive=False)
if __name__=='__main__':
 c=certificate();print(json.dumps(c,indent=2))
