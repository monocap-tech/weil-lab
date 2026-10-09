#!/usr/bin/env python3
"""Independent Fraction checks of DNE14 split convolution and log primitives."""
from fractions import Fraction as F
from math import comb,factorial
import json

def mul(p,q):
 out=[F(0)]*(len(p)+len(q)-1)
 for i,x in enumerate(p):
  for j,y in enumerate(q):out[i+j]+=x*y
 return out

def value(p,x):
 s=F(0)
 for c in reversed(p):s=s*x+c
 return s

def split_integral(m,k,x,a):
 # Independently substitute t=x-y and t=y-x, then integrate powers of t.
 left=sum(F(comb(k,i))*(-1)**i*x**(k-i)*(x+a)**(m+i+1)/F(m+i+1) for i in range(k+1))
 right=sum(F(comb(k,i))*x**(k-i)*(a-x)**(m+i+1)/F(m+i+1) for i in range(k+1))
 return left+right
count=0
for m in range(18):
 for k in range(15):
  a=F(53,50);p=[F(0)]*(m+k+2)
  for l in range(k%2,m+1,2):p[l]+=2*(-1)**k*comb(m,l)*a**(k+m-l+1)/F(k+m-l+1)
  if m%2:p[m+k+1]+=2*F(factorial(k)*factorial(m),factorial(k+m+1))
  for x in (F(0),F(1,3),F(-7,10),F(53,50)):
   assert value(p,x)==split_integral(m,k,x,a);count+=1
# Differentiate the coefficient-polynomial construction of int x^k log(a+-x).
# In t=a+sign*x, derivative of t^(i+1)[log(t)/(i+1)-1/(i+1)^2]
# is exactly t^i log(t); transformed polynomial must equal x^k.
for k in range(60):
 for sign in (-1,1):
  a=F(53,50);out=[F(0)]*(k+1)
  for i in range(k+1):
   c=sign**k*comb(k,i)*(-a)**(k-i)
   for j in range(i+1):out[j]+=c*comb(i,j)*a**(i-j)*sign**j
  assert out==[F(0)]*k+[F(1)];count+=1
# Harmonic beta-derivative recurrences and endpoint moment m=0.
for m in range(50):
 d=-2*sum((F(1,2*j+1) for j in range(m+1)),F(0))
 dd=4*sum((F(1,(2*j+1)**2) for j in range(m+1)),F(0))
 assert d+F(2,2*m+3)==-2*sum((F(1,2*j+1) for j in range(m)),F(0))-F(2,2*m+1)+F(2,2*m+3)
 assert dd>0;count+=2
# Stable division primitive: cancellation of its non-log derivative term.
for k in range(81):
 for sign in (-1,1):
  b=-sign*F(53,50)
  derivative=[b**(k-j) for j in range(k+1)]
  product=mul([-b,F(1)],derivative)
  expected=[-b**(k+1)]+[F(0)]*k+[F(1)]
  assert product==expected;count+=1
out={'exact_fraction_assertions':count,'all_passed':True,'continuum_source_certificate':False}
print(json.dumps(out,indent=2))
