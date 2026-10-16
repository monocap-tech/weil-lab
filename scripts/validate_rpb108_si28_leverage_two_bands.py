#!/usr/bin/env python3
"""SI28 — inverse-leverage selection of two NEW signed positive windows.

Original signed 7-prime multiplier certified on ALL frequencies in
[2.08,2.12] and [2.30,2.34] (and reflections), not midpoint guesses.
Two true supported Jensen means appended to the SI27 nine-feature
physical Loewner reference. The complete 11x11 signed physical Gram,
original odd pole overlaps, true Simpson interval remainders and
correct-sign rational Woodbury dual certificate are replayable.

Only an original SUPPORTED one-pole inverse UPPER is proved, not
the full odd negative-frequency Birman-Schwinger condition or RH.
"""
from fractions import Fraction as F

from validate_rpb108_si27_independent_high_band import (
    FEATURES as NINE_FEATURES,
)
from validate_rpb108_si25_first_moment_bessel import (
    feature_terms, linear_interval, bilinear_interval,
)
from validate_rpb108_si21_odd_jensen_four import (
    B, PI, KAPPA, outward, midpoint, solve_exact, variational_lower,
    certify_original_window,
)
from validate_rpb108_si13_odd_fourier_reference import arch_lower, certify_window
from validate_rpb108_si14_odd_multiband_nogo import certify_positive_window
from validate_rpb108_si06_negative_band import prime_interval
from validate_rpb108_si12_even_supported_inverse import sinh_bounds

NEW_WINDOWS=(
    (F(21,10),F(1,50),F(6,5)),  # [2.08, 2.12], delta=1.2
    (F(58,25),F(1,50),F(5,2)),  # [2.30, 2.34], delta=2.5
)
FEATURES=NINE_FEATURES+tuple((c,r,d,0) for c,r,d in NEW_WINDOWS)
CELLS=128

def certify_original_continuum(c,r,delta):
    """Prove signed m(xi)>kappa+delta on an ENTIRE rational interval.

    Archimedean term monotone in xi>=0 (SI13). The seven signed prime
    cosines have rigorously bounded derivative magnitude below 69
    (SI06). Each of 128 cells uses its left endpoint, midpoint prime
    enclosure and pays the full half-cell derivative uncertainty.
    """
    assert c-r>0 and r>0
    minimum=None
    for j in range(CELLS):
        a=c-r+2*r*j/CELLS
        b=c-r+2*r*(j+1)/CELLS
        mid=(a+b)/2
        lower=arch_lower(a)+prime_interval(mid)[0]-F(69,2)*(b-a)
        assert lower>KAPPA+delta, (
            "SI28 original signed window not certified",
            str(c),j,float(lower),float(KAPPA+delta)
        )
        minimum=lower if minimum is None else min(minimum,lower)
    return minimum

def build_intervals():
    assert len(NINE_FEATURES)==9 and len(FEATURES)==11
    tau=[]
    gamma=[]
    terms=[]
    q=[]
    for i,(c,r,d,deg) in enumerate(FEATURES):
        beta=2*PI[1]*r*B
        if deg==0:
            t=beta**4/F(180)
        else:
            assert deg==1
            t=3*(4*beta**3+beta**4)/F(180)*F(1,4)**4
        tau.append(t)
        gamma.append(4*r*d/(3 if deg else 1))
        tt=feature_terms(c,r,deg)
        terms.append(tt)
        lo,hi=linear_interval(tt)
        q.append(outward((lo-F(3,4)*t,hi+F(3,4)*t),12))
    assert max(tau)<F(11,10**6)
    assert 0<tau[-1]<F(3,10**6)
    assert all(g>0 for g in gamma)
    assert q[9][0]>F(3,100) and q[10][0]>F(7,100)

    Gram=[]
    for i in range(len(FEATURES)):
        row=[]
        for j in range(len(FEATURES)):
            lo,hi=bilinear_interval(terms[i],terms[j])
            err=4*B*(tau[i]+tau[j])
            row.append(outward((lo-err,hi+err),12))
        Gram.append(row)
    assert all(Gram[i][j]==Gram[j][i]
               for i in range(11) for j in range(11))
    return q,Gram,gamma,tau

