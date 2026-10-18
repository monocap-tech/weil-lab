#!/usr/bin/env python3
"""SM27: original C33 COMPLETE 890-source SURROGATE Schur index >=1,
versus the true original signed odd physical response on the SAME g.

Actual original analytic/evidence imports:
 SM13 17 continuous negative packets x 33 physical positive means,
        exact signed original seven-prime physical Rayleigh.
 SM12 33 protected sign-positive original physical Jensen means,
        C33>=kappa I and A_o>=C33 (no odd pole included).
 SM10 original complete 107-block/890 Taylor signed-negative upper,
        Kneg<=UDU*+eta I.
 SM14 13 additional sign-positive disjoint original bands on g,
        <g,(Ao-C33)g>>1/2.
 SM15 actual entire signed-negative plus odd pole source witness
        is independently inherited; not used to derive surrogate
        spectral inertia.

Consequence: ind_-(D^-1-U*(C33-eta I)^-1 U)>=1 (SURROGATE);
no implication for true Astar=A_o-2ss* or whole odd W_o.
All O1/O2 and even/Weil/CC27/RH closure flags remain open.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from validate_rpb108_sm13_c33_physical_negative_rayleigh import (
    positive_data,physical_single_rayleigh,
    check_new_positive_windows,certify_all_negative_windows
)
from validate_rpb108_sm14_continuum import (
    run as sm14_original_positive_replay,C as ORIGINAL_WITNESS
)
from validate_rpb108_sm15_global_negative_witness import (
    original_positive_lower
)
from validate_rpb108_sm10_explicit_odd_cap_moments import (
    full_upper_leaves,BITS,TAU
)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_sm17_compact_spectral_gate import (
    KAPPA,ETA_UP
)

ROOT=Path(__file__).resolve().parents[1]
MARGIN_FLOOR=F(3,200)


def true_original_full_source_evidence():
    assert ORIGINAL_WITNESS==F(721,50)
    neg_window=certify_all_negative_windows()
    pos_window=check_new_positive_windows()
    assert neg_window<-F(2,5)
    assert pos_window>F(2001,1000)
    positive=positive_data()
    assert len(positive)==33
    packet=physical_single_rayleigh(ORIGINAL_WITNESS,positive)
    margin=packet["margin"]
    assert margin>MARGIN_FLOOR
    assert packet["negative_lower"]>packet["positive_upper"]
    assert packet["norm_lo"]>F(0)
    assert packet["norm_hi"]>packet["norm_lo"]
    assert packet["old_positive_terms_upper"]>0
    assert packet["new_positive_terms_upper"]>0

    # SM10 COMPLETE 107 negative moment covariance blocks, all 890
    # Taylor columns and full original infinite all-frequency eta.
    clusters,width,mass,total=full_upper_leaves()
    assert len(clusters)==107 and 0<ETA_UP<KAPPA
    orders=[taylor_order(cl[-1][1]-cl[0][0],BITS)[0]
            for cl in clusters]
    assert len(orders)==107 and sum(orders)==890
    assert all(k>0 for k in orders)
    assert TAU==F(1,1024)

    # SM14 is revalidated, including all real original seven-prime
    # multiplier lower on 13 extra positive intervals and their
    # pairwise disjointness against the old C33 and negative packet.
    sm14_original_positive_replay()

    # Independent original 13-band positive-response numerical
    # rational lower (SM15 same actual source g), from all 13 means;
    # it is NOT a proof of whole W_o sign.
    ao_lower,extra=original_positive_lower()
    assert extra>F(2,3)>F(1,2)
    assert ao_lower>=extra
    # For any prospective W_o PSD, missing positive response on g
    # must exceed margin + actual nonnegative odd pole loss.
    # The displayed conservative 3/200 is already exceeded.
    assert extra>MARGIN_FLOOR
    return margin,extra,packet,orders


def finite_full_cap_index_identity():
    # Two-column signed/block Schur example only:
    # A=C33-eta I>0, D>0, actual cap U.  A-U D U^t and
    # D^-1-U^t A^-1 U have the same negative index.
    # One source creates negative even though A and D are positive.
    a=[F(3,4),F(2)]
    d=[F(1),F(1)]
    u=[F(1),F(1,3)]
    primal=[a[i]-d[i]*u[i]**2 for i in range(2)]
    dual=[1/d[i]-u[i]**2/a[i] for i in range(2)]
    assert primal[0]==-F(1,4)
    assert dual[0]==-F(1,3)
    assert primal[1]>0 and dual[1]>0
    assert sum(x<0 for x in primal)==sum(x<0 for x in dual)==1
    # A larger TRUE original positive operator Ao can fix witness:
    original_positive=[a[i]+1 for i in range(2)]
    restored=[original_positive[i]-d[i]*u[i]**2 for i in range(2)]
    assert all(x>0 for x in restored)
    # With odd pole subtracted, any surrogate quadratic only drops;
    # this does NOT make the true odd operator negative.
    pole=[F(1,10),F(0)]
    with_pole=[primal[i]-2*pole[i]**2 for i in range(2)]
    assert with_pole[0]<primal[0]
    return primal,dual,restored


def run():
    g=json.loads((ROOT/"research/obligations.json").read_text())
    assert g["active_obligation"]=="W-ODD-NEG"
    assert g["objective"]["status"]=="open"
    assert g["governance"]["no_automatic_promotion"] is True
    assert "SM26" in g["evidence"] and "SM27" in g["evidence"]
    odd=next(x for x in g["obligations"] if x["id"]=="W-ODD-NEG")
    assert odd["status"]=="open"
    assert "SM26" in odd["evidence"] and "SM27" in odd["evidence"]
    assert "O1/O2" in odd["acceptance"]
    margin,extra,p,orders=true_original_full_source_evidence()
    primal,dual,true_case=finite_full_cap_index_identity()

    print("SM27 actual original physical witness center",ORIGINAL_WITNESS,flush=True)
    print("SM27 true original full negative Kneg witness lower",
          float(p["negative_lower"]),flush=True)
    print("SM27 original all 33 positive means reference quadratic UPPER",
          float(p["positive_upper"]),flush=True)
    print("SM27 true signed original C33 failure margin LOWER",
          float(margin),"> 3/200",flush=True)
    print("SM27 complete SM10 original signed-negative cap clusters",
          len(orders),"columns",sum(orders),"eta bound",ETA_UP,flush=True)
    print("SM27 COMPLETE ORIGINAL C33-conditioned surrogate 890-source"
          " negative index >= 1 by whole-operator Schur inertia",flush=True)
    print("SM27 original 13 extra genuinely positive disjoint bands"
          " on same witness true Ao-C33 response LOWER",float(extra),flush=True)
    print("SM27 2x2 full Schur inertia finite witness",primal,dual,
          "and stronger TRUE positive operator illustrative",true_case,flush=True)
    print("SM27 PASS SCOPED: unaltered C33 original supported reference"
          " fails full coupled 890-source negative-cap Schur PSD."
          " Original A_o provides extra positive CONTINUUM on the same"
          " witness, so this does NOT determine the true Astar/odd"
          " signed Weil operator inertia; complete W-ODD-NEG O1/O2,"
          " even E1-E4, whole Weil, native CC27 and RH OPEN."
          " Independent analytic review still required.",flush=True)


if __name__=="__main__":
    run()
