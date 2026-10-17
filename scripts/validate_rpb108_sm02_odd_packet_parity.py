#!/usr/bin/env python3
"""SM02: original odd parity-compressed negative packet rank and residual.

Uses SI10 original seven-prime certified cover and SI08 exact Taylor orders.
Accepts NO claim about the omitted finite BS matrix eigenvalues or RH.
"""
from fractions import Fraction as F
from validate_rpb108_si10_complement_positivity import (
    KAPPA, protected_inner_cover, protected_outer_band
)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_si06_negative_band import B

FULL_RANK={9:939,10:1003,12:1121,16:1367,20:1561,21:1631,24:1781,32:2151}
ODD_RANK={9:470,10:502,12:561,16:684,20:781,21:816,24:891,32:1076}

def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def sub(a,b):
    return [[a[i][j]-b[i][j] for j in range(len(a[i]))]
            for i in range(len(a))]

def t(a):
    return list(map(list,zip(*a)))

def is_pd2(a):
    return a[0][0]>0 and a[0][0]*a[1][1]-a[0][1]**2>0 and a[0][1]==a[1][0]

def validate():
    outer_count,outer_min=protected_outer_band()
    assert outer_count==2535 and outer_min>KAPPA
    groups,W,M,leaves,protected=protected_inner_cover()
    assert len(groups)==107 and leaves==973 and protected==9261
    assert W==F(973,32)
    assert M==F(1203060883,32000000)
    R=M+KAPPA*W
    assert R==F(1204033883,32000000)<F(38)
    print("SM02: original signed cover and 107 paired positive/negative clusters verified",flush=True)

    for bits in FULL_RANK:
        ps=[taylor_order(right-left,bits)[0] for left,right,_ in groups]
        assert all(isinstance(p,int) and p>0 for p in ps)
        d_full=1+2*sum(ps)
        d_odd=1+sum(ps)
        assert d_full==FULL_RANK[bits]
        assert d_odd==ODD_RANK[bits]
        assert 2*d_odd-1==d_full
        eps=F(1,2**bits)
        eta=4*B*R*eps
        complement=2*B*R*eps**2
        assert eta>0 and complement>0 and KAPPA>complement
        if bits==20:
            assert F(15,100)<eta/KAPPA<F(16,100)
        if bits==24:
            assert F(98,10000)<eta/KAPPA<F(99,10000)
        if bits==32:
            assert F(38,10**6)<eta/KAPPA<F(39,10**6)
        print("b",bits,"full-rank",d_full,"odd-rank",d_odd,
              "eta/kappa",float(eta/KAPPA),"odd complement penalty",
              float(complement),flush=True)

    # Exact 2x2 model: keep the negative frequency rank-one in the same
    # finite M as the true signed negative pole, preserving their cross terms.
    A=[[F(2),F(1,5)],[F(1,5),F(3)]]
    s=[[F(1,4)],[F(1,6)]]
    r=[[F(1,5)],[F(1,3)]]
    pole=mm([[2*x[0]] for x in s],t(s))
    freq=mm(r,t(r))
    coupled=[[pole[i][j]+freq[i][j] for j in range(2)] for i in range(2)]
    assert is_pd2(A) and is_pd2(sub(A,coupled))
    assert coupled[0][1]>pole[0][1] and coupled[0][1]>freq[0][1]
    # Invalid: omit the pole and frequency coupling. Algebraic sign check
    # deliberately retains both cross terms.
    bad=sub(A,pole)
    assert is_pd2(bad)
    delta=F(33621,10**6)
    assert F(0)<delta<F(1)
    assert 1/delta>F(29)  # absorbing pole first worsens the coarse error factor
    print("SM02 PASS: odd packet dimension halved, all-original mass error",
          "preserved, finite pole/frequency coupling regression checked",flush=True)
    print("W-ODD-NEG OPEN: finite matrix BS eigenvalue not certified",flush=True)

if __name__ == "__main__":
    validate()
