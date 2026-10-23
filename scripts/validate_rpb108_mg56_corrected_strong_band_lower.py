#!/usr/bin/env python3
"""MG56 — new original pole-corrected strong-action moment source lower.

Use accepted *physical* MG29 original 24D Fourier cells on [0,4] and
the original MG24 pole-column interval b=F^*s. The genuine original
A_* = A_o - 2|s><s| strong-action SOURCE Fourier response is

  u_j(xi)=a_o(xi) t_j(xi) - 2 t_p(xi) b_j.

On each real-frequency cell, a_o is ONE scalar with midpoint ac,
radius da; t=v+s d+e, |e_i|<=r_i. The exact affine source midpoint
and derivative are u0=ac*v-2*v_p*bmid and
u1=ac*d-2*d_p*bmid. Bound remaining error independently by
 |ac|r_j + da(|v_j|+half|d_j|+r_j)
 +2|bmid_j|r_p+2 brad_j(|v_p|+half|d_p|+r_p).
Using MG15's independently accepted exact-directional Young/affine
quadratic lower produces a genuine 24D band lower for the ACTUAL
pole-corrected all-frequency strong moment S_*=(A_*F)^*(A_*F):

   S_* >= S_[0,4] >= L_[0,4]   in Loewner order.

No claim L_[0,4]>0 is made without exact rational classification.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import (
    original_H24_from_physical_source,deserialize)
from validate_rpb108_mg25_robust_source_aware_residual import (
    Id,T,plus,sub,mul,psd,gersh_lower)
from validate_rpb108_mg41_ideal_cross_error_feasibility import classify_ideal
import validate_rpb108_mg32_joint_fourier_residual as m32
N=24;P=23
def enc(a):return [[str(x) for x in row] for row in a]
def mat(a):
 a=deserialize(a)
 assert len(a)==N and all(len(r)==N for r in a)
 return a
def tr(a):return sum((a[i][i] for i in range(N)),Q(0))
def qf(v,a):return sum((v[i]*a[i][j]*v[j] for i in range(N) for j in range(N)),Q(0))
def direct_original_strong_action_band(cells,bmid,brad):
 output={"strong":{"mass":(m32.zero(),m32.zero())}}
 taus={str(t):0 for t in m32.CHOSEN_TAUS}
 outcells=[];error=Q(0)
 for left,right,wl,wu,v,d,r in cells:
  assert Q(0)<=left<right<=Q(4)
  width=right-left;half=width/2
  assert wl>0 and wl<=wu
  ac=(wl+wu)/2;da=(wu-wl)/2
  c=[ac*v[j]-2*v[P]*bmid[j] for j in range(N)]
  slope=[ac*d[j]-2*d[P]*bmid[j] for j in range(N)]
  pole_amplitude=abs(v[P])+half*abs(d[P])+r[P]
  rad=[
    abs(ac)*r[j]
    +da*(abs(v[j])+half*abs(d[j])+r[j])
    +2*abs(bmid[j])*r[P]
    +2*brad[j]*pole_amplitude
    for j in range(N)]
  assert len(c)==len(slope)==len(rad)==N
  assert all(z>=0 for z in rad)
  # Per cell select the best EXACT rational lower trace from a
  # previously fixed finite Young grid, no test-ray tuning.
  tau=max(m32.CHOSEN_TAUS,key=lambda t:(
     m32.lower_cell_trace((Q(1),Q(1)),width,c,slope,rad,t),-t))
  assert Q(0)<tau<Q(1)
  taus[str(tau)]+=1
  m32.add_directed_cell(output,"strong","mass",(Q(1),Q(1)),
                         width,c,slope,rad,tau)
  error+=sum(rad,Q(0))
  outcells.append({
   "left":str(left),"right":str(right),"multiplier_lower":str(wl),
   "multiplier_upper":str(wu),"tau":str(tau),
   "strong_midpoint_source":[str(z) for z in c],
   "strong_affine_slope":[str(z) for z in slope],
   "strong_error_radius":[str(z) for z in rad]})
 L,U,_,_=m32.finalize(output["strong"]["mass"])
 assert L==T(L) and U==T(U) and psd(sub(U,L))
 assert psd(U)
 return L,U,taus,error,outcells
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--verified-mg24-json",required=True)
 p.add_argument("--verified-mg29-json",required=True)
 p.add_argument("--output",default="artifacts/mg56_original_corrected_strong_band_lower.json")
 args=p.parse_args()
 a24=json.loads((ROOT/args.verified_mg24_json).read_text())
 a29=json.loads((ROOT/args.verified_mg29_json).read_text())
 assert a24["status"]=="ORIGINAL_COMPLETE_FREQUENCY_24CHANNEL_COUPLED_SOURCE_MATRIX_ENCLOSURES"
 assert a29["status"]=="ORIGINAL_ADAPTED_THIRD_FOURIER_SOURCE_MOMENT_REFINEMENT"
 assert a24["canonical_W_ODD_NEG"]==a29["canonical_W_ODD_NEG"]=="OPEN"
 assert a29["verified_MG24_run_id"]==39378465438
 hm,hr,he=original_H24_from_physical_source()
 assert he==Q(a24["physical_Gram_Loewner_row_error"])
 bmid=[hm[i][P] for i in range(N)]
 brad=[hr[i][P] for i in range(N)]
 assert [str(z) for z in bmid]==a24["original_pole_b_center"]
 assert [str(z) for z in brad]==a24["original_pole_b_radii"]
 cells,HClo,HCup,rad29,cell_taus=m32.exact_original_cells()
 assert len(cells)==32 and cells[0][0]==0 and cells[-1][1]==4
 assert rad29==Q(next(z for z in a29["meshes"]
                      if z["mesh_cells"]==32)["total_source_radius_MG29"])
 L,U,taus,error,details=direct_original_strong_action_band(
    cells,bmid,brad)
 # Actual whole source action S_* is PSD and S_*>= this physical
 # positive frequency [0,4] strong moment, so the new L is a valid
 # ORIGINAL full-frequency 24D Loewner lower even if L is indefinite.
 kind,wit=classify_ideal(L)
 assert kind in ("NEGATIVE_EXACT_RATIONAL_RAYLEIGH",
                 "POSITIVE_EXACT_RATIONAL_LDL","INCONCLUSIVE")
 if kind=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH":
  w=[Q(x) for x in wit["rational_vector"]]
  assert qf(w,L)==Q(wit["exact_negative_quadratic"])<0
 # Certified scalar positivity on each fixed rational coordinate
 # requires merely L_jj>0, regardless of other full24 directions.
 coordinates=[i for i in range(N) if L[i][i]>0]
 comparisons=[]
 for k in (12,16):
  Lstar=mat(next(z for z in a24["cases"]
                 if z["cutoff_k"]==k)["complete_Sstar_lower"])
  assert Lstar==T(Lstar) and psd(mul(-1,Lstar))
  delta=sub(L,Lstar)
  comparisons.append({
   "cutoff_k":k,
   "old_full_original_MG24_lower_is_negative_semidefinite":True,
   "new_strong_band_lower_minus_MG24_lower_PSD":psd(delta),
   "strict_positive_diagonal_directions_old":sum(Lstar[i][i]>0 for i in range(N)),
   "strict_positive_diagonal_directions_new":len(coordinates),
   "old_lower_trace":str(tr(Lstar)),
   "new_lower_trace":str(tr(L))
  })
 out={
  "status":"ORIGINAL_MG56_POLE_CORRECTED_STRONG_ACTION_BAND_24D_LOWER",
  "canonical_W_ODD_NEG":"OPEN",
  "accepted_inputs":{"MG24":39378465438,"MG29":39440914565},
  "original_same_SI10_MG11_23adapted_plus_true_sinh_pole":True,
  "genuine_original_ao_minus_2_pole_action_not_unpoled_surrogate":True,
  "original_seven_prime_digamma_multiplier":True,
  "original_real_frequency_band_positive_mirror":["0","4"],
  "source_cells":32,
  "new_Fourier_data":False,
  "all_original_high_frequencies_covered_by_positive_remaining_strong_moment":True,
  "true_original_full_frequency_Sstar_ge_new_band_L_in_Loewner":True,
  "original_true_full_strong_moment_PSD":True,
  "mg29_physical_source_radius_sum":str(rad29),
  "mg56_corrected_action_source_radius_sum":str(error),
  "exact_band_lower":enc(L),
  "exact_band_upper":enc(U),
  "band_lower_trace":str(tr(L)),
  "band_upper_trace":str(tr(U)),
  "band_lower_gersh":str(gersh_lower(L)),
  "band_lower_inertia":kind,
  "band_lower_inertia_witness":wit,
  "positive_coordinate_indices":coordinates,
  "positive_coordinate_count":len(coordinates),
  "all_24_coordinate_lower_values":[str(L[i][i]) for i in range(N)],
  "original_strong_full24_positive_definite":kind=="POSITIVE_EXACT_RATIONAL_LDL",
  "strong_band_young_counts":taus,
  "accepted_MG24_lower_comparisons":comparisons,
  "cells_exact_rational":details,
  "original_source_contraction":False,
  "original_470D_inverse":False,
  "signed_odd_51over56_cap":False,
  "independent_original_Fourier_form_domain_audit":"OPEN",
  "even_Weil_CC27_RH":"OPEN"}
 dst=ROOT/args.output;dst.parent.mkdir(parents=True,exist_ok=True)
 dst.write_text(json.dumps(out,indent=2)+"\n")
 print("MG56 ORIGINAL corrected strong-action band [0,4]",{
  "trace":float(tr(L)),"Gersh":float(gersh_lower(L)),
  "strictly_positive_coordinate_directions":len(coordinates),
  "full24_positive":out["original_strong_full24_positive_definite"],
  "old_MG24_NSDS_lower":True,"470D_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
