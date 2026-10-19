#!/usr/bin/env python3
"""SM47: certified ORIGINAL low [0,4096] 25-source LOWER form, not an inverse.

Unlike SM46's symmetric approximation to a limited source-window stiffness,
SM47 has NO unproved contribution from uncovered positive frequencies:
  a_o(xi) = max(kappa,m_original(xi)) >= kappa everywhere on [0,4096].
SM42 Parseval/source tail gives the whole-band floor
  A_low >= kappa*(H-(2E/L)*I), L=4096, E=202/25.
On the 17 disjoint original SM12 signed-positive REAL windows
I_j=[c_j-r,c_j+r] with m(xi)>kappa+DELTA (DELTA=2), Jensen gives
  A_low >= kappa*(H-(2E/L)*I)+4*r*DELTA*sum u_j*u_j^T
where u_j is the exact frequency-average of the 25 ORIGINAL physical
sine transforms T_i over I_j.

SM44/SM46's certified midpoint source intervals and true source second
frequency derivative bounds prove |u_ij-v_ij|<=
  midpoint_interval_radius + K_ij*r*r/6.
The frequency average cancels the first derivative exactly. All 25
source cross terms, including the true sinh pole, remain. Exact rational
Cauchy supplies a Loewner epsilon for P=4*r*DELTA*sum v_j*v_j^T.
SM42's exact original 25x25 physical interval Gram supplies Hq and an
independent full-matrix Gershgorin rounding error eps_H.

FINAL PROVED CONDITIONAL ON INHERITED ORIGINAL PHYSICAL/FOURIER IDENTITIES:
  A_low_original25 >= kappa*Hq + P -
         (kappa*(2E/L+eps_H)+eps_P)*I25.
This is a ONE-SIDED true-original whole LOW form inequality, not a
complete 25-source inverse, all 470 sources, whole odd Schur, Weil or RH.
"""
import argparse
import json
from fractions import Fraction as F

from validate_rpb108_si06_negative_band import B
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm12_positive_reference_33 import (
    CENTERS as POS_CENTERS, RADIUS, DELTA, check_new_positive_windows
)
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    original_full_25_physical_interval_gram, hyperbolic_interval
)
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT, original_source_centered_windows, ceil_rat, floor_rat
)
from validate_rpb108_sm44_physical_fourier_cell_gram import (
    quantize, sqrt_upper, original_exact_physical_fourier_midpoint,
    original_full_second_derivative_upper
)
from validate_rpb108_sm46_affine_physical_fourier_source import (
    original_midpoint_derivative_intervals, original_third_spatial_moment
)

L=4096
E=F(202,25)  # Original SM42/SM41 exact raw source high-frequency L2 tail.
TAIL=2*E/L


def full_original_rational_gram(gram):
    """Whole ORIGINAL physical 25x25 Gram: interval -> symmetric rational.

    If |(H-Hq)_ij|<=err_ij, then -eps_H I<=H-Hq<=eps_H I
    via exact rational absolute-row-sum domination.
    """
    n=len(gram)
    assert n==25 and all(len(row)==n for row in gram)
    h=[[quantize(t.mid()) for t in row] for row in gram]
    row_errors=[]
    for i in range(n):
        row_errors.append(sum(
            max(abs(gram[i][j].l-h[i][j]),
                abs(gram[i][j].h-h[i][j]))
            for j in range(n)
        ))
    eps=max(row_errors)
    assert eps>=0
    assert all(h[i][j]==h[j][i] for i in range(n) for j in range(n))
    return h,eps


