#!/usr/bin/env python3
"""SM30 TRUE ORIGINAL positive-frequency COVERAGE near remote 389.56.

Two disjoint original whole-real, seven-prime m>kappa+2 bands
 [389.35,389.41] and [389.72,389.78] give a strictly >3/10
 positive *physical* quadratic on the ORIGINAL negative SM11
 Jensen packet g_389.56, with every signed original sine overlap
 enclosed, not falsely orthogonalized or sampled.
SM29's thirteen full continuous bands near14 contribute only
small remote amplitude, so two remote bands genuinely change
frequency coverage; their entire continuum Tleft+Tright is
operator PSD with a Jensen lower and all positive within-band
variance preserved.

Separately replay SM15's FULL original signed-negative cap
integral on the remote physical source, including ALL 973 leaves,
entire 107-block SM10 map, all remote amplitudes and odd pole.
Only if the actual exact rational positive-vs-FULL-negative margin
is positive is that ONE original test vector certified positive.
Even then O1/O2 and RH remain OPEN.

Scoped accepting arithmetic does not independently prove original
infinite-dimensional signed-Fourier/Weil operator identification.
"""
from pathlib import Path
from fractions import Fraction as F
import json
from validate_rpb108_si06_negative_band import PI,B,prime_interval
from validate_rpb108_si13_odd_fourier_reference import arch_lower
from validate_rpb108_si18_odd_rank_two_woodbury import gram
from validate_rpb108_sm11_rank17_c16_nogo import (
    CENTERS as NEG_CENTERS,
    RADIUS as NEG_RADIUS,
    DELTA as NEG_DELTA,
    certify_all_negative_windows,
)
from validate_rpb108_sm12_positive_reference_33 import (
    CENTERS as POS_OLD_CENTERS,
    RADIUS as POS_OLD_R,
    check_new_positive_windows,
)
from validate_rpb108_sm28_positive_continuum_legendre_tower import (
    S as SM28_BANDS,R as SM28_RADIUS
)
from validate_rpb108_sm17_compact_spectral_gate import (
    KAPPA,KAPPA_STAR,ETA_UP
)
from validate_rpb108_sm10_explicit_odd_cap_moments import (
    full_upper_leaves,BITS,TAU
)
from validate_rpb108_si08_multiband_rank import taylor_order
import validate_rpb108_sm15_global_negative_witness as sm15

ROOT=Path(__file__).resolve().parents[1]
REMOTE_C=F(38956,100)
R=F(3,100)
DELTA=F(2)
N=16
# Candidate original positive real-frequency windows. Full signed
# seven-prime sign must be checked on every subcell below.
BANDS=((F(38938,100),R,DELTA),(F(38975,100),R,DELTA))
POSITIVE_MIN=F(3,10)


def certify_original_remote_positive_bands():
    assert REMOTE_C in NEG_CENTERS and NEG_RADIUS==F(1,100)
    assert len(BANDS)==2 and B==F(11,10)
    assert PI[0]>3 and PI[1]<F(22,7)
    assert F(0)<ETA_UP<KAPPA_STAR<KAPPA
    assert certify_all_negative_windows()<-NEG_DELTA
    # All historical SM12 positive windows certified independently.
    assert check_new_positive_windows()>KAPPA+F(2)
    old=[(c-POS_OLD_R,c+POS_OLD_R) for c in POS_OLD_CENTERS]
    historical=[(F(n,50)-SM28_RADIUS,F(n,50)+SM28_RADIUS)
                for n,d in SM28_BANDS]
    existing=old+historical
    assert len(existing)==30
    intervals=[(c-r,c+r) for c,r,delta in BANDS]
    assert intervals[0][1]<intervals[1][0]
    assert all(not(a<rr and ll<b)
               for a,b in intervals for ll,rr in existing)
    assert all(not(a<REMOTE_C+NEG_RADIUS and REMOTE_C-NEG_RADIUS<b)
               for a,b in intervals)
    minima=[]
    for c,r,delta in BANDS:
        whole_min=None
        for j in range(N):
            l=c-r+2*r*j/N
            h=c-r+2*r*(j+1)/N
            mid=(l+h)/2
            certified=arch_lower(l)+prime_interval(mid)[0]-F(69,2)*(h-l)
            assert certified>KAPPA+delta,(
                "SM30 uncetified ORIGINAL signed real band",str(c),j,float(certified))
            whole_min=certified if whole_min is None else min(whole_min,certified)
        minima.append(whole_min)
    return intervals,minima


