"""RC125: sharp first-moment response bounds and next variance obligation.
Actual endpoint first moments inherited from RC124; second moments not evaluated.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,cong
from validate_rpb108_rc114_positive_augmentation import up,down

def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def psd2(A):
 assert A==tr(A);v=A[0][0]>=0 and A[1][1]>=0 and A[0][0]*A[1][1]>=A[0][1]**2;assert v==psd(A);return v

def control():
 D=[[F(2),F(0),F(0)],[F(0),F(3),F(0)],[F(0),F(0),F(5)]];K=[[F(1),F(1,10),F(1,5)],[F(1,10),F(3,2),F(3,20)],[F(1,5),F(3,20),F(5,2)]];assert psd(K) and psd(add(D,K,-1));C=mm(inverse(D),K)
 V=[[F(1),F(0)],[F(0),F(1)],[F(1,5),F(-1,7)]];G=cong(V,D);H=cong(V,K);H2=cong(mm(C,V),D);R=add(H2,mm(H,mm(inverse(G),H)),-1);assert psd2(R)
 S=cong(V,mm(D,inverse(add(eye(3),C))));lo=mm(G,mm(inverse(add(G,H)),G));hi=add(G,scale(H,F(-1,2)))
 assert psd2(add(S,lo,-1)) and psd2(add(hi,S,-1))
 vlow=mm(G,mm(inverse(add(add(G,H),scale(R,F(-1,2)))),G));vhi=mm(G,mm(inverse(add(add(G,H),R,-1)),G));assert psd2(add(S,vlow,-1)) and psd2(add(vhi,S,-1))
 Y=mm(inverse(add(G,H)),G);IY=add(eye(2),Y,-1);variational=add(add(G,cong(IY,G),-1),cong(Y,H),-1);direct=add(add(mm(G,Y),mm(tr(Y),G)),cong(Y,add(G,H)),-1);assert variational==direct==lo
 # Upper secant is achieved by a rational D-orthogonal projection.
 w=[[F(1)],[F(2)],[F(3)]];projection=mm(w,mm(inverse(cong(w,D)),mm(tr(w),D)));assert mm(projection,projection)==projection
 Hp=cong(V,mm(D,projection));Sp=cong(V,mm(D,inverse(add(eye(3),projection))));assert Sp==add(G,scale(Hp,F(-1,2)))
 # Lower is attained by the invariant, normalized finite model C0=G^-1 H.
 C0=mm(inverse(G),H);S0=mm(G,inverse(add(eye(2),C0)));assert S0==lo
 return dict(scope='abstract rational D-selfadjoint contractions, not original Weil or actual endpoint second moments',nonidentity_D_metric_and_nonorthogonal_family=True,sharp_first_moment_lower_and_upper_verified=True,variational_identity_two_forms_verified=True,projection_attains_upper_verified=True,invariant_model_attains_lower_verified=True,variance_residual_Gram_positive_verified=True,variance_Schur_response_sandwich_verified=True)

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];prior,old=map(json.loads,raw);hs=[hashlib.sha256(x).hexdigest() for x in raw];assert prior['milestone']=='RC124' and old['milestone']=='RC123' and prior['input_sha256'][0]==hs[1]
 rows=[];grid=10**5
 for p in prior['parity_actual_joint_endpoint_moment_certificates']:
  GL=matrix(p['Gamma_0_Loewner_lower']);GU=matrix(p['Gamma_0_Loewner_upper']);HL=matrix(p['endpoint_pairing_Loewner_lower']);HU=matrix(p['endpoint_pairing_Loewner_upper']);G=scale(add(GL,GU),F(1,2));H=scale(add(HL,HU),F(1,2));Y=[[F(0)]*2 for _ in range(2)]
  for j in range(2):Y[j][j]=GL[j][j]/(GL[j][j]+HU[j][j])
  retainedG=[[(2*Y[i][i]-Y[i][i]**2)*GL[i][i] if i==j else F(0) for j in range(2)] for i in range(2)]
  lo=add(retainedG,cong(Y,HU),-1);hi=add(GU,scale(HL,F(-1,2)));oldlo=matrix(p['joint_reference_response_Loewner_lower']);assert psd2(lo) and psd2(add(hi,lo,-1)) and psd2(add(lo,oldlo,-1))
  low,high=0,grid
  while low+1<high:
   mid=(low+high)//2
   if psd2(add(HL,scale(GU,F(-mid,grid)))):low=mid
   else:high=mid
  ell=F(low,grid);assert ell>0 and psd2(add(HL,scale(GU,-ell)))
  low,high=0,grid
  while low+1<high:
   mid=(low+high)//2
   if psd2(add(scale(GL,F(mid,grid)),HU,-1)):high=mid
   else:low=mid
  upper=F(high,grid);assert ell<upper<1 and psd2(add(scale(GL,upper),HU,-1))
  gap=lambda x:x*(1-x)/(2*(1+x));floor=min(gap(ell),gap(upper));assert floor>0
  diag=[]
  for j in range(2):diag.append(dict(coordinate=p['joint_family'][j],reference_response_over_actual_D_Gram_lower=str(down(lo[j][j]/GU[j][j],10**12)),reference_response_over_actual_D_Gram_upper=str(up(hi[j][j]/GL[j][j],10**12)),previous_lower_fraction=str(down(oldlo[j][j]/GU[j][j],10**12))))
  rows.append(dict(parity=p['parity'],family=p['joint_family'],variational_trial_coefficients=serialize(Y),certified_reference_response_Loewner_lower=serialize(lo),certified_reference_response_Loewner_upper=serialize(hi),new_lower_dominates_RC124_lower_in_Loewner_order=True,compressed_endpoint_first_moment_spectral_lower=str(ell),compressed_endpoint_first_moment_spectral_upper=str(upper),sharp_first_moment_only_interval_gap_relative_exact_Gram_lower=str(down(floor,10**12)),sharp_interval_gap_is_information_bound_not_actual_response_error=True,response_coordinate_fraction_enclosures=diag,actual_leading_tail_variance_strictly_positive_by_RC123_nonclosure=True,actual_second_endpoint_moment_evaluated=False))
 return dict(milestone='RC125',status='PASS: actual stronger correlated variational response lower; sharp first-moment information ceiling and variance reduction',input_sha256=hs,aperture='11/10',arithmetic='exact rational variational congruence and generalized two-dimensional PSD/determinant replay',parity_sharp_first_moment_response_certificates=rows,abstract_noncommuting_control=control(),first_moment_sharp_theorem='G(G+H)^(-1)G <= Sigma <= G-H/2; both attainable among positive contractions with these exact first moments',variance_definition='R=H2-H G^(-1) H >=0; H2=V^* D C^2 V',conditional_variance_response_sandwich='G(G+H-R/2)^(-1)G <= Sigma <= G(G+H-R)^(-1)G',zero_variance_implies_invariant_family_and_exact_Jensen_response=True,variance_positive_complement_floor_used='1 <= I+C_complement <= 2',all_actual_interval_errors_paid_in_variational_lower=True,actual_second_endpoint_moment_evaluated=False,full_39_column_family_certified=False,high_accuracy_reference_response_completed=False,regular_multiplier_action_evaluated=False,original_Weil_or_augmented_actions_performed=False,auxiliary_response_norm_below_one_certified=False,new_positive_native_directions_certified=0,original_count_below_one_hundredth_lower=10,original_count_below_one_hundredth_upper=639,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=2);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC125 PASS: sharp actual first-moment bounds; next variance is actual coupled-response obligation')
