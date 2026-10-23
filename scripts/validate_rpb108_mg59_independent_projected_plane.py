#!/usr/bin/env python3
"""MG59 independent complete-original physical 2D strong-action projection.

No MG59 producer imports. Recreate 41 accepted original physical MG57
Fourier source cells and full original pole column. Verify each
2D projected action error by a differently ordered coefficient-wise
interval derivation that respects SAME multiplier scalar and SAME
source e_p. Independently accumulate and check exact 2x2 physical
affine Young source moments, positive det / coercivity and
negative conclusions. Never assert a global 24D rank-two lower.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
import validate_rpb108_mg32_joint_fourier_residual as orig
N=24;P=23
def dot(a,b):return sum((Q(x)*Q(y) for x,y in zip(a,b)),Q(0))
def action_cell(source,left_right,b,berr):
 left,right,wl,wu,v,d,r=left_right
 half=(right-left)/2
 mid=(wl+wu)/2;delta=(wu-wl)/2
 polecenter=dot(source,b)
 Fv=dot(source,v);Fd=dot(source,d)
 center=mid*Fv-2*v[P]*polecenter
 derivative=mid*Fd-2*d[P]*polecenter
 # Source remainder (common pole channel e_p) coefficient.
 corrected_coeff=[mid*Q(source[j]) for j in range(N)]
 corrected_coeff[P]-=2*polecenter
 coefficient_error=sum((abs(x)*y for x,y in zip(corrected_coeff,r)),Q(0))
 # True multiplier delta is SINGLE physical scalar, not one per source.
 uncertainty_t=delta*(abs(Fv)+half*abs(Fd)+sum(
    (abs(Q(source[j]))*r[j] for j in range(N)),Q(0)))
 # Pole b interval is independent of the source error.
 b_unc=sum((abs(Q(source[j]))*berr[j] for j in range(N)),Q(0))
 error_b=2*b_unc*(abs(v[P])+half*abs(d[P])+r[P])
 return center,derivative,coefficient_error+uncertainty_t+error_b
def build_cells(arch):
 source,*_=orig.exact_original_cells()
 assert len(source)==32
 interval=[]
 for x in arch["MG57_refined_true_physical_fourier_source_cells"]:
  interval.append((Q(x["left"]),Q(x["right"]),
   Q(x["multiplier_lower"]),Q(x["multiplier_upper"]),
   [Q(v) for v in x["source_midpoint"]],
   [Q(v) for v in x["source_derivative"]],
   [Q(v) for v in x["source_error"]]))
 assert len(interval)==12
 cells=[]
 for k,x in enumerate(source):
  if k in (1,2,3):cells.extend(interval[4*(k-1):4*k])
  else:cells.append(x)
 assert len(cells)==41
 assert cells[0][0]==0 and cells[-1][1]==4
 assert all(cells[j][1]==cells[j+1][0] for j in range(40))
 return cells
def replay(cells,x,y,b,berr):
 L=[[Q(0) for j in range(2)] for i in range(2)]
 U=[[Q(0) for j in range(2)] for i in range(2)]
 sig=pen=Q(0)
 young_counts={str(t):0 for t in orig.CHOSEN_TAUS}
 for cell in cells:
  l,r=cell[0],cell[1];h=r-l
  a0,a1,ar=action_cell(x,cell,b,berr)
  b0,b1,br=action_cell(y,cell,b,berr)
  center=(a0,b0);slope=(a1,b1);rad=(ar,br)
  energy=a0*a0+b0*b0+(h*h/12)*(a1*a1+b1*b1)
  er=ar+br
  tt=max(orig.CHOSEN_TAUS,key=lambda t:(
      2*h*(1-t)*energy-2*h*((1-t)/t)*er*er,-t))
  young_counts[str(tt)]+=1
  sig+=2*h*(1-tt)*energy
  pen+=2*h*(1-tt)/tt*er*er
  for i in range(2):
   for j in range(2):
    a=center[i]*center[j]+h*h*slope[i]*slope[j]/12
    L[i][j]+=2*h*(1-tt)*a
    U[i][j]+=2*h*(1+tt)*a
   L[i][i]-=2*h*(1-tt)/tt*er*rad[i]
   U[i][i]+=2*h*(1+tt)/tt*er*rad[i]
 assert L[0][1]==L[1][0]
 return L,U,sig,pen,young_counts
def qf(v,a,w=None):
 if w is None:w=v
 return sum((Q(v[i])*Q(a[i][j])*Q(w[j])
             for i in range(N) for j in range(N)),Q(0))
def main():
 p=argparse.ArgumentParser()
 for x in ("mg24","mg57","mg59"):
  p.add_argument("--verified-"+x+"-json",required=True)
 args=p.parse_args()
 inp={k:json.loads((ROOT/getattr(args,"verified_"+k+"_json")).read_text())
      for k in ("mg24","mg57","mg59")}
 old,report=inp["mg57"],inp["mg59"]
 assert report["status"]=="ORIGINAL_MG59_TRUE_ACTION_PREPROJECTED_TWO_PLANE_LOEWER"
 assert all(x["canonical_W_ODD_NEG"]=="OPEN" for x in inp.values())
 H,Hrad,err=original_H24_from_physical_source()
 assert err==Q(inp["mg24"]["physical_Gram_Loewner_row_error"])
 b=[H[j][P] for j in range(N)]
 berr=[Hrad[j][P] for j in range(N)]
 cells=build_cells(old)
 L24=[[Q(x) for x in row] for row in old["refined_original_true_strong_lower"]]
 assert len(report["candidates"])==report["tested_two_plane_count"]==10
 success=0
 for trial in report["candidates"]:
  v=[Q(x) for x in trial["first_original_integer_vector"]]
  w=[Q(x) for x in trial["second_original_integer_vector"]]
  assert len(v)==len(w)==N
  LL,UU,sig,pen,counts=replay(cells,v,w,b,berr)
  assert [[str(x) for x in row] for row in LL]==trial["new_true_original_2D_projected_action_lower"]
  assert [[str(x) for x in row] for row in UU]==trial["new_true_original_2D_projected_action_upper"]
  assert str(sig)==trial["original_new_2D_affine_signal_trace"]
  assert str(pen)==trial["original_new_2D_source_error_charge_trace"]
  assert counts==trial["chosen_Young_parameter_counts"]
  original=[[qf(t,L24,u) for u in (v,w)] for t in (v,w)]
  assert [[str(x) for x in row] for row in original]==trial[
     "old_MG57_full24_lower_restricted_to_same_2D_plane"]
  a=LL[0][0];c=LL[1][1];det=a*c-LL[0][1]*LL[0][1]
  assert str(det)==trial["exact_new_2D_gram_determinant"]
  passed=a>0 and c>0 and det>0
  assert passed==trial["exact_new_2D_strict_positive"]
  if passed:
   norm=dot(v,v)+dot(w,w)
   C=det/((a+c)*norm)
   assert C>0
   assert str(C)==trial["exact_2D_normalized_source_coercivity"]
   success+=1
  else:
   assert trial["exact_2D_normalized_source_coercivity"] is None
  assert trial["source_2D_moment_is_valid_true_original_Fourier_pole_corrected"]
  assert trial["no_global_24D_rank_two_Loewner_claim"]
 assert success==report["strict_positive_original_2D_subspaces"]
 assert bool(success)==bool(report["selected_original_positive_2D_source_label"])
 assert not report["no_original_24D_source_residual_contraction"]==False
 assert report["no_full24_source_action_coercivity"]
 assert report["independent_original_Fourier_form_domain_audit"]=="OPEN"
 assert report["even_Weil_CC27_RH"]=="OPEN"
 print("MG59 INDEPENDENT original common-scalar projected-physical-action 10-plane 2D exact rational PASS",{
  "tested":len(report["candidates"]),"positive2D_planes":success,
  "full24_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
