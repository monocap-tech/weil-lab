#!/usr/bin/env python3
"""SM49: actual original source-adaptive extra positive Jensen response.

SM48's reference gap is a LOWER-reference insufficiency, NOT negativity
of the actual signed Weil form. Here seek missing true ORIGINAL positive
continuum near already-certified SM12 positive-frequency bands, and
score new, DISJOINT windows by response on SM48's actual physical source2
witness. No positive continuum may be counted twice.

All candidate m_original>kappa+delta windows are individually
rigorously certified with SI13 arch_lower + SI06 7-prime interval plus
the original |prime'|<=69 Lipschitz. This discovery is finite and
deterministic, with no approximate original m samples.

Each original actual 25-supported-source Fourier frequency mean is
enclosed using SM42 exact transforms and SM46 true T''/T''' bounds.
The linear source frequency derivative integrates to ZERO across
each whole symmetric rational frequency cell.

A_true_positive_low,25 >= L47 + P_extra - eps_extra I25
for all 25 original sources and cross, including true sinh pole.
An independent *direction-specific* error for source e2 is often
strictly smaller than the full-matrix Loewner eps_extra:
  e2*A_pos*e2 >= e2*L47*e2 + (P_extra)22-eps_source2.
Do not confuse the two errors or claim original full Schur positivity.

SM48 negative 15-band original suboperator lower is retained unchanged:
a reduction of its e2 gap against a positive LOWER reference is a
PROGRESS METRIC, NOT PROOF of true original signed Weil positivity.
"""
import argparse
import json
from fractions import Fraction as F

from validate_rpb108_si06_negative_band import B, prime_interval
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_si13_odd_fourier_reference import arch_lower
from validate_rpb108_sm12_positive_reference_33 import (
    CENTERS as BASE_CENTERS, RADIUS as BASE_RADIUS
)
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    F0,hyperbolic_interval,original_full_25_physical_interval_gram
)
from validate_rpb108_sm43_positive_cell_envelope import (
    ROOT, original_source_centered_windows, ceil_rat, floor_rat
)
from validate_rpb108_sm44_physical_fourier_cell_gram import (
    quantize, sqrt_upper,original_exact_physical_fourier_midpoint,
    original_full_second_derivative_upper
)
from validate_rpb108_sm46_affine_physical_fourier_source import (
    original_midpoint_derivative_intervals,original_third_spatial_moment
)
from validate_rpb108_sm47_original_full_low_jensen import (
    full_original_rational_gram, build_original_positive_jensen,TAIL
)
from validate_rpb108_sm48_original_signed_jensen_deficit import (
    original_15_negative_source_lower
)

N=25
FOCUS=2
WIDTH=F(1,50)
SIDE_CELLS=12
KEEP=32
DEN=10**12

def qceil(x):return ceil_rat(x,DEN)
def qfloor(x):return floor_rat(x,DEN)


def original_adaptive_candidate_cells(centers,sources):
    """Rigorously signed-positive full REAL candidate cells, disjoint base.

    Width 1/50 and each flank begins exactly at the old SM12
    radius 1/100. Distinct base bands are separated by >5, so
    disjoint candidate interval interiors are automatic.
    """
    assert len(BASE_CENTERS)==17 and len(sources)==N
    typ,j,k=sources[FOCUS]
    assert typ=="cluster" and k==0 and j>=0
    center_source=centers[j]
    Kfocus=original_full_second_derivative_upper(sources)[FOCUS]
    candidates=[]
    rejected=0
    for base_idx,c in enumerate(BASE_CENTERS):
        for sign in (-1,1):
            for idx in range(SIDE_CELLS):
                if sign==1:
                    a=c+BASE_RADIUS+idx*WIDTH
                    b=a+WIDTH
                else:
                    b=c-BASE_RADIUS-idx*WIDTH
                    a=b-WIDTH
                assert F(0)<a<b<F(4096)
                midpoint=(a+b)/2
                # SI13 arch_lower(a) is monotone original digamma lower.
                # Original complete all-seven-prime m(mid) interval,
                # whole-real signed derivative |mprime| for prime <=69.
                m_lower=arch_lower(a)+prime_interval(midpoint)[0]-F(69,2)*WIDTH
                if m_lower<=KAPPA+F(1,5):
                    rejected+=1
                    continue
                # Downward rational rounding guarantees no over-credit.
                delta=qfloor(m_lower-KAPPA)
                assert delta>=F(1,5) and delta<=m_lower-KAPPA
                gamma=2*WIDTH*delta
                # Original physical true selected focus SIN source only
                # at rational midpoint; no global FFT/sampling.
                transform=(F0(center_source-midpoint)-F0(center_source+midpoint))/2
                v=quantize(transform.mid())
                rad=qceil(max(abs(transform.l-v),abs(transform.h-v)))
                err=rad+Kfocus*(WIDTH/2)**2/6
                lower_gain=gamma*(v*v-2*abs(v)*err-err*err)
                candidates.append({
                    "a":a,"b":b,"c":midpoint,"base":base_idx,
                    "sign":sign,"step":idx,"delta":delta,"gamma":gamma,
                    "focus_gain_coarse":lower_gain
                })
    assert candidates and rejected>=0
    candidates.sort(key=lambda row:(row["focus_gain_coarse"],-row["c"]),
                    reverse=True)
    # We want true source-directed improvement, not global band count.
    positive=[row for row in candidates if row["focus_gain_coarse"]>0]
    assert len(positive)>=KEEP,(
        "Not enough rigorously certified source-adaptive windows",
        len(positive),len(candidates),rejected)
    chosen=positive[:KEEP]
    sorted_bands=sorted((x["a"],x["b"]) for x in chosen)
    for i in range(len(sorted_bands)-1):
        assert sorted_bands[i][1]<=sorted_bands[i+1][0]
    for a,b in sorted_bands:
        assert all(b<=c-BASE_RADIUS or a>=c+BASE_RADIUS
                   for c in BASE_CENTERS)
    return chosen,len(candidates),rejected,center_source


