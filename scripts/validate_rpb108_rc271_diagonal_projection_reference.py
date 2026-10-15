"""RC271: positive reference operators with exact diagonal Legendre augmentation."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc270_threshold_adapted_coverage as parent
import validate_rpb108_rc230_augmentation_range_bridge as bridge
import validate_rpb108_rc268_two_pivot_schur_reduction as signed
ROOT=parent.ROOT;up=parent.up;down=parent.down;p=bridge.p;orig=parent.ellipse.orig
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc270_threshold_adapted_coverage.json':'c61286445210f82170c5d6b5b3e48540b7b3b66d','notes/RPB108_RC270_THRESHOLD_ADAPTED_COVERAGE_20261014.md':'f87db9cbe1a78d935f33d5116ab6320e881d47ad'})
HELPER_PINS['scripts/validate_rpb108_rc270_threshold_adapted_coverage.py']='07ae56dabe4242e05c56de26133dcabfc187078d'

def controls(reverse):
 I=[[F(i==j) for j in range(3)] for i in range(3)]
 D=[[F([2,3,4][i] if i==j else 0) for j in range(3)] for i in range(3)]
 L=[[F(2),F(1,5),F(0)],[F(1,5),F(2),F(1,10)],[F(0),F(1,10),F(2)]]
 U=[[F(2),F(0)],[F(0),F(3)],[F(0),F(0)]];Ut=p.trans(U);Mass=p.mm(Ut,U)
 P=p.mm(U,p.mm(p.inv(Mass),Ut));J=[[F(1,2),F(0),F(0)],[F(0),F(1,2),F(0)],[F(0),F(0),F(1,100)]]
 gamma=F(1,10);penalty=F(2);delta2=F(1,1000);theta=F(1);lam=penalty*(1+theta);eta=gamma-penalty*(1+1/theta)*delta2
 assert p.mm(P,P)==P and p.trans(P)==P
 assert p.psd(p.add(L,I,-1))
 assert p.psd(p.add(P,p.mm(p.trans(p.mm(J,P)),p.mm(J,P)),-1))
 Q=p.add(I,P,-1);JQ=p.mm(J,Q)
 assert p.psd(p.add(p.scale(delta2,I),p.mm(p.trans(JQ),JQ),-1))
 lower=p.add(p.scale(gamma,L),p.scale(penalty,p.mm(p.trans(J),J)),-1)
 shapes=[('negative',[[F(-1,10),F(1,100),F(0)],[F(1,100),F(1,5),F(0)],[F(0),F(0),F(1)]]),('zero',[[F(1,100),F(1,100),F(0)],[F(1,100),F(1,100),F(0)],[F(0),F(0),F(1)]]),('positive',p.scale(F(1,2),I))]
 if reverse:shapes.reverse()
 rows=[]
 for name,G0 in shapes:
  assert p.psd(p.add(G0,lower,-1))
  G=p.add(G0,p.scale(lam,P));assert p.psd(p.add(G,p.scale(eta,L),-1)) and p.inv(G)
  M=p.mm(p.inv(D),L);N=p.mm(p.inv(D),G);H=p.mm(p.inv(L),G)
  assert p.mm(M,H)==N and p.mm(M,N)!=p.mm(N,M)
  direct=p.mm(p.inv(N),p.mm(p.inv(D),U))
  assert direct==p.mm(p.inv(G),U)==p.mm(p.inv(H),p.mm(p.inv(L),U))
  T=p.mm(Ut,direct);gate=p.add(Mass,p.scale(lam,T),-1)
  ig=signed.inertia(G0);ib=signed.inertia(gate)
  assert ig['negative']==ib['negative'] and ig['zero']==ib['zero']
  assert ig['positive']==ib['positive']+1
  Y=[[F(1,7),F(-1,9)],[F(2,11),F(1,13)],[F(1,17),F(1,19)]]
  e=p.add(p.mm(p.inv(D),U),p.mm(N,Y),-1)
  center=p.add(p.add(p.mm(Ut,Y),p.mm(p.trans(Y),U)),p.mm(p.trans(Y),p.mm(G,Y)),-1)
  correction=p.mm(p.trans(e),p.mm(D,p.mm(p.inv(N),e)))
  assert T==p.add(center,correction) and p.psd(correction)
  assert T!=p.add(center,correction,-1)
  lower_metric_factor=F(1,3);assert p.psd(p.add(L,p.scale(lower_metric_factor,D),-1))
  assert p.psd(p.add(p.scale(1/(lower_metric_factor*eta),p.mm(p.trans(e),p.mm(D,e))),correction,-1))
  rows.append(dict(name=name,original_inertia=ig,auxiliary_gate_inertia=ib,exact_projection=p.ser(P),nonidentity_native_auxiliary_metric=p.ser(Mass),actual_metric_response=p.ser(T),native_response_gate=p.ser(gate),added_residual_covariance=p.ser(correction),noncommuting_bridge_verified=True))
 # Orthogonality of physical Legendre polynomials is checked by integration.
 for n in range(9):
  for j in range(n+1):
   value=orig.integral(orig.product(orig.legendre(n),orig.legendre(j)))
   assert value==(F(2,2*n+1) if n==j else 0)
   assert F(11,10)*value==(orig.mass(n) if n==j else 0)
 return dict(cases=sorted(rows,key=lambda v:v['name']),exact_Legendre_mass_controls=True,source_bridge_and_added_correction_verified=True,positive_reference_does_not_imply_original_positivity=True)

def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  if path.endswith('.json'):data[path]=json.loads(b)
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 coverage=get('270_threshold_adapted_coverage');legacy=get('114_positive_augmentation');metric=get('129_four_vector_joint_moment');oldbridge=get('230_augmentation_range_bridge')
 a=F(oldbridge['canonical_metric_D_equivalence_lower']);B=F(11,10)
 slo=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);shi=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B)
 assert 0<slo<=shi and a==F(32125,230953)
 models=[]
 for target in coverage['threshold_adapted_coverage_certificates']:
  rows=[]
  for parity,r in enumerate(target['parity_certificates']):
   b=r['original_concentration_budget'];gamma=F(b['reference_floor']);penalty=F(b['low_band_penalty_upper']);delta2=F(r['Fourier_restriction_squared_tail_upper'])
   beta=gamma-penalty*delta2;assert beta>=F(r['original_canonical_complement_floor_lower'])>0
   theta=F(1) if F(target['threshold']) else 2*penalty*delta2/beta
   lam=penalty*(1+theta);eta=down(gamma-penalty*(1+1/theta)*delta2);assert eta>0
   old=legacy['parity_positive_augmentation_certificates'][parity]
   bold=F(next(c for c in old['positive_augmentation_certificates'] if c['Young_parameter']=='1/4')['positive_augmented_operator_upper'])
   upper=up(bold+lam);mu=down(a*eta);nu=up(2*upper);assert 0<mu<nu
   degrees=r['retained_native_Chebyshev_degrees'];assert degrees==list(range(parity,r['exact_comparison_kernel_truncation_length'],2))
   diagonal=[]
   for j in sorted(degrees,reverse=reverse):
    mass=orig.mass(j);h=orig.H(j)
    diagonal.append(dict(Legendre_degree=j,native_auxiliary_mass=str(mass),D_source_coefficient_lower=str(down(1/(h+shi))),D_source_coefficient_upper=str(up(1/(h+slo))),D_augmentation_multiplier_lower=str(down(lam/(h+shi))),D_augmentation_multiplier_upper=str(up(lam/(h+slo)))))
   source=up(1/slo);generic=up(lam*source/mu);assert generic>1
   budgets=bridge.polynomial_budgets(mu,nu,source,lam) if F(target['threshold']) else []
   rows.append(dict(parity=r['parity'],rank=len(degrees),retained_Legendre_degrees=degrees,Young_parameter=str(theta),original_reference_floor=str(gamma),original_low_band_penalty=str(penalty),physical_high_projection_Fourier_squared_norm_upper=str(delta2),new_exact_projection_augmentation_coefficient=str(lam),new_canonical_positive_reference_floor=str(eta),fresh_canonical_reference_upper=str(upper),D_energy_reference_lower=str(mu),D_energy_reference_upper=str(nu),D_energy_condition_number_upper=str(up(nu/mu)),native_auxiliary_metric_diagonal_certificates=sorted(diagonal,key=lambda v:v['Legendre_degree']),augmentation_zero_on_all_other_Legendre_degrees=True,source_operator_squared_norm_upper=str(source),generic_auxiliary_response_upper=str(generic),generic_bound_closes_gate=False,conditional_exact_action_inverse_budgets=budgets))
   print('RC271 model '+str(target['explicit_canonical_exceptional_space_dimension'])+' '+r['parity']+': rank '+str(len(degrees))+'; positive reference floor '+str(float(eta)),flush=True)
  models.append(dict(model_rank=sum(r['rank'] for r in rows),source_coverage_threshold=target['threshold'],parity_projection_reference_certificates=rows,canonical_reference_floor_lower=str(min(F(r['new_canonical_positive_reference_floor']) for r in rows)),new_auxiliary_metric_exact_diagonal=True,new_frequency_Gram_required=False,augmentation_action_requires_no_Fourier_kernel_approximation=True,new_original_source_inverse_responses_computed=False,new_response_norm_below_one_certified=False))
 assert [v['model_rank'] for v in models]==[608,582]
 return dict(milestone='RC271',starting_commit='3fc9cd092f9f49e18cc0fe28c68257e8991df8c6',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,projection_reference_models=models,exact_controls=controls(reverse),
  exact_projection_formula='P_m f=sum_j P_j <P_j,f>_2 / mass_j; retained matching j<m',
  new_reference_formula='H_proj=A_Q+lambda i* P_m i',new_D_action_formula='N_proj=N0+lambda D^-1 P_m',
  full_response_gate='Mass-lambda T positive definite; T_ij=<P_i,N_proj^-1 D^-1 P_j>_2',
  residual_formula='T=U*Y+Y*U-Y*D N_proj Y+e*D N_proj^-1 e; e=D^-1 U-N_proj Y',
  residual_correction_sign='added',legacy_rank_639_rational_augmentation_unchanged=True,
  old_two_positive_signed_pivots_transferred_to_new_models=False,old_inverse_action_budgets_transferred=False,
  actual_original_Weil_actions_performed=False,new_augmented_inverse_responses_computed=False,
  original_below_one_hundredth_count_upper_preserved=608,original_nonpositive_count_upper_preserved=582,
  finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,
  next_cursor='RC272: assemble paid original-action residuals for the 608-source diagonal projection reference; use its exact native mass metric, pay added inverse covariance, and compare with the legacy two-pivot route before committing to full-range solves')

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
 if args.replay:assert result==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC271 VALIDATED: exact diagonal projection references; coupled response gate open',flush=True)
