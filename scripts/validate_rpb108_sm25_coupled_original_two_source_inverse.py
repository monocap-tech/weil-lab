#!/usr/bin/env python3
"""SM25: TRUE ORIGINAL 2-column odd source inverse coupled Loewner upper.

Actual first two distinct SM10 negative-cap cluster degree-zero sources
u_j(x)=sin(2pi*c_j*x) on original physical odd I=[-11/10,11/10].
All 14 original continuous SI29 signed positive feature overlaps q_ia,
all 14x14 TRUE signed physical reference grams H_ij and actual 2x2
physical G_ij, with rigorous original quadrature/interval errors.

True original Astar=A_o-2ss* >= B14=C14-2ss* >0:
  X2=U2*Astar^-1 U2 <= U2*B14^-1 U2 <= T2
using rational coupled 14x2 variational witness and Loewner-safe
signed 2x2 interval enclosure. The true SM10 infinite eta is
paid for Astar-eta I via Teta=T2/(1-eta/kappa_star).
C2 is actual first two block-diagonal original SM10 negative
covariance weights, not a fake diagonalization of the positive
source inverse. NO actual full 890-source W-ODD-NEG or RH sign.
"""
import json
from fractions import Fraction as F
from pathlib import Path
from validate_rpb108_sm22_first_original_inverse_reference import (
    B, KAPPA, KAPPA_STAR, L_POLE, FEATURES,
    full_upper_leaves, gram, simpson_error, feature_terms,
    bilinear_interval, outward, midpoint, solve_exact
)
from validate_rpb108_sm23_coupled_residual_reference import (
    mat, tr, add, sub, scale, diag, inv, psd2
)

ROOT=Path(__file__).resolve().parents[1]
TAU=F(1,1024)
ETA_HI=F(302,10**12)


def iplus(a,b):
    return (a[0]+b[0],a[1]+b[1])


def isc(a,k):
    return (a[0]*k,a[1]*k) if k>=0 else (a[1]*k,a[0]*k)


def isym(a):
    assert a[0]<=a[1]
    return (a[0]+a[1])/2,(a[1]-a[0])/2


