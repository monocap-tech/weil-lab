"""RC253: exact prime boundary projections and coupled tails through 512."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import argparse,hashlib,json
import validate_rpb108_rc252_signed_endpoint_tail as parent
direct=parent.direct;native=parent.native;orig=parent.orig;p=parent.p;B=parent.B
up=parent.up;down=parent.down;root=parent.root;rootdown=parent.rootdown
ROOT=Path(__file__).resolve().parents[1];END=512
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc252_signed_endpoint_tail.json':'c226751e6c785f4ee29fade7a01b18b53504d84d','notes/RPB108_RC252_SIGNED_ENDPOINT_TAIL_20261014.md':'2abc7d3ab1c5f81f7890bebdef33194d0cf8395e'})
HELPER_PINS['scripts/validate_rpb108_rc252_signed_endpoint_tail.py']='e3b89120820dc08b049c87bcc2867a5bc94b8ad9'
def evaluate(poly,x):
 result=F(0)
 for c in reversed(poly):result=result*x+c
 return result
def derivative(poly):return [(k+1)*c for k,c in enumerate(poly[1:])]
def legendre_values(x,last):
 values=[F(1),x]
 for n in range(1,last):values.append(((2*n+1)*x*values[n]-n*values[n-1])/F(n+1))
 return values[:last+1]
def model_segments(q,parameters,parity):
 terms=[]
 for row in parameters:
  ell=F(row['chosen_translation']);c=F(row['chosen_coefficient'])
  for sign in [-1,1]:
   off=sign*ell/B;l=max(F(-1),-1-off);r=min(F(1),1-off)
   poly=[-c*sum((q[k]*comb(k,m)*off**(k-m) for k in range(m,len(q))),F(0)) for m in range(len(q))];terms.append((l,r,poly))
 knots=sorted({F(-1),F(1)}|{x for l,r,v in terms for x in [l,r]});segments=[]
 for l,r in zip(knots,knots[1:]):
  mid=(l+r)/2;v=[sum((w[k] for ll,rr,w in terms if ll<mid<rr),F(0)) for k in range(len(q))];segments.append((l,r,v))
 assert len(terms)==14 and len(segments)==15 and F(0) not in knots
 for l,r,v in segments:
  mirror=next(w for ll,rr,w in segments if ll==-r and rr==-l);assert mirror==[(-1)**(parity+k)*c for k,c in enumerate(v)]
 return segments
def prime_boundary(a,parity,proof,reverse):
 q=native.input_poly(a);segments=model_segments(q,proof['chosen_prime_model_parameters'],parity)
 assert native.segment_digest(segments)==proof['prime_segment_polynomial_sha256']
 norm=B*sum((orig.integral(orig.product(v,v),l,r) for l,r,v in segments),F(0))
 assert str(down(norm))==proof['full_prime_output_physical_energy_lower'] and str(up(norm))==proof['full_prime_output_physical_energy_upper']
 boundaries=[]
 for i in range(len(segments)-1):
  b=segments[i][1]
  if b<0:continue
  left=segments[i][2];right=segments[i+1][2];jump=[x-y for x,y in zip(left,right)];jc=[orig.project(jump,d) for d in range(len(q))]
  assert all(x==0 for x in native.addpoly(native.input_poly(jc),[-v for v in jump]))
  values=legendre_values(b,END);dv=[F(0)]+[d*(b*values[d]-values[d-1])/(b*b-1) for d in range(1,len(q))]
  for d in range(8):assert values[d]==evaluate(orig.legendre(d),b) and dv[d]==evaluate(derivative(orig.legendre(d)),b)
  boundaries.append((b,[jc[d]*values[d] for d in range(len(q))],[jc[d]*dv[d] for d in range(len(q))],values))
 assert len(boundaries)==7
 print('RC253 '+('even' if parity==0 else 'odd')+' seven positive boundary resolvents prepared',flush=True)
 coefficients=[]
 for n in range(END+1):
  if n%2!=parity:coefficients.append(F(0));continue
  if n<len(q):
   pn=orig.legendre(n);v=F(2*n+1,2)*sum((orig.integral(orig.product(poly,pn),l,r) for l,r,poly in segments),F(0))
  else:
   parts=[];lam=n*(n+1)
   for b,jv,jd,pn in boundaries:
    value=sum((c/F(lam-d*(d+1)) for d,c in enumerate(jv)),F(0));slope=sum((c/F(lam-d*(d+1)) for d,c in enumerate(jd)),F(0));dp=n*(b*pn[n]-pn[n-1])/(b*b-1)
    parts.append((1-b*b)*(slope*pn[n]-value*dp))
   if reverse:parts.reverse()
   # Reflected boundaries give the same contribution at matching parity.
   v=(2*n+1)*sum(parts,F(0))
  coefficients.append(v)
  if n in [127,128,255,256,383,384,511,512]:print('RC253 '+('even' if parity==0 else 'odd')+' prime boundary output through '+str(n),flush=True)
 captured=sum((orig.mass(n)*c*c for n,c in enumerate(coefficients)),F(0));assert captured<=norm
 return coefficients,up(norm-captured),dict(complete_prime_pairs=7,support_segments=15,positive_interior_boundaries=7,opposite_boundaries_paid_by_exact_parity=True,segment_polynomial_digest_replayed=True,full_prime_model_norm_replayed=True,all_boundary_jump_polynomials_reconstructed=True,boundary_low_Legendre_values_and_derivatives_replayed=True,prime_projection_cutoff=END,all_input_and_cross_prime_terms_retained=True)
def controls():
 # L=-((1-x^2)u')' is diagonal on the Legendre basis. This identity
 # proves the finite-polynomial resolvent used in Green's boundary formula.
 for n in list(range(65))+[65,128,256,512]:
  poly=orig.legendre(n);Lp=[F(0)]*len(poly)
  for k,c in enumerate(poly):
   Lp[k]+=k*(k+1)*c
   if k>=2:Lp[k-2]-=k*(k-1)*c
  assert Lp==[n*(n+1)*c for c in poly]
 # Direct polynomial integration checks the sign and normalization of Green's identity.
 for n in [5,8]:
  u=[F(1),F(-2),F(3)];uc=[orig.project(u,d) for d in range(3)];v=native.input_poly([uc[d]/F(n*(n+1)-d*(d+1)) for d in range(3)]);pn=orig.legendre(n);l=F(-2,3);r=F(3,5)
  W=lambda x:(1-x*x)*(evaluate(derivative(v),x)*evaluate(pn,x)-evaluate(v,x)*evaluate(derivative(pn),x))
  assert orig.integral(orig.product(u,pn),l,r)==W(r)-W(l)
 return dict(exact_Legendre_sturm_liouville_identity=True,exact_polynomial_resolvent_Green_boundary_control=True)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin');data[path]=json.loads(b) if path.endswith('.json') else b.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('252_signed_endpoint_tail');centers=get('251_extended_coupled_residual');old=get('248_direct_coupled_residual');tails=get('250_coupled_original_output_tail');forms=get('247_materialized_four_trial_response');bounds=get('232_augmented_polynomial_action');metric=get('129_four_vector_joint_moment')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);harmonics=[F(0)]
 for n in range(1,1027):harmonics.append(harmonics[-1]+F(1,n))
 rows=[]
 for parity,r in enumerate(prior['signed_endpoint_tail_response_certificates']):
  oldr=old['selected_direct_residual_certificates'][parity];a=list(map(F,oldr['original_combination_action_certificate']['exact_original_combination_input']));oldproof=tails['coupled_output_tail_response_certificates'][parity]['coupled_original_output_tail_certificate']
  pc,physical,proof=prime_boundary(a,parity,oldproof['prime_controls'],reverse)
  assert native.segment_digest([(F(0),F(256),pc[:257])])==oldproof['prime_model_coefficient_sha256']
  proof['all_prime_coefficients_through_256_match_pinned_digest']=True;proof['prime_coefficients_through_512_sha256']=native.segment_digest([(F(0),F(END),pc)])
  first=513 if parity else 514;remaining_prime=up(physical/(harmonics[first]+sl));endpoint,endpointcontrol=parent.tail_bound(a,first,sl,harmonics)
  endpointterms=r['signed_endpoint_tail_certificate']['explicit_endpoint_output_energy_257_through_1024'];endremaining=F(r['signed_endpoint_tail_certificate']['remaining_beyond_1024']['endpoint_D_omitted_energy_upper']);endpoint=min(endpoint,up(sum((F(t['endpoint_D_energy_upper']) for t in endpointterms if t['degree']>=first),F(0))+endremaining))
  remaining=up((root(endpoint)+root(remaining_prime))**2);terms=[];prime_terms=[]
  ll=lh=F(0) # No log2 uncertainty occurs above the input degree.
  for n in range(257,END+1):
   if n%2!=parity:continue
   h,rad=native.endpoint(a,n,ll,lh);assert rad==0;v=h+pc[n];terms.append(dict(degree=n,combined_original_D_energy_upper=str(up(orig.mass(n)*v*v/(harmonics[n]+sl)))));prime_terms.append(up(orig.mass(n)*pc[n]**2/(harmonics[n]+sl)))
  energies=[F(t['combined_original_D_energy_upper']) for t in terms]
  if reverse:energies.reverse();prime_terms.reverse()
  explicit=up(sum(energies,F(0)));neworiginal=up(explicit+remaining);accepted=min(F(r['new_original_combination_D_energy_beyond_256_upper']),neworiginal)
  c=centers['extended_coupled_residual_response_certificates'][parity];augmentation=F(c['augmentation_D_omitted_output_energy_upper']);omitted=up((root(accepted)+root(augmentation))**2);finite=F(c['residual_finite_rounding_D_energy_upper']);fault=F(c['unchanged_original_model_fault_D_norm_upper']);rational=F(c['unchanged_rational_augmentation_comparison_D_error_squared_upper']);E=min(F(r['complete_direct_residual_D_error_squared_upper']),up((root(up(finite+omitted))+fault+root(rational))**2))
  residual=c['extended_complete_direct_residual_center'];degrees=list(range(257));degrees=degrees[::-1] if reverse else degrees;nl=sum((orig.mass(n)*(harmonics[n]+sl)*F(residual[n]['coefficient'])**2 for n in degrees),F(0));nh=sum((orig.mass(n)*(harmonics[n]+sh)*F(residual[n]['coefficient'])**2 for n in degrees),F(0));rl=down(max(F(0),rootdown(nl)-root(E))**2);rh=up((root(nh)+root(E))**2)
  b=bounds['polynomial_augmented_action_certificates'][parity];mu=F(b['fresh_augmented_N_D_lower']);nu=F(b['fresh_augmented_N_D_upper']);lam=F(b['augmentation_coefficient']);pr=forms['parity_materialized_four_trial_response_certificates'][parity];F0=[[(F(a),F(b)) for a,b in row] for row in pr['original_trial_form_intervals']];Gy=[[(F(a),F(b)) for a,b in row] for row in pr['frequency_trial_Gram_intervals']];y=list(map(F,r['selected_trial_coefficients']))
  cl,ch=direct.center_intervals(F0,Gy,y,lam);tl=down(cl+rl/nu);th=up(ch+rh/mu);u=[1-y[0],-y[1],-y[2],-y[3]];ql,qh=direct.quadratic(F0,u);al,ah=direct.quadratic(Gy,y);dl=down(ql+lam*al-rh/mu);dh=up(qh+lam*ah-rl/nu)
  actualtl=max(F(r['actual_original_action_inverse_response_lower']),tl);actualth=min(F(r['actual_original_action_inverse_response_upper']),th);actualdl=max(F(r['actual_signed_gap_lower']),dl,down(F0[0][0][0]-actualth));actualdh=min(F(r['actual_signed_gap_upper']),dh,up(F0[0][0][1]-actualtl));assert actualtl<=actualth and actualdl<=actualdh
  rows.append(dict(parity=r['parity'],source=r['source'],selected_trial_coefficients=r['selected_trial_coefficients'],unchanged_retained_residual_center_origin='RC251 degree 256',prime_boundary_projection_certificate=proof,prime_physical_energy_beyond_512_upper=str(physical),prime_weighted_D_energy_beyond_512_upper=str(remaining_prime),prime_weighted_D_energy_beyond_256_upper=str(up(sum(prime_terms,F(0))+remaining_prime)),endpoint_remaining_beyond_512_control=endpointcontrol,accepted_endpoint_D_energy_beyond_512_upper=str(endpoint),coupled_original_output_energy_257_through_512=terms,explicit_coupled_original_D_energy_257_through_512_upper=str(explicit),coupled_original_D_energy_beyond_512_upper=str(remaining),new_original_D_energy_beyond_256_upper=str(neworiginal),accepted_original_D_energy_beyond_256_upper=str(accepted),previous_original_D_energy_beyond_256_upper=r['new_original_combination_D_energy_beyond_256_upper'],complete_direct_residual_D_error_squared_upper=str(E),previous_direct_residual_D_error_squared_upper=r['complete_direct_residual_D_error_squared_upper'],complete_direct_residual_actual_D_energy_lower=str(rl),complete_direct_residual_actual_D_energy_upper=str(rh),direct_inverse_response_lower=str(tl),direct_inverse_response_upper=str(th),direct_signed_gap_lower=str(dl),direct_signed_gap_upper=str(dh),actual_original_action_inverse_response_lower=str(actualtl),actual_original_action_inverse_response_upper=str(actualth),previous_original_action_inverse_response_upper=r['actual_original_action_inverse_response_upper'],actual_signed_gap_lower=str(actualdl),actual_signed_gap_upper=str(actualdh),original_action_inverse_upper_improved=actualth<F(r['actual_original_action_inverse_response_upper']),signed_gap_positive_certified=actualdl>0,actual_negative_gap_proved=actualdh<0))
 return dict(milestone='RC253',starting_commit='a69d9769095b75a0ede918ecbf9266c8ba3cf741',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,actual_response_source_count=2,response_trials_per_parity=4,prime_boundary_tail_response_certificates=rows,source_and_trial_spaces_unchanged=True,retained_direct_residual_output_degree_unchanged=256,prime_tail_explicit_degree=END,all_original_and_rational_augmentation_model_faults_preserved=True,exact_controls=controls(),new_response_enclosures_intersected_with_RC252=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC254: exploit the boundary projection interface for further prime tails or improve band remainder and residual inverse estimates; full signed positivity remains required')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();c=run(a.replay)
 if a.replay:assert c==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC253 VALIDATED: exact prime boundary tails; full signed gate open',flush=True)
