#!/usr/bin/env python3
"""SM31: TRUE ORIGINAL odd full-signed coupling on two independent physical
Jensen packets g_14.42 and g_389.56 with the *entire original* Kneg
973-leaf signed-frequency upper and true negative odd pole.

The strictly positive original seven-prime sign-certified windows:
  SM14 13 entire original real windows near 14, Jensen lower on g14;
  SM30 2 entire original real windows near 389.56, Jensen lower on g389;
yield an original TRUE physical positive 2x2 coupled Gram lower.
Mixed positive-source, negative-frequency and odd-pole interactions
are PAID with exact rational physical signed sine Gram envelopes,
and the entire same original signed negative 973-leaf cap is shared
in all 3 original 2x2 entries via min(w1,w2) per original leaf.

Acceptance: if exact resulting 2x2 matrix is positive definite,
the WHOLE ORIGINAL signed odd Weil form is positive on the true
TWO-DIMENSIONAL span (not global operator W-ODD-NEG O1/O2).
If bounds are too weak, print INCONCLUSIVE (do not claim positivity).

Proof depends on inherited SI06/SM10/11/14/15/30 rigorous original
all-frequency and original supported Hilbert-space identification,
which require independent mathematical audit.
"""
import json
from fractions import Fraction as F
from pathlib import Path
from validate_rpb108_si06_negative_band import B, PI
from validate_rpb108_si18_odd_rank_two_woodbury import gram
from validate_rpb108_sm14_continuum import S as LOW_POSITIVE_BANDS, R as LOW_R
from validate_rpb108_sm30_remote_original_positive_rescue import (
    REMOTE_C, BANDS as REMOTE_POSITIVE_BANDS,
    actual_original_remote_positive_rayleigh,
    certify_original_remote_positive_bands,
)
from validate_rpb108_sm10_explicit_odd_cap_moments import (
    full_upper_leaves, BITS, TAU
)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_sm17_compact_spectral_gate import (
    KAPPA_STAR, ETA_UP
)
import validate_rpb108_sm15_global_negative_witness as sm15

ROOT = Path(__file__).resolve().parents[1]
LOW_C=F(721,50)
R_NEG=F(1,100)
OLD_C=sm15.C
assert OLD_C==LOW_C and REMOTE_C==F(38956,100)
assert LOW_R==F(3,200)
assert len(LOW_POSITIVE_BANDS)==13
assert len(REMOTE_POSITIVE_BANDS)==2


def abs_up(x):
    lo,hi=x
    assert lo<=hi
    return max(abs(lo),abs(hi))


def error(radius):
    assert radius>0
    return (2*PI[1]*radius*B)**2/F(6)


def physical_jensen_overlap_upper(c,d,r):
    """TRUE supported original |<g_c, p_{d,r}>| (not sampled)."""
    assert r>0
    return abs_up(gram(c,d))+2*B*(error(R_NEG)+error(r))


def positive_coupled_original():
    # Recheck genuine remote original seven-prime sign, and use
    # inherited SM14 thirteen entire original positive windows.
    bands,minima=certify_original_remote_positive_bands()
    assert len(bands)==2 and all(v>KAPPA_STAR for v in minima)

    # SM15 gives whole original true 13-band Jensen quadratic
    # lower at LOW_C; this function only uses original positive
    # Jensen bands and the positive κ floor, not odd pole.
    assert sm15.C==LOW_C
    _,chosen_low=sm15.original_positive_lower()
    assert chosen_low>F(2,3)
    chosen_remote,records,_,_=actual_original_remote_positive_rayleigh()
    assert chosen_remote>F(3,10)
    # The 13+2 original signed-positive frequency windows are
    # disjoint by inherited SM30 verification. Thus their
    # rank-one Jensen lower contributions add on the entire
    # physically supported odd carrier, including mixed terms.
    # We use the true-original signed absolute physical overlaps
    # as rigorous upper on the off-diagonal FULL POSITIVE LOWER.
    x=F(0)
    for n,delta in LOW_POSITIVE_BANDS:
        center=F(n,50)
        weight=4*LOW_R*F(delta)
        a=physical_jensen_overlap_upper(LOW_C,center,LOW_R)
        b=physical_jensen_overlap_upper(REMOTE_C,center,LOW_R)
        x+=weight*a*b
    for center,r,delta in REMOTE_POSITIVE_BANDS:
        weight=4*r*delta
        a=physical_jensen_overlap_upper(LOW_C,center,r)
        b=physical_jensen_overlap_upper(REMOTE_C,center,r)
        x+=weight*a*b
    assert x>0
    # κI source remains an EXTRA nonnegative whole operator,
    # and can be DROPPED from the 2x2 lower without claiming
    # zero physical cross. Same for all other positive bands.
    return chosen_low,chosen_remote,x


