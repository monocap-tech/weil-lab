#!/usr/bin/env python3
"""NF452: strict two-sided original J8 terminal signed moment enclosure.

Exact-rational verification imports the already source-certified NF411 u4(B)
Arb ball (including its native radius), NF450 outward complete z(B), NF451
compact-kernel modulus, and original NF411 seven independent prime weights.
No x/t quadrature, no polynomial shadow, no full J7/J8 sign promotion.
"""
import argparse
import hashlib
import json
import re
from fractions import Fraction as Q
from pathlib import Path

B = Q(11, 10)
DELTA = Q(1, 10**15)
SOURCE_SHA = "0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAMS_SHA = "c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
PRIMES = (2, 3, 4, 5, 7, 8, 9)

def read(path):
    raw = Path(path).read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()

def arb_ball(s):
    """Outward decimal Arb display [center e exponent +/- radius e exponent]."""
    m = re.fullmatch(r"\[([+-]?[0-9]+(?:\.[0-9]+)?)e([+-]?[0-9]+)\s+\+/-\s+([0-9]+(?:\.[0-9]+)?)e([+-]?[0-9]+)\]", s.strip())
    assert m is not None, "unrecognized native original endpoint ball"
    center = Q(m.group(1)) * (Q(10) ** int(m.group(2)))
    radius = Q(m.group(3)) * (Q(10) ** int(m.group(4)))
    assert radius > 0
    return center-radius, center+radius

def log_interval(t, n=48):
    """Exact rational Taylor/artanh enclosure of log(t), t>1."""
    assert t > 1
    z = (t-1) / (t+1)
    assert 0 < z < 1
    partial = 2 * sum((z**(2*k+1))/Q(2*k+1) for k in range(n))
    remainder = 2*z**(2*n+1)/(Q(2*n+1)*(1-z*z))
    return partial, partial+remainder

