"""Exact finite resolvent/gap controls; no analytic or actual spectral certification."""
from fractions import Fraction as F
from pathlib import Path
import json

count=0
def check(b):
    global count
    assert b
    count+=1
def inv(M):
    n=len(M);A=[row[:]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(M)]
    for j in range(n):
        p=next(i for i in range(j,n) if A[i][j]);A[j],A[p]=A[p],A[j]
        d=A[j][j];A[j]=[x/d for x in A[j]]
        for i in range(n):
            if i!=j:
                d=A[i][j];A[i]=[x-d*y for x,y in zip(A[i],A[j])]
    return [row[n:] for row in A]
def mm(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def add(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(A,c):return [[c*x for x in row] for row in A]
def diag(xs):return [[xs[i] if i==j else F(0) for j in range(len(xs))] for i in range(len(xs))]

# Noncommuting finite positive form/mass matrices: mass shift is not beta I.
J=diag([F(1),F(1,2),F(1,3)])
M=mm(J,J)
A=[[F(2),F(1,3),F(1,7)],[F(1,3),F(3),F(1,5)],[F(1,7),F(1,5),F(4)]]
for beta in [F(2),F(7),F(19)]:
    B=add(A,scale(M,beta));Bi=inv(B)
    check(B!=add(A,scale(diag([F(1)]*3),beta)))
    physicalR=mm(mm(J,Bi),J)
    physicalL=mm(mm(inv(J),A),inv(J))
    check(mm(add(physicalL,scale(diag([F(1)]*3),beta)),physicalR)==diag([F(1)]*3))
    for eps in [F(1,10),F(1,100),F(1,1000)]:
        change=[[eps*F(i+j+1,11) for j in range(3)] for i in range(3)]
        newB=add(B,change);newBi=inv(newB)
        check(add(newBi,scale(Bi,-1))==scale(mm(mm(newBi,change),Bi),-1))
        newR=mm(mm(J,newBi),J)
        check(add(newR,scale(physicalR,-1))==scale(mm(mm(mm(mm(J,newBi),change),Bi),J),-1))

# Independent diagonal cluster controls, not computed actual eigenvalues.
for r in range(1,9):
    beta=F(5);delta=F(2,3)
    old=[F(0)]*r+[delta,2*delta,3*delta]
    for eps in [F(1,100),F(1,1000),F(1,10000)]:
        new=[-eps**(2*j+1) for j in range(r)]+[delta-eps,2*delta-eps,3*delta-eps]
        check(sum(x<0 for x in new)==r)
        check(all(x!=0 for x in new))
        check(new[r]>=delta/2)
        oldR=[1/(beta+x) for x in old];newR=[1/(beta+x) for x in new]
        norm=max(abs(x-y) for x,y in zip(oldR,newR))
        gap=1/beta-1/(beta+delta)
        check(norm<gap/3)
        check(sum(x>1/beta for x in newR)==r)
        # Relative positive-level opening need not yield negative original energy.
        mu=F(1,4);original=[mu+x for x in new]
        check(all(0<x<mu for x in original[:r]))
        check(all(x>mu for x in original[r:]))
        residual=diag(new[:r]);mass=diag([F(1)]*r)
        source=add(residual,scale(mass,mu))
        check(add(source,scale(mass,-mu))==residual)

out={"passed":True,"exact_checks":count,"scope":"finite exact mass-resolvent identities and explicitly synthetic isolated-cluster controls","analytic_certification":False,"actual_native_eigenvalues_computed":False,"lean_certification":False,"F4_closed":False}
Path('notes/data/RPB108_FULL_CONTACT_CLUSTER_VALIDATION_20261007.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
