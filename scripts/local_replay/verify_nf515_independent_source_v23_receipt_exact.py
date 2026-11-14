#!/usr/bin/env python3
"""NF515 independent Fraction acceptance of original selected-v23 bridge.

Re-checks strict exterior-source sign, original pole-shear algebra,
NF514 witness norm, original NF505 projection power, and the 0.48%-0.5%
rank-one fraction WITHOUT trusting rounded display comparisons.
Does not independently reintegrate the original 400 H/U coefficients.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
M401="644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515"
NF494="39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181"
NF505="ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec"
SEED="39a8679197447975f54629a04c9608659e47aadf61dffb6e5dea11d0df2dc6b0"
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
def read(p):
 b=Path(p).read_bytes()
 return json.loads(b),hashlib.sha256(b).hexdigest()
def iv(v):
 a,b=map(F,v);assert a<=b
 return a,b
def overlap(a,b):return max(a[0],b[0])<=min(a[1],b[1])
def main():
 p=argparse.ArgumentParser()
 for x in ("native","nf505","nf514","output"):p.add_argument("--"+x,required=True)
 o=p.parse_args()
 a,sha=read(o.native);old,oldsha=read(o.nf505);w,wsha=read(o.nf514)
 assert a["pass"]=="NF515-authentic-original-source-selected-v23-exterior-moment-exact"
 assert oldsha==NF505 and old["pass"]=="NF504-native"
 assert w["pass"]=="NF514-authentic-original-selected-23D-subspace-leverage-lower-exact"
 assert a["NF401_original_source_SHA256"]==M401
 assert a["NF494_original_source_SHA256"]==NF494
 assert a["NF505_original_source_SHA256"]==oldsha
 assert a["NF514_selected_witness_SHA256"]==w["witness_seed_SHA256"]==SEED
 assert a["source_nf407_sha256"]==old["source_original_NF407_sha256"]==SRC
 assert a["source_nf406_sha256"]==old["source_original_NF406_sha256"]==SEAM
 a0=F(6677356497477490213,4611686018427387904)
 pre=iv(a["original_global_I_pre_shear_selected_witness_moment"])
 pole=iv(a["original_global_I_sinh_pole_selected_witness_moment"])
 centered=iv(a["original_global_I_centered_W_selected_witness_moment"])
 collar=iv(a["original_terminal_two_collar_W_selected_witness_moment"])
 exterior=iv(a["original_exterior_O_centered_W_selected_witness_moment"])
 assert overlap(centered,(pre[0]-a0*pole[1],pre[1]-a0*pole[0]))
 assert centered[1]>=centered[0]
 assert overlap(exterior,(centered[0]-collar[1],centered[1]-collar[0]))
 assert exterior[1]>=exterior[0]
 assert exterior[0]<=exterior[1]<0
 norm=iv(a["original_witness_norm_squared_on_O"])
 oldnorm=iv(w["witness_full_original_O_L2_squared_outward"])
 assert overlap(norm,oldnorm) and norm[0]>0
 P=iv(a["original_exterior_complete_J242_projection_power"])
 oldP=iv(old["original_original_W_exterior_selected_projection_power_outward"])
 assert overlap(P,oldP) and P[0]>0
 c=iv(a["original_rank_one_v23_projection_power_on_O"])
 frac=iv(a["original_rank_one_fraction_of_complete_selected_projection_power"])
 inferred=(exterior[1]**2/norm[1],exterior[0]**2/norm[0])
 assert overlap(c,inferred)
 implied=(c[0]/P[1],c[1]/P[0])
 assert overlap(frac,implied)
 assert F(48,10000)<frac[0]<=frac[1]<F(1,200)
 edge=F(a["rank_one_global_fit_power_on_edge_H4094_union_H4095_lower"])
 assert 0<edge<=F(2,5)*c[1]
 assert edge>F(14,10**25)
 assert old["original_support_saturated_physical_Hilbert_gate"]=="CERTIFIED_PHYSICAL_SUPPORT_NO_GO"
 assert a["original_complete_J242_globally_fitted_local_eH"]=="OPEN"
 assert a["original_named_NF404_physical_gate"]=="OPEN"
 assert a["Weil_source_image_graph_domain"]==a["W_ODD_NEG"]==a["RH"]=="OPEN"
 result={
 "pass":"NF515-independent-exact-source-witness-receipt-audit",
 "standing":"Independent original SHA, pole shear/source subtraction and rational rank-one energy acceptance; no second original H400/U400 source reintegration",
 "source_original_nf515_receipt_sha256":sha,
 "source_nf514_selected_witness_sha256":SEED,
 "source_nf505_full_selected_sha256":NF505,
 "authentic_original_selected_witness_exterior_moment":list(map(str,exterior)),
 "source_original_rank_one_selected_projection_power":list(map(str,c)),
 "source_fraction_of_full_original_selected_projection_power":list(map(str,frac)),
 "selected_witness_fraction_strict_between_0p0048_and_0p005":True,
 "original_true_edge_rank_one_selected_energy_lower":str(edge),
 "original_globally_fitted_J242_local_residual":"OPEN",
 "original_NF404_named_physical_gate":"OPEN",
 "Weil_source_image_graph_domain":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"
 }
 Path(o.output).write_text(json.dumps(result,indent=2)+"\n")
 print("NF515 independent Fraction source bridge acceptance PASS")
 print("source actual exterior <W,v23>",float(exterior[0]),float(exterior[1]))
 print("v23 original projection fraction",float(frac[0]),float(frac[1]))
 print("Full 242D globally fitted local e_H, Weil domain and RH OPEN")
if __name__=="__main__":main()
