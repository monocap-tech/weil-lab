#!/usr/bin/env python3
"""SM24: first ACTUAL original odd residual inverse-energy upper by cancellation.

This uses the true original 37/64 odd SM10 source and full original SI29
14 positive Jensen/Legendre feature Gram to get SM22's source *inverse*
upper U_B. Because E=u-lambda*A_star*u with true A_star (not B14),
  <E,A_star^-1 E>
  = <u,A_star^-1u> -2lambda||u||^2 +lambda^2<u,A_star*u>.
Enclose forward energy via graph M and exact-rational Cauchy/Young.
This is NOT an upper for <E,B14^-1 E>, nor the full 890-source odd gate.
A 3x2 exact finite matrix replay checks the all-column Loewner identity.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from validate_rpb108_sm22_first_original_inverse_reference import (
    B, KAPPA, KAPPA_STAR, L_POLE, FEATURES, TAIL_A2, YOUNG,
    full_upper_leaves, gram, signed_odd_overlap, simpson_error,
    feature_terms, bilinear_interval, outward, midpoint,
    solve_exact, variational_lower, sqlo, abshi
)
from validate_rpb108_sm23_coupled_residual_reference import (
    mat, tr, add, sub, scale, diag, inv, psd2
)

ROOT=Path(__file__).resolve().parents[1]


def finite_all_column_regression():
    # Arbitrary positive model, not a numerical evaluation of the
    # original physical seven-prime A_*.
    A=diag([F(2),F(3),F(4)])
    B0=diag([F(1),F(2),F(3)])  # B0 <= A
    U=[[F(1),F(0)],[F(1),F(1)],[F(0),F(1)]]
    Y=[[F(1,7),F(0)],[F(0),F(1,11)],[F(1,5),F(1,13)]]
    E=sub(U,mat(A,Y))
    actual=mat(mat(tr(E),inv(A)),E)
    source=mat(mat(tr(U),inv(A)),U)
    HY=sub(add(mat(tr(U),Y),mat(tr(Y),U)),mat(mat(tr(Y),A),Y))
    assert add(HY,actual)==source
    source_reference=mat(mat(tr(U),inv(B0)),U)
    assert psd2(sub(source_reference,source))
    # With B0-inverse residual *instead*, the exact cancellation
    # does not hold; these must remain distinct mathematical objects.
    surrog=mat(mat(tr(E),inv(B0)),E)
    assert surrog!=actual
    return source,actual,surrog


def run():
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert "SM23" in gov["evidence"] and "SM24" in gov["evidence"]
    assert KAPPA==F(1,1000) and KAPPA_STAR==F(33621,10**9)
    assert F(0)<L_POLE<1

    # All source data below are independently reconstructed from
    # the same original source files as SM22, not hardcoded from logs.
    clusters,width,mass,total=full_upper_leaves()
    center=(clusters[0][0][0]+clusters[0][-1][1])/2
    assert center==F(37,64) and len(FEATURES)==14
    nlo,nhi=outward(gram(center,center),12)
    assert F(0)<nlo<=nhi<F(9,4)

    terms=[];tau=[];gamma=[]
    for source_c,r,d,deg in FEATURES:
        terms.append(feature_terms(source_c,r,deg))
        err=simpson_error(r,deg)
        bound=outward((err,err),15)[1]
        assert 0<err<=bound<F(1,1000)
        tau.append(bound)
        gamma.append(4*r*d/(3 if deg else 1))

    q=[]
    for i,term in enumerate(terms):
        lo,hi=bilinear_interval(term,((center,F(1)),))
        q.append(outward((lo-2*B*tau[i],hi+2*B*tau[i]),12))
    H=[[None]*14 for _ in range(14)]
    for i in range(14):
        for j in range(i,14):
            lo,hi=bilinear_interval(terms[i],terms[j])
            eps=4*B*(tau[i]+tau[j])
            H[i][j]=H[j][i]=outward((lo-eps,hi+eps),12)

    K=[[(v[0]/KAPPA+(1/gamma[i] if i==j else 0),
         v[1]/KAPPA+(1/gamma[i] if i==j else 0))
        for j,v in enumerate(H[i])] for i in range(14)]
    z0=solve_exact([[midpoint(a) for a in row] for row in K],
                   [midpoint(v) for v in q])
    unit=10**10
    z=[F((a*unit).numerator//(a*unit).denominator,unit) for a in z0]
    correction=variational_lower(q,K,z)
    assert correction>0
    upper_C=nhi/KAPPA-correction/KAPPA**2
    assert upper_C>0
    upper_B=upper_C/(1-L_POLE)
    assert upper_B>0

    # True first SM21 original source-energy and original full
    # unbounded a^2 graph bound, including negative signed odd pole.
    pole=outward(signed_odd_overlap(center),12)
    positive=KAPPA*nlo+sum((gamma[i]*sqlo(q[i])
                             for i in range(14)),F(0))
    source_rayleigh=positive-2*abshi(pole)**2
    assert source_rayleigh>0
    qL=max(source_rayleigh,KAPPA_STAR*nlo)
    M=1360*nhi+2*TAIL_A2
    lam=qL/M
    assert M>0 and F(0)<lam<1
    Dhi=nhi-qL*qL/M
    assert Dhi>0 and Dhi<nhi

    # Apply rational Cauchy to the true original A_* forward energy,
    # NOT its fourteen-feature reference lower.
    # For r>0, <u,A_*u> <= ||u|| ||A_*u||
    # <= n_hi/(2r) + r*M/2.
    r=F(1,37)
    q_upper=nhi/(2*r)+r*M/2
    assert q_upper>qL>0 and q_upper<F(40)
    exact_cancel_upper=upper_B-2*lam*nlo+lam*lam*q_upper
    assert exact_cancel_upper>0
    # Strict first-source improvement of the TRUE inverse-residual
    # upper, using actual signed cross and source-energy inequalities.
    assert exact_cancel_upper<upper_B

    # SM22's earlier residual upper is for the *surrogate*
    # B14^-1 response. Unlike our actual-A_* result, it cannot use
    # the exact -2lam||u||² cancellation.
    young=min(((1+d)*upper_B+
               (1+1/d)*lam*lam*M/KAPPA_STAR)
              for d in YOUNG)
    uniform=Dhi/KAPPA_STAR
    previous=min(young,uniform)
    assert exact_cancel_upper<previous
    assert previous>0

    src,exact_finite,surrogate_finite=finite_all_column_regression()
    print("SM24 actual first SM10 original odd center",center,flush=True)
    print("SM24 original first source norm²",float(nlo),float(nhi),flush=True)
    print("SM24 actual source Rayleigh lower",float(qL),flush=True)
    print("SM24 original all-frequency A_star graph M",float(M),flush=True)
    print("SM24 true SM21 forward lambda",float(lam),flush=True)
    print("SM24 SI29 14 signed true-feature variational correction",
          float(correction),flush=True)
    print("SM24 true original A_star^-1 first-source upper",
          float(upper_B),flush=True)
    print("SM24 actual original forward energy upper by rational Young",
          float(q_upper),flush=True)
    print("SM24 exact original inverse-residual cancellation upper",
          float(exact_cancel_upper),flush=True)
    print("SM24 previous surrogate-B14 Young residual upper",
          float(young),flush=True)
    print("SM24 original scalar residual upper",float(uniform),flush=True)
    print("SM24 strict improvement factor vs previous residual bound",
          float(previous/exact_cancel_upper),flush=True)
    print("SM24 exact 2-column original-operator finite replay",src,
          exact_finite,flush=True)
    print("SM24 surrogate finite B^-1 residual != actual A^-1 residual",
          surrogate_finite!=exact_finite,flush=True)
    print("SM24 PASS SCOPED: original first source true inverse-residual"
          " cancellation, physical SI29 signed 14-feature first-source"
          " inverse upper, full original a² graph and rational forward"
          " upper; strict improvement over SM22 surrogate/Young."
          " Actual physical 890-source coupled Gram, original odd"
          " W-ODD-NEG, original Weil, native CC27 D-Riesz and RH OPEN.",
          flush=True)

if __name__=="__main__":
    run()
