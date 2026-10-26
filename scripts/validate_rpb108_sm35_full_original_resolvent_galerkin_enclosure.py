#!/usr/bin/env python3
"""SM35 exact full-original odd 470-source Galerkin RESOLVENT enclosure.

Actual original mathematical statement (conditional on inherited original
SI10/SI29/SM33/SM34 signed Fourier and domain proofs):
  J:R^470 -> H_odd, 469 genuine b9 odd physical Taylor generators
  plus original pole s, ANALYTICALLY LINEARLY INDEPENDENT because
  positive cluster centers are distinct and exp-polynomials with
  frequency ±2pi i c_j and ±1/2 have unique coefficients.
  A=Astar=Ao-2|s><s| >= kstar I, whole original pole/arch included.
  K=Kneg full genuine seven-prime negative Fourier, 0<=K<=H I.
  Z is full A-Galerkin trial: V*(J-AZ)=0 with V superset E0.
  R=J-AZ; G0=Z*AZ, E=R*R, N0=Z*KZ.
  TRUE 470x470 full matrices:
   G=J*A^-1 J=G0+R*A^-1 R >=G0
   N=J*A^-1 K A^-1 J
    <=(1+t)N0+(1+1/t)*H/kstar² E, t>0.
  Original SM10 107/890 full cap upper K<=UDU*+eta I
  permits N0<=Z*UDU*Z+eta Z*Z.
  If entire 470x470 matrix above <=51/56 G0, SM34 gives
  ORIGINAL whole odd positivity. THE ACTUAL 470x470 MATRICES ARE
  NOT BUILT OR CERTIFIED BY THIS SCRIPT. Canonical W-ODD-NEG OPEN.

Regression proves full exact 3D nonzero-residual Galerkin example with
2D coupled source, two-sided original-style Loewner inequalities and
an adverse original-style example with positive first Ritz but failing
second source and complete 2x2 matrix. These are algebra tests only.
Exact original 107 cluster geometry/470 independent source analytic
premises and 973 leaves/890 cap are replayed with Fraction arithmetic.
"""
from fractions import Fraction as F
from pathlib import Path
import json

from validate_rpb108_si10_complement_positivity import (
    protected_inner_cover,B,KAPPA
)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_sm33_original_odd_negative_mixed_bound import (
    full_original_clusterwise_negative_mixed
)
from validate_rpb108_sm10_explicit_odd_cap_moments import (
    full_upper_leaves,BITS as NEG_BITS,TAU
)
from validate_rpb108_sm17_compact_spectral_gate import (
    KAPPA_STAR, ETA_UP
)
from validate_rpb108_sm34_positive_energy_dual_schur import CLEAN_THRESHOLD
ROOT=Path(__file__).resolve().parents[1]


def mat(rows): return [[F(x) for x in row] for row in rows]
def transpose(M): return list(map(list,zip(*M)))
def mm(X,Y):
    assert len(X[0])==len(Y)
    return [[sum((X[i][k]*Y[k][j] for k in range(len(Y))),F(0))
             for j in range(len(Y[0]))] for i in range(len(X))]
def scale(c,X):return [[c*x for x in row] for row in X]
def add(X,Y):return [[a+b for a,b in zip(x,y)] for x,y in zip(X,Y)]
def sub(X,Y):return add(X,scale(F(-1),Y))
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def inv(A):
    n=len(A)
    t=[list(A[i])+eye(n)[i] for i in range(n)]
    for i in range(n):
        assert t[i][i]!=0
        piv=t[i][i];t[i]=[x/piv for x in t[i]]
        for j in range(n):
            if j==i:continue
            f=t[j][i]
            t[j]=[a-f*b for a,b in zip(t[j],t[i])]
    return [row[n:] for row in t]
def quad(X,v):
    return sum((v[i]*sum((X[i][j]*v[j] for j in range(len(v))),F(0))
                for i in range(len(v))),F(0))
def psd2(X,strict=False):
    assert len(X)==len(X[0])==2 and X[0][1]==X[1][0]
    d=X[0][0]*X[1][1]-X[0][1]**2
    return X[0][0]>0 and d>0 if strict else X[0][0]>=0 and d>=0 and X[1][1]>=0


