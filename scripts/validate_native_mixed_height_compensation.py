"""Finite exact mixed-block controls; no analytic or actual-zeta certification."""
from fractions import Fraction as F
from pathlib import Path
import json
from certify_native_kernel_de_branges_attachment import g,add,sub,mul,conj,scale,abs2

count=0
def check(b):
    global count
    assert b
    count+=1
def total(xs):
    out=g()
    for x in xs:out=add(out,x)
    return out
def mv(M,v):return [total(mul(x,y) for x,y in zip(row,v)) for row in M]
def quadratic(M,c):return total(mul(mul(c[i],M[i][j]),conj(c[j])) for i in range(len(c)) for j in range(len(c)))

for r in range(1,6):
    a=[g(F(i+1,3),F((-1)**i,4)) for i in range(r)]
    b=a+[scale(x,-1) for x in a]
    M=[[mul(x,conj(y)) for y in b] for x in b]
    lam=sum(abs2(x) for x in b)
    check(lam==2*sum(abs2(x) for x in a))
    check(mv(M,b)==[scale(x,lam) for x in b])
    for i in range(2*r):
        for j in range(2*r):
            check(M[i][j]==conj(M[j][i]))
            check(mul(M[i][j],M[0][0])==mul(M[i][0],M[0][j]))
    for j in range(r):
        v=[g()]*(2*r);v[j]=g(1);v[r+j]=g(1)
        check(mv(M,v)==[g()]*(2*r))
        check(quadratic(M,v)==g())
        check(M[j][j]==M[r+j][r+j])
        check(M[j][r+j]==scale(M[j][j],-1))
    for seed in range(1,7):
        c=[g(F(seed+i,7),F(seed-i,5)) for i in range(2*r)]
        amplitude=total(mul(c[i],b[i]) for i in range(2*r))
        check(quadratic(M,c)==g(abs2(amplitude)))
        check(abs2(amplitude)>=0)
    # Native shifted Gram: source = energy Gram + mu physical Gram.
    mass=[[g(int(i==j)+1) for j in range(2*r)] for i in range(2*r)]
    energy=[[g(int(i==j and i>=r)) for j in range(2*r)] for i in range(2*r)]
    for mu in [F(0),F(1,3),F(2)]:
        source=[[add(energy[i][j],scale(mass[i][j],mu)) for j in range(2*r)] for i in range(2*r)]
        for i in range(r):
            for j in range(r,2*r):
                check(source[i][j]==scale(mass[i][j],mu))
                check(sub(source[i][j],scale(mass[i][j],mu))==g())

out={"passed":True,"exact_checks":count,"scope":"finite Gaussian-rational rank-one and shifted Gram algebra only","analytic_certification":False,"actual_zeta_nodes_computed":False,"lean_certification":False,"F4_closed":False}
Path('notes/data/RPB108_MIXED_HEIGHT_COMPENSATION_VALIDATION_20261007.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
