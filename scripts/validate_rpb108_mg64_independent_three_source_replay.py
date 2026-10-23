#!/usr/bin/env python3
"""MG64 independently rebuild all real physical original 3x3 source Jensen moments.

NO MG64 producer imports, NO numerical eigensolver, NO proposal search.
Regenerate the original 55 source frequency cells from MG58's separately
authored actual Fourier primitive generator + accepted MG57 source, read
the true original MG24 sinh pole Gram, and project the true
pole-corrected action via MG59 independent scalar source formula.

Every selected genuine 3..24-cell physical Jensen Q, Frobenius error
E, exact 3x3 Gram determinant/e2 singular lower, and rational source
coefficient norm constant is reproduced, including failure results.
A positive source plane is RESTRICTED; global 24D NOT claimed.
"""
import argparse,json,sys
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
from validate_rpb108_mg58_independent_adaptive_2D_replay import generator_cells
from validate_rpb108_mg59_independent_projected_plane import build_cells,action_cell,dot
N=24;P=23
V=tuple(F(x) for x in (-3,0,-2,2,2,0,1,2,1,2,2,2,1,-2,-2,2,0,2,2,2,2,1,-3,-2))
def physical55(a57,a58):
 baseline=build_cells(a57)
 new=generator_cells(8)
 assert len(baseline)==41 and len(new)==16
 archive=next(x for x in a58["candidates"]
              if x["new_subdivisions_per_original_cell"]==8)
 for cell,row in zip(new,archive["new_actual_physical_fourier_source_cells"]):
  assert [str(x) for x in cell[:4]]==[
    row["left"],row["right"],row["multiplier_lower"],row["multiplier_upper"]]
  assert [str(x) for x in cell[4]]==row["source_midpoint"]
  assert [str(x) for x in cell[5]]==row["source_derivative"]
  assert [str(x) for x in cell[6]]==row["source_error"]
 cells=[]
 for cell in baseline:
  if cell[0]==F(5,8):cells.extend(new[:8])
  elif cell[0]==F(3,4):cells.extend(new[8:])
  else:cells.append(cell)
 assert len(cells)==55 and cells[0][0]==0 and cells[-1][1]==4
 assert all(cells[k][1]==cells[k+1][0] for k in range(54))
 assert sum((c[1]-c[0] for c in cells),F(0))==4
 return cells
def source_row(cell,b,err,three):
 phys=[action_cell(v,cell,b,err) for v in three]
 c=[a[0] for a in phys]
 radii=[a[2] for a in phys]
 factor=2*(cell[1]-cell[0])
 assert factor>0 and all(r>=0 for r in radii)
 return {
  "center":[factor*c[i]*c[j] for i,j in (
    (0,0),(0,1),(0,2),(1,1),(1,2),(2,2))],
  "error":factor*sum((e*e for e in radii),F(0))}
def rational_check(rows,subset,norm,arch):
 ids=arch["original_physical_cell_indices"]
 assert ids==sorted(set(ids))
 assert all(isinstance(i,int) and 0<=i<55 for i in ids)
 assert len(ids)==arch["true_original_selected_cell_count"]==subset>=3
 vec=[sum((rows[i]["center"][k] for i in ids),F(0))
      for k in range(6)]
 a,b,c,d,e,f=vec
 E=sum((rows[i]["error"] for i in ids),F(0))
 # Recompute symmetric polynomial using the principal 2x2 minors,
 # not a numeric LDL or producer matrix helper.
 e2=(a*d-b*b)+(a*f-c*c)+(d*f-e*e)
 # Alternative determinant expansion, exactly equal to producer.
 det=a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b
 assert all(x>=0 for x in (a,d,f,E))
 L=det/e2 if e2>0 and det>0 else F(0)
 good=(L>E and L>0)
 C=(L-E)**2/(4*L*norm) if good else None
 for name,val in (
    ("center_gram_00",a),("center_gram_01",b),
    ("center_gram_02",c),("center_gram_11",d),
    ("center_gram_12",e),("center_gram_22",f),
    ("center_3D_second_elementary_symmetric",e2),
    ("center_3D_exact_determinant",det),
    ("center_3D_min_eigenvalue_rational_lower",L),
    ("original_physical_mean_error_Frobenius_sq_upper",E)):
  assert F(arch[name])==val,(name,subset)
 assert arch["exact_3D_singular_gap_positive"]==good
 assert arch["all_unmeasured_true_original_action_frequency_energy_PSD"]
 assert arch["no_global_24D_strong_source_Loewner_claim"]
 if good:
  assert C>0 and C==F(arch["restricted_true_original_source_3D_coercivity"])
 else:
  assert arch["restricted_true_original_source_3D_coercivity"] is None
 return good,C
