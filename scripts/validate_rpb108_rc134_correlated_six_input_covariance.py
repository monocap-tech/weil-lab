"""RC134: paid action trial and full correlated six-input projected covariance."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup,psd,ser
from validate_rpb108_rc129_four_vector_joint_moment import inv,mm,transpose,cong,add

def smul(a,b):
 from validate_rpb108_rc127_enriched_even_endpoint_action import lc,hc
 productsL=[lc.multiply(x,y) for x in a for y in b]
 productsU=[hc.multiply(x,y) for x in a for y in b]
 return min(productsL),max(productsU)

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];joint,new,capture,remaining,old,response=map(json.loads,raw)
 hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [x['milestone'] for x in (joint,new,capture,remaining,old,response)]==['RC133','RC132','RC131','RC130','RC129','RC128']
 assert joint['input_sha256']==hs[1:] and new['input_sha256']==hs[2:]
 src=Path(__file__).with_name('validate_rpb108_rc133_six_vector_joint_matrices.py').read_text()
 cut=src.index(" print('RC133 six-vector Gram independence certified'")
 namespace={'__file__':str(Path(__file__).with_name('validate_rpb108_rc133_six_vector_joint_matrices.py'))}
 exec(compile(src[:cut]+'\n return locals()\n','RC133-reconstruction','exec'),namespace)
 d=namespace['run'](paths[1:],replay)
 vectors=d['vectors'];dn=d['dn'];diag=d['diag'];T=d['T'];lam=d['lam'];zf=d['zf'];rho=F(lam,zf)
 N=6;O=8191;M=4095
 assert ser(d['GLp'])==joint['finite_prefix_actual_Gram_entry_lower']
 assert ser(d['GUp'])==joint['finite_prefix_actual_Gram_entry_upper']
 source={n:v for n,v in vectors[4].items() if n<=M};jobs=sorted(source,reverse=replay)
 action={};centers={}
 for n in range(0,O+1,2):
  val=Z
  for m in jobs:
   entry=diag[n] if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
   val=plus(val,mul(entry,source[m]))
  lo,hi=bounds(div(val,dn[n]));action[n]=(rat(lo)[0],rat(hi)[1]);centers[n]=down((lo+hi)/2)
 print('RC134 finite Cv source action complete',flush=True)
 # A finite-prefix least-squares trial chooses coefficients only; acceptance
 # uses a direct residual norm enclosure and does not invert uncertain matrices.
 Gmid=[[(d['GLp'][i][j]+d['GUp'][i][j])/2 for j in range(N)] for i in range(N)]
 pairing=[];pairBounds=[];actionEnergyLower=F(0)
 ns=list(range(0,O+1,2));ns=ns[::-1] if replay else ns
 for i in range(N):
  val=Z
  for n in ns:
   if n in vectors[i]:val=plus(val,smul(mul(rat(2*B/F(2*n+1)),dn[n]),smul(vectors[i][n],rat(centers[n]))))
  lo,hi=bounds(val);pairing.append([(lo+hi)/2]);pairBounds.append((lo,hi))
 Y=[down(r[0],10**20) for r in mm(inv(Gmid),pairing)]
 residual=F(0);payload=[]
 for n in ns:
  trial=Z
  for i in range(N):
   if n in vectors[i]:trial=plus(trial,smul(rat(Y[i]),vectors[i][n]))
  r=minus(action[n],trial);lo,hi=bounds(r);radius=max(abs(lo),abs(hi))
  residual+=up(2*B/F(2*n+1)*F(dn[n][1])*radius*radius,10**100)
  payload.append(dict(degree=n,action_center=str(centers[n]),residual_lower=str(lo),residual_upper=str(hi)))
 # All infinite trial tails share eta0 times an explicit rational polynomial.
 # Combine coefficients before absolute values, preserving cancellations.
 mu=d['mu'];nuv=d['nuv'];nuz=d['nuz'];oldlam=d['oldlam']
 def tail_poly(y):
  K=max(len(mu),len(nuv),len(nuz));q=[]
  for k in range(K):
   term=(y[1] if k==0 else F(0))
   if k<len(mu):term+=y[3]*mu[k]*F(oldlam,lam)**k
   if k<len(nuv):term+=y[4]*nuv[k]
   if k<len(nuz):term+=y[5]*nuz[k]
   q.append(term)
  return q
 q=tail_poly(Y);amp=up(sum(abs(qk)*rho**k for k,qk in enumerate(q)))
 trialTail=up(T*amp*amp,10**100)
 total=Z
 for m in jobs:total=plus(total,source[m])
 sourceOutputFactor=up(F(total[1])/(1-rho))
 outputTail=up(T*sourceOutputFactor*sourceOutputFactor,10**100)
 omittedInput=F(joint['endpoint_omitted_finite_and_analytic_source_D_energy_upper'][4])
 err=up(sqrtup(residual)+sqrtup(trialTail)+sqrtup(outputTail)+sqrtup(omittedInput))
 GentryU=[[F(x) for x in row] for row in joint['actual_D_Gram_entry_upper']]
 rv=min(up(err*err,10**100),GentryU[4][4]/4)
 # A lower bound on the finite-prefix least-squares distance is independent
 # of the chosen trial. The true Cv prefix differs only by the omitted input.
 for n in ns:
  actionEnergyLower+=down(2*B/F(2*n+1)*F(dn[n][0])*F(action[n][0])**2,10**100)
 K=inv(d['GLprefix']);projectionUpper=F(0)
 for i in range(N):
  for j in range(N):
   terms=[x*K[i][j]*y for x in pairBounds[i] for y in pairBounds[j]]
   projectionUpper+=max(terms)
 finiteDistanceLower=max(F(0),down(actionEnergyLower-projectionUpper,10**100))
 distanceLower=max(F(0),sqrtup(finiteDistanceLower)-F(1,10**40)-sqrtup(omittedInput))
 vLower=down(distanceLower*distanceLower,10**100)
 assert 0<vLower<=rv
 # v-z source difference: exact finite centers and a combined analytic tail.
 deltaFinite=F(0)
 for n in ns:
  delta=F(vectors[4][n][0])-F(vectors[5][n][0])
  assert vectors[4][n][0]==vectors[4][n][1] and vectors[5][n][0]==vectors[5][n][1]
  deltaFinite+=up(2*B/F(2*n+1)*F(dn[n][1])*delta*delta,10**100)
 differencePoly=tail_poly([F(0),F(0),F(0),F(0),F(-1),F(1)])
 differenceAmp=up(sum(abs(x)*rho**k for k,x in enumerate(differencePoly)))
 deltaEnergy=up(deltaFinite+T*differenceAmp*differenceAmp,10**100)
 # Residual generators: rpsi, rf, rw-alpha*rpsi, rv, rz-rv.
 budget=new['balanced_action_and_shared_covariance_budgets'][1];alpha=F(new['alpha'])
 p=F(budget['union_psi_covariance_upper']);f=F(remaining['paid_f0_covariance_upper']);ew=F(budget['shared_residual_difference_D_energy_upper'])
 generator=[p,f,ew,rv,deltaEnergy]
 # Rows map five residual generators to original six source residuals.
 A=[[F(0)]*5,[F(1),F(0),F(0),F(0),F(0)],[F(0),F(1),F(0),F(0),F(0)],[alpha,F(0),F(1),F(0),F(0)],[F(0),F(0),F(0),F(1),F(0)],[F(0),F(0),F(0),F(1),F(1)]]
 upper=mm(mm(A,[[5*generator[i] if i==j else F(0) for j in range(5)] for i in range(5)]),transpose(A))
 assert psd(upper)
 diagonal=[F(0),p,f,F(budget['union_w_covariance_upper']),rv,min(up((sqrtup(rv)+sqrtup(deltaEnergy))**2,10**100),GentryU[5][5]/4)]
 entryL=[[F(0)]*N for _ in range(N)];entryU=[[F(0)]*N for _ in range(N)]
 for i in range(N):
  entryU[i][i]=diagonal[i]
  if i==4:entryL[i][i]=vLower
  for j in range(i+1,N):
   cross=sqrtup(diagonal[i]*diagonal[j]);entryL[i][j]=entryL[j][i]=-cross;entryU[i][j]=entryU[j][i]=cross
 # Paid signed correlation identities coexist with generic entry enclosures.
 sharedCross=F(budget['union_mixed_deviation_from_alpha_Rpsipsi_upper'])
 vzDeviation=sqrtup(rv*deltaEnergy);zzDeviation=up(2*sqrtup(rv*deltaEnergy)+deltaEnergy)
 # A complementary Schur lower can be tested with the full covariance upper,
 # but broad inherited endpoint intervals may prevent acceptance.
 GL=[[F(x) for x in r] for r in joint['actual_D_Gram_Loewner_lower']]
 HL=[[F(x) for x in r] for r in joint['actual_endpoint_pairing_Loewner_lower']]
 Mlow=add(add(GL,HL),upper,-1);schur=psd(Mlow)
 # Rational controls: opposite new-vector coefficients cancel common rv;
 # omitting correlations would incorrectly charge twice its energy.
 for coeff in ([F(0),F(0),F(0),F(0),F(1),F(-1)],[F(0),-alpha,F(0),F(1),F(0),F(0)]):
  quadratic=mm(mm([coeff],upper),transpose([coeff]))[0][0]
  target=5*(deltaEnergy if coeff[4] else ew)
  assert quadratic==target
 return dict(milestone='RC134',status='PASS: full six-input covariance, genuine v obstruction and correlated response differences',starting_commit='5356cac08f038d1198b8822002993a85ef6724e8',input_sha256=hs,aperture='11/10',joint_family=joint['joint_family'],family_dimension=6,Cv_source_prefix_degree=M-1,Cv_output_prefix_degree=O-1,Cv_trial_coefficients=list(map(str,Y)),Cv_finite_action_and_residual_coefficient_sha256=hashlib.sha256(json.dumps(sorted(payload,key=lambda x:x['degree']),sort_keys=True,separators=(',',':')).encode()).hexdigest(),Cv_finite_residual_D_energy_upper=str(residual),Cv_omitted_input_D_energy_upper=str(omittedInput),Cv_omitted_output_D_energy_upper=str(outputTail),Cv_trial_combined_tail_polynomial=list(map(str,q)),Cv_trial_analytic_tail_D_energy_upper=str(trialTail),full_Cv_trial_D_norm_error_upper=str(err),v_projected_covariance_upper=str(rv),v_projected_covariance_lower=str(vLower),v_covariance_relative_own_D_Gram_lower=str(down(vLower/GentryU[4][4],10**12)),Cv_finite_action_D_energy_lower=str(actionEnergyLower),Cv_finite_projection_D_energy_upper=str(projectionUpper),Cv_finite_distance_to_family_D_energy_lower=str(finiteDistanceLower),z_minus_v_finite_source_D_energy_upper=str(deltaFinite),z_minus_v_combined_tail_polynomial=list(map(str,differencePoly)),z_minus_v_full_source_D_energy_upper=str(deltaEnergy),residual_generator_order=['rpsi','rf','rw-alpha*rpsi','rv','rz-rv'],residual_generator_D_energy_upper=list(map(str,generator)),residual_generator_to_six_input_matrix=ser(A),full_six_input_projected_covariance_entry_lower=ser(entryL),full_six_input_projected_covariance_entry_upper=ser(entryU),full_six_input_projected_covariance_Loewner_upper=ser(upper),exact_P0_covariance_row_zero=True,full_six_input_covariance_upper_certified=True,v_z_mixed_deviation_from_Rvv_upper=str(vzDeviation),zz_deviation_from_Rvv_upper=str(zzDeviation),psi_w_shared_deviation_upper=str(sharedCross),correlated_difference_controls_passed=True,full_six_input_covariance_lower_obstruction_certified=True,full_Cz_or_Cpsi_action_evaluated=False,Cv_full_action_approximated_with_paid_errors=True,reference_Schur_lower_test_matrix=ser(Mlow),reference_Schur_lower_psd_verified=schur,new_reference_response_interval_certified=False,RC130_reference_response_interval_inherited_unchanged=True,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,next_cursor='capture certified common new-vector residual; retain paid signed differences and refine endpoint Schur enclosure')

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=6);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC134 PASS: correlated full six-input covariance paid')
