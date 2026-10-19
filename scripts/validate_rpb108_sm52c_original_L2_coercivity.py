#!/usr/bin/env python3
"""SM52C: certified ORIGINAL signed 2-source L2 coercivity corollary.

Uses the exact compact rational *complete coupled* original signed
SM52 2x2 Loewner lower pinned from passing Actions 39205091881.
The two actual supported original SI10 functions on [-B,B] are
g_2=sin(2*pi*c*x) and g_17=x*cos(2*pi*c*x), c=1845/128.
For any real coefficients z:
  Wodd(z_0*g2+z_1*g17) >= z^T L_SM52 z
                           >= lambda_G |z|^2
                           >= (69/200)*||z_0*g2+z_1*g17||_L2^2.
The Gram bound is ENTIRELY ANALYTIC:
 ||g2||^2 <= 2B, ||g17||^2 <= 2B^3/3,
 and positive Gram spectral norm <= trace <= 2B+2B^3/3.
Lambda_G=min_i (Lii-sum_{j !=i}|Lij|) via rigorous 2x2
Gershgorin. All comparisons are exact fractions.

The SI06/SM42/SI10 source/form identities are inherited, not
independently proved here. This certifies precisely a two-dimensional
trial space, not any of the remaining 23 actual physical sources,
the full 470-source inverse, complete odd negative index or RH.
"""
import json
from pathlib import Path
from fractions import Fraction as F

ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/"certificates/rpb108_sm52_original_coupled_source_matrix.json"
OUTPUT=ROOT/"artifacts/sm52c_original_2source_L2_coercivity.json"
B=F(11,10)
C=F(69,200)

def main():
    a=json.loads(INPUT.read_text())
    assert a["source_indices"]==[2,17]
    assert a["source_center"]=="1845/128"
    assert a["original_head"]=="45780c198f066c8f5934721e16244136940152b2"
    assert "39205091881" in a["source"]
    m=[[F(t) for t in row] for row in a["matrix"]]
    assert len(m)==2 and all(len(row)==2 for row in m)
    assert m[0][1]==m[1][0]
    assert all(m[i][i]>0 for i in range(2))
    det=m[0][0]*m[1][1]-m[0][1]*m[1][0]
    assert det==F(a["original_sylvester_determinant"]) and det>0
    # This denominator/compression fee was already PAID in the actual
    # original complete Loewner lower of the SM52 passing certificate.
    assert F(a["rounding_fee"])==F(7597,10**12)
    ell=min(m[i][i]-sum(abs(m[i][j]) for j in range(2) if i!=j)
            for i in range(2))
    assert ell>0
    # Original Gram H=(<g_i,g_j>) is nonnegative. Spectral upper
    # <= trace(H) <= 2B+2B^3/3 by genuine support and |sin|,|cos|<=1.
    trace_upper=2*B+2*B**3/3
    assert trace_upper==F(4631,1500)
    ratio=ell/trace_upper
    assert ratio>C
    # By L>=ell*I2 and H<=trace_upper*I2,
    # L>=C*H. Thus signed Wodd>=C||h||_L2^2 on exact 2D span.
    out={
       "status":"CERTIFIED_ORIGINAL_SIGNED_ODD_TWO_SOURCE_PHYSICAL_L2_COERCIVITY_ONLY",
       "original_W_ODD_NEG":"OPEN",
       "source_run":a["source"],
       "same_original_source_indices":a["source_indices"],
       "original_source_frequency_center":a["source_center"],
       "original_2x2_signed_lower_determinant":str(det),
       "rigorous_original_2x2_coefficient_Euclidean_lower":str(ell),
       "true_original_2x2_physical_Gram_trace_upper":str(trace_upper),
       "original_signed_over_physical_L2_lower_ratio":str(ratio),
       "certified_original_supported_two_source_L2_coercivity":str(C),
       "strict_exact_rational_margin":str(ell-C*trace_upper),
       "complete_original_25source_signed_PSD":False,
       "complete_original_470source_Astar_inverse":False,
       "original_entire_odd_O1O2_even_Weil_CC27_RH":"OPEN",
       "independent_original_Fourier_domain_audit":"OPEN",
       "interpretation":"SM52 actual original signed Wodd complete 2x2 lower implies Wodd(h)>=69/200 ||h||^2 on its genuine supported sin/xcos source span ONLY. No full odd/even spectral-index or RH conclusion."
    }
    OUTPUT.parent.mkdir(exist_ok=True,parents=True)
    OUTPUT.write_text(json.dumps(out,indent=2)+"\n")
    print("SM52C original signed trial-space physical L2:",json.dumps({
       "ell":str(ell),
       "Gram_trace_upper":str(trace_upper),
       "coercivity_lower":str(C),
       "strict_margin":str(ell-C*trace_upper),
       "full_Wodd_Weil_RH":"OPEN"
    }),flush=True)
if __name__=="__main__":main()
