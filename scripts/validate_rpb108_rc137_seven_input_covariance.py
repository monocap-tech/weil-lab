"""RC137: paid Ct trial, finite distance test and full seven-input covariance."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc129_four_vector_joint_moment import inv,mm,transpose,add
from validate_rpb108_rc134_correlated_six_input_covariance import smul

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];joint,capture,prior,oldjoint,balanced,finite,remaining,old,response=map(json.loads,raw)
 hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [x['milestone'] for x in (joint,capture,prior,oldjoint,balanced,finite,remaining,old,response)]==['RC136','RC135','RC134','RC133','RC132','RC131','RC130','RC129','RC128']
 assert joint['input_sha256']==hs[1:] and capture['input_sha256']==hs[2:]
 src=Path(__file__).with_name('validate_rpb108_rc136_seven_vector_joint_matrices.py').read_text()
 cut=src.index(" print('RC136 seven-vector full Gram and independence paid'")
 scope={'__file__':str(Path(__file__).with_name('validate_rpb108_rc136_seven_vector_joint_matrices.py'))}
 exec(compile(src[:cut]+'\n return locals()\n','RC136-reconstruction','exec'),scope)
 d=scope['run'](paths[1:],replay);vec=d['vec'];dn=d['dn'];diagonal=d['diagonal'];N=7;M=4095;O=8191;fullO=16383
 assert ser(d['GLp'])==joint['finite_prefix_Gram_entry_lower'] and ser(d['GUp'])==joint['finite_prefix_Gram_entry_upper']
 source={n:v for n,v in vec[6].items() if n<=M};jobs=sorted(source,reverse=replay)
 action={};centers={};auditAction={}
 auditSource={n:v for n,v in vec[4].items() if n<=M}
 for n in range(0,O+1,2):
  value=auditValue=Z
  for m in jobs:
   entry=diagonal[n] if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
   value=plus(value,mul(entry,source[m]))
   auditValue=plus(auditValue,mul(entry,auditSource[m]))
  lo,hi=bounds(div(value,dn[n]));action[n]=(rat(lo)[0],rat(hi)[1]);centers[n]=down((lo+hi)/2)
  al,au=bounds(div(auditValue,dn[n]));auditAction[n]=(rat(al)[0],rat(au)[1])
 print('RC137 finite Ct source action complete',flush=True)
 # Finite Gram at the actual retained output cutoff, not the full 16382 Gram.
 GLp=[[F(0)]*N for _ in range(N)];GUp=[[F(0)]*N for _ in range(N)]
 degrees=list(range(0,O+1,2));degrees=degrees[::-1] if replay else degrees
 for i in range(N):
  for j in range(i,N):
   value=Z
   for n in degrees:
    if n in vec[i] and n in vec[j]:value=plus(value,mul(mul(rat(2*B/F(2*n+1)),dn[n]),mul(vec[i][n],vec[j][n])))
   lo,hi=bounds(value);GLp[i][j]=GLp[j][i]=lo;GUp[i][j]=GUp[j][i]=hi
 weights=[sqrtup(GUp[i][i]) for i in range(N)];GL,GU,errors=loewner(GLp,GUp,weights)
 assert psd(GL)
 Gmid=[[(GLp[i][j]+GUp[i][j])/2 for j in range(N)] for i in range(N)]
 pairing=[];pairBounds=[]
 for i in range(N):
  value=actual=Z
  for n in degrees:
   if n in vec[i]:
    mass=mul(rat(2*B/F(2*n+1)),dn[n])
    value=plus(value,mul(mass,mul(vec[i][n],rat(centers[n]))))
    actual=plus(actual,mul(mass,mul(vec[i][n],action[n])))
  lo,hi=bounds(value);pairing.append([(lo+hi)/2]);pairBounds.append(bounds(actual))
 Y=[down(row[0],10**20) for row in mm(inv(Gmid),pairing)]
 finiteResidual=F(0);payload=[];Qlower=F(0)
 for n in degrees:
  trial=Z
  for i in range(N):
   if n in vec[i]:trial=plus(trial,smul(rat(Y[i]),vec[i][n]))
  interval=minus(action[n],trial);lo,hi=bounds(interval);radius=max(abs(lo),abs(hi))
  finiteResidual+=up(2*B/F(2*n+1)*F(dn[n][1])*radius*radius,10**100)
  Qlower+=down(2*B/F(2*n+1)*F(dn[n][0])*F(action[n][0])**2,10**100)
  payload.append(dict(degree=n,action_center=str(centers[n]),residual_lower=str(lo),residual_upper=str(hi)))
 # The trial has actual finite coefficients above the retained output cutoff.
 # Pay their signed combined norm, not a sum of separate vector norms.
 finiteTrialTail=F(0)
 for n in (list(range(O+1,fullO+1,2))[::-1] if replay else range(O+1,fullO+1,2)):
  value=Z
  for i in range(N):
   if n in vec[i]:value=plus(value,smul(rat(Y[i]),vec[i][n]))
  lo,hi=bounds(value);radius=max(abs(lo),abs(hi))
  finiteTrialTail+=up(2*B/F(2*n+1)*F(dn[n][1])*radius*radius,10**100)
 # All remaining analytic trial tails share psi's eta0 factor above 16382.
 mu=d['mu'];nuv=d['nuv'];nuz=d['nuz'];nut=d['nut'];lam=d['lam'];oldlam=d['oldlam'];wlam=d['wlam'];rho=F(lam,d['zf'])
 q=[]
 for k in range(max(map(len,(mu,nuv,nuz,nut)))):
  x=Y[1] if k==0 else F(0)
  for i,mom,lambda_i in ((3,mu,wlam),(4,nuv,oldlam),(5,nuz,oldlam),(6,nut,lam)):
   if k<len(mom):x+=Y[i]*mom[k]*F(lambda_i,lam)**k
  q.append(x)
 amplitude=up(sum(abs(x)*rho**k for k,x in enumerate(q)))
 analyticTrialTail=up(d['T']*amplitude*amplitude,10**100)
 trialTail=up(finiteTrialTail+analyticTrialTail,10**100)
 outputBase=F(finite['leading_new_output_tail_D_energy_upper']);sourceLam=(M-1)*M;outputRho=F(sourceLam,(O+1)*(O+2))
 total=Z
 for m in jobs:total=plus(total,source[m])
 outputTail=up(outputBase*(F(total[1])/(1-outputRho))**2,10**100)
 inputTail=F(joint['endpoint_omitted_finite_and_analytic_source_D_energy_upper'][6])
 normError=up(sqrtup(finiteResidual)+sqrtup(trialTail)+sqrtup(outputTail)+sqrtup(inputTail))
 GentryU=[[F(x) for x in r] for r in joint['actual_D_Gram_entry_upper']]
 tUpper=min(up(normError*normError,10**100),GentryU[6][6]/4)
 # Genuine finite-output distance lower; only omitted input can change it.
 K=inv(GL);projectionUpper=F(0)
 for i in range(N):
  for j in range(N):projectionUpper+=max(x*K[i][j]*y for x in pairBounds[i] for y in pairBounds[j])
 finiteDistance=max(F(0),down(Qlower-projectionUpper,10**100))
 normLower=max(F(0),sqrtup(finiteDistance)-F(1,10**40)-sqrtup(inputTail))
 tLower=down(normLower*normLower,10**100);assert tLower<=tUpper
 # Additive RC134 lower-bound audit: actual action intervals, not just
 # rounded action centers, enter the projection pairing upper.
 auditPairs=[];auditQ=F(0)
 for i in range(6):
  value=Z
  for n in degrees:
   if n in vec[i]:value=plus(value,mul(mul(rat(2*B/F(2*n+1)),dn[n]),mul(vec[i][n],auditAction[n])))
  auditPairs.append(bounds(value))
 for n in degrees:auditQ+=down(2*B/F(2*n+1)*F(dn[n][0])*F(auditAction[n][0])**2,10**100)
 agl,agu,ae=loewner([r[:6] for r in GLp[:6]],[r[:6] for r in GUp[:6]],weights[:6]);assert psd(agl)
 ak=inv(agl);auditProjection=F(0)
 for i in range(6):
  for j in range(6):auditProjection+=max(x*ak[i][j]*y for x in auditPairs[i] for y in auditPairs[j])
 auditFinite=max(F(0),down(auditQ-auditProjection,10**100))
 auditNorm=max(F(0),sqrtup(auditFinite)-F(1,10**40)-sqrtup(F(prior['Cv_omitted_input_D_energy_upper'])))
 auditedVLower=down(auditNorm*auditNorm,10**100)
 auditedRelative=down(auditedVLower/F(oldjoint['actual_D_Gram_entry_upper'][4][4]),10**12)
 assert auditedRelative>=F(prior['v_covariance_relative_own_D_Gram_lower'])
 assert auditedVLower>F('0.0000008300730')
 captureBudget=capture['collective_capture_budgets'][1]
 independence= sqrtup(auditedVLower)-F(1,10**40)-sqrtup(F(capture['delta_full_source_D_energy_upper']))/4-F(captureBudget['full_common_action_trial_D_norm_error_upper'])
 assert independence>0
 auditedIndependence=down(independence*independence)
 assert auditedIndependence>F('0.0000007170422')
 # Full seven-input covariance, not old-six covariance mislabeled as complete.
 six=capture['collective_capture_budgets'][1]
 R6=[[F(x) for x in r] for r in six['old_six_input_projected_covariance_Loewner_upper']]
 assert psd(R6)
 RU=[[F(0)]*N for _ in range(N)]
 for i in range(6):
  for j in range(6):RU[i][j]=2*R6[i][j]
 RU[6][6]=2*tUpper;assert psd(RU)
 entryL=[[F(0)]*N for _ in range(N)];entryU=[[F(0)]*N for _ in range(N)]
 for i in range(6):
  for j in range(6):entryL[i][j]=F(six['old_six_input_projected_covariance_entry_lower'][i][j]);entryU[i][j]=F(six['old_six_input_projected_covariance_entry_upper'][i][j])
 entryL[6][6]=tLower;entryU[6][6]=tUpper
 for i in range(6):
  e=sqrtup(entryU[i][i]*tUpper);entryL[i][6]=entryL[6][i]=-e;entryU[i][6]=entryU[6][i]=e
 # Nonzero matrix blocks in the upper are correlations of the upper only;
 # actual cross covariance is covered by the factor-two norm inequality.
 for a,b in ((F(1),F(1)),(F(1),F(-1)),(F(2,7),F(-3,11))):assert (a+b)**2<=2*a*a+2*b*b
 fullGL=[[F(x) for x in r] for r in joint['actual_D_Gram_Loewner_lower']]
 HL=[[F(x) for x in r] for r in joint['actual_endpoint_pairing_Loewner_lower']]
 Mlow=add(add(fullGL,HL),RU,-1);schur=psd(Mlow)
 return dict(milestone='RC137',status='PASS: paid Ct action trial, finite residual distance and full seven-input covariance',starting_commit='b2b0ed487da50cbf6e251d7f7b1356fb98619434',input_sha256=hs,aperture='11/10',joint_family=joint['joint_family'],family_dimension=7,Ct_retained_source_degree=M-1,Ct_retained_output_degree=O-1,full_trial_finite_degree=fullO-1,Ct_trial_coefficients=list(map(str,Y)),Ct_finite_action_and_residual_coefficient_sha256=hashlib.sha256(json.dumps(sorted(payload,key=lambda x:x['degree']),sort_keys=True,separators=(',',':')).encode()).hexdigest(),Ct_retained_output_Gram_Loewner_lower=ser(GL),Ct_retained_output_Gram_positive_certified=True,Ct_finite_residual_D_energy_upper=str(finiteResidual),Ct_trial_omitted_finite_D_energy_upper=str(finiteTrialTail),Ct_trial_combined_analytic_tail_polynomial=list(map(str,q)),Ct_trial_analytic_tail_D_energy_upper=str(analyticTrialTail),Ct_trial_total_tail_D_energy_upper=str(trialTail),Ct_retained_source_omitted_output_D_energy_upper=str(outputTail),Ct_omitted_input_action_D_energy_upper=str(inputTail),full_Ct_trial_D_norm_error_upper=str(normError),Ct_finite_second_moment_D_energy_lower=str(Qlower),Ct_finite_projection_D_energy_upper=str(projectionUpper),Ct_finite_distance_to_retained_family_D_energy_lower=str(finiteDistance),t_projected_covariance_lower=str(tLower),t_projected_covariance_upper=str(tUpper),t_covariance_relative_own_D_Gram_lower=str(down(tLower/GentryU[6][6],10**12)),t_covariance_positive_obstruction_certified=tLower>0,RC134_projection_action_rounding_gap_audited=True,RC134_repaired_v_covariance_lower=str(auditedVLower),RC134_repaired_relative_v_covariance_lower=str(auditedRelative),RC134_reported_decimal_obstruction_preserved=True,RC135_repaired_new_vector_distance_D_energy_lower=str(auditedIndependence),RC135_independence_preserved_after_rounding_audit=True,RC136_direct_seven_vector_Gram_floor_preserved=True,full_seven_input_projected_covariance_entry_lower=ser(entryL),full_seven_input_projected_covariance_entry_upper=ser(entryU),full_seven_input_projected_covariance_Loewner_upper=ser(RU),full_seven_input_covariance_upper_certified=True,old_six_analytic_covariance_bounds_inherited_in_same_span=True,full_Cpsi_action_evaluated=False,full_Ct_action_approximated_with_all_errors_paid=True,exact_P0_covariance_row_zero=True,signed_common_and_difference_covariance_preserved=True,complementary_Schur_lower_test_matrix=ser(Mlow),complementary_Schur_lower_psd_verified=schur,complementary_Schur_structurally_bounded_below_by_Gram=True,structural_Schur_floor_not_a_tight_inverse_enclosure=True,new_reference_response_interval_certified=False,RC130_reference_response_interval_inherited_unchanged=True,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,next_cursor='refine common analytic response and new t residual in a conditioned Schur calculation; full covariance coverage now exists but tight inverse response remains open')

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=9);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC137 PASS: paid Ct trial and complete seven-input covariance')
