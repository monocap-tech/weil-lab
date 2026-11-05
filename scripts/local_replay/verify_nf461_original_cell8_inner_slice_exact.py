#!/usr/bin/env python3
"""NF461 exact independent source/charge replay for the native 244D J8 slice."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2]
D=ROOT/"notes/data/provisional"
SOURCE="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAMS="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
RANK="9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2"
def load(name):
    raw=(D/name).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def main(native_path):
    source,hs=load("NF407_original_fourth_physical_coefficients_native.json")
    seams,hg=load("NF406_original_prime_support_partition_exact.json")
    nf451,h451=load("NF451_original_J8_terminal_collar_custody_index.json")
    nf450,h450=load("NF450_original_B_complete_Laplace_native_sign_custody_index.json")
    jet,hjet=load("NF411_original_source_boundary_jet.json")
    p,hp=load("NF407_original_prime_jump_log_power_exact.json")
    nf404,h404=load("NF404_original_selected_pole_shear_exact.json")
    nf403,h403=load("NF403_original_joint_complement_power_exact.json")
    nf459,h459=load("NF459_original_native_244D_terminal_K_custody.json")
    native=json.loads(native_path.read_text())
    assert hs==SOURCE and hg==SEAMS and nf459["original_rank_sha256"]==RANK
    assert jet["nf407_source_sha256"]==SOURCE
    assert nf451["original_source_sha256"]==nf450["source_SHA256"]==SOURCE
    assert nf451["original_seams_sha256"]==nf450["seams_SHA256"]==SEAMS
    assert p["source_all_original_prime_jumps_cancelled_from_z"] is True
    assert nf404["original_rank_sha256"]==RANK and nf404["original_dimension"]==242
    assert nf459["original_complete_two_sided_terminal_T_collar_power_strict_upper"]=="8e-32"
    assert nf451["analytic_modulus"]=="|z(B-d)-z(B)|<14000*d+600*d*log(2B/d)"
    assert nf451["original_J8_seam_n9_strictly_before_collar"] is True
    assert native["source_rank_sha256"]==RANK
    assert native["original_terminal_K_lt_12996"] is True
    assert native["NF461_outer_delta"]=="1e-13"
    assert native["NF461_whole_outer_K_lt_12996"] is True
    assert native["working_precision_bits"]==4096
    assert native["exterior_quotient_strict_SPD"] is True
    assert native["K_correlated_taylor_terms"]==72
    assert native["NF461_original_J8_two_sided_bulk_slice_upper_if_certified"]=="2.6e-29"
    B=F(11,10)
    inner=F(1,10**15)
    outer=F(1,10**13)
    assert 0<inner<outer<F(1,1000)
    assert F(8,3)**32>2*B/outer
    vlow,vhigh=map(F,p["original_source_u4_endpoint_interval"])
    assert -F(117,10**13)<vlow<=vhigh<0
    c8=sum(F(t["c_n_positive_outward"][1]) for t in jet["all_seven_original_prime_seam_derivative_identities"])
    assert c8<F(18,5)
    zl,zu=map(F,nf450["complete_z_B_outward_24_decimal"])
    assert -F(44,10**11)<zl<=zu<0
    modulus=outer*(F(14000)+F(600)*32)
    assert modulus==F(33200,10**13)
    Rhi=F(nf404["original_selected_after_pole_shear_power_upper_exact"])
    dUP=F(nf403["source_strict_joint_dual_power_upper"])
    Rlo=F(nf404["original_selected_after_pole_shear_power_lower_exact"])
    gamma2=F(nf403["source_sufficient_Jperp_full_action_power_budget"])
    assert Rhi+dUP<F(34,10**12)**2
    projection=F(114)*F(34,10**12)
    regular=F(117,10**13)*c8+F(44,10**11)+modulus+projection
    assert regular<F(8,10**9)
    actual_upper_formula=4*outer*(F(117,2*10**13)**2*(32**2+2*32+2)+F(8,10**9)**2)
    assert actual_upper_formula<F(26,10**30)
    budget=gamma2-dUP-(Rhi-Rlo)-F(26,10**30)
    assert F("3.284e-26")<budget<F("3.285e-26")
    result={
       "pass":"NF461",
       "standing":"ACCEPTED original J8 two-sided short bulk slice physical L2 upper; remaining bulk OPEN",
       "source_sha256":hs,"seams_sha256":hg,"original_rank_sha256":RANK,
       "nf451_sha256":h451,"nf450_sha256":h450,"nf411_sha256":hjet,
       "nf404_sha256":h404,"nf403_sha256":h403,"nf459_sha256":h459,
       "original_true_244D_K_outer_native":native["NF461_whole_outer_K_Arb"],
       "original_extended_outer_delta":"1e-13",
       "original_full_extended_two_sided_T_strict_upper":"2.6e-29",
       "original_bulk_slice_Bminus_1e13_to_Bminus_1e15_twosided_strict_upper":"2.6e-29",
       "actual_rational_two_sided_extended_power_formula":str(actual_upper_formula),
       "remaining_interior_bulk_T_sufficient_budget_approx":format(float(budget),".17e"),
       "remaining_original_J8_bulk":"OPEN","other_seven_cells_bulk":"OPEN",
       "full_T_upper":"OPEN","NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"}
    return result
if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--native",required=True)
    ap.add_argument("--output")
    args=ap.parse_args()
    out=main(Path(args.native))
    content=json.dumps(out,indent=2)+"\n"
    if args.output:
        f=Path(args.output);f.parent.mkdir(parents=True,exist_ok=True);f.write_text(content)
    print(content)
