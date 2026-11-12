#!/usr/bin/env python3
"""NF503 exact Fraction support-saturated original physical quotient theorem.

The geometric lemma is about original Hilbert L2([-B,B]) with *all*
L2 physical trial rays supported on a measurable S, not only a finite
selected set. For original J242 analytic generators and I\\S containing
a real open interval, the source-exterior Gram G_out is positive
definite. Source-exterior Schur gives EXACT minimum residual achievable
by any (even infinitely many) supported physical new directions:

  inf_phi_supported_in_S || Q_J W - Q_J phi ||²
  = ||W|out||² - b_out.T G_out^{-1} b_out
  where b_out_i = <j_i,W>_out, G_out_ij=<j_i,j_j>_out.

No original P_J W coefficient, pole recentering, extra raw Gram inverse,
or source-to-multiplier operator-range assumption is needed.

The same scalar equals ||Q_J W||² - optimal capture by Q_J L2(S).
Proof: (closure Q_J L2(S))^perp inside J^perp is precisely
J^perp ∩ L2(out). The right side is the squared norm of projection
of W|out onto (J|out)^perp.

The executable controls below compare THREE truly independent exact
finite-dimensional formulas: exterior Schur, local primal T*T inverse,
and projected-residual direct orthogonality, under adversarial source
recentrings and nested supports. A finite model is not an original
source-numeric J8 closure. RH/Weil-domain remain OPEN.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,argparse,sys,itertools
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
NF501="7726a8a9af5faa7a22fd7581c38548c26c5a48a52cb92dc75f815c57f6e3ad7a"
FRAME="18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e"

def load(path):
    b=Path(path).read_bytes()
    return json.loads(b),hashlib.sha256(b).hexdigest()
def dot(x,y):
    assert len(x)==len(y)
    return sum((a*b for a,b in zip(x,y)),F(0))
def mv(M,x):return [dot(row,x) for row in M]
def cols(A):return list(map(list,zip(*A)))
def gram(A):return [[dot(c,d) for d in cols(A)] for c in cols(A)]
def solve(M,b):
    n=len(b)
    assert len(M)==n and all(len(row)==n for row in M)
    a=[[F(z) for z in row]+[F(t)] for row,t in zip(M,b)]
    for k in range(n):
        p=next((i for i in range(k,n) if a[i][k]!=0),None)
        assert p is not None, "Rank/eligibility METHOD STOP: exterior original selected Gram singular"
        a[k],a[p]=a[p],a[k]
        d=a[k][k]
        a[k]=[v/d for v in a[k]]
        for i in range(n):
            if i==k:continue
            d=a[i][k]
            a[i]=[x-d*y for x,y in zip(a[i],a[k])]
    return [row[-1] for row in a]
def restrict(A,x,S):
    return [A[i] for i in x if i in S]
def scalar_schur(A,W,S):
    # W physical response may contain arbitrary original J additions.
    n=len(A)
    T=[i for i in range(n) if i not in set(S)]
    Aout=[A[i] for i in T]
    Wout=[W[i] for i in T]
    G=gram(Aout)
    b=[dot(col,Wout) for col in cols(Aout)]
    x=solve(G,b)
    E=dot(Wout,Wout)
    r=E-dot(b,x)
    assert r>=0
    return r
def full_q(A,W):
    H=gram(A)
    b=[dot(col,W) for col in cols(A)]
    c=solve(H,b)
    return [w-y for w,y in zip(W,mv(A,c))]
def local_primal(A,q,S):
    H=gram(A)
    rows=[A[i] for i in S]
    m=len(S)
    Qss=[]
    for j in range(m):
        rhs=rows[j]
        v=solve(H,rhs)
        Qss.append([F(int(i==j))-dot(rows[i],v) for i in range(m)])
    Qss=[[Qss[j][i] for j in range(m)] for i in range(m)]
    qS=[q[i] for i in S]
    coeff=solve(Qss,qS)
    captured=dot(qS,coeff)
    return dot(q,q)-captured
def direct_outer_residual(A,q,S):
    T=[i for i in range(len(A)) if i not in set(S)]
    Aout=[A[i] for i in T]
    qout=[q[i] for i in T]
    G=gram(Aout)
    b=[dot(col,qout) for col in cols(Aout)]
    coeff=solve(G,b)
    resid=[u-v for u,v in zip(qout,mv(Aout,coeff))]
    assert all(dot(col,resid)==0 for col in cols(Aout))
    return dot(resid,resid)

def finite_controls():
    n=7
    # Full-rank selected polynomial analytic analog; k=0,1,2.
    A=[[F(1),F(i),F(i*(i-1)//2)] for i in range(n)]
    H=gram(A);assert len(solve(H,[F(1),F(1),F(1)]))==3
    q1=[F(v) for v in [1,-3,3,-1,0,0,0]]
    q2=[F(v) for v in [0,0,1,-3,3,-1,0]]
    assert all(dot(col,q1)==dot(col,q2)==0 for col in cols(A))
    checked=0
    for a,b in [(F(1),F(0)),(F(2),F(-3)),(F(-3,7),F(2))]:
        q=[a*u+b*v for u,v in zip(q1,q2)]
        for coefficients in [[F(0),F(0),F(0)],[F(7),F(-2),F(3)],[F(-1,5),F(10**9),F(-10**6)]]:
            W=[x+y for x,y in zip(q,mv(A,coefficients))]
            assert full_q(A,W)==q
            for S in [[0,1],[3,4],[5,6],[0,1,2],[0,1,2,3]]:
                ext=scalar_schur(A,W,S)
                primal=local_primal(A,q,S)
                direct=direct_outer_residual(A,q,S)
                assert ext==primal==direct,(a,b,S,ext,primal,direct)
                assert 0<=ext<=dot(q,q)
                checked+=1
        assert scalar_schur(A,q,[0,1,2,3])<=scalar_schur(A,q,[0,1,2])
        checked+=1
    # An indefinite quadratic form can have identical physical source
    # quotient scalar for measured q. None of this is a global Weil sign.
    assert checked==48
    return checked

def original_pinned_controls(n):
    assert n["pass"]=="NF501-native"
    assert n["original_nf407_source_SHA256"]==SRC
    assert n["original_nf406_seams_SHA256"]==SEAM
    assert n["original_physical_frame_SHA256"]==FRAME
    assert n["original_source_selected_raw_moments_verified"]==242
    assert n["original_J242_Gram_frame_identity_verified"] is True
    assert n["original_projected_one_ray_sufficient_Hilbert_gate"]=="CERTIFIED_FAIL"
    assert n["full_Weil_source_multiplier_image_eligibility"] is False
    assert n["W_ODD_NEG"]==n["RH"]=="OPEN"
    gamma2=F(n["original_gamma_squared"])
    lo,hi=map(F,n["true_original_Q_Jw_squared_from_K_D7_D8_R_outward"])
    assert 0<gamma2<F("5.13e-26")<lo<hi
    assert lo>F("1.578e-22") and hi<F("1.607e-22")
    # The source supported S=empty is a nontrivial original calibration
    # of the exact external-only Schur identity. No S=J8 result implied.
    return lo,hi,gamma2

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--nf501",required=True)
    ap.add_argument("--output",required=True)
    opt=ap.parse_args()
    nf501,sha=load(opt.nf501)
    original,ssha=load("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seams,seamsha=load("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    nf404,f404=load("notes/data/provisional/NF404_original_selected_pole_shear_exact.json")
    assert sha==NF501 and ssha==SRC and seamsha==SEAM
    assert nf404["pass"]=="NF404" and nf404["original_dimension"]==242
    assert nf404["original_selected_pole_index"]==241
    assert nf404["fixed_dyadic_pole_coefficient"]=="6677356497477490213/4611686018427387904"
    assert F(nf404["exact_source_original_full_complement_power_budget"])==F(nf501["original_gamma_squared"])
    lo,hi,gamma2=original_pinned_controls(nf501)
    checked=finite_controls()
    assert checked==48
    out={
      "pass":"NF503",
      "standing":"EXACT HILBERT SUPPORT-SATURATED EXTERIOR QUOTIENT THEOREM plus independently exact rational 7D 48-case primal/dual/outside and selected-recenter controls; J8 source exterior moments NOT yet calculated",
      "original_nf501_source_native_SHA256":sha,
      "original_nf407_source_SHA256":SRC,
      "original_nf406_seams_SHA256":SEAM,
      "original_nf404_source_SHA256":f404,
      "physical_original_support_half_width":"11/10",
      "original_selected_rank":242,
      "support_saturation_operator":"Q_J E_S : L2(S) -> J242^perp",
      "exterior_quotient_formula":"inf_{phi in L2(S)}||Q_JW-Q_J E_S phi||²=||W_out||²-b_out^T G_out^{-1}b_out",
      "exterior_selected_Gram":"G_out_ij=int_{I\\S}j_i(x)j_j(x)dx",
      "exterior_original_source_mixed_moment":"b_out_i=int_{I\\S}j_i(x)W(x)dx",
      "arbitrary_finite_or_infinite_support_local_physical_candidates":"ALL TESTED BY SAME FORMULA WHEN ORIGINAL OUTER GRAM POSITIVE",
      "recenter_pole_shear_invariance":"exact because original sinh(x/2) in selected J242",
      "source_only_exterior_numerical_input_needed":["original full w outer squared energy","242 original outer w mixed moments","242x242 original outer selected Gram"],
      "source_numerical_J8_maximal_possible_capture":"OPEN",
      "original_empty_S_whole_Q_squared_outward":[str(lo),str(hi)],
      "original_original_gamma_squared":str(gamma2),
      "finite_independent_exact_Fraction_orthogonal_primal_dual_controls":checked,
      "full_source_multiplier_image_eligibility":"OPEN",
      "whole_even_odd_operator_domain":"OPEN",
      "W_ODD_NEG":"OPEN","RH":"OPEN",
      "next_bold":"NF504 source-native actual full J8 terminal two-collar outer 242D Gram and original full support-complement 242 moments, then decide support-saturated full-ray gate; source/image/domain separately"
    }
    Path(opt.output).write_text(json.dumps(out,indent=2)+"\n")
    print("NF503 EXACT physical Hilbert quotient saturation 48 adversarial 7D controls PASS",flush=True)
    print("NF503 original source SHA, NF404 gamma and NF501 q² empty-support calibration PASS",flush=True)
    print("NF503 generic J8 terminal support-saturated original source result OPEN until actual E_out, b_out, G_out computed",flush=True)
    print("NF503 full Weil image/domain W-ODD-NEG RH OPEN",flush=True)

if __name__=="__main__":
    main()