def actual_original_basis_and_cap_geometry():
    clusters,width,mass,n_unresolved,n_protected=protected_inner_cover()
    assert n_unresolved==973 and n_protected==9261
    assert len(clusters)==107 and width==F(973,32)
    assert KAPPA==F(1,1000) and B==F(11,10)
    # Explicit original odd basis: for k even x^k sin(2pi c_jx)
    # and for k odd x^k cos(2pi c_jx); original odd pole s.
    # Positive disjoint original cluster center frequencies are
    # distinct, so the +/- imaginary exponential-polynomial
    # exponents and +/- 1/2 of s cannot overlap.
    orders=[]
    centers=[]
    odd_sin=odd_cos=0
    for l,r,weight in clusters:
        assert l<r and weight>=0
        center=(l+r)/2
        assert center>0
        if centers:
            assert center>centers[-1]
        centers.append(center)
        order,_=taylor_order(r-l,9)
        orders.append(order)
        odd_sin+=(order+1)//2
        odd_cos+=order//2
    assert len(set(centers))==107
    assert sum(orders)==469 and odd_sin==260 and odd_cos==209
    assert 469+1==470
    assert centers[-1]<896
    # No numerical lower eigenvalue of physical 470 basis Gram
    # is inferred from analytic linear independence.

    # Whole true K negative original-frequency cap remains ALL
    # original 107 complete moment covariance clusters and
    # exactly 890 finite true sine-Taylor source directions;
    # the infinite eta residual remains positive in the cap.
    cap,W,Mneg,Mnegk=full_upper_leaves()
    assert len(cap)==107 and W==width
    cols=sum(taylor_order(cl[-1][1]-cl[0][0],NEG_BITS)[0]
             for cl in cap)
    assert cols==890 and TAU==F(1,1024)
    assert F(0)<ETA_UP<KAPPA_STAR
    assert Mneg==mass
    assert Mnegk==mass+KAPPA*width
    # True original Kminus=(kappa-m)_+ global norm upper inherited
    # from CORRECTED SM33: pay h+kappa on EVERY unresolved cell.
    # This equals the complete original SM10 cap mass Mneg+kappa*W.
    s=full_original_clusterwise_negative_mixed()
    assert s["source_count"]==470 and s["legacy_h_only_mass"]==mass
    assert s["mass"]==mass+KAPPA*width==Mnegk
    H=s["neg_global_norm"]
    assert H==2*B*(mass+KAPPA*width) and F(80)<H<F(83)
    # Exact original resolvent-error tolerance for t=1 and
    # trial N0 <= theta/4 G0, entirely unachieved at this stage.
    threshold=CLEAN_THRESHOLD*KAPPA_STAR**2/(4*H)
    assert F(3,10**12)<threshold<F(4,10**12)
    assert CLEAN_THRESHOLD==F(51,56)
    return dict(clusters=len(clusters),leaves=n_unresolved,
                protected=n_protected,odd_sin=odd_sin,odd_cos=odd_cos,
                source_dim=odd_sin+odd_cos+1,cap_columns=cols,
                full_negative_mass=mass,full_negative_norm=H,
                residual_budget=threshold)


def galerk3_model(Kdiag):
    # COMPLETELY FINITE exact rational model, NOT original 470
    # physical Gram. A SPD with off-trial coupling and lower >=1:
    A=mat([[2,0,F(1,10)],[0,3,F(1,10)],
           [F(1,10),F(1,10),2]])
    J=mat([[1,0],[0,1],[0,0]])
    # Full 2-source simultaneous Galerkin using V=span(e1,e2)
    Z=mat([[F(1,2),0],[0,F(1,3)],[0,0]])
    K=mat([[Kdiag[0],0,0],[0,Kdiag[1],0],[0,0,Kdiag[2]]])
    H=max(Kdiag)
    kstar=F(1)
    R=sub(J,mm(A,Z))
    assert R[2][0]!=0 and R[2][1]!=0 # TRUE nonzero residual
    assert mm(transpose(Z),R)==mat([[0,0],[0,0]]) # Galerkin
    G0=mm(mm(transpose(Z),A),Z)
    H0=mm(transpose(R),R)
    Ai=inv(A)
    G=mm(mm(transpose(J),Ai),J)
    G_exact=add(G0,mm(mm(transpose(R),Ai),R))
    assert G==G_exact
    assert psd2(sub(G,G0))
    assert psd2(sub(add(G0,scale(1/kstar,H0)),G))
    N0=mm(mm(transpose(Z),K),Z)
    N=mm(mm(mm(mm(transpose(J),Ai),K),Ai),J)
    t=F(1)
    Nup=add(scale(1+t,N0),scale((1+1/t)*H/kstar**2,H0))
    assert psd2(sub(Nup,N))
    assert psd2(N) and psd2(G0,strict=True)
    accepted=psd2(sub(scale(CLEAN_THRESHOLD,G0),Nup))
    return dict(A=A,J=J,Z=Z,R=R,G0=G0,G=G,
                N0=N0,N=N,Nup=Nup,accepted=accepted,H=H,
                residual=H0,theta=CLEAN_THRESHOLD)