def main():
 p=argparse.ArgumentParser()
 for key in ("mg24","mg57","mg58","mg63","mg64"):
  p.add_argument("--verified-"+key+"-json",required=True)
 opt=p.parse_args()
 files={k:json.loads((ROOT/getattr(opt,"verified_"+k+"_json")).read_text())
        for k in ("mg24","mg57","mg58","mg63","mg64")}
 out=files["mg64"]
 assert all(z["canonical_W_ODD_NEG"]=="OPEN" for z in files.values())
 assert out["status"]=="ORIGINAL_MG64_GENUINE_PHYSICAL_THREE_SOURCE_JENSEN_SINGULAR_GAP"
 assert files["mg63"]["coordinate5_positive_source_plane_certified"]
 assert out["three_source_exact_rational_singular_acceptance_only"]
 assert out["true_physical_pole_corrected_strong_action_unchanged"]
 assert out["float_only_proposes_original_cell_subsets"]
 assert out["original_genuine_physical_Fourier_cell_count"]==55
 assert len(out["cases"])==out["trial_original_source_plane_count"]
 assert tuple(out["trial_source_coordinate_axes"])==(0,1,2,11,20,23)
 assert dot(V,V)==82 and V[5]==0
 cells=physical55(files["mg57"],files["mg58"])
 phys,rad,poleErr=original_H24_from_physical_source()
 assert poleErr==F(files["mg24"]["physical_Gram_Loewner_row_error"])
 b=[phys[i][P] for i in range(N)]
 brad=[rad[i][P] for i in range(N)]
 win=[];num=0
 for case in out["cases"]:
  j=case["original_source_third_coordinate"]
  alpha=F(case["physical_anchor_alpha"])
  beta=F(case["physical_third_beta"])
  assert j in (0,1,2,11,20,23)
  assert alpha in (F(1,128),F(1,256))
  assert beta in (F(1),F(1,16),F(1,256))
  vec=(tuple(alpha*x for x in V),
       tuple(F(k==5) for k in range(N)),
       tuple(beta*F(k==j) for k in range(N)))
  norm=sum((dot(v,v) for v in vec),F(0))
  assert norm>0 and norm==F(case["source_basis_three_vector_normtrace"])
  gram=[[dot(x,y) for y in vec] for x in vec]
  assert [[str(x) for x in row] for row in gram]==case["original_source_coefficient_Gram"]
  a,b01,c=gram[0]
  d,e,f=gram[1][1],gram[1][2],gram[2][2]
  gd=a*d*f+2*b01*c*e-a*e*e-d*c*c-f*b01*b01
  assert gd>0 and gd==F(case["original_source_coefficient_Gram_determinant"])
  rows=[source_row(cell,b,brad,vec) for cell in cells]
  archive=case["best_certificate_per_subset_size"]
  assert [r["subset_size"] for r in archive]==[3,4,6,8,12,16,24]
  passed=0
  for item in archive:
   n=item["subset_size"]
   assert item["number_exact_candidate_subsets_tested"]>=1
   value=item["best_exact_source_3D_subset"]
   yes,C=rational_check(rows,n,norm,value)
   if item["number_exact_positive_subsets"]>0:
    assert yes and C>0
   passed+=int(yes)
   num+=1
   if yes:win.append((C,j,alpha,beta,value["original_physical_cell_indices"]))
  assert bool(passed)==case["positive_source_three_plane"]
 assert num==len(out["cases"])*7
 assert bool(win)==out["three_dimensional_strict_source_moment_certified"]
 if win:
  top=max(win,key=lambda item:item[0])
  assert top[1]==out["best_third_original_coordinate"]
  assert str(top[2])==out["best_original_anchor_alpha"]
  assert str(top[3])==out["best_original_third_beta"]
  assert top[0]==F(out["best_strict_restricted_source3D_coercivity"])
  assert top[4]==out["best_original_three_source_physical_cell_indices"]
 else:
  assert out["best_third_original_coordinate"] is None
  assert out["best_original_anchor_alpha"] is None
  assert out["best_original_third_beta"] is None
  assert out["best_strict_restricted_source3D_coercivity"] is None
 assert not out["original_full24_strong_action_coercivity"]
 assert not out["original_source24_residual_contraction"]
 assert not out["original_full470_inverse"]
 assert not out["odd_signed_51over56"]
 assert out["independent_original_Fourier_form_domain_audit"]=="OPEN"
 assert out["even_Weil_CC27_RH"]=="OPEN"
 print("MG64 INDEPENDENT original true physical Fourier 3D mean Gram exact rational PASS",{
  "original_source_third_coordinates":len(set(c["original_source_third_coordinate"] for c in out["cases"])),
  "fully_rebuilt_selected_exact_source_3D_moments":num,
  "positive_3D_selected_exact_source_Grams":len(win),
  "full24_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
