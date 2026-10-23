#!/usr/bin/env python3
"""MG56 loss-census and NEGATIVE-DEFINITE strong lower classification.

Post-acceptance exact rational analysis of independently verified
MG56 genuine original strong-action 0–4 Loewner lower. A negative
definite *lower bound* is strictly dominated by the universally valid
S_* >= 0, and does NOT indicate a negative physical operator mode.

Audit the global MG15 Young radius-square charge, localization in
three actual original Fourier cells, and exact LDL sign of -L.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
N=24
def read(x):
 a=[[Q(z) for z in row] for row in x]
 assert len(a)==N and all(len(r)==N for r in a)
 return a
def symmetric(a):return all(a[i][j]==a[j][i] for i in range(N) for j in range(N))
def exact_positive_pivots(a):
 assert symmetric(a)
 m=[r[:] for r in a];p=[]
 for k in range(N):
  d=m[k][k]
  assert d>0,("not positive definite",k,str(d))
  p.append(d)
  for i in range(k+1,N):
   for j in range(i,N):
    m[i][j]-=m[k][i]*m[k][j]/d
    m[j][i]=m[i][j]
 return p
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--verified-mg56-json",required=True)
 p.add_argument("--output",default="artifacts/mg56_strong_lower_negative_definite_error_census.json")
 args=p.parse_args()
 a=json.loads((ROOT/args.verified_mg56_json).read_text())
 assert a["status"]=="ORIGINAL_MG56_POLE_CORRECTED_STRONG_ACTION_BAND_24D_LOWER"
 assert a["canonical_W_ODD_NEG"]=="OPEN"
 L=read(a["exact_band_lower"])
 assert symmetric(L) and all(L[i][i]<0 for i in range(N))
 pivots=exact_positive_pivots([[-z for z in row] for row in L])
 assert len(pivots)==24
 rows=[];signal=Q(0);penalty=Q(0)
 for i,cell in enumerate(a["cells_exact_rational"]):
  l=Q(cell["left"]);r=Q(cell["right"]);h=r-l
  t=Q(cell["tau"])
  v=[Q(x) for x in cell["strong_midpoint_source"]]
  d=[Q(x) for x in cell["strong_affine_slope"]]
  e=[Q(x) for x in cell["strong_error_radius"]]
  assert 0<h and 0<t<1 and all(x>=0 for x in e)
  sig=2*h*(1-t)*(sum((z*z for z in v),Q(0))
                  +h*h*sum((z*z for z in d),Q(0))/12)
  charge=2*h*(1/t-1)*sum(e,Q(0))**2
  signal+=sig;penalty+=charge
  rows.append((i,l,r,sig,charge))
 assert len(rows)==32
 assert [x[0] for x in rows if x[0] in (1,2,3)]==[1,2,3]
 assert all(rows[i][2]==rows[i+1][1] for i in range(31))
 exact_trace=sum((L[i][i] for i in range(N)),Q(0))
 assert exact_trace==Q(a["band_lower_trace"])
 # MG14 outward compaction makes certified L slightly LOWER than
 # the raw rational per-cell Young lower, never more optimistic.
 roundloss=(signal-penalty)-exact_trace
 assert 0<=roundloss<Q(1,1000)
 worst3=sum((rows[i][4] for i in (1,2,3)),Q(0))
 assert penalty>signal>0
 assert Q(3,4)<worst3/penalty<Q(4,5)
 assert rows[1][1]==Q(1,8) and rows[3][2]==Q(1,2)
 assert all(x["new_strong_band_lower_minus_MG24_lower_PSD"]
            for x in a["accepted_MG24_lower_comparisons"])
 output={
   "status":"MG56_INDEPENDENT_ACCEPTED_STRONG_BAND_EXACT_ERROR_LOSS_CLASSIFICATION",
   "accepted_original_MG56_run":39894269994,
   "true_original_pole_corrected_strong_lower":True,
   "whole_original_24D_new_band_lower_NEGATIVE_DEFINITE":True,
   "full24_exact_rational_negative_LDL_pivots":24,
   "zero_PSD_lower_strictly_dominates_this_certificate":True,
   "true_original_physical_strong_action_Sstar_still_PSD":True,
   "new_original_strong_action_negative_eigenmode_claim":False,
   "mg56_compacted_lower_trace":str(exact_trace),
   "original_full24_directional_affine_signal_trace":str(signal),
   "original_full24_directional_error_charge_trace":str(penalty),
   "outward_compaction_extra_trace_loss":str(roundloss),
   "strict_negative_pivot_count":len(pivots),
   "earliest_three_dominant_original_fourier_cell_indices":[1,2,3],
   "earliest_three_dominant_original_fourier_frequency":[str(rows[1][1]),str(rows[3][2])],
   "three_cell_total_exact_diagonal_Young_charge":str(worst3),
   "three_cell_share_of_total_Young_charge":str(worst3/penalty),
   "all_original_full24_MG24_lower_comparisons_loewner_improved":True,
   "no_original_24D_source_contraction":True,
   "no_original_470D_inverse":True,
   "no_signed_odd_51over56":True,
   "independent_original_Fourier_form_domain_audit":"OPEN",
   "even_Weil_CC27_RH":"OPEN"}
 path=ROOT/args.output;path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(output,indent=2)+"\n")
 print("MG56 STRONG ACTION LOSS CENSUS exact rational PASS",{
  "negative_definite_lower":True,
  "raw_signal_trace":float(signal),
  "raw_young_error_trace":float(penalty),
  "three_cell_error_share":float(worst3/penalty),
  "source_24D_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
