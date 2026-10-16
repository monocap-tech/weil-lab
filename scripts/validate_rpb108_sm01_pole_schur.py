#!/usr/bin/env python3
"""SM01: exact-rational consequence and Schur-sign regression for the
parallel structural-mechanism front.

The functional analytic theorems are proved in the accompanying note, not
by passing numerical tests. The SI29 odd-pole bound is imported as a
conservative rational threshold from its focused passing GitHub Actions
run 38977766432; SM01 does NOT claim the full signed K is bounded.
"""
from fractions import Fraction as F

KAPPA=F(1,1000)
SI29_POLE_UB=F(966379,1000000) # certified displayed upper: 0.966378735...
DELTA=1-SI29_POLE_UB
B=F(11,10)
NEGATIVE_MASS_R=F(1204033883,32000000)

def inv2(a):
    det=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    assert det>0
    return [[a[1][1]/det,-a[0][1]/det],
            [-a[1][0]/det,a[0][0]/det]]

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)), F(0))

def mv(m,v):
    return [dot(row,v) for row in m]

def certify():
    # Genuine SI29 full original supported ODD pole-only result
    # A_o-2|s><s| >= (1-lambda)A_o >= delta*kappa I.
    assert DELTA==F(33621,1000000)>0
    assert DELTA*KAPPA==F(33621,1000000000)
    assert SI29_POLE_UB<F(1)
    print("SM01: SI29 pole-only certified lambda UPPER",float(SI29_POLE_UB))
    print("SM01: uniform odd pole-absorbed coercivity fraction >",float(DELTA))
    print("SM01: uniform physical odd L2 lower >",float(DELTA*KAPPA))

    # Exact SI11 universal negative-frequency signed-cover mass, NOT an
    # observed actual operator norm and NOT positivity of its BS operator.
    assert NEGATIVE_MASS_R<F(38)
    eta24=4*B*NEGATIVE_MASS_R / 2**24
    eta28=4*B*NEGATIVE_MASS_R / 2**28
    eta32=4*B*NEGATIVE_MASS_R / 2**32
    assert F(29,100)<eta24/(DELTA*KAPPA)<F(30,100)
    assert F(18,1000)<eta28/(DELTA*KAPPA)<F(19,1000)
    assert F(11,10000)<eta32/(DELTA*KAPPA)<F(12,10000)
    print("SM01: SI11 original signed K frequency residual relative to pole-absorbed floor")
    for bits in (24,28,32):
        eta=4*B*NEGATIVE_MASS_R/2**bits
        print("bits",bits,"negative-frequency residual relative UPPER",float(eta/(DELTA*KAPPA)))
    # These are coarse FULL-operator perturbation estimates and do NOT
    # establish any finite-dimensional negative-frequency eigenvalue.

    # Rational 2x2 algebraic regression of the complete exact pole Schur:
    # A*=A-2ss*, lambda=2s*A^-1s, a=R A^-1R*,
    # R A*^-1R* = a + 2(R A^-1s)^2/(1-lambda).
    A=[[F(2),F(1)], [F(1),F(3)]]
    s=[F(1,4),F(1,3)]
    r=[F(1,5),F(2,7)]
    IA=inv2(A)
    pole=2*dot(s,mv(IA,s))
    assert F(0)<pole<1
    Astar=[[A[i][j]-2*s[i]*s[j] for j in range(2)] for i in range(2)]
    Istar=inv2(Astar)
    a=dot(r,mv(IA,r))
    coupling=dot(r,mv(IA,s))
    schur=a+2*coupling**2/(1-pole)
    direct=dot(r,mv(Istar,r))
    assert schur==direct
    assert direct>a
    # Forgetting cross coupling underestimates the negative BS and can
    # invalidate an attempted positivity certificate.
    print("SM01: exact 2x2 pole elimination check",float(direct))
    print("SM01: naive uncoupled frequency inverse LOWER than true",float(a))
    print("SM01 PASS: algebraic Schur sign and rational residual budgets")
    print("NO full signed negative-frequency BS, full Weil positivity, Stage I, Lean, RH")

if __name__=="__main__":
    certify()