def run(source_path, seams_path, nf411_path, nf450_path, nf451_path):
    source, original_sha = read(source_path)
    seams, seam_sha = read(seams_path)
    jet, jet_sha = read(nf411_path)
    endpoint, endpoint_sha = read(nf450_path)
    collar, collar_sha = read(nf451_path)

    assert original_sha == SOURCE_SHA and seam_sha == SEAMS_SHA
    assert source["original_dimension"] == 242
    assert len(source["original_exact_native_original_four_critical_coefficients_mid_radius"]) == 4
    assert len(source["original_source_critical_sine_frequencies"]) == 32
    assert jet["nf407_source_sha256"] == original_sha
    assert jet["original_source_selected_count"] == 242
    assert jet["original_source_critical_count"] == 4
    assert jet["original_source_native_radii_paid_for_endpoint_derivative"]
    assert not jet["original_full_arch_x_t_quadrature_certified"]
    assert endpoint["source_SHA256"] == original_sha
    assert endpoint["seams_SHA256"] == seam_sha
    assert endpoint["original_raw_JSON_permanent_repo_archive_due"]
    assert endpoint["original_CI_result"] == "SUCCESS"
    assert endpoint["complete_z_B_strictly_negative"]
    assert collar["original_source_sha256"] == original_sha
    assert collar["original_seams_sha256"] == seam_sha
    assert collar["CI_result"] == "SUCCESS"
    assert collar["collar_width"] == str(DELTA)
    assert collar["collar_original_p_strictly_negative"]
    assert Q(collar["collar_z_strict_upper"]) == -Q(4, 10**10)

    n9 = next(r for r in seams["original_prime_power_log_shifts"] if r["n"] == 9)
    assert 2*B - Q(n9["log_upper"]) > Q(1,1000) > DELTA

    v_lo, v_hi = arb_ball(jet["original_original_source_value_at_B_arb"])
    # Independently check explicit strict rational source-v bounds.
    assert -Q(116799,10**16) < v_lo < v_hi < -Q(116798,10**16)
    z_lo, z_hi = (Q(s) for s in endpoint["complete_z_B_outward_24_decimal"])
    assert z_lo < z_hi < 0
    assert -Q(5,10**10) < z_lo < z_hi < -Q(4,10**10)
    v_abs_lo,v_abs_hi = -v_hi,-v_lo
    z_abs_lo,z_abs_hi = -z_hi,-z_lo

    weights = jet["all_seven_original_prime_seam_derivative_identities"]
    assert tuple(w["prime_power"] for w in weights) == PRIMES
    C_lo = sum(Q(w["c_n_positive_outward"][0]) for w in weights)
    C_hi = sum(Q(w["c_n_positive_outward"][1]) for w in weights)
    assert 3 < C_lo <= C_hi < 4

    # log(B/DELTA) = log(11/10)+15*log(5/4)+45*log(2).
    # Every summand is enclosed via its own positive-argument atanh series.
    logB_lo,logB_hi = log_interval(Q(11,10))
    logfive_lo,logfive_hi = log_interval(Q(5,4))
    logtwo_lo,logtwo_hi = log_interval(Q(2))
    L_lo = logB_lo + 15*logfive_lo +45*logtwo_lo
    L_hi = logB_hi + 15*logfive_hi +45*logtwo_hi
    assert L_lo < L_hi and 34 < L_lo < L_hi < 36
    # Independent finite-rational checks without relying on log evaluation.
    # e>8/3, e<11/4; both from elementary exponential series bounds.
    assert Q(11,4)**34 < B/DELTA < Q(8,3)**36

    # Original principal p(B-d)=v*(log(B/d)/2+C).
    # Exact constant-endpoint model after analytic log integration:
    # D0=2*DELTA*v*Z*(L+1+2*C)+2*DELTA*Z^2.
    model_lo = 2*DELTA*v_abs_lo*z_abs_lo*(L_lo+1+2*C_lo) + 2*DELTA*z_abs_lo*z_abs_lo
    model_hi = 2*DELTA*v_abs_hi*z_abs_hi*(L_hi+1+2*C_hi) + 2*DELTA*z_abs_hi*z_abs_hi

    # NF451 accepted complete source modulus:
    # |e(d)|=|z(B-d)-Z|<d*(14000+600*log(2B/d)).
    # Since log 2<1, <=d*(14600+600*h), h=log(B/d).
    # Define M as the latter majorant. All h^j d integrals are exact.
    # I0=DELTA^2/2, I1=I0*(L+1/2), I2=I0*(L^2+L+1/2).
    i0 = DELTA*DELTA/2
    i1up = i0*(L_hi+Q(1,2))
    i2up = i0*(L_hi*L_hi+L_hi+Q(1,2))
    int_M = 14600*i0 + 600*i1up
    # |p|M <= |v| d (h/2+C)(14600+600*h)
    #       <= |v| d (300*h^2+11500*h+102200).
    int_pM = v_abs_hi*(300*i2up + 11500*i1up + 102200*i0)
    # d*(14000+600 log(2B/d)) is increasing on (0,DELTA].
    Mmax = DELTA*(14000+600*(L_hi+1))
    assert Mmax < Q(37400,10**15)
    error_bound = 4*int_pM + 4*z_abs_hi*int_M + 2*Mmax*int_M
    D_lo,D_hi = model_lo-error_bound,model_hi+error_bound

    # Exact strict two-sided integral gate; no numerical mesh estimates.
    assert D_lo > Q(75,10**35), "lower certificate misses 7.5e-34"
    assert D_hi < Q(9,10**34), "upper certificate misses 9e-34"
    assert D_lo > Q(collar["original_D8_terminal_collar_strict_lower"])
    assert D_lo < D_hi

    return {
        "pass":"NF452",
        "standing":"ACCEPTED only after focused exact-rational source-native-jet custody CI; actual original J8 terminal collar TWO-SIDED signed moment, not whole J8/J7",
        "original_source_sha256":original_sha,
        "original_seams_sha256":seam_sha,
        "original_nf411_endpoint_native_receipt_sha256":jet_sha,
        "original_nf450_endpoint_custody_sha256":endpoint_sha,
        "original_nf451_terminal_custody_sha256":collar_sha,
        "original_physical_source_generators":246,
        "original_273_frequency_order_groups_retained":True,
        "original_n9_seam_outside_terminal_collar":True,
        "delta":str(DELTA),
        "original_source_v_interval":[str(v_lo),str(v_hi)],
        "original_zB_interval":[str(z_lo),str(z_hi)],
        "original_all_seven_prime_weight_C_interval":[str(C_lo),str(C_hi)],
        "log_B_over_delta_rational_enclosure":[str(L_lo),str(L_hi)],
        "exact_original_endpoint_model":[str(model_lo),str(model_hi)],
        "original_complete_compact_remainder_integral_error_upper":str(error_bound),
        "original_terminal_D8_strict_interval":[str(D_lo),str(D_hi)],
        "simple_strict_2sided_original_D8_collar":[str(Q(75,10**35)),str(Q(9,10**34))],
        "certified_original_signed_D8_collar_lower_gt_7p5e_minus34":True,
        "certified_original_signed_D8_collar_upper_lt_9e_minus34":True,
        "whole_original_J8_signed_integral":"OPEN",
        "whole_original_J7_signed_integral":"OPEN",
        "NF410_NF404_global":"OPEN",
        "E_p":"OPEN",
        "J242_fourth_exterior":"OPEN",
        "W_ODD_NEG":"OPEN",
        "RH":"OPEN",
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    ap.add_argument("--nf411",default="notes/data/provisional/NF411_original_source_boundary_jet.json")
    ap.add_argument("--nf450",default="notes/data/provisional/NF450_original_B_complete_Laplace_native_sign_custody_index.json")
    ap.add_argument("--nf451",default="notes/data/provisional/NF451_original_J8_terminal_collar_custody_index.json")
    ap.add_argument("--output",default=None)
    args=ap.parse_args()
    result=run(args.source,args.seams,args.nf411,args.nf450,args.nf451)
    if args.output:
        path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(json.dumps(result,indent=2)+"\n")
    print("NF452 original signed terminal two-sided:",result["simple_strict_2sided_original_D8_collar"])
    print("NF452 true original J7/J8 whole cells, W-ODD-NEG, RH OPEN")
if __name__=="__main__":main()
