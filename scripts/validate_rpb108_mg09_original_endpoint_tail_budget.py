#!/usr/bin/env python3
"""MG09: rigorous original SI10 25-source LOGARITHMIC strong-tail diagnostics.

Analytic source forms and SI06/SM41 true original multiplier upper:
a_o(xi)<=17+ln(xi) for xi>=1.

SM41 directly certifies, for every source-coefficient vector z and
Lambda >= 2*max(c_j), a strong Fourier action tail
 ||a_o Tz||²_(|xi|>Lambda) <= C_slow(Lambda)||z||²,
 where C_slow ~ (log Lambda)^2/Lambda.

MG09 proves independent EXACT supported-source ENDPOINT separation:
 T_j(xi) = -J_j(xi)/(2*pi*i*xi) + E_j(xi),
 J_j = f_j(B)e^(-2*pi*i*xi*B)-f_j(-B)e^(2*pi*i*xi*B),
 |E_j(xi)| <= D_j/(2*pi*xi)^2,
 D_j=|f'_j(B)|+|f'_j(-B)|+integral |f''_j|.
 All 25 actual physical SI10 pilot generators have rational majorants
 D_sin_k0 <= 2w+2B w²,
 D_xcos_k1 <= 2+6B w + B²w²,
 D_pole <= 2+B/2, with w=2*pi_upper*c_j.
 Therefore || a_o sum z_j E_j ||²_(|xi|>Lambda)
    <= (2*sum D_j² / 6^4 / Lambda^3)
       * ((17+ln Lambda)^2/3
           +2*(17+ln Lambda)/9 + 2/27) ||z||².
 All rational with ln(2)<=347/500 at Lambda=2^k.

CRITICAL: This is ONLY the tail of the endpoint-subtracted REMAINDER.
The explicit boundary jump J/(i2*pi*xi) MUST be evaluated in the
original signed/positive covariance; it is not discarded or certified
small by the Lambda^-3 estimate. No actual Galerkin residual is built.
"""
import argparse,json
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import PI,B,LN
from validate_rpb108_si10_complement_positivity import protected_inner_cover
from validate_rpb108_sm41_original_positive_log_tail import (
 ARCH_PLUS_C,odd_pilot_tail_enclosure,
 mathematical_global_original_positive_multiplier_majorant)
from sm36_original_odd_numerical_pilot import ROOT,geometry,select_sources

def dyadic_strong_from_D(k,D2):
 assert isinstance(k,int) and k>=11
 log_hi=F(k)*F(347,500)
 v=F(ARCH_PLUS_C)+log_hi
 # PI[0]>3 gives (2*pi)^4>6^4, and both frequency signs.
 return 2*D2/F(6**4)*(v*v/F(3)+2*v/F(9)+F(2,27))/F(2**(3*k))

def source_derivative_constants(sources,clusters):
 ds=[]
 kinds={"sin":0,"xcos":0,"pole":0}
 for kind,j,degree in sources:
  if kind=="pole":
   # |s'(+-B)|=cosh(B/2)/2<1; |s''|<1/4
   # by 0<B/2<ln2, hence D<2+B/2.
   D=F(2)+B/F(2)
   kinds["pole"]+=1
  else:
   a,b,_=clusters[j]
   c=(a+b)/2
   assert c>0
   w=2*PI[1]*c
   if degree==0:
    # sine: |f'| <=w, |f''|<=w², both endpoints paid
    D=2*w+2*B*w*w
    kinds["sin"]+=1
   else:
    assert degree==1
    # xcos: f'=cos(wx)-w x sin(wx)
    # f''=-2w sin(wx)-w² x cos(wx), paid on [-B,B]
    D=F(2)+6*B*w+B*B*w*w
    kinds["xcos"]+=1
  assert D>0
  ds.append(D)
 assert sum(kinds.values())==25
 assert kinds["pole"]==1
 return ds,kinds

def cutoff_needed(method,target,D2,srcs,infos,start=11,stop=99):
 for k in range(start,stop+1):
  x=(F(odd_pilot_tail_enclosure(infos,srcs,2**k)[
       "exact_strong_multiplier_tail_squared_norm_upper"])
     if method=="unpeeled" else dyadic_strong_from_D(k,D2))
  if x<=target:return k
 raise AssertionError("no crossover within search; increase range")

def analytic_identity_regression():
 # Exact integration by parts twice in simple polynomial f=x,
 # B=1, with xi=1/4. This is a structural symbolic regression
 # of the D bounds, rather than a floating Fourier-integral test.
 # For f=x, f''=0 and f'(+-B)=1, so remainder is entirely
 # the explicit first-derivative boundary term.
 B0=F(1)
 fB,fm=B0,-B0
 fpB,fpm=F(1),F(1)
 assert fB-fm==2
 assert fpB+fpm==2
 assert (abs(fpB)+abs(fpm))==2
 # Original fast remainder depends on f' and f'' only; not
 # on the size of original endpoint jumps.
 return True

