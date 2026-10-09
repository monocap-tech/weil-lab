#!/usr/bin/env python3
"""DNE4 finite exact-Fraction controls: full killed ground-state transform.

The analytic DNE4 theorem covers the actual infinite-dimensional native
operator. These tests verify factors, killing payment, regularization,
and a higher-odd-zero countercontrol on a rational three-site graph.
"""
from fractions import Fraction as F
from itertools import product
import json

def run():
    phi = (F(1), F(2), F(1))
    edges = {(0,1):F(1,2), (1,2):F(1,2), (0,2):F(1,4)}
    killing = (F(3,2), F(1,2), F(3,2))
    mu = F(1)
    J = ((F(9,4),-F(1,2),-F(1,4)),
         (-F(1,2),F(3,2),-F(1,2)),
         (-F(1,4),-F(1,2),F(9,4)))
    checks=0
    def check(q):
        nonlocal checks
        assert q
        checks+=1

    def bilinear(x,y):
        internal=sum((c*(x[i]-x[j])*(y[i]-y[j])
                      for (i,j),c in edges.items()),F(0))
        external=sum((killing[i]*x[i]*y[i] for i in range(3)),F(0))
        return internal+external

    def mass(x):
        return sum((z*z for z in x),F(0))

    def weighted(u):
        return sum((c*phi[i]*phi[j]*(u[i]-u[j])**2
                    for (i,j),c in edges.items()),F(0))

    check(all(sum((J[i][k]*phi[k] for k in range(3)),F(0)) ==
              mu*phi[i] for i in range(3)))
    check(all(bilinear(tuple(F(int(i==k)) for i in range(3)),
                       tuple(F(int(i==j)) for i in range(3)))==J[k][j]
              for k in range(3) for j in range(3)))
    check(all(v>0 for v in killing))
    check(all(v>0 for v in edges.values()))

    epsilons=(F(1),F(1,2),F(1,4),F(1,8))
    for entries in product((-2,-1,0,1,2), repeat=3):
        f=tuple(F(x) for x in entries)
        u=tuple(f[i]/phi[i] for i in range(3))
        E=bilinear(f,f)-mu*mass(f)
        check(E==weighted(u))
        check(E>=0)
        for eps in epsilons:
            g=tuple(f[i]**2/(phi[i]+eps) for i in range(3))
            W_eps=sum((c*(phi[i]+eps)*(phi[j]+eps)*
                    (f[i]/(phi[i]+eps)-f[j]/(phi[j]+eps))**2
                    for (i,j),c in edges.items()),F(0))
            B_eps=sum((killing[i]*eps*f[i]**2/(phi[i]+eps)
                        for i in range(3)),F(0))
            last=mu*sum((eps*f[i]**2/(phi[i]+eps)
                         for i in range(3)),F(0))
            check(bilinear(phi,g)==mu*sum((phi[i]*g[i]
                                           for i in range(3)),F(0)))
            check(bilinear(f,f)-bilinear(phi,g)==W_eps+B_eps)
            check(E==W_eps+B_eps-last)

    odd=(F(1),F(0),F(-1))
    G=tuple(odd[i]/phi[i] for i in range(3))
    check(all(sum((J[i][j]-(F(5,2) if i==j else F(0)))*
                    odd[j] for j in range(3))==0 for i in range(3)))
    check(weighted(G)==F(3))
    check(mass(odd)==F(2))
    check(weighted(G)/mass(odd)==F(3,2))
    assert checks==1758
    return {
        "stage":"DNE4 global weighted jump domain algebra",
        "all_passed":True,
        "exact_fraction_checks":checks,
        "ground_level_mu":"1",
        "exterior_killing":"3/2,1/2,3/2",
        "odd_higher_zero_gap":"3/2",
        "full_infinite_domain_proved_by_script":False,
        "native_Weil_spectral_surplus_proved":False,
        "RH_proved":False,
        "lean_certified":False,
    }

if __name__=="__main__":
    print(json.dumps(run(),indent=2))