def actual_original_remote_positive_rayleigh():
    # Actual Jensen SM11 negative physical source is g_c(x)=
    # sin(2pi*c*x)*sinc(2pi*NEG_RADIUS*x), not center sine alone.
    # On EACH whole original positive real band J_j, the exact
    # Jensen mean p_j(x)=sin(2pi*d_j*x)*sinc(2pi*R*x)
    # obeys Ao >= 4*R*DELTA * |p_j><p_j|.
    eps_n=(2*PI[1]*NEG_RADIUS*B)**2/6
    eps_p=(2*PI[1]*R*B)**2/6
    assert 0<eps_n<F(1,100) and 0<eps_p<F(1,100)
    records=[];positive=F(0)
    for center,r,delta in BANDS:
        iv=gram(REMOTE_C,center)
        assert iv[0]<=iv[1]
        # These near-remote ORIGINAL signed overlaps are strictly
        # positive in the actual odd physical interval.
        signed_lo=max(F(0),iv[0],-iv[1])
        assert signed_lo>0
        overlap_lo=max(F(0),signed_lo-2*B*(eps_n+eps_p))
        assert overlap_lo>F(3,4)
        contrib=4*r*delta*overlap_lo**2
        positive+=contrib
        records.append((center,overlap_lo,contrib))
    # Pairwise real-frequency disjointness means original signed
    # Fourier positive band masses add without double-counting.
    assert positive>POSITIVE_MIN
    return positive,records,eps_n,eps_p


def whole_original_remote_negative_replay():
    # This is the EXACT existing SM15 original complete 973-leaf
    # signed negative integral and full original odd-pole upper,
    # applied to a DIFFERENT true remote physical Jensen packet.
    # C is a module-level source frequency in the original SM15
    # implementation; restore it after synchronous evaluation.
    previous=sm15.C
    assert previous==F(721,50)
    assert sm15.RN==NEG_RADIUS
    try:
        sm15.C=REMOTE_C
        entire,old,near,far,removed,top,clusters,local,remote,average,avg_gain=(
            sm15.signed_negative_global_upper())
        pole,pole_iv=sm15.pole_upper()
    finally:
        sm15.C=previous
    assert len(clusters)==107
    assert entire>=0 and near+far==entire and pole>=0
    assert entire<=old
    assert local+remote==973
    # No omitted original remote frequencies: entire includes all
    # true 973 original negative signed leaves + exterior zero.
    return entire,pole,near,far,removed,local,remote


def full_original_cap_standing():
    clusters,width,mass,total=full_upper_leaves()
    orders=[taylor_order(cl[-1][1]-cl[0][0],BITS)[0]
            for cl in clusters]
    assert len(clusters)==len(orders)==107
    assert sum(orders)==890
    assert TAU==F(1,1024) and ETA_UP<KAPPA_STAR
    return len(orders),sum(orders)


def run():
    manifest=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in manifest["obligations"] if x["id"]=="W-ODD-NEG")
    assert manifest["active_obligation"]=="W-ODD-NEG"
    assert manifest["objective"]["status"]=="open"
    assert manifest["governance"]["no_automatic_promotion"] is True
    assert odd["status"]=="open"
    assert all(x in odd["evidence"] for x in ("SM28","SM29","SM30"))
    assert "O1/O2" in odd["acceptance"]

    bands,minima=certify_original_remote_positive_bands()
    positive,terms,en,ep=actual_original_remote_positive_rayleigh()
    print("SM30 original whole-real signed positive intervals",bands,
          "minima",*[float(x) for x in minima],flush=True)
    print("SM30 actual original remote Jensen 389.56 source positive"
          " physical signed band overlaps / positive contributions",
          [(float(c),float(v),float(p)) for c,v,p in terms],flush=True)
    print("SM30 TRUE ORIGINAL positive Ao lower from 2 NEW"
          " remote whole CONTINUUM bands",float(positive),">3/10",flush=True)

    neg,pole,near,far,removed,local,remote=whole_original_remote_negative_replay()
    margin=positive-neg-pole
    print("SM30 TRUE ORIGINAL entire negative-frequency signed"
          " Kneg quadratic UPPER",float(neg),"near",float(near),
          "far",float(far),flush=True)
    print("SM30 TRUE ORIGINAL negative odd pole quadratic UPPER",
          float(pole),flush=True)
    print("SM30 original true signed whole-minus-two-band"
          " diagnostic physical Rayleigh LOWER",float(margin),flush=True)
    if margin>0:
        print("SM30 PASS SCOPED WHOLE-ORIGINAL SINGLE-VECTOR POSITIVE:"
              " actual entire signed odd original W_o(g389.56)>0,"
              " every original negative frequency and odd pole paid."
              " DOES NOT prove full original odd operator PSD.",
              flush=True)
    else:
        print("SM30 PASS SCOPED POSITIVE FREQUENCY COVERAGE:"
              " genuine remote positive response >3/10 but"
              " existing global negative UPPER is not yet"
              " sufficiently small to prove even this single"
              " true original whole-form positive witness.",
              flush=True)
    nblocks,ncols=full_original_cap_standing()
    print("SM30 full complete original SM10 negative cap retained",
          nblocks,ncols,"eta<kappa_star; NO full coupled inverse PSD",
          flush=True)
    print("SM30 W-ODD-NEG O1/O2 original full operator,"
          " even E1-E4, whole signed Weil, CC27 D-Riesz"
          " and RH OPEN; inherited infinite-dimensional"
          " spectral identification requires independent audit.",
          flush=True)


if __name__=="__main__":
    run()
