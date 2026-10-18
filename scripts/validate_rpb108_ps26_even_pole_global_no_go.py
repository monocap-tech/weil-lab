#!/usr/bin/env python3
"""PS26 — partition-INDEPENDENT obstruction to pole-blind global Z certificates.

Checks pinned RC315 actual original even constant-mode Weil Q[u0] ~.040259,
exact PS15 13-source geometry and form-stable sharp split, and proves
that deleting the POSITIVE EVEN rank-one pole makes both original Q and
the actual source-ELIMINATED complementary Schur strictly NEGATIVE on
explicit constant-mode-derived witnesses.

Thus NO positive scalar block Z-majorant that drops the even pole can
certify full original complementary PSD, regardless of cell count,
cell width, or weighted-diagonal-dominance optimization.

Also records exact parity/rank-one reformulation of the *actual* even
sector. No claim that original complete Weil form is negative or
positive. No native CC27 D-Riesz bridge, W-ODD-NEG or RH closure.
"""
from fractions import Fraction as F
from pathlib import Path
import json

import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps25_finite_scale_majorant as ps25

ROOT=Path(__file__).resolve().parents[1]

def run():
    ps25.run()
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT" and lane["status"]=="open"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert all(v is False for v in lane["closures"].values())

    receipt=json.loads((ROOT/"certificates/rpb108_rc315_low_mode_sign.json").read_text())
    assert receipt["milestone"]=="RC315" and receipt["original_source_pin"]==old.ORIGINAL_PIN
    assert receipt["original_CC27_native_source_from_RC313"]
    assert receipt["original_low_diagonals"][0]["n"]==0
    assert receipt["original_low_diagonals"][1]["n"]==1
    assert not receipt["RH"] and not receipt["signed_Schur_positive_certified"]
    q0_lo,q0_hi=map(F,receipt["original_low_diagonals"][0]["physically_normalized_original_Weil_diagonal_interval"])
    assert F(0)<q0_lo<=q0_hi<F(41,1000)
    q1_lo,q1_hi=map(F,receipt["original_low_diagonals"][1]["physically_normalized_original_Weil_diagonal_interval"])
    assert F(0)<q1_lo<=q1_hi<F(7,50)

    # Original whole physical interval I=[-11/10,11/10].
    # u0(x)=1/sqrt(R), ||u0||_2=1.  c(x)=cosh(x/2)>=1.
    # Even positive pole +2|<c,u0>|^2 is >=2R=4.4.
    R=F(11,5)
    B=F(11,10)
    assert R==2*B
    whole_even_pole_lower=2*R
    original_pole_dropped_upper=q0_hi-whole_even_pole_lower
    assert original_pole_dropped_upper < -F(43,10)  # <-4.3

    # True PS15 13-source P has 13 tiny intervals of width
    # delta=2B-log9, and its L2 orthogonal complement is C.
    # Sharp 1_C u0 is actually in the ORIGINAL log-form domain
    # by PS13/PS15 form-stable interval indicators.
    ell9=old.log_i(F(9))
    delta=old.IV(R-ell9.hi,R-ell9.lo)
    assert F(1,400)<delta.lo<=delta.hi<F(1,350)
    assert len({F(1),F(9)}|{F(n) for n in (2,3,4,5,7,8)}
               |{F(9,n) for n in (2,4,5,7,8)})==13
    # c>=1 implies <c,1_C u0> >= (R-13delta)/sqrt(R).
    # Use an EXPLICIT rational lower, independent of transcendental
    # sqrt or cosh evaluation: delta <1/350.
    C_measure_lower=R-F(13,350)
    assert C_measure_lower>F(0)
    positive_even_pole_C_lower=2*C_measure_lower**2/R
    assert positive_even_pole_C_lower > F(17,4)  # >4.25
    mass_C_lower=C_measure_lower/R
    assert mass_C_lower>F(98,100)

    # The TRUE original source Schur is
    # S_C[h]=inf_{p in D_P} Q[p+h] (PS15-PS16, A_P>.323).
    # For h=1_C u0, use permissible p=1_P u0 to get
    # S_C[h] <=Q[u0]<=q0_hi. This is a VARIATIONAL UPPER bound,
    # NOT positivity of S_C.
    # Define pole-BLIND surrogate B_C[h]=S_C[h]-2|<c_C,h>|².
    # Then on h=1_C u0, B_C[h] <=q0_hi-even_pole_C_lower.
    schur_pole_dropped_upper=q0_hi-positive_even_pole_C_lower
    assert schur_pole_dropped_upper < -F(21,5)  # <-4.2
    # The same genuine surrogate has an explicit negative EVEN
    # direction, while the ORIGINAL S_C sign remains UNKNOWN.

    # More strongly, any fraction theta of the original positive even
    # pole retained in the surrogate after TRUE source elimination
    # would need theta >99.05% for positive semidefiniteness on h:
    # S_C^theta=S_C-(1-theta)*2|<c_C,h>|².
    theta_C=F(9905,10000)
    assert q0_hi - (1-theta_C)*positive_even_pole_C_lower < 0
    threshold_C=1-q0_hi/positive_even_pole_C_lower
    assert threshold_C>theta_C
    assert threshold_C<F(1)

    # Before source elimination: actual Q^theta = Q -
    # (1-theta)*2|<c,f>|² has negative u0 if theta <=99.08%.
    theta_whole=F(9908,10000)
    assert q0_hi-(1-theta_whole)*whole_even_pole_lower<0
    threshold_whole=1-q0_hi/whole_even_pole_lower
    assert threshold_whole>theta_whole

    # UNIVERSAL NO-GO (analytic implication):
    # For ANY finite/countable measurable exact partition {C_j}
    # of the ORIGINAL whole source complement, any PS25-style
    # scalar Z-majorant M that DROPS the positive even pole and
    # otherwise lower-bounds the actual source-eliminated signed
    # pole-blind form on all admissible vectors obeys
    #    (||1_{C_j} h||)_j^T M (||1_{C_j} h||)_j
    #        <= B_C[h] < -4.2,
    # on h=1_C u0. Thus M cannot be PSD. This conclusion holds
    # for EVERY mesh resolution, number of channels, and positive
    # weighted diagonal-dominance witness, not just PS25's 12.
    # The 12-window local M>1/4 never purported to cover C.
    assert schur_pole_dropped_upper < 0

    # Exact PARITY/RANK-ONE gate:
    # Original physical source/complement P,C commute with
    # reflection (labels r<->9/r). J, seven signed physical
    # prime translations in the symmetric pair form, c even
    # and s odd; original Q, A_P, its inverse, T_C and S_C
    # therefore preserve even/odd parity.
    labels={F(1),F(9)}|{F(n) for n in (2,3,4,5,7,8)}
    labels|={F(9,n) for n in (2,4,5,7,8)}
    assert len(labels)==13 and all(F(9)/r in labels for r in labels)
    # Let c_C=1_C cosh(x/2), phi=c_C/||c_C||. It lies in
    # original form domain by sharp projection invariance.
    # Write B_C=S_C -2|c_C><c_C|.
    # For any odd h, <c_C,h>=0 -> B_C[h]=S_C[h].
    # For even h=a phi+k (k even, <c_C,k>=0), exact identity:
    # S_C[a phi+k]= B_C[a phi+k]+2||c_C||² |a|².
    # An EXACT AND SUFFICIENT formal acceptance split is:
    #  (i) S_C>=0 on odd form-domain sector;
    #  (ii) B_C>=0 on even K=c_C^\perp sector;
    #  (iii) inf_{k in K form domain}
    #        (B_C[phi+k]+2||c_C||²)>=0.
    # All 3 are OPEN; the above pin proves B_C has a
    # negative even direction, necessarily coherent with c_C.
    # No bounded K-complement operator / inverse is fabricated.
    print("PS26 pinned true ORIGINAL RC315 even constant Q interval",
          float(q0_lo),float(q0_hi),flush=True)
    print("PS26 TRUE whole original even positive pole lower",
          float(whole_even_pole_lower),flush=True)
    print("PS26 original WHOLE even-pole-DROPPED Q[u0] upper",
          float(original_pole_dropped_upper),flush=True)
    print("PS26 original sharp C measure lower",float(C_measure_lower),flush=True)
    print("PS26 TRUE source-complement positive even pole on h=1_C u0 lower",
          float(positive_even_pole_C_lower),flush=True)
    print("PS26 TRUE source-eliminated even pole-DROPPED Schur[h] upper",
          float(schur_pole_dropped_upper),flush=True)
    print("PS26 NECESSARY positive even pole fraction before source >",
          float(theta_whole),flush=True)
    print("PS26 NECESSARY positive even pole fraction after source >",
          float(theta_C),flush=True)
    print("PS26 PASS SCOPED: exact partition-INDEPENDENT no-go for"
          " completing PS25's positive-even-pole-DROPPED scalar"
          " Z-majorant to the full original source complement:"
          " pinned constant test makes EVERY such full-domain"
          " Z-majorant non-PSD, regardless of mesh. Original"
          " source Schur even pole contributes >4.25, and a"
          " hypothetical global pole fraction must exceed"
          " 99.05%. PARITY-SPLIT c_C-orthogonal even carrier"
          " plus one rank-one scalar variational gate identified."
          " This is NEGATIVITY OF A SURROGATE, NOT original Q."
          " Odd native positivity, even orthogonal positivity,"
          " scalar even correction, native CC27 D-Riesz,"
          " W-ODD-NEG, W-EVEN-FORM, actual Weil and RH OPEN.",
          flush=True)

if __name__=="__main__":
    run()
