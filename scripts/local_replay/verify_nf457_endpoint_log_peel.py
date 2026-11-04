#!/usr/bin/env python3
"""NF457: authentic J8 endpoint peel, conditional collar contract; T upper OPEN."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,runpy
root=Path(__file__).resolve().parents[2]
d=root/"notes/data/provisional"
def read(name):
    raw=(d/name).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
source,hs=read("NF407_original_fourth_physical_coefficients_native.json")
seams,hg=read("NF406_original_prime_support_partition_exact.json")
jet,hj=read("NF411_original_source_boundary_jet.json")
end,he=read("NF450_original_B_complete_Laplace_native_sign_custody_index.json")
coll,hc=read("NF451_original_J8_terminal_collar_custody_index.json")
nf404,h404=read("NF404_original_selected_pole_shear_exact.json")
nf403,h403=read("NF403_original_joint_complement_power_exact.json")
expected="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
geometry="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
assert hs==expected and hg==geometry
assert jet["nf407_source_sha256"]==expected
assert end["source_SHA256"]==coll["original_source_sha256"]==expected
assert end["seams_SHA256"]==coll["original_seams_sha256"]==geometry
assert source["original_dimension"]==242
assert jet["original_source_selected_count"]==242
assert jet["original_source_critical_count"]==4
assert nf404["original_dimension"]==242
assert nf404["original_selected_pole_index"]==241
assert end["complete_z_B_strictly_negative"] is True
assert coll["original_J8_seam_n9_strictly_before_collar"] is True
assert nf403["original_512_513_orthogonal_remainder_upper_computed"] is False
arb=runpy.run_path(str(root/"scripts/local_replay/verify_nf453_original_j7_j8_principal_energy_signed_island.py"))
vlo,vhi=arb["orig_arb_ball"](jet["original_original_source_value_at_B_arb"])
assert -F(117,10**13)<vlo<vhi<-F(116,10**13)<0
weights=jet["all_seven_original_prime_seam_derivative_identities"]
assert tuple(a["prime_power"] for a in weights)==(2,3,4,5,7,8,9)
c8lo=sum((F(a["c_n_positive_outward"][0]) for a in weights),F(0))
c8hi=sum((F(a["c_n_positive_outward"][1]) for a in weights),F(0))
assert F(7,2)<c8lo<c8hi<F(18,5)
zl,zu=map(F,end["complete_z_B_outward_24_decimal"])
assert -F(44,10**11)<zl<zu<0
B=F(11,10)
delta=F(coll["collar_width"])
assert delta==F(1,10**15)
mod=F(coll["collar_sup_absolute_z_difference_upper"])
assert mod<=F(374,10**13) # 3.74e-11
regular_unprojected=F(44,10**11)+mod+F(117,10**13)*F(18,5)
assert regular_unprojected<F(55,10**11) # |z+v*C8|<5.5e-10
# Nonzero log coefficient c=v/2 is analytically irremovable by bounded
# elements of authentic finite J242 + physical q512,q513. L2 remains finite.
cabs=F(117,2*10**13)
# e>8/3, so log(B/delta)<36 by exact integer rational comparison.
assert F(8,3)**36 > B/delta
log_primitive_bound=F(36**2+2*36+2)
# A *conditional* bound only: if sup_collar |P_(J+E)f|<=9e-9
# then |g|<=1e-8 and 2-side |c log +g|² is rigorously bounded.
projected_sup_ASSUMPTION=F(9,10**9)
M=F(1,10**8)
assert regular_unprojected+projected_sup_ASSUMPTION<M
collar_conditional=4*cabs*cabs*delta*log_primitive_bound+4*M*M*delta
assert collar_conditional<F(401,10**33) # 4.01e-31
gamma2=F(nf403["source_sufficient_Jperp_full_action_power_budget"])
dup=F(nf403["source_strict_joint_dual_power_upper"])
Rlo=F(nf404["original_selected_after_pole_shear_power_lower_exact"])
Rhi=F(nf404["original_selected_after_pole_shear_power_upper_exact"])
Tbudget=gamma2-dup-(Rhi-Rlo)
assert Tbudget>collar_conditional>0
# If the conditional collar hypothesis AND a verified bulk integral upper
# below Tbudget-collar_conditional hold, then NF404 sufficient gate passes.
# Neither condition is newly source-certified here.
out={"pass":"NF457","standing":"ACCEPTED original endpoint-log and unprojected regular collar bound; conditional residual collar contract; full T OPEN",
"source_sha256":hs,"geometry_sha256":hg,"jet_sha256":hj,"endpoint_sha256":he,"collar_sha256":hc,"nf404_sha256":h404,
"v_negative_nonzero":True,"original_endpoint_log_coefficient":"u4(B)/2",
"unprojected_original_regular_part_strict_abs_upper":"5.5e-10",
"selected_plus_two_exterior_dim":244,
"bounded_finite_basis_cannot_remove_log_endpoint":True,
"conditional_projected_collar_sup_required":"9e-9",
"conditional_two_sided_residual_collar_energy_upper":"4.01e-31",
"original_T_sufficient_budget_approx":format(float(Tbudget),".17e"),
"conditional_bulk_T_remaining_budget_approx":format(float(Tbudget-collar_conditional),".17e"),
"actual_projected_collar_sup_verified":False,"actual_bulk_residual_energy_verified":False,
"unmeasured_T_upper":"OPEN","NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"}
print(json.dumps(out,indent=2))
