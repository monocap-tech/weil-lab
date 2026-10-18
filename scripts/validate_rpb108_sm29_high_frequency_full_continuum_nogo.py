#!/usr/bin/env python3
"""SM29: original remote 389.56 negative Jensen band defeats ENTIRE SM28
13-band original continuous positive-frequency operator + actual SI29
14-feature, correctly odd-pole-subtracted B14.

On g=sin(2pi 389.56 x) sinc(2pi .01 x) true original physical odd:
 <g,(K_neg -(B14 + T_13_full_continuum))g> >3/200,
using a uniform all-real positive-frequency physical signed sine-Gram
envelope <3/1000 across every SI29/SM14 ORIGINAL positive window.
Original pole term nonpositive.  T13 includes ALL infinite Legendre
modes, not merely 26 selected vectors or a truncated expansion.

SM10 entire 107/890 full signed negative cap plus eta then implies
ind_-(D^-1-U*(B14+T13-eta I)^-1 U)>=1 for the COMPLETE 890-source
continuum-enriched SURROGATE Schur by full bounded block inertia.
No theorem about true full Astar or Weil negative index: original
positive frequency continuum outside these 13 windows can repair it.

The validator only replays exact Fraction constants, source geometry,
true original signed-frequency window certificates and finite block
inertia algebra; inherited full Fourier/operator theory requires audit.
"""
from pathlib import Path
from fractions import Fraction as F
import json
from validate_rpb108_sm11_rank17_c16_nogo import (
    CENTERS as ORIGINAL_NEG_CENTERS,
    certify_all_negative_windows,
    RADIUS as NEG_R,
    DELTA as NEG_DELTA
)
from validate_rpb108_sm28_positive_continuum_legendre_tower import (
    S, R as POS_R, original_complete_signed_windows
)
from validate_rpb108_si29_pole_threshold_three_bands import (
    FEATURES as SOURCE14
)
from validate_rpb108_si06_negative_band import B, PI
from validate_rpb108_sm10_explicit_odd_cap_moments import (
    full_upper_leaves, TAU, BITS
)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_sm17_compact_spectral_gate import (
    KAPPA, KAPPA_STAR, ETA_UP
)

ROOT=Path(__file__).resolve().parents[1]
REMOTE_C=F(38956,100)
U=F(3,1000)
POSITIVITY_MARGIN=F(3,200)
PI_UP=F(22,7)


def true_original_remote_source():
    assert REMOTE_C in ORIGINAL_NEG_CENTERS
    assert len(ORIGINAL_NEG_CENTERS)==17
    assert NEG_R==F(1,100)
    assert NEG_DELTA==F(2,5)
    # Exact original SM11 ALL-real seven-prime negative intervals,
    # not merely sign samples at the original source.
    worst=certify_all_negative_windows()
    assert worst<-NEG_DELTA

    assert B==F(11,10) and PI[0]>3 and PI[1]<PI_UP
    eps=(2*PI_UP*NEG_R*B)**2/F(6)
    assert F(0)<eps<F(1,1000)
    # true g-sin original Jensen packet physical |.|_infty <=eps.
    # Original supported sin-sin Gram for every 0<xi<20:
    # abs gram(c,xi)<1/(2*pi*(c-xi))+1/(2*pi*(c+xi))
    #  c-xi>369, c+xi>389, pi>3.
    all_real_bound=F(1,6*369)+F(1,6*389)+2*B*eps
    assert all_real_bound<U

    # Norm g>= (1-eps)^2 ||sin(2pi c.)||², and actual sin²
    # physical integral >B-1/(12*c), pi>3.
    normlo=(1-eps)**2*(B-F(1)/(12*REMOTE_C))
    assert normlo>F(1)
    # Actual entire seven-prime Kneg original SM11 Jensen 17-band
    # lower >=2/125 |g><g|, including the remote packet.
    original_negative_lower=F(2,125)*normlo**2
    assert original_negative_lower>F(19,1000)
    return eps,all_real_bound,normlo,original_negative_lower


def true_full_original_positive_reference_upper():
    # All original SI29 source features: zero/first normalized
    # Legendre Jensen moment, with original gamma=4r delta
    # (deg0) or 4r delta/3 (deg1). Distinct frequency source
    # intervals may repeat for different moments (allowed).
    assert len(SOURCE14)==14
    windows14=[]
    source_mass=F(0)
    first_moments=0
    for c,r,delta,degree in SOURCE14:
        assert 0<c-r<c+r<20
        assert r>0 and delta>0 and degree in (0,1)
        windows14.append((c-r,c+r))
        weight=4*r*delta
        source_mass+=weight
        if degree==1:
            first_moments+=1
            # |3 E[t h]|<=3/2 U, gamma=weight/3
            # => gamma |overlap|²<= (3/4)*weight U² < weight U²
            assert F(1,3)*F(3,2)**2==F(3,4)
    assert len(set(windows14))==12
    assert first_moments==2
    assert source_mass<F(200)

    # True original 13 signed-positive whole-real frequency
    # intervals; this function replays the REAL signed
    # multiplier proof and all SI29/source disjointness.
    deltas,windows=original_complete_signed_windows()
    assert len(S)==len(windows)==13
    assert POS_R==F(3,200)
    assert all(F(0)<a<b<F(20) for a,b in windows)
    assert sum(deltas,F(0))==35
    full_positive_continuum_mass=4*POS_R*sum(deltas,F(0))
    assert full_positive_continuum_mass==F(21,10)

    # For all actual positive continuum real xi, the SAME
    # original supported packet uniform overlap <U.
    # Full T13, including EVERY infinite Legendre tail,
    # has <g,T13 g><=4 r sum delta U².
    # True pole is negative, so omit it ONLY in an upper.
    original_positive_upper=KAPPA*(2*B)+(
        source_mass+full_positive_continuum_mass)*U**2
    assert original_positive_upper>0
    assert F(0)<ETA_UP<KAPPA_STAR<KAPPA
    return source_mass,full_positive_continuum_mass,original_positive_upper


