#!/usr/bin/env python3
"""Exact finite controls; no actual source selection or contact is computed."""
from fractions import Fraction as F
import json

def inv(m):
    a,b,c,d=m[0][0],m[0][1],m[1][0],m[1][1]
    det=a*d-b*c
    assert det>0
    return ((d/det,-b/det),(-c/det,a/det))
def mv(m,v): return tuple(sum(x*y for x,y in zip(row,v)) for row in m)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def quad(m,v): return dot(v,mv(m,v))

def main():
    matrices=residuals=padding=0
    for r in (F(1,2),F(1),F(2)):
        for q in (F(-1),F(0),F(1)):
            for t in (F(0),F(1,2),F(1)):
                for z in (F(-1),F(0),F(1)):
                    R,T=(r,q),(t,z)
                    G=((r*r,r*q),(r*q,1+q*q))
                    Gi=inv(G)
                    Gp=tuple(tuple(G[i][j]+T[i]*T[j] for j in range(2)) for i in range(2))
                    Gpi=inv(Gp)
                    B=dot(R,mv(Gi,T)); J=1+dot(T,mv(Gi,T))
                    assert B==t/r and J>=1
                    Dp=((1-quad(Gpi,R),-dot(R,mv(Gpi,T))),
                        (-dot(T,mv(Gpi,R)),1-quad(Gpi,T)))
                    assert Dp==((B*B/J,-B/J),(-B/J,1/J))
                    u=-r; up=(u,B*u)
                    assert up==(-r,-t) and mv(Dp,up)==(0,0)
                    rhs=tuple(R[i]*up[0]+T[i]*up[1] for i in range(2))
                    assert tuple(-x for x in mv(Gpi,rhs))==(1,0)
                    assert quad(Dp,(u,F(0)))==t*t/J
                    if t: assert quad(Dp,(u,F(0)))>0
                    matrices+=1
                    for v in ((F(1),F(0)),(F(0),F(1)),(F(1),F(-1))):
                        e,ep=quad(Gi,v),quad(Gpi,v)
                        correction=dot(T,mv(Gi,v))**2/J
                        assert e-ep==correction
                        assert e/J<=ep<=e
                        residuals+=1
    # Singular old G: h=(1,1) and h+(0,d) share old coefficients.
    for d in (F(-2),F(0),F(3)):
        h=(F(1),F(1)+d)
        old=-h[0]
        new=(old,-h[1])
        assert old==-1 and new[0]==old
        assert dot(new,new)==old*old+h[1]*h[1]
        padding+=1
    assert F(2)*(F(1)**2+F(1)**2)==4  # New neutral total mass, formerly 2.
    print(json.dumps({'status':'rational_controls_pass','schur_matrix_cases':matrices,
                      'inverse_gain_cases':residuals,'blind_kernel_cases':padding,
                      'scope':'algebra controls; no actual arithmetic contact or Lean certification'},sort_keys=True))

if __name__=='__main__': main()