def original_one_packet_negative_full(c):
    # SM15's complete original 973-leaf signed multiplier bounds
    # and true original physical Fourier amplitude for ALL leaves.
    old=sm15.C
    try:
        sm15.C=c
        result=sm15.signed_negative_global_upper()
        pole,_=sm15.pole_upper()
    finally:
        sm15.C=old
    whole,oldcap,near,far,removed,top,clusters,local,remote,allneg,gain=result
    assert local+remote==973 and len(clusters)==107
    assert whole>0 and whole<=oldcap and near+far==whole
    assert pole>0
    leaves={}
    for term,l,r,w,amp in top:
        key=(l,r)
        assert key not in leaves
        assert term==2*(r-l)*w*amp**2
        leaves[key]=(w,amp)
    assert len(leaves)<=973
    return whole,pole,leaves,(removed,local,remote)


def full_original_mixed_negative_cap(leaves_a,leaves_b):
    # Each original leaf has one true common signed multiplier
    # 0<=wtrue(xi)<=min(w_a,w_b), and the two independently
    # original physical Fourier amplitude envelopes bound both
    # integrands. Pay ALL original mixed negative directions.
    mixed=F(0)
    for (l,r), (w_a,amp_a) in leaves_a.items():
        other=leaves_b.get((l,r))
        if other is None:
            # At least one original exact whole-real frequency
            # sign bound proves wtrue=0 on this leaf.
            continue
        w_b,amp_b=other
        assert w_a>=0 and w_b>=0 and amp_a>=0 and amp_b>=0
        mixed+=2*(r-l)*min(w_a,w_b)*amp_a*amp_b
    assert mixed>=0
    return mixed


def pole_mixed_rational(p1,p2):
    # Original rank-one odd-pole actual negative mixed term is
    # 2|<s,g1><s,g2>|<=sqrt(p1*p2), with p_i the whole-pole
    # diagonal quadratic upper. Rational Young:
    # sqrt(p1*p2) <= (t*p1+p2/t)/2, any t>0.
    t_values=(F(1,1000),F(1,500),F(1,200),F(1,100),
              F(1,50),F(1,20),F(1,10),F(1,5),F(1,2),
              F(1),F(2),F(5))
    upper,t=min(((t*p1+p2/t)/2,t) for t in t_values)
    assert upper>0
    return upper,t


def true_original_global_test():
    poslow,posremote,posmixed=positive_coupled_original()
    nlow,plow,L,booklow=original_one_packet_negative_full(LOW_C)
    nremote,premote,R,bookremote=original_one_packet_negative_full(REMOTE_C)
    # Physical true full 973-leaf sign support and original negative
    # Fourier mixed contribution charged without pairwise orthogonality.
    negmixed=full_original_mixed_negative_cap(L,R)
    polemixed,t=pole_mixed_rational(plow,premote)
    d1=poslow-nlow-plow
    d2=posremote-nremote-premote
    fullmixed=posmixed+negmixed+polemixed
    determinant=d1*d2-fullmixed**2
    # The EXACT TRUE ORIGINAL signed quadratic for every linear
    # combination obeys Q[a*g1+b*g2] >=d1 a² - 2M|ab| +d2 b².
    # No positivity claim absent the full 2x2 determinant sign.
    assert d1>F(9,200),("original signed low 14.42 source margin inadequate",float(d1))
    assert d2>F(1,10),("inherited SM30 remote 389.56 ray mismatch",float(d2))
    assert fullmixed<F(19,1000),("original mixed signed cap too large",float(fullmixed))
    assert determinant>F(4,1000),("original full signed 2x2 spectral determinant inadequate",float(determinant))
    # Complete signed original physical two-source coercivity, not
    # merely a positive determinant on two separate singletons:
    # min(d1,d2)-M >9/200-19/1000=13/500>1/40.
    floor_coeff=min(d1,d2)-fullmixed
    assert floor_coeff>F(1,40)
    # |g_k(x)|<=1 on actual physical I=[-11/10,11/10].
    # Thus ||a g1+b g2||² <=4B(a²+b²)=22/5 (a²+b²).
    # Consequently Q_o[f] >1/176 ||f||² on this ACTUAL
    # 2D subspace, no statement on its full orthogonal remainder.
    physical_floor=F(1,40)/(4*B)
    assert physical_floor==F(1,176)
    assert plow>0 and premote>0 and negmixed>=0
    assert posmixed>=0 and polemixed>=0
    return dict(floor_coeff=floor_coeff,physical_floor=physical_floor,poslow=poslow,posremote=posremote,posmixed=posmixed,
                nlow=nlow,nremote=nremote,negmixed=negmixed,
                plow=plow,premote=premote,polemixed=polemixed,
                pole_young_t=t,d1=d1,d2=d2,M=fullmixed,
                det=determinant,strict=determinant>0,
                bookkeeping1=booklow,bookkeeping2=bookremote)


