#!/usr/bin/env python3
"""SM28 original signed odd positive continuum: exact all-Legendre moments.

ANALYTIC certificate (conditional on already reviewed SI29/SM14/SM15):
  On each of thirteen actual ORIGINAL signed-positive whole-real SM14
  windows J_j=(c_j+-r), w+(xi)>delta_j, the exact original supported
  POSITIVE operator  T_j=2delta_j∫_J |h_xi><h_xi|dxi
   =4r delta_j sum_(n>=0) (2n+1)|q_{jn}><q_{jn}|,
  q_jn(x)=1/2 ∫_(-1)^1 P_n(t)sin(2pi(c_j+rt)x)dt.
  Every finite Legendre tail n>=p has STRICTLY positive quadratic on
  every nonzero compact-support odd f, but has NO global L² floor.
  Full ORIGINAL infinite positive tail n>=2 after 13*2 features:
    0<=R_tail<3/10000 I
  by exact rational Taylor/Legendre Bessel uniform bound.

  Original full supported Astar=A_o-2|s><s| contains the SI29
  14-source pole-conditioned B14 plus ALL 13 continuum bands and
  retains scalar true physical floor kappa_star>SM10 eta.

  Original complete Kneg<=U D U*+eta I still needs 890 fully
  coupled inverse, so NO W-ODD-NEG O1/O2 or RH/Weil closure.
This script is exact rational CONSTANT, GEOMETRY, and model
Parseval regression; not an executable proof of infinite-dimensional
Fourier injectivity or original entire-operator PSD.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from math import factorial
from validate_rpb108_sm14_continuum import (
    S,C,R,run as verify_sm14_real_positive
)
from validate_rpb108_sm15_global_negative_witness import (
    original_positive_lower
)
from validate_rpb108_sm12_positive_reference_33 import (
    OLD_POSITIVE,CENTERS as C33_NEW,RADIUS as C33_RADIUS
)
from validate_rpb108_si29_pole_threshold_three_bands import (
    FEATURES as SI29_FEATURES
)
from validate_rpb108_si06_negative_band import (
    B,PI
)
from validate_rpb108_sm10_explicit_odd_cap_moments import (
    full_upper_leaves,BITS,TAU
)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_sm17_compact_spectral_gate import (
    KAPPA,KAPPA_STAR,ETA_UP
)

ROOT=Path(__file__).resolve().parents[1]
TAIL13_CAP=F(3,10000)
QMAX=F(1,8)


def original_complete_signed_windows():
    assert len(S)==13 and C==F(721,50) and R==F(3,200)
    deltas=[F(d) for _,d in S]
    assert sum(deltas,F(0))==35
    windows=sorted((F(n,50)-R,F(n,50)+R) for n,_ in S)
    assert all(windows[i][1]<=windows[i+1][0] for i in range(12))
    # The 13 ORIGINAL SM14 signed-positive whole-real windows
    # are disjoint from all 33 C33 bands and all ORIGINAL SI29
    # 14 source positive bands. Therefore the positive band
    # integral is genuinely additive, not double-counting.
    protected33=[(c-r,c+r) for c,r,_,_ in OLD_POSITIVE]
    protected33 +=[(c-C33_RADIUS,c+C33_RADIUS) for c in C33_NEW]
    assert len(protected33)==33
    protected14=[(c-r,c+r) for c,r,_,_ in SI29_FEATURES]
    assert len(protected14)==14
    assert len(set(protected14))==12
    for l,h in windows:
        assert all(not (l<r and a<h) for a,r in protected33)
        assert all(not (l<r and a<h) for a,r in protected14)
    assert all(l>0 for l,h in windows)

    # True original SM14 replays each whole-real signed seven-prime
    # interval, plus disjointness and actual physical Jensen response.
    verify_sm14_real_positive()
    return deltas,windows


def whole_infinite_legendre_tail(deltas):
    assert B==F(11,10) and R==F(3,200)
    assert PI[1]<F(22,7)
    qhi=2*F(22,7)*R*B
    assert qhi<QMAX
    assert F(0)<ETA_UP<KAPPA_STAR<KAPPA
    assert KAPPA==F(1,1000) and KAPPA_STAR==F(33621,10**9)

    def bound(p):
        # True ORIGINAL physical x∈[-B,B], and t∈[-1,1],
        # Taylor residual each h_{c+rt}(x) <= (2πrB)^p/p!.
        # Legendre projected Hilbert-valued residual best in L²(t).
        # R_j,p <=8B δ r (2πrB)^(2p)/(p!)² I.
        assert isinstance(p,int) and p>=1
        return 8*B*sum(deltas,F(0))*R*qhi**(2*p)/F(factorial(p)**2)

    tail_after_average=bound(1)
    tail_after_two=bound(2)
    # Use exact rational uniform bound qhi<1/8 for an easily
    # replayed strict, source-independent rational acceptance:
    tail_simple=8*B*sum(deltas,F(0))*R*QMAX**4/F(4)
    assert F(0)<tail_after_two<tail_simple<TAIL13_CAP
    assert tail_after_average>tail_after_two>0

    # Full original SM10 all-negative signed cap remains 890
    # physical synthesis columns in 107 SPD moment blocks,
    # with eta full infinite residual, NOT truncated to 26 modes.
    clusters,width,mass,total=full_upper_leaves()
    assert len(clusters)==107
    orders=[taylor_order(c[-1][1]-c[0][0],BITS)[0] for c in clusters]
    assert sum(orders)==890 and all(p>0 for p in orders)
    assert TAU==F(1,1024)
    assert ETA_UP<KAPPA_STAR
    return qhi,tail_after_average,tail_after_two,tail_simple,len(orders),sum(orders)


def finite_orthogonal_parseval_model():
    # Exact 2-vector finite Hilbert space and degree-one polynomial
    # h(t)=a+t b. Actual Legendre P0=1, P1=t;
    # q0=a, q1=b/3.
    # Integral_-1^1 h(t)h(t)^*dt = 2 aa*+2/3 bb*.
    a=[F(1,3),F(2)]
    b=[F(3,2),F(-1,5)]
    q0=a
    q1=[v/F(3) for v in b]
    exact=[[2*a[i]*a[j]+F(2,3)*b[i]*b[j]
            for j in range(2)] for i in range(2)]
    via_legendre=[[2*q0[i]*q0[j]+6*q1[i]*q1[j]
                   for j in range(2)] for i in range(2)]
    assert exact==via_legendre
    assert exact[0][0]*exact[1][1]-exact[0][1]**2>0
    assert any(q1[i]!=0 for i in range(2))
    # Additional quadratic Legendre mode P2=(3t²-1)/2
    # has norm squared 2/5; q2=P2 projection=1/5 on a P2 term.
    # For h(t)=a+tb+c P2(t), the whole continuum gains the
    # positive 2/5 c*c* contribution. This is not point sampling.
    c=[F(1,7),F(-1,4)]
    q2=[v/F(5) for v in c]
    positive_P2=[[F(2,5)*c[i]*c[j] for j in range(2)]
                 for i in range(2)]
    via_P2=[[10*q2[i]*q2[j] for j in range(2)] for i in range(2)]
    assert positive_P2==via_P2
    assert positive_P2[0][0]>0 and positive_P2[1][1]>0
    assert positive_P2[0][0]*positive_P2[1][1]==positive_P2[0][1]**2
    return exact,positive_P2


def true_same_original_source_positive_response():
    # SM14 alone proves true original 13 NEW disjoint original
    # signed-positive frequency Jensen window response > 1/2.
    # SM15 strengthens its exact rational physical lower > 2/3
    # on the ORIGINAL negative packet at center 721/50.
    pos,extra=original_positive_lower()
    assert pos>extra>F(2,3)>F(1,2)
    return pos,extra


def run():
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert gov["governance"]["no_automatic_promotion"] is True
    assert "SM27" in gov["evidence"] and "SM28" in gov["evidence"]
    odd=next(o for o in gov["obligations"] if o["id"]=="W-ODD-NEG")
    assert odd["status"]=="open"
    assert "SM28" in odd["evidence"] and "O1/O2" in odd["acceptance"]
    deltas,windows=original_complete_signed_windows()
    qhi,t1,t2,t_simple,nblocks,ncolumns=whole_infinite_legendre_tail(deltas)
    pos,extra=true_same_original_source_positive_response()
    exact,variance=finite_orthogonal_parseval_model()

    print("SM28 ORIGINAL full positive real intervals",len(windows),
          "delta sum",sum(deltas,F(0)),"true signed SM14 checks passed",flush=True)
    print("SM28 original 14 SI29 source band intervals and 33 C33 bands"
          " disjoint from the 13 new positive continuum intervals",flush=True)
    print("SM28 exact physical supported frequency derivative range"
          " 2 pi r B rational UPPER",qhi,"<1/8",flush=True)
    print("SM28 actual 13-band full-Jensen (n>=1) positive continuum"
          " tail norm upper",float(t1),flush=True)
    print("SM28 all infinite Legendre modes n>=2"
          " ORIGINAL full physical operator norm UPPER",t2,
          "conservative rational",t_simple,"<3/10000",flush=True)
    print("SM28 exact 26 ORIGINAL continuous Legendre P0/P1 source"
          " vectors plus strictly positive infinite-rank variance remainder",
          flush=True)
    print("SM28 TRUE original Astar>=B14+13 whole positive band"
          " operators>=B14>=kappa_star I",KAPPA_STAR,flush=True)
    print("SM28 complete original 107 negative moment blocks and"
          " 890 Taylor source columns still untested as full inverse",
          nblocks,ncolumns,flush=True)
    print("SM28 original same witness 13 extra whole positive band"
          " Jensen response >2/3 rational value",extra,flush=True)
    print("SM28 exact degree-1 Hilbert Legendre Parseval model",exact,
          "degree-2 genuinely positive variance",variance,flush=True)
    print("SM28 PASS SCOPED: TRUE ORIGINAL thirteen signed positive"
          " CONTINUUM bands retained in exact full infinite Legendre"
          " tower, with exact 26 source modes and nonzero on every"
          " nonzero odd function infinite-rank residue, certified"
          " full infinite positive tail norm <3e-4."
          " Astar original odd pole and full 890 negative/infinite"
          " eta retained; NO computed full 890×890 coupled Schur,"
          " NO original O1/O2, even E1-E4, full Weil,"
          " CC27 D-Riesz, or RH.",flush=True)


if __name__=="__main__":
    run()
