#!/usr/bin/env python3
"""MG15: source-coordinate directional covariance error on original MG14 cells.

SCOPE: 24 ORIGINAL SI10 Fourier low-frequency panels, 23 actual
MG11 double-boundary-vanishing supported physical source functions
plus original sinh pole; both Ao and Ao² source moments.

MG14 uses -delta I <= T T^T - V V^T <= delta I for T=V+e.
MG15 retains actual separate pointwise source error radii
|e_i|<=r_i. By weighted Cauchy,
     e e^T <= D := (sum_i r_i) diag(r_i).
For any rational 0<tau<1, whole matrix Young gives
   (1-tau) V V^T - (1/tau-1) D <= T T^T
                                  <= (1+tau) V V^T+(1+1/tau)D.
On a symmetric cell V(t)=v+d*t, the COMPLETE true original source
reference integral is C=v v^T + h² d d^T/12. Thus
     2h*l*[(1-tau)C-(1/tau-1)D] <= M1cell
        <= 2h*u*[(1+tau)C+(1+1/tau)D];
with (l²,u²) for M2=Ao².

This is a genuinely anisotropic, coefficient-adapted *full Loewner*
bound on all 24x24 source crosses, NOT a diagonal approximation of
the true moment. Source phases, pole and original multiplier are
unchanged. Adaptive cellwise scalar/directional selection retains
complete paired lower and upper matrices. It does NOT infer a true
negative eigenvector or whole-operator theorem from lower inertia.

The final code independently regenerates/replays MG14 complete
24x24 affine baseline source moment matrices on identical cells,
then verifies exact rational 24D matrix inertia of all candidates.
No entire low band, Astar² pole correction, Galerkin residual,
full470 odd, even/Weil/CC27/RH certificate.
"""
import argparse,json
from fractions import Fraction as F
from validate_rpb108_mg14_affine_original_two_moments import (
 ROOT,N,PHYS,POLE,PIVOT,B,
 source_panel_run,transformed_affine,exact_affine_error,
 abs_cap,ORDERS, original_source_centered_windows,
 original_full_25_physical_interval_gram,
 protected_inner_cover,boundary_intervals,
 derivative_intervals_and_D3,interval_out,pair_coefficients,
 positive_gap,panel_windows,hyperbolic_interval,
 original_physical_source_lipschitz,
 original_full_second_derivative_upper,
 local_source_first_derivative_at_midpoint,
 original_exact_physical_fourier_midpoint,
 original_midpoint_derivative_intervals,
 original_third_spatial_moment,
 positive_cell_weight_interval,
 zero,sym,add_rank_one,add_policy_cell,
 finalize,down,up
)
from validate_rpb108_sm62_full25_338signed_positive import exact_inertia_general

TAUS=(F(1,64),F(1,32),F(1,16),F(1,8),F(1,4),F(1,2),F(3,4))
LABELS=tuple("tau_"+str(t.numerator)+"_"+str(t.denominator) for t in TAUS)

def matrix_sub(A,B):
 return [[A[i][j]-B[i][j] for j in range(len(A))] for i in range(len(A))]
def exact_directional_regression():
 """Exercise sharp interval-weighted Young on nonzero signed e."""
 from validate_rpb108_sm62_full25_338signed_positive import exact_inertia_general
 v=[F(3),F(-4),F(5)]
 radii=[F(1,8),F(1,16),F(1,32)]
 S=sum(radii,F(0))
 D=[S*z for z in radii]
 for e in ((radii[0],-radii[1],radii[2]),
           (-radii[0],radii[1],-radii[2]),
           (F(0),radii[1],F(0))):
  X=[v[i]+e[i] for i in range(3)]
  actual=[[X[i]*X[j] for j in range(3)] for i in range(3)]
  for tau in TAUS:
   low=[[(1-tau)*v[i]*v[j]-
         ((1/tau-1)*D[i] if i==j else 0)
         for j in range(3)] for i in range(3)]
   hi=[[(1+tau)*v[i]*v[j]+
        ((1+1/tau)*D[i] if i==j else 0)
        for j in range(3)] for i in range(3)]
   assert exact_inertia_general(matrix_sub(actual,low))[1]==0
   assert exact_inertia_general(matrix_sub(hi,actual))[1]==0
 return True

def add_directed_cell(matrices,policy,order,coeffs,width,
                      v,d,r,tau):
 l,u=coeffs
 assert 0<tau<1 and l>0 and l<=u
 lo,hi=matrices[policy][order]
 S=sum(r,F(0));diag=[S*x for x in r]
 h2=width*width/12
 lower_scale=2*width*l*(1-tau)
 upper_scale=2*width*u*(1+tau)
 add_rank_one(lo,v,lower_scale)
 add_rank_one(lo,d,lower_scale*h2)
 add_rank_one(hi,v,upper_scale)
 add_rank_one(hi,d,upper_scale*h2)
 for i in range(N):
  lo[i][i]-=2*width*l*(1/tau-1)*diag[i]
  hi[i][i]+=2*width*u*(1+1/tau)*diag[i]
 return diag

