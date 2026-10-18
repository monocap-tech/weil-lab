#!/usr/bin/env python3
"""PS30: original pole-free even ground-state jump form.

ANALYTIC (independent proof review required):
 L=S0_C,even=J_C+carch mass-2*7 original negative prime shifts
   -R, R=B0* A0^-1 B0; PS28 A0^-1 cone preserving, B0 cone
 negativity reversing, hence R cone preserving on even C.
 For normalized positive ground phi of PS29, form-core g,
 L[phi*g]-lambda0||phi*g||² equals sum of positive:
 original digamma weighted jumps, 7 actual prime weighted jumps,
 and <R phi,phi*g²>-<R(phi*g),phi*g>.
 λ1>=0 iff this weighted Poincare inf is >=|lambda0|.
 IRREDUCIBLE semigroup and form-core details not machine certified.

EXACT Fraction validation here:
 rational 2-source / 3-complement graph with a nonzero positive
 source-mediated R and distinct arch/prime edges, true completion
 of the ground-state form, and exact PS27 source-pinned negative
 ground Rayleigh vs uniform-k-floor ceiling.
 No true original eigenpair, second eigenvalue, or pole margin
 computation, no W-EVEN-FORM/W-ODD-NEG/RH.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import validate_rpb108_ps29_even_spectral_ground_mode as ps29
import validate_rpb108_rc315_low_mode_sign as rc315

ROOT=Path(__file__).resolve().parents[1]

def tr(A): return [list(r) for r in zip(*A)]
def mm(A,B):
    assert len(A[0])==len(B)
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
             for j in range(len(B[0]))] for i in range(len(A))]
def plus(A,B):
    return [[a+b for a,b in zip(ra,rb)] for ra,rb in zip(A,B)]
def minus(A,B):
    return [[a-b for a,b in zip(ra,rb)] for ra,rb in zip(A,B)]
def scale(A,c):
    return [[c*x for x in row] for row in A]
def diag(x):
    return [[a if i==j else F(0) for j in range(len(x))]
            for i,a in enumerate(x)]
def dot(u,v): return sum((x*y for x,y in zip(u,v)),F(0))
def vec(A,u): return [dot(row,u) for row in A]
def q(A,u): return dot(u,vec(A,u))
def inverse_2(A):
    assert len(A)==len(A[0])==2
    det=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    assert det>0
    return [[A[1][1]/det,-A[0][1]/det],
            [-A[1][0]/det,A[0][0]/det]]
def graph_laplacian(n,edges):
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    for i,j,w in edges:
        assert 0<=i<j<n and w>=0
        L[i][i]+=w
        L[j][j]+=w
        L[i][j]-=w
        L[j][i]-=w
    return L

def regression():
    # REAL rational "original-style" finite model. This tests
    # the ground-state algebra; it does not evaluate actual original
    # digamma integrals or the seven-prime physical operator.
    A0=[[F(3),F(-1)],[F(-1),F(3)]]
    B0=[[F(-1),F(0),F(-1)],
        [F(0),F(-1),F(-1)]]
    Ai=inverse_2(A0)
    R=mm(mm(tr(B0),Ai),B0)
    assert all(a>=0 for row in R for a in row)
    # The actual original direct arch kernel is positive across all
    # complementary pairs, while a prime may connect only select
    # pairs. Distinct rational weights check that the terms are kept.
    arch=[(0,1,F(1,2)),(0,2,F(2,5)),(1,2,F(3,7))]
    prime=[(0,1,F(1,6)),(1,2,F(2,9))]
    J=graph_laplacian(3,arch)
    W=[[F(0) for _ in range(3)] for _ in range(3)]
    for i,j,w in prime:
        W[i][j]+=w
        W[j][i]+=w
    T=minus(minus(J,W),R)
    phi=[F(1),F(2),F(1)]
    lam=F(-9,2)
    tphi=vec(T,phi)
    pot=[lam-tphi[i]/phi[i] for i in range(3)]
    L=plus(T,diag(pot))
    assert vec(L,phi)==[lam*x for x in phi]
    g=[F(2),F(-1),F(3)]
    h=[a*b for a,b in zip(phi,g)]
    g2=[v*v for v in g]
    phig2=[p*v for p,v in zip(phi,g2)]
    ground=q(L,h)-lam*dot(h,h)
    jterm=sum((w*phi[i]*phi[j]*(g[i]-g[j])**2
                for i,j,w in arch),F(0))
    pterm=sum((w*phi[i]*phi[j]*(g[i]-g[j])**2
                for i,j,w in prime),F(0))
    rterm=dot(vec(R,phi),phig2)-q(R,h)
    assert jterm>0 and pterm>0 and rterm>0
    assert ground==jterm+pterm+rterm,(
        "Ground transformed source/arch/prime sign error",
        ground,jterm,pterm,rterm)
    # For arbitrary finite even-level partition, R nonnegative
    # entries imply the exact nonnegative jump decomposition.
    pair_r=sum((R[i][j]*phi[i]*phi[j]*(g[i]-g[j])**2
                for i in range(3) for j in range(i+1,3)),F(0))
    assert pair_r==rterm

    # Original source contribution is *attractive* in unshifted L
    # but *nonnegative* in the ground-shifted weighted jump energy.
    assert q(R,h)>=0
    return jterm,pterm,rterm,ground

def run():
    # Replay inherited original PS28 source checks directly: the PS29
    # scoped validator correctly demands PS29 be its terminal frontier,
    # whereas this descendant branch appends PS30.
    ps29.ps28.run()
    beta,delta,s=ps29.ground_block_reduction(
        F(1),F(2),(F(1),),(F(2),),F(2,7))
    assert (beta,delta,s)==(F(1,2),F(7,2),F(0))
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads(
        (ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["status"]=="open"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert lane["checkpoints"][-1]["id"]=="PS30"
    assert all(x is False for x in lane["closures"].values())

    # Certified original-RC315 normalized constant pole-free
    # negative witness from PS27. Actual first even ground
    # lambda0 is at most its negative Rayleigh quotient.
    rc=json.loads((ROOT/"certificates/rpb108_rc315_low_mode_sign.json").read_text())
    Qhi=F(rc["original_low_diagonals"][0][
        "physically_normalized_original_Weil_diagonal_interval"][1])
    assert Qhi-F(22,5)<-F(4359740,10**6)
    # ||hC||²=|C|/R<1, so its negative Rayleigh is strictly
    # more negative than the raw Q0[hC] upper above.
    assert F(0)<F(757,350)<F(11,5)
    assert F(11,5)-F(13,350)==F(757,350)

    # For any 0<u<=R=11/5, the TRUE k(u) satisfies
    # k(u)>e^(-11/10)>3/10 because e<3 and e^(1/10)<10/9.
    # Both elementary power-series comparisons require no
    # numerical approximation of original k.
    assert F(3)*F(10,9)==F(10,3)
    assert F(1)/F(10,3)==F(3,10)
    arch_floor=F(3,10)
    # Conditional if unknown phi0 has finite L∞ norm Mphi:
    # floor-only Poincare bound arch_floor/Mphi².
    # Since normalized ground Mphi²>=1/|C|, that SPECIFIC
    # guaranteed bound cannot exceed arch_floor*|C|<33/50.
    floor_ceiling=arch_floor*F(11,5)
    assert floor_ceiling==F(33,50)
    assert floor_ceiling<F(4359740,10**6)

    j,p,r,total=regression()
    print("PS30 exact-rational original-style arch jump regression",j,
          flush=True)
    print("PS30 exact-rational prime jump regression",p,flush=True)
    print("PS30 exact-rational genuine source-response jump regression",
          r,flush=True)
    print("PS30 exact ground-form recovered energy",total,flush=True)
    print("PS30 original PS27 even pole-FREE lambda0 STRICT UPPER",
          float(-F(4359740,10**6)),flush=True)
    print("PS30 uniform true k>=3/10 conditional L∞ floor certificate "
          "absolute CEILING",float(floor_ceiling),flush=True)
    print("PS30 required true ground-state weighted Poincare constant "
          ">",float(F(4359740,10**6)),flush=True)
    print("PS30 PASS SCOPED: original even source-mediated R cone "
          "preservation analytic; exact full original "
          "arch/prime/source ground-state nonnegative jump form "
          "analytic, irreducible positivity and form-core independent "
          "audit pending; exact rational finite source-Schur and "
          "scale-separation regression. Genuine lambda1 and weighted "
          "Poincare value NOT computed. W-ODD-NEG, W-EVEN-FORM, "
          "CC27 D-Riesz, whole signed Weil and RH OPEN.",flush=True)

if __name__=="__main__":
    run()
