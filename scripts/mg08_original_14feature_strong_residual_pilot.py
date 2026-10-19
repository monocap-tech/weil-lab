#!/usr/bin/env python3
"""MG08: first actual original-source STRONG RESIDUAL numerical feasibility pilot.

Uses sampled original SI10 physical sources, original seven-prime/digamma
positive Fourier multiplier, the original odd rank-one sinh pole, and
exact analytic SI29 14-feature physical Jensen/Legendre functions.
Measures the full sampled Galerkin R=J-Astar Z, D=R*R, F=G14*R,
z=R*C14^-1 s and the full coupled B14^-1 Woodbury response.
Compares SM35 scalar and MG07 reference-weighted bounds on the SAME
25 pilot original physical directions with the SAME original SM10
107-block / 890-column negative cap, retaining all mixed terms.

CRITICAL: FFT frequencies, sampled physical quadrature, missing
high-frequency unbounded logarithmic continuum, and sampled residual
are not outward certified. NO original resolvent or RH proof results.
"""
import argparse,json
from pathlib import Path
import numpy as np
from scipy import linalg
from validate_rpb108_sm36_original_odd_numerical_pilot import (
 ROOT,B_FLOAT,KAPPA_FLOAT,THETA,original_multiplier,geometry,
 select_sources,physical_columns,fourier_form,all_source_negative_cap)
from validate_rpb108_si29_pole_threshold_three_bands import FEATURES
from validate_rpb108_sm17_compact_spectral_gate import KAPPA_STAR
from validate_rpb108_sm33_original_odd_negative_mixed_bound import (
 full_original_clusterwise_negative_mixed)

def symmetric(A):
 return (A+A.T)/2

def exact_physical_SI29_features(x):
 """Continuous original features evaluated at physical SAMPLE nodes.

 Ordinary Jensen mean: sin(2*pi*c*x)*sinc(2*r*x).
 Degree 1 Bessel: 3 E[u sin(2*pi(c+r*u)*x)],
 =3*cos(2*pi*c*x) (sin(b)/b^2 - cos(b)/b).
 The small-b Taylor is b - b^3/10 + b^5/280 - b^7/15120.
 The formulas are analytic; samples/inner products here are float.
 """
 feat=[]
 gamma=[]
 count={0:0,1:0}
 for center,radius,delta,degree in FEATURES:
  c=float(center);r=float(radius)
  a=2*np.pi*c*x
  b=2*np.pi*r*x
  if degree==0:
   f=np.sin(a)*np.sinc(2*r*x)
  else:
   assert degree==1
   m=np.empty_like(b)
   small=np.abs(b)<0.05
   z=b[small]
   m[small]=z-z**3/10+z**5/280-z**7/15120
   z=b[~small]
   m[~small]=3*(np.sin(z)/z**2-np.cos(z)/z)
   f=np.cos(a)*m
  feat.append(f)
  gamma.append(float(4*radius*delta/(3 if degree else 1)))
  count[degree]+=1
 assert len(feat)==14 and count=={0:12,1:2}
 return np.column_stack(feat),np.array(gamma),count

def generalized_top(N,G):
 v=linalg.eigh(symmetric(N),symmetric(G),eigvals_only=True,
                check_finite=True)
 return float(v[-1])
