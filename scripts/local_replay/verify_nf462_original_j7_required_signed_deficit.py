#!/usr/bin/env python3
"""NF462 exact original signed J7 necessity and projector-elimination gate.

No new signed continuous D7/D8 integral is inferred here. Replays the
accepted original NF454/NF456 source-pinned Fraction certificates.
"""
from fractions import Fraction as F
from pathlib import Path
import runpy,json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2]
D=ROOT/"notes/data/provisional"
def read(name):
    raw=(D/name).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
v=runpy.run_path(str(ROOT/"scripts/local_replay/verify_nf454_gate.py"))
nf403,h403=read("NF403_original_joint_complement_power_exact.json")
nf404,h404=read("NF404_original_selected_pole_shear_exact.json")
nf453,h453=read("NF453_original_J7_J8_principal_and_island_custody.json")
nf456,h456=read("NF456_original_J242_two_ray_residual_custody.json")
nf461,h461=read("NF461_original_cell8_inner_bulk_energy_custody.json")
S="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
G="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
assert nf453["source_sha256"]==nf456["original_source_nf407_sha256"]==S
assert nf453["seams_sha256"]==nf461["source_nf406_seams_sha256"]==G
assert nf456["source_403_sha256"]==h403 and nf456["source_404_sha256"]==h404
assert nf461["original_nf407_source_sha256"]==S if "original_nf407_source_sha256" in nf461 else nf461["source_nf407_sha256"]==S
assert nf453["D7_whole"]==nf453["D8_whole"]=="OPEN"
assert nf456["NF404"]==nf461["nf404"]=="OPEN"
sl,su=v["sl"],v["su"]
pl,pu=v["pl"],v["pu"]
e7lo,e7hi=v["l7"],v["u7"]
e8lo,e8hi=v["l8"],v["u8"]
Klo,Khi=pl+sl,pu+su
C=v["C"]
Rlo=F(nf404["original_selected_after_pole_shear_power_lower_exact"])
Rhi=F(nf404["original_selected_after_pole_shear_power_upper_exact"])
gamma=F(nf404["exact_source_original_full_complement_power_budget"])
dlow=F(nf403["source_strict_joint_dual_power_lower"])
dup=F(nf403["source_strict_joint_dual_power_upper"])
assert C==Rlo+gamma
assert 0<dlow<dup<gamma
assert 0<e7lo<=e7hi and 0<e8lo<=e8hi
assert 0<Klo<=Khi
# ORIGINAL positive half cell signed D_j = 4 int pz + 2 int z²
# = 2(E_j - Ep_j), E_j=int(p+z)²>=0.
# Thus full J8 D8 >= -2 Ep8 >= -2 e8hi.
d8lower=-2*e8hi
# For original full physical centered energy:
# Efull=K+D7+D8, K=Ep+sum_j=1^6 D_j.
# So Efull<=C implies D7 <= C-K-D8.
# K>=Klo and D8>=d8lower entail the necessary full J7 gate:
j7_necessary=C-Klo-d8lower
d78_sufficient=C-Khi
d78_failure=C-Klo
# The original two-witness projection also imposes
# Efull>=Rlo+dlow, i.e. D78>=Rlo+dlow-Khi.
d78_floor=Rlo+dlow-Khi
assert d78_floor<d78_sufficient<d78_failure
assert d78_sufficient-d78_floor==gamma-dlow
assert d78_failure-d78_sufficient==Khi-Klo
assert j7_necessary< -F("2e-22")
assert d8lower<0
# Total original whole J8 physical squared E8 is unmeasured,
# and there is NO signed upper on D8.
assert "2.6e-29"==nf461["actual_extended_two_sided_power_strict_upper"]
def fmt(x):return format(float(x),".17e")
out={
 "pass":"NF462",
 "standing":"SOURCE-EXACT original J8 signed floor and necessary J7 negative deficit; full D7/D8 integral OPEN",
 "original_source_nf407_sha256":S,"original_seams_nf406_sha256":G,
 "source_receipts":{"NF403":h403,"NF404":h404,"NF453":h453,"NF456":h456,"NF461":h461,
                    "NF454_sources":v["receipt"]},
 "original_full_identity":"Efull=K+D7+D8=R+d12+T, K=Ep+sum(D1..D6)",
 "original_J8_D8_floor_identity":"D8=2(E8-Ep8)>=-2 Ep8",
 "original_J8_D8_strict_lower_approx":fmt(d8lower),
 "original_J7_necessary_negative_deficit_if_NF404_cap_approx":fmt(j7_necessary),
 "original_J7_negative_deficit_strictly_more_than":"2e-22",
 "original_J7_necessary_is_conditional":True,
 "original_K_interval_approx":[fmt(Klo),fmt(Khi)],
 "original_K_width_approx":fmt(Khi-Klo),
 "original_K_width_over_gamma_approx":fmt((Khi-Klo)/gamma),
 "original_D7_plus_D8_sufficient_gate_approx":fmt(d78_sufficient),
 "original_D7_plus_D8_cap_failure_gate_approx":fmt(d78_failure),
 "original_D7_plus_D8_true_projection_floor_approx":fmt(d78_floor),
 "original_correlated_same_K_floor_to_gate_gap":fmt(gamma-dlow),
 "original_J7_D7_whole_measured":False,"original_J8_D8_whole_measured":False,
 "new_original_J8_D8_upper_computed":False,
 "original_NF404_cap_decided":False,
 "old_NF461_real_small_J8_physical_residual_power_remains":True,
 "accepted_mathematical_route":"prioritize whole source-correlated J7 signed D7 and coupled J8, not another 244D bulk projector quadrature",
 "W_ODD_NEG":"OPEN","RH":"OPEN"}
print(json.dumps(out,indent=2))
if __name__=="__main__":
 ap=argparse.ArgumentParser()
 ap.add_argument("--output")
 args=ap.parse_args()
 if args.output:
    q=Path(args.output);q.parent.mkdir(parents=True,exist_ok=True)
    q.write_text(json.dumps(out,indent=2)+"\n")
