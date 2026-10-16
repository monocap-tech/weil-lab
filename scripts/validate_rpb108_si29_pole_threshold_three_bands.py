#!/usr/bin/env python3
"""SI29: verify a strict ORIGINAL odd pole-only BS gate, not full K."""
from fractions import Fraction as F
from validate_rpb108_si28_leverage_two_bands import (
    FEATURES as OLD, certify_original_continuum, inverse_upper)
from validate_rpb108_si25_first_moment_bessel import (
    feature_terms, linear_interval, bilinear_interval)
from validate_rpb108_si21_odd_jensen_four import B, PI, KAPPA, outward
from validate_rpb108_si12_even_supported_inverse import sinh_bounds

NEW = ((F(18,25),F(1,50),F(3,4)),
       (F(14,5),F(1,50),F(2,5)),
       (F(17,5),F(1,50),F(4)))
FEATURES = OLD + tuple((c,r,d,0) for c,r,d in NEW)

def certify():
    assert len(OLD)==11 and len(FEATURES)==14
    windows=sorted(set((c-r,c+r) for c,r,d,deg in FEATURES))
    assert len(windows)==12
    assert all(windows[i][1]<=windows[i+1][0] for i in range(11))
    assert sorted((c-r,c+r) for c,r,d in NEW)==[
        (F(7,10),F(37,50)),
        (F(139,50),F(141,50)),
        (F(169,50),F(171,50))]
    minima=[certify_original_continuum(c,r,d) for c,r,d in NEW]
    assert all(m>KAPPA+d for m,(_,_,d) in zip(minima,NEW))

    terms=[]; tau=[]; gamma=[]; q=[]
    for c,r,d,degree in FEATURES:
        beta=2*PI[1]*r*B
        e=(beta**4/F(180) if degree==0
           else 3*(4*beta**3+beta**4)/F(180)*F(1,4)**4)
        assert F(0)<e<F(11,10**6)
        tau.append(e)
        gamma.append(4*r*d/(3 if degree else 1))
        term=feature_terms(c,r,degree)
        terms.append(term)
        lo,hi=linear_interval(term)
        q.append(outward((lo-F(3,4)*e,hi+F(3,4)*e),12))
    assert gamma[-3:]==[F(3,50),F(4,125),F(8,25)]

    H=[]
    for i in range(14):
        row=[]
        for j in range(14):
            lo,hi=bilinear_interval(terms[i],terms[j])
            err=4*B*(tau[i]+tau[j])
            row.append(outward((lo-err,hi+err),12))
        H.append(row)
    assert all(H[i][j]==H[j][i] for i in range(14) for j in range(14))

    # True physical rank-14 Jensen/Bessel reference C14 <= A_odd.
    # Exact-rational signed variational Woodbury, using all 196 H entries.
    before,_=inverse_upper(q,H,gamma,list(range(11)))
    one,_=inverse_upper(q,H,gamma,list(range(12)))
    two,_=inverse_upper(q,H,gamma,list(range(13)))
    result,witness=inverse_upper(q,H,gamma,list(range(14)))
    assert before<F(5,4)
    assert F(0)<result<F(1), ("pole-only gate not achieved",float(result))
    assert result<before

    print("SI29 PASS: original odd pole-only BS norm strictly below 1")
    print("new original signed full-window minima:",*[float(x) for x in minima])
    print("new physical source q:",[(float(a),float(b)) for a,b in q[-3:]])
    print("new positive Jensen weights:",*[float(x) for x in gamma[-3:]])
    print("complete signed physical Gram:",[[(float(a),float(b)) for a,b in row] for row in H])
    print("11/12/13/14 feature inverse UPPER:",
          float(before),float(one),float(two),float(result))
    print("14 rational inverse witness:",[float(z) for z in witness])
    print("NO complete negative-frequency K or even-sector gate, Stage I/F4/Lean/RH")

if __name__=="__main__":
    certify()