def build_original_positive_jensen(centers,sources):
    """17 genuinely positive original real bands, complete source coupling.

    One exact mean vector u per band; v is certified rational midpoint
    source vector. Original true T'' upper K on each real band allows
    |mean(T)-T(c)|<=K*r²/6, not the pointwise K*r²/2.
    """
    assert len(POS_CENTERS)==17 and len(sources)==25
    assert all(F(0)<c-RADIUS<c+RADIUS<F(L) for c in POS_CENTERS)
    assert all(POS_CENTERS[j]+RADIUS<POS_CENTERS[j+1]-RADIUS
               for j in range(len(POS_CENTERS)-1))
    signed_lower=check_new_positive_windows()
    assert signed_lower>KAPPA+DELTA
    assert DELTA==2 and RADIUS==F(1,100)
    gamma=4*RADIUS*DELTA
    assert gamma==F(2,25)

    sh=hyperbolic_interval(B/2,"sinh")
    ch=hyperbolic_interval(B/2,"cosh")
    second_glob=original_full_second_derivative_upper(sources)
    third_glob=original_third_spatial_moment(sources)
    n=len(sources)
    matrix=[[F(0) for _ in range(n)] for _ in range(n)]
    eps=F(0)
    max_single_rad=F(0)
    local_second_improvements=0
    bands=[]
    for c in POS_CENTERS:
        m=original_exact_physical_fourier_midpoint(c,centers,sources,(sh,ch))
        v=[q for q,rad in m]
        midpoint_rad=[rad for q,rad in m]
        _,seconds=original_midpoint_derivative_intervals(
            c,centers,sources,(sh,ch))
        K=[]
        for s,g,t in zip(seconds,second_glob,third_glob):
            ki=g if s is None else min(g,max(abs(s.l),abs(s.h))+t*RADIUS)
            assert 0<=ki<=g
            if ki<g:local_second_improvements+=1
            K.append(ki)
        err=[rr+ki*RADIUS**2/6 for rr,ki in zip(midpoint_rad,K)]
        assert len(err)==n
        max_single_rad=max(max_single_rad,max(err))
        v2=sum((q*q for q in v),F(0))
        e2=sum((q*q for q in err),F(0))
        # ||uu^T-vv^T|| <= 2||v||||u-v||+||u-v||²,
        # with exact integer-square-root certified upward rounding.
        band_eps=gamma*(2*sqrt_upper(v2*e2)+e2)
        eps+=band_eps
        for i in range(n):
            for j in range(i,n):
                matrix[i][j]+=gamma*v[i]*v[j]
        bands.append({
            "center":str(c),
            "gamma":str(gamma),
            "source_mean_interval_norm2_radius_up":str(
                ceil_rat(e2,10**9)),
            "rational_full_25_source_band_Loewner_error_up":str(
                ceil_rat(band_eps,10**9))
        })
    for i in range(n):
        for j in range(i):
            matrix[i][j]=matrix[j][i]
    assert all(matrix[i][j]==matrix[j][i]
               for i in range(n) for j in range(n))
    assert all(matrix[i][i]>=0 for i in range(n))
    # Matrix P is PSD by exact Gram factorization, but P-eps*I
    # is NOT claimed PSD on its kernel.
    return matrix,eps,local_second_improvements,max_single_rad,bands,signed_lower


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm47_original_full_low_25_source_jensen_lower.json")
    args=p.parse_args()
    manifest=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in manifest["obligations"] if x["id"]=="W-ODD-NEG")
    assert manifest["active_obligation"]=="W-ODD-NEG"
    assert manifest["objective"]["status"]=="open" and odd["status"]=="open"
    assert manifest["governance"]["no_automatic_promotion"] is True
    assert "SM46" in odd["evidence"] and "SM42" in odd["evidence"]
    centers,sources,_=original_source_centered_windows()
    physical_gram,gram_sources,pole=original_full_25_physical_interval_gram()
    assert sources==gram_sources
    h,eps_h=full_original_rational_gram(physical_gram)
    P,eps_p,local_improvements,max_rad,bands,signed_lower=build_original_positive_jensen(
        centers,sources)
    n=25
    total_err=KAPPA*(TAIL+eps_h)+eps_p
    lower=[[KAPPA*h[i][j]+P[i][j]-(total_err if i==j else F(0))
            for j in range(n)] for i in range(n)]
    assert all(lower[i][j]==lower[j][i] for i in range(n) for j in range(n))
    assert len(bands)==17 and local_improvements>0
    # Fail closed on quantitative feasibility: unlike SM46's coarse
    # source-window two-sided fee 76.979, narrow original signed-positive
    # Jensen means must be controlled more tightly.
    assert eps_p<F(1,10),("SM47 original 17-window mean Loewner budget too large",
                          float(eps_p))
    positive_diag=[i for i in range(n) if P[i][i]>total_err]
    assert positive_diag,("No actual 25-source diagonal with resolved gain",
                          float(eps_p),float(max(P[i][i] for i in range(n))))
    result={
       "status":"CERTIFIED_SCOPED_ORIGINAL_25_SOURCE_WHOLE_LOW_ONE_SIDED_JENSEN_LOWER",
       "canonical_W_ODD_NEG":"OPEN",
       "original_positive_low_frequency_region":"[0,4096]",
       "entire_low_accounted_for_by":"SM42 global kappa Parseval floor and rigorous high tail; omit all other nonnegative excess; SM12 disjoint certified real positive windows yield Jensen gain",
       "original_genuine_signed_positive_windows":17,
       "original_SM12_signed_multiplier_lower_exact_outward":str(floor_rat(signed_lower,10**6)),
       "actual_original_source_dimension":25,
       "physical_sources":"16 zero-extended sin, 8 zero-extended xcos, 1 actual sinh pole",
       "true_original_spectral_lower":"A_low_25 >= kappa*Hq + P - (kappa*(2E/4096+eps_H)+eps_P)*I25",
       "SM42_high_frequency_tail_raw_upper_I":str(TAIL),
       "original_25x25_physical_gram_quantization_error_exact_up":str(
            ceil_rat(eps_h,10**12)),
       "original_17_positive_band_25x25_mean_Gram_error_exact_up":str(
            ceil_rat(eps_p,10**12)),
       "complete_lower_matrix_error_exact_up":str(
            ceil_rat(total_err,10**12)),
       "source_mean_max_component_radius_exact_up":str(
            ceil_rat(max_rad,10**12)),
       "certified_local_second_derivative_strict_improvements":local_improvements,
       "original_source_directions_with_Jensen_gain_above_full_band_matrix_error":len(positive_diag),
       "original_source_directions_with_gain_above_Jensen_error":positive_diag,
       "exact_rational_full_25x25_original_low_lower_matrix":[
           [str(v) for v in row] for row in lower],
       "exact_rational_17_window_positive_25x25_reference_matrix":[
           [str(v) for v in row] for row in P],
       "window_diagnostics":bands,
       "entire_true_original_low_lower_bound_certified":True,
       "entire_low_two_sided_stiffness_certified":False,
       "all_470_original_Astar_inverse_certified":False,
       "complete_original_odd_O1_O2_certified":False,
       "original_even_E1_E4_Weil_CC27_RH_certified":False,
       "independent_original_Fourier_and_closed_domain_audit":"OPEN"
    }
    dest=ROOT/args.output
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(result,indent=2)+"\n")
    print("SM47 original complete-low 25-source JENSEN lower:",json.dumps({
        "positive_real_windows":len(bands),
        "full_original_gram_err":result["original_25x25_physical_gram_quantization_error_exact_up"],
        "jensen_source_mean_err":result["original_17_positive_band_25x25_mean_Gram_error_exact_up"],
        "whole_low_lower_err":result["complete_lower_matrix_error_exact_up"],
        "positive_diagonal_gains":len(positive_diag),
        "local_second_improvements":local_improvements,
        "full_odd_Weil_RH":"OPEN"
    }),flush=True)
    print("SM47 SCOPED: no source-window interpolation fee in this independent one-sided source Jensen route; complete [0,4096] covered by kappa floor and a 17-band PSD gain; full 470 Astar inverse, complete W-ODD-NEG, even, Weil, CC27, RH remain OPEN.",flush=True)

if __name__=="__main__":
    main()
