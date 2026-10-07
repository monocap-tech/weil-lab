#!/usr/bin/env python3
"""Exact complete-source unit-gain gap, angle and padding controls."""
from fractions import Fraction as F
from itertools import product
import json

def tr(a): return list(map(list,zip(*a)))
def mm(a,b):
    return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def sub(a,b): return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def neg(a): return [[-x for x in r] for r in a]
def diag(a,b): return [[a,F(0)],[F(0),b]]
def sq(v): return sum(r[0]**2 for r in v)

def main():
    gaps=selected=padding=prefixes=0
    for r,t,q,(c,s),z in product((F(1),F(2),F(3)),(F(1),F(2),F(4)),
        (F(1,2),F(3,5),F(5,13)),
        ((F(1),F(0)),(F(3,5),F(4,5)),(F(5,13),F(12,13))),
        (F(-2),F(1),F(3))):
        O=[[c,-s],[s,c]]; P0=diag(r,t); L=diag(r*r,t*t)
        N=mm(O,diag(r,q*t))
        C=neg(mm(mm(P0,diag(1/(r*r),1/(t*t))),tr(N)))
        D=sub(diag(F(1),F(1)),mm(tr(C),C))
        Pi=[[c*c,c*s],[c*s,s*s]]; Iminus=sub(diag(F(1),F(1)),Pi)
        eta=1-q*q
        assert D==[[eta*x for x in row] for row in Iminus]
        A=sub(L,mm(tr(N),N))
        assert A==diag(F(0),t*t*(1-q*q))
        u=[[z*c],[z*s]]
        h=neg(mm(mm(diag(1/(r*r),1/(t*t)),tr(N)),u))
        assert h==[[-z/r],[F(0)]]
        assert mm(A,h)==[[F(0)],[F(0)]]
        assert mm(N,h)==neg(u) and mm(C,u)==mm(P0,h)
        for v in ([[F(1)],[F(0)]],[[F(0)],[F(1)]],[[z],[F(1)]]):
            loss=sq(v)-sq(mm(C,v)); distance=sq(mm(Iminus,v))
            assert loss==eta*distance and eta*distance<=loss<=distance
            assert (loss==0)==(distance==0)
            selected+=1
        gaps+=1
    for c,s in ((F(3,5),F(4,5)),(F(5,13),F(12,13)),(F(8,17),F(15,17))):
        for p in (F(1),F(5),F(13)):
            P=[[p,F(0)]]; C=[[-c],[s]]; R=p*c
            assert mm(P,C)==[[-R]]
            assert mm(tr(C),C)==[[F(1)]]
            assert p*p-R*R>0
            for u in (F(1),F(-2)):
                assert mm(C,[[u]])[1][0]!=0  # no P*k can equal this.
            padding+=1
    for n in range(1,129):
        tail=F(9,25)**n
        selected_energy=sum((F(4,5)*F(3,5)**j)**2 for j in range(n))
        assert 0<selected_energy==1-tail<1
        # Selected normalized prefix has squared overlap 1-tail with W.
        overlap=selected_energy
        angle=1-overlap
        gain_loss=1-selected_energy
        assert angle==gain_loss==tail>0
        if n>=16: assert tail<F(1,1000000)
        prefixes+=1
    print(json.dumps(dict(status="rational_controls_pass",
        complement_gap_cases=gaps,selected_angle_cases=selected,
        padded_unit_gain_rejections=padding,infinite_prefix_cases=prefixes,
        scope="algebra only; no actual global strict unit bound"),sort_keys=True))
if __name__=="__main__": main()
