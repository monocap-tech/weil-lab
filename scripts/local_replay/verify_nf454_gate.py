#!/usr/bin/env python3
"""NF454 exact Fraction reduction, original source receipts; E78 still open."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
d=Path(__file__).resolve().parents[2]/"notes/data/provisional"
def load(n):
    b=(d/n).read_bytes()
    return json.loads(b),hashlib.sha256(b).hexdigest()
def I(v,scale="1"):
    a,b=F(v[0])*F(scale),F(v[1])*F(scale)
    assert a<=b
    return a,b
S="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
G="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
rows=[
("NF442_original_true_cell1_signed_source_custody_index.json","original_complete_true_signed_D1_conservative_interval_times_1e_minus24","1e-24"),
("NF443_original_true_cell2_complete_signed_custody_index.json","original_true_J2_signed_D2_interval_conservative_x_1e_minus23","1e-23"),
("NF437_original_true_cell3_signed_decision_custody_index.json","true_original_cell3_D3_4pz_plus_2z2_outward_decimal_conservative","1"),
("NF439_original_true_cell4_complete_signed_custody_index.json","original_true_J4_D4_signed_outward_conservative_times_1e_minus23","1e-23"),
("NF440_original_true_cell5_three_panel_full_signed_custody_index.json","original_true_J5_D5_signed_outward_decimal","1"),
("NF432_original_true_cell6_signed_decision_custody_index.json","original_true_J6_nonprincipal_signed_4pz_plus_2z2_outward_decimal_at_1e_minus44","1")]
a=[];receipt={}
for i,(fn,key,m) in enumerate(rows,1):
    j,h=load(fn)
    assert S in j.values() and G in j.values()
    a.append(I(j[key],m));receipt[str(i)]=h
assert all(v[0]>0 for v in a[:3]) and all(v[1]<0 for v in a[3:])
sl=sum((v[0] for v in a),F(0));su=sum((v[1] for v in a),F(0))
j,h=load("NF410_original_signed_taylor_moments.json")
assert j["original_nf406_source_sha256"]==G
pl,pu=I(j["original_known_principal_power_outward"]);receipt["NF410"]=h
j,h=load("NF404_original_selected_pole_shear_exact.json")
C=F(j["exact_sufficient_new_full_supported_centered_scalar_power_upper_target"])
assert C==F(j["original_selected_after_pole_shear_power_lower_exact"])+F(j["exact_source_original_full_complement_power_budget"])
receipt["NF404"]=h
j,h=load("NF453_original_J7_J8_principal_and_island_custody.json")
assert j["CI_status"]=="SUCCESS" and j["source_sha256"]==S and j["seams_sha256"]==G
assert j["D7_whole"]==j["D8_whole"]=="OPEN"
l7,u7=I(j["original_j7_ep"]);l8,u8=I(j["original_j8_ep"]);receipt["NF453"]=h
# Full original centered power = A + 2 E78, E78 integral of (p+z)^2 on positive J7+J8.
al=pl+sl-2*(u7+u8);au=pu+su-2*(l7+l8)
tl=(C-au)/2;tu=(C-al)/2
assert F("5.7e-22")<al<=au<F("5.8e-22")<C
assert F("2.59e-22")<tl<=tu<F("2.62e-22")
assert au+2*F("2.59e-22")<C<al+2*F("2.62e-22")
print(json.dumps({"pass":"NF454","standing":"Original source exact reduction; E78 unmeasured",
  "receipt_sha256":receipt,"six_signed":[float(sl),float(su)],
  "A":[float(al),float(au)],"E78_gate":[float(tl),float(tu)],
  "C":float(C),"guaranteed_pass_E78_le":"2.59e-22",
  "guaranteed_cap_failure_E78_ge":"2.62e-22","RH":"OPEN"},indent=2))
