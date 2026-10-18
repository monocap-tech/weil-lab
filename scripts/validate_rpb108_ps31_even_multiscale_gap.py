#!/usr/bin/env python3
"""PS31: original PS30 even-ground jump exponential layers and graph gate.

ORIGINAL ANALYTIC (requires independent review of PS28-30):
  k(u)=sum_{j>=0}exp(-(2j+1/2)*u).
  For even phi,g on PS15 C, exact original digamma ground jump
  J=2 int_{x>y, x,y in C+} [k(x-y)+k(x+y)]
       phi(x)phi(y)(g(x)-g(y))^2 dxdy.
  Let mu=2phi^2 dx and W_N=K_N/(2phi(x)phi(y)).
  If w_ij<=essinf_{Ai x Aj}W_N, and mu_i are the
  genuine positive original phi² bin masses, the finite graph
  Loewner/within-bin test gap>=rho lower bounds lambda1-lambda0.

SCOPED exact rational checks, NOT original phi mass certification:
  geometric/exponential identity at ORIGINAL displacement 2log2,
  Taylor envelopes on original B=11/10, even mirror 4-node graph,
  2/3-cell variance/Loewner algebra, coarse original lambda0 lower.
Real odd/even Weil sign, true lambda1, native CC27 D-Riesz, RH OPEN.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import validate_rpb108_ps30_ground_state_gap as ps30

ROOT=Path(__file__).resolve().parents[1]


def expsum_lower(x,n):
    assert x>0 and n>=0
    term=F(1); res=F(1)
    for j in range(1,n+1):
        term=term*x/j
        res+=term
    return res,term


def expsum_upper(x,n):
    # Positive Taylor tail starts at order n+1, and its successive
    # term ratios <= x/(n+2) for all subsequent orders.
    s,t=expsum_lower(x,n)
    next_term=t*x/(n+1)
    r=x/(n+2)
    assert 0<r<1
    return s+next_term/(1-r)


def det(M):
    n=len(M)
    assert all(len(row)==n for row in M)
    if n==0:return F(1)
    if n==1:return M[0][0]
    return sum(
        (F(-1) if j%2 else F(1))*M[0][j]*
        det([row[:j]+row[j+1:] for row in M[1:]])
        for j in range(n)
    )


def psd(M):
    n=len(M)
    assert all(len(row)==n for row in M)
    assert all(M[i][j]==M[j][i] for i in range(n) for j in range(n))
    # Sylvester principal-minors characterization for semidefiniteness.
    return all(det([[M[i][j] for j in ids] for i in ids])>=0
               for k in range(1,n+1)
               for ids in combinations(range(n),k))


def graph_gate(mu,w,rho):
    n=len(mu)
    assert n>=2 and all(x>0 for x in mu)
    assert sum(mu,F(0))==1 and rho>0
    assert len(w)==n and all(len(row)==n for row in w)
    assert all(w[i][j]==w[j][i] and w[i][j]>=0
               for i in range(n) for j in range(n))
    ell=[sum((w[i][j]*mu[j] for j in range(n)),F(0))
         for i in range(n)]
    G=[[(sum((w[i][k]*mu[i]*mu[k]
              for k in range(n) if k!=i),F(0))
          if i==j else -w[i][j]*mu[i]*mu[j])
        for j in range(n)] for i in range(n)]
    D=[[(mu[i] if i==j else F(0))-mu[i]*mu[j]
        for j in range(n)] for i in range(n)]
    certificate=[[G[i][j]-rho*D[i][j] for j in range(n)]
                 for i in range(n)]
    return all(v>=rho for v in ell) and psd(certificate),ell,G,D


def variances_identity(mu,w,m,v):
    assert len(mu)==len(w)==len(m)==len(v)
    n=len(mu)
    assert sum(mu,F(0))==1 and all(x>=0 for x in v)
    # Exact integration of all within- and cross-cell contributions
    # of a piecewise lower bounded jump kernel, not a sampled
    # original phi_0 or numerical original seven-prime coupling.
    raw=F(0)
    for i in range(n):
        raw+=w[i][i]*mu[i]*mu[i]*v[i]
        for j in range(i+1,n):
            raw+=w[i][j]*mu[i]*mu[j]*(
                (m[i]-m[j])**2+v[i]+v[j])
    mean_part=sum((w[i][j]*mu[i]*mu[j]*(m[i]-m[j])**2
                   for i in range(n)
                   for j in range(i+1,n)),F(0))
    ell=[sum((w[i][j]*mu[j] for j in range(n)),F(0))
         for i in range(n)]
    within_part=sum((mu[i]*v[i]*ell[i] for i in range(n)),F(0))
    assert raw==mean_part+within_part
    mean=sum((mu[i]*m[i] for i in range(n)),F(0))
    var=sum((mu[i]*(v[i]+(m[i]-mean)**2) for i in range(n)),F(0))
    assert var>0
    return raw,var


def even_reflection_demo():
    # Four-point symmetric +/- x,+/- y kernel layer model.
    # The true original physical even reflection combinatorics is
    # checked without pretending rational toy edge weights are k(u).
    a,b=F(3,4),F(1,3)
    phi=[F(2),F(1),F(2),F(1)]
    gg=[F(3),F(-1),F(3),F(-1)]
    edges=[(0,1,a),(2,3,a),(0,3,b),(1,2,b)]
    all_jumps=sum((w*phi[i]*phi[j]*(gg[i]-gg[j])**2
                    for i,j,w in edges),F(0))
    reflected=2*(a+b)*phi[0]*phi[1]*(gg[0]-gg[1])**2
    assert all_jumps==reflected and reflected>0
    return reflected


def run():
    # Inherited original source arithmetic + PS30 exact source-Schur
    # transformation tested on an auxiliary finite rational model.
    # Prior validator's checkpoint terminal assertion PS30 is not
    # directly replayed because this branch appends PS31.
    ps30.ps29.ps28.run()
    r0=ps30.regression()
    assert all(v>0 for v in r0)

    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert lane["status"]=="open"
    assert lane["checkpoints"][-1]["id"]=="PS31"
    assert all(v is False for v in lane["closures"].values())

    # Exact original displacement 2log2, whose e^(-u/2)=1/2:
    # k(u)= (1/2)/(1-1/16) = 8/15, N exponential layers
    # exhaust by a geometric sum, with strictly positive tail.
    exact=F(8,15)
    for N in (1,2,4,8,16):
        finite=sum((F(1,2)*F(1,16)**j for j in range(N)),F(0))
        rem=exact*F(1,16)**N
        assert finite+rem==exact and rem>0 and finite>0

    # Certify e^(11/20)<7/4 and >5/3 with rational exponential
    # Taylor plus a TRUE geometric upper tail, not raw floats.
    small=F(11,20)
    assert expsum_lower(small,3)[0]>F(5,3)
    assert expsum_upper(small,5)<F(7,4)
    assert expsum_lower(F(11,5),6)[0]>F(8)
    # 4/7< k(B) < 24/35 from e^(B/2), e^(2B).
    k_lo=F(4,7)
    k_hi=F(24,35)
    assert F(0)<k_lo<k_hi
    only_uniform_ceiling=k_hi*F(11,5)
    assert only_uniform_ceiling==F(264,175)
    assert only_uniform_ceiling<F(151,100)
    assert only_uniform_ceiling<F(4359740,10**6)

    reflected=even_reflection_demo()

    # Graph residual lower preserving within-cell variances.
    mu=[F(1,3),F(2,3)]
    w=[[F(5),F(3)],[F(3),F(4)]]
    success,exit_rate,G,D=graph_gate(mu,w,F(3))
    assert success and exit_rate==[F(11,3),F(11,3)]
    assert G==[[F(2,3),-F(2,3)],[-F(2,3),F(2,3)]]
    # Q_graph = 3 D on two unequal masses, so threshold 3 is tight.
    assert all(G[i][j]==3*D[i][j] for i in range(2) for j in range(2))
    fail,_,_,_=graph_gate(mu,w,F(7,2))
    assert not fail

    mu3=[F(1,2),F(1,3),F(1,6)]
    w3=[[F(2),F(4),F(4)],
        [F(4),F(4),F(4)],
        [F(4),F(4),F(4)]]
    accepted,l3,G3,D3=graph_gate(mu3,w3,F(3))
    assert accepted and l3==[F(3),F(4),F(4)]
    assert all(G3[i][j]==4*D3[i][j]
               for i in range(3) for j in range(3))
    rejected,_,_,_=graph_gate(mu3,w3,F(4))
    assert not rejected  # cell 0 exit rate only 3
    test_energy,test_var=variances_identity(
        mu3,w3,[F(1),F(0),F(-2)],
        [F(1,4),F(1,9),F(1,16)])
    assert test_energy>=F(3)*test_var

    # Genuine PS17 V_C full physical bound, PS27 true original
    # source inverse/cross envelopes and removed true positive pole.
    # This is a bound on ORIGINAL pole-free even L, not a measured
    # lambda0 eigenvalue.
    v_abs=F(13)+F(539,90)
    source_abs=F(1403,80)**2/F(1997,9000)
    lam_abs_max=v_abs+source_abs
    assert F(4359740,10**6)<lam_abs_max<F(1406)
    # Original RC315/PS27 negative witness:
    # 4.359740<|lambda0|<1406; 4.359740 is NECESSARY
    # and not a sufficient threshold to close lambda1.
    assert F(264,175)<F(4359740,10**6)

    print("PS31 exact original digamma exponential layer rational check",
          exact,flush=True)
    print("PS31 rigorous original even reflection kernel k(B) in",
          (k_lo,k_hi),flush=True)
    print("PS31 even constant-floor proof ceiling",
          only_uniform_ceiling,flush=True)
    print("PS31 exact symmetric 4-point even arch jump",reflected,flush=True)
    print("PS31 graph 2-cell exact accepted rho 3; rejected rho 7/2",
          flush=True)
    print("PS31 graph 3-cell exact accepted rho 3; rejected rho 4",
          flush=True)
    print("PS31 3-cell original-style variance lower",test_energy,
          "total variance",test_var,flush=True)
    print("PS31 source/cross/operator bound |lambda0| STRICT UPPER",
          float(lam_abs_max)," <1406",flush=True)
    print("PS31 PASS SCOPED: exact positive digamma exponential layers,"
          " mirrored original even arch jump identity, rational"
          " uneven-cell finite Loewner/within-cell Poincare gate,"
          " true first-principles coarse original lambda0 envelope."
          " Actual phi0 and all physical cell masses/kernel w_ij"
          " NOT measured; no lambda1 sign or effective-pole Delta,"
          " W-EVEN-FORM, W-ODD-NEG, full signed Weil, CC27 D-Riesz"
          " or RH closure.",flush=True)

if __name__=="__main__":
    run()
