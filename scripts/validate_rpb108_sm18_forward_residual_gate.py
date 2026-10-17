#!/usr/bin/env python3
"""SM18 exact-rational 2x2 forward-residual proof regression only.

No original supported 890-source inverse evaluation is performed. The
math identity and matrix inequality are verified with exact fractions;
W-ODD-NEG stays open.
"""
from fractions import Fraction as F

def tr(A):
    return [list(col) for col in zip(*A)]

def mm(A,B):
    assert len(A[0])==len(B)
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
             for j in range(len(B[0]))] for i in range(len(A))]

def plus(A,B):
    return [[a+b for a,b in zip(ra,rb)] for ra,rb in zip(A,B)]

def neg(A):
    return [[-x for x in row] for row in A]

def minus(A,B):
    return plus(A,neg(B))

def scale(A,c):
    return [[c*x for x in row] for row in A]

def is_spd2(A):
    return (len(A)==2 and len(A[0])==2 and A[0][1]==A[1][0]
            and A[0][0]>0 and A[0][0]*A[1][1]-A[0][1]**2>0)

def inv2(A):
    assert is_spd2(A)
    det=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return [[A[1][1]/det,-A[0][1]/det],
            [-A[1][0]/det,A[0][0]/det]]

def validate():
    # True prototype coercivity A >= 2I is exact-rational SPD.
    A=[[F(4),F(1)],[F(1),F(3)]]
    I=[[F(1),F(0)],[F(0),F(1)]]
    k=F(2)
    assert is_spd2(minus(A,scale(I,k)))
    U=I
    Y=[[F(1,4),F(0)],[F(0),F(1,3)]]
    E=minus(U,mm(A,Y))
    H=minus(plus(mm(tr(U),Y),mm(tr(Y),U)),mm(mm(tr(Y),A),Y))
    Q=mm(mm(tr(U),inv2(A)),U)
    exact=plus(H,mm(mm(tr(E),inv2(A)),E))
    assert Q==exact, "SM18 inverse residual IDENTITY failed"
    upper=plus(H,scale(mm(tr(E),E),F(1)/k))
    assert is_spd2(minus(upper,Q)), "SM18 upper error not Loewner-positive"
    Cinv=[[F(1),F(0)],[F(0),F(1,2)]]
    mu0=F(999,1000)
    margin=minus(scale(Cinv,mu0),upper)
    assert is_spd2(margin), "SM18 toy coupled gate not SPD"
    assert not is_spd2(minus(scale(Cinv,F(1,4)),upper)), (
        "SM18 intentionally insufficient threshold silently accepted")
    # Link the conditional full SM10 error margin by *exact* rational.
    kappastar=F(33621,10**9)
    eta=F(302,10**12)
    tau=F(1,1024)
    assert kappastar>0 and (1+tau)*mu0+eta/kappastar<1
    print("SM18 toy exact inverse",Q)
    print("SM18 forward residual",E)
    print("SM18 coupled rational margin",margin)
    print("SM18 PASS (EXACT TOY/CONDITIONAL): no original 890-source data")
    print("SM18 W-ODD-NEG and RH OPEN")

if __name__=="__main__":
    validate()
