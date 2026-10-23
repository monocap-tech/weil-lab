#!/usr/bin/env python3
"""MG58 independent true physical Fourier action-moment full24 and 2D replay.

This file NEVER imports MG58's producer. It reconstructs new original
5/8–7/8 source cells by directly calling accepted physical MG29
Fourier/Taylor primitives and original SM43 seven-prime/digamma weight.
For matrix accumulation use separately authored MG57 independent exact
rational affine Young/outer-product formula, not MG57/MG58 producers.
Check reverse-order exact 24D LDL inertias and, if and only if 2D
positive exists, exact 2x2 Gram determinant and coercivity constant.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
from validate_rpb108_mg57_independent_pole_refinement_replay import independent_matrices
import validate_rpb108_mg32_joint_fourier_residual as orig
N=24;P=23
PREV_V=(-3,0,-2,2,2,0,1,2,1,2,2,2,1,-2,-2,2,0,2,2,2,2,1,-3,-2)
def rd(a):
 z=[[Q(x) for x in row] for row in a]
 assert len(z)==N and all(len(r)==N for r in z)
 return z
def qf(v,A,w=None):
 if w is None:w=v
 return sum((Q(v[i])*A[i][j]*Q(w[j]) for i in range(N)
              for j in range(N)),Q(0))
def reverse_index(A):
 assert all(A[i][j]==A[j][i] for i in range(N) for j in range(N))
 z=[row[:] for row in A]
 pos=neg=0
 for k in reversed(range(N)):
  pivot=z[k][k]
  assert pivot!=0,("zero reverse pivot",k)
  pos+=int(pivot>0);neg+=int(pivot<0)
  for i in range(k):
   for j in range(i,k):
    z[i][j]-=z[i][k]*z[k][j]/pivot
    z[j][i]=z[i][j]
 return pos,neg
def generator_cells(n):
 prep=orig.original_partition_preparation()
 centers,src,a,c,hyp,g2,g3=prep
 assert len(src)==25 and src[24][0]=="pole"
 g4=orig.original_fourth_global(src)
 cells=[]
 for i in (5,6):
  left=Q(i,8)
  for j in range(n):
   lo=left+Q(j,8*n);hi=left+Q(j+1,8*n)
   assert hi-lo==Q(1,8*n)
   mid=(lo+hi)/2;half=(hi-lo)/2
   wlo,whi,_=orig.positive_cell_weight_interval(lo,hi)
   mid_phys=orig.original_exact_physical_fourier_midpoint(mid,centers,src,hyp)
   derivative,second=orig.original_midpoint_derivative_intervals(
      mid,centers,src,hyp)
   K=[min(cap,orig.abs_cap(z)+d3*half) if z is not None else cap
      for cap,z,d3 in zip(g2,second,g3)]
   v,d,rough=orig.transformed_affine(mid_phys,derivative,K,a,c,half)
   rec=orig.splits_original_source(v,d,rough,K,half,
                                   mid_phys,derivative,a,c,23,24)
   actual2=orig.exact_original_second_midpoint(mid,centers,src,hyp)
   third=orig.third_adapted_whole_cell(mid,centers,src,hyp,
                                       a,c,g3,half,g4)
   old_bound=orig.true_direct_adapted_curvature(
      actual2,g3,a,c,K,half)
   radius=[]
   for k,(centerr,deriv_error,_,_) in enumerate(rec):
    D2=(actual2[k]-a[k]*actual2[24]-c[k]*actual2[23]
        if k<23 else actual2[24])
    capped=min(old_bound[k][0],orig.abs_cap(D2)+third[k][0]*half)
    e=orig.up(centerr+deriv_error+half*half*capped/2)
    assert Q(0)<=e<=rough[k]
    radius.append(e)
   cells.append((lo,hi,wlo,whi,v,d,radius))
 return cells
def baseline(a57):
 original,*_=orig.exact_original_cells()
 assert len(original)==32
 archive=a57["MG57_refined_true_physical_fourier_source_cells"]
 assert len(archive)==12
 real=[]
 for rec in archive:
  real.append((
   Q(rec["left"]),Q(rec["right"]),
   Q(rec["multiplier_lower"]),Q(rec["multiplier_upper"]),
   [Q(z) for z in rec["source_midpoint"]],
   [Q(z) for z in rec["source_derivative"]],
   [Q(z) for z in rec["source_error"]]))
 out=[]
 for i,x in enumerate(original):
  if i in (1,2,3):out.extend(real[(i-1)*4:i*4])
  else:out.append(x)
 assert len(out)==41 and out[0][0]==0 and out[-1][1]==4
 return out
def validate_plane(L,row):
 plane=row["positive_original_two_dimensional_source_plane"]
 if plane is None:
  assert not row["genuine_2D_positive_action_moment_CERTIFIED"]
  assert row["original_full24_conservative_LDL_inertia"]["positive"]<2
  return
 assert row["genuine_2D_positive_action_moment_CERTIFIED"]
 u=[Q(x) for x in plane["first_integer_vector"]]
 v=[Q(x) for x in plane["second_integer_vector"]]
 assert len(u)==len(v)==N
 a=qf(u,L);b=qf(u,L,v);c=qf(v,L);delta=a*c-b*b
 assert a>0 and c>0 and delta>0
 assert a==Q(plane["gram_00"]) and b==Q(plane["gram_01"])
 assert c==Q(plane["gram_11"]) and delta==Q(plane["gram_determinant"])
 normu=sum(x*x for x in u);normv=sum(x*x for x in v)
 assert normu==Q(plane["first_integer_coefficient_norm_squared"])
 assert normv==Q(plane["second_integer_coefficient_norm_squared"])
 constant=delta/((a+c)*(normu+normv))
 assert constant>0
 assert constant==Q(plane["normalized_2D_strict_lower_bound"])
 assert plane["exact_2D_positive_definite"]
 assert plane["bound_applies_only_to_span_NOT_whole24"]
def main():
 p=argparse.ArgumentParser()
 for name in ("mg24","mg57","mg58"):
  p.add_argument("--verified-"+name+"-json",required=True)
 args=p.parse_args()
 data={name:json.loads((ROOT/getattr(args,"verified_"+name+"_json")).read_text())
       for name in ("mg24","mg57","mg58")}
 a24,a57,a58=data["mg24"],data["mg57"],data["mg58"]
 assert a58["status"]=="ORIGINAL_MG58_TRUE_FOURIER_ADAPTIVE_2D_STRONG_SUBSPACE"
 assert all(z["canonical_W_ODD_NEG"]=="OPEN" for z in data.values())
 hm,hr,er=original_H24_from_physical_source()
 assert er==Q(a24["physical_Gram_Loewner_row_error"])
 bc=[hm[i][P] for i in range(N)]
 br=[hr[i][P] for i in range(N)]
 old=baseline(a57)
 L57,U57,rows57=independent_matrices(old,bc,br,True)
 assert L57==rd(a57["refined_original_true_strong_lower"])
 assert U57==rd(a57["refined_original_true_strong_upper"])
 assert reverse_index(L57)==(1,23)
 assert str(sum(L57[i][i] for i in range(N)))==a58["original_MG57_baseline_lower_trace"]
 assert qf(PREV_V,L57)>0
 assert len(a58["candidates"])==2
 highest=(-1,Q(-10**6))
 for i,(n,case) in enumerate(zip((4,8),a58["candidates"])):
  assert case["new_subdivisions_per_original_cell"]==n
  physical=generator_cells(n)
  saved=case["new_actual_physical_fourier_source_cells"]
  assert len(physical)==len(saved)==2*n
  for x,y in zip(physical,saved):
   assert [str(z) for z in x[:4]]==[
    y["left"],y["right"],y["multiplier_lower"],y["multiplier_upper"]]
   assert [str(z) for z in x[4]]==y["source_midpoint"]
   assert [str(z) for z in x[5]]==y["source_derivative"]
   assert [str(z) for z in x[6]]==y["source_error"]
  new=[]
  for x in old:
   if x[0]==Q(5,8):new.extend(physical[:n])
   elif x[0]==Q(3,4):new.extend(physical[n:])
   else:new.append(x)
  assert len(new)==41+2*(n-1)==case["total_true_original_source_cell_count"]
  assert all(new[k][1]==new[k+1][0] for k in range(len(new)-1))
  assert new[0][0]==0 and new[-1][1]==4
  L,U,rows=independent_matrices(new,bc,br,True)
  assert L==rd(case["new_full24_original_corrected_action_lower"])
  assert U==rd(case["new_full24_original_corrected_action_upper"])
  pos,neg=reverse_index(L)
  assert (pos,neg)==(
   case["original_full24_conservative_LDL_inertia"]["positive"],
   case["original_full24_conservative_LDL_inertia"]["negative"])
  assert pos+neg==24
  assert case["full24_strong_action_coercivity_CERTIFIED"]==(pos==24)
  assert str(sum(L[k][k] for k in range(N)))==case["true_original_strong_action_lower_trace"]
  assert sum(L[k][k]>0 for k in range(N))==case["positive_original_source_coordinate_diagonals"]
  validate_plane(L,case)
  selected_charge=sum((Q(x["trace_error_penalty"]) for x in rows
      if Q(5,8)<=Q(x["left"]) and Q(x["right"])<=Q(7,8)),Q(0))
  original_charge=sum((Q(x["trace_error_penalty"]) for x in rows57
      if Q(5,8)<=Q(x["left"]) and Q(x["right"])<=Q(7,8)),Q(0))
  assert str(selected_charge)==case["new_physical_original_subcells_Young_charge"]
  assert str(original_charge)==case["original_baseline_two_highest_loss_cells_Young_charge"]
  assert str(original_charge-selected_charge)==case["focused_absolute_Young_charge_reduction"]
  assert str(sum(Q(x["trace_error_penalty"]) for x in rows))==case["total_original_source_Young_error_charge"]
  assert str(sum(Q(x["trace_signal"]) for x in rows))==case["total_original_source_affine_signal_trace"]
  assert str(qf(PREV_V,L))==case["MG57_previous_positive_integer_ray_under_new_lower"]
  assert case["whole_source_true_original_pole_correction"]
  assert case["no_inference_full24_from_trace_or_single_ray"]
  rank=(pos,sum(L[k][k] for k in range(N)))
  if rank>highest:highest=rank
 assert a58["selected_conservative_positive_index"]==highest[0]
 best=max(a58["candidates"],key=lambda z:(
    z["original_full24_conservative_LDL_inertia"]["positive"],
    Q(z["true_original_strong_action_lower_trace"])))
 assert best["new_subdivisions_per_original_cell"]==a58["selected_refinement_n"]
 assert a58["selected_strict_original_2D_action_subspace_CERTIFIED"]==best[
   "genuine_2D_positive_action_moment_CERTIFIED"]
 assert not a58["original_source_residual_24D_contraction"]
 assert not a58["original_full470_inverse"]
 assert not a58["original_signed_odd_51over56"]
 assert a58["independent_original_Fourier_form_domain_audit"]=="OPEN"
 assert a58["even_Weil_CC27_RH"]=="OPEN"
 print("MG58 INDEPENDENT actual physical original source 47 and 55 cells, reverse 24D inertia and 2D strict rational subspace gate PASS",{
   "selected_original_source_positive_index":highest[0],
   "2D_strict_coercivity":a58["selected_strict_original_2D_action_subspace_CERTIFIED"],
   "full24_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
