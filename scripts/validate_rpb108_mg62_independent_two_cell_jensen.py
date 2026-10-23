#!/usr/bin/env python3
"""MG62 independent true original two-cell source Jensen singular-gap audit.

NO MG62 producer import. Rebuild true original 55-cell physical Fourier
source from MG58's separately authored independent primitive generator.
Reconstruct the pole-column original physical Gram and cell-projected
source moment using MG59's independent original action_cell formula.
For EVERY archived source-plane and proposed cell pair, recompute
exact rational (center Gram, Frobenius mean-error charge), verify
strict 2D singular gap and conservative source Euclidean coercivity.
No claim from float ranking, no global rank-two Loewner promotion.
"""
import argparse,json,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
from validate_rpb108_mg58_independent_adaptive_2D_replay import generator_cells
from validate_rpb108_mg59_independent_projected_plane import build_cells,action_cell,dot
N=24;P=23
V=(-3,0,-2,2,2,0,1,2,1,2,2,2,1,-2,-2,2,0,2,2,2,2,1,-3,-2)
def original55(mg57,mg58):
 base=build_cells(mg57);new=generator_cells(8)
 assert len(base)==41 and len(new)==16
 parent=next(a for a in mg58["candidates"] if a["new_subdivisions_per_original_cell"]==8)
 for cell,record in zip(new,parent["new_actual_physical_fourier_source_cells"]):
  assert [str(z) for z in cell[:4]]==[
   record["left"],record["right"],record["multiplier_lower"],record["multiplier_upper"]]
  assert [str(z) for z in cell[4]]==record["source_midpoint"]
  assert [str(z) for z in cell[5]]==record["source_derivative"]
  assert [str(z) for z in cell[6]]==record["source_error"]
 cells=[]
 for old in base:
  if old[0]==Q(5,8):cells.extend(new[:8])
  elif old[0]==Q(3,4):cells.extend(new[8:])
  else:cells.append(old)
 assert len(cells)==55 and cells[0][0]==0 and cells[-1][1]==4
 assert all(cells[i][1]==cells[i+1][0] for i in range(54))
 return cells
def replay_pair(cells,pair,u,w,b,rad,original_norm):
 z00=z01=z11=err=Q(0)
 for idx in pair:
  l,r,*_=cells[idx]
  h=r-l
  a=action_cell(u,cells[idx],b,rad)
  d=action_cell(w,cells[idx],b,rad)
  mid=(a[0],d[0]);error=(a[2],d[2])
  factor=2*h
  z00+=factor*mid[0]**2
  z01+=factor*mid[0]*mid[1]
  z11+=factor*mid[1]**2
  err+=factor*(error[0]**2+error[1]**2)
 det=z00*z11-z01*z01
 tr=z00+z11
 lam=det/tr if tr>0 else Q(0)
 accepted=lam>err and lam>0
 coefficient=((lam-err)**2/(4*lam*original_norm)
              if accepted else None)
 return (z00,z01,z11,det,lam,err,accepted,coefficient)
def main():
 p=argparse.ArgumentParser()
 for x in ("mg24","mg57","mg58","mg61","mg62"):
  p.add_argument("--verified-"+x+"-json",required=True)
 args=p.parse_args()
 data={x:json.loads((ROOT/getattr(args,"verified_"+x+"_json")).read_text())
       for x in ("mg24","mg57","mg58","mg61","mg62")}
 out=data["mg62"]
 assert out["status"]=="ORIGINAL_MG62_TWO_REAL_FOURIER_CELL_JENSEN_SINGULAR_SOURCE_PLANE_GATE"
 assert all(z["canonical_W_ODD_NEG"]=="OPEN" for z in data.values())
 assert out["float_proposal_not_mathematical_acceptance"]
 assert out["exact_rational_coercivity_acceptance_only"]
 assert out["two_measured_physical_cell_mean_interval_Jensen"]
 assert out["actual_original_strong_energy_remaining_frequency_PSD"]
 assert len(out["results"])==out["tested_original_source_planes"]==48
 assert out["tested_genuine_cell_pairs"]==144
 assert len(V)==24 and sum(x*x for x in V)==82
 src=original55(data["mg57"],data["mg58"])
 physical,pole_r,he=original_H24_from_physical_source()
 assert he==Q(data["mg24"]["physical_Gram_Loewner_row_error"])
 pole=[physical[j][P] for j in range(N)]
 uncertainty=[pole_r[j][P] for j in range(N)]
 total_good=0;planes=0;best=None
 for expected_alpha in (Q(1,9),Q(1,18)):
  u=tuple(expected_alpha*Q(x) for x in V)
  for axis in range(N):
   row=out["results"][(0 if expected_alpha==Q(1,9) else 24)+axis]
   assert row["original_coordinate"]==axis
   assert Q(row["anchor_scale"])==expected_alpha
   v=tuple(Q(j==axis)-Q(V[axis])*Q(V[j])/82 for j in range(N))
   assert dot(V,v)==0
   assert [str(x) for x in v]==row["original_second_orthogonal_vector"]
   norm=dot(u,u)+dot(v,v)
   assert norm>0 and norm==Q(row["source_plane_coordinate_norm_trace"])
   assert len(row["exact_original_Jensen_pair_tests"])==3
   used=set();local_good=0
   for t in row["exact_original_Jensen_pair_tests"]:
    i,j=t["source_cell_indices"]
    assert isinstance(i,int) and isinstance(j,int)
    assert 0<=i<j<55 and (i,j) not in used
    used.add((i,j))
    assert t["original_cell_interval_endpoints"]==[
      [str(src[k][0]),str(src[k][1])] for k in (i,j)]
    q00,q01,q11,det,lam,er,good,c=replay_pair(
      src,(i,j),u,v,pole,uncertainty,norm)
    for key,val in (
      ("center_gram00",q00),("center_gram01",q01),
      ("center_gram11",q11),("center_gram_determinant",det),
      ("center_min_singular_squared_lower",lam),
      ("original_two_cell_mean_error_Frobenius_squared_upper",er)
    ):
     assert Q(t[key])==val
    assert t["exact_positive_2D_singular_gap"]==good
    if good:
     assert c is not None and c>0
     assert c==Q(t["strict_original_restricted_source_coercivity"])
     total_good+=1;local_good+=1
     if best is None or c>best[0]:best=(c,axis,expected_alpha)
    else:assert t["strict_original_restricted_source_coercivity"] is None
    assert t["not_original_global24_rank2_Loewner"]
   assert row["positive_two_cell_source_pair_count"]==local_good
   planes+=int(local_good>0)
 assert planes==out["strict_positive_2D_planes_certified"]
 if best:
  assert out["best_original_source_coordinate"]==best[1]
  assert Q(out["best_original_source_scale"])==best[2]
  assert Q(out["best_exact_original_source_coercivity_constant"])==best[0]
 else:
  assert out["best_original_source_coordinate"] is None
  assert out["best_original_source_scale"] is None
  assert out["best_exact_original_source_coercivity_constant"] is None
 assert out["no_original_global_24D_rank_two_Loewner"]
 assert out["no_original_24D_source_residual_contraction"]
 assert out["no_original_470D_inverse"]
 assert out["no_original_signed_51over56_odd_cap"]
 assert out["independent_original_Fourier_form_domain_audit"]=="OPEN"
 assert out["even_Weil_CC27_RH"]=="OPEN"
 print("MG62 INDEPENDENT original two physical Fourier cell Jensen singular-gap 144 exact 2D checks PASS",{
   "strict_pairs":total_good,"strict_2D_original_source_planes":planes,
   "original_full24_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
