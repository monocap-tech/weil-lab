"""RC238: weighted omitted-output refinements of RC237 response trials."""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
import argparse,hashlib,json
import validate_rpb108_rc237_two_trial_signed_response as parent
orig=parent.orig;material=parent.material;p=parent.p
up=parent.up;down=parent.down;root=parent.root;B=parent.B;CUT=64;EXT=96;END=256
ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc237_two_trial_signed_response.json':'04bf1539dda4cfd79b4ecdc2d3e310daa2d3b657','notes/RPB108_RC237_TWO_TRIAL_SIGNED_RESPONSE_20261014.md':'a0b6740d463623f9b2bd1c91028dfa75b86289ae'})
HELPER_PINS['scripts/validate_rpb108_rc237_two_trial_signed_response.py']='d13e909c8aa8b91d5b55ec5e5e5179cdaf9325d2'
def endpoint_tail(d,sl,reverse):
 assert d in range(4) and END>CUT>d
 terms=[]
 for n in range(CUT+1,END+1):
  if (n-d)%2:continue
  c=F(2*n+1,(n-d)*(n+d+1))
  # Rounded individual positive summands avoid unnecessarily large common denominators.
  terms.append(up(orig.mass(n)*c*c/(orig.H(n)+sl)))
 if reverse:terms.reverse()
 first=END+1 if (END+1-d)%2==0 else END+2
 remainder=up(3*B/((orig.H(first)+sl)*(END-d)**2))
 return up(sum(terms,F(0))+remainder),dict(summed_through_degree=END,exact_positive_terms_rounded_up=list(map(str,terms if not reverse else terms[::-1])),remaining_endpoint_D_energy_upper=str(remainder))
def extended_columns(U,degrees,pi0,pierr,reverse):
 # The pinned helpers use module-level truncation parameters. Scope and restore
 # them; the published helper files and their source bytes are never changed.
 oldp=parent.CUT;oldm=material.CUT
 try:
  parent.CUT=EXT;material.CUT=EXT
  aa,bb=material.spherical_polynomials()
  return [parent.extended_band_coefficients(U,d,pi0,pierr,aa,bb,reverse) for d in degrees]
 finally:parent.CUT=oldp;material.CUT=oldm
def refined_augmentation(d,gram,oldgram,oldbudget,lam,sl,reverse):
 band=[parent.isc(g,1/orig.mass(n)) for n,g in enumerate(gram)]
 for n in range(CUT+1):assert gram[n]==oldgram[n],('retained band mismatch',d,n)
 captured=sum((orig.mass(n)*material.minabs(a)**2 for n,a in enumerate(band)),F(0))
 physicaltail=up(gram[d][1]-captured);assert physicaltail>=0
 first=EXT+1 if (EXT+1-d)%2==0 else EXT+2
 terms=[up(lam*lam*orig.mass(n)*max(abs(band[n][0]),abs(band[n][1]))**2/(orig.H(n)+sl)) for n in range(CUT+1,EXT+1)]
 if reverse:terms.reverse()
 remainder=up(lam*lam*physicaltail/(orig.H(first)+sl))
 weighted=up(sum(terms,F(0))+remainder)
 omitted=min(weighted,F(oldbudget['omitted']))
 finite=F(oldbudget['finite']);rational=F(oldbudget['rational'])
 E=up((root(finite)+root(omitted)+root(rational))**2)
 return E,dict(previous_omitted_output_D_energy_upper=oldbudget['omitted'],weighted_omitted_output_D_energy_upper=str(weighted),accepted_omitted_output_D_energy_upper=str(omitted),degree_65_through_96_D_energy_upper=str(up(sum(terms,F(0)))),beyond_96_physical_output_energy_upper=str(physicaltail),beyond_96_D_energy_upper=str(remainder),unchanged_finite_rounding_D_energy_upper=str(finite),unchanged_rational_to_band_D_energy_upper=str(rational),degree_65_through_96_summand_upper=list(map(str,terms if not reverse else terms[::-1])))
