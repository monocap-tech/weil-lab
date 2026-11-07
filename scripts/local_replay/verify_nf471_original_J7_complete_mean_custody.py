#!/usr/bin/env python3
"""NF471 EXACT RATIONAL custody replay of already source-native certified mean.

This is a receipt consistency check; actual original source computation is
the 4096-bit/6000-image scoped CI #42410633241, not this small validator.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
base=Path(__file__).resolve().parents[2]
fn=base/"notes/data/provisional/NF471_original_J7_complete_macroscopic_mean_custody.json"
nf470=base/"notes/data/provisional/NF470_original_J7_native_regular_mean_and_two_joint_points_custody.json"
r=json.loads(fn.read_text());s=json.loads(nf470.read_text())
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
assert (r["source_sha256"],r["seams_sha256"])==(SRC,SEAM)
assert (s["original_nf407_sha256"],s["original_nf406_sha256"])==(SRC,SEAM)
assert r["original_source_generators"]==246 and r["original_grouped_modes"]==273
assert r["arb_bits"]==4096 and r["source_linear_image_modes"]==6000
assert r["physical_panel"]==["26/25","53/50"] and F(r["panel_length"])==F(1,50)
assert r["verification"][-1]["status"]=="SUCCESS" and r["verification"][-1]["run_id"]==42410633241
assert r["independent_NF470_compact_source_center_overlap"]
def I(key):return tuple(map(F,r[key]))
jl,ju=I("original_joint_arch_mean_outward_coarsened")
fl,fu=I("original_six_prime_regular_mean_outward")
zl,zu=I("original_complete_z_mean_outward_coarsened")
assert (fl,fu)==tuple(map(F,s["original_finite_regular_mean_interval_decimal_outward"]))
assert jl<ju<0<fl<fu and 0<zl<zu
assert zl<=jl+fl<=ju+fu<=zu, "Outward re-coarsening must contain original arithmetic sum"
assert zu-zl<F(1,10**17)
cl,cu=I("original_joint_arch_center_x_21_20_outward_coarsened")
nl,nu=map(F,s["original_full_J7_points"]["21/20"]["joint_arch_decimal_outward"])
assert cl<=nu and nl<=cu
tail=F(100*10**160,6000)*F(3,8)**480
assert tail<F(1,10**40)
assert len(r["final_json_sha256"])==64 and len(r["final_zip_sha256"])==64
assert r["full_signed_J7_panel"]==r["nf466_covariance_variance"]==r["nf404"]=="OPEN"
assert r["W_ODD_NEG"]==r["RH"]=="OPEN"
print(json.dumps({"pass":"NF471","standing":"exact receipt-only replay",
"source_sha256":SRC,"original_joint_arch_mean_outward_coarsened":[str(jl),str(ju)],
"original_complete_z_mean_outward_coarsened":[str(zl),str(zu)],
"original_complete_mean_sign":"POSITIVE",
"source_native_full_CI":42410633241,
"whole_original_J7_signed":"OPEN",
"original_input_full_replay":"CI #42410633241, not this receipt-only checker"},indent=2))
