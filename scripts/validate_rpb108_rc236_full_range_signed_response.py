"""RC236: exhaustive physical polynomial parameterization and signed
original-action inverse criterion; only the P0/P1 numerical instance runs."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import argparse,hashlib,json
import validate_rpb108_rc235_frequency_metric_response as parent
bridge=parent.bridge;orig=parent.orig;p=bridge.p
up=bridge.up;down=bridge.down;root=bridge.rootup;rootdown=parent.rootdown
ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc235_frequency_metric_response.json':'f166ee1808c3e6b528720fd6a8ff60f8915848c4','notes/RPB108_RC235_ACTUAL_FREQUENCY_METRIC_AND_COUPLED_RESPONSE_20261014.md':'385a7323d6ff4877edfa3ccd0b969a7c402220ca'})
HELPER_PINS['scripts/validate_rpb108_rc235_frequency_metric_response.py']='d429d0c29ddb4b3d3f36867762500a0dc766e3d7'
def cheb(n):
 a=[F(1)];b=[F(0),F(1)]
 if n==0:return a
 for k in range(1,n):
  c=[F(0)]*(k+2)
  for i,x in enumerate(b):c[i+1]+=2*x
  for i,x in enumerate(a):c[i]-=x
  a,b=b,c
 return b
def moment_diagonal(n):return orig.mass(n)*(F(1) if n==0 else F(2**(2*n-1),comb(2*n,n)))
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  raw=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==sha,(path,'pin')
  data[path]=json.loads(raw) if path.endswith('.json') else raw.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 frequency=get('235_frequency_metric_response');action=get('234_materialized_band_action');old=get('231_original_polynomial_action');bounds=get('232_augmented_polynomial_action');rangeproof=get('230_augmentation_range_bridge');kernel=get('115_rational_fourier_adjoint');metric=get('129_four_vector_joint_moment')
 assert rangeproof['full_chosen_augmentation_rank']==639 and frequency['actual_frequency_metric_certified_on_test_span']
 B=F(11,10);sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B)
 controls=0
 for i in range(13):
  for j in range(13):
   value=B*orig.integral(orig.product(cheb(i),orig.legendre(j)))
   if j>i or (i-j)%2:assert value==0;controls+=1
   if i==j:assert value==moment_diagonal(i)>0;controls+=1
 parameterizations=[]
 for row in rangeproof['parity_source_range_and_bridge_certificates']:
  indices=row['retained_native_indices'];assert len(indices)==row['rank']
  diagonal=[]
  for n in indices:
   x=moment_diagonal(n);assert x>0
   diagonal.append(dict(degree=n,positive=True,numerator_bit_length=x.numerator.bit_length(),denominator_bit_length=x.denominator.bit_length(),moment_diagonal_sha256=bridge.digest_fraction(x)))
  src=next(r for r in kernel['parity_rational_Fourier_adjoint_sources'] if r['parity']==row['parity'])
  delta=root(F(src['finite_model_squared_J_approximation_error_upper']));f2=up((1+delta)**2);lam=F(src['polynomial_model_augmentation_coefficient'])
  parameterizations.append(dict(parity=row['parity'],physical_trial_basis=['P'+str(n) for n in indices],dimension=len(indices),maximum_degree=indices[-1],positive_physical_moment_diagonal_controls=diagonal,moment_map_lower_triangular=True,physical_Fhat_restriction_bijects_onto_full_frequency_range=True,full_input_D_Gram_recipe='diagonal 2B/(2n+1)*(H_n+s)',physical_Fhat_squared_norm_upper=str(f2),augmentation_coefficient=str(lam),conditional_frequency_gap_per_unit_signed_D_floor_lower=str(down(sl/(lam*f2))),full_signed_D_floor_numerically_certified=False))
 assert sum(r['dimension'] for r in parameterizations)==639
 tests=[]
 for j,row in enumerate(action['parity_materialized_augmented_action_certificates']):
  o=old['polynomial_original_action_certificates'][j];pr=bounds['polynomial_augmented_action_certificates'][j];fq=frequency['parity_frequency_metric_response_certificates'][j]
  O=[F(r['coefficient']) for r in o['finite_original_D_action']];A=[F(r['coefficient']) for r in row['finite_complete_augmented_D_action']]
  Eo=F(o['complete_original_action_D_error_squared_upper']);Ea=F(row['actual_augmentation_action_D_error_squared_upper']);lam=F(pr['augmentation_coefficient'])
  flo=F(row['sharper_original_test_form_lower']);fhi=F(row['sharper_original_test_form_upper']);gyl=F(fq['actual_frequency_Gram_lower']);gyh=F(fq['actual_frequency_Gram_upper']);mu=F(pr['fresh_augmented_N_D_lower']);nu=F(pr['fresh_augmented_N_D_upper'])
  def trial(z):
   v=[a-z*b for a,b in zip(O,A)];terms=[(n,orig.mass(n)*x*x) for n,x in enumerate(v)]
   if reverse:terms.reverse()
   nl=sum((x*(orig.H(n)+sl) for n,x in terms),F(0));nh=sum((x*(orig.H(n)+sh) for n,x in terms),F(0))
   fault=abs(1-z)*root(Eo)+abs(z)*root(Ea)
   rl=down(max(F(0),rootdown(nl)-fault)**2);rh=up((root(nh)+fault)**2)
   coef=2*z-z*z;cl=down(min(coef*flo,coef*fhi)-lam*z*z*gyh);ch=up(max(coef*flo,coef*fhi)-lam*z*z*gyl)
   tl=down(cl+rl/nu);th=up(ch+rh/mu)
   # Couple the same original test form in F0-T rather than separately
   # subtracting two independent interval copies of that form.
   dl=down((1-z)**2*flo+lam*z*z*gyl-rh/mu);dh=up((1-z)**2*fhi+lam*z*z*gyh-rl/nu)
   return dict(trial_coefficient=str(z),source='N0 P'+str(j),residual_D_Gram_lower=str(rl),residual_D_Gram_upper=str(rh),original_action_inverse_response_lower=str(tl),original_action_inverse_response_upper=str(th),coupled_signed_gap_lower=str(dl),coupled_signed_gap_upper=str(dh),shared_original_action_fault_multiplier=str(abs(1-z)),shared_augmentation_fault_multiplier=str(abs(z)))
  candidates=sorted(set([F(k,1000) for k in range(-50,51)]+[flo/(fhi+lam*gyh),fhi/(flo+lam*gyl),F(0)]))
  t=[trial(z) for z in candidates];lower=max(t,key=lambda r:F(r['original_action_inverse_response_lower']));upper=min(t,key=lambda r:F(r['original_action_inverse_response_upper']))
  tl=max(F(0),F(lower['original_action_inverse_response_lower']));th=F(upper['original_action_inverse_response_upper'])
  dl=max(down(flo-th),max(F(r['coupled_signed_gap_lower']) for r in t));dh=min(up(fhi-tl),min(F(r['coupled_signed_gap_upper']) for r in t));assert tl<=th and dl<=dh
  tests.append(dict(parity=row['parity'],input='P'+str(j),actual_D_source='N0 P'+str(j),actual_canonical_source='A_Q P'+str(j),original_test_form_lower=str(flo),original_test_form_upper=str(fhi),actual_original_action_inverse_response_lower=str(tl),actual_original_action_inverse_response_upper=str(th),actual_signed_response_gap_lower=str(dl),actual_signed_response_gap_upper=str(dh),selected_inverse_lower_trial=lower,selected_inverse_upper_trial=upper,selected_signed_gap_lower_trial=max(t,key=lambda r:F(r['coupled_signed_gap_lower'])),selected_signed_gap_upper_trial=min(t,key=lambda r:F(r['coupled_signed_gap_upper'])),candidate_count=len(t),signed_gap_positive_certified=dl>0,actual_negative_gap_proved=dh<0))
 # Exact general identity controls, including an indefinite original form.
 D=[[F(2),F(0)],[F(0),F(3)]];Fhat=[[F(1),F(1,2)],[F(1,3),F(2,3)]];Ft=p.trans(Fhat);K=p.mm(Ft,Fhat);lam=F(9,4);I=[[F(1),F(0)],[F(0),F(1)]];abstract=[]
 for label,G0 in [('positive',[[F(4),F(1)],[F(1),F(5)]]),('indefinite',[[-F(1,2),F(1,5)],[F(1,5),F(4,3)]]),('singular_nonnegative',[[F(0),F(0)],[F(0),F(1)]])]:
  G=p.add(G0,p.scale(lam,K));assert p.psd(G)
  N=p.mm(p.inv(D),G);N0=p.mm(p.inv(D),G0);assert p.mm(N,N0)!=p.mm(N0,N)
  T=p.mm(G0,p.mm(p.inv(G),G0));Delta=p.add(G0,T,-1);BB=p.scale(lam,p.mm(Fhat,p.mm(p.inv(G),Ft)))
  assert p.mm(Ft,p.mm(p.add(I,BB,-1),Fhat))==p.scale(1/lam,Delta)
  assert p.mm(Ft,p.mm(BB,Fhat))==p.add(K,p.scale(1/lam,Delta),-1)
  positive=p.psd(G0);assert p.psd(Delta)==p.psd(p.add(I,BB,-1))==positive
  if label=='positive':assert p.inv(Delta) and p.inv(p.add(I,BB,-1))
  if label=='singular_nonnegative':
   E=p.add(I,BB,-1)
   assert Delta[0][0]*Delta[1][1]-Delta[0][1]*Delta[1][0]==E[0][0]*E[1][1]-E[0][1]*E[1][0]==0
  abstract.append(dict(control=label,original_form_nonnegative=positive,original_form_strictly_positive=label=='positive',nonnegative_singular_gap_is_not_below_one_gate=label=='singular_nonnegative',original_form=p.ser(G0),positive_augmented_form=p.ser(G),signed_gap=p.ser(Delta),frequency_response=p.ser(BB),noncommuting_exact_identity_verified=True,is_actual_Weil_counterexample=False))
 return dict(milestone='RC236',starting_commit='22904e21740833c773c7caa984fc80158d15ba2a',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,full_frequency_range_exhausted_by_physical_parameterization=True,full_parameter_dimension=639,parity_physical_parameterizations=parameterizations,small_physical_moment_controls=controls,exact_full_range_signed_identity='(Fhat V)* (I-Bhat) (Fhat V) = Delta_V/lambda; Delta_V=V* D N0 V-(N0 V)* D N^-1 (N0 V)',full_norm_below_one_iff_signed_gap_positive_on_both_full_parameter_spaces=True,quantitative_conditional_rule='If Delta_V >= c V*D V on a parity space, its full frequency gap is >= c*s_lower/(lambda*||Fhat||_physical^2); take the minimum of both parity gaps',numerical_full_signed_gap_matrix_evaluated=False,full_signed_gap_positive_certified=False,full_frequency_Gram_inversion_required_by_this_criterion=False,actual_original_operator_inverse_used=False,actual_N0_source_inverse_response_test_count=2,two_source_original_action_inverse_response_certificates=tests,actual_original_action_inverse_response_Gram_lower=[[tests[0]['actual_original_action_inverse_response_lower'],'0'],['0',tests[1]['actual_original_action_inverse_response_lower']]],actual_original_action_inverse_response_Gram_upper=[[tests[0]['actual_original_action_inverse_response_upper'],'0'],['0',tests[1]['actual_original_action_inverse_response_upper']]],actual_two_input_signed_gap_lower=[[tests[0]['actual_signed_response_gap_lower'],'0'],['0',tests[1]['actual_signed_response_gap_lower']]],actual_two_input_signed_gap_upper=[[tests[0]['actual_signed_response_gap_upper'],'0'],['0',tests[1]['actual_signed_response_gap_upper']]],two_input_signed_gap_positive_certified=all(r['signed_gap_positive_certified'] for r in tests),actual_negative_original_direction_proved=any(r['actual_negative_gap_proved'] for r in tests),noncommuting_positive_and_indefinite_abstract_controls=abstract,original_augmented_full_auxiliary_norm_below_one_certified=False,dense_639_solve_count_required=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC237: certify richer augmented inverse responses of original-action sources N0 V and the complete signed gap; use the exhaustive polynomial parameterization rather than treating two frequency vectors as full coverage')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();c=run(args.replay)
 if args.replay:assert c==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC236 VALIDATED: exhaustive signed-response criterion; actual full signed-gap positivity remains open',flush=True)
