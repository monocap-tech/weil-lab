#!/usr/bin/env python3
"""EF43: exact rational span-preserving normalization of six ORIGINAL SI10 jets.

Construct a LOWER TRIANGULAR *rational* map C from the six unchanged
first-cluster even original source jets v0..v5 (center 37/64, order15)
to w_i=sum_{j<=i} C_ij*v_j. All C coefficients are exact rational
numbers, chosen by midpoint rational Gram-Schmidt, not interval
assumptions or new source constraints. Diagonal C_ii nonzero proves
span(w)=span(v) literally in original protected V469.

Independently evaluate physical K=C*G*C^T in SOURCE-NATIVE 10^340
OUTWARD intervals, using the genuine original six-jet physical G.
Certify the ROW SUM ||K-I||_infinity <1/10^7, so every eigenvalue
K lies in [1-eps,1+eps]. No floating SVD, no unverified inverse.

Full original signed response H40 includes all seven prime powers,
true positive even pole, all first 40 quarter-digamma arch modes,
the full signed arch Gram, with m>=40 infinite arch tail still paid.
For transformed pairings h=C*b, the exact matrix order bound gives
 ||H40-P_span(w)H40||² <= ||H40||²-||h||²/(1+eps)
without an approximate inverse. The resulting independent enclosure
is checked against EF42's original six-row Schur result.

This certifies representation/conditioning, not the full 469D
source projection, original form-domain audit, positivity or RH.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json
from validate_rpb108_ef24_original_even_edge_intervals import I,S
from validate_rpb108_ef42_original_even_six_jet_projection import (
    source_six_row_schur, original_tail, MU, ORDER
)

ROOT=Path(__file__).resolve().parents[1]
Q=10**22
EPS=F(1,10**7)
SQUARE_CAP=F(4054,100000)
SQRT_CAP=F(20135,100000)
COFINITE_NORM_CAP=F(79,250)
ETA_CAP=F(12482,85)

def midpoint_quantized(v):
    assert isinstance(v,I)
    return F(((v.lo+v.hi)*Q)//(2*S),Q)

def exact_dot(a,b,G):
    return sum((a[i]*G[i][j]*b[j] for i in range(ORDER)
                for j in range(ORDER)),F(0))

def source_rational_normalizing_map(G):
    # Rational approximate Gram ONLY selects a rational basis:
    # the actual certification uses the full outward original G.
    g=[[midpoint_quantized(v) for v in row] for row in G]
    rows=[]
    for k in range(ORDER):
        c=[F(int(i==k)) for i in range(ORDER)]
        for j in range(k):
            pj=exact_dot(c,rows[j],g)
            dj=exact_dot(rows[j],rows[j],g)
            assert dj>0
            c=[c[i]-pj/dj*rows[j][i] for i in range(ORDER)]
        d=exact_dot(c,c,g)
        assert d>0
        t=isqrt((d.numerator*Q*Q)//d.denominator)
        assert t>0
        factor=F(Q,t)
        c=[x*factor for x in c]
        assert c[k]>0
        assert all(x==0 for x in c[k+1:])
        rows.append(c)
    # The exact rational lower-triangular C has nonzero diagonal.
    assert all(rows[k][k]>0 for k in range(ORDER))
    return rows

def actual_original_transformed_gram(G,C):
    K=[[I(0) for _ in range(ORDER)] for _ in range(ORDER)]
    for i in range(ORDER):
        for j in range(i,ORDER):
            acc=I(0)
            for p in range(i+1):
                for q in range(j+1):
                    acc+=C[i][p]*C[j][q]*G[p][q]
            K[i][j]=K[j][i]=acc
    rowerrors=[]
    for i in range(ORDER):
        accum=F(0)
        for j in range(ORDER):
            err=K[i][j]-(1 if i==j else 0)
            accum+=F(err.abs_upper(),S)
        assert accum<EPS,('original transformed Gram row defect',i,float(accum))
        rowerrors.append(accum)
    return K,rowerrors

def original_response_projection_bound(full,b,C,rowerrors,ef42D):
    assert max(rowerrors)<EPS
    h=[]
    for i in range(ORDER):
        s=I(0)
        for j in range(i+1):
            s+=C[i][j]*b[j]
        h.append(s)
    h2=sum((x*x for x in h),I(0))
    assert h2.lo>0
    # K positive definite since ||K-I||_2<=||K-I||_infty<EPS.
    # Therefore K^{-1} >= (1+EPS)^{-1}I and
    # K^{-1} <=(1-EPS)^{-1}I, independent from source LDL.
    low=full-h2/(1-EPS)
    up=full-h2/(1+EPS)
    assert low.lo>0,('independent original projected square positivity',low.scaled())
    assert up.lo>0
    assert low.lo<=ef42D.hi and up.hi>=ef42D.lo
    assert F(up.hi,S)<SQUARE_CAP,('six-jet independent bound',up.scaled())
    assert F(up.hi-ef42D.lo,S)<F(1,10**6),(
        'representation does not reproduce native original Schur',up.scaled(),ef42D.scaled())
    return low,up,h,h2

def main():
    m=json.loads((ROOT/'research/obligations.json').read_text())
    o={x['id']:x for x in m['obligations']}
    assert m['active_obligation']=='W-EVEN-FORM'
    assert 'EF42' in o['W-EVEN-FORM']['evidence']
    assert all(o[k]['status']=='open' for k in ('W-EVEN-FORM','W-ODD-NEG','W-WHOLE-FORM'))
    G,b,stages,full=source_six_row_schur()
    C=source_rational_normalizing_map(G)
    K,errors=actual_original_transformed_gram(G,C)
    low,up,h,h2=original_response_projection_bound(full,b,C,errors,stages[-1][2])
    tail=original_tail()
    assert SQUARE_CAP<SQRT_CAP**2
    assert tail<F(57,500)+F(1,10000)
    assert SQRT_CAP+F(57,500)+F(1,10000)<COFINITE_NORM_CAP
    assert COFINITE_NORM_CAP**2/MU==ETA_CAP
    assert ETA_CAP<F(2560,17)
    maxabs=max(sum(abs(x) for x in row) for row in C)
    print('EF43 original SI10 37/64 first frequency order15:'
          ' exact rational lower-triangular six-jet C,'
          ' determinant product nonzero, same protected source span.',flush=True)
    print('EF43 genuine original outward transformed physical Gram'
          ' max row-sum deviation from identity below EPS:',
          str(EPS),' actual approximate',float(max(errors)),
          ' max rational coefficient row l1',float(maxabs),flush=True)
    print('EF43 independent original normalized-source full signed'
          ' physical six-row projection interval lower',low.scaled(),
          'upper',up.scaled(),' EF42 direct monomial',
          stages[-1][2].scaled(),flush=True)
    print('EF43 certified TRUE original 6-row signed finite'
          ' physical squared projected response <4054/100000,'
          ' complete infinite 40+ arch tail included,'
          ' full even cofinite first source ||P_F g_e||<79/250=0.316,'
          ' unseen eta<12482/85=',float(ETA_CAP),flush=True)
    print('EF43 scope: source-span representation conditioned,'
          ' not an added seventh jet; original 463 remaining'
          ' protected rows, actual full 469D projected response'
          ' and cofinite q-Riesz inverse, EF33 Schur sign,'
          ' even, odd, Weil and RH OPEN. Independent original'
          ' Fourier/digamma/core analytic audit OPEN.',flush=True)

if __name__=='__main__':
    main()