def exact_full_matrix_regression():
    good=galerk3_model((F(1,8),F(1,8),F(1,16)))
    assert good["accepted"]
    assert psd2(sub(scale(CLEAN_THRESHOLD,good["G"]),
                    good["N"]))
    # Original-style adverse model: one source direction positive
    # but the other violates the full 2x2 matrix. No componentwise
    # inference from the first diagonal or selected 1D Ritz block.
    bad=galerk3_model((F(1,8),F(4),F(1,16)))
    assert not bad["accepted"]
    assert CLEAN_THRESHOLD*bad["G"][0][0]>bad["N"][0][0]
    assert CLEAN_THRESHOLD*bad["G"][1][1]<bad["N"][1][1]
    assert not psd2(sub(scale(CLEAN_THRESHOLD,bad["G"]),bad["N"]))
    assert good["residual"][0][1]!=0
    return good,bad


def run():
    m=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(o for o in m["obligations"] if o["id"]=="W-ODD-NEG")
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]=="open"
    assert m["governance"]["no_automatic_promotion"] is True
    assert odd["status"]=="open" and "O1/O2" in odd["acceptance"]
    assert all(x in m["evidence"] and x in odd["evidence"]
               for x in ("SM33","SM34","SM35"))
    assert "original_odd_470_galerkin_residual_gate" in m["governance"]
    g=actual_original_basis_and_cap_geometry()
    good,bad=exact_full_matrix_regression()
    print("SM35 original SI10 107 signed cluster centers distinct"
          " and positive, 469 original polynomial degree sources"
          " plus one original odd pole => analytic independent"
          " physical odd dimension EXACT",g["source_dim"],flush=True)
    print("SM35 actual original source parity sine/cosine",
          g["odd_sin"],g["odd_cos"],"973 negative leaves",
          g["leaves"],"107 clusters and original SM10"
          " negative 890-cap columns",g["cap_columns"],flush=True)
    print("SM35 actual original full negative multiplier mass",
          float(g["full_negative_mass"]),"true K norm bound",
          float(g["full_negative_norm"]),flush=True)
    print("SM35 original positive pole conditioned kappa_star",
          KAPPA_STAR,"and whole 470-source theta=51/56",
          CLEAN_THRESHOLD,flush=True)
    print("SM35 conditional t=1 and trial N0<=theta/4 G0"
          " actual full ORIGINAL source residual-squared"
          " matrix tolerance coefficient",float(g["residual_budget"]),
          "(STRICT not measured)",flush=True)
    print("SM35 exact NONZERO RESIDUAL 3D original-style"
          " full two-source coupled Galerkin toy gate PASSES",
          good["accepted"],"matrix upper",
          [[float(x) for x in row] for row in good["Nup"]],flush=True)
    print("SM35 exact adverse whole-coupled toy gate fails while"
          " first 1D source test passes; no false full"
          " original promotion",not bad["accepted"],flush=True)
    print("SM35 PASS SCOPED: rigorous entire original 470-source"
          " Galerkin strong residual matrix identity and"
          " complete signed-negative cap upper -> full Loewner"
          " sufficient operator acceptance theorem, with exact"
          " original source geometry and conditioned precision"
          " budget. ACTUAL true original source stiffness,"
          " resolvent residual, 470x470 G/N and 890 physical"
          " mixed cap Gram NOT computed; no W-ODD-NEG O1/O2,"
          " even E1-E4, full signed Weil, CC27 D-Riesz or RH."
          " Independent original analytic review needed.",flush=True)


if __name__=="__main__":
    run()
