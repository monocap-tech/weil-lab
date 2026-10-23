#!/usr/bin/env python3
"""MG64: true original physical strong-action THREE-source Jensen singular gap.

MG62/MG63 independently certified strict original strong-action energy
on all 24 separately restricted source coordinate TWO-PLANES sharing
MG57 anchor v. These do NOT imply rank>=3.

MG64 fixes SAME original 55 physical MG57/MG58 Fourier cells, SI10 25
physical -> MG11 23 adapted plus actual sinh pole, signed 7-prime and
digamma scalar multiplier and actual pole-corrected action. It projects
each original physical cell onto 3 source coefficient directions
[v*alpha,e5,e_j*beta] before any uncertainty enclosure.

For selected disjoint physical frequency cells, physical Jensen means
form a 3x3 center Gram Q=sum 2h c c^T, with actual mean uncertainty
Frobenius-square bound E=sum 2h sum rho_k^2. For positive Gram Q,
e2=sum of its 2x2 principal minors=det(Q)*trace(inv(Q)); hence
lambda_min(Q)>=det(Q)/e2=:L. An EXACT RATIONAL L>E proves
strict 3D original physical source action coercivity on the whole
restricted source span, with coefficient norm constant
(L-E)^2/[4 L trace(W^T W)]>0. Floating cell choice is proposal ONLY.

NO inference of full 24D strong action coercivity, actual residual
contraction, 470D inverse, signed odd spectral cap or RH.
"""
import argparse,json,math,sys
from fractions import Fraction as Q
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import ROOT
from validate_rpb108_mg25_original24_robust_trial import original_H24_from_physical_source
import validate_rpb108_mg59_projected_true_action_plane as m59
import validate_rpb108_mg62_two_cell_jensen_gap as m62
N=24;P=23
V=tuple(Q(x) for x in m59.ANCHOR)
assert len(V)==N and V[5]==0 and sum(x*x for x in V)==82
THIRD_AXES=(0,1,2,11,20,23)
ANCHOR_SCALES=(Q(1,128),Q(1,256))
THIRD_SCALES=(Q(1),Q(1,16),Q(1,256))
TARGET_SIZES=(3,4,6,8,12,16,24)
def gram_data(z):
 a,b,c,d,e,f,E=z
 tr=a+d+f
 m01=a*d-b*b
 m02=a*f-c*c
 m12=d*f-e*e
 e2=m01+m02+m12
 det=a*m12-b*(b*f-c*e)+c*(b*e-c*d)
 L=det/e2 if e2>0 and det>0 else Q(0)
 return tr,e2,det,L,E
def proj_three(cell,vectors,bmid,brad):
 h=cell[1]-cell[0]
 assert h>0
 v=[m59.project_one(s,cell,bmid,brad) for s in vectors]
 factor=2*h
 c=[x[0] for x in v]
 rad=[x[2] for x in v]
 assert all(r>=0 for r in rad)
 a=factor*c[0]*c[0]
 b=factor*c[0]*c[1]
 cc=factor*c[0]*c[2]
 d=factor*c[1]*c[1]
 e=factor*c[1]*c[2]
 f=factor*c[2]*c[2]
 er=factor*sum(r*r for r in rad)
 return (a,b,cc,d,e,f,er)
def group(data,indices):
 return tuple(sum((data[i][k] for i in indices),Q(0)) for k in range(7))
def exact(data,ids,source_norm):
 tr,e2,det,L,E=gram_data(group(data,ids))
 passed=L>E and L>0
 const=(L-E)**2/(4*L*source_norm) if passed else None
 assert not passed or const>0
 return {
  "original_physical_cell_indices":list(ids),
  "true_original_selected_cell_count":len(ids),
  "center_gram_00":str(group(data,ids)[0]),
  "center_gram_01":str(group(data,ids)[1]),
  "center_gram_02":str(group(data,ids)[2]),
  "center_gram_11":str(group(data,ids)[3]),
  "center_gram_12":str(group(data,ids)[4]),
  "center_gram_22":str(group(data,ids)[5]),
  "center_3D_second_elementary_symmetric":str(e2),
  "center_3D_exact_determinant":str(det),
  "center_3D_min_eigenvalue_rational_lower":str(L),
  "original_physical_mean_error_Frobenius_sq_upper":str(E),
  "exact_3D_singular_gap_positive":passed,
  "restricted_true_original_source_3D_coercivity":str(const) if passed else None,
  "all_unmeasured_true_original_action_frequency_energy_PSD":True,
  "no_global_24D_strong_source_Loewner_claim":True
 }
