#!/usr/bin/env python3
"""NF456 exact original J242+2 genuine exterior witnesses reconciliation."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,runpy
root=Path(__file__).resolve().parents[2]
d=root/"notes/data/provisional"
def load(p):
    raw=(d/p).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
v=runpy.run_path(str(root/"scripts/local_replay/verify_nf455_projection_energy_floor.py"))
nf403,h403=load("NF403_original_joint_complement_power_exact.json")
joint,hjoint=load("NF389_original_joint_lower_exact_parent.json")
upper,hupper=load("NF389_original_two_ray_sharper_upper_exact.json")
nf404,h404=load("NF404_original_selected_pole_shear_exact.json")
assert nf403["original_nf389_joint_lower_report_sha256"]==hjoint
assert nf403["original_nf389_joint_upper_report_sha256"]==hupper
assert nf403["original_cutoff"]==2**24
assert joint["certified_physical_G_strictly_SPD"] is True
assert "n512,n513" in joint["original_orthogonality"]
assert upper["original_physical_and_signed_overlap_preflight_pass"] is True
assert upper["certified_whole_two_ray_fraction_strict_upper"]=="307/2000"
assert nf403["original_512_513_orthogonal_remainder_upper_computed"] is False
assert nf403["W_ODD_NEG"]==nf403["RH"]=="OPEN"
dlow=F(joint["certified_squared_dual_lower_best_rational_ray"])
assert dlow==F(nf403["source_strict_joint_dual_power_lower"])
dup=F(nf403["source_strict_joint_dual_power_upper"])
assert dup==F(307,2000)*F(joint["original_direction_four_squared_budget"])
Rlo,Rhi=v["Rlo"],v["Rhi"]
Alo,Ahi=v["a_lo"],v["a_hi"]
gamma2=v["budget"]
assert gamma2==F(nf403["source_sufficient_Jperp_full_action_power_budget"])
assert gamma2==F(nf404["exact_source_original_full_complement_power_budget"])
assert 0<dlow<dup<gamma2
assert dlow>F(35,100)*gamma2
assert dup<F(36,100)*gamma2
# Orthogonal source-native original physical decomposition:
# Efull = R + d12 + T = A + 2 E78.
# E=span(q512,q513) within J242-perp, T=||(Q-P_E)w||²>=0.
E78lower=(Rlo+dlow-Ahi)/2
assert E78lower>(Rlo-Ahi)/2
assert E78lower>F("2.59897e-22")
remaining_necessary=gamma2-dlow
remaining_sufficient=gamma2-dup-(Rhi-Rlo)
assert remaining_sufficient>0
assert F("3.28e-26")<remaining_sufficient<remaining_necessary<F("3.32e-26")
assert (Rhi-Rlo)<gamma2/F(10000)
assert gamma2-remaining_necessary==dlow
# No missing remainder bound is claimed, only the correct necessary/sufficient
# bounds that a future source-correlated original complementary calculation must meet.
out={
 "pass":"NF456",
 "standing":"Accepted source-native original two-witness contribution and sharpened J7/J8 physical energy lower; missing orthogonal remainder OPEN",
 "source_403_sha256":h403,"source_389_lower_sha256":hjoint,
 "source_389_upper_sha256":hupper,"source_404_sha256":h404,
 "original_exact_two_ray_dual_power":[str(dlow),str(dup)],
 "original_two_ray_lower_approx":format(float(dlow),".17e"),
 "original_two_ray_upper_approx":format(float(dup),".17e"),
 "original_J78_E_lower_approx":format(float(E78lower),".17e"),
 "original_full_budget_approx":format(float(gamma2),".17e"),
 "remaining_remainder_necessary_upper_approx":format(float(remaining_necessary),".17e"),
 "remaining_remainder_sufficient_upper_approx":format(float(remaining_sufficient),".17e"),
 "original_two_ray_budget_share":"strictly between 35% and 36%",
 "original_full_identity":"A+2E78=R+d12+T",
 "original_NF404_condition":"(R-Rlo)+d12+T <= gamma2",
 "actual_remainder_T_upper":"OPEN",
 "whole_E78_upper":"OPEN","NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"}
print(json.dumps(out,indent=2))
