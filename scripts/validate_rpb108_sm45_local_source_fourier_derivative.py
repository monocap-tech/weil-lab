#!/usr/bin/env python3
"""SM45: verified LOCAL physical-source Fourier derivative, complete matrix.

SM44 proves actual original selected 25 odd SI10 supported Fourier
source positive-frequency WINDOW stiffness:
  -eps44 I <= A_original,W - P44 <= eps44 I
with full original 25x25 rational P44.

SM45 computes rigorous true exact-rational midpoint T'_j INTERVALS
using the ORIGINAL SM42 physical F1/F2/pole_xcos formulas, then
bounds T'' by source-supported exact rational spatial moments,
hence on every genuine original frequency cell width h,
 |T_j(xi)-v_j|
  <= midpoint_T_interval_radius
   + min(global SM44 source L_j*h/2,
         original local upper |T'_j(mid)|*h/2+K_j*h²/8).
The original SM44 source Cauchy whole FULL 25x25 Loewner
mathematics is retained with a SMALLER certified E2 per cell.
The source matrix P44 is UNCHANGED at every identical mesh,
the same true ORIGINAL seven-prime/digamma positive multiplier
and true supported odd sinh pole and 25 source-window union
are UNCHANGED. All crosses paid, no dropped odd sector.

Do NOT infer complete true low [0,4096], original 470 source
Astar resolvent, O1/O2, Weil or RH from this SOURCE WINDOW bound.
"""
import argparse,json
from fractions import Fraction as F
from pathlib import Path
from validate_rpb108_sm44_physical_fourier_cell_gram import (
    ROOT,compute,original_source_centered_windows,
    original_full_second_derivative_upper,original_physical_source_lipschitz,
    local_source_first_derivative_at_midpoint
)
from validate_rpb108_si06_negative_band import PI,B


def exact_taylor_sharpness_regression():
    """Real-rational quadratic saturates local midpoint estimate.

    f(x)=d*x+K*x²/2 on [-h/2,h/2]:
      |f(h/2)-f(0)|=d*h/2+K*h²/8, d,K>0.
    It would be unsound to drop curvature or midpoint derivative.
    """
    h=F(1,8);d=F(7,11);K=F(20)
    def f(x):return d*x+K*x*x/2
    assert f(h/2)-f(0)==d*h/2+K*h*h/8
    assert f(h/2)-f(0)>d*h/2
    # All original SOURCE Fourier second derivatives have an
    # independently valid physical moment ceiling, with no
    # assumption of sampling/analytic decay.
    assert 3<PI[0]<=PI[1]<4 and B==F(11,10)
    return True


def case(step,centers,sources,windows):
    prev=compute(step,centers,sources,windows,derivative_mode="global")
    now=compute(step,centers,sources,windows,derivative_mode="local_certified")
    assert prev["derivative_mode"]=="global"
    assert now["derivative_mode"]=="local_certified"
    assert prev["real_frequency_cells"]==now["real_frequency_cells"]
    assert prev["whole_original_cell_reference_types"]==now["whole_original_cell_reference_types"]
    assert prev["actual_true_source_window_measure"]==now["actual_true_source_window_measure"]
    assert now["locally_improved_source_cell_components"]>0
    assert 0<now["certified_local_vs_global_source_amplitude_error_sum_ratio_float"]<1
    # A stronger Loewner error for the IDENTICAL FULL rational
    # ORIGINAL physical source matrix -- not a toy comparison.
    assert now["exact_rational_complete_25x25_proxy_matrix"]==prev["exact_rational_complete_25x25_proxy_matrix"]
    assert F(now["original_true_weight_interpolation_Loewner_eps_outward"])==F(
        prev["original_true_weight_interpolation_Loewner_eps_outward"])
    assert F(now["new_true_physical_Fourier_cell_Gram_Loewner_eps_outward"])<F(
        prev["new_true_physical_Fourier_cell_Gram_Loewner_eps_outward"])
    assert F(now["total_true_original_weighted_source_window_stiffness_Loewner_eps_outward"])<F(
        prev["total_true_original_weighted_source_window_stiffness_Loewner_eps_outward"])
    # Keep audit output small by retaining actual full 625-entry
    # matrix only in the fine mesh, identical to SM44 original.
    return prev,now


