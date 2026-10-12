"""RC135: one collective action trial for (v+z)/2, all tails paid."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup,psd,ser
from validate_rpb108_rc129_four_vector_joint_moment import mm,transpose

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];prior,joint,new,capture,remaining,old,response=map(json.loads,raw)
 hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [c['milestone'] for c in (prior,joint,new,capture,remaining,old,response)]==['RC134','RC133','RC132','RC131','RC130','RC129','RC128']
 assert prior['input_sha256']==hs[1:] and joint['input_sha256']==hs[2:]
 # Recover exact finite collective source coefficients without changing history.
 src=Path(__file__).with_name('validate_rpb108_rc133_six_vector_joint_matrices.py').read_text()
 cut=src.index(" print('RC133 six-vector Gram independence certified'")
 ns={'__file__':str(Path(__file__).with_name('validate_rpb108_rc133_six_vector_joint_matrices.py'))}
 exec(compile(src[:cut]+'\n return locals()\n','RC133-reconstruction','exec'),ns)
 d=ns['run'](paths[2:],replay)
 assert ser(d['GLp'])==joint['finite_prefix_actual_Gram_entry_lower']
 vec=d['vectors'];source={n:(F(vec[4][n][0])+F(vec[5][n][0]))/2 for n in vec[4]}
 assert all(vec[i][n][0]==vec[i][n][1] for i in (4,5) for n in vec[i])
 assert min(source.values())>0
 L=8191;O=16383;lam=(L-1)*L;first=O+1;zf=first*(first+1);rho=F(lam,zf)
 harmonic=d['d']['harmonic'][:];s=d['s'];log=d['d']['log']
 for n in range(len(harmonic),2*O+1):harmonic.append(plus(harmonic[-1],rat(F(1,n))))
 dn={n:plus(harmonic[n],s) for n in range(0,O+1,2)}
 diagonal={n:minus(plus(minus(mul(rat(2),harmonic[2*n]),mul(rat(2),harmonic[n])),rat(F(1,2*n+1))),log) for n in range(0,O+1,2)}
 jobs=sorted(source,reverse=replay);poly=[];polyError=F(0)
 for n in range(0,O+1,2):
  value=Z
  for m in jobs:
   entry=diagonal[n] if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
   value=plus(value,mul(entry,rat(source[m])))
  lo,hi=bounds(div(value,dn[n]));center=down((lo+hi)/2);radius=max(center-lo,hi-center)
  poly.append(dict(degree=n,center=str(center),radius=str(radius)))
  polyError+=up(2*B/F(2*n+1)*F(dn[n][1])*radius*radius,10**100)
  if n and n%4096==0:print('RC135 collective output through',n,flush=True)
 print('RC135 common finite action complete',flush=True)
 moments=[]
 for k in range(61):
  value=Z
  for m in jobs:value=plus(value,mul(rat(source[m]),rat(F(m*(m+1),lam)**k)))
  lo,hi=bounds(value);center=down((lo+hi)/2);radius=max(center-lo,hi-center)
  assert lo>0
  moments.append(dict(order=k,lower=str(lo),upper=str(hi),center=str(center),radius=str(radius)))
 T=up(B/(F(plus(harmonic[O-1],s)[0])*(O-2)*(O-1)))
 # Exact common input analytic moments above 8190 share RC131 eta_k.
 nuv=d['nuv'];nuz=d['nuz'];commonMoments=[((nuv[k] if k<len(nuv) else F(0))+(nuz[k] if k<len(nuz) else F(0)))/2 for k in range(max(len(nuv),len(nuz)))]
 oldRho=F(d['lam'],8192*8193)
 inputAmplitude=up(sum(x*oldRho**k for k,x in enumerate(commonMoments)))
 inputTail=up(d['T']*inputAmplitude*inputAmplitude,10**100)
 GL=[[F(x) for x in r] for r in joint['actual_D_Gram_entry_lower']]
 GU=[[F(x) for x in r] for r in joint['actual_D_Gram_entry_upper']]
 uGramLower=(GL[4][4]+2*GL[4][5]+GL[5][5])/4
 deltaSource=F(prior['z_minus_v_full_source_D_energy_upper'])
 # For delta=z-v in E, projection trial delta/2 and positive contraction
 # improve the old difference bound to R_delta<=||delta||²/4.
 deltaResidual=deltaSource/4
 vOldLower=F(prior['v_projected_covariance_lower']);budgets=[]
 bnew=new['balanced_action_and_shared_covariance_budgets'][1]
 psi=F(bnew['union_psi_covariance_upper']);f=F(remaining['paid_f0_covariance_upper']);ew=F(bnew['shared_residual_difference_D_energy_upper']);alpha=F(new['alpha'])
 for digits in (6,12,24):
  target=F(1,10**digits);K=0
  while True:
   omitted=up(T*(F(moments[K+1]['upper'])*rho**(K+1)/(1-rho))**2,10**100)
   rounding=up(T*sum(F(moments[k]['radius'])*rho**k for k in range(K+1))**2,10**100)
   finiteError=up(sqrtup(polyError)+sqrtup(rounding)+sqrtup(omitted))
   if finiteError*finiteError<=target*target*uGramLower:break
   K+=1;assert K<60
  fullError=up(finiteError+sqrtup(inputTail));commonVariance=up(fullError*fullError,10**100)
  coordinateNorm=up(fullError+sqrtup(deltaResidual)/2);coordinateVar=up(coordinateNorm*coordinateNorm,10**100)
  distance=sqrtup(vOldLower)-F(1,10**40)-sqrtup(deltaResidual)/2-fullError
  assert distance>0 and coordinateVar<vOldLower/100
  energies=[psi,f,ew,commonVariance,deltaResidual]
  A=[[F(0)]*5,[F(1),F(0),F(0),F(0),F(0)],[F(0),F(1),F(0),F(0),F(0)],[alpha,F(0),F(1),F(0),F(0)],[F(0),F(0),F(0),F(1),F(-1,2)],[F(0),F(0),F(0),F(1),F(1,2)]]
  upper=mm(mm(A,[[5*energies[i] if i==j else F(0) for j in range(5)] for i in range(5)]),transpose(A));assert psd(upper)
  diagonal=[F(0),psi,f,F(bnew['union_w_covariance_upper']),coordinateVar,coordinateVar]
  el=[[F(0)]*6 for _ in range(6)];eu=[[F(0)]*6 for _ in range(6)]
  for i in range(6):
   eu[i][i]=diagonal[i]
   for j in range(i+1,6):
    cross=sqrtup(diagonal[i]*diagonal[j]);el[i][j]=el[j][i]=-cross;eu[i][j]=eu[j][i]=cross
  # Both signed response combinations are exactly paid by the generator map.
  for coeff,expected in [([F(0)]*4+[F(1),F(-1)],5*deltaResidual),([F(0)]*4+[F(1,2),F(1,2)],5*commonVariance)]:
   assert mm(mm([coeff],upper),transpose([coeff]))[0][0]==expected
  budgets.append(dict(relative_common_source_D_norm_target=str(target),retained_tail_highest_order=K,retained_tail_feature_count=K+1,added_collective_vector_count=1,enlarged_projection_span_dimension=7,analytic_moment_centers=[moments[k]['center'] for k in range(K+1)],finite_output_rounding_D_energy_upper=str(polyError),moment_rounding_D_energy_upper=str(rounding),omitted_finite_source_output_D_energy_upper=str(omitted),finite_common_action_trial_D_norm_error_upper=str(finiteError),common_analytic_source_action_D_energy_upper=str(inputTail),full_common_action_trial_D_norm_error_upper=str(fullError),common_projected_covariance_upper=str(commonVariance),v_and_z_projected_covariance_each_upper=str(coordinateVar),v_relative_own_D_Gram_upper=str(up(coordinateVar/GL[4][4],10**15)),z_relative_own_D_Gram_upper=str(up(coordinateVar/GL[5][5],10**15)),old_v_coordinate_lower_over_new_upper=str(down(vOldLower/coordinateVar,10**6)),new_vector_distance_to_old_six_span_D_energy_lower=str(down(distance*distance)),old_six_input_projected_covariance_entry_lower=ser(el),old_six_input_projected_covariance_entry_upper=ser(eu),old_six_input_projected_covariance_Loewner_upper=ser(upper),residual_generator_to_old_six_matrix=ser(A),residual_generator_D_energy_upper=list(map(str,energies)),signed_common_and_difference_controls_passed=True))
 controls=[]
 for z in (zf,2*zf):
  weights={0:F(3,7),2:F(1,11),L-1:F(1,100000)}
  for K in (0,4,12):
   exact=sum(x/(1-F(m*(m+1),z)) for m,x in weights.items())
   mu=[sum(x*F(m*(m+1),lam)**k for m,x in weights.items()) for k in range(K+2)]
   prefix=sum(mu[k]*F(lam,z)**k for k in range(K+1));remainder=mu[K+1]*F(lam,z)**(K+1)/(1-F(lam,z))
   assert 0<exact-prefix<=remainder
   controls.append(dict(z=z,order=K,zero_degree_mass_and_positive_remainder_verified=True))
 return dict(milestone='RC135',status='PASS: one common response trial captures both new-vector leakages with paid full old-six covariance',starting_commit='ca2ca9d1003aacc72d305855b1c4024cb75c969d',input_sha256=hs,aperture='11/10',old_family=joint['joint_family'],common_source_definition='u=(v10+z_b6)/2',difference_source_definition='delta=z_b6-v10',source_finite_degree=L-1,finite_output_degree=O-1,finite_output_polynomial_coefficient_count=len(poly),finite_output_polynomial_center_radius_sha256=hashlib.sha256(json.dumps(poly,sort_keys=True,separators=(',',':')).encode()).hexdigest(),common_finite_source_coefficient_sha256=hashlib.sha256(json.dumps([dict(degree=n,center=str(source[n])) for n in sorted(source)],sort_keys=True,separators=(',',':')).encode()).hexdigest(),tail_Lambda=str(lam),output_geometric_ratio_upper=str(rho),leading_output_tail_D_energy_upper=str(T),positive_finite_source_moment_intervals=moments,common_input_analytic_moment_centers=list(map(str,commonMoments)),common_input_analytic_tail_D_energy_upper=str(inputTail),delta_full_source_D_energy_upper=str(deltaSource),delta_projected_action_covariance_upper=str(deltaResidual),collective_capture_budgets=budgets,selected_relative_common_source_D_norm_target='1/1000000000000',new_collective_vector_independence_from_old_six_certified=True,new_projection_span_dimension=7,full_old_six_input_covariance_paid=True,full_seven_vector_Gram_and_endpoint_pairing_evaluated=False,new_vector_action_evaluated=False,full_seven_input_covariance_evaluated=False,new_reference_response_interval_certified=False,RC130_reference_response_interval_inherited_unchanged=True,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,exact_rational_geometric_controls=controls,next_cursor='certify seven-vector joint family and remaining analytic actions; refine correlated Schur enclosure without transferring old-six covariance to seven inputs')

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=7);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC135 PASS: single common response capture and full old-six covariance paid')
