#!/usr/bin/env python3
"""DNE7 exact Fraction bounds and reflection-algebra controls.

Native continuum proof: see DNE7 report. This validator checks the
rational support/mass guards and finite-codimension reflection algebra,
NOT actual zeta null eigenfunctions or infinite-domain statements.
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
    lo,hi=F(2,3),F(7,10)   # true strict bounds for log(2)
    eps=F(1,100)
    cap=F(53,50)
    ck(lo<hi)
    ck(F(3,8)*lo-eps>0)
    ck(F(5,8)*hi+eps<cap)
    ck(lo/F(4)>2*eps)
    ck(F(3,4)*lo-2*eps>lo/F(2))
    ck(F(5,4)*hi+2*eps<1) # log(3)>1; no prime n>=3
    ck(F(8)*eps==F(2,25))
    ck(F(2,25)<F(2,9))
    ck(F(4,9)/2==F(2,9))
    ck(lo/F(3)==F(2,9))  # c_2/2>(log2 lower)/3
    ck(2*eps < lo/F(4))
    ck(F(3,8)*lo-eps >0 and F(5,8)*hi+eps < cap)
    # Arch kernel on both spots is <= 2 by j(log2/2)<2, using
    # j(log2/2)=2*2^(-1/4); the strict root inequality is analytic.
    # Reversed-pair algebra and finite-moment annihilation toy controls.
    def arch(f):
        t0=sum((f[i]/F(100+i) for i in range(8)), F(0))
        t1=sum((f[i]/F(50+i) for i in range(8)), F(0))
        return t0*t0+t1*t1
    a=(F(1),F(-2),F(1),F(0))
    b=(F(0),F(1),F(-2),F(1))
    for aa,bb in product(range(-2,3),repeat=2):
        g=[F(aa)*a[i]+F(bb)*b[i] for i in range(4)]
        ck(sum(g,F(0))==0)
        ck(sum(((i+1)*g[i] for i in range(4)),F(0))==0)
        for sign in (-1,1):
            f=g+[sign*v for v in g]
            norm=sum((v*v for v in f),F(0))
            Rf=[f[i+4] for i in range(4)]+f[:4]
            cross=sum((f[i]*Rf[i] for i in range(8)),F(0))
            ck(cross==sign*norm)
            A=arch(f)
            ck(A>=0)
            ck(A<=F(2,25)*norm)
            C=A+F(4,9)*cross
            if sign<0:
                ck(C<=-F(2,9)*norm)
            else:
                ck(C>=F(4,9)*norm)
    assert checks==262, checks
    return dict(stage="DNE7 reflected arithmetic Hankel controls",
                all_passed=True,exact_fraction_checks=checks,
                cap="53/50",interval_halfwidth="1/100",
                prime_two_lower="4/9",arch_bound="2/25",
                moment_model="two finite-rank independent linear conditions",
                continuous_prime_reflection_sign_indefinite=True,
                actual_zeta_null_tested=False,
                full_original_Weil_negative_vector=False,
                RH_proved=False,lean_certified=False)

if __name__=="__main__":
    print(json.dumps(run(),indent=2))
