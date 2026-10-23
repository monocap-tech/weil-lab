#!/usr/bin/env python3
"""MG66 independently reconstruct original physical source 3D mean/error sign gate.

Never imports MG66 producer. Rebuilds all 55 genuine physical original
Fourier source cells from MG58's separately authored exact physical
generator, plus MG57 original source baseline, and physical pole Gram
from MG24. The accepted MG59 INDEPENDENT source response is
reprojected on six MG65 source-plane/physical-cell witness selections.

For every selected real original physical Fourier mean, independently
assemble center Q and elementwise absolute-error covariance
R=sum 2h rho rho^T, then recheck all four global-sign-inequivalent
H_D=Q-D R D exact 3x3 SPD gates, eigenvalue determinant/e2 lower,
and source-coordinate coercivity normalization.

This validates a SUFFICIENT rank-three gate only if all 4 SPD tests
pass for at least one source plane; no actual negativity from failure.
"""
import argparse,json,sys
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
from validate_rpb108_mg58_independent_adaptive_2D_replay import generator_cells
from validate_rpb108_mg59_independent_projected_plane import build_cells,action_cell,dot
N=24;P=23
ANCHOR=(-3,0,-2,2,2,0,1,2,1,2,2,2,1,-2,-2,2,0,2,2,2,2,1,-3,-2)
def physical55(a57,a58):
 old=build_cells(a57);real=generator_cells(8)
 assert len(real)==16 and len(old)==41
 verified=next(c for c in a58["candidates"]
               if c["new_subdivisions_per_original_cell"]==8)
 for x,y in zip(real,verified["new_actual_physical_fourier_source_cells"]):
  assert [str(z) for z in x[:4]]==[
    y["left"],y["right"],y["multiplier_lower"],y["multiplier_upper"]]
  assert [str(z) for z in x[4]]==y["source_midpoint"]
  assert [str(z) for z in x[5]]==y["source_derivative"]
  assert [str(z) for z in x[6]]==y["source_error"]
 cells=[]
 for c in old:
  if c[0]==F(5,8):cells.extend(real[:8])
  elif c[0]==F(3,4):cells.extend(real[8:])
  else:cells.append(c)
 assert len(cells)==55 and cells[0][0]==0 and cells[-1][1]==4
 assert all(cells[k][1]==cells[k+1][0] for k in range(54))
 return cells
def from_physical_original_cells(cells,witness,vectors,b,berr):
 Qm=[[F(0) for _ in range(3)] for _ in range(3)]
 Rm=[[F(0) for _ in range(3)] for _ in range(3)]
 ids=witness["original_selected_physical_source_cell_indices"]
 assert ids==sorted(set(ids)) and ids and all(0<=k<55 for k in ids)
 for k in ids:
  phys=cells[k]
  width=phys[1]-phys[0]
  assert width>0
  readings=[action_cell(src,phys,b,berr) for src in vectors]
  centers=[r[0] for r in readings]
  errors=[r[2] for r in readings]
  assert all(r>=0 for r in errors)
  for i in range(3):
   for j in range(i,3):
    Qm[i][j]+=2*width*centers[i]*centers[j]
    Rm[i][j]+=2*width*errors[i]*errors[j]
 for i in range(3):
  for j in range(i):
   Qm[i][j]=Qm[j][i]
   Rm[i][j]=Rm[j][i]
 return Qm,Rm
def cmp_matrix(A,st):
 assert [[str(x) for x in line] for line in A]==st
def recheck_signs(Qm,Rm,case):
 assert len(case["four_exact_sign_gates"])==4
 assert case["full_eight_sign_patterns_checked_using_four_global_sign_equivalences"]
 exact_positive=[]
 for signs,arch in zip(((1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1)),
                       case["four_exact_sign_gates"]):
  assert arch["source_coefficient_signs"]==list(signs)
  H=[[Qm[i][j]-signs[i]*signs[j]*Rm[i][j] for j in range(3)]
     for i in range(3)]
  cmp_matrix(H,arch["exact_difference_3D_Gram"])
  a,b,c=H[0];d=H[1][1];e=H[1][2];f=H[2][2]
  p01=a*d-b*b
  p02=a*f-c*c
  p12=d*f-e*e
  # Different exact 3x3 determinant formula from MG66 producer.
  det=a*(d*f-e*e)-b*(b*f-c*e)+c*(b*e-c*d)
  e2=p01+p02+p12
  assert a==F(arch["first_principal_minor"])
  assert p01==F(arch["second_leading_principal_minor"])
  assert [str(p02),str(p12)]==arch["other_principal_2D_minors"]
  assert det==F(arch["full_exact_3D_determinant"])
  assert e2==F(arch["second_elementary_symmetric"])
  passed=(a>0 and p01>0 and det>0)
  assert passed==arch["strict_exact_rational_three_source_error_domination"]
  if passed:
   assert e2>0
   lower=det/e2
   assert lower>0
   assert lower==F(arch["positive_min_eigenvalue_rational_lower"])
   exact_positive.append(lower)
  else:assert arch["positive_min_eigenvalue_rational_lower"] is None
 success=len(exact_positive)==4
 assert success==case["all_sign_patterns_strictly_positive"]
 if success:
  mu=min(exact_positive)
  assert mu==F(case["certified_min_3D_QminusDRD_lower"])
  norm=F(case["original_source_basis_normtrace"])
  trq=sum(Qm[k][k] for k in range(3))
  trr=sum(Rm[k][k] for k in range(3))
  assert norm>0 and trq>0 and trr>=0
  # Exact norm estimate is uniform in source coefficient signs.
  lower=mu*mu/(2*(trq+trr)*norm)
  assert lower>0
  assert lower==F(case["certified_original_source_3D_coefficient_norm_coercivity"])
  return lower
 assert case["certified_min_3D_QminusDRD_lower"] is None
 assert case["certified_original_source_3D_coefficient_norm_coercivity"] is None
 return None
