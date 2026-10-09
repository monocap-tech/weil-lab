#!/usr/bin/env python3
"""DNE10 exact-rational full-high rank-one pole-transfer controls.

Two low and two high modes are abstract controls, not an actual Weil source.
Checks the parity signs, complete high inverse, Schur response, residual
transfer, and a source-invisible extra high coordinate.
"""
from fractions import Fraction as F
from itertools import product
import json

def dot(x,y):
    return sum((a*b for a,b in zip(x,y)), F(0))

def mv(A,x):
    return [dot(row,x) for row in A]

def inv2(A):
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    assert d>0
    return [[A[1][1]/d,-A[0][1]/d],
            [-A[1][0]/d,A[0][0]/d]]

def add(x,y):
    return [a+b for a,b in zip(x,y)]

def scale(c,x):
    return [c*a for a in x]

def qblock(A,B,C,x,y):
    # B is high x low (2x2).
    return dot(x,mv(A,x))+2*dot(y,mv(B,x))+dot(y,mv(C,y))

def run():
    checks=0
    def ck(value):
        nonlocal checks
        assert value
        checks+=1

    A=[[F(5),F(1,2)],[F(1,2),F(6)]]
    B=[[F(1,4),F(1,3)],[F(-1,5),F(2,7)]]
    C=[[F(2),F(1,4)],[F(1,4),F(3)]]
    inv=inv2(C)
    mE=[F(1),F(-1,2)]

    for sig in (F(1),F(-1)):
        for mF in ([F(0),F(0)],[F(1,10),F(1,12)]):
            vm=mv(inv,mF)
            beta=dot(mF,vm)
            den=1-sig*2*beta
            ck(den>0)
            ck(beta>=0)
            for x0,x1 in product(range(-2,3),repeat=2):
                x=[F(x0),F(x1)]
                bx=mv(B,x)
                tQ=scale(F(-1),mv(inv,bx))
                alpha=dot(mE,x)+dot(mF,tQ)
                tH=add(tQ,scale(sig*2*alpha/den,vm))
                cH=[[C[i][j]-sig*2*mF[i]*mF[j]
                     for j in range(2)] for i in range(2)]
                bH=[bx[i]-sig*2*dot(mE,x)*mF[i]
                    for i in range(2)]
                ck(add(mv(cH,tH),bH)==[F(0),F(0)])
                SQ=qblock(A,B,C,x,tQ)
                SH=qblock(A,B,C,x,tH)
                momentH=dot(mE,x)+dot(mF,tH)
                SH-=sig*2*momentH**2
                ck(SH==SQ-sig*2*alpha**2/den)
                ck(momentH==alpha/den)
                ck(tH==add(tQ,scale(sig*2*alpha/den,vm)))
                for weight in (F(0),F(1,2),F(1)):
                    y=scale(weight,tQ)
                    mw=dot(mE,x)+dot(mF,y)
                    rQ=add(bx,mv(C,y))
                    rH=add(rQ,scale(-sig*2*mw,mF))
                    predicted=add(bH,mv(cH,y))
                    ck(rH==predicted)
                    # full signed-minus-pole identity on all tested y
                    ck(qblock(A,B,C,x,y)-sig*2*mw**2 ==
                       dot(x,mv(A,x))+2*dot(y,bH)
                       -sig*2*dot(mE,x)**2+dot(y,mv(cH,y)))
            # relative high-tail bound: test normalized v in source controls
            ck(beta <= F(1000,207)*dot(mF,mF))
    # Additional unmeasured high coordinate can create a hidden null:
    # E=R, high C=identity on R²; only first high mixed entry measured zero.
    for t in (F(0),F(1,4),F(1,2)):
        low=F(1,16)
        source=[F(0),t]
        true_schur=low-dot(source,source)
        ck(low>0)
        ck(source[0]==0)
        ck(true_schur==low-t*t)
        if t==F(1,4):
            ck(true_schur==0)
    return {
       "stage":"DNE10 full-high signed Q/pole-free H bridge",
       "all_passed":True,
       "exact_fraction_checks":checks,
       "real_Weil_residual_computed":False,
       "physical_pole_profile_tail":"<1e-150 (analytic Taylor bound)",
       "full_high_source_G_to_H_transfer":True,
       "original_first_two_high_columns_sufficient":False,
       "contact_excluded":False,
       "RH_proved":False,
       "lean_certified":False,
    }

if __name__=="__main__":
    print(json.dumps(run(),indent=2))
