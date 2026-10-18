#!/usr/bin/env python3
"""PS36: fail-closed typed ORIGINAL spectral acceptance and exact Fraction logic.

This is a STRUCTURAL ACCEPTANCE REGRESSION, NOT a certificate of
the uncomputed original source-eliminated even lambda1/index, true
positive-ground orthogonal remainder, d-pole beta/Delta, or actual
all-frequency odd signed operator positivity.
Supports accepted PS27/PS29 structural implications only.
"""
import json
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
GATE_PATH=ROOT/"research/typed_spectral_acceptance.json"
OBL_PATH=ROOT/"research/obligations.json"
PS_PATH=ROOT/"research/parallel_investigations/w_physical_shift.json"

EVEN_KEYS=[
    "E1_NEGATIVE_INDEX",
    "E2_FULL_GROUND_ORTHOGONAL_REMAINDER",
    "E3_EFFECTIVE_POLE_NULL_AND_ANGLE",
    "E4_POLE_COMPENSATION_AND_EVEN_COMPLETE",
]
ODD_KEYS=["O1_COMPLETE_ODD_SIGNED_OPERATOR",
          "O2_COMPLETE_ODD_RESIDUAL_SPECTRAL_CLASSIFICATION"]
CROSS_KEYS=["C1_PARITY_COMPOSITION","C2_NATIVE_DOMAIN_AND_RH"]


def dot(x,y):
    return sum((a*b for a,b in zip(x,y)),F(0))

def quadratic(a,v):
    assert len(a)==len(v)
    return sum((v[i]*a[i][j]*v[j]
                for i in range(len(v)) for j in range(len(v))),F(0))

def determinant(a):
    n=len(a)
    assert all(len(row)==n for row in a)
    if n==0:return F(1)
    if n==1:return a[0][0]
    return sum(((-1 if i%2 else 1)*a[0][i]*
                determinant([row[:i]+row[i+1:] for row in a[1:]])
                for i in range(n)),F(0))

def principal_psd(a):
    n=len(a)
    assert all(len(row)==n for row in a)
    assert all(a[i][j]==a[j][i] for i in range(n) for j in range(n))
    return all(determinant([[a[i][j] for j in ix] for i in ix])>=0
               for k in range(1,n+1) for ix in combinations(range(n),k))

def rank_one_restore(lam,d,alpha):
    return [[(lam[i] if i==j else F(0))+alpha*d[i]*d[j]
             for j in range(len(d))] for i in range(len(d))]

