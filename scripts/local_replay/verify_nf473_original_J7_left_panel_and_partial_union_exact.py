#!/usr/bin/env python3
"""NF473 independent exact-Fraction original J7 [1,26/25] signed and union audit.

Reads the authentic original 4096-bit original native JSON produced by
nf473_original_J7_left_macro_signed_native.py; does not substitute new
points or infer whole J7 from the certified partial union.
"""
from fractions import Fraction as F
from pathlib import Path
import json, argparse
HERE=Path(__file__).resolve().parents[2]
NF472=HERE/"notes/data/provisional/NF472_original_J7_macroscopic_signed_moments_custody.json"
NF470=HERE/"notes/data/provisional/NF470_original_J7_native_regular_mean_and_two_joint_points_custody.json"
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
def interval(vals):
    low,high=map(F,vals)
    assert low<=high
    return low,high
def sign(lo,hi):
    return "STRICT_NEGATIVE" if hi<0 else "STRICT_POSITIVE" if lo>0 else "UNDECIDED"
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--native",required=True)
    ap.add_argument("--nf472",default=str(NF472))
    ap.add_argument("--nf470",default=str(NF470))
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    a=json.loads(Path(args.native).read_text())
    o=json.loads(Path(args.nf472).read_text())
    q=json.loads(Path(args.nf470).read_text())
    assert a["pass"]=="NF473"
    assert (a["original_nf407_source_sha256"],a["original_nf406_seams_sha256"])==(SRC,SEAM)
    assert (o["original_nf407_sha256"],o["original_nf406_sha256"])==(SRC,SEAM)
    assert (q["original_nf407_sha256"],q["original_nf406_sha256"])==(SRC,SEAM)
    assert a["native_precision_bits"]==4096 and a["original_source_generators"]==246 and a["original_modes"]==273
    assert a["genuine_original_J7_panel"]==["1","26/25"] and a["original_six_regular_minus_prime_powers"]==[2,3,4,5,7,8]
    assert a["source_centered_Taylor_analytic_radius"]=="1/25"
    assert a["source_truncated_branch_Cauchy_M"]=="10^350"
    assert a["fixed_source_Chebyshev_or_Taylor_basis"].endswith("degree 1599")
    assert a["original_true_right_boundary_cross_check_NF470"]
    assert not a["original_true_mean_cross_check_NF471"]  # disjoint panel: no invented mean cross-check
    assert F(a["original_source_arb_coefficient_aggregate_width"])<F(1,10**40)
    assert F(a["original_source_Taylor_remainder"])<F(1,10**120)
    assert F(a["original_joint_image_real_tail"])<F(1,10**40)
    assert a["certified_sup_z_minus_polynomial"]=="1/10^28"
    pzlo,pzhi=interval(a["original_pz_normalized_mean_outward"])
    qlo,qhi=interval(a["original_z2_normalized_mean_outward"])
    dl,dh=interval(a["source_original_D_I_outward"])
    L=F(1,25)
    # Independent signed witness uses the separately certified source moments,
    # not the source-native DI sign flag. The bounds are allowed to be wider.
    directlo=L*(4*pzlo+2*qlo)
    directhi=L*(4*pzhi+2*qhi)
    assert directlo<=dh and directhi>=dl, "Original D interval and independent source moments must overlap"
    direct_sign=sign(directlo,directhi)
    native_sign=sign(dl,dh)
    assert native_sign == ("STRICT_"+a["source_original_D_I_strict_sign"] if a["source_original_D_I_strict_sign"] in ("NEGATIVE","POSITIVE") else "UNDECIDED")
    # Strict partial union: [1,26/25] from NF473 and [26/25,53/50] from
    # accepted independent original NF472. No gap or double-counted volume.
    rl,rh=interval(o["original_signed_D_I_outward_coarsened"])
    assert o["physical_panel"]==["26/25","53/50"] and rh<0
    total_lo=dl+rl
    total_hi=dh+rh
    out={
      "pass":"NF473",
      "standing":"exact-rational audit of source-certified true [1,26/25] J7 signed panel and contiguous partial J7 union",
      "original_nf407_sha256":SRC,"original_nf406_sha256":SEAM,
      "source_native_J7_left_interval":[str(dl),str(dh)],
      "independent_source_moment_direct_interval":[str(directlo),str(directhi)],
      "source_native_J7_left_sign":native_sign,
      "independent_source_moment_direct_sign":direct_sign,
      "source_normalized_pz_outward":[str(pzlo),str(pzhi)],
      "source_normalized_z2_outward":[str(qlo),str(qhi)],
      "NF470_original_right_boundary_overlap":True,
      "original_NF472_adjacent_signed_interval":[str(rl),str(rh)],
      "original_contiguous_partial_J7_union":["1","53/50"],
      "original_partial_union_signed_interval":[str(total_lo),str(total_hi)],
      "original_partial_union_sign":sign(total_lo,total_hi),
      "whole_original_J7":"OPEN","whole_original_J8":"OPEN",
      "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"}
    Path(args.output).write_text(json.dumps(out,indent=2)+"\n")
    print("NF473 independent genuine original J7 [1,26/25] sign",native_sign)
    print("NF473 independent mixed/quadratic moment sign",direct_sign)
    print("NF473 original contiguous [1,53/50] partial signed union",float(total_lo),float(total_hi),sign(total_lo,total_hi))
    print("NF473 whole J7/J8 NF404 W-ODD-NEG RH OPEN")
if __name__=="__main__":main()
