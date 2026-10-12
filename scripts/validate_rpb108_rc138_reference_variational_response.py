"""RC138: direct reference inverse response with correlated action trials."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
from validate_rpb108_rc127_enriched_even_endpoint_action import down,up,sqrtup,psd,ser
from validate_rpb108_rc129_four_vector_joint_moment import inv,mm,transpose,cong,add

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];action,joint,common,balanced,response,baseline=map(json.loads,raw)
 hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [x['milestone'] for x in (action,joint,common,balanced,response,baseline)]==['RC137','RC136','RC135','RC132','RC128','RC130']
 assert action['input_sha256'][0]==hs[1] and action['input_sha256'][1]==hs[2] and action['input_sha256'][4]==hs[3] and action['input_sha256'][6]==hs[5] and action['input_sha256'][8]==hs[4]
 assert action['full_seven_input_covariance_upper_certified'] and action['RC134_projection_action_rounding_gap_audited']
 def mat(key):return [[F(x) for x in row] for row in joint[key]]
 GL=mat('actual_D_Gram_entry_lower');GU=mat('actual_D_Gram_entry_upper');GM=[[(GL[i][j]+GU[i][j])/2 for j in range(7)] for i in range(7)]
 GLo=mat('actual_D_Gram_Loewner_lower');GHi=mat('actual_D_Gram_Loewner_upper')
 HL=mat('actual_endpoint_pairing_entry_lower');HU=mat('actual_endpoint_pairing_entry_upper')
 alpha=F(balanced['alpha']);alo=HL[0][0]/GU[0][0];ahi=HU[0][0]/GL[0][0];a=down((alo+ahi)/2)
 # Trial source frame: P0, f, B=w-alpha*psi, u=(v+z)/2, t.
 S=[[F(0)]*5 for _ in range(7)];S[0][0]=1;S[2][1]=1;S[3][2]=1;S[1][2]=-alpha;S[4][3]=S[5][3]=F(1,2);S[6][4]=1
 # Approximated actions are paid in the full carrier norm before projection.
 T=[[F(0)]*5 for _ in range(7)];T[0][0]=a;T[1][0]=T[2][0]=1;T[3][1]=1;T[5][2]=1;T[6][3]=1
 for i in range(7):T[i][4]=F(action['Ct_trial_coefficients'][i])
 eps=[max(a-alo,ahi-a)*sqrtup(GU[0][0]),F(response['collective_response_enrichment_budgets'][2]['full_Cf0_approximation_D_norm_error_upper']),F(balanced['balanced_action_and_shared_covariance_budgets'][1]['shared_residual_difference_D_norm_upper']),F(common['collective_capture_budgets'][1]['full_common_action_trial_D_norm_error_upper']),F(action['full_Ct_trial_D_norm_error_upper'])]
 pairs=[(i,j) for i in range(7) for j in range(7)];pairs=pairs[::-1] if replay else pairs
 def bil(x,y,L,U):
  lo=hi=F(0)
  for i,j in pairs:
   c=x[i]*y[j];lo+=c*(L[i][j] if c>=0 else U[i][j]);hi+=c*(U[i][j] if c>=0 else L[i][j])
  return lo,hi
 scols=transpose(S);tcols=transpose(T);norms=[sqrtup(cong([[x] for x in s],GHi)[0][0]) for s in scols]
 HSL=[[F(0)]*5 for _ in range(5)];HSU=[[F(0)]*5 for _ in range(5)]
 for i in range(5):
  for j in range(i,5):
   lo,hi=bil(scols[i],scols[j],HL,HU)
   # Intersect both action directions. B eliminates the leading Cpsi action.
   for acted,other in ((i,j),(j,i)):
    l,u=bil(tcols[acted],scols[other],GL,GU);e=eps[acted]*norms[other]
    lo=max(lo,l-e);hi=min(hi,u+e)
   assert lo<=hi
   HSL[i][j]=HSL[j][i]=lo;HSU[i][j]=HSU[j][i]=hi
 candidates=[]
 for count in (3,4,5):
  SS=[row[:count] for row in S];TT=[row[:count] for row in T];K=add(SS,TT)
  Q=cong(K,GM);assert psd(Q)
  rhs=mm(transpose(K),[[GM[i][0]] for i in range(7)])
  coefficients=[down(row[0],10**20) for row in mm(inv(Q),rhs)]
  y=mm(SS,[[x] for x in coefficients]);yc=[row[0] for row in y]
  residual=mm(K,[[x] for x in coefficients]);residual[0][0]-=1
  nominalResidual=cong(residual,GHi)[0][0];assert nominalResidual>=0
  actionError=sum(abs(coefficients[i])*eps[i] for i in range(count))
  fullResidual=up(sqrtup(nominalResidual)+actionError);residualEnergy=up(fullResidual*fullResidual,10**100)
  pL,pU=bil([F(i==0) for i in range(7)],yc,GL,GU)
  gramL=cong(y,GLo)[0][0];gramU=cong(y,GHi)[0][0]
  hL=hU=F(0)
  order=[(i,j) for i in range(count) for j in range(count)];order=order[::-1] if replay else order
  for i,j in order:
   c=coefficients[i]*coefficients[j];hL+=c*(HSL[i][j] if c>=0 else HSU[i][j]);hU+=c*(HSU[i][j] if c>=0 else HSL[i][j])
  lower=2*pL-gramU-hU;upper=2*pU-gramL-hL+residualEnergy
  assert 0<lower<=upper
  candidates.append(dict(trial_frame_count=count,trial_frame_coefficients=list(map(str,coefficients)),source_seven_vector_coefficients=list(map(str,yc)),nominal_operator_residual_source_coefficients=[str(row[0]) for row in residual],nominal_operator_residual_D_energy_upper=str(nominalResidual),paid_full_action_error_D_norm_upper=str(actionError),full_IplusC_trial_residual_D_norm_upper=str(fullResidual),full_IplusC_trial_residual_D_energy_upper=str(residualEnergy),P0_trial_pairing_lower=str(pL),P0_trial_pairing_upper=str(pU),trial_D_Gram_lower=str(gramL),trial_D_Gram_upper=str(gramU),trial_endpoint_energy_lower=str(hL),trial_endpoint_energy_upper=str(hU),variational_functional_lower=str(lower),variational_functional_upper=str(2*pU-gramL-hL),reference_response_absolute_lower=str(lower),reference_response_absolute_upper=str(upper),normalized_reference_response_lower=str(down(lower/GU[0][0],10**12)),normalized_reference_response_upper=str(up(upper/GL[0][0],10**12))))
 old=baseline['reference_response_coordinate_enclosures'][0]
 oldLower=F(old['reference_response_over_own_D_Gram_lower']);oldUpper=F(old['best_coordinate_upper_from_separate_valid_bounds'])
 lower=max([oldLower]+[F(x['normalized_reference_response_lower']) for x in candidates]);upper=min([oldUpper]+[F(x['normalized_reference_response_upper']) for x in candidates]);assert oldLower<lower<upper<oldUpper
 width=upper-lower;improvement=down((oldUpper-oldLower)/width,10**6);assert improvement>200
 selectedLower=max(candidates,key=lambda x:F(x['normalized_reference_response_lower']))['trial_frame_count']
 selectedUpper=min(candidates,key=lambda x:F(x['normalized_reference_response_upper']))['trial_frame_count']
 controls=[]
 for lam in (F(0),F(1,4),F(1,2),F(1)):
  for yy in (F(0),F(1,3),F(-2,5)):
   exact=1/(1+lam);L=2*yy-(1+lam)*yy*yy;r=((1+lam)*yy-1)**2
   assert L+r/2<=exact<=L+r
   controls.append(dict(C_eigenvalue=str(lam),signed_trial=str(yy),variational_residual_identity_and_endpoint_bounds_verified=True))
 return dict(milestone='RC138',status='PASS: narrower P0 reference inverse interval from fully paid direct variational trials',starting_commit='3fb7af434df933b3c2fae985b5787adf01072786',input_sha256=hs,aperture='11/10',carrier_family=joint['joint_family'],carrier_family_dimension=7,new_family_vectors_added=0,trial_frame=['P0','f0','w14-alpha*psi0','(v10+z_b6)/2','t10'],trial_source_matrix=ser(S),trial_action_approximation_matrix=ser(T),trial_action_D_norm_error_upper=list(map(str,eps)),trial_frame_endpoint_entry_lower=ser(HSL),trial_frame_endpoint_entry_upper=ser(HSU),candidate_reference_trials=candidates,normalized_P0_reference_response_lower=str(lower),normalized_P0_reference_response_upper=str(upper),normalized_P0_reference_response_interval_width=str(width),previous_RC130_normalized_P0_lower=str(oldLower),previous_RC130_normalized_P0_upper=str(oldUpper),previous_width_over_new_width_lower=str(improvement),selected_lower_trial_frame_count=selectedLower,selected_upper_trial_frame_count=selectedUpper,analytic_action_cancellation_exact=True,all_infinite_action_errors_paid_before_projection=True,center_matrices_used_only_to_choose_trials=True,acceptance_uses_actual_Gram_endpoint_and_action_error_enclosures=True,global_IplusC_inverse_variational_residual_bound_used=True,uniform_numerical_Schur_lower_psd_required=False,full_seven_input_covariance_inherited=True,reference_P0_inverse_interval_improved=True,high_accuracy_reference_inverse_completed=False,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,exact_rational_variational_controls=controls,next_cursor='tighten common-source and t endpoint energies and direct trial residual; test the required reference-response tolerance before original source transport')

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=6);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC138 PASS: direct P0 reference inverse interval improved')