def full_spectral_regression():
    # Positive-simple ground does NOT imply index exactly one.
    # L=-3I-J_3, with J all-ones, connected offdiagonal -1,
    # ground phi=(1,1,1) eigenvalue -6, orth eigs -3,-3.
    L=[[-F(4),-F(1),-F(1)],
       [-F(1),-F(4),-F(1)],
       [-F(1),-F(1),-F(4)]]
    phi=[F(1),F(1),F(1)]
    v=[F(1),F(-1),F(0)]
    w=[F(1),F(1),F(-2)]
    assert dot(phi,v)==dot(phi,w)==dot(v,w)==0
    assert all(dot(row,phi)==-6*phi[i] for i,row in enumerate(L))
    assert all(dot(row,v)==-3*v[i] for i,row in enumerate(L))
    assert all(dot(row,w)==-3*w[i] for i,row in enumerate(L))
    assert quadratic(L,v)<0 and quadratic(L,w)<0
    for alpha in (F(1),F(100),F(10**6)):
        # Even a very strong POSITIVE coherent pole on phi
        # cannot remove negative phi-orthogonal modes.
        LR=[[L[i][j]+alpha*phi[i]*phi[j] for j in range(3)]
            for i in range(3)]
        assert quadratic(LR,v)==quadratic(L,v)<0
        assert quadratic(LR,w)==quadratic(L,w)<0

    # Complete full-source Schur, not positive individual blocks.
    A=F(2); D=F(1,4); B=F(1)
    assert A>0 and D>0
    schur=D-B*B/A
    assert schur==F(-1,4) and schur<0
    assert A*D<B*B  # (alpha-mu)*(beta-mu)>gamma² fails
    assert determinant([[A,B],[B,D]])==A*schur<0

    # Spectral correction iff alpha Delta >= |lambda0|
    # after index=1, null orthogonality, and Delta>0.
    lam_abs=F(2)
    a=F(2); b=[F(1),F(1,2)]
    mu=[F(3),F(5)]
    beta=sum((b[i]**2/mu[i] for i in range(2)),F(0))
    delta=a*a-lam_abs*beta
    alpha_threshold=lam_abs/delta
    assert beta==F(23,60) and delta==F(97,30)
    assert alpha_threshold==F(60,97)
    for alpha in (F(1,2),alpha_threshold,F(1)):
        Lfull=rank_one_restore(
            [-lam_abs,*mu],[a,*b],alpha)
        expected=alpha>=alpha_threshold
        assert principal_psd(Lfull)==expected
        # Actual Schur after eliminating ALL positive directions
        # (not omitting source-mode cross).
        scalar=-lam_abs+alpha*a*a/(1+alpha*beta)
        assert (scalar>=0)==expected

    # A source-renormalized positive pole that couples to a NULL
    # direction does NOT repair one negative mode by any alpha.
    Lnull=[[-F(1),F(0),F(0)],
           [F(0),F(0),F(0)],
           [F(0),F(0),F(2)]]
    dnull=[F(1),F(1),F(0)]
    cancellation=[F(1),F(-1),F(0)]
    assert dot(dnull,cancellation)==0
    assert quadratic(Lnull,cancellation)==-1
    for alpha in (F(1),F(1000)):
        restored=[[Lnull[i][j]+alpha*dnull[i]*dnull[j]
                   for j in range(3)] for i in range(3)]
        assert quadratic(restored,cancellation)==-1

    # Delta==0 yields K_eff PSD but no FINITE restored PSD.
    for alpha in (F(1,10),F(1),F(1000000)):
        eq=rank_one_restore([-F(1),F(1)],[F(1),F(1)],alpha)
        assert determinant(eq)==-1 and not principal_psd(eq)
        assert quadratic([[-F(1),F(0)],[F(0),F(1)]],[F(1),-F(1)])==0

    # Complete odd: individual nonnegative signed diagonal
    # is insufficient when full negative packets CROSS.
    Astar=[[F(1),F(0)],[F(0),F(1)]]
    Kneg=[[F(1),F(1)],[F(1),F(1)]]
    Wodd=[[Astar[i][j]-Kneg[i][j] for j in range(2)]
          for i in range(2)]
    assert all(Wodd[i][i]>=0 for i in range(2))
    assert quadratic(Wodd,[F(1),F(1)])==-2
    assert not principal_psd(Wodd)
    # R=[1,1]: full Birman-Schwinger R Astar^-1 R* =2>1.
    r=[F(1),F(1)]
    assert dot(r,r)==2>1
    return beta,delta,alpha_threshold,schur


