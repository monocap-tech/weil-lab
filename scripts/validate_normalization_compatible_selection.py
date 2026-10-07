#!/usr/bin/env python3
"""Exact controls for physical transport and normalized eligible-row repair."""
from fractions import Fraction as F
from itertools import product
import json

def dot(x,y): return sum(a*b for a,b in zip(x,y))
def mv(a,x): return [dot(r,x) for r in a]
def tr(a): return list(map(list,zip(*a)))
def mm(a,b): return [[dot(r,c) for c in zip(*b)] for r in a]
def neg(x): return [-v for v in x]
def inv2(a):
    d=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    assert d
    return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]
def covariance(r,t):
    return [[r[0]**2,r[0]*r[1]],[r[0]*r[1],t*t+r[1]**2]]

def main():
    transport=mismatch=repair=blocked=passing=0
    rows=[(F(r),F(b)) for r,b in product((1,2,3),(-2,0,2))]
    for r1,r2,r3,t,p in product(rows,rows,rows,(F(1),F(2)),(F(1),F(3,2))):
        k=[p,F(0)]
        u=[-dot(r,k) for r in (r1,r2,r3)]
        gs=[inv2(covariance(r,t)) for r in (r1,r2,r3)]
        for r,g,v in zip((r1,r2,r3),gs,u):
            assert neg(mv(g,[r[0]*v,r[1]*v]))==k
            assert F(1)-dot(r,mv(g,r))==0
            # G energy equals selected energy for this actual-null control.
            assert dot(k,mv(covariance(r,t),k))==v*v
        j21=dot(r2,mv(gs[0],r1))
        j12=dot(r1,mv(gs[1],r2))
        j32=dot(r3,mv(gs[1],r2))
        j31=dot(r3,mv(gs[0],r1))
        assert j21*u[0]==u[1] and j12*j21==1
        assert j32*j21==j31
        assert neg(mv(gs[1],[r2[0]*j21*u[0],r2[1]*j21*u[0]]))==k
        assert (j21*j21==1)==(u[0]*u[0]==u[1]*u[1])
        if u[0]*u[0]!=u[1]*u[1]:
            assert 2*u[0]*u[0]!=2*u[1]*u[1]
            mismatch+=1
        transport+=1
    # Complete negative rows are a rational orthogonal basis.
    # A=0 on this two-dimensional K, complete positive rows are identical.
    for c,s in ((F(1),F(0)),(F(3,5),F(4,5)),(F(5,13),F(12,13))):
        r=[c,s]; b=[-s,c]; blind=[-s,c]
        assert dot(r,blind)==0 and dot(b,blind)==1
        assert mm(tr([r,b]),[r,b])==[[F(1),F(0)],[F(0),F(1)]]
        # k with nonzero retained selected coefficient; q is background sample.
        for p,q in product((F(1),F(2),F(-3)),(F(0),F(1),F(-2))):
            k=[p*c-q*s,p*s+q*c]
            assert dot(r,k)==p and dot(b,k)==q
            eligible=dot(b,k)==0
            restricted_injection=eligible and dot(b,blind)!=0
            # Exhaust all two possible disjoint finite additions.
            repairs=[]
            for add in (False,True):
                norm_preserved=(not add) or dot(b,k)==0
                separates=add and dot(b,blind)!=0
                if norm_preserved and separates: repairs.append(add)
                new_energy=p*p+(q*q if add else 0)
                assert (new_energy==p*p)==norm_preserved
                assert 2*new_energy==2*p*p+(2*q*q if add else 0)
            assert bool(repairs)==restricted_injection
            if eligible: passing+=1
            else:
                # All-row separation holds, but no normalized repair exists.
                assert not repairs and dot(b,blind)!=0
                blocked+=1
            repair+=1
    print(json.dumps(dict(status="rational_controls_pass",
        transport_cases=transport, metric_mismatch_cases=mismatch,
        repair_cases=repair, repair_passes=passing, repair_obstructions=blocked,
        scope="algebra controls; eligible actual-zeta injection unproved"),sort_keys=True))

if __name__=="__main__": main()
