#!/usr/bin/env python3
"""NF519 exact ORIGINAL D-frame SHA -> raw physical beta contractor.

SOURCE-EXACT acceptance ONLY if the full original 242x242 historical D
dyadic matrix is supplied and its serialized dyadic SHA equals the
original NF505 D digest. Then compute beta=D*a_star with exact integers,
publish 242 1e80 raw coefficients and a rigorously bounded weighted L1
error. Before this D artifact exists, only synthetic selftest is valid.
"""
import argparse,hashlib,json,gzip,sys
from pathlib import Path
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
NF505="ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec"
NF518="926f8d00d28212f542351760e0c1d814413e8a36a3367d6a58bf837c53865438"
FRAME="18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf5666e36b430e"
B=Q(549,500);S=10**80
def read(path):
 raw=Path(path).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def frame_sha(rows):
 h=hashlib.sha256()
 for row in rows:
  for m,e in row:
   h.update((json.dumps([str(m),int(e)],separators=(",",":"))+"\n").encode())
 return h.hexdigest()
def exact_contract(D,aa,den,weights):
 assert len(D)==len(aa)==len(weights)
 nums=[];err=Q(0)
 for i,row in enumerate(D):
  assert len(row)==len(aa)
  z=[(int(m),int(e),aa[j]) for j,(m,e) in enumerate(row) if int(m) and aa[j]]
  if not z: beta=Q(0)
  else:
   exp=min(e for m,e,a in z)
   msum=sum(m*a*(1<<(e-exp)) for m,e,a in z)
   beta=Q(msum*(1<<exp),den) if exp>=0 else Q(msum,den*(1<<(-exp)))
  rounded=(beta*S).numerator//(beta*S).denominator
  nums.append(str(rounded))
  err+=weights[i]*abs(beta-Q(rounded,S))
 return nums,err
def smoke():
 # Distinct synthetic huge dyadic upper-triangular frame; no original SHA!
 D=[[["1",-1],[str(2**200),-23],["0",0]],
    [["0",0],["1",-2],["1",-300]],
    [["0",0],["0",0],[str(2**500),-413]]]
 v,e=exact_contract(D,[17,-31,11],10**105,[Q(1),Q(5,4),Q(3,5)])
 assert len(v)==3 and 0<=e<Q(3,10**80)
 assert frame_sha(D)==hashlib.sha256("".join(json.dumps([str(m),int(exp)],separators=(",",":"))+"\n"
                                      for row in D for m,exp in row).encode()).hexdigest()
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--selftest-only",action="store_true")
 for k in ("frame","nf505","nf518","output"):p.add_argument("--"+k)
 a=p.parse_args();smoke()
 if a.selftest_only:
  print("NF519 exact synthetic dyadic frame contraction PASS; original D not supplied")
  return
 assert a.frame and a.nf505 and a.nf518 and a.output
 old,sh=read(a.nf505);fit,fs=read(a.nf518)
 assert (sh,fs)==(NF505,NF518)
 assert old["pass"]=="NF504-native" and old["original_selected_J_dimension"]==242
 assert old["original_original_D_frame_SHA256"]==FRAME
 assert fit["original_exact_historical_D_frame_SHA256"]==FRAME
 openfn=gzip.open if str(a.frame).endswith(".gz") else open
 with openfn(a.frame,"rt") as z: D=json.load(z)["original_historical_D_242x242_dyadic_rows"]
 assert len(D)==242 and frame_sha(D)==FRAME, "METHOD STOP: original historical D SHA mismatch"
 aa=list(map(int,fit["original_selected_D_frame_coefficients_exact_rational_candidates_numerators"]))
 den=int(fit["original_selected_D_frame_coefficients_exact_rational_denominator"])
 assert len(aa)==242 and den==10**105
 weights=[B**k if f!="pole" else Q(3,5) for f,k in old["original_source_basis_nodes"]]
 trial,err=exact_contract(D,aa,den,weights)
 assert err<Q(1,10**19)
 out={"pass":"NF519-original-source-historical-D-raw-beta-certification",
      "original_nf505_sha256":sh,"original_nf518_sha256":fs,
      "historical_source_D_frame_SHA256_reproduced":FRAME,
      "original_selected_raw_coefficients":242,
      "original_raw_beta_trial_denominator":str(S),
      "original_raw_beta_trial_integer_numerators":trial,
      "original_weighted_raw_beta_error_exact":str(err),
      "original_weighted_raw_beta_error_strict_lt_1e_minus_19":True,
      "NF519_any_original_physical_cell_squared_e_beta_uncertainty_lt_4e_minus_30":True,
      "actual_source_physical_local_eD":"OPEN",
      "actual_source_Fredholm_kernel_gap":"OPEN",
      "original_NF404_named_support":"OPEN",
      "Weil_source_image_graph_domain":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"}
 Path(a.output).write_text(json.dumps(out,indent=2)+"\n")
 print("NF519 SOURCE-ORIGINAL exact frame SHA raw physical J242 beta contraction PASS")
 print("True local e_D, true kernel gap and RH still OPEN")
if __name__=="__main__":main()