def check_repository_contract():
    g=json.loads(GATE_PATH.read_text())
    ob=json.loads(OBL_PATH.read_text())
    ps=json.loads(PS_PATH.read_text())
    assert g["schema_version"]==1
    assert g["canonical_active_obligation"]=="W-ODD-NEG"
    assert g["objective_status"]=="open"
    assert g["no_automatic_promotion"] is True
    assert ob["active_obligation"]=="W-ODD-NEG"
    assert ob["objective"]["status"]=="open"
    assert ob["governance"]["no_automatic_promotion"] is True
    assert ob["governance"]["typed_spectral_acceptance_ref"]=="research/typed_spectral_acceptance.json"
    assert ps["id"]=="W-PHYSICAL-SHIFT"
    assert ps["active_frontier_unchanged"]=="W-ODD-NEG"
    assert ps["checkpoints"][-1]["id"]=="PS36"
    assert ps["status"]=="open" and all(v is False for v in ps["closures"].values())
    gates=g["gates"]
    assert list(gates)==EVEN_KEYS+ODD_KEYS+CROSS_KEYS
    assert g["semantic_status"]=="acceptance_contracted_open"
    assert all(x is False for x in g["closure_flags"].values())
    assert g["proven_scoped_baseline"]["status"]=="proved_conditional_on_inherited_analytic_premises"
    for i,key in enumerate(EVEN_KEYS+ODD_KEYS+CROSS_KEYS):
        v=gates[key]
        assert v["status"]=="open" and v["required_evidence"]
        assert v["forbidden_shortcuts"]
        assert v["scope"] in {
            "COMPLETE_COMPLEMENT","COMPLETE_PARITY",
            "WHOLE_SIGNED_WEIL","NATIVE_TRANSFER_RH"}
        for dep in v.get("prerequisites",[]):
            assert dep in gates and gates[dep]["status"]=="open"
        assert len(set(v.get("prerequisites",[])))==len(v.get("prerequisites",[]))
    assert gates["E3_EFFECTIVE_POLE_NULL_AND_ANGLE"]["prerequisites"]==EVEN_KEYS[:2]
    assert gates["E4_POLE_COMPENSATION_AND_EVEN_COMPLETE"]["prerequisites"]==EVEN_KEYS[:3]
    assert gates["C1_PARITY_COMPOSITION"]["prerequisites"]==[EVEN_KEYS[3],*ODD_KEYS]
    assert gates["C2_NATIVE_DOMAIN_AND_RH"]["prerequisites"]==[CROSS_KEYS[0]]
    assert [x["tier"] for x in g["scope_levels"]]==list(range(1,7))
    assert all(x["closure_eligible"] is False for x in g["scope_levels"][:3])
    assert set(g["typed_components"]["primes"])=={2,3,4,5,7,8,9}
    assert "BEFORE" in g["typed_components"]["even_pole_policy"]
    assert "negative" in g["typed_components"]["odd_pole_policy"]
    even=next(o for o in ob["obligations"] if o["id"]=="W-EVEN-FORM")
    odd=next(o for o in ob["obligations"] if o["id"]=="W-ODD-NEG")
    assert even["status"]==odd["status"]=="open"
    assert "E1" in even["acceptance"] and "E4" in even["acceptance"]
    assert "O1" in odd["acceptance"] and "O2" in odd["acceptance"]
    assert g["analytical_review"]=="pending"
    return True


def run():
    check_repository_contract()
    beta,delta,alpha_threshold,schur=full_spectral_regression()
    print("PS36 typed original spectral acceptance: all 8 complete parity/Weil/bridge gates OPEN",flush=True)
    print("PS36 inherited original even ind_-(L)>=1; ind_-(L)=1/lambda1>=0 UNPROVED",flush=True)
    print("PS36 ground simple/positive 3x3 irreducible exact counterexample has 3 negative eigenvalues",flush=True)
    print("PS36 original STYLE full source Schur despite positive diagonal",schur,flush=True)
    print("PS36 exact 3x3 pole beta",beta,"Delta",delta,"alpha threshold",alpha_threshold,flush=True)
    print("PS36 nullspace coupling, Delta=0 no-finite-pole, and full odd cross sign counterexamples PASS",flush=True)
    print("PS36 PASS SCOPED: typed POSITIVITY and COMPOSITION acceptance contract fail-closed."
          " Original even negative index, full orthogonal PSD, original effective pole"
          " Delta/alpha margin, original complete odd sign/residual, native CC27 D-Riesz"
          " and full Weil/RH remain OPEN. Exact toy Fraction algebra is NOT original"
          " infinite-dimensional sign certification.",flush=True)


if __name__=="__main__":
    run()
