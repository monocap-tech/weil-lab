#!/usr/bin/env python3
"""NF460: original physical bulk seam jumps and H1 method obstruction."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json,argparse
B=F(11,10);DELTA=F(1,10**15)
SOURCE="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
GEOM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
D=Path(__file__).resolve().parents[2]/"notes/data/provisional"
def load(name):
    raw=(D/name).read_bytes()
    return json.loads(raw),sha256(raw).hexdigest()
def pair(z):return tuple(map(F,z))
def overlap(a,b):return a[0]<=b[1] and b[0]<=a[1]
def dec(a,n=26):
    factor=10**n
    lower=a[0]*factor;upper=a[1]*factor
    floor=lower.numerator//lower.denominator
    ceil=-((-upper.numerator)//upper.denominator)
    return [str(F(floor,factor)),str(F(ceil,factor))]
def main():
    jet,hjet=load("NF411_original_source_boundary_jet.json")
    principal,hprincipal=load("NF407_original_prime_jump_log_power_exact.json")
    seams,hseams=load("NF406_original_prime_support_partition_exact.json")
    nf404,h404=load("NF404_original_selected_pole_shear_exact.json")
    nf403,h403=load("NF403_original_joint_complement_power_exact.json")
    nf459,h459=load("NF459_original_native_244D_terminal_K_custody.json")
    nf458,h458=load("NF458_original_endpoint_leverage_gate_custody.json")
    assert jet["nf407_source_sha256"]==nf459["original_nf407_source_sha256"]==SOURCE
    assert jet["nf407_principal_sha256"]==hprincipal
    assert principal["original_nf406_seams_sha256"]==hseams==GEOM
    assert nf459["original_nf406_seams_sha256"]==GEOM
    assert principal["source_all_original_prime_jumps_cancelled_from_z"] is True
    assert "Lambda(n)/sqrt(n)" in principal["source_r_formula"]
    assert nf459["original_complete_two_sided_terminal_T_collar_power_strict_upper"]=="8e-32"
    assert nf458["physical_augmented_dimension"]==244
    assert nf404["original_dimension"]==242 and nf404["original_selected_pole_index"]==241
    v=pair(principal["original_source_u4_endpoint_interval"])
    assert v[1]<0
    jumps=principal["source_true_original_prime_jump_terms"]
    coeff=jet["all_seven_original_prime_seam_derivative_identities"]
    knots=seams["certified_ordered_knots"]
    order=(3,4,2,5,7,8,9)
    pos=[k for k in knots if F(k["low"])>=0]
    assert len(pos)==9 and [k["label"] for k in pos]==(
        ["0","B-log(3)","-B+log(4)","B-log(2)","-B+log(5)",
         "-B+log(7)","-B+log(8)","-B+log(9)","+B"])
    assert all(F(pos[i]["high"])<F(pos[i+1]["low"]) for i in range(8))
    assert F(pos[-2]["high"])<B-DELTA
    out=[]
    for term,der in zip(jumps,coeff):
        n=term["n"]
        assert n==der["prime_power"] and n in order
        w=pair(term["signed_mangoldt_weight_positive_interval"])
        assert pair(der["c_n_positive_outward"])==w and w[0]>0
        a=pair(term["source_jump_amplitude_interval"])
        product=(v[0]*w[1],v[1]*w[0])
        assert overlap(product,a) and a[1]<0
        loc=pair(term["positive_jump_location_absolute_interval"])
        knot=pos[order.index(n)+1]
        assert overlap(loc,(F(knot["low"]),F(knot["high"])))
        out.append(dict(n=n,positive_seam_location_approx=float(sum(loc)/2),
                        residual_jump_outward_decimal=dec(a),strict_negative=True))
    seven=next(pair(t["source_jump_amplitude_interval"]) for t in jumps if t["n"]==7)
    assert -seven[1]>F(859,10**14)  # >8.59e-12
    assert all(-seven[1]>-pair(t["source_jump_amplitude_interval"])[0]
               for t in jumps if t["n"]!=7)
    continuous_uniform_error_floor=-seven[1]/2
    assert continuous_uniform_error_floor>F(429,10**14) # >4.29e-12
    # A continuous global model approximating h on both sides of an interior
    # jump must have uniform error >= half that jump, independently of degree.
    # This is NOT an L2 obstruction; segmentwise source models remain allowed.
    gamma=F(nf404["exact_source_original_full_complement_power_budget"])
    dup=F(nf403["source_strict_joint_dual_power_upper"])
    rl=F(nf404["original_selected_after_pole_shear_power_lower_exact"])
    rh=F(nf404["original_selected_after_pole_shear_power_upper_exact"])
    bulk_budget=gamma-dup-(rh-rl)-F(8,10**32)
    bulk_length=2*(B-DELTA)
    assert F("3.286e-26")<bulk_budget<F("3.288e-26")
    assert 0<bulk_budget/bulk_length<F(123,10**15)**2
    assert continuous_uniform_error_floor>34*F(123,10**15)
    assert jet["source_derivative_nonzero_certified"] is True
    assert all(row["derivative_jump_identity"]==
       ("+c_n*u4_prime(B)" if row["prime_power"] in (2,3)
        else "-c_n*u4_prime(B)") for row in coeff)
    output={
      "pass":"NF460",
      "standing":"ACCEPTED original bulk jump geometry and global H1/uniform-continuous method STOP; Tbulk upper OPEN",
      "source_sha256":SOURCE,"seams_sha256":GEOM,
      "jet_sha256":hjet,"principal_sha256":hprincipal,
      "NF404_sha256":h404,"NF459_sha256":h459,
      "original_244D_projection_smooth_at_every_seam":True,
      "original_residual_seven_positive_jump_order":list(order),
      "original_positive_bulk_cells":8,
      "original_two_sided_bulk_cells":16,
      "original_seam_amplitudes":out,
      "original_largest_jump_at_n":7,
      "original_max_jump_abs_strict_lower":"8.59e-12",
      "any_global_continuous_uniform_approx_error_strict_lower":"4.29e-12",
      "complete_original_bulk_h_in_global_H1":False,
      "bulk_T_sufficient_budget_approx":format(float(bulk_budget),".17e"),
      "bulk_T_allowable_RMS_below":"1.23e-13",
      "global_uniform_lower_vs_bulk_RMS_gate_factor_gt":34,
      "global_uniform_method_stop_NOT_L2_impossibility":True,
      "all_seven_derivative_contact_signs_source_replayed":True,
      "full_actual_bulk_T_upper":"OPEN",
      "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
      "next":"NF461 source-correlated segmented L2 energy of h; preserve seven signed jumps, true projector and original endpoint charge"}
    return output
if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--output")
    args=ap.parse_args()
    result=main();text=json.dumps(result,indent=2)+"\n"
    if args.output:
        q=Path(args.output);q.parent.mkdir(parents=True,exist_ok=True);q.write_text(text)
    print(text)
