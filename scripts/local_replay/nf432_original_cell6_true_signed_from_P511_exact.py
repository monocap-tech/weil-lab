#!/usr/bin/env python3
"""NF432: exact original true-cell6 signed pz, z² from sourcewise P511 tail.

Never accept a negative partial polynomial alone. This requires the
source-exact NF432 true-z vs finite P511 uniform bound AND the immutable
original NF428/29/31 source-coefficient, p-moment, raw dx-moment and
signed P511 partial certificates.
"""
import argparse,hashlib,json,zipfile
from pathlib import Path
from fractions import Fraction as F

HASHES={
 "low":"d4e812d685813f8711aa4dce6422df27c301789cc23e944094c518e2f9247c3c",
 "high":"10c93ca7f4b7779334fd686ef1fd348f79fe873068af3897c2a936487dbdcbf8",
 "p":"bc7c98e1ac16b1147eaff91f11a6bf33ce4326d6237b5728c1987cec39f8cf25",
 "j":"8f83c9658dec776b84f9d013eb22d7ed1533a02e464ba975553c76210435e1d1",
 "partial":"e04a0bc019128509afd0d6e0a37b8da9b6c397ac5260854d03f7862c3bb70418"
}
def load(path,expected=None):
 raw=Path(path).read_bytes()
 if zipfile.is_zipfile(path):
  with zipfile.ZipFile(path) as z:
   names=[n for n in z.namelist() if n.endswith(".json")]
   assert len(names)==1
   raw=z.read(names[0])
 sha=hashlib.sha256(raw).hexdigest()
 if expected:assert sha==expected,(str(path),sha,expected)
 return json.loads(raw),sha
def ball(pair):
 x,y=map(F,pair)
 assert x<=y
 return x,y
def widen(pair,err):
 a,b=ball(pair)
 return a-err,b+err
