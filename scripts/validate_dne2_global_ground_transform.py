#!/usr/bin/env python3
"""DNE2 exact rational connected-graph transfer controls.

The genuine infinite-dimensional positivity-improving theorem is analytic;
these finite checks discriminate the false inference that a connected
conservative Doob transform excludes a higher original zero eigenmode.
"""
from fractions import Fraction as F
from itertools import product
import json

def run():
    checks=0
    def ck(v):
        nonlocal checks
        assert v
        checks+=1

    phi=[F(1),F(2),F(1)]
    lam=F(-3,2)
    edges={(0,1):F(1,2),(1,2):F(1,2),(0,2):F(1,4)}
    n=3
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    for (i,j),w in edges.items():
        L[i][j]=-w
        L[j][i]=-w
        L[i][i]+=w*phi[j]/phi[i]
        L[j][j]+=w*phi[i]/phi[j]
    assert L==[[F(5,4),-F(1,2),-F(1,4)],
               [-F(1,2),F(1,2),-F(1,2)],
               [-F(1,4),-F(1,2),F(5,4)]]
    ck(all(sum(L[i][j]*phi[j] for j in range(n))==0 for i in range(n)))
    ck(all(L[i][j]<0 for i in range(n) for j in range(n) if i!=j))
    G=[[L[i][j]*phi[j]/phi[i] for j in range(n)] for i in range(n)]
    ck(all(sum(G[i])==0 for i in range(n)))
    ck(all(G[i][j]<0 for i in range(n) for j in range(n) if i!=j))
    weights=[v*v for v in phi]
    ck(all(weights[i]*(-G[i][j])==weights[j]*(-G[j][i])
           for i in range(n) for j in range(n) if i!=j))
    ck(all(-G[i][j]>0 for i in range(n) for j in range(n) if i!=j))
    for mode in ([F(1),-F(1),F(1)],[F(1),F(0),-F(1)]):
        ck(all(sum(L[i][j]*mode[j] for j in range(n)) ==
               F(3,2)*mode[i] for i in range(n)))
        ck(sum(phi[i]*mode[i] for i in range(n))==0)
        ck(all(sum((L[i][j]-(lam if i==j else F(0)))*mode[j]
                    for j in range(n))==0 for i in range(n))) if False else None
        # H=L+lambda*I, so both modes are exact H-null.
        ck(all(sum((L[i][j]+(lam if i==j else 0))*mode[j]
                    for j in range(n))==0 for i in range(n)))

    def energy(u):
        h=[phi[i]*u[i] for i in range(n)]
        return sum((h[i]*L[i][j]*h[j] for i in range(n)
                    for j in range(n)),F(0))
    def jumps(u):
        return sum((w*phi[i]*phi[j]*(u[i]-u[j])**2
                   for (i,j),w in edges.items()),F(0))
    for vals in product((-1,0,1,2),repeat=3):
        u=[F(x) for x in vals]
        ck(energy(u)==jumps(u)>=0)
        clipped=[max(F(0),min(F(1),x)) for x in u]
        ck(jumps(clipped)<=jumps(u))
    return {"stage":"DNE2 global Doob-transform graph controls",
            "all_passed":True,
            "rational_checks":checks,
            "weighted_phi":"1,2,1",
            "ground_eigenvalue":"-3/2",
            "higher_odd_zero_preserved":True,
            "higher_even_zero_preserved":True,
            "actual_weil_ground_eigenvector_evaluated":False,
            "full_native_jump_domain_certified":False,
            "RH_proved":False,"lean_certified":False}

if __name__=="__main__":
    print(json.dumps(run(),indent=2))