def original_additional_positive_source_matrix(centers,sources,chosen):
    """Complete new 25x25 positive outer product, all source cross.

    The error is both full Loewner AND separately exact source2
    entry-level, never incorrectly inferring one from the other.
    """
    sh=hyperbolic_interval(B/2,"sinh")
    ch=hyperbolic_interval(B/2,"cosh")
    global_second=original_full_second_derivative_upper(sources)
    spatial_third=original_third_spatial_moment(sources)
    matrix=[[F(0) for _ in range(N)] for _ in range(N)]
    full_error=F(0)
    focus_error=F(0)
    improved_derivatives=0
    rows=[]
    for item in chosen:
        c=item["c"];h=item["b"]-item["a"];r=h/2
        assert h==WIDTH
        gamma=item["gamma"]
        vector=original_exact_physical_fourier_midpoint(c,centers,sources,(sh,ch))
        v=[x for x,rad in vector]
        rad0=[rad for x,rad in vector]
        _,second=original_midpoint_derivative_intervals(
            c,centers,sources,(sh,ch))
        rr=[]
        for rr0,t2,glob,third in zip(rad0,second,global_second,spatial_third):
            K=glob if t2 is None else min(glob,max(abs(t2.l),abs(t2.h))+third*r)
            improved_derivatives+=int(K<glob)
            assert K>=0 and K<=glob
            rr.append(rr0+K*r*r/6)
        v2=sum((x*x for x in v),F(0))
        e2=sum((x*x for x in rr),F(0))
        # Full source-coupled Loewner certificate
        full_error+=gamma*(2*sqrt_upper(v2*e2)+e2)
        # Independently source-coordinate directional error, not
        # the (much larger) entire 25x25 scalar envelope.
        focus_error+=gamma*(2*abs(v[FOCUS])*rr[FOCUS]+rr[FOCUS]**2)
        for i in range(N):
            for j in range(i,N):
                matrix[i][j]+=gamma*v[i]*v[j]
        rows.append({
            "frequency_left":str(item["a"]),
            "frequency_right":str(item["b"]),
            "original_seven_prime_signed_excess_lower":str(item["delta"]),
            "Jensen_weight_gamma":str(gamma),
            "focus_original_source2_positive_gain_full_error_coarse":str(
                qfloor(item["focus_gain_coarse"])),
            "whole_25source_band_Loewner_error_up":str(qceil(
                gamma*(2*sqrt_upper(v2*e2)+e2)))
        })
    for i in range(N):
        for j in range(i): matrix[i][j]=matrix[j][i]
    assert all(matrix[i][j]==matrix[j][i] for i in range(N) for j in range(N))
    assert all(matrix[i][i]>=0 for i in range(N))
    return matrix,qceil(full_error),qceil(focus_error),improved_derivatives,rows


