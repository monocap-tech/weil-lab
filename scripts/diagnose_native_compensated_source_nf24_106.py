#!/usr/bin/env python3
"""NON-CERTIFYING Decimal Gauss diagnostic of the authenticated NF24
compensated source. No interval quadrature error is claimed.
Uses the original regular kernel directly, exact singular polynomial,
the endpoint log and original prime/pole actions.
"""
from decimal import Decimal as D,getcontext
from fractions import Fraction as F
from math import cos,pi,comb,factorial
import json,argparse
getcontext().prec=90
A=D(53)/50
def dec(q):
    q=F(q);return D(q.numerator)/D(q.denominator)

def gauss(n):
    out=[]
    for k in range(1,n+1):
        x=D(str(cos(pi*(k-.25)/(n+.5))))
        for it in range(20):
            p0=D(1);p1=x
            for j in range(2,n+1):p0,p1=p1,((2*j-1)*x*p1-(j-1)*p0)/j
            dp=n*(x*p1-p0)/(x*x-1)
            dx=p1/dp;x-=dx
            if abs(dx)<D('1e-85'):break
        assert abs(dx)<D('1e-80')
        out.append((x,2/((1-x*x)*dp*dp)))
    return out

def poly(p,x):
    y=D(0)
    for c in p[::-1]:y=y*x+c
    return y

def legendre(n):
    # Exact rational polynomial before normalized Decimal conversion.
    out=[F(0)]*(n+1)
    for k in range(n//2+1):
        out[n-2*k]=F((-1)**k*factorial(2*n-2*k),2**n*factorial(k)*factorial(n-k)*factorial(n-2*k))
    return out

def physical_poly(ids,coeff):
    out=[D(0)]*(max(ids)+1)
    for n,v in zip(ids,coeff):
        v=dec(v)*(D(2*n+1)/(2*A)).sqrt()
        for k,b in enumerate(legendre(n)):
            if b:out[k]+=v*dec(b)/A**k
    return out

def singular_poly(p):
    out=[D(0)]*len(p)
    for m,v in enumerate(p):
        if not v:continue
        out[m]+=v*sum((D(1)/k for k in range(1,m+1)),D(0))
        for j in range(1,m,2):out[m-1-j]-=v*A**(j+1)/D(j+1)
    return out

def integration(fun,l,u,nodes):
    mid=(l+u)/2;half=(u-l)/2
    return half*sum((w*fun(mid+half*t) for t,w in nodes),D(0))

def diagnose(targets,inner=96,outer=64):
    ni=gauss(inner);no=gauss(outer)
    # High precision analytic constants for NON-CERTIFYING evaluation.
    gamma=D('0.577215664901532860606512090082402431042159335939923598805767234884867726777664670936947063')
    piD=D('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825')
    c=-gamma-(2*piD).ln()
    powers=(2,3,4,5,7,8)
    shifts=[(s*D(n).ln(),D(2 if n in (4,8) else n).ln()/D(n).sqrt()) for n in powers for s in (-1,1)]
    cuts=sorted([-A,A]+[A-t if t>0 else -A-t for t,w in shifts])
    result=dict(certifying=False,decimal_precision=getcontext().prec,inner_order=inner,outer_order=outer)
    for row in targets['authenticated_compensated_targets']:
        ids=row['retained_indices']+row['high_indices'];coeff=row['retained_coefficients']+row['exact_rational_high_compensation']
        p=physical_poly(ids,coeff);sing=singular_poly(p)
        coords=[str((F(l)+F(u))/2) for l,u in row['low_source_coordinates']]
        low=physical_poly(row['retained_indices'],coords)
        mplus=integration(lambda y:(y/2).exp()*poly(p,y),-A,A,ni)
        mminus=integration(lambda y:(-y/2).exp()*poly(p,y),-A,A,ni)
        total=D(0);full=D(0)
        projected={k:D(0) for k in range(116 if row['parity']=='even' else 117,181,2)}
        for idx,(l,u) in enumerate(zip(cuts,cuts[1:])):
            mid=(l+u)/2;selected=[(t,w) for t,w in shifts if abs(mid+t)<A]
            def integrand(y):
                if idx==0:z=(u-l)*y**4;x=-A+z;left=z;right=2*A-z;jac=4*(u-l)*y**3
                elif idx==12:z=(u-l)*y**4;x=A-z;left=2*A-z;right=z;jac=4*(u-l)*y**3
                else:x=l+(u-l)*y;left=A+x;right=A-x;jac=u-l
                px=poly(p,x)
                def conv(T,s):
                    def f(t):
                        r=(-t/2).exp()/(1-(-2*t).exp())-1/(2*t)
                        return r*poly(p,x+s*t)
                    return integration(f,D(0),T,ni)
                arch=px*(c-(left*right).ln()/2)+poly(sing,x)-conv(left,-1)-conv(right,1)
                prime=-sum((w*poly(p,x+t) for t,w in selected),D(0))
                pole=(x/2).exp()*mminus+(-x/2).exp()*mplus
                source=arch+prime+pole
                residual=source-poly(low,x)
                return residual*residual*jac,source*source*jac,source*jac,x
            midY=D('.5');half=D('.5')
            for t,w in no:
                r,s,sj,x=integrand(midY+half*t)
                total+=half*w*r;full+=half*w*s
                p0=D(1);p1=x/A
                for k in range(2,181):
                    p0,p1=p1,((2*k-1)*x/A*p1-(k-1)*p0)/k
                    if k in projected:projected[k]+=half*w*sj*p1*(D(2*k+1)/(2*A)).sqrt()
        energy=dec((F(row['compensated_energy'][0])+F(row['compensated_energy'][1]))/2)
        result[row['parity']]=dict(physical_residual_square=str(total),complete_source_square=str(full),
            compensated_energy=str(energy),residual_square_over_energy=str(total/energy),
            residual_square_over_sufficient_threshold=str(total/(D('0.207')*energy)),
            projected_high_source={str(k):str(v) for k,v in projected.items()},
            projected_high_square_over_energy=str(sum((v*v for v in projected.values()),D(0))/energy))
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('targets');p.add_argument('--inner',type=int,default=96);p.add_argument('--outer',type=int,default=64)
    a=p.parse_args();print(json.dumps(diagnose(json.load(open(a.targets)),a.inner,a.outer),indent=2))