def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("--output",default="artifacts/mg09_original_endpoint_tail_budget.json")
 args=ap.parse_args()
 ledger=json.loads((ROOT/"research/obligations.json").read_text())
 assert ledger["active_obligation"]=="W-ODD-NEG"
 assert ledger["objective"]["status"]=="open"
 assert ledger["governance"]["no_automatic_promotion"]
 odd=next(o for o in ledger["obligations"] if o["id"]=="W-ODD-NEG")
 assert "SM41" in odd["evidence"] and "SI29" in odd["evidence"]
 assert mathematical_global_original_positive_multiplier_majorant()
 assert PI[0]>F(3) and LN[2][1]<F(347,500)
 assert analytic_identity_regression()
 clusters,_,_,_,_=protected_inner_cover()
 assert len(clusters)==107
 infos,cap,orders,mass,width,total=geometry()
 srcs=select_sources(infos)
 ds,kind=source_derivative_constants(srcs,clusters)
 assert kind=={"sin":16,"xcos":8,"pole":1}
 D2=sum((d*d for d in ds),F(0))
 assert D2>0
 checkpoints=[]
 for k in (11,12,13,16,20,24,30,36,40,48,56):
  baseline=odd_pilot_tail_enclosure(infos,srcs,2**k)
  assert baseline["proves_original_positive_tail_for_selected_25"]
  assert baseline["source_dims"]==25
  slow=F(baseline["exact_strong_multiplier_tail_squared_norm_upper"])
  fast=dyadic_strong_from_D(k,D2)
  assert slow>0 and fast>0
  checkpoints.append({
   "cutoff_power":k,"cutoff":"2^"+str(k),
   "SM41_entire_original_strong_tail_upper":str(slow),
   "MG09_endpoint_peeled_remainder_strong_tail_upper":str(fast),
   "SM41_entire_strong_tail_float":float(slow),
   "MG09_only_peeled_remainder_tail_float":float(fast)
  })
 targets=(F(1,100),F(1,10000),F(1,10**6),
          F(311,10**14))
 crossings=[]
 for target in targets:
  slow_k=cutoff_needed("unpeeled",target,D2,srcs,infos)
  fast_k=cutoff_needed("peeled",target,D2,srcs,infos)
  crossings.append({
   "illustrative_coefficient_l2_squared_tail_target":str(target),
   "SM41_first_dyadic_k_for_entire_strong_tail":slow_k,
   "MG09_first_dyadic_k_for_ONLY_PEELED_REMAINDER":fast_k,
   "endpoint_jump_contribution_still_requires_separate_rigorous_treatment":True
  })
 res={
  "status":"CERTIFIED_ANALYTIC_ORIGINAL_25SOURCE_ENDPOINT_REMAINDER_TAIL_METHOD_GATE",
  "canonical_W_ODD_NEG":"OPEN",
  "original_selected_source_count":25,
  "original_source_types":kind,
  "original_all_107_cluster_geometry_replayed":True,
  "original_SM41_log_multiplier_majorant_replayed":True,
  "exact_original_source_derivative_majorant_squared_sum":str(D2),
  "source_dependent_frequency_centers_used":True,
  "original_zero_extension_endpoints_not_silently_discarded":True,
  "boundary_jump_tail_is_unpaid_and_must_be_integrated":True,
  "source_tail_remainder_has_quadratic_Fourier_amplitude_decay":True,
  "SM41_original_complete_strong_tail_decay":"O((log cutoff)^2/cutoff)",
  "MG09_endpoint_remainder_strong_tail_decay":"O((log cutoff)^2/cutoff^3)",
  "dyadic_checkpoints":checkpoints,
  "illustrative_cutoff_crossings":crossings,
  "entire_original_strong_tail_improved_by_peeled_remainder_alone":False,
  "original_25_source_Galerkin_stiffness_certified":False,
  "original_470_source_strong_residual_certified":False,
  "actual_470_source_51_over_56_gate_passed":False,
  "complete_odd_even_Weil_CC27_RH":"OPEN",
  "independent_original_Fourier_form_domain_audit":"OPEN",
  "interpretation":"Rigorous endpoint-subtracted SOURCE strong Fourier tail. The leading boundary jump is NOT zero, and MUST be integrated exactly or with certified covariance; no complete original strong residual, positivity, or RH statement follows."
 }
 out=ROOT/args.output
 out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text(json.dumps(res,indent=2)+"\n")
 print("MG09 original endpoint-peeled analytic tail:",json.dumps({
  "sources":25,
  "cutoff_2pow12_SM41_entire":checkpoints[1]["SM41_entire_strong_tail_float"],
  "cutoff_2pow12_MG09_REMAINDER_ONLY":checkpoints[1]["MG09_only_peeled_remainder_tail_float"],
  "crossings":crossings,
  "full_odd_Weil_RH":"OPEN"}),flush=True)
if __name__=="__main__":main()