def inverse_upper(q,H,gamma,indices):
    """Exact ORIGINAL physical reference inverse upper via rational dual."""
    n=len(indices)
    M=[[(H[i][j][0]/KAPPA+(1/gamma[i] if i==j else 0),
         H[i][j][1]/KAPPA+(1/gamma[i] if i==j else 0))
        for j in indices] for i in indices]
    qq=[q[i] for i in indices]
    z=solve_exact([[midpoint(a) for a in row] for row in M],
                  [midpoint(a) for a in qq])
    corr=variational_lower(qq,M,z)
    assert corr>0
    S_up=F(235648,10**6)
    assert sinh_bounds(B)[1]-B<S_up
    result=2*(S_up/KAPPA-corr/KAPPA**2)
    assert result>0
    return result,z

def certify():
    existing=sorted(set((c-r,c+r) for c,r,d,deg in NINE_FEATURES))
    assert len(existing)==7
    additions=sorted((c-r,c+r) for c,r,d in NEW_WINDOWS)
    assert additions==[(F(52,25),F(53,25)),(F(23,10),F(117,50))]
    for a,b in additions:
        assert all(b<=l or a>=r for l,r in existing)
    assert additions[0][1]<additions[1][0]
    assert all(b<=c or a>=d
               for i,(a,b) in enumerate(existing+additions)
               for j,(c,d) in enumerate(existing+additions) if i!=j)

    original_minima=[certify_original_window(c,d)
                     for c,r,d,deg in NINE_FEATURES[:4]]
    assert all(v>KAPPA+NINE_FEATURES[i][2]
               for i,v in enumerate(original_minima))
    si13_min=certify_window()
    assert si13_min>KAPPA+F(1399,1000)
    existing_high=certify_positive_window(F(219,100),F(223,100))
    assert existing_high>KAPPA+1
    new_minima=[certify_original_continuum(c,r,d)
                for c,r,d in NEW_WINDOWS]
    assert len(new_minima)==2

    q,H,gamma,tau=build_intervals()
    ref9,z9=inverse_upper(q,H,gamma,list(range(9)))
    ref10,z10=inverse_upper(q,H,gamma,list(range(10)))
    alt10,zalt=inverse_upper(q,H,gamma,list(range(9))+[10])
    ref11,z11=inverse_upper(q,H,gamma,list(range(11)))

    # Strict original physically supported one-pole upper (A_o>=C11).
    # This target does NOT imply <=1, even for the one-pole term.
    assert ref9<F(2)  # SI27 independently reproduced at same intervals
    assert ref10<F(4,3),("SI28 first selected window failed",float(ref10))
    assert alt10<F(3,2),("SI28 second candidate failed",float(alt10))
    assert ref11<F(5,4),("SI28 joint <1.25 bound failed",float(ref11))
    assert ref11<ref10 and ref10<ref9
    assert ref11<alt10<ref9

    # Two extra windows are original disjoint continuous Fourier bands.
    # Exact Jensen gives A_o>=C11>=C9 with unchanged kappa scalar floor.
    print("SI28 PASS: inverse-leverage selected signed independent 11-feature reference")
    print("original existing SI27 high-band minimum:",float(existing_high))
    print("new original whole-band minima [2.08,2.12] [2.30,2.34]:",
          *(float(v) for v in new_minima))
    print("positive deltas:",*(float(t[2]) for t in NEW_WINDOWS))
    print("all 11 centers:",*(float(x[0]) for x in FEATURES))
    print("new positive coefficients:",float(gamma[9]),float(gamma[10]))
    print("new true Jensen Simpson errors:",float(tau[9]),float(tau[10]))
    print("new signed source overlaps:",[(float(a),float(b)) for a,b in q[9:]])
    print("full physical SIGNED 11x11 Gram intervals:",
          [[(float(a),float(b)) for a,b in row] for row in H])
    print("reference-9 inverse UPPER:",float(ref9))
    print("reference-10 at 2.10 inverse UPPER:",float(ref10))
    print("alternative reference-10 at 2.32 inverse UPPER:",float(alt10))
    print("reference-11 joint inverse UPPER:",float(ref11))
    print("11-feature rational dual witness:",[float(v) for v in z11])
    print("NO actual original inverse equality, full K Birman-Schwinger, Stage I/F4/Lean/RH")

if __name__=="__main__":
    certify()
