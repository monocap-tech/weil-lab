"""Finite exact physical-mass controls; no analytic/actual-node certification."""
from fractions import Fraction as F
from pathlib import Path
import json

count=0
def check(b):
    global count
    assert b
    count+=1
def mv(A,v):return [sum(x*y for x,y in zip(row,v)) for row in A]
def q(A,v):return sum(x*y for x,y in zip(v,mv(A,v)))
def det2(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]

# Independent rational positive Fourier measures: exact truncated layer cake.
nodes=[F(0),F(1,2),F(-2),F(3),F(-7),F(11)]
mass=[F(1,3),F(2,5),F(1,7),F(3,8),F(1,11),F(2,13)]
for R in [F(1),F(2),F(5),F(10),F(20)]:
    head=sum(x*x*v for x,v in zip(nodes,mass) if abs(x)<=R)
    layer=sum(min(x*x,R*R)*v for x,v in zip(nodes,mass))
    check(head<=layer)
    check(layer==head+R*R*sum(v for x,v in zip(nodes,mass) if abs(x)>R))
    # Cosine lower-band budget and logarithmic upper-band division are separate.
    for alpha in [F(1,3),F(3,4),F(9,10)]:
        check(2-alpha>1)
        check(alpha<1)

# Synthetic dyadic physical tail model, clearly not actual Fourier data.
for n in range(2,65):
    H=sum(F(2**j,j) for j in range(1,n+1))
    check(H<=F(8*2**n,n))
    V=sum(F(1,j*2**j) for j in range(n+1,129))
    check(V<=F(1,n*2**n))

# Exact mass-normalized compression, with independent rational small remainders.
for k in range(4,45):
    t=F(1,2**k);L=F(k);c2=F(9,4);m=F(3,2)
    C=-c2*t*(1+F(1,k*k));D=c2*t/L*(1-F(1,2*k));R=m-D
    check(D>0 and 2*m-D>0)
    Q=[[F(0),C],[C,F(0)]];M=[[m,R],[R,m]]
    sumv=[F(1),F(1)];diff=[F(1),F(-1)]
    ls=C/(2*m-D);ld=-C/D
    check(q(Q,sumv)==2*C)
    check(q(Q,diff)==-2*C)
    check(q(M,sumv)==2*(2*m-D))
    check(q(M,diff)==2*D)
    check(mv(Q,sumv)==[ls*x for x in mv(M,sumv)])
    check(mv(Q,diff)==[ld*x for x in mv(M,diff)])
    check(ls<0 and ld>0)
    check(ld/L==(1+F(1,k*k))/(1-F(1,2*k)))
    for mu in [F(0),F(1,5),F(3)]:
        original=[[Q[i][j]+mu*M[i][j] for j in range(2)] for i in range(2)]
        for value in [mu+ls,mu+ld]:
            check(det2([[original[i][j]-value*M[i][j] for j in range(2)] for i in range(2)])==0)

out={"passed":True,"exact_checks":count,"scope":"finite rational mass/compression algebra and explicitly synthetic tail controls","analytic_certification":False,"actual_fourier_nodes_computed":False,"lean_certification":False,"F4_closed":False}
Path('notes/data/RPB108_PHYSICAL_TRANSLATION_SCALE_VALIDATION_20261007.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