def main():
 p=argparse.ArgumentParser()
 for k in ("mg24","mg57","mg58","mg65","mg66"):
  p.add_argument("--verified-"+k+"-json",required=True)
 args=p.parse_args()
 d={k:json.loads((ROOT/getattr(args,"verified_"+k+"_json")).read_text())
    for k in ("mg24","mg57","mg58","mg65","mg66")}
 result=d["mg66"]
 assert result["status"]=="ORIGINAL_MG66_FULL_SIGN_COVARIANT_DIRECTIONAL_THREE_SOURCE_ERROR_GATES"
 assert all(z["canonical_W_ODD_NEG"]=="OPEN" for z in d.values())
 assert len(result["cases"])==result["source_plane_count"]==6
 assert result["rational_3D_sign_matrix_count"]==24
 assert result["source_3D_error_sign_covariance_is_sufficient_gate_NOT_operator_change"]
 assert result["all_global_sign_equivalent_error_cases_tested"]
 assert result["original_real_55_Fourier_source_cells_and_signed_multiplier_unchanged"]
 assert result["original_actual_full_frequency_strong_action_positive_tail_retained"]
 physical=physical55(d["mg57"],d["mg58"])
 H,hr,e=original_H24_from_physical_source()
 assert e==F(d["mg24"]["physical_Gram_Loewner_row_error"])
 b=[H[j][P] for j in range(N)]
 berr=[hr[j][P] for j in range(N)]
 wins=[]
 for witness in result["cases"]:
  j=witness["original_third_source_coordinate"]
  alpha=F(witness["original_anchor_scale"])
  beta=F(witness["original_third_scale"])
  assert j in (0,1,2,11,20,23)
  v=(tuple(alpha*F(a) for a in ANCHOR),
     tuple(F(int(k==5)) for k in range(N)),
     tuple(beta*F(int(k==j)) for k in range(N)))
  gram=[[dot(x,y) for y in v] for x in v]
  ga,gb,gc=gram[0];gd=gram[1][1];ge=gram[1][2];gf=gram[2][2]
  source_det=ga*gd*gf+2*gb*gc*ge-ga*ge*ge-gd*gc*gc-gf*gb*gb
  assert source_det>0,("Three original source basis vectors must be independent",j)
  assert sum(gram[k][k] for k in range(3))==F(witness["original_source_basis_normtrace"])
  Qm,Rm=from_physical_original_cells(physical,witness,v,b,berr)
  cmp_matrix(Qm,witness["original_3D_center_Gram"])
  cmp_matrix(Rm,witness["original_3D_mean_error_covariance_upper"])
  assert sum(Qm[k][k] for k in range(3))==F(witness["center_trace"])
  assert sum(Rm[k][k] for k in range(3))==F(witness["uncertainty_covariance_trace"])
  yes=recheck_signs(Qm,Rm,witness)
  if yes is not None:wins.append((yes,j))
  assert witness["unchanged_true_original_pole_and_multiplier_source"]
  assert witness["original_full_unselected_action_frequency_energy_PSD"]
  assert witness["only_restricted_3D_coercivity_not_global24"]
 assert result["certified_original_three_dimensional_source_plane_count"]==len(wins)
 assert result["rank_at_least_three_on_original_source_frame_CERTIFIED"]==bool(wins)
 if wins:
  best=max(wins,key=lambda t:t[0])
  assert best[1]==result["best_original_3D_third_source"]
  assert best[0]==F(result["best_restricted_original_3D_coercivity"])
 else:
  assert result["best_original_3D_third_source"] is None
  assert result["best_restricted_original_3D_coercivity"] is None
 assert not result["original_full24_source_strong_action_coercivity"]
 assert not result["original_24D_source_residual_contraction"]
 assert not result["original_full470_inverse"]
 assert not result["signed_odd_51over56"]
 assert result["independent_original_Fourier_form_domain_audit"]=="OPEN"
 assert result["even_Weil_CC27_RH"]=="OPEN"
 print("MG66 INDEPENDENT original real physical source 3D sign-covariant 24 matrix replay PASS",{
  "true_original_source_planes":6,
  "exact_3D_sign_covariance_matrices":24,
  "strict_3D_original_source_planes":len(wins),
  "best":(wins[0][1],str(wins[0][0])) if wins else None,
  "original_full24_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
