#!/usr/bin/env python3
"""NF22 NON-CERTIFYING numerical diagnostic for the COMPLETE original
physical Weil source on the first two Legendre modes at a=53/50.

The source includes archimedean kernel, all six original prime powers in
both directions, and signed Hermitian poles. Uses SciPy quadrature and
double precision: output is NOT an interval proof of cross terms or P2.
See certify_native_arch_source_square_nf22_106.py for rigorous arch
squares and the NF21 exact producer for prime+pole squared sectors.
"""
import math,json
from fractions import Fraction as F
from math import comb,factorial
import numpy as np
from scipy.integrate import quad,IntegrationWarning
from scipy.special import digamma
import warnings
a=53/50;N=320
h=[]
for n in range(N+1):
    v=F(1,2**n*factorial(n))
    for k in range(1,n//2+1):
        v-=F(2,factorial(2*k+1))*h[n-2*k]
    h.append(v/2)
coeff=np.array([0.,.5]+[float(h[k]/(k+1)) for k in range(1,N+1)])
C0=1/math.sqrt(2*a);C1=math.sqrt(3/(2*a))/a
alpha=float(digamma(.25)-math.log(math.pi))
active=(2,3,4,5,7,8)
weights={n:math.log(2 if n in (4,8) else n)/math.sqrt(n) for n in active}
sh=math.sinh(a/2);ch=math.cosh(a/2)
m0=4*sh*C0;m1=(4*ch-8*sh/a)*math.sqrt(3/(2*a))
def F_regular(t):return np.polynomial.polynomial.polyval(t,coeff)
def J(t):
    u=math.exp(-t/2)
    return math.atanh(u)+math.atan(u)
def arch(x,p):
    H=alpha+J(a-x)+J(a+x)
    return C0*H if p==0 else C1*(x*H+F_regular(a+x)-F_regular(a-x))
def prime(x,p):
    z=0.
    for n in active:
        t=math.log(n)
        if abs(x+t)<a:z+=weights[n]*(C0 if p==0 else C1*(x+t))
        if abs(x-t)<a:z+=weights[n]*(C0 if p==0 else C1*(x-t))
    return -z
def pole(x,p):
    return 2*m0*math.cosh(x/2) if p==0 else -2*m1*math.sinh(x/2)
pieces={'arch':arch,'prime':prime,'pole':pole}
cutpoints=[-a,a]
for n in active:
    t=math.log(n)
    for x in (-a+t,a-t,-a-t,a+t):
        if -a<x<a:cutpoints.append(x)
cutpoints=sorted(set(cutpoints))
def integral(fun):
    total=0.;error=0.
    for l,u in zip(cutpoints[:-1],cutpoints[1:]):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore',IntegrationWarning)
            value,e=quad(fun,l,u,epsabs=1e-10,epsrel=1e-10,limit=200)
        total+=value;error+=e
    return [total,error]
def diagnose():
    out={'aperture':'53/50','support_cells':len(cutpoints)-1,
         'certifying_source_square':False,'method':'nonrigorous SciPy sanity integration'}
    for p in (0,1):
        d={}
        for k,f in pieces.items():
            d[k+'2']=integral(lambda x:f(x,p)**2)
        for x,y in [('arch','prime'),('arch','pole'),('prime','pole')]:
            d['2*'+x+'*'+y]=integral(lambda t:2*pieces[x](t,p)*pieces[y](t,p))
        d['complete_source_squared']=integral(lambda x:sum(f(x,p) for f in pieces.values())**2)
        d['native_form_diagonal_via_source']=integral(lambda x:
           (C0 if p==0 else C1*x)*sum(f(x,p) for f in pieces.values()))
        out['even' if p==0 else 'odd']=d
    return out
if __name__=='__main__':print(json.dumps(diagnose(),indent=2))
