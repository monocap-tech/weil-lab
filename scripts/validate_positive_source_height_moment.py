#!/usr/bin/env python3
"""Exact source derivative/translation pair algebra and height-tail controls."""
from fractions import Fraction as F
from itertools import product
import json

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def scale(s,a): return (s*a[0],s*a[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def sq(a): return a[0]*a[0]+a[1]*a[1]
def pair(fbar,fz): return (scale(F(1,2),add(fbar,fz)),scale(F(1,2),sub(fbar,fz)))

def main():
    derivative=translation=budgets=tail=borderline=0
    values=[(F(1),F(0)),(F(-2),F(3)),(F(4,5),F(-3,5))]
    for fb,fz,theta,beta in product(values,values,(F(-3),F(0),F(5)),
        (F(-1,2),F(0),F(1,4))):
        p,n=pair(fb,fz)
        # F_h'(z)=-iz F_h(z): z=theta+i beta.
        dp,dn=pair(mul((-beta,-theta),fb),mul((beta,-theta),fz))
        assert dp==sub(mul((F(0),-theta),p),scale(beta,n))
        assert dn==sub(mul((F(0),-theta),n),scale(beta,p))
        assert scale(theta,p)==mul((F(0),F(1)),add(dp,scale(beta,n)))
        derivative+=1
    for fb,fz,r,phase in product(values,values,(F(1,2),F(1),F(2)),
        ((F(1),F(0)),(F(3,5),F(4,5)),(F(5,13),F(-12,13)))):
        p,n=pair(fb,fz)
        ch=(r+1/r)/2; sh=(r-1/r)/2
        # r=exp(beta*t); phase=exp(i theta*t); algebra only.
        tp,tn=pair(mul(phase,scale(r,fb)),mul(phase,scale(1/r,fz)))
        assert tp==mul(phase,add(scale(ch,p),scale(sh,n)))
        assert tn==mul(phase,add(scale(ch,n),scale(sh,p)))
        assert ch*ch-sh*sh==1 and sq(phase)==1
        translation+=1
    for x,y,z in product((F(0),F(1),F(3)),repeat=3):
        assert (x+y+z)**2<=3*(x*x+y*y+z*z)
        budgets+=1
    for n in range(1,129):
        p=[F(4,5)*F(3,5)**j for j in range(n)]
        theta=[F(5,3)**j for j in range(n)]
        energy=sum(a*a for a in p)
        moment=sum(t*t*a*a for t,a in zip(theta,p))
        assert energy+F(9,25)**n==1
        assert moment==F(16,25)*n
        # Negative sequence e0 has full energy one and finite support.
        assert energy<1 and 1-energy>0
        tail+=1
        # Dyadic borderline moment blocks stay constant; stricter blocks sum.
        assert sum(F(1) for j in range(n))==n
        assert sum(F(1,2)**(j+1) for j in range(n))<1
        if n>1:
            assert sum(F(1,j*j) for j in range(n+1,2*n+1))<=F(1,n)
        borderline+=1
    print(json.dumps(dict(status="rational_controls_pass",
        derivative_pair_cases=derivative,translation_pair_cases=translation,
        square_budgets=budgets,height_moment_tail_cases=tail,
        borderline_rate_cases=borderline,
        scope="source algebra and tail controls; no actual arithmetic moment estimate"),
        sort_keys=True))

if __name__=="__main__": main()
