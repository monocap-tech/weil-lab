"""RC239: exterior band-projection energy lowers complete interior tails."""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
from math import comb,factorial
import argparse,hashlib,json
import validate_rpb108_rc238_weighted_action_tails as parent
trial=parent.parent;orig=parent.orig;p=parent.p
up=parent.up;down=parent.down;root=parent.root;B=parent.B
ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc238_weighted_action_tails.json':'d429659619b4226d2275472aa714302566ab5fe6','notes/RPB108_RC238_WEIGHTED_ACTION_TAILS_20261014.md':'a383818734d303cd5033d97ee94a0cd17b5be4e4'})
HELPER_PINS['scripts/validate_rpb108_rc238_weighted_action_tails.py']='a3922068c7ff8ae3d00435d8ee7f7733d5825748'
def exterior_bound(d,U):
 assert d in range(4) and U>1
 q=orig.legendre(d)
 # P_d(1-v/B) as a polynomial in physical distance v.
 boundary_poly=[sum((q[k]*comb(k,m)*(-1/B)**m for k in range(m,len(q))),F(0)) for m in range(len(q))]
 assert boundary_poly[0]==1
 alpha_lower=6*U;T=2*B
 # Si(alpha*T)/pi >= 1/2-2/(pi*alpha*T).
 # Elementary finite sine moments pay all remaining polynomial terms.
 moments=[F(0),F(2)/alpha_lower,T/alpha_lower+1/alpha_lower**2,T*T/alpha_lower+2*T/alpha_lower**2+4/alpha_lower**3]
 correction=2/(3*alpha_lower*T)+sum((abs(boundary_poly[k])*moments[k]/3 for k in range(1,len(boundary_poly))),F(0))
 b=down(F(1,2)-correction);assert b>0
 # pi in (3,4), and exp(9)>24BU, bound integral_0^(3B)|K| <=10/3.
 exp9_lower=sum((F(9)**k/factorial(k) for k in range(21)),F(0));assert exp9_lower>24*B*U
 derivative_sup=[F(0),F(1),F(3),F(6)][d]
 L=up(2*U+1/(6*B)+derivative_sup*F(10,3)/B)
 width=down(b/L);assert 0<width<=B
 # Integrate the nonnegative linear lower envelope on both exterior edges.
 leakage=down(2*(b*b*width-b*L*width*width+L*L*width**3/3))
 ideal=2*b**3/(3*L);assert 0<leakage<=ideal
 return leakage,dict(input='P'+str(d),boundary_distance_polynomial=list(map(str,boundary_poly)),sine_integral_and_polynomial_correction_upper=str(up(correction)),band_projection_at_right_boundary_lower=str(b),band_projection_exterior_derivative_abs_upper=str(L),exterior_interval_width=str(width),both_edges_exterior_band_projection_energy_lower=str(leakage),exponential_9_positive_series_lower=str(exp9_lower),logarithm_argument_upper=str(24*B*U),absolute_kernel_integral_0_through_3B_upper='10/3',both_exterior_edges_paid=True,physical_full_line_band_projection_used=True)