def controls():
 # 3(n+d+1)^2-(2n+1)(n-d) has these coefficients in n.
 endpoint_difference={str(d):[3*(d+1)**2+d,8*d+5,1] for d in range(4)}
 assert all(v>0 for row in endpoint_difference.values() for v in row)
 # D-selfadjoint noncommuting exact example: compare a trial inverse
 # response with its signed-gap residual identity, including cross terms.
 D=[[F(2),F(0)],[F(0),F(3)]]
 F0=[[F(1),F(1,4)],[F(1,4),F(2)]];Gy=[[F(2),F(1,3)],[F(1,3),F(1)]];lam=F(3)
 N=p.mm(p.inv(D),p.add(F0,p.scale(lam,Gy)));N0=p.mm(p.inv(D),F0)
 assert p.mm(N,N0)!=p.mm(N0,N)
 q=[[F(1)],[F(0)]];y=[[F(1,7)],[-F(1,11)]];O=p.mm(N0,q);e=p.add(O,p.mm(N,y),-1)
 response=p.mm(p.mm(p.trans(O),D),p.mm(p.inv(N),O))[0][0]
 residual=p.mm(p.mm(p.trans(e),D),p.mm(p.inv(N),e))[0][0]
 center=2*p.mm(p.trans(y),p.mm(F0,q))[0][0]-p.mm(p.trans(y),p.mm(p.add(F0,p.scale(lam,Gy)),y))[0][0]
 u=p.add(q,y,-1);gap=p.mm(p.trans(q),p.mm(F0,q))[0][0]-response
 assert response==center+residual
 assert gap==p.mm(p.trans(u),p.mm(F0,u))[0][0]+lam*p.mm(p.trans(y),p.mm(Gy,y))[0][0]-residual
 # Weighted splitting with unequal positive metric weights is an upper
 # bound, including the case when the remaining physical bound is loose.
 weights=[F(5),F(7),F(9)];energy=[F(1,4),F(1,9),F(1,16)];tailbound=sum(energy,F(0))+F(1,100)
 exact=sum((a/w for a,w in zip(energy,weights)),F(0))
 split=energy[0]/weights[0]+energy[1]/weights[1]+(tailbound-energy[0]-energy[1])/weights[2]
 assert exact<=split<=tailbound/weights[0]
 return dict(nonidentity_metric_noncommuting_signed_residual_identity=True,unequal_metric_weight_tail_split_control=True,endpoint_tail_difference_polynomial_coefficients=endpoint_difference)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  data[path]=json.loads(b) if path.endswith('.json') else b.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 old=get('237_two_trial_signed_response');baseorig=get('231_original_polynomial_action');baseaug=get('234_materialized_band_action');bounds=get('232_augmented_polynomial_action');kernel=get('115_rational_fourier_adjoint');metric=get('129_four_vector_joint_moment')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B)
 pi0=F(kernel['rational_pi']);pierr=F(kernel['rational_pi_error_upper']);rows=[]
 for base in [0,1]:
  prior=old['parity_two_trial_signed_response_certificates'][base];bound=bounds['polynomial_augmented_action_certificates'][base];lam=F(bound['augmentation_coefficient']);U=F(bound['rational_frequency_half_bandwidth']);degrees=[base,base+2]
  extra=extended_columns(U,degrees,pi0,pierr,reverse);columns=[];refinements=[]
  for k,d in enumerate(degrees):
   if k==0:
    original=deepcopy(baseorig['polynomial_original_action_certificates'][base]);aug=baseaug['parity_materialized_augmented_action_certificates'][base];action=aug['finite_complete_augmented_D_action'];oldE=aug['complete_augmented_action_D_error_squared_upper'];oldAE=aug['actual_augmentation_action_D_error_squared_upper']
    oldgram=[(F(r['lower']),F(r['upper'])) for r in aug['actual_band_Gram_column']]
    budget=dict(omitted=aug['augmentation_omitted_output_D_error_squared_upper'],finite=aug['augmentation_finite_rounding_D_error_squared_upper'],rational=aug['rational_to_band_augmentation_D_error_squared_upper'])
   else:
    original=deepcopy(prior['new_complete_original_action']);action=prior['new_complete_augmented_D_action'];oldE=prior['new_complete_augmented_D_action_D_error_squared_upper'];oldAE=prior['new_augmentation_action_D_error_squared_upper']
    oldgram=[(F(r['lower']),F(r['upper'])) for r in prior['new_band_Gram_column']];b=prior['new_augmentation_action_budget']
    budget=dict(omitted=b['augmentation_D_omitted_output_squared_upper'],finite=b['augmentation_D_finite_rounding_squared_upper'],rational=b['rational_to_band_D_error_squared_upper'])
   oldOE=original['complete_original_action_D_error_squared_upper'];comp=original['D_energy_component_squared_errors'];newtail,endpoint=endpoint_tail(d,sl,reverse);oldtail=F(comp['endpoint_omitted_output']);comp['endpoint_omitted_output']=str(min(oldtail,newtail))
   OE=up(sum((root(F(v)) for v in comp.values()),F(0))**2);assert OE<=F(oldOE);original['complete_original_action_D_error_squared_upper']=str(OE)
   gram,bandcontrols=extra[k];AE,bandbudget=refined_augmentation(d,gram,oldgram,budget,lam,sl,reverse);assert AE<=F(oldAE)
   E=up((root(OE)+root(AE))**2);assert E<=F(oldE)
   columns.append(dict(original=original,finite_complete_augmented_D_action=action,augmentation_action_D_error_squared_upper=str(AE),complete_augmented_action_D_error_squared_upper=str(E)))
   refinements.append(dict(input='P'+str(d),previous_original_action_D_error_squared_upper=oldOE,refined_original_action_D_error_squared_upper=str(OE),previous_endpoint_omitted_output_D_energy_upper=str(oldtail),weighted_endpoint_omitted_output_D_energy_upper=str(newtail),accepted_endpoint_omitted_output_D_energy_upper=comp['endpoint_omitted_output'],endpoint_controls=endpoint,previous_augmentation_action_D_error_squared_upper=oldAE,refined_augmentation_action_D_error_squared_upper=str(AE),band_tail_budget=bandbudget,band_controls=bandcontrols,degree_65_through_96_band_Gram_column=[dict(degree=n,lower=str(gram[n][0]),upper=str(gram[n][1])) for n in range(CUT+1,EXT+1)],previous_complete_augmented_action_D_error_squared_upper=oldE,refined_complete_augmented_action_D_error_squared_upper=str(E)))
  F0=[[(F(a),F(b)) for a,b in row] for row in prior['original_trial_form_intervals']];Gy=[[(F(a),F(b)) for a,b in row] for row in prior['frequency_trial_Gram_intervals']]
  previous=deepcopy(prior['source_inverse_response']);previous['actual_signed_response_gap_lower']=previous['actual_signed_gap_lower'];previous['actual_signed_response_gap_upper']=previous['actual_signed_gap_upper'];previous['selected_inverse_upper_trial']['trial_coefficient']=previous['selected_inverse_upper_trial']['trial_coefficients'][0]
  result=parent.response(base,columns,F0,Gy,lam,F(bound['fresh_augmented_N_D_lower']),F(bound['fresh_augmented_N_D_upper']),sl,sh,previous,reverse)
  # The inherited generator receives the first coordinate as one scalar
  # proposal. The certified RC237 two-component result is preserved by
  # interval intersection, independently of the new candidate choices.
  rows.append(dict(parity=prior['parity'],source=previous['source'],response_trial_basis=prior['response_trial_basis'],action_tail_refinements=refinements,source_inverse_response=result,original_trial_form_intervals=prior['original_trial_form_intervals'],frequency_trial_Gram_intervals=prior['frequency_trial_Gram_intervals'],complete_two_trial_action_error_D_Gram_upper=[[str(2*F(columns[0]['complete_augmented_action_D_error_squared_upper'])),'0'],['0',str(2*F(columns[1]['complete_augmented_action_D_error_squared_upper']))]]))
  print('RC238 weighted tails and response '+prior['parity']+' complete',flush=True)
 return dict(milestone='RC238',starting_commit='867a8a506b1fffdb1c1a0d3f4454d2b5e1a31c31',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,retained_action_degree=64,additional_band_tail_coefficients_through_degree=EXT,endpoint_tail_explicit_sum_through_degree=END,finite_action_centers_unchanged=True,actual_response_source_count=2,actual_response_source_order=['N0 P0','N0 P1'],response_trials_per_parity=2,global_augmented_inverse_lower_bound_unchanged=True,same_parity_action_errors_assumed_orthogonal=False,shared_source_original_action_error_coupled=True,parity_weighted_tail_response_certificates=rows,exact_controls=controls(),full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC239: reduce the remaining rational-to-band and complete output errors or add residual-shaped actual action trials; full 639-dimensional signed positivity remains required')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();c=run(a.replay)
 if a.replay:assert c==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC238 VALIDATED: weighted complete action tails; full signed gap open',flush=True)
