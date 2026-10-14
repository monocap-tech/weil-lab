"""RC249: certified scalar tuning and a uniform obstruction for its envelope."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc248_direct_coupled_residual as parent
orig=parent.orig;p=parent.p;B=parent.B
up=parent.up;down=parent.down;root=parent.root;rootdown=parent.rootdown
ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc248_direct_coupled_residual.json':'8e1afdf8e6728a078dab80f6547af6b3d790e2af','notes/RPB108_RC248_DIRECT_COUPLED_RESIDUAL_20261014.md':'4d906ca38e92b255eab89f3e03ac8f2bef811230'})
HELPER_PINS['scripts/validate_rpb108_rc248_direct_coupled_residual.py']='4837487293d9451148b84793ef994b9b20eb683c'
def dot(a,b,w,reverse=False):
 terms=list(range(len(w)));terms=terms[::-1] if reverse else terms
 return sum((w[n]*a[n]*b[n] for n in terms),F(0))
def scalar_controls():
 # A nonidentity metric and noncommuting operators replay the scaled identity
 # and the exact variational inverse identity with nonzero residuals.
 D=[[F(2),F(0)],[F(0),F(3)]];form=[[F(3),F(1,2)],[F(1,2),F(4)]]
 N=p.mm(p.inv(D),form);N0=p.mm(p.inv(D),[[F(1),F(1,3)],[F(1,3),F(2)]])
 mu=F(1,2);nu=F(3);assert p.psd(p.add(form,p.scale(mu,D),-1)) and p.psd(p.add(p.scale(nu,D),form,-1))
 assert p.mm(N,N0)!=p.mm(N0,N)
 f=p.mm(N0,[[F(1)],[F(0)]]);z=[[F(1,7)],[-F(2,11)]];e=p.add(f,p.mm(N,z),-1)
 T=p.mm(p.trans(f),p.mm(D,p.mm(p.inv(N),f)))[0][0]
 for t in [F(-2),F(0),F(3,4),F(1),F(5,4),F(3)]:
  tz=p.scale(t,z);et=p.add(p.scale(t,e),p.scale(1-t,f))
  assert et==p.add(f,p.mm(N,tz),-1)
  c=2*p.mm(p.trans(tz),p.mm(D,f))[0][0]-p.mm(p.trans(tz),p.mm(form,tz))[0][0]
  assert T==c+p.mm(p.trans(et),p.mm(D,p.mm(p.inv(N),et)))[0][0]
  energy=p.mm(p.trans(et),p.mm(D,et))[0][0]
  assert c+energy/nu<=T<=c+energy/mu
 return dict(nonidentity_metric_noncommuting_scaled_residual_identity=True,exact_variational_inverse_identity=True,exact_positive_augmented_residual_inverse_enclosures=True)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  data[path]=json.loads(b) if path.endswith('.json') else b.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 previous=get('248_direct_coupled_residual');source=get('245_source_refined_response');forms=get('247_materialized_four_trial_response');bounds=get('232_augmented_polynomial_action');metric=get('129_four_vector_joint_moment')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);rows=[]
 for parity,r in enumerate(previous['selected_direct_residual_certificates']):
  src=source['parity_source_refined_response_certificates'][parity]['refined_complete_original_source_action'];sc=src['finite_original_D_action'];ec=r['complete_direct_residual_center'];assert len(sc)==len(ec)==129
  f=[F(x['coefficient']) for x in sc];e=[F(x['coefficient']) for x in ec];v=[a-b for a,b in zip(e,f)]
  assert all(f[n]==e[n]==0 for n in range(129) if n%2!=parity)
  wl=[orig.mass(n)*(orig.H(n)+sl) for n in range(129)];wh=[orig.mass(n)*(orig.H(n)+sh) for n in range(129)]
  nl=[dot(f,f,wl,reverse),2*dot(f,v,wl,reverse),dot(v,v,wl,reverse)];nh=[dot(f,f,wh,reverse),2*dot(f,v,wh,reverse),dot(v,v,wh,reverse)]
  Es=F(src['complete_original_action_D_error_squared_upper']);Ee=F(r['complete_direct_residual_D_error_squared_upper']);ds=root(Es);de=root(Ee)
  b=bounds['polynomial_augmented_action_certificates'][parity];mu=F(b['fresh_augmented_N_D_lower']);nu=F(b['fresh_augmented_N_D_upper']);lam=F(b['augmentation_coefficient']);y=list(map(F,r['selected_trial_coefficients']))
  pr=forms['parity_materialized_four_trial_response_certificates'][parity];F0=[[(F(a),F(b)) for a,b in row] for row in pr['original_trial_form_intervals']];Gy=[[(F(a),F(b)) for a,b in row] for row in pr['frequency_trial_Gram_intervals']]
  def evaluate(t):
   ty=[t*x for x in y];lo=nl[0]+t*nl[1]+t*t*nl[2];hi=nh[0]+t*nh[1]+t*t*nh[2];assert 0<=lo<=hi
   delta=up(abs(t)*de+abs(1-t)*ds);rl=down(max(F(0),rootdown(lo)-delta)**2);rh=up((root(hi)+delta)**2)
   cl,ch=parent.center_intervals(F0,Gy,ty,lam);tl=down(cl+rl/nu);th=up(ch+rh/mu)
   u=[1-ty[0],-ty[1],-ty[2],-ty[3]];ql,qh=parent.quadratic(F0,u);al,ah=parent.quadratic(Gy,ty)
   dl=down(ql+lam*al-rh/mu);dh=up(qh+lam*ah-rl/nu)
   return dict(scale=str(t),trial_coefficients=list(map(str,ty)),complete_scaled_residual_D_error_norm_upper=str(delta),actual_scaled_residual_D_energy_lower=str(rl),actual_scaled_residual_D_energy_upper=str(rh),inverse_response_lower=str(tl),inverse_response_upper=str(th),signed_gap_lower=str(dl),signed_gap_upper=str(dh))
  # This is a finite rational proposal search, not a claim of scalar optimality.
  grid=[F(k,5000) for k in range(4500,5501)];grid=grid[::-1] if reverse else grid
  candidates=[evaluate(t) for t in grid]
  upper=min(candidates,key=lambda c:(F(c['inverse_response_upper']),F(c['scale'])))
  lower=max(candidates,key=lambda c:(F(c['inverse_response_lower']),-F(c['scale'])))
  gaplower=max(candidates,key=lambda c:(F(c['signed_gap_lower']),-F(c['scale'])))
  gapupper=min(candidates,key=lambda c:(F(c['signed_gap_upper']),F(c['scale'])))
  # For every real t, upper-center >= its entrywise midpoint Cnom(t),
  # residual center norm squared >= nl(t), and delta(t)^2 >= t^2 Ee.
  # Dropping 2*delta*sqrt(nh) gives the quadratic envelope below.
  fm=[[(a+b)/2 for a,b in row] for row in F0];gm=[[(a+b)/2 for a,b in row] for row in Gy]
  coupling=sum((y[k]*fm[0][k] for k in range(4)),F(0));nform=sum((y[j]*y[k]*(fm[j][k]+lam*gm[j][k]) for j in range(4) for k in range(4)),F(0))
  q=[nl[0]/mu,2*coupling+nl[1]/mu,(nl[2]+Ee)/mu-nform];assert q[2]>0
  tstar=-q[1]/(2*q[2]);floor=q[0]-q[1]*q[1]/(4*q[2]);assert floor>F0[0][0][1]
  # The direct signed-gap LOWER formula <= midpoint F00 - q(t).
  # These are bounds on the certification formulas, not on true T or gap.
  ceiling=fm[0][0]-floor;assert ceiling<0
  for c in candidates:
   t=F(c['scale']);qt=q[0]+t*q[1]+t*t*q[2]
   assert F(c['inverse_response_upper'])>=qt>=floor
   assert F(c['signed_gap_lower'])<=fm[0][0]-qt<=ceiling
   assert qt==floor+q[2]*(t-tstar)**2
  tl=max(F(r['actual_original_action_inverse_response_lower']),F(lower['inverse_response_lower']));th=min(F(r['actual_original_action_inverse_response_upper']),F(upper['inverse_response_upper']))
  dl=max(F(r['actual_signed_gap_lower']),F(gaplower['signed_gap_lower']),down(F0[0][0][0]-th));dh=min(F(r['actual_signed_gap_upper']),F(gapupper['signed_gap_upper']),up(F0[0][0][1]-tl));assert tl<=th and dl<=dh
  rows.append(dict(parity=r['parity'],source=r['source'],residual_identity='e(t)=t e(1)+(1-t) N0 Pbase',source_center_origin='RC245 retained degree 128',source_complete_D_error_squared_upper=str(Es),direct_residual_complete_D_error_squared_upper=str(Ee),source_and_direct_residual_errors_combined_by_norm_triangle=True,same_parity_errors_assumed_orthogonal=False,scaled_center_D_energy_polynomial_lower=list(map(str,nl)),scaled_center_D_energy_polynomial_upper=list(map(str,nh)),grid=dict(lower='9/10',upper='11/10',step='1/5000',candidate_count=1001),selected_upper_trial=upper,selected_lower_trial=lower,selected_signed_gap_lower_trial=gaplower,selected_signed_gap_upper_trial=gapupper,uniform_all_real_scalar_obstruction=dict(quadratic_lower_envelope_coefficients=list(map(str,q)),quadratic_leading_coefficient_positive=True,exact_quadratic_minimizer=str(tstar),exact_inverse_UPPER_formula_floor=str(floor),original_source_form_upper=str(F0[0][0][1]),exact_direct_signed_gap_LOWER_formula_ceiling=str(ceiling),all_real_scalars_covered=True,certificate_formula_cannot_close_signed_test=True,true_inverse_response_lower_bound_claimed=False,actual_negative_gap_claimed=False),actual_original_action_inverse_response_lower=str(tl),actual_original_action_inverse_response_upper=str(th),previous_original_action_inverse_response_upper=r['actual_original_action_inverse_response_upper'],actual_signed_gap_lower=str(dl),actual_signed_gap_upper=str(dh),original_action_inverse_upper_improved=th<F(r['actual_original_action_inverse_response_upper']),signed_gap_positive_certified=dl>0,actual_negative_gap_proved=dh<0))
 return dict(milestone='RC249',starting_commit='ca8ab074bde5ec4216c75226a812d7c772763cd6',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,actual_response_source_count=2,response_trials_per_parity=4,source_and_trial_spaces_unchanged=True,scalar_residual_tuning_certificates=rows,exact_controls=scalar_controls(),all_omitted_output_and_model_faults_inherited_and_paid=True,uniform_scalar_certificate_obstruction_not_true_operator_obstruction=True,new_response_enclosures_intersected_with_RC248=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC250: improve complete direct residual output tails or inverse coercivity; scalar rescaling with the inherited norm envelope cannot close the signed source tests')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();c=run(a.replay)
 if a.replay:assert c==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC249 VALIDATED: exact scalar tuning and uniform certificate obstruction; full signed gate open',flush=True)