def ff(x):
 try:return float(x)
 except OverflowError:return float("inf") if x>0 else float("-inf")
def float_gram(z):
 a,b,c,d,e,f,er=z
 tr=a+d+f
 e2=(a*d-b*b)+(a*f-c*c)+(d*f-e*e)
 det=a*(d*f-e*e)-b*(b*f-c*e)+c*(b*e-c*d)
 L=max(0.0,det/e2) if e2>0 and det>0 else 0.0
 return L-er,L/max(er,1e-250)
def heuristic(data):
 fp=[tuple(ff(x) for x in row) for row in data]
 seeds=[]
 # Numerics propose only. Never accept positivity or numerical rank.
 # Include two-thirds of physical span selected by prior 2D results.
 for i in range(55):
  for j in range(i+1,55):
   for k in range(j+1,55):
    z=tuple(fp[i][q]+fp[j][q]+fp[k][q] for q in range(7))
    gap,ratio=float_gram(z)
    if math.isfinite(gap) and math.isfinite(ratio):
     seeds.append((gap,ratio,i,j,k))
 seeds.sort(reverse=True)
 ratios=sorted(seeds,key=lambda x:(x[1],x[0]),reverse=True)
 origins=list(dict.fromkeys((x[2],x[3],x[4]) for x in (
  seeds[:3]+ratios[:3])))
 origins.extend([(1,11,20),(2,12,22),(11,14,22)])
 origins=list(dict.fromkeys(tuple(sorted(i)) for i in origins))
 assert origins
 pool={n:[] for n in TARGET_SIZES}
 for triple in origins:
  chosen=list(triple)
  summed=[sum(fp[i][q] for i in chosen) for q in range(7)]
  pool[3].append(tuple(chosen))
  while len(chosen)<max(TARGET_SIZES):
   left=(k for k in range(55) if k not in chosen)
   nextid=max(left,key=lambda k:(
     *float_gram(tuple(summed[q]+fp[k][q] for q in range(7))),-k))
   chosen.append(nextid)
   summed=[summed[q]+fp[nextid][q] for q in range(7)]
   if len(chosen) in pool:
    pool[len(chosen)].append(tuple(sorted(chosen)))
 for n in TARGET_SIZES:
  pool[n]=list(dict.fromkeys(pool[n]))
 return pool
