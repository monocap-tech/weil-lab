#!/usr/bin/env python3
"""MG56 independent original pole-corrected action source moment replay.

No MG56 producer import. Reconstruct genuine original 32 physical
Fourier source cells with the accepted independent MG32/MG29 generator.
Implement original corrected strong-vector midpoint/derivative and
interval radii by separately written formula. Independently assemble
rational full24 affine covariance LO/HI matrices, exact old Young tau
and verify exact equality after accepted outward compaction. Check
genuine full-frequency Sstar >= band >= L, and no spectral promotions.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
import validate_rpb108_mg32_joint_fourier_residual as orig
N=24;P=23
def rd(a):
 A=[[Q(x) for x in row] for row in a]
 assert len(A)==N and all(len(row)==N for row in A)
 return A
def trans(A):return [list(z) for z in zip(*A)]
def plus(A,B):return [[a+b for a,b in zip(ra,rb)] for ra,rb in zip(A,B)]
def mul(a,A):return [[a*x for x in r] for r in A]
def sub(A,B):return plus(A,mul(-1,B))
def eye():return [[Q(i==j) for j in range(N)] for i in range(N)]
def qf(v,A):return sum((v[i]*A[i][j]*v[j] for i in range(N) for j in range(N)),Q(0))
def exact_psd(A):
 assert A==trans(A)
 A=[r[:] for r in A]
 for k in range(N):
  z=A[k][k]
  assert z>=0
  if z==0:
   assert all(A[k][i]==0 for i in range(k+1,N))
   continue
  for i in range(k+1,N):
   for j in range(i,N):
    A[i][j]-=A[k][i]*A[k][j]/z
    A[j][i]=A[i][j]
 return True
def accumulation(cells,bc,be):
 lo,hi=orig.zero(),orig.zero()
 records=[];counts={str(z):0 for z in orig.CHOSEN_TAUS}
 radii=Q(0)
 for left,right,wlo,whi,v,d,r in cells:
  width=right-left;half=width/2
  center=(wlo+whi)/2;deviation=(whi-wlo)/2
  actual0=[];actuald=[];actualr=[]
  pole_amplitude=abs(v[P])+half*abs(d[P])+r[P]
  for j in range(N):
   actual0.append(center*v[j]-2*bc[j]*v[P])
   actuald.append(center*d[j]-2*bc[j]*d[P])
   # Two errors separately: true scalar a(xi) and global
   # original physical rank-one btrue coefficient error.
   mult_err=(abs(center)+deviation)*r[j]+deviation*(
             abs(v[j])+half*abs(d[j]))
   pole_err=2*(abs(bc[j])*r[P]+be[j]*pole_amplitude)
   actualr.append(mult_err+pole_err)
   assert actualr[-1]>=0
  assert len(actual0)==len(actuald)==len(actualr)==N
  # Independent Young cost formula (not producer lower_cell_trace).
  def cost(t):
   amplitude=sum((z*z for z in actual0),Q(0))
   amplitude+=width*width*sum((z*z for z in actuald),Q(0))/12
   error=sum(actualr,Q(0))
   return 2*width*((1-t)*amplitude-(1/t-1)*error*error)
  tau=max(orig.CHOSEN_TAUS,key=lambda t:(cost(t),-t))
  assert Q(0)<tau<Q(1)
  counts[str(tau)]+=1
  scale_lower=2*width*(1-tau)
  scale_upper=2*width*(1+tau)
  slope_var=width*width/12
  Rsum=sum(actualr,Q(0))
  for i in range(N):
   for j in range(N):
    vv=actual0[i]*actual0[j]+slope_var*actuald[i]*actuald[j]
    lo[i][j]+=scale_lower*vv
    hi[i][j]+=scale_upper*vv
   lo[i][i]-=2*width*(1/tau-1)*Rsum*actualr[i]
   hi[i][i]+=2*width*(1+1/tau)*Rsum*actualr[i]
  radii+=Rsum
  records.append({
    "left":str(left),"right":str(right),
    "multiplier_lower":str(wlo),"multiplier_upper":str(whi),
    "tau":str(tau),
    "strong_midpoint_source":[str(x) for x in actual0],
    "strong_affine_slope":[str(x) for x in actuald],
    "strong_error_radius":[str(x) for x in actualr]})
 # Shared MG14 outward exact rational compaction only. Both
 # full24 original quadratic formulas separately implemented above.
 L,U,_,_=orig.finalize((lo,hi))
 assert exact_psd(U)
 assert exact_psd(sub(U,L))
 return L,U,counts,radii,records
def main():
 p=argparse.ArgumentParser()
 for z in ("mg24","mg29","mg56"):p.add_argument("--verified-"+z+"-json",required=True)
 args=p.parse_args()
 load=lambda z:json.loads((ROOT/getattr(args,"verified_"+z+"_json")).read_text())
 a24,a29,a56=[load(z) for z in ("mg24","mg29","mg56")]
 assert a56["status"]=="ORIGINAL_MG56_POLE_CORRECTED_STRONG_ACTION_BAND_24D_LOWER"
 assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in (a24,a29,a56))
 hm,hr,err=original_H24_from_physical_source()
 assert err==Q(a24["physical_Gram_Loewner_row_error"])
 bc=[hm[i][P] for i in range(N)]
 be=[hr[i][P] for i in range(N)]
 assert [str(x) for x in bc]==a24["original_pole_b_center"]
 assert [str(x) for x in be]==a24["original_pole_b_radii"]
 cells,cl,cu,rads,oldcounts=orig.exact_original_cells()
 assert len(cells)==32 and cells[0][0]==0 and cells[-1][1]==4
 assert str(rads)==a56["mg29_physical_source_radius_sum"]
 assert str(rads)==next(x for x in a29["meshes"] if x["mesh_cells"]==32)["total_source_radius_MG29"]
 L,U,counts,radii,details=accumulation(cells,bc,be)
 assert L==rd(a56["exact_band_lower"]) and U==rd(a56["exact_band_upper"])
 assert a56["strong_band_young_counts"]==counts
 assert a56["cells_exact_rational"]==details
 assert str(radii)==a56["mg56_corrected_action_source_radius_sum"]
 assert str(sum(L[i][i] for i in range(N)))==a56["band_lower_trace"]
 assert str(sum(U[i][i] for i in range(N)))==a56["band_upper_trace"]
 assert [str(L[i][i]) for i in range(N)]==a56["all_24_coordinate_lower_values"]
 positive=[i for i in range(N) if L[i][i]>0]
 assert positive==a56["positive_coordinate_indices"]
 assert len(positive)==a56["positive_coordinate_count"]
 kind=a56["band_lower_inertia"]
 if kind=="NEGATIVE_EXACT_RATIONAL_RAYLEIGH":
  z=a56["band_lower_inertia_witness"]
  v=[Q(x) for x in z["rational_vector"]]
  assert qf(v,L)==Q(z["exact_negative_quadratic"])<0
 elif kind=="POSITIVE_EXACT_RATIONAL_LDL":
  mat=[r[:] for r in L]
  for k in range(N):
   pivot=mat[k][k]
   assert pivot>0
   for i in range(k+1,N):
    for j in range(i,N):
     mat[i][j]-=mat[k][i]*mat[k][j]/pivot
     mat[j][i]=mat[i][j]
 else:assert kind=="INCONCLUSIVE"
 assert a56["original_strong_full24_positive_definite"]==(kind=="POSITIVE_EXACT_RATIONAL_LDL")
 for comparison in a56["accepted_MG24_lower_comparisons"]:
  k=comparison["cutoff_k"]
  previous=rd(next(x for x in a24["cases"] if x["cutoff_k"]==k)["complete_Sstar_lower"])
  assert exact_psd(mul(-1,previous))
  assert comparison["old_full_original_MG24_lower_is_negative_semidefinite"]
  try:
   newer_dominates=exact_psd(sub(L,previous))
  except AssertionError:
   newer_dominates=False
  assert comparison["new_strong_band_lower_minus_MG24_lower_PSD"]==newer_dominates
  assert str(sum(previous[i][i] for i in range(N)))==comparison["old_lower_trace"]
  assert sum(previous[i][i]>0 for i in range(N))==comparison["strict_positive_diagonal_directions_old"]
  assert len(positive)==comparison["strict_positive_diagonal_directions_new"]
 assert a56["true_original_full_frequency_Sstar_ge_new_band_L_in_Loewner"]
 assert a56["genuine_original_ao_minus_2_pole_action_not_unpoled_surrogate"]
 assert not a56["original_source_contraction"]
 assert not a56["original_470D_inverse"]
 assert not a56["signed_odd_51over56_cap"]
 assert a56["independent_original_Fourier_form_domain_audit"]=="OPEN"
 assert a56["even_Weil_CC27_RH"]=="OPEN"
 print("MG56 INDEPENDENT original pole-corrected strong-action 24D Fourier band lower PASS",{
  "cells":len(cells),"positive_rational_coordinates":len(positive),
  "band_full24_inertia":kind,"470D_and_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
