#!/usr/bin/env python3
"""SM17: exact Fraction conditional original odd 890-source cap budget.

Analytic compactness and extension theorem are not executable proofs.
The original 890-column supported inverse value remains OPEN.
"""
from fractions import Fraction as F

KAPPA = F(1,1000)
L_POLE = F(966379,10**6)
KAPPA_STAR = KAPPA*(1-L_POLE)
TAU = F(1,1024)
ETA_UP = F(302,10**12)
TEST_MU = F(999,1000)

def validate():
    assert KAPPA_STAR == F(33621,10**9)
    assert F(0)<ETA_UP<KAPPA_STAR
    threshold = (1-ETA_UP/KAPPA_STAR)/(1+TAU)
    assert threshold == F(4303449344,4307690625)
    assert TEST_MU < threshold < F(1)
    upper=(1+TAU)*TEST_MU+ETA_UP/KAPPA_STAR
    assert upper < 1 and 1-upper>F(1,100000)
    tr_upper = F(11,5)*38/KAPPA_STAR
    assert F(0)<tr_upper<F(2486542)
    # Conditional negative witness identity for exact sample eigenvalue.
    lam=F(6,5)
    assert lam-lam*lam == lam*(1-lam) == -F(6,25)
    # Positive 2x2 block can coexist with a negative third Schur direction.
    assert F(1)*F(1)-F(0)**2>0 and F(-1)-F(0)<0
    print("SM17 sufficient 890-source lambda_max threshold:",str(threshold),float(threshold))
    print("SM17 IF mu<=999/1000, lambda_max(T)<",float(upper))
    print("SM17 conditional exact margin",float(1-upper))
    print("SM17 trace bound (loose)",float(tr_upper))
    print("SM17 PASS (CONDITIONAL ONLY); original 890-source inverse and W-ODD-NEG OPEN")

if __name__=="__main__":
    validate()
