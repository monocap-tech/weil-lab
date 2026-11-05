#!/usr/bin/env python3
"""NF460 exact ORIGINAL source trial-function bulk residual acceptance contract."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
d=Path(__file__).resolve().parents[2]/"notes/data/provisional"
def read(n):
    raw=(d/n).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
rank,hr=read("parents/pr350_original_BS_pruned_rank_bound.json")
geo,hgeo=read("NF406_original_prime_support_partition_exact.json")
nf403,h403=read("NF403_original_joint_complement_power_exact.json")
nf404,h404=read("NF404_original_selected_pole_shear_exact.json")
nf459,h459=read("NF459_original_native_244D_terminal_K_custody.json")
nf457,h457=read("NF457_original_log_peel_info_ceiling_custody.json")
assert nf403["W_ODD_NEG"]==nf404["W_ODD_NEG"]=="OPEN"
assert nf459["original_rank_sha256"]==hr
assert nf404["original_rank_sha256"]==hr
assert nf459["original_nf406_seams_sha256"]==nf457["source_original_nf406_seams_sha256"]
assert geo["original_support_half_width"]=="11/10"
assert geo["number_of_open_physical_support_cells"]==16
assert len(geo["certified_ordered_knots"])==17
assert geo["certified_ordered_knots"][8]["label"]=="0"
assert [z["n"] for z in geo["original_prime_power_log_shifts"]]==[2,3,4,5,7,8,9]
assert nf459["original_whole_collar_K_strict_upper"]=="12996"
assert nf459["original_complete_two_sided_terminal_T_collar_power_strict_upper"]=="8e-32"
assert nf459["real_total_T_upper"]=="OPEN"
Rlo=F(nf404["original_selected_after_pole_shear_power_lower_exact"])
Rhi=F(nf404["original_selected_after_pole_shear_power_upper_exact"])
dl=F(nf403["source_strict_joint_dual_power_lower"])
du=F(nf403["source_strict_joint_dual_power_upper"])
gamma2=F(nf403["source_sufficient_Jperp_full_action_power_budget"])
assert gamma2==F(nf404["exact_source_original_full_complement_power_budget"])
norm_max=F(34,10**12)
assert Rhi+du<norm_max**2
delta=F(1,10**15)
assert delta==F(nf457["original_terminal_collar_delta"])
assert F(nf457["original_regular_plus_actual_prime_term_strict_uniform_bound"])==F(55,10**11)
assert F(nf459["original_whole_collar_K_strict_upper"])==114**2
# NF457 original f=(v/2)*log(B/d)+regular, |v|/2<117/(2*10^13),
# |regular|<5.5e-10. Exact log-square primitive and original oddness.
c=F(117,2*10**13)
reg=F(55,10**11)
L=36
f_collar_bound=4*delta*(c*c*(L*L+2*L+2)+reg*reg)
assert f_collar_bound<F(14,10**34)
# Any ORIGINAL trial g in V=J242+span(q512,q513) with ||g||<=3.4e-11
# has |g|<=114||g|| on both native endpoint collars, whence
# ||f-g||^2_collar <8e-32 (same exact source log integration).
trial_collar_bound=4*delta*(c*c*(L*L+2*L+2)+(reg+114*norm_max)**2)
assert trial_collar_bound<F(8,10**32)
charge=F(8,10**32)
cap=gamma2-du-(Rhi-Rlo)-charge
assert cap>0 and F("3.2868e-26")<cap<F("3.2870e-26")
# Orthogonality: Pi=P_V f; ||f||²=R+d12+T and
# T = min_(g in V)||f-g||².
# Source-certified cap: bulk ||f-g||²<=cap, ||g||<=norm_max.
bulk_f_lower=Rlo+dl-f_collar_bound
assert bulk_f_lower>F("3.309e-11")**2
assert cap<F("1.814e-13")**2
# Every successful original-norm-bounded trial must have
# ||g||_bulk>=||f||_bulk-sqrt(cap)>3.29e-11.
assert F("3.309e-11")-F("1.814e-13")>F("3.29e-11")
assert bulk_f_lower>30000*cap
# Bulk cosine necessary for a successful trial:
# cos(theta)>=1-cap/(2||f_bulk|| ||g_bulk||)>1-16e-6.
assert cap< F(16,10**6)*2*F("3.309e-11")*F("3.29e-11")
assert nf459["real_bulk_T_upper"]=="OPEN"
out={"pass":"NF460","standing":"ACCEPTED exact ORIGINAL 244D trial-function bulk sufficiency and necessary norm/correlation gates; actual bulk trial NOT produced",
"source_receipts":{"rank":hr,"support":hgeo,"nf403":h403,"nf404":h404,"nf457":h457,"nf459":h459},
"original_positive_bulk_cells":8,"all_original_seams":[2,3,4,5,7,8,9],
"original_physical_trial_space_dimension":244,
"trial_norm_upper":"3.4e-11",
"trial_collar_upper_proved_by_original_NF459_K_and_NF457_log":"8e-32",
"whole_original_f_unprojected_collar_upper":str(f_collar_bound),
"trial_bulk_L2_power_sufficient_upper":str(cap),
"trial_bulk_L2_power_sufficient_upper_approx":format(float(cap),".17e"),
"trial_bulk_L2_radius_sufficient_upper":"1.814e-13",
"necessary_successful_trial_full_norm_strictly_gt":"3.29e-11",
"necessary_successful_trial_bulk_correlation_cosine_gt":"0.999984",
"zero_trial_bulk_rejected_by_factor_gt":30000,
"exact_mathematical_reason":"T=min_(g in V)||f-g||²; bound entire trial terminal plus 8 original bulk cell residuals",
"actual_trial_coefficients_certified":False,"actual_bulk_integrated":False,
"actual_original_T_upper":"OPEN","NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"}
print(json.dumps(out,indent=2))