def main():
    a=argparse.ArgumentParser()
    a.add_argument("--output",default="artifacts/sm49_original_25source_adaptive_positive_jensen.json")
    args=a.parse_args()
    m=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in m["obligations"] if x["id"]=="W-ODD-NEG")
    assert m["active_obligation"]=="W-ODD-NEG"
    assert odd["status"]==m["objective"]["status"]=="open"
    assert m["governance"]["no_automatic_promotion"] is True
    assert "SM48" in m["evidence"] and "SM48" in odd["evidence"]
    centers,sources,_=original_source_centered_windows()
    assert len(sources)==N
    chosen,available,rejected,focus_center=original_adaptive_candidate_cells(
        centers,sources)
    Padd,eps_add,eps_e2,improved,rows=original_additional_positive_source_matrix(
        centers,sources,chosen)
    actual_gram,src_check,pole=original_full_25_physical_interval_gram()
    assert sources==src_check
    Hq,epsH=full_original_rational_gram(actual_gram)
    Pbase,epsP,local,mrad,bands,signed_lo=build_original_positive_jensen(
        centers,sources)
    Nmat,epsN,mneg,localneg,neg_rows=original_15_negative_source_lower(
        centers,sources)
    epsH=qceil(epsH);epsP=qceil(epsP);epsN=qceil(epsN)
    oldfee=epsP+KAPPA*(TAIL+epsH)
    oldlower=KAPPA*Hq[FOCUS][FOCUS]+Pbase[FOCUS][FOCUS]-oldfee
    neg_lower=Nmat[FOCUS][FOCUS]-epsN
    old_gap=neg_lower-oldlower
    gain_focus=Padd[FOCUS][FOCUS]-eps_e2
    new_lower=oldlower+gain_focus
    new_gap=neg_lower-new_lower
    assert old_gap>F(17,1000),(
        "SM48 exact original signed source-2 reference gap disappeared",
        float(old_gap))
    assert gain_focus>F(1,1000000),(
        "Adaptive original signed-positive source search supplied no meaningful rigorous e2 lower gain",float(gain_focus))
    assert new_gap<old_gap
    # Full-matrix lower valid even if scalar error makes the extra
    # displayed lower matrix indefinite in some directions.
    full_low_lower=[
      [KAPPA*Hq[i][j]+Pbase[i][j]+Padd[i][j]
        -(oldfee+eps_add if i==j else F(0))
       for j in range(N)] for i in range(N)
    ]
    assert all(full_low_lower[i][j]==full_low_lower[j][i]
               for i in range(N) for j in range(N))
    # Effective source-2 improvement from a *directional* error
    # does not imply the full source-coupled matrix is PSD.
    result={
      "status":"CERTIFIED_ORIGINAL_SOURCE_ADAPTIVE_EXTRA_POSITIVE_JENSEN_25SOURCE_ONLY",
      "canonical_W_ODD_NEG":"OPEN",
      "true_original_positive_low_band":"[0,4096]",
      "source_count":N,
      "all_original_25_source_cross_included":True,
      "actual_sinh_pole_retained":True,
      "focus_original_signed_deficit_witness_source_index":FOCUS,
      "focus_original_physical_source_center":str(focus_center),
      "baseline_true_original_positive_bands":17,
      "new_disjoint_signed_positive_bands":len(chosen),
      "new_certified_positive_candidate_cells":available,
      "candidate_cells_rejected_by_original_whole_real_signed_gate":rejected,
      "true_original_low_positive_full_25source_new_Loewner_error_up":str(
          eps_add),
      "true_original_low_positive_new_source2_direction_error_up":str(
          eps_e2),
      "old_original_SM47_positive_low_error_up":str(oldfee),
      "original_15band_negative_lower_source2":str(qfloor(neg_lower)),
      "old_original_SM48_nonpole_reference_deficit_source2":str(qceil(old_gap)),
      "NEW_true_original_adaptive_positive_source2_gain_lower":str(
          qfloor(gain_focus)),
      "NEW_original_15band_minus_adaptive_reference_source2_gap":str(
          qceil(new_gap)),
      "exact_fraction_strict_positive_gain":True,
      "new_original_local_second_derivative_strict_improvements":improved,
      "full_25x25_new_rational_positive_adaptive_matrix":[
          [str(q) for q in row] for row in Padd],
      "full_25x25_total_original_low_one_sided_lower_matrix":[
          [str(q) for q in row] for row in full_low_lower],
      "original_source2_directional_extra_gain_lower_matrix_cell":"(Padd)_22-epsilon_source2, independent of full25 scalar epsilon_add",
      "original_positive_band_details":rows,
      "complete_original_negative_frequency_cap_and_470_Astar_inverse":False,
      "complete_original_odd_O1_O2_even_Weil_CC27_RH":False,
      "external_original_Fourier_domain_audit":"OPEN",
      "interpretation":"New full 25-source original whole-low PSD Jensen addition and true directional improvement on original SM48 e2 method reference. Neither a genuine original signed form sign test nor complete inverse or RH."
    }
    dest=ROOT/args.output
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(result,indent=2)+"\n")
    print("SM49 actual original adaptive source-positive response",json.dumps({
       "signed_candidates":available,
       "selected":len(chosen),
       "source2_center":str(focus_center),
       "new_full_matrix_error":str(eps_add),
       "new_source2_error":str(eps_e2),
       "old_reference_deficit":float(old_gap),
       "certified_source2_extra_positive_gain":float(gain_focus),
       "new_source2_reference_gap":float(new_gap),
       "source_derivative_improvements":improved,
       "original_complete_odd_Weil_RH":"OPEN"
    }),flush=True)
    print("SM49 SCOPED: actual signed-positive adaptive 25-source Jensen gain; complete odd/even Weil and RH OPEN.",flush=True)

if __name__=="__main__":
    main()