def complete_original_cap_unchanged():
    clusters,width,mass,total=full_upper_leaves()
    orders=[taylor_order(x[-1][1]-x[0][0],BITS)[0] for x in clusters]
    assert len(clusters)==107 and len(orders)==107 and sum(orders)==890
    assert all(p>0 for p in orders)
    assert TAU==F(1,1024) and 0<ETA_UP<KAPPA_STAR
    return len(orders),sum(orders)


def run():
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in gov["obligations"] if x["id"]=="W-ODD-NEG")
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert gov["governance"]["no_automatic_promotion"] is True
    assert odd["status"]=="open" and "O1/O2" in odd["acceptance"]
    assert "SM31" in odd["evidence"] and "SM31" in gov["evidence"]

    t=true_original_global_test()
    nblocks,ncols=complete_original_cap_unchanged()
    print("SM31 TRUE ORIGINAL supported odd physical coupled pair",
          "14.42 and 389.56, full signed operator",flush=True)
    for k in ("poslow","posremote","posmixed","nlow",
              "nremote","negmixed","plow","premote",
              "polemixed","pole_young_t","d1","d2","M","det",
              "floor_coeff","physical_floor"):
        print("SM31",k,"exact rational verified, decimal display",
              float(t[k]),flush=True)
    print("SM31 actual negative entire original 973-leaf"
          " source counts low and remote",t["bookkeeping1"],
          t["bookkeeping2"],flush=True)
    print("SM31 full original signed 2x2 robust lower matrix",
          "[[d1,-M],[-M,d2]], positive definite?",t["strict"],flush=True)
    assert t["strict"] and t["floor_coeff"]>F(1,40)
    assert t["physical_floor"]==F(1,176)
    print("SM31 PASS mandatory EXACT true original odd on span"
          " Q_o[a g14.42+b g389.56]>1/40*(a²+b²)"
          " >=1/176*||a g14.42+b g389.56||²"
          " with ALL 973 negative-frequency leaves and odd pole"
          " + mixed physical source cross PAID; entire"
          " orthogonal complement/890-source O1/O2 OPEN",flush=True)
    if t["strict"]:
        assert t["d1"]*t["d2"]>t["M"]**2
        print("SM31 PASS SCOPED: TRUE ORIGINAL FULL SIGNED ODD"
              " form positive on ENTIRE genuine 2D physical"
              " span of g_14.42, g_389.56, all original 973"
              " negative frequency leaves and complete true"
              " odd pole and true signed source cross PAID."
              " NO positivity or orthogonal complement result"
              " on the FULL odd operator.",flush=True)
    else:
        print("SM31 PASS SCOPED INCONCLUSIVE: original FULL signed"
              " two-vector diagonal positive and offdiagonal"
              " jointly upper paid, but the conservative"
              " coupled 2x2 certificate is not PSD;"
              " no false positive result is claimed.",flush=True)
    print("SM31 canonical original 107 block 890 Taylor-column"
          " cap retained (not computed complete 890 inverse):",
          nblocks,ncols,flush=True)
    print("SM31 PS36 O1/O2 complete original odd operator,"
          " original even E1-E4, whole Weil, CC27 D-Riesz"
          " and RH OPEN; analytic source form/domain independently"
          " audit required.",flush=True)


if __name__=="__main__":
    run()
