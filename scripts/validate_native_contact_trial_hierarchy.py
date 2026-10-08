"""Finite rational polynomial/Schur checks; no analytic or actual kernel certification."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

count=0
def check(b):
    global count
    assert b
    count+=1
def tr(M):return [list(x) for x in zip(*M)]
def mm(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def inv(M):
    n=len(M);A=[row[:]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(M)]
    for j in range(n):
        p=next(i for i in range(j,n) if A[i][j]);A[j],A[p]=A[p],A[j]
        d=A[j][j];A[j]=[x/d for x in A[j]]
        for i in range(n):
            if i!=j:
                d=A[i][j];A[i]=[x-d*y for x,y in zip(A[i],A[j])]
    return [row[n:] for row in A]
def det(M):
    A=[row[:] for row in M];out=F(1)
    for j in range(len(A)):
        p=next((i for i in range(j,len(A)) if A[i][j]),None)
        if p is None:return F(0)
        if p!=j:A[j],A[p]=A[p],A[j];out=-out
        d=A[j][j];out*=d
        for i in range(j+1,len(A)):
            s=A[i][j]/d
            for k in range(j+1,len(A)):A[i][k]-=s*A[j][k]
    return out
def scale(M,c):return [[c*x for x in row] for row in M]
def add(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def quadratic(M,x):return sum(x[i]*M[i][j]*x[j] for i in range(len(x)) for j in range(len(x)))

for r in range(1,9):
    n=[r-1-j for j in range(r)]
    U=[[F(1,factorial(n[j])*factorial(n[k])*(n[j]+n[k]+1)) for k in range(r)] for j in range(r)]
    H=[[(-1)**(j+k)*U[j][k] for k in range(r)] for j in range(r)]
    A=[[F((-1)**(r+k),factorial(n[j]+n[k]+1)) for k in range(r)] for j in range(r)]
    for size in range(1,r+1):
        check(det([row[:size] for row in U[:size]])>0)
        check(det([row[:size] for row in H[:size]])>0)
    check(mm(mm(A,inv(H)),tr(A))==U)
    for j in range(r):
        for k in range(r):
            m=n[j]+n[k]+1
            s=sum(F((-1)**q,factorial(q)*factorial(m-q)) for q in range(n[j]+1))
            check(s==F((-1)**n[j],m*factorial(n[j])*factorial(n[k])))
    for t in [F(1,3),F(1,11),F(2,15)]:
        c2=F(9,4)
        C=[[c2*t*t**n[j]*A[j][k]*t**n[k] for k in range(r)] for j in range(r)]
        T=[[F(0) if k<j else (-t)**(k-j)/factorial(k-j) for k in range(r)] for j in range(r)]
        TC=mm(T,C);B=scale(add(TC,tr(TC)),-1)
        expectedB=[[2*c2*t*t**n[j]*H[j][k]*t**n[k] for k in range(r)] for j in range(r)]
        check(B==expectedB)
        E=scale(mm(mm(C,inv(B)),tr(C)),-1)
        expectedE=[[-c2*t/F(2)*t**n[j]*U[j][k]*t**n[k] for k in range(r)] for j in range(r)]
        check(E==expectedE)
        for size in range(1,r+1):check(det([row[:size] for row in scale(E,-1)[:size]])>0)
        x=[F(j+1,j+2) for j in range(r)]
        y=[-v[0] for v in mm(mm(inv(B),tr(C)),[[a] for a in x])]
        mixed=sum(x[j]*C[j][k]*y[k] for j in range(r) for k in range(r))
        check(2*mixed+quadratic(B,y)==quadratic(E,x))
        check(quadratic(E,x)<0)
        # Synthetic leading mass matrix: exact normalized positive level L.
        for L in [F(7),F(23)]:
            massR=scale(B,1/L)
            check(scale(massR,L)==B)
            for mu in [F(0),F(1,5),F(2)]:
                sourceR=add(B,scale(massR,mu))
                check(add(sourceR,scale(massR,-mu))==B)
    check(sorted([2*v+1 for v in n])==list(range(1,2*r,2)))

out={"passed":True,"exact_checks":count,"dimensions_checked":list(range(1,9)),"scope":"finite exact polynomial Gram and Schur algebra only; mass model is synthetic leading algebra","analytic_certification":False,"actual_kernel_computed":False,"lean_certification":False,"F4_closed":False}
Path('notes/data/RPB108_CONTACT_TRIAL_HIERARCHY_VALIDATION_20261007.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
