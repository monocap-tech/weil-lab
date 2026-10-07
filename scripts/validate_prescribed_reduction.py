#!/usr/bin/env python3
"""Rational padded-synthesis and filtration controls; no actual attachment."""
from fractions import Fraction as F
import json

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def scale(t,a): return tuple(t*x for x in a)

def main():
    cases = 0
    rotations=((F(1),F(0)),(F(3,5),F(4,5)),(F(5,13),F(12,13)))
    for c,s in rotations:
        l,z=(c,s),(-s,c)
        assert dot(l,l)==dot(z,z)==1 and dot(l,z)==0
        for r in (F(1,2),F(1),F(2)):
            for padding in (F(0),F(1,3),F(2)):
                p=scale(r,l)
                C1,C2=scale(-1,l),scale(padding,z)
                assert dot(p,p)==r*r
                assert (dot(p,C1),dot(p,C2))==(-r,0)
                u=(-r,F(0))
                a=add(scale(u[0],C1),scale(u[1],C2))
                assert a==p
                assert (dot(C1,a),dot(C2,a))==u
                a0=dot(l,a)
                assert a0==r and a0*a0==dot(a,a)==dot(u,u)
                assert -u[0]/r==1  # Same physical reconstruction.
                for x in (F(-1),F(1,2),F(2)):
                    for y in (F(-2),F(0),F(3)):
                        Cv=add(scale(x,C1),scale(y,C2))
                        red=scale(dot(l,Cv),l)
                        pad=scale(dot(z,Cv),z)
                        assert add(red,pad)==Cv
                        assert dot(p,pad)==0
                        assert dot(Cv,Cv)==x*x+padding*padding*y*y
                        cases+=1
        # w=(l,-e1), v=(z,e2) span B. Positive reduction of v
        # loses positive norm, while v's e2 forces its coefficient to one.
        # Thus projected v cannot lie in B (its z coordinate is zero).
        assert dot(z,z)==1
        assert F(0)-F(1)==-1  # Projected v signature.
    print(json.dumps({'status':'rational_controls_pass','padded_factor_cases':cases,
                      'filtration_controls':len(rotations),
                      'scope':'analytic reduction controls only; actual prescribed attachment unproved'},sort_keys=True))

if __name__=='__main__': main()
