#!/usr/bin/env python3
"""MG59: physically valid original 2D source-action moment projection BEFORE Young.

The accepted 41-cell original physical Fourier source strong action is
u_j(xi)=a(xi)*t_j(xi)-2*t_p(xi)*b_j in 23 adapted + true sinh pole 24D.

For a SOURCE COEFFICIENT vector z, project first:
 y_z(xi)=a(xi)*sum(z_j*t_j(xi))-2*t_p(xi)*sum(z_j*b_j).

Crucially, with t=v+s*d+e, the SAME source coordinate error e_p
must be counted as |ac*z_p-2*(z.bmid)|*r_p, and the SAME multiplier
delta_a shared across all j is bounded by |z.v|+half|z.d|
before absolute summation. This valid 2D action covariance lower
can be MUCH sharper than restriction of MG57's conservative full24
source lower. No promotion from 2D ray tests to global 24D Loewner.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
import validate_rpb108_mg32_joint_fourier_residual as ori
N=24;P=23
ANCHOR=(-3,0,-2,2,2,0,1,2,1,2,2,2,1,-2,-2,2,0,2,2,2,2,1,-3,-2)
ALT=(-33,-2,-23,21,22,2,11,23,14,24,24,15,11,-22,-25,22,2,21,22,25,25,14,-25,-23)
COORDS=(0,1,2,5,8,11,16,20,23)
def dot(a,b):return sum((Q(x)*Q(y) for x,y in zip(a,b)),Q(0))
def qf(v,A,w=None):
 if w is None:w=v
 return sum((Q(v[i])*Q(A[i][j])*Q(w[j]) for i in range(N) for j in range(N)),Q(0))
def accepted_original_41_source_cells(a57):
 old,*_=ori.exact_original_cells()
 assert len(old)==32
 new=[]
 for rec in a57["MG57_refined_true_physical_fourier_source_cells"]:
  new.append((Q(rec["left"]),Q(rec["right"]),
    Q(rec["multiplier_lower"]),Q(rec["multiplier_upper"]),
    [Q(z) for z in rec["source_midpoint"]],
    [Q(z) for z in rec["source_derivative"]],
    [Q(z) for z in rec["source_error"]]))
 assert len(new)==12
 result=[]
 for i,cell in enumerate(old):
  result.extend(new[(i-1)*4:i*4] if i in (1,2,3) else [cell])
 assert len(result)==41
 assert result[0][0]==0 and result[-1][1]==4
 assert all(result[i][1]==result[i+1][0] for i in range(40))
 return result
def project_one(z,cell,bmid,berr):
 left,right,wl,wu,v,d,r=cell
 h=(right-left)/2
 ac=(wl+wu)/2;da=(wu-wl)/2
 b=dot(z,bmid);e=sum((abs(Q(zi))*ei for zi,ei in zip(z,berr)),Q(0))
 tv=dot(z,v);td=dot(z,d)
 projected0=ac*tv-2*v[P]*b
 projectedd=ac*td-2*d[P]*b
 # SAME source e_p and scalar multiplier delta_a, before absolute vals.
 source_error=sum((abs(ac*Q(z[j])-(2*b if j==P else Q(0)))*r[j]
                   for j in range(N)),Q(0))
 scalar_error=da*(abs(tv)+h*abs(td)+sum((abs(Q(z[j]))*r[j]
                                      for j in range(N)),Q(0)))
 pole_coeff_error=2*e*(abs(v[P])+h*abs(d[P])+r[P])
 rho=source_error+scalar_error+pole_coeff_error
 assert rho>=0
 return projected0,projectedd,rho,source_error,scalar_error,pole_coeff_error
def twoD_moment(cells,z,w,bmid,berr):
 low=[[Q(0),Q(0)],[Q(0),Q(0)]]
 high=[[Q(0),Q(0)],[Q(0),Q(0)]]
 tau_counts={str(x):0 for x in ori.CHOSEN_TAUS}
 charges={"projected_source_remainder":Q(0),
          "common_multiplier_uncertainty":Q(0),
          "true_pole_column_error":Q(0)}
 totalsig=totalpen=Q(0)
 for cell in cells:
  left,right=cell[0],cell[1]
  width=right-left
  entries=[project_one(x,cell,bmid,berr) for x in (z,w)]
  v=[x[0] for x in entries];d=[x[1] for x in entries]
  r=[x[2] for x in entries]
  base=sum((x*x for x in v),Q(0))+width*width*sum((x*x for x in d),Q(0))/12
  rad=sum(r,Q(0))
  tau=max(ori.CHOSEN_TAUS,key=lambda t:(
     2*width*((1-t)*base-(1/t-1)*rad*rad),-t))
  assert Q(0)<tau<1
  tau_counts[str(tau)]+=1
  for i in range(2):
   for j in range(2):
    gram=v[i]*v[j]+width*width*d[i]*d[j]/12
    low[i][j]+=2*width*(1-tau)*gram
    high[i][j]+=2*width*(1+tau)*gram
   low[i][i]-=2*width*(1/tau-1)*rad*r[i]
   high[i][i]+=2*width*(1+1/tau)*rad*r[i]
  sig=2*width*(1-tau)*base
  penalty=2*width*(1/tau-1)*rad*rad
  totalsig+=sig;totalpen+=penalty
  for key,idx in (("projected_source_remainder",3),
                  ("common_multiplier_uncertainty",4),
                  ("true_pole_column_error",5)):
   charges[key]+=penalty*sum((x[idx] for x in entries),Q(0))/rad if rad else Q(0)
 assert low[0][1]==low[1][0] and high[0][1]==high[1][0]
 return low,high,totalsig,totalpen,charges,tau_counts
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--verified-mg24-json",required=True)
 p.add_argument("--verified-mg57-json",required=True)
 p.add_argument("--output",default="artifacts/mg59_original_projected_two_plane_action_moments.json")
 arg=p.parse_args()
 a24=json.loads((ROOT/arg.verified_mg24_json).read_text())
 a57=json.loads((ROOT/arg.verified_mg57_json).read_text())
 assert a24["canonical_W_ODD_NEG"]==a57["canonical_W_ODD_NEG"]=="OPEN"
 H,hr,err=original_H24_from_physical_source()
 assert err==Q(a24["physical_Gram_Loewner_row_error"])
 bmid=[H[j][P] for j in range(N)];berr=[hr[j][P] for j in range(N)]
 cells=accepted_original_41_source_cells(a57)
 L57=[[Q(z) for z in row] for row in a57["refined_original_true_strong_lower"]]
 assert qf(ANCHOR,L57)>0
 candidates=[("coordinate_"+str(i),tuple(int(j==i) for j in range(N)))
             for i in COORDS]+[("second_MG57_integer_ray",ALT)]
 reports=[]
 for name,other in candidates:
  low,upper,signal,penalty,charge,counts=twoD_moment(
       cells,ANCHOR,other,bmid,berr)
  a,b,c=low[0][0],low[0][1],low[1][1]
  det=a*c-b*b
  good=a>0 and c>0 and det>0
  norm1=dot(ANCHOR,ANCHOR);norm2=dot(other,other)
  assert norm1>0 and norm2>0
  # On source plane span(ANCHOR,other), exact coercivity constant.
  constant=det/((a+c)*(norm1+norm2)) if good else None
  if good:assert constant>0
  existing=[[qf(v,L57,w) for w in (ANCHOR,other)]
             for v in (ANCHOR,other)]
  reports.append({
    "second_vector_label":name,
    "first_original_integer_vector":[str(x) for x in ANCHOR],
    "second_original_integer_vector":[str(x) for x in other],
    "new_true_original_2D_projected_action_lower":[[str(x) for x in row] for row in low],
    "new_true_original_2D_projected_action_upper":[[str(x) for x in row] for row in upper],
    "old_MG57_full24_lower_restricted_to_same_2D_plane":[[str(x) for x in row] for row in existing],
    "exact_new_2D_gram_determinant":str(det),
    "exact_new_2D_strict_positive":good,
    "exact_2D_normalized_source_coercivity":str(constant) if good else None,
    "original_new_2D_affine_signal_trace":str(signal),
    "original_new_2D_source_error_charge_trace":str(penalty),
    "source_error_charge_provenance_diagnostic":{k:str(v) for k,v in charge.items()},
    "physical_source_cell_count":41,
    "source_2D_moment_is_valid_true_original_Fourier_pole_corrected":True,
    "no_global_24D_rank_two_Loewner_claim":True,
    "chosen_Young_parameter_counts":counts
   })
  print("MG59 ORIGINAL source pre-projected 2D",name,{
   "L00":float(a),"L11":float(c),"det_sign":int(det>0)-int(det<0),
   "2D_coercivity_certified":good},flush=True)
 positives=[x for x in reports if x["exact_new_2D_strict_positive"]]
 best=max(positives,key=lambda row:Q(row["exact_2D_normalized_source_coercivity"])) if positives else None
 result={
   "status":"ORIGINAL_MG59_TRUE_ACTION_PREPROJECTED_TWO_PLANE_LOEWER",
   "canonical_W_ODD_NEG":"OPEN",
   "accepted_source_archives":{"MG24":39378465438,"MG57":39897754515},
   "original_true_sinh_pole_action_and_signed_prime7_digamma":True,
   "original_23_adapted_plus_true_pole_source_24D_frame":True,
   "true_whole_frequency_Sstar_ge_projected_0to4_moment":True,
   "genuine_original_41_cell_source_measurements_not_new_Fourier_sampling":True,
   "source_remainder_and_multiplier_shared_scalar_combined_before_absolute":True,
   "full24_MG57_accepted_lower_positive_index":1,
   "tested_two_plane_count":len(reports),
   "strict_positive_original_2D_subspaces":len(positives),
   "selected_original_positive_2D_source_label":best["second_vector_label"] if best else None,
   "best_proved_2D_source_coercivity":best["exact_2D_normalized_source_coercivity"] if best else None,
   "no_full24_source_action_coercivity":True,
   "no_original_24D_source_residual_contraction":True,
   "no_original_470D_inverse":True,
   "no_signed_odd_51over56":True,
   "independent_original_Fourier_form_domain_audit":"OPEN",
   "even_Weil_CC27_RH":"OPEN",
   "candidates":reports}
 path=ROOT/arg.output;path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(result,indent=2)+"\n")
 print("MG59 ORIGINAL independent-of-MG58 true physical projected-two-plane candidate constructed",{
  "candidate_planes":len(reports),"strict_certified_planes":len(positives),
  "2D_success":bool(positives),"whole24_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
