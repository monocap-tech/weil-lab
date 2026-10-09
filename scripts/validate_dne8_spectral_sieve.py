#!/usr/bin/env python3
"""DNE8 exact rational low-energy spectral-sieve and sign countercontrols.

The analytic killed-semigroup/Carleman arguments live in the DNE8 report.
These checks test only arithmetic cap guards, reflection packet geometry
and rational connected-graph algebra, NOT actual zeta eigenvectors.
"""
from fractions import Fraction as F
from itertools import product
import json

def run():
    checks=0
    def ck(value):
        nonlocal checks
        assert value
        checks+=1

    a=F(53,50); eps=F(1,10**22)
    lo=F(2,3); hi=F(7,10)  # lower/upper for log 2
    m=8*eps
    ck(a>1)
    ck(a<2)
    ck(F(3,8)*lo-eps>0)
    ck(F(5,8)*hi+eps<a)
    ck(F(1,4)*lo>2*eps) # two reflection intervals disjoint
    ck(F(5,4)*hi+2*eps<1) # no reflected prime n >=3
    ck(F(3,4)*lo-2*eps>F(1,2)*lo)
    ck(m==F(8,10**22))
    ck(m*3**36 < F(1,1000)) # genuine spectral mass bound
    ck(4*a<5)
    ck(F(1,2)+2*a==F(131,50))
    ck(F(22,7)*F(131,50)+4<13) # reflected operator norm
    ck(F(12093,3740)<4)
    ck(F(4,9)>F(2,25))
    ck(F(8)*eps<F(2,9)) # DNE7 strict negative packets remain
    ck(5*3**35>0)

    root_options=(F(1,10),F(1,20),F(1,30),F(1,40))
    arch_options=(F(0),F(1,10),F(1,5),F(1,2))
    for q,delta in product(root_options,arch_options):
        p=q*q
        # Positive connected jump J; H=J-2p*I; original analogue
        # Q=H+2|c><c| with c=(q,q), leaving an odd zero.
        J=((p,-p),(-p,p))
        H=((-p,-p),(-p,-p))
        Q=((p,p),(p,p))
        odd=(F(1),F(-1))
        ck(all(sum((J[i][k]*odd[k] for k in (0,1)),F(0))==
               2*p*odd[i] for i in (0,1)))
        ck(all(sum((H[i][k]*odd[k] for k in (0,1)),F(0))==0
               for i in (0,1)))
        ck(all(sum((Q[i][k]*odd[k] for k in (0,1)),F(0))==0
               for i in (0,1)))
        ck(q*sum(odd,F(0))==0) # pole-invisible odd null
        ck(2*odd[0]*odd[1]+delta*sum(odd,F(0))**2<0)
        for x,y in product(range(-3,4),repeat=2):
            x,y=F(x),F(y)
            physical_jump=p*(x-y)**2
            pole_free=-p*(x+y)**2
            original=p*(x+y)**2
            reflected=2*x*y+delta*(x+y)**2
            ck(physical_jump>=0)
            ck(pole_free==x*(H[0][0]*x+H[0][1]*y)+
                 y*(H[1][0]*x+H[1][1]*y))
            ck(original>=0)
            ck(reflected==x*(delta*x+(1+delta)*y)+y*((1+delta)*x+delta*y))
    return {
        "stage":"DNE8 exact native low-energy sieve model preflight",
        "all_passed":True,
        "exact_fraction_checks":checks,
        "rational_packet_halfwidth":str(eps),
        "reflected_full_support_mass_upper":"1/1000",
        "rank_bound":"N_(53/50,kappa) < 5 * 3^35",
        "reflected_operator_norm_bound":"13",
        "false_generic_sign_transfer_rejected":True,
        "actual_native_jump_eigenbasis_evaluated":False,
        "global_null_excluded":False,
        "RH_proved":False,
        "lean_proved":False
    }

if __name__=="__main__":
    print(json.dumps(run(),indent=2))