def main():
    a=argparse.ArgumentParser()
    a.add_argument("--output",default="artifacts/sm45_local_original_source_fourier_derivative.json")
    args=a.parse_args()
    m=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(o for o in m["obligations"] if o["id"]=="W-ODD-NEG")
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]=="open" and odd["status"]=="open"
    assert m["governance"]["no_automatic_promotion"] is True
    assert all(e in m["evidence"] and e in odd["evidence"]
               for e in ("SM43","SM44","SM45"))
    assert "sm45_true_original_local_source_Fourier_derivative" in m["governance"]
    exact_taylor_sharpness_regression()
    centers,sources,windows=original_source_centered_windows()
    assert len(sources)==25
    l=original_physical_source_lipschitz(sources)
    k=original_full_second_derivative_upper(sources)
    assert len(l)==len(k)==25 and all(x>0 for x in l+k)
    from validate_rpb108_sm42_original_physical_gram_and_low_gate import hyperbolic_interval
    sh=hyperbolic_interval(B/2,"sinh")
    ch=hyperbolic_interval(B/2,"cosh")
    probe=local_source_first_derivative_at_midpoint(F(0),centers,sources,(sh,ch))
    assert len(probe)==25 and all(x>=0 for x in probe)
    results=[]
    for step in (F(1,4),F(1,8)):
        prev,now=case(step,centers,sources,windows)
        def slim(v):
            return {k:x for k,x in v.items()
                    if k!="exact_rational_complete_25x25_proxy_matrix"}
        print("SM45 ORIGINAL true local physical source Fourier"
              " derivative full25x25 Loewner",str(step),
              json.dumps({"previous_SM44":slim(prev),
                          "new_SM45":slim(now)},sort_keys=True),
              flush=True)
        results.append((prev,now))
    (old_coarse,new_coarse),(old_fine,new_fine)=results
    assert new_fine["real_frequency_cells"]==129
    assert new_coarse["real_frequency_cells"]==65
    assert new_fine["true_cell_gram_error_float"]<new_coarse["true_cell_gram_error_float"]
    assert new_fine["total_error_float"]<new_coarse["total_error_float"]
    # Target a MEANINGFUL practical contraction (>=5%) rather
    # than merely changing floating output or relaxing the proof.
    assert F(new_fine["new_true_physical_Fourier_cell_Gram_Loewner_eps_outward"]) < F(95,100)*F(
        old_fine["new_true_physical_Fourier_cell_Gram_Loewner_eps_outward"]),(
            "SM45 certified original local Fourier derivative failed practical >=5% reduction gate")
    def slim(v):return {k:x for k,x in v.items() if k!="exact_rational_complete_25x25_proxy_matrix"}
    output={
        "status":"CERTIFIED_TRUE_ORIGINAL_LOCAL_FOURIER_DERIVATIVE_FULL_SOURCE_WINDOW_LOEWNER",
        "canonical_W_ODD_NEG":"OPEN",
        "valid_scoped_operator_statement":
          "-eps_SM45 I25 <= original true Ao positive selected source-window stiffness - SAME full 25x25 rational SM44 matrix <= eps_SM45 I25",
        "original_true_physical_source_count":25,
        "original_zero_extended_supported_source_types":"16 genuine sin k0; 8 genuine xcos k1; 1 genuine sinh odd pole",
        "original_frequency_window_measure":"1029/64",
        "source_Fourier_midpoint_derivative":{
            "sin":"pi*(F1(c-xi)+F1(c+xi))",
            "xcos":"pi*(F2(xi+c)+F2(xi-c))",
            "sinh":"2*pi*pole_xcos(xi)",
            "true_cell_error":"midpoint interval radius+min(global first derivative*h/2, |certified true midpoint T'|*h/2 + full physical spatial-moment T'' upper*h^2/8)",
            "proof_type":"all real exact original SI06 rational phase intervals and whole source cross Cauchy; no FFT or sampled spectral sign",
            "adversarial_sharp_quadratic":"PASSED"
        },
        "coarse_SM44":slim(old_coarse),
        "coarse_SM45":slim(new_coarse),
        "fine_SM44":slim(old_fine),
        "fine_SM45":new_fine,
        "entire_original_positive_low_0_to_4096_certified":False,
        "all_470_original_odd_source_positive_Astar_inverse_certified":False,
        "original_full_odd_complete_O1_O2_certified":False,
        "remaining":[
            "higher-order source local derivative/interval and matrix-preconditioned error if still large",
            "entire original true positive low frequency [0,4096] beyond source windows",
            "full original 470 source higher-degree polynomial Fourier positive log tail and true pole-conditioned strong resolvent",
            "complete original odd Wodd O1/O2, even E1-E4, whole signed Weil, native CC27 and RH",
            "independent original Fourier and closed-domain mathematical audit"
        ]
    }
    dest=ROOT/args.output
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(output,indent=2)+"\n")
    print("SM45 SCOPED PASS: TRUE original full 25x25 source-window"
          " rational SM44 proxy unchanged; complete Fourier"
          " matrix Loewner error strictly improved using EXACT"
          " original local physical Fourier midpoint derivative"
          " and whole-real second derivative Taylor remainder."
          " Entire [0,4096], all470 Astar inverse, full odd,"
          " even, Weil, CC27 and RH OPEN.",flush=True)

if __name__=="__main__":
    main()
