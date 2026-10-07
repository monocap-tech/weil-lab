"""Exact finite controls; no analytic, actual-zeta, or Lean certification."""
from fractions import Fraction as F
from pathlib import Path
import json
from certify_native_kernel_de_branges_attachment import g,add,sub,mul,scale,abs2

count=0
def check(b):
    global count
    assert b
    count+=1

for N in [1,3,10,32]:
    for theta in range(-3*N,3*N+1):
        for beta in [F(0),F(1,4),F(-3,8)]:
            p=g(F(theta+1,7),F(2,5));n=g(F(1,3),F(theta-1,11))
            gp=sub(scale(mul(g(0,-1),p),theta-N),scale(n,beta))
            gn=sub(scale(mul(g(0,-1),n),theta-N),scale(p,beta))
            check(add(gp,scale(n,beta))==scale(mul(g(0,-1),p),theta-N))
            check(add(gn,scale(p,beta))==scale(mul(g(0,-1),n),theta-N))
            v=abs2(p)+abs2(n)
            check((theta-N)**2*v<=2*(abs2(gp)+abs2(gn)+beta**2*v))
            check(abs(abs(theta)-N)<=abs(theta-N))
            if abs(theta)>2*N:
                check(abs(theta)<=2*abs(theta-N))
                check(abs(theta)*v<=F(2,N)*(theta-N)**2*v)

# Independent finite Cauchy and tail budgets.
for N in [2,5,17]:
    theta=list(range(-4*N,4*N+1));weights=[F(1,(abs(t-N)+1)**4) for t in theta]
    V=sum(weights);M=sum((t-N)**2*v for t,v in zip(theta,weights))
    first=sum(abs(t-N)*v for t,v in zip(theta,weights))
    check(first**2<=M*V)
    tail=sum(abs(t)*v for t,v in zip(theta,weights) if abs(t)>2*N)
    check(tail<=F(2,N)*M)

# Synthetic rational double-limit control, not an actual divisor/source packet.
# H(n,j)=min(n,j), normalized by n: fixed j tends to zero; fixed n tends to one.
for j in range(1,33):
    n=128*j
    check(F(min(n,j),n)==F(1,128))
for n in range(1,65):
    check(F(min(n,2*n),n)==1)

# The energy-readout witness has vanishing energy with a nonzero row limit.
# Finite rational algebra controls only; analytic realization is in the note.
for j in range(2,66):
    energy=F(1,j*j);ell=1-F(1,j)
    check(ell**2/energy==(j-1)**2)

out={"passed":True,"exact_checks":count,"scope":"finite exact source-coupling/tail algebra and explicitly synthetic limit controls","analytic_certification":False,"actual_zeta_nodes_computed":False,"lean_certification":False,"F4_closed":False}
Path('notes/data/RPB108_HEIGHT_LIMIT_NONUNIFORMITY_VALIDATION_20261007.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
