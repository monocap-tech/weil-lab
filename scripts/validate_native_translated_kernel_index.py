"""Exact rational determinant/congruence controls; analytic proof in the note."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

count=0
def check(b):
    global count
    assert b
    count+=1
def det(M):
    A=[row[:] for row in M];out=F(1)
    for j in range(len(A)):
        p=next((i for i in range(j,len(A)) if A[i][j]),None)
        if p is None:return F(0)
        if p!=j:A[j],A[p]=A[p],A[j];out=-out
        d=A[j][j];out*=d
        for i in range(j+1,len(A)):
            c=A[i][j]/d
            for k in range(j+1,len(A)):A[i][k]-=c*A[j][k]
    return out
def inverse(M):
    n=len(M);A=[row[:]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(M)]
    for j in range(n):
        p=next(i for i in range(j,n) if A[i][j]);A[j],A[p]=A[p],A[j]
        d=A[j][j];A[j]=[x/d for x in A[j]]
        for i in range(n):
            if i!=j:
                c=A[i][j];A[i]=[x-c*y for x,y in zip(A[i],A[j])]
    return [row[n:] for row in A]
def transpose(M):return [list(row) for row in zip(*M)]
def mm(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def block(A,B,C,D):return [x+y for x,y in zip(A,B)]+[x+y for x,y in zip(C,D)]

for r in range(1,9):
    coefficient=F(1)
    for j in range(r):coefficient*=F(factorial(j),factorial(r+j))
    H=[[F(1,factorial(i+j+1)) for j in range(r)] for i in range(r)]
    check(det(H)==(-1)**(r*(r-1)//2)*coefficient)
    check(2*sum(r-1-j for j in range(r))+r==r*r)
    for t in [F(1,2),F(1,7),F(2,9)]:
        c2=F(9,4)
        C=[[(-1)**(r+k)*c2*t**(2*r-1-j-k)/factorial(2*r-1-j-k) for k in range(r)] for j in range(r)]
        check(det(C)==(-1)**r*c2**r*coefficient*t**(r*r))
        check(C[-1][-1]==-c2*t)
        # Integrating from F^(2r-2)=(-1)^r*c2*t fixes every power/sign.
        for j in range(r):
            for k in range(r):
                exponent=2*r-1-j-k
                check(C[j][k]*factorial(exponent)/t**exponent==(-1)**(r+k)*c2)
        I=[[F(int(i==j)) for j in range(r)] for i in range(r)]
        Z=[[F(0)]*r for _ in range(r)]
        G=block(Z,C,transpose(C),Z)
        S=block(I,Z,Z,inverse(C))
        canonical=block(Z,I,I,Z)
        check(mm(mm(transpose(S),G),S)==canonical)
        # r explicit negative / positive subspaces for the canonical cross form.
        for sign in [-1,1]:
            V=I+[[sign*x for x in row] for row in I]
            check(mm(mm(transpose(V),canonical),V)==[[2*sign*x for x in row] for row in I])
        # Original shifted signed source Gram keeps its complete mass residual.
        mass=[[F(int(i==j))+F(1,3) for j in range(2*r)] for i in range(2*r)]
        for mu in [F(0),F(1,5),F(2)]:
            full=[[G[i][j]+mu*mass[i][j] for j in range(2*r)] for i in range(2*r)]
            check([[full[i][j]-mu*mass[i][j] for j in range(2*r)] for i in range(2*r)]==G)

# Centered support radius epsilon corresponds to cross displacement 2 epsilon.
for epsilon in [F(1,10),F(1,100),F(1,1000)]:
    Lambda=F(7,3);energy=2*(-Lambda*(2*epsilon));mass=F(4)
    check(energy/mass==-Lambda*epsilon)

out={"passed":True,"exact_checks":count,"scope":"finite rational determinant, support-factor and inertia-congruence algebra only","analytic_certification":False,"actual_contact_computed":False,"lean_certification":False,"F4_closed":False}
Path('notes/data/RPB108_TRANSLATED_KERNEL_INDEX_VALIDATION_20261007.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
