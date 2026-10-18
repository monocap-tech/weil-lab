#!/usr/bin/env python3
"""SM34: ORIGINAL odd Astar-positive-energy dual exceptional Schur.

Given original pole-conditioned TRUE whole positive Astar>=kappa*>0,
original full negative K>=0, and ORIGINAL SI10 b9 E0<=470 odd
physical source span, define a NEW nonorthogonal finite exception
 E_A=Astar^-1(E0), F=E0^perp.
Then H=E_A dotplus F (finite T=P_E0 Astar^-1 P_E0 SPD), and
  a_star(Astar^-1 h,f)=<h,f>=0  for all f in F.
Consequently the entire original full signed mixed W=Astar-K cross
from E_A to F equals -<K e,f>; NO unbounded positive arch/Cplus
cross is left, and true odd pole is already IN Astar exactly.

Original SM32 D_F=W|F>=mu I (mu=17/25000). Original SM33
Q0 K Q0<=epsilon I on all F, epsilon = all 973 signed-negative
frequency leaves, 107 source-specific Taylor errors, <1/15000.
Full relative negative cross gives
 ||Q0 K e||² <=epsilon <e,K e>,
 0<=<Q0 K e,D_F^-1 Q0 K e> <=(epsilon/mu)<e,K e>.
EXACT complete-operator finite Schur:
 S_A(e)=a_star(e,e)-<e,K e>-<QK e,D_F^-1 QK e>.
Entire W>=0 iff S_A>=0 (conditional on inherited closed-domain
analytic SI29/SI10/SM32/SM33 premises), and negative index equal.
Sufficient complete original ODD full-operator gate on all 470 dual
source coefficients h is
  N(h)=<Astar^-1 h, K Astar^-1 h> <=51/56 * G(h),
  G(h)=<h,Astar^-1 h>.
Since eps/mu<5/51, 1+eps/mu<56/51. Gate is NOT evaluated.

The code replays ALL original source/negative residual arithmetic,
checks exact new 51/56 rational threshold, and tests finite exact
Astar energy-dual form, full mixed correction, true determinant
congruence and adversarial countermodels. No full odd or RH promotion.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from validate_rpb108_sm33_original_odd_negative_mixed_bound import (
    full_original_clusterwise_negative_mixed
)
from validate_rpb108_sm32_parity_cofinite_odd_schur import MU
from validate_rpb108_sm17_compact_spectral_gate import KAPPA_STAR

ROOT=Path(__file__).resolve().parents[1]
CLEAN_THRESHOLD=F(51,56)
EPSILON_CEILING=F(1,15000)
RELATIVE_CEILING=F(5,51)


def full_original_dual_threshold_replay():
    # The TRUE original SI10 signed seven-prime, 973 unresolved
    # leaves, 107 clusters, b9 all-source odd parity exception,
    # complete true Q0KQ0<=eps I and D_F>=mu I.
    x=full_original_clusterwise_negative_mixed()
    assert x["leaves"]==973 and x["clusters"]==107
    assert x["source_count"]==470
    eps=x["leak"]
    mu=MU
    assert mu==F(17,25000)
    assert eps>0 and eps<EPSILON_CEILING
    assert KAPPA_STAR==F(33621,10**9)>0
    ratio=eps/mu
    assert ratio<RELATIVE_CEILING
    assert EPSILON_CEILING/mu==RELATIVE_CEILING
    assert F(1)+RELATIVE_CEILING==F(56,51)
    assert CLEAN_THRESHOLD*(F(56,51))==F(1)
    actual_threshold=mu/(mu+eps)
    assert actual_threshold>CLEAN_THRESHOLD
    # The clean rational 51/56 source generalized-eigenvalue
    # gate on ORIGINAL full 470 dual space remains unmeasured.
    return eps,mu,ratio,actual_threshold,x


def form2(A,x,y):
    return sum((x[i]*sum((A[i][j]*y[j] for j in range(2)),F(0))
                for i in range(2)),F(0))


def finite_energy_dual_exact_test(k11,k22):
    # TRUE operator algebra model only, never an asserted original
    # 470-source Gram. A is strict positive with NONZERO
    # source-vs-physical-orthogonal positive offdiagonal.
    A=[[F(2),F(1)],[F(1),F(2)]]
    Ai=[[F(2,3),F(-1,3)],[F(-1,3),F(2,3)]]
    K=[[k11,F(0)],[F(0),k22]]
    assert k11>0 and k22>0
    assert A[0][1]==1
    e=[Ai[0][0],Ai[1][0]] # A^-1 e1 in exact rational
    f=[F(0),F(1)]         # the ENTIRE F=E0^perp, exactly
    old_basis=[F(1),F(0)]
    assert form2(A,old_basis,f)==1 # old positive mixed Cplus!=0
    assert form2(A,e,f)==0         # NEW full a_star mixed ==0
    assert form2(A,e,e)==F(2,3)
    assert e[0]*f[1]-e[1]*f[0]==F(2,3)!=0
    assert form2(K,e,f)==e[1]*k22

    W=[[A[i][j]-K[i][j] for j in range(2)] for i in range(2)]
    g=form2(A,e,e)
    neg=form2(K,e,e)
    fin=form2(W,e,e)
    d=form2(W,f,f)
    c=form2(W,e,f)
    assert d==F(2)-k22
    assert c==-form2(K,e,f)
    assert d>0 # positive complete true F as used in original SI10
    s=fin-c*c/d
    # TRUE full block determinant in old coordinate and nonorth
    # source-dual physical adapted basis must match EXACTLY.
    det_orig=W[0][0]*W[1][1]-W[0][1]*W[1][0]
    det_adapt=fin*d-c*c
    assert det_adapt==F(4,9)*det_orig
    assert s*d==det_adapt

    # True PSD K Cauchy estimate on entire F, and complete
    # positive D inverse RESPONSE on the nonorth splitting.
    eps=k22
    mu=d
    assert c*c<=eps*neg
    correction=c*c/d
    assert correction<=eps*neg/mu
    lower=g-(F(1)+eps/mu)*neg
    assert s>=lower

    # The genuine exact source generalized pair in basis h=e1:
    # G=<h,A^-1h>, N=<A^-1h,K A^-1h>.
    assert g==F(2,3)
    true_ratio=neg/g
    return dict(g=g,neg=neg,source_ratio=true_ratio,eps=eps,
                mu=mu,full_exact_schur=s,full_det=det_orig,
                adapted_det=det_adapt,full_mixed=c,correction=correction,
                lower=lower)


def exact_nonorthogonal_schur_regressions():
    # Benign PSD true coupled test with matching relative
    # eps/mu<5/51; if its finite GENERALIZED source response
    # is below 51/56 then the entire coupled operator must PSD.
    good=finite_energy_dual_exact_test(F(1),F(1,16))
    assert good["eps"]/good["mu"]==F(1,31)<RELATIVE_CEILING
    assert good["source_ratio"]==F(65,96)<CLEAN_THRESHOLD
    assert good["full_exact_schur"]>0 and good["full_det"]>0
    assert good["lower"]>0

    # ADVERSE genuine PSD negative K, true positive A and true
    # positive D_F, finite dual diagonal even positive, but full
    # corrected Schur NEGATIVE owing original K mixed term.
    # This shows why a nonorthogonal dual split is exact Schur,
    # NOT automatic positivity from finite diagonal or SI10.
    bad=finite_energy_dual_exact_test(F(1,10),F(19,10))
    assert bad["g"]>bad["neg"] and bad["mu"]>0
    assert bad["full_exact_schur"]<0 and bad["full_det"]<0
    assert bad["full_mixed"]!=0
    assert bad["source_ratio"]<1
    assert bad["eps"]/bad["mu"]>RELATIVE_CEILING
    assert bad["lower"]<0
    return good,bad


def run():
    m=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(o for o in m["obligations"] if o["id"]=="W-ODD-NEG")
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]=="open"
    assert m["governance"]["no_automatic_promotion"] is True
    assert odd["status"]=="open" and "O1/O2" in odd["acceptance"]
    assert all(k in odd["evidence"] and k in m["evidence"]
               for k in ("SM32","SM33","SM34"))
    assert "positive_energy_dual_odd_gate" in m["governance"]
    eps,mu,relative,threshold,src=full_original_dual_threshold_replay()
    good,bad=exact_nonorthogonal_schur_regressions()
    print("SM34 original complete signed seven-prime negative"
          " 973 leaves",src["leaves"],"107 clusters",src["clusters"],
          "physical odd source bound",src["source_count"],flush=True)
    print("SM34 true original full negative odd L2 complement"
          " spectral leakage epsilon",float(eps),"<1/15000",flush=True)
    print("SM34 true original entire signed odd F=E0-perp"
          " form floor mu",mu,"and exact epsilon/mu",
          float(relative),"<5/51",flush=True)
    print("SM34 exact original positive pole conditioned Astar"
          " lower",KAPPA_STAR,"and full energy-dual E_A=Astar^-1 E0"
          " eliminates ALL positive continuum/arch and odd-pole"
          " cross inside Astar (not pole separately)",flush=True)
    print("SM34 original COMPLETE infinite response relative"
          " bound correction <=(epsilon/mu)*<e,Kneg e>;"
          " exact source generalized threshold",float(threshold),
          "> CLEAN 51/56",float(CLEAN_THRESHOLD),flush=True)
    print("SM34 original full odd sufficient 470D generalized"
          " Loewner gate N=<Astar^-1h,Kneg Astar^-1h>"
          " <=51/56 G=<h,Astar^-1h> remains UNMEASURED,"
          " O1/O2 OPEN.",flush=True)
    print("SM34 finite EXACT energy-dual coupled PSD model"
          " original spectral det",float(good["full_det"]),
          "signed Schur",float(good["full_exact_schur"]),
          "source N/G",float(good["source_ratio"]),flush=True)
    print("SM34 finite EXACT adversarial positive diagonal D"
          " & positive finite dual but full signed INDEFINITE det",
          float(bad["full_det"]),"corrected Schur",
          float(bad["full_exact_schur"]),flush=True)
    print("SM34 PASS SCOPED: true ORIGINAL positive Astar energy"
          " dual projection cancels the entire otherwise unbounded"
          " positive Fourier/arch mixed Cplus exactly, while"
          " odd pole remains paid IN Astar; ALL signed negative"
          " 973 leaves contribute only a full-infinite"
          " relative Schur correction <=epsilon/mu."
          " Correct full ORIGINAL exceptional spectral sign"
          " equivalent to finite corrected energy-dual S_A;"
          " rational 51/56 sufficient 470D original generalized"
          " eigenvalue gate is NOT checked. Full O1/O2, E1-E4,"
          " signed whole Weil, CC27 D-Riesz, RH OPEN;"
          " inherited original operator/domain identification"
          " independent audit required.",flush=True)


if __name__=="__main__":
    run()