def lower_cell_trace(coeffs,width,v,d,r,tau):
 l,u=coeffs
 S=sum(r,F(0))
 Cv=sum((x*x for x in v),F(0))
 Cd=sum((x*x for x in d),F(0))
 return (2*width*l*((1-tau)*(Cv+width*width*Cd/12)
         -(1/tau-1)*S*S))

def full_measured_run():
 assert exact_directional_regression()
 mg14=source_panel_run()
 assert mg14["source_panel_cell_count"]==24
 assert mg14["total_coupled_source_channels"]==N
 assert mg14["exact_24D_lower_reference_spectral_classification_completed"]
 assert mg14["certified_method_comparison"]["one"]["affine_lower_reference_PSD_certified"] is False
 assert mg14["certified_method_comparison"]["two"]["affine_lower_reference_PSD_certified"] is False

 centers,sources,_=original_source_centered_windows()
 assert len(sources)==PHYS and sources[POLE][0]=="pole"
 H,phys,_=original_full_25_physical_interval_gram()
 assert phys==sources and len(H)==PHYS
 clusters,*_=protected_inner_cover()
 b=[interval_out(x) for x in boundary_intervals(sources,clusters)]
 boundary_d,_=derivative_intervals_and_D3(sources,clusters)
 free=tuple(i for i in range(PHYS) if i not in (PIVOT,POLE))
 determinant,a,c=pair_coefficients(b,boundary_d,PIVOT,free)
 assert positive_gap(determinant)>0
 panels,spans=panel_windows(centers,sources)
 hyp=(hyperbolic_interval(B/2,"sinh"),hyperbolic_interval(B/2,"cosh"))
 lips=original_physical_source_lipschitz(sources)
 Kglobal=original_full_second_derivative_upper(sources)
 Kthird=original_third_spatial_moment(sources)

 names=("scalar",)+LABELS+("directional_best","adaptive")
 mats={policy:{order:(zero(),zero()) for order in ORDERS}
       for policy in names}
 counts={order:{"scalar":0,"directional":0} for order in ORDERS}
 direction_choices={order:{name:0 for name in LABELS} for order in ORDERS}
 diagnostics=[]
 for left,right,region in panels:
  width=right-left;half=width/2;mid=(left+right)/2
  l,u,_=positive_cell_weight_interval(left,right)
  l=down(l);u=up(u)
  assert 0<l<=u
  vals=original_exact_physical_fourier_midpoint(mid,centers,sources,hyp)
  derivatives,second=original_midpoint_derivative_intervals(
     mid,centers,sources,hyp)
  K=[]
  for gb,sp,third in zip(Kglobal,second,Kthird):
   cap=abs_cap(sp)+third*half if sp is not None else gb
   K.append(min(gb,cap))
  v,d,r=transformed_affine(vals,derivatives,K,a,c,half)
  scalar_error,v2,d2,r2=exact_affine_error(v,d,r,half)
  candidate=[]
  for tau,name in zip(TAUS,LABELS):
   a1=lower_cell_trace((l,u),width,v,d,r,tau)
   candidate.append((a1,name,tau))
  _,best_name,best_tau=max(candidate,key=lambda x:(x[0],-TAUS.index(x[2])))
  trace_scalar={}
  for order in ORDERS:
   wl,wu=(l,u) if order=="one" else (l*l,u*u)
   trace_scalar[order]=2*width*wl*(
      v2+width*width*d2/12-N*scalar_error)
   add_policy_cell(mats,order,"scalar",v,d,scalar_error,width,wl,wu)
   for tau,name in zip(TAUS,LABELS):
    add_directed_cell(mats,name,order,(wl,wu),width,v,d,r,tau)
   add_directed_cell(mats,"directional_best",order,(wl,wu),width,
                     v,d,r,best_tau)
   trace_directional=lower_cell_trace((wl,wu),width,v,d,r,best_tau)
   chosen="directional" if trace_directional>trace_scalar[order] else "scalar"
   counts[order][chosen]+=1
   direction_choices[order][best_name]+=int(chosen=="directional")
   if chosen=="directional":
    add_directed_cell(mats,"adaptive",order,(wl,wu),width,v,d,r,best_tau)
   else:
    add_policy_cell(mats,order,"adaptive",v,d,scalar_error,width,wl,wu)
  diagnostics.append({
   "region":region,"cell_left":str(left),"cell_right":str(right),
   "source_radii_norm_sq":str(up(r2)),
   "source_radii_L1_squared":str(up(sum(r,F(0))**2)),
   "scalar_covariance_error":str(scalar_error),
   "trace_optimal_directional_tau":str(best_tau),
   "scalar_first_lower_trace_contribution":str(trace_scalar["one"]),
   "directional_first_lower_trace_contribution":str(
      lower_cell_trace((l,u),width,v,d,r,best_tau))
  })
 assert len(diagnostics)==24
 for order in ORDERS:
  assert sum(counts[order].values())==24
  assert sum(direction_choices[order].values())==counts[order]["directional"]
 all_results={}
 for name in names:
  sub={}
  for order in ORDERS:
   lower,upper,fee_l,fee_u=finalize(mats[name][order])
   inertia=exact_inertia_general(lower)
   assert sum(inertia)==N
   lo_trace=sum((lower[i][i] for i in range(N)),F(0))
   up_trace=sum((upper[i][i] for i in range(N)),F(0))
   sub[order]={
    "complete_24x24_lower":[[str(x) for x in row] for row in lower],
    "complete_24x24_upper":[[str(x) for x in row] for row in upper],
    "lower_trace":str(lo_trace),"upper_trace":str(up_trace),
    "lower_exact_inertia":{
       "positive":inertia[0],"negative":inertia[1],"zero":inertia[2]},
    "lower_export_fee":str(fee_l),"upper_export_fee":str(fee_u)
   }
  all_results[name]=sub

 # Compare full 576 rational entries to MG14, not only traces.
 for order in ORDERS:
  original=mg14["policies"]["affine"][order]
  new=all_results["scalar"][order]
  assert original["lower_trace"]==new["lower_trace"]
  assert original["upper_trace"]==new["upper_trace"]
  assert original["complete_24x24_lower"]==new["complete_24x24_lower"]
  assert original["complete_24x24_upper"]==new["complete_24x24_upper"]
 gain={}
 for order in ORDERS:
  original=all_results["scalar"][order]
  chosen=all_results["adaptive"][order]
  dirbest=all_results["directional_best"][order]
  gain[order]={
   "adaptive_lower_trace_minus_MG14":str(F(chosen["lower_trace"])-F(original["lower_trace"])),
   "directional_lower_trace_minus_MG14":str(F(dirbest["lower_trace"])-F(original["lower_trace"])),
   "adaptive_upper_trace_reduction":str(F(original["upper_trace"])-F(chosen["upper_trace"])),
   "MG14_original_lower_reference_exact_inertia":original["lower_exact_inertia"],
   "MG15_adaptive_lower_reference_exact_inertia":chosen["lower_exact_inertia"],
   "selected_directional_cells":counts[order]["directional"],
   "selected_scalar_cells":counts[order]["scalar"],
   "adaptive_true_lowband_PSD_certified":False
  }
  # Scoped actual source lower PSD accepted only via exact inertia,
  # which is *not* the actual operator's inertia.
  gain[order]["adaptive_lower_reference_strict_PSD"]=(
      chosen["lower_exact_inertia"]["negative"]==0
      and chosen["lower_exact_inertia"]["zero"]==0)
 return {
  "status":"SCOPED_EXACT_ORIGINAL_DIRECTIONAL_AFFINE_COVARIANCE_MOMENTS",
  "canonical_W_ODD_NEG":"OPEN",
  "MG14_verified_actions_run":39346488631,
  "original_physical_source_count":PHYS,
  "original_boundary_adapted_dimension":23,
  "original_sinh_pole_channel_included":True,
  "complete_physical_fourier_source_channels":N,
  "same_24_frequency_cells_as_MG14":True,
  "actual_selected_original_cell_count":len(panels),
  "all_576_mixed_source_terms_preserved":True,
  "exact_MG14_full_24x24_baseline_replayed":True,
  "full_per_source_affine_Taylor_radii_used":True,
  "directional_Young_positive_semidefinite_envelope_regression":True,
  "source_weighted_error_matrix":
    "D=(sum_i source_error_radius_i)*diag(source_error_radius_i)",
  "exact_directed_Loewner_family":
    "(1-tau)C-(1/tau-1)D <= TT^T <= (1+tau)C+(1+1/tau)D",
  "tau_candidates":[str(t) for t in TAUS],
  "adaptive_choice_counts":counts,
  "adaptive_directional_tau_choices":direction_choices,
  "per_cell_diagnostics":diagnostics,
  "candidate_matrices":all_results,
  "method_comparison":gain,
  "original_first_and_second_moments_scoped_only":True,
  "original_second_moment_Ao_squared_not_Astar_squared":True,
  "whole_0_to_cutoff_original_frequency_covered":False,
  "original_full23_Galerkin_residual_certified":False,
  "full_470_source_strong_inverse_and_odd_remainder":"OPEN",
  "even_Weil_CC27_RH":"OPEN",
  "independent_original_Fourier_closed_domain_audit":"OPEN",
  "decision":"Evaluate exact lower-reference inertia vs MG14. Continue only if useful; lower-reference negative eigenvalues are NOT original operator negative modes."
 }

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--output",default="artifacts/mg15_original_directional_affine_covariance.json")
 args=p.parse_args()
 data=full_measured_run()
 target=ROOT/args.output
 target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(json.dumps(data,indent=2)+"\n")
 print("MG15 original directional covariance result:",json.dumps({
   "sources":N,"cells":data["actual_selected_original_cell_count"],
   "method_comparison":data["method_comparison"],
   "candidate_lower_inertias":{
      name:{order:pair[order]["lower_exact_inertia"] for order in ORDERS}
      for name,pair in data["candidate_matrices"].items()},
   "selection":data["adaptive_choice_counts"],
   "original_470_odd_even_Weil_RH":"OPEN"
 }),flush=True)
if __name__=="__main__":
 main()
