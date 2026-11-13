#!/usr/bin/env python3
"""NF502 exact source-pinned angular cone-distance obstruction.

Given ORIGINAL source-native NF501 actual original 242D Q_J log trial:
q=Q_J w, e=Q_J ell_U, original gamma² from NF404.
If a physical perturbation h yields a ray Q_J(ell_U+h)
capturing all but gamma² of ||q||², then
||h||_L2(I) >= distance(e,K) >9.337e-12
where K is the two-sided cone around q with cos² >=1-gamma²/||q||².

Proof is exact planar Euclidean geometry plus rational bounds on
source-accepted ||e||², <q,e>, ||q||² and original gamma².
No full Weil source-range, domain, RH, global sign theorem.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib, json, argparse, sys
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)

NF501_SHA="7726a8a9af5faa7a22fd7581c38548c26c5a48a52cb92dc75f815c57f6e3ad7a"
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
FRAME="18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e"

def read(p):
    v=Path(p).read_bytes()
    return json.loads(v), hashlib.sha256(v).hexdigest()
def span(v):
    assert isinstance(v,list) and len(v)==2
    a,b=map(F,v)
    assert a<=b
    return a,b

def cone_controls():
    # Exact 2D Hilbert geometry: q=e1, initial e=(a,b), a,b>0.
    # For cone cosθ>=α and tanθ=β/α, the closest cone ray has
    # normal signed distance b α − a β (provided positive).
    # Integer Pythagorean triple: α=4/5, β=3/5, e=(1,2).
    a,b=F(1),F(2)
    alpha,beta=F(4,5),F(3,5)
    assert alpha**2+beta**2==1
    assert b*alpha-a*beta==F(1)
    # Nearest point on boundary ray (alpha,beta).
    t=a*alpha+b*beta
    nearest=(t*alpha,t*beta)
    assert (a-nearest[0])**2+(b-nearest[1])**2 ==F(1)
    # Invariance under scaling the original ray, source polarity.
    for sign in [-1,1]:
        assert abs(sign*a)==a
    # A vector outside the cone may be projected into the cone only
    # through a perturbation whose norm reaches the positive distance.
    assert b*alpha>a*beta
    return 6

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--nf501",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    n,sha=read(args.nf501)
    original,originalsha=read("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seams,seamsha=read("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    nf404,nf404sha=read("notes/data/provisional/NF404_original_selected_pole_shear_exact.json")
    assert sha==NF501_SHA and n["pass"]=="NF501-native"
    assert originalsha==n["original_nf407_source_SHA256"]==SRC
    assert seamsha==n["original_nf406_seams_SHA256"]==SEAM
    assert n["original_nf404_SHA256"]==nf404sha
    assert n["original_physical_frame_SHA256"]==FRAME
    assert n["original_J242_Gram_frame_identity_verified"] is True
    assert n["original_source_selected_raw_moments_verified"]==242
    assert n["original_source_correlated_U110_and_basisTaylor_order"]==600
    assert nf404["pass"]=="NF404" and nf404["original_dimension"]==242
    assert nf404["original_selected_pole_index"]==241
    assert n["original_projected_one_ray_sufficient_Hilbert_gate"]=="CERTIFIED_FAIL"
    assert n["full_Weil_source_multiplier_image_eligibility"] is False
    assert n["full_even_odd_Weil_operator_graph_domain"]==n["W_ODD_NEG"]==n["RH"]=="OPEN"

    qlo,qhi=span(n["true_original_Q_Jw_squared_from_K_D7_D8_R_outward"])
    elo,ehi=span(n["true_original_Q_J_ell_squared_outward"])
    vlo,vhi=span(n["true_original_Q_J_centered_w_inner_Qell_outward"])
    gamma2=F(n["original_gamma_squared"])
    assert gamma2==F(nf404["exact_source_original_full_complement_power_budget"])
    assert qlo>F("1.578e-22") and qhi<F("1.607e-22")
    assert elo>F("8.73e-23") and ehi<F("8.74e-23")
    assert vlo<=vhi<0 and -vlo<F("2.59e-25")
    assert 0<gamma2<F("5.13e-26")

    # q direction qhat, and e decomposition parallel a and perpendicular b:
    # a=|<q,e>|/||q||, b²=||e||²-a².
    # True ||q|| >1.25e-11, gamma <2.27e-13.
    qnormlo=F("1.25e-11")
    gamma_hi=F("2.27e-13")
    assert qlo>qnormlo*qnormlo
    assert gamma2<gamma_hi*gamma_hi
    a_hi=F("2.072e-14")
    b_lo=F("9.34e-12")
    assert (-vlo)<a_hi*qnormlo
    assert elo-a_hi*a_hi>b_lo*b_lo

    # Capturing all but gamma² requires |<qhat,u>|/||u|| >= alpha,
    # alpha=sqrt(1-gamma²/||q||²), beta=gamma/||q||.
    # Exact rational root-free safety brackets:
    beta_hi=F("0.019")
    alpha_lo=F("0.9998")
    assert gamma_hi/qnormlo<beta_hi
    assert alpha_lo**2+beta_hi**2<1

    # The angular distance from e to the union of eligible cones is
    # min||e-u|| >= b*alpha-a*beta, where b perpendicular to qhat,
    # a=abs(<qhat,e>), beta=sin(max allowed angle).
    # Our strict rational bounds certify the separation without roots.
    dist_lb=b_lo*alpha_lo-a_hi*beta_hi
    assert dist_lb==F("9.33773832e-12")
    assert dist_lb>F("9.337e-12")
    assert dist_lb>F("1e-29")
    assert cone_controls()==6

    # Independently confirm close smooth candidate is far inside STOP
    # neighborhood. This does not classify arbitrary distant directions.
    assert F(n["original_global_L2_smoothing_error_eta_upper"])==F("1e-29")
    assert F("1e-29")<dist_lb
    result={
        "pass":"NF502",
        "standing":"EXACT original-source angular-cone separation: ANY physical L2 perturbation of the specific terminal log ray ell_U capable of passing unchanged original one-ray NF404 Hilbert complement gate requires norm >9.337e-12; not a global source-family, Weil-domain, or RH theorem",
        "original_nf501_native_SHA256":sha,
        "original_nf404_SHA256":nf404sha,
        "source_original_nf407_SHA256":SRC,
        "source_original_nf406_seam_SHA256":SEAM,
        "original_selected_dim":242,
        "original_full_Q_Jw_squared_strict_lower":"1.578e-22",
        "original_original_Q_Jell_squared_strict_lower":"8.73e-23",
        "original_original_Q_Jell_inner_Q_Jw_abs_strict_upper":"2.59e-25",
        "original_gamma_squared_strict_upper":"5.13e-26",
        "original_q_norm_strict_lower":str(qnormlo),
        "original_gamma_norm_strict_upper":str(gamma_hi),
        "cone_parallel_a_strict_upper":str(a_hi),
        "cone_perpendicular_b_strict_lower":str(b_lo),
        "necessary_capture_cone_alpha_strict_lower":str(alpha_lo),
        "necessary_capture_cone_beta_strict_upper":str(beta_hi),
        "exact_rational_distance_lower":str(dist_lb),
        "necessary_physical_perturbation_L2_greater_than":"9.337e-12",
        "old_NF499_smooth_collar_L2_error_less_than":"1e-29",
        "frozen_original_J_and_gamma_one_ray_smooth_collars_must_FAIL":True,
        "new_direction_source_range_or_graph_domain":"OPEN",
        "unrestricted_new_subspace_or_new_source_family":"OPEN",
        "W_ODD_NEG":"OPEN","RH":"OPEN"
    }
    Path(args.output).write_text(json.dumps(result,indent=2)+"\n")
    print("NF502 ORIGINAL exact-Fraction cone geometry and original source custody PASS")
    print("NF502 any one-ray replacement of genuine original ell_U meeting frozen NF404 gate needs physical L2 displacement >9.337e-12")
    print("NF502 certified smoothed original NF499 phi at <1e-29 is decisively excluded without operator/domain assumptions")
    print("NF502 general selected source, full Weil sign, RH OPEN")

if __name__=="__main__":
    main()
