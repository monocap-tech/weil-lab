"""RC248: certify selected residuals directly as N0(Pbase-Z)-lambda A Z."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse,hashlib,json
import validate_rpb108_rc247_materialized_four_trial_response as parent
material=parent.parent;native=material.parent.native;aggregate=material.aggregate
orig=parent.orig;p=parent.p;B=parent.B;up=parent.up;down=parent.down;root=parent.root
rootdown=parent.interface.rootdown;quadratic=parent.interface.quadratic
ROOT=Path(__file__).resolve().parents[1];CUT=128
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc247_materialized_four_trial_response.json':'b139c6998aaaedd96a8b072b5c54ad2b89cbf504','notes/RPB108_RC247_MATERIALIZED_FOUR_TRIAL_RESPONSE_20261014.md':'3fa8a80824c5bcd21eb513e02ca5876db2b52c41'})
HELPER_PINS['scripts/validate_rpb108_rc247_materialized_four_trial_response.py']='e5c6eb566e3b84c00d5a39716f02fa220725fc43'
def original_combination(a,parity,reg,eps,prime,sl,sh,reverse):
 q=native.input_poly(a);mass=sum((orig.mass(n)*c*c for n,c in enumerate(a)),F(0));assert mass==B*orig.integral(orig.product(q,q))
 rp=native.regular(q,parity,reg);rc=[orig.project(rp,n) for n in range(len(rp))];rt=up(sum((orig.mass(n)*v*v for n,v in enumerate(rc) if n>CUT),F(0)))
 print('RC248 direct original regular '+('even' if parity==0 else 'odd')+' complete',flush=True)
 pc,pt,pfault,proof=native.prime_action(q,a,parity,prime,reverse)
 print('RC248 direct original prime '+('even' if parity==0 else 'odd')+' complete',flush=True)
 phi=[F(11,20)**k/factorial(k) if k%2==parity else F(0) for k in range(41)];moment=B*orig.integral(orig.product(q,phi));pole=[2*(-1)**parity*moment*v for v in phi];oc=[orig.project(pole,n) for n in range(CUT+1)];tau=2*F(11,20)**41/factorial(41);polefault=up(16*B*tau*root(mass))
 ll=2*sum((F(1,3)**(2*k+1)/F(2*k+1) for k in range(100)),F(0));lh=ll+2*F(1,3)**201/(201*(1-F(1,9)));coeff=[];rounding=F(0)
 for n in range(CUT+1):
  if n%2!=parity:coeff.append(dict(degree=n,coefficient='0',radius='0'));continue
  h,hr=native.endpoint(a,n,ll,lh);identity=a[n] if n<len(a) else F(0);v=h-rc[n]+pc[n]+oc[n]-F(789,125)*identity
  values=[x/(orig.H(n)+s)+identity for x in [v-hr,v+hr] for s in [sl,sh]];lo=min(values);hi=max(values);c=down((lo+hi)/2);rad=max(c-lo,hi-c);rounding+=orig.mass(n)*(orig.H(n)+sh)*rad*rad;coeff.append(dict(degree=n,coefficient=str(c),radius=str(up(rad))))
 first=129 if parity else 130;et,ep=native.endpoint_tail(a,parity,sl,ll,lh,reverse)
 comp=dict(finite_rounding=up(rounding),endpoint_omitted_output=et,regular_omitted_output=up(rt/(orig.H(first)+sl)),prime_omitted_output=up(pt/(orig.H(first)+sl)),regular_kernel=up((2*B*eps)**2*mass/sl),prime_arithmetic=up(pfault*pfault/sl),pole_Taylor=up(polefault*polefault/sl))
 return coeff,comp,dict(exact_original_combination_input=list(map(str,a)),input_physical_energy=str(mass),prime_controls=proof,endpoint_tail_controls=ep,component_D_energy_squared_errors={k:str(v) for k,v in comp.items()},all_input_cross_terms_retained=True)
def center_intervals(F0,Gy,y,lam):
 cl=ch=F(0)
 for i in range(4):
  for k in range(4):
   w=(y[k] if i==0 else 0)+(y[i] if k==0 else 0)-y[i]*y[k];a,b=F0[i][k];cl+=min(w*a,w*b);ch+=max(w*a,w*b)
   w=-lam*y[i]*y[k];a,b=Gy[i][k];cl+=min(w*a,w*b);ch+=max(w*a,w*b)
 return down(cl),up(ch)
def controls():
 # The direct source identity is exact without N0/N commutation.
 D=[[F(2),F(0)],[F(0),F(3)]];F0=[[F(1),F(1,4)],[F(1,4),F(2)]];A=[[F(2),F(1,3)],[F(1,3),F(1)]];lam=F(3)
 N0=p.mm(p.inv(D),F0);Aop=p.mm(p.inv(D),A);N=p.add(N0,p.scale(lam,Aop));v=[[F(1)],[F(0)]];z=[[F(1,7)],[-F(2,11)]]
 assert p.mm(N0,N)!=p.mm(N,N0)
 assert p.add(p.mm(N0,v),p.mm(N,z),-1)==p.add(p.mm(N0,p.add(v,z,-1)),p.scale(lam,p.mm(Aop,z)),-1)
 return dict(noncommuting_metric_direct_original_augmentation_residual_identity=True,output_blocks_orthogonal_not_input_errors=True)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin');data[path]=json.loads(b) if path.endswith('.json') else b.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('247_materialized_four_trial_response');inputs=get('242_residual_original_actions');bounds=get('232_augmented_polynomial_action');kernel=get('115_rational_fourier_adjoint');metric=get('129_four_vector_joint_moment');regular=get('46_native_archimedean_head');prime=get('43_native_prime_head')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);reg=list(map(F,regular['regular_kernel_coefficients']));eps=F(regular['regular_kernel_uniform_error_upper']);pi0=F(kernel['rational_pi']);pierr=F(kernel['rational_pi_error_upper']);rows=[]
 for parity,r in enumerate(prior['parity_materialized_four_trial_response_certificates']):
  old=r['source_inverse_response'];y=list(map(F,old['selected_inverse_upper_trial']['trial_coefficients']));assert len(y)==4
  R=list(map(F,inputs['parity_residual_original_action_certificates'][parity]['exact_input_Legendre_coefficients']));Z=[y[3]*c for c in R]
  for k in range(3):Z[parity+2*k]+=y[k]
  Q=[-c for c in Z];Q[parity]+=1;assert all(c==0 for n,c in enumerate(Q) if n%2!=parity)
  bound=bounds['polynomial_augmented_action_certificates'][parity];lam=F(bound['augmentation_coefficient']);U=F(bound['rational_frequency_half_bandwidth']);epsilon=F(bound['physical_Fhat_star_Fhat_to_J_star_J_operator_norm_upper']);mu=F(bound['fresh_augmented_N_D_lower']);nu=F(bound['fresh_augmented_N_D_upper'])
  oc,components,originalproof=original_combination(Q,parity,reg,eps,prime,sl,sh,reverse)
  gram,bandproof=material.band_column(Z,parity,U,pi0,pierr,reverse);outside,partition=aggregate.leakage(Z,parity,U,pi0,pierr,reverse);massZ=sum((orig.mass(n)*c*c for n,c in enumerate(Z)),F(0));glo=ghi=F(0)
  for n,c in enumerate(Z):
   values=[c*gram[n][0],c*gram[n][1]];glo+=min(values);ghi+=max(values)
  glo=max(glo,massZ-outside[1]);ghi=min(ghi,massZ-outside[0]);assert 0<glo<=ghi
  output=[material.isc(g,1/orig.mass(n)) for n,g in enumerate(gram)];captured=sum((orig.mass(n)*material.band.minabs(g)**2 for n,g in enumerate(output)),F(0));physical_tail=up(ghi-captured);assert physical_tail>=0
  first=129 if parity else 130;augmentation_tail=up(lam*lam*physical_tail/(orig.H(first)+sl));rational=up(lam*lam*epsilon*epsilon*massZ/sl);residual=[];finite=F(0)
  for n,g in enumerate(output):
   values=[lam*c/(orig.H(n)+s) for c in g for s in [sl,sh]];lo=min(values);hi=max(values);ac=down((lo+hi)/2);ar=max(ac-lo,hi-ac);o=oc[n];c=F(o['coefficient'])-ac;rad=F(o['radius'])+ar;finite+=orig.mass(n)*(orig.H(n)+sh)*rad*rad;residual.append(dict(degree=n,coefficient=str(c),radius=str(up(rad))))
  assert all(F(x['coefficient'])==0 and F(x['radius'])==0 for n,x in enumerate(residual) if n%2!=parity)
  original_tail=sum((root(components[k]) for k in ['endpoint_omitted_output','regular_omitted_output','prime_omitted_output']),F(0));tail_error=up((original_tail+root(augmentation_tail))**2)
  original_model_fault=sum((root(components[k]) for k in ['regular_kernel','prime_arithmetic','pole_Taylor']),F(0));error_norm=up(root(up(finite+tail_error))+original_model_fault+root(rational));E=up(error_norm*error_norm)
  terms=list(range(CUT+1));terms=terms[::-1] if reverse else terms
  nl=sum((orig.mass(n)*(orig.H(n)+sl)*F(residual[n]['coefficient'])**2 for n in terms),F(0));nh=sum((orig.mass(n)*(orig.H(n)+sh)*F(residual[n]['coefficient'])**2 for n in terms),F(0));rl=down(max(F(0),rootdown(nl)-root(E))**2);rh=up((root(nh)+root(E))**2)
  F0=[[(F(a),F(b)) for a,b in row] for row in r['original_trial_form_intervals']];Gy=[[(F(a),F(b)) for a,b in row] for row in r['frequency_trial_Gram_intervals']];cl,ch=center_intervals(F0,Gy,y,lam);tl=down(cl+rl/nu);th=up(ch+rh/mu);u=[1-y[0],-y[1],-y[2],-y[3]];qlo,qhi=quadratic(F0,u);alo,ahi=quadratic(Gy,y);dl=down(qlo+lam*alo-rh/mu);dh=up(qhi+lam*ahi-rl/nu)
  actualtl=max(F(old['actual_original_action_inverse_response_lower']),tl);actualth=min(F(old['actual_original_action_inverse_response_upper']),th);actualdl=max(F(old['actual_signed_gap_lower']),dl,down(F0[0][0][0]-actualth));actualdh=min(F(old['actual_signed_gap_upper']),dh,up(F0[0][0][1]-actualtl));assert actualtl<=actualth and actualdl<=actualdh
  rows.append(dict(parity=r['parity'],source=old['source'],selected_trial_coefficients=list(map(str,y)),exact_Z_input_Legendre_coefficients=list(map(str,Z)),original_combination_action_certificate=originalproof,finite_original_combination_D_action=oc,band_materialization_controls=bandproof,band_input_energy_partition_certificate=partition,complete_direct_residual_center=residual,residual_finite_model_rounding_D_energy_upper=str(up(finite)),residual_model_omitted_output_D_energy_upper=str(tail_error),original_combination_model_fault_D_norm_upper=str(up(original_model_fault)),rational_augmentation_comparison_D_error_squared_upper=str(rational),complete_direct_residual_D_error_squared_upper=str(E),complete_direct_residual_actual_D_energy_lower=str(rl),complete_direct_residual_actual_D_energy_upper=str(rh),direct_inverse_response_lower=str(tl),direct_inverse_response_upper=str(th),direct_signed_gap_lower=str(dl),direct_signed_gap_upper=str(dh),actual_original_action_inverse_response_lower=str(actualtl),actual_original_action_inverse_response_upper=str(actualth),previous_original_action_inverse_response_upper=old['actual_original_action_inverse_response_upper'],actual_signed_gap_lower=str(actualdl),actual_signed_gap_upper=str(actualdh),original_action_inverse_upper_improved=actualth<F(old['actual_original_action_inverse_response_upper']),signed_gap_lower_improved=actualdl>F(old['actual_signed_gap_lower']),signed_gap_positive_certified=actualdl>0,actual_negative_gap_proved=actualdh<0,all_original_input_and_prime_cross_terms_retained=True,all_augmentation_input_cross_terms_retained=True,separate_input_action_errors_not_added_for_direct_residual=True))
 return dict(milestone='RC248',starting_commit='8b2e080af767cde8ce0f8d1d094493e927ff383b',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,actual_response_source_count=2,response_trials_per_parity=4,selected_direct_residual_certificates=rows,exact_controls=controls(),direct_identity='N0(Pbase-Z)-lambda D^-1 Fhat*Fhat Z',complete_actual_residuals_certified=True,all_omitted_outputs_and_rational_model_errors_paid=True,source_and_trial_spaces_unchanged=True,new_response_enclosures_intersected_with_RC247=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC249: exploit sharper direct residuals with refined output tails or stronger residual inverse estimates; full signed positivity remains required')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();c=run(a.replay)
 if a.replay:assert c==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC248 VALIDATED: direct coupled actual residuals; full signed gate open',flush=True)