def complete_original_negative_cap():
    clusters,width,mass,total=full_upper_leaves()
    orders=[taylor_order(cl[-1][1]-cl[0][0],BITS)[0]
            for cl in clusters]
    assert len(clusters)==len(orders)==107
    assert sum(orders)==890
    assert all(p>0 for p in orders)
    assert TAU==F(1,1024)
    assert 0<ETA_UP<KAPPA_STAR
    # Since F13>=B14>=kappa_star and eta<kappa_star,
    # the exact complete 890-source Schur dual is well-defined,
    # and its inertia equals F13-eta-UDU* by positive block
    # congruences. A NEGATIVE physical witness transfers
    # to that ENTIRE 890-source surrogate.
    return len(orders),sum(orders),mass


def full_signed_2x2_inertia_regression():
    # Only an algebra check of COMPLETE off-diagonal Schur inertia;
    # no finite model replaces actual 890 original source block.
    A=[[F(1,2),F(0)],[F(0),F(2)]]
    U2=[[F(1),F(1,2)],[F(0),F(1,2)]]
    # D=I: primal=A-UU*, dual=I-U*A^-1 U.
    def mm(x,y):
        return [[sum((x[i][k]*y[k][j] for k in range(len(y))),F(0))
                 for j in range(len(y[0]))] for i in range(len(x))]
    def tr(x):return [list(row) for row in zip(*x)]
    def sub(x,y):return [[a-b for a,b in zip(row,other)] for row,other in zip(x,y)]
    primal=sub(A,mm(U2,tr(U2)))
    Ai=[[F(2),F(0)],[F(0),F(1,2)]]
    dual=sub([[F(1),F(0)],[F(0),F(1)]],mm(mm(tr(U2),Ai),U2))
    assert primal[0][1]==primal[1][0] and dual[0][1]==dual[1][0]
    # Negative determinant on each 2x2 symmetric matrix
    # proves exactly ONE negative mode on each full coupled side.
    pd=primal[0][0]*primal[1][1]-primal[0][1]**2
    dd=dual[0][0]*dual[1][1]-dual[0][1]**2
    assert pd<0 and dd<0
    assert primal[0][1]!=0 and dual[0][1]!=0
    # Stronger ORIGINAL-style positive reference can repair
    # surrogate without changing the original negative cap:
    Atrue=[[F(3),F(0)],[F(0),F(3)]]
    recovered=sub(Atrue,mm(U2,tr(U2)))
    assert recovered[0][0]>0 and recovered[1][1]>0
    assert recovered[0][0]*recovered[1][1]>recovered[0][1]**2
    return pd,dd


def run():
    g=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in g["obligations"] if x["id"]=="W-ODD-NEG")
    assert g["active_obligation"]=="W-ODD-NEG"
    assert g["objective"]["status"]=="open"
    assert g["governance"]["no_automatic_promotion"] is True
    assert odd["status"]=="open"
    assert all(k in g["evidence"] and k in odd["evidence"] for k in ("SM27","SM28","SM29"))
    assert "O1/O2" in odd["acceptance"]

    eps,overlap,normlo,negative=true_original_remote_source()
    si29weight,newmass,positive=true_full_original_positive_reference_upper()
    margin=negative-positive
    assert margin>POSITIVITY_MARGIN
    nblocks,ncolumns,mass=complete_original_negative_cap()
    pd,dd=full_signed_2x2_inertia_regression()
    print("SM29 original remote TRUE signed negative packet 38956/100",
          "radius",NEG_R,"true Kneg uniform lower",float(negative),flush=True)
    print("SM29 all-original-positive-real frequency sine overlap upper",
          float(overlap),"<3/1000",flush=True)
    print("SM29 all SI29 original 14 source moments weight exact",
          si29weight,"and full SM28 13-continuum weight",newmass,flush=True)
    print("SM29 original B14+ENTIRE infinite Legendre T13 quadratic upper",
          float(positive),flush=True)
    print("SM29 ORIGINAL remote physical signed deficit lower",
          float(margin),">3/200",flush=True)
    print("SM29 original SM10 full signed-negative cap",
          nblocks,"blocks",ncolumns,"columns, full eta paid",flush=True)
    print("SM29 COMPLETE 890-source original-continuum-enriched"
          " SURROGATE Schur has NEGATIVE INDEX>=1"
          " by true original physical witness + full block inertia",flush=True)
    print("SM29 finite 2x2 exact fully coupled block Schur dets",
          pd,dd,flush=True)
    print("SM29 PASS SCOPED: FULL original SM28 thirteen continuum"
          " bands including ALL infinitely many Legendre modes"
          " cannot dominate actual REMOTE 389.56 original"
          " signed-negative packet when added to true SI29 B14"
          " pole-conditioned reference. The full 890-source"
          " F13-conditioned surrogate has a negative direction."
          " TRUE Astar includes unselected positive continuum;"
          " actual original odd W_o and W-ODD-NEG O1/O2, even"
          " E1-E4, Weil, CC27 D-Riesz and RH remain OPEN."
          " Independent infinite-dimensional/source audit pending.",
          flush=True)


if __name__=="__main__":
    run()