def main():
 p=argparse.ArgumentParser()
 for k in ("mg24","mg57","mg58","mg63"):
  p.add_argument("--verified-"+k+"-json",required=True)
 p.add_argument("--output",default="artifacts/mg64_original_three_source_Jensen.json")
 args=p.parse_args()
 input={k:json.loads((ROOT/getattr(args,"verified_"+k+"_json")).read_text())
       for k in ("mg24","mg57","mg58","mg63")}
 assert all(z["canonical_W_ODD_NEG"]=="OPEN" for z in input.values())
 assert input["mg63"]["status"]=="ORIGINAL_MG63_GENUINE_E5_MULTICELL_JENSEN_2D_SOURCE"
 assert input["mg63"]["coordinate5_positive_source_plane_certified"]
 cells=m62.source55(input["mg57"],input["mg58"])
 assert len(cells)==55 and cells[0][0]==0 and cells[-1][1]==4
 assert all(cells[i][1]==cells[i+1][0] for i in range(54))
 H,Rad,err=original_H24_from_physical_source()
 assert err==Q(input["mg24"]["physical_Gram_Loewner_row_error"])
 b=[H[k][P] for k in range(N)]
 brad=[Rad[k][P] for k in range(N)]
 e5=tuple(Q(i==5) for i in range(N))
 assert m59.dot(e5,V)==0
 allcases=[];positive=[]
 for j in THIRD_AXES:
  ej=tuple(Q(k==j) for k in range(N))
  for alpha in ANCHOR_SCALES:
   for beta in THIRD_SCALES:
    u=tuple(alpha*x for x in V)
    third=tuple(beta*x for x in ej)
    vectors=(u,e5,third)
    source_norm=sum(m59.dot(v,v) for v in vectors)
    assert source_norm>0 and j!=5
    source_gram=[
     [m59.dot(vectors[x],vectors[y]) for y in range(3)]
     for x in range(3)]
    # This plane genuinely has 3 independent vectors. Check
    # exact rational gram determinant, NOT unverified float rank.
    a,bg,c=source_gram[0];d=source_gram[1][1];e=source_gram[1][2];f=source_gram[2][2]
    determinant=a*(d*f-e*e)-bg*(bg*f-c*e)+c*(bg*e-c*d)
    assert determinant>0
    data=[proj_three(cell,vectors,b,brad) for cell in cells]
    proposals=heuristic(data)
    archive=[]
    for n in TARGET_SIZES:
     tests=[exact(data,ids,source_norm) for ids in proposals[n]]
     success=[r for r in tests if r["exact_3D_singular_gap_positive"]]
     if success:
      chosen=max(success,key=lambda r:Q(r["restricted_true_original_source_3D_coercivity"]))
     else:
      chosen=max(tests,key=lambda r:Q(r["center_3D_min_eigenvalue_rational_lower"])
                                 -Q(r["original_physical_mean_error_Frobenius_sq_upper"]))
     archive.append({
      "subset_size":n,
      "number_exact_candidate_subsets_tested":len(tests),
      "number_exact_positive_subsets":len(success),
      "best_exact_source_3D_subset":chosen})
    good=[r for r in archive if r["number_exact_positive_subsets"]>0]
    allcases.append({
     "original_source_third_coordinate":j,
     "physical_anchor_alpha":str(alpha),
     "physical_third_beta":str(beta),
     "original_source_coefficient_Gram":[[str(z) for z in row] for row in source_gram],
     "original_source_coefficient_Gram_determinant":str(determinant),
     "source_basis_three_vector_normtrace":str(source_norm),
     "tested_original_physical_subset_sizes":list(TARGET_SIZES),
     "positive_source_three_plane":bool(good),
     "best_certificate_per_subset_size":archive})
    for row in good:
     positive.append((j,alpha,beta,row["best_exact_source_3D_subset"]))
    if j in (0,11,23):
     print("MG64 physical original three-source Jensen",{
      "coordinate":j,"alpha":str(alpha),"beta":str(beta),
      "passed_sizes":[r["subset_size"] for r in good]},flush=True)
 selected=max(positive,key=lambda x:Q(x[3]["restricted_true_original_source_3D_coercivity"])) if positive else None
 result={
  "status":"ORIGINAL_MG64_GENUINE_PHYSICAL_THREE_SOURCE_JENSEN_SINGULAR_GAP",
  "canonical_W_ODD_NEG":"OPEN",
  "accepted_true_original_source_runs":{"MG24":39378465438,"MG57":39897754515,
                                      "MG58":39902364126,"MG63":39997475198},
  "original_SI10_MG11_23adapted_plus_true_sinh_pole":True,
  "original_signed_sevenprime_digamma_multiplier_unchanged":True,
  "true_physical_pole_corrected_strong_action_unchanged":True,
  "true_positive_physical_frequency_domain":["0","4"],
  "original_genuine_physical_Fourier_cell_count":55,
  "negative_original_Fourier_mirror_counted":True,
  "unselected_physical_strong_action_frequency_energy_PSD":True,
  "float_only_proposes_original_cell_subsets":True,
  "three_source_exact_rational_singular_acceptance_only":True,
  "trial_source_coordinate_axes":list(THIRD_AXES),
  "trial_original_source_plane_count":len(allcases),
  "three_dimensional_strict_source_moment_certified":bool(positive),
  "best_third_original_coordinate":selected[0] if selected else None,
  "best_original_anchor_alpha":str(selected[1]) if selected else None,
  "best_original_third_beta":str(selected[2]) if selected else None,
  "best_strict_restricted_source3D_coercivity":selected[3]["restricted_true_original_source_3D_coercivity"] if selected else None,
  "best_original_three_source_physical_cell_indices":selected[3]["original_physical_cell_indices"] if selected else None,
  "original_full24_strong_action_coercivity":False,
  "original_source24_residual_contraction":False,
  "original_full470_inverse":False,
  "odd_signed_51over56":False,
  "independent_original_Fourier_form_domain_audit":"OPEN",
  "even_Weil_CC27_RH":"OPEN",
  "cases":allcases}
 dest=ROOT/args.output;dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(result,indent=2)+"\n")
 print("MG64 original true physical three-source exact Jensen certificate finished",{
  "trial_source_planes":len(allcases),
  "three_dimensional_source_strong_positive":bool(positive),
  "best_coordinate":result["best_third_original_coordinate"],
  "full24_RH":"OPEN"},flush=True)
if __name__=="__main__":main()