def out(pair):return list(map(str,pair))
def main():
 ap=argparse.ArgumentParser()
 for key in ("low","high","p","j","partial","tail"):
  ap.add_argument("--"+key,required=True)
 ap.add_argument("--output",required=True)
 a=ap.parse_args()
 d={}
 for key in ("low","high","p","j","partial"):
  d[key],_=load(getattr(a,key),HASHES[key])
 d["tail"],tail_sha=load(a.tail)
 l=d["low"];h=d["high"];p=d["p"];j=d["j"];partial=d["partial"];t=d["tail"]
 assert l["pass"]==p["pass"]=="NF428"
 assert h["pass"]==partial["pass"]=="NF431"
 assert j["pass"]=="NF429" and t["pass"]=="NF432"
 src=l["source_sha256"];seams=l["seams_sha256"]
 assert src==h["source_sha256"]==p["nf407_original_full_source_sha256"]==j["nf407_original_source_sha256"]==partial["source_sha256"]==t["original_nf407_full_source_sha256"]
 assert seams==h["seams_sha256"]==p["nf406_original_seams_sha256"]==j["nf406_original_seams_sha256"]==partial["seams_sha256"]==t["original_nf406_seams_sha256"]
 assert l["original_true_cell6"]==h["original_true_cell6"]==p["original_x_domain"]==j["original_actual_log7_log8_cell6"]==t["original_true_cell6"]
 assert t["original_post_seam_primes"]==l["original_all_five_post_seam_primes_retained"]==h["original_all_five_post_seam_primes_retained"]==[2,3,4,5,7]
 assert t["original_neither_primes"]==l["original_two_neither_branches"]==h["original_two_neither_branches"]==[8,9]
 assert t["original_source_generators"]==l["original_four_selected_plus_critical_count"]==h["original_four_selected_plus_critical_count"]==246
 assert t["original_NF404_center"]==l["original_exact_NF404_dyadic_center"]==h["original_exact_NF404_dyadic_center"]
 assert all(x["W_ODD_NEG"]==x["RH"]=="OPEN" for x in d.values())
 assert t["true_source_high_Chebyshev_tail_starts_at_n"]==512
 assert partial["original_partial_z_modes"]==512 and partial["original_missing_z_modes"]==753
 assert not partial["actual_original_cell6_integral_certified"]
 assert p["all_1500_source_signed_chebyshev_moments_certified"]
 assert len(j["original_cell6_raw_Chebyshev_dx_moments_n0_to_n2998"])==2999
 coeff=l["coefficients"]+h["coefficients"]
 assert [x["n"] for x in coeff]==list(range(512))
 c=[ball(x["true_original_cell6_fixed_branch_coefficient_outward_interval"]) for x in coeff]
 assert all(y-x<F(1,10**25) for x,y in c)
 pmax=sum((max(abs(x),abs(y)) for x,y in c),F(0))
 p0=ball(p["original_signed_p_chebyshev_moments_n0_to_n1499"][0])
 assert p0[1]<0
 length=ball(j["original_cell6_raw_Chebyshev_dx_moments_n0_to_n2998"][0])
 assert F(0)<length[0]<length[1]<F(1,7)
 eps=F(t["original_true_z_vs_original_P511_uniform_error_exact_rational_upper"])
 assert F(0)<eps<F(1,10**20)
 # On this specific original support cell p(x)<0, so int|p|=-m0.
 # For z=P511+r, |r|<=eps, original pz and z² differences:
 # |int p*r|<=eps*(-p0.lower)
 # |int(2 P511*r+r²)|<=|J6|*(2 eps sum|a_n|+eps²).
 pzfee=eps*(-p0[0])
 z2fee=length[1]*(2*eps*pmax+eps**2)
 orig_pz=widen(partial["original_P511_pz_outward_interval"],pzfee)
 orig_z2=widen(partial["original_P511_squared_outward_interval"],z2fee)
 signedfee=4*pzfee+2*z2fee
 signed=widen(partial["original_P511_nonprincipal_signed_2z2_plus_4pz_outward_interval"],signedfee)
 # Same signed enclosure can independently be constructed from pz/z².
 assert 4*orig_pz[0]+2*orig_z2[0]<=signed[1]
 assert 4*orig_pz[1]+2*orig_z2[1]>=signed[0]
 assert orig_z2[0]>0
 assert orig_pz[1]<0
 assert signed[1]<0,("original true cell6 signed sign NOT certified",float(signed[1]))
 assert signed[1]-signed[0]<F(1,10**21)
 outdata={
  "pass":"NF432",
  "standing":"COMPLETE TRUE ORIGINAL PHYSICAL CELL6 SIGNED pz AND z² RIGOROUSLY CERTIFIED NEGATIVE NONPRINCIPAL CONTRIBUTION; WHOLE NF410/NF404 OPEN",
  "original_nf407_source_sha256":src,
  "original_nf406_seams_sha256":seams,
  "source_artifact_json_sha256":HASHES,
  "sourcewise_uniform_tail_json_sha256":tail_sha,
  "original_true_cell6":"(log(7)-11/10,log(8)-11/10)",
  "original_active_prime_power_branches":[2,3,4,5,7],
  "original_inactive_prime_power_branches":[8,9],
  "original_P511_interval_polynomial_modes":512,
  "original_high_modes_n512_to_infinity_bounded_without_individual_certificates":True,
  "source_exact_true_z_minus_P511_uniform_error_rational_upper":str(eps),
  "original_P511_sup_bound_from_absolute_source_coefficients":str(pmax),
  "original_true_cell6_length_outward":out(length),
  "original_true_cell6_signed_p_integral_outward":out(p0),
  "sourcewise_original_pz_error_fee":str(pzfee),
  "sourcewise_original_z2_error_fee":str(z2fee),
  "sourcewise_original_2z2_4pz_error_fee":str(signedfee),
  "true_original_cell6_pz_outward_interval":out(orig_pz),
  "true_original_cell6_z2_outward_interval":out(orig_z2),
  "true_original_cell6_nonprincipal_signed_2z2_plus_4pz_outward_interval":out(signed),
  "true_original_cell6_nonprincipal_signed_contribution_strict_negative":True,
  "true_original_cell6_signed_integrals_decision_quality":True,
  "original_remaining_seven_cell_signed_integrals_complete":False,
  "original_NF410_NF404_whole_signed_scalar_accepted":False,
  "original_fourth_J242_exterior_upper":False,
  "W_ODD_NEG":"OPEN","RH":"OPEN"
 }
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(outdata,indent=2)+"\n")
 print("NF432 PASS true ORIGINAL complete cell6 signed nonprincipal <0, whole NF410/NF404 OPEN")
 print("tail epsilon",float(eps),"signed",float(signed[0]),float(signed[1]),"total error",float(signedfee))
if __name__=="__main__":
 main()