def controls():
 # Independent expansion of the boundary-distance polynomials.
 expected=[[F(1)],[F(1),-1/B],[F(1),-3/B,F(3,2)/B**2],[F(1),-6/B,F(15,2)/B**2,-F(5,2)/B**3]]
 for d in range(4):
  _,r=exterior_bound(d,F(100));assert list(map(F,r['boundary_distance_polynomial']))==expected[d]
 # The derivative bounds 0,1,3,6 hold on [-1,1] directly from these
 # degree-at-most-two derivative polynomials (their endpoint/vertex values).
 assert orig.legendre(1)==[F(0),F(1)]
 assert orig.legendre(2)==[-F(1,2),F(0),F(3,2)]
 assert orig.legendre(3)==[F(0),-F(3,2),F(0),F(5,2)]
 assert max(abs(-F(3,2)),abs(F(15,2)-F(3,2)))==6
 # Positive contraction control realized by a compression of an actual
 # orthogonal projection. Total projected energy splits into interior and
 # exterior energies exactly; interval subtraction remains conservative.
 # The second block uses the rational 3/5,4/5 unit vector.
 P=[[F(1,2),F(0),F(1,2),F(0)],[F(0),F(9,25),F(0),F(12,25)],[F(1,2),F(0),F(1,2),F(0)],[F(0),F(12,25),F(0),F(16,25)]]
 assert p.mm(P,P)==P and P==p.trans(P)
 q=[[F(2)],[F(1)],[F(0)],[F(0)]];h=p.mm(P,q)
 total=p.mm(p.trans(q),p.mm(P,q))[0][0];inside=sum((v[0]**2 for v in h[:2]),F(0));outside=sum((v[0]**2 for v in h[2:]),F(0))
 assert total==inside+outside and outside>0
 assert inside<=total-outside/2<total
 return dict(boundary_polynomials_independently_replayed=True,Legendre_derivative_suprema_verified=True,full_projection_interior_exterior_energy_split_verified=True,interval_exterior_subtraction_control=True)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  data[path]=json.loads(b) if path.endswith('.json') else b.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 old=get('238_weighted_action_tails');actions=get('237_two_trial_signed_response');baseorig=get('231_original_polynomial_action');baseaug=get('234_materialized_band_action');bounds=get('232_augmented_polynomial_action');metric=get('129_four_vector_joint_moment')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);rows=[]
 for base in [0,1]:
  prior=old['parity_weighted_tail_response_certificates'][base];ar=actions['parity_two_trial_signed_response_certificates'][base];bound=bounds['polynomial_augmented_action_certificates'][base];lam=F(bound['augmentation_coefficient']);U=F(bound['rational_frequency_half_bandwidth']);columns=[];refinements=[]
  for k,d in enumerate([base,base+2]):
   oldr=prior['action_tail_refinements'][k];budget=oldr['band_tail_budget'];leak,proof=exterior_bound(d,U)
   physical=up(F(budget['beyond_96_physical_output_energy_upper'])-leak);assert physical>=0
   first=97 if d%2 else 98
   remaining=up(lam*lam*physical/(orig.H(first)+sl));resolved=F(budget['degree_65_through_96_D_energy_upper']);weighted=up(resolved+remaining);omitted=min(F(budget['accepted_omitted_output_D_energy_upper']),weighted)
   AE=up((root(F(budget['unchanged_finite_rounding_D_energy_upper']))+root(omitted)+root(F(budget['unchanged_rational_to_band_D_energy_upper'])))**2)
   OE=F(oldr['refined_original_action_D_error_squared_upper']);E=up((root(OE)+root(AE))**2)
   assert AE<F(oldr['refined_augmentation_action_D_error_squared_upper']) and E<F(oldr['refined_complete_augmented_action_D_error_squared_upper'])
   if k==0:original=deepcopy(baseorig['polynomial_original_action_certificates'][base]);action=baseaug['parity_materialized_augmented_action_certificates'][base]['finite_complete_augmented_D_action']
   else:original=deepcopy(ar['new_complete_original_action']);action=ar['new_complete_augmented_D_action']
   original['complete_original_action_D_error_squared_upper']=str(OE);original['D_energy_component_squared_errors']['endpoint_omitted_output']=oldr['accepted_endpoint_omitted_output_D_energy_upper']
   columns.append(dict(original=original,finite_complete_augmented_D_action=action,augmentation_action_D_error_squared_upper=str(AE),complete_augmented_action_D_error_squared_upper=str(E)))
   refinements.append(dict(input='P'+str(d),exterior_energy_certificate=proof,previous_beyond_96_physical_output_energy_upper=budget['beyond_96_physical_output_energy_upper'],exterior_corrected_beyond_96_physical_output_energy_upper=str(physical),exterior_corrected_beyond_96_D_energy_upper=str(remaining),unchanged_degree_65_through_96_D_energy_upper=str(resolved),accepted_omitted_augmentation_output_D_energy_upper=str(omitted),original_action_D_error_squared_upper=str(OE),previous_augmentation_action_D_error_squared_upper=oldr['refined_augmentation_action_D_error_squared_upper'],refined_augmentation_action_D_error_squared_upper=str(AE),previous_complete_augmented_action_D_error_squared_upper=oldr['refined_complete_augmented_action_D_error_squared_upper'],refined_complete_augmented_action_D_error_squared_upper=str(E)))
  F0=[[(F(a),F(b)) for a,b in row] for row in prior['original_trial_form_intervals']];Gy=[[(F(a),F(b)) for a,b in row] for row in prior['frequency_trial_Gram_intervals']]
  previous=deepcopy(prior['source_inverse_response']);previous['actual_signed_response_gap_lower']=previous['actual_signed_gap_lower'];previous['actual_signed_response_gap_upper']=previous['actual_signed_gap_upper'];previous['selected_inverse_upper_trial']['trial_coefficient']=previous['selected_inverse_upper_trial']['trial_coefficients'][0]
  result=trial.response(base,columns,F0,Gy,lam,F(bound['fresh_augmented_N_D_lower']),F(bound['fresh_augmented_N_D_upper']),sl,sh,previous,reverse)
  rows.append(dict(parity=prior['parity'],response_trial_basis=prior['response_trial_basis'],action_exterior_tail_refinements=refinements,source_inverse_response=result,original_trial_form_intervals=prior['original_trial_form_intervals'],frequency_trial_Gram_intervals=prior['frequency_trial_Gram_intervals'],complete_two_trial_action_error_D_Gram_upper=[[str(2*F(columns[0]['complete_augmented_action_D_error_squared_upper'])),'0'],['0',str(2*F(columns[1]['complete_augmented_action_D_error_squared_upper']))]]))
 return dict(milestone='RC239',starting_commit='392adda1bc45967e02e1ec0acb1f0ce5b39a0d37',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,retained_action_degree=64,paid_band_tail_coefficients_through_degree=96,physical_exterior_band_energy_lower_bounds_certified=True,chosen_rational_augmentation_unchanged=True,finite_action_centers_unchanged=True,actual_response_source_count=2,actual_response_source_order=['N0 P0','N0 P1'],response_trials_per_parity=2,same_parity_action_errors_assumed_orthogonal=False,shared_source_original_action_error_coupled=True,parity_exterior_tail_response_certificates=rows,exact_controls=controls(),full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC240: sharpen the exterior lower envelope or certify richer full actions/responses; complete 639-dimensional signed positivity remains required')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();c=run(a.replay)
 if a.replay:assert c==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC239 VALIDATED: exterior band energy paid; full signed gap open',flush=True)