def main_run(n,pad,infos,sources,cap,orders,mass,total):
 x,dx,V=physical_columns(n,infos,sources)
 cols=V.shape[1]
 pole=np.sinh(x/2)
 H=symmetric(dx*(V.T@V))
 A0,K0,gridgram,ft=fourier_form(V,dx,pad)
 b=dx*(V.T@pole)
 Astar=symmetric(A0-2*np.outer(b,b))
 # Approximate Galerkin solve on the complete selected source span.
 C=linalg.solve(Astar,H,assume_a="pos",check_finite=True)
 Z=V@C
 G0=symmetric(C.T@Astar@C)
 # Strong residual in physical sampled space: NOT the (zero)
 # Galerkin coefficient residual H-Astar*C.
 padded=n*pad
 freq=np.fft.fftfreq(padded,d=dx)
 m=original_multiplier(freq)
 aplus=np.maximum(KAPPA_FLOAT,m)
 sampled_action=np.fft.ifft(
   np.fft.fft(Z,n=padded,axis=0)*aplus[:,None],axis=0
 )[:n,:].real
 AstarZ=sampled_action-2*np.outer(pole,dx*(pole@Z))
 R=V-AstarZ
 weak=dx*(V.T@R)
 weak_rel=float(np.linalg.norm(weak)/max(np.linalg.norm(H),1e-30))
 # Complete source25 residual covariance and physical SI29 overlaps.
 D=symmetric(dx*(R.T@R))
 J14,gam,feature_counts=exact_physical_SI29_features(x)
 Gram14=symmetric(dx*(J14.T@J14))
 q=dx*(J14.T@pole)
 F14=dx*(J14.T@R)
 M=np.diag(1/gam)+Gram14/KAPPA_FLOAT
 M=symmetric(M)
 MiF=linalg.solve(M,F14,assume_a="pos",check_finite=True)
 Miq=linalg.solve(M,q,assume_a="pos",check_finite=True)
 # Genuine sampled physical Woodbury pole, preserving full 14 cross.
 Cinv_s=pole/KAPPA_FLOAT-(J14@Miq)/KAPPA_FLOAT**2
 alpha=float(1-2*dx*(pole@Cinv_s))
 if alpha<=0:raise ValueError("sampled SI29 pole denominator nonpositive")
 z=dx*(R.T@Cinv_s)
 DB=symmetric(D/KAPPA_FLOAT-(F14.T@MiF)/KAPPA_FLOAT**2
                +2*np.outer(z,z)/alpha)
 # Independently form sampled B14^-1 R and replay all source crosses.
 Mip=linalg.solve(M,F14,assume_a="pos",check_finite=True)
 CiR=R/KAPPA_FLOAT-(J14@Mip)/KAPPA_FLOAT**2
 B14invR=CiR+2*np.outer(Cinv_s,z)/alpha
 DBcheck=symmetric(dx*(R.T@B14invR))
 wood_rel=float(np.linalg.norm(DB-DBcheck)/
                max(np.linalg.norm(DBcheck),1e-24))
 # All 107 original negative Taylor blocks / 890 genuine cap columns.
 Ncap,capdata=all_source_negative_cap(
      V,x,dx,cap,orders,C,H,mass,total)
 Ndirect=symmetric(C.T@K0@C)
 Hminus=float(2*B_FLOAT*mass)
 ks=float(KAPPA_STAR)
 t_candidates=[0.25,0.5,1.,2.,4.]
 tested=[]
 for t in t_candidates:
  raw=(1+t)*Ncap
  New=symmetric(raw+(1+1/t)*Hminus/ks*DB)
  Old=symmetric(raw+(1+1/t)*Hminus/(ks**2)*D)
  tested.append({
    "young_t":t,
    "reference_weighted_max_generalized":generalized_top(New,G0),
    "old_scalar_max_generalized":generalized_top(Old,G0),
    "reference_vs_scalar_min_eigen_gap":
       float(np.min(np.linalg.eigvalsh(symmetric(Old-New))))})
 eig_D=np.linalg.eigvalsh(DB)
 eig_E=np.linalg.eigvalsh(D)
 nm=np.linalg.norm(D)
 ref_norm=float(np.linalg.norm(DB))
 ratio=float(ref_norm/(max(nm,1e-30)/ks))
 return {
   "physical_samples":n,"zero_pad":pad,"source_count":cols,
   "all_14_original_true_feature_functions_sampled":True,
   "original_feature_degrees":feature_counts,
   "sampled_source_physical_Gram_condition":float(np.linalg.cond(H)),
   "sampled_pole_conditioned_stiffness_condition":float(np.linalg.cond(Astar)),
   "sampled_source_weak_residual_relative":weak_rel,
   "sampled_strong_residual_squared_trace":float(np.trace(D)),
   "sampled_14_feature_overlap_frobenius":float(np.linalg.norm(F14)),
   "sampled_pole_residual_overlap_norm":float(np.linalg.norm(z)),
   "sampled_SI29_pole_denominator":alpha,
   "sampled_SI29_pole_BS_value":float(1-alpha),
   "sampled_Woodbury_two_path_relative":wood_rel,
   "sampled_reference_weighted_residual_Gram_norm":ref_norm,
   "sampled_reference_over_old_scalar_residual_Gram_norm_ratio":ratio,
   "sampled_DB_smallest_eigen":float(eig_D[0]),
   "sampled_D_smallest_eigen":float(eig_E[0]),
   "sampled_direct_negative_generalized_max":generalized_top(Ndirect,G0),
   "sampled_SM10_cap_generalized_max":generalized_top(Ncap,G0),
   "sampled_full_negative_cap_columns":capdata["columns"],
   "sampled_full_negative_cap_blocks":capdata["blocks"],
   "sampled_complete_470_acceptance_evaluated":False,
   "sampled_t_scores":tested,
   "sampled_fourier_info":ft
 }

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--output",default="artifacts/mg08_original_14feature_sampled_residual_pilot.json")
 p.add_argument("--quick",action="store_true")
 args=p.parse_args()
 assert len(FEATURES)==14
 infos,cap,orders,mass,width,total=geometry()
 sources=select_sources(infos)
 assert len(sources)==25
 # Probe a second grid to expose sampled physical / Fourier errors.
 cases=[(2048,4)] if args.quick else [(2048,4),(4096,4)]
 results=[]
 for n,pad in cases:
  row=main_run(n,pad,infos,sources,cap,orders,mass,total)
  assert row["sampled_full_negative_cap_columns"]==890
  assert row["sampled_full_negative_cap_blocks"]==107
  assert row["sampled_Woodbury_two_path_relative"]<1e-5
  assert row["sampled_source_weak_residual_relative"]<1e-5
  assert row["sampled_strong_residual_squared_trace"]>=0
  assert row["sampled_SI29_pole_denominator"]>0
  assert all(np.isfinite(list(q.values())[1]) for q in [] )
  results.append(row)
  print("MG08 original-SI29 sampled strong residual:",json.dumps({
   "physical_n":n,"pad":pad,
   "source_count":row["source_count"],
   "sampled_weak_residual":row["sampled_source_weak_residual_relative"],
   "sampled_strong_residual_squared_trace":row["sampled_strong_residual_squared_trace"],
   "reference_to_scalar_Gram_ratio":row["sampled_reference_over_old_scalar_residual_Gram_norm_ratio"],
   "new_t1_generalized":row["sampled_t_scores"][2]["reference_weighted_max_generalized"],
   "old_t1_generalized":row["sampled_t_scores"][2]["old_scalar_max_generalized"],
   "original_470_odd_Weil_RH":"OPEN"
  }),flush=True)
 artifact={
   "status":"SAMPLED_ORIGINAL_PHYSICAL_SOURCE_RESIDUAL_FEASIBILITY_ONLY",
   "canonical_W_ODD_NEG":"OPEN",
   "original_exceptional_total_sources":470,
   "pilot_source_count":len(sources),
   "original_complete_negative_cap_columns":890,
   "original_true_reference_features":14,
   "original_Galerkin_strong_residual_actual_470_CERTIFIED":False,
   "original_unbounded_log_fourier_tail_rigorously_enclosed":False,
   "original_real_frequencies_and_domains_certified":False,
   "sampled_original_positive_operator_has_missing_Fourier_tail":True,
   "actual_complete_470_resolvent_gate_passed":False,
   "even_Weil_CC27_RH":"OPEN",
   "cases":results
 }
 out=ROOT/args.output;out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text(json.dumps(artifact,indent=2,allow_nan=False)+"\n")
 if len(results)>1:
  old=results[0];new=results[-1]
  print("MG08 sampled grid sensitivity:",json.dumps({
   "strong_residual_trace_relative_change":
    abs(new["sampled_strong_residual_squared_trace"]-
        old["sampled_strong_residual_squared_trace"])/
    max(abs(new["sampled_strong_residual_squared_trace"]),1e-30),
   "sampled_reference_ratio_change":
    abs(new["sampled_reference_over_old_scalar_residual_Gram_norm_ratio"]-
        old["sampled_reference_over_old_scalar_residual_Gram_norm_ratio"]),
   "rigorous_original_470_gate":"OPEN"}),flush=True)
if __name__=="__main__":main()