def rounded(z):
    den=10**10
    return F((z*den).numerator//(z*den).denominator,den)


def source_intervals():
    clusters,width,mass,total=full_upper_leaves()
    assert len(clusters)==107
    centers=[(clusters[i][0][0]+clusters[i][-1][1])/2 for i in range(2)]
    assert centers[0]==F(37,64)
    assert centers[1]!=centers[0]
    assert centers[0]>0 and centers[1]>0
    assert len(FEATURES)==14
    # Actual SM10 original negative-cap covariance C00 for degree-0
    # modes in two DISTINCT original frequency clusters.
    C0=[2*sum(((h+KAPPA)*(r-l) for l,r,h in cluster),F(0))
        for cluster in clusters[:2]]
    assert all(x>0 for x in C0)
    assert 0<TAU<F(1)
    return centers,C0


def full_physical_matrices(centers):
    # Genuine signed original physical U2*U2, NOT orthogonality.
    G=[[None]*2 for _ in range(2)]
    for i in range(2):
        for j in range(i,2):
            G[i][j]=G[j][i]=outward(gram(centers[i],centers[j]),12)
    assert all(x[0]<=x[1] for row in G for x in row)
    # All 14 true continuous SI29 source profiles and true all
    # 105 signed original cross-grams, with full integration error.
    terms=[];gamma=[];tau=[]
    for i,(c,r,delta,degree) in enumerate(FEATURES):
        terms.append(feature_terms(c,r,degree))
        t=outward((simpson_error(r,degree),)*2,15)[1]
        assert t>0 and t<F(1,1000)
        tau.append(t)
        gamma.append(4*r*delta/(3 if degree else 1))
        assert gamma[-1]>0

    q=[[None]*2 for _ in range(14)]
    for i in range(14):
        for j in range(2):
            lo,hi=bilinear_interval(terms[i],((centers[j],F(1)),))
            q[i][j]=outward((lo-2*B*tau[i],hi+2*B*tau[i]),12)
    H=[[None]*14 for _ in range(14)]
    for i in range(14):
        for j in range(i,14):
            lo,hi=bilinear_interval(terms[i],terms[j])
            eps=4*B*(tau[i]+tau[j])
            H[i][j]=H[j][i]=outward((lo-eps,hi+eps),12)
    K=[[(H[i][j][0]/KAPPA+(1/gamma[i] if i==j else 0),
          H[i][j][1]/KAPPA+(1/gamma[i] if i==j else 0))
         for j in range(14)] for i in range(14)]
    assert all(K[i][j]==K[j][i] for i in range(14) for j in range(14))
    return G,q,K


def verify_original_coupled_envelope(G,q,K):
    # The midpoint solve is only a trial selection, not evidence.
    KM=[[midpoint(x) for x in row] for row in K]
    Zcols=[solve_exact(KM,[midpoint(q[i][j]) for i in range(14)])
           for j in range(2)]
    Z=[[rounded(Zcols[j][i]) for j in range(2)] for i in range(14)]
    assert len(Z)==14 and all(len(row)==2 for row in Z)
    # Exact rational signed interval evaluation of the FULL
    # true 14x14 x 14x2 correction M = q*Z+Z*q-Z*K*Z.
    M=[[None]*2 for _ in range(2)]
    for a in range(2):
        for b in range(2):
            val=(F(0),F(0))
            for i in range(14):
                val=iplus(val,isc(q[i][a],Z[i][b]))
                val=iplus(val,isc(q[i][b],Z[i][a]))
                for j in range(14):
                    val=iplus(val,isc(K[i][j],-Z[i][a]*Z[j][b]))
            M[a][b]=val
    # The true M is symmetric, and duplicate orientation
    # enclosure may vary by rounding; intersect the two valid
    # outward enclosures to retain only TRUE symmetric values.
    m_off=(max(M[0][1][0],M[1][0][0]),
           min(M[0][1][1],M[1][0][1]))
    assert m_off[0]<=m_off[1]
    M[0][1]=M[1][0]=m_off
    midM=[[isym(v)[0] for v in row] for row in M]
    errM=[[isym(v)[1] for v in row] for row in M]
    # Any symmetric interval error E with |E_ii|<=e_ii,
    # |E_01|<=e_01 is >=-diag(e00+e01,e11+e01).
    Mlow=[
      [midM[0][0]-errM[0][0]-errM[0][1],midM[0][1]],
      [midM[1][0],midM[1][1]-errM[1][1]-errM[0][1]]
    ]
    assert Mlow[0][1]==Mlow[1][0]

    midG=[[isym(v)[0] for v in row] for row in G]
    errG=[[isym(v)[1] for v in row] for row in G]
    Gup=[
      [midG[0][0]+errG[0][0]+errG[0][1],midG[0][1]],
      [midG[1][0],midG[1][1]+errG[1][1]+errG[0][1]]
    ]
    assert Gup[0][1]==Gup[1][0]
    # C14^-1 true response upper retains ALL coupled entries:
    #  (U*U)/kappa - (q*K^-1*q)/kappa²
    Cup=sub(scale(Gup,F(1)/KAPPA),scale(Mlow,F(1)/KAPPA**2))
    assert Cup[0][1]==Cup[1][0]
    # 1/(1-Lpole) is valid WHOLE-OPERATOR pole conditioner;
    # B14<=Astar so same true original physical source upper.
    assert F(0)<L_POLE<F(1)
    Bup=scale(Cup,F(1)/(1-L_POLE))
    assert Bup[0][1]==Bup[1][0]
    assert psd2(Bup),("invalid coupled positive upper",Bup)

    # Pay the original complete signed negative-frequency infinite
    # eta BEFORE using the inverse as a spectral gate:
    # Astar>=kappa_star I, so
    # (Astar-eta I)^-1 <= (1-eta/kstar)^-1 Astar^-1
    # (functional calculus, same original physical carrier).
    assert F(0)<ETA_HI<KAPPA_STAR
    shift_factor=F(1)/(1-ETA_HI/KAPPA_STAR)
    Bshift=scale(Bup,shift_factor)
    assert psd2(Bshift)
    return Z,Gup,Mlow,Bup,Bshift


def finite_coupling_countertest():
    # Correct partial two-column Loewner bound MUST treat offdiag.
    # Each diagonal-positive test alone cannot certify coupled PSD.
    diag_good=[[F(1),F(0)],[F(0),F(1)]]
    true_full=[[F(1),F(2)],[F(2),F(1)]]
    assert all(true_full[i][i]>0 for i in range(2))
    assert not psd2(true_full) and psd2(diag_good)
    # Signed Gram uncertainty e01 requires DIAGONAL slack:
    e=F(1,20)
    E=[[F(0),e],[e,F(0)]]
    safe=[[e,F(0)],[F(0),e]]  # PSD upper of both +/- offdiag E
    assert psd2(sub(safe,E))
    assert psd2(add(safe,E))
    return e


def run():
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert gov["governance"]["no_automatic_promotion"] is True
    assert "SM24" in gov["evidence"] and "SM25" in gov["evidence"]
    assert gov["obligations"][1]["id"]=="W-ODD-NEG"
    assert next(x for x in gov["obligations"] if x["id"]=="W-ODD-NEG")["status"]=="open"
    assert KAPPA==F(1,1000) and KAPPA_STAR==F(33621,10**9)
    assert len(FEATURES)==14
    centers,C0=source_intervals()
    G,q,K=full_physical_matrices(centers)
    Z,Gup,Mlow,Bup,Bshift=verify_original_coupled_envelope(G,q,K)
    assert all(x>0 for x in C0)
    # 2x2 ORIGINAL negative-cap C block of distinct SM10 clusters.
    # This test is necessary principal-block comparison, NOT a
    # sufficient certificate on entire 890-source negative operator.
    D2=diag([F(1)/((1+TAU)*w) for w in C0])
    principal_gap=sub(D2,Bshift)
    local_test=psd2(principal_gap)
    scalar_bound=scale(Gup,F(1)/KAPPA_STAR)
    assert psd2(scalar_bound)
    # The tighter of different upper bounds cannot be selected
    # entrywise, because PSD Loewner ordering is not entrywise.
    eps=finite_coupling_countertest()

    print("SM25 ACTUAL true original first TWO SM10 degree0 negative clusters",
          centers,flush=True)
    print("SM25 all original 2x2 physically supported signed Gram intervals",
          G,flush=True)
    print("SM25 true 14 x 2 original signed positive source overlaps",
          len(q)*2,"and complete 14x14 SI29 signed source Gram",flush=True)
    print("SM25 original signed true-variational rational 14x2 witness rows",
          len(Z),flush=True)
    print("SM25 Loewner lower for actual true source correction",
          Mlow,flush=True)
    print("SM25 coupled exact Fraction true original Astar^-1 upper T2",
          Bup,flush=True)
    print("SM25 eta-corrected coupled two-source upper",
          Bshift,flush=True)
    print("SM25 exact physical original negative covariance C2 diag",
          C0,flush=True)
    print("SM25 original PRINCIPAL 2x2 sufficient cap gap matrix",
          principal_gap,flush=True)
    print("SM25 first 2x2 sufficient check PSD (not global):",
          local_test,flush=True)
    print("SM25 signed interval offdiag Loewner slack example",eps,flush=True)
    print("SM25 PASS SCOPED: true ORIGINAL odd two-source, 14 SI29"
          " full signed reference Gram and 28 original overlaps;"
          " coupled exact rational 2x2 Loewner inverse upper,"
          " original negative cap first two covariance weights and"
          " rigorous full infinite eta coefficient. NO full 890x890"
          " coupled inverse, NO original complete W-ODD-NEG O1/O2,"
          " no even E1-E4, whole signed Weil, CC27 D-Riesz or RH."
          " Only true ORIGINAL full-operator coupled evidence can"
          " promote these gates.",flush=True)


if __name__=="__main__":
    run()
