"""RC270: threshold-adapted original canonical coverage, ranks 608 and 582."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc269_smaller_canonical_exceptional_space as parent
ellipse=parent.ellipse; ROOT=parent.ROOT;down=parent.down;up=ellipse.up
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc269_smaller_canonical_exceptional_space.json':'25a3ac10a49f01564b381d47c90cf1832309f7f1','notes/RPB108_RC269_SMALLER_CANONICAL_EXCEPTIONAL_SPACE_20261014.md':'e146b9dee28e5cf983c11e763e30322ef3d045d6'})
HELPER_PINS['scripts/validate_rpb108_rc269_smaller_canonical_exceptional_space.py']='2474275f35fbf79df916daadb26216b07ce140bd'

def budget(L,k,reverse):
 # RC112's high-frequency reserve determines an admissible reference floor.
 elo,ehi=ellipse.exp_negative_interval(L,reverse)
 Tlo=down(1/ehi);U=up(1/elo);assert 60<Tlo<U
 ceiling=(L-k-1/Tlo)/(L+3/Tlo)
 gamma=down(ceiling)-F(1,10**10);assert 0<gamma<1
 reserve=down((1-gamma)*L-k-(1+3*gamma)/Tlo);assert reserve>0
 penalty=up(F(31,5)+k+gamma*(L+1))
 return gamma,penalty,U,dict(frequency_log_cutoff=str(L),negative_exponential_lower=str(elo),negative_exponential_upper=str(ehi),frequency_cutoff_lower=str(Tlo),frequency_cutoff_upper=str(U),physical_negative_nonarch_allowance=str(k),reference_floor_ceiling_from_high_reserve=str(ceiling),reference_floor_safety_subtraction='1/10000000000',reference_floor=str(gamma),high_frequency_reserve_lower=str(reserve),low_band_penalty_upper=str(penalty))

def controls():
 # Algebraic threshold margin, including zero in the excluded spectral interval.
 for L,k,Tlo in [(F(5),F(4),F(100)),(F(6),F(5),F(200))]:
  ceiling=(L-k-1/Tlo)/(L+3/Tlo)
  assert (1-ceiling)*L-k-(1+3*ceiling)/Tlo==0
  gamma=ceiling-F(1,1000)
  assert (1-gamma)*L-k-(1+3*gamma)/Tlo==F(1,1000)*(L+3/Tlo)>0
 c=parent.controls();c.update(reference_floor_high_frequency_reserve_identity=True,nonpositive_count_includes_nullity=True)
 return c

def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  if path.endswith('.json'):data[path]=json.loads(b)
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 original=get('112_parity_spectral_coverage');prior=get('269_smaller_canonical_exceptional_space');kernel=get('115_rational_fourier_adjoint')
 pi=F(kernel['rational_pi'])+F(kernel['rational_pi_error_upper'])
 targets=[]
 for threshold,choices,expected in [(F(1,100),[(4166,472),(4636,745)],608),(F(0),[(4126,454),(4588,711)],582)]:
  rows=[]
  for parity,(lognumerator,m) in enumerate(choices):
   old=original['parity_coverage_certificates'][parity];k=F(old['physical_negative_nonarch_allowance'])
   gamma,penalty,U,proof=budget(F(lognumerator,1000),k,reverse)
   assert gamma>threshold
   candidates=[];skipped=[]
   for q in sorted(range(120,181),reverse=reverse):
    r=F(q,100);lo,_,_=ellipse.coercive.log_interval(r)
    gap=m*lo-2*pi*ellipse.B*U*(r-1/r)/2
    if not 0<2*gap<100:
     skipped.append(dict(radius=str(r),twice_gap_lower=str(2*gap)));continue
    hs,c=ellipse.contour(r,m,parity,U,pi,reverse);assert c['first_omitted_degree']==m
    candidates.append((hs,r,c))
   hs,r,c=min(candidates,key=lambda v:(v[0],v[1]))
   beta=down(gamma-penalty*hs);margin=down(beta-threshold);assert margin>0
   degrees=list(range(parity,m,2));rank=len(degrees)
   rows.append(dict(parity=old['parity'],original_concentration_budget=proof,
    exact_comparison_kernel_truncation_length=m,retained_native_Chebyshev_degrees=degrees,
    canonical_Riesz_moment_span_dimension=rank,largest_retained_native_degree=degrees[-1],
    radius_grid_numerators=list(range(120,181)),radius_grid_denominator=100,
    all_admissible_contour_certificates=[v[2] for v in sorted(candidates,key=lambda v:v[1])],
    skipped_radius_certificates=sorted(skipped,key=lambda v:F(v['radius'])),
    selected_integrated_contour_certificate=c,Fourier_restriction_squared_tail_upper=str(hs),
    original_canonical_complement_floor_lower=str(beta),threshold_margin_lower=str(margin),
    inherited_1250_effective_strong_dimension=625-rank,
    original_spectral_count_at_requested_threshold_upper=rank))
   print('RC270 threshold '+str(threshold)+' '+old['parity']+': rank '+str(rank)+'; complement floor '+str(float(beta)),flush=True)
  count=sum(r['canonical_Riesz_moment_span_dimension'] for r in rows);assert count==expected
  floor=min(F(r['original_canonical_complement_floor_lower']) for r in rows)
  targets.append(dict(threshold=str(threshold),spectral_interval='strictly below threshold' if threshold else 'at or below zero',parity_certificates=rows,explicit_canonical_exceptional_space_dimension=count,original_complement_floor_lower=str(floor),threshold_margin_lower=str(down(floor-threshold)),original_spectral_count_upper=count,inherited_1250_effective_strong_dimension=1250-count))
 low,zero=targets
 assert low['original_spectral_count_upper']<prior['original_eigenvalues_strictly_below_one_hundredth_count_upper']
 assert zero['original_spectral_count_upper']<prior['original_nonpositive_spectral_dimension_upper']
 return dict(milestone='RC270',starting_commit='cbdb78b41af82ae8c06240286fea4d8918f58d44',
  input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,
  threshold_adapted_coverage_certificates=targets,exact_controls=controls(),
  original_eigenvalues_strictly_below_one_hundredth_count_lower=10,
  original_eigenvalues_strictly_below_one_hundredth_count_upper=608,
  original_nonpositive_spectral_dimension_upper=582,nonpositive_bound_includes_kernel_dimension=True,
  previous_below_one_hundredth_count_upper=609,previous_nonpositive_dimension_upper=609,
  threshold_specific_spaces_are_distinct=True,zero_threshold_count_not_used_as_one_hundredth_count=True,
  actual_canonical_Riesz_representatives_used=True,exceptional_space_invariance_claimed=False,
  minimum_possible_exceptional_dimension_claimed=False,original_arithmetic_allowances_unchanged=True,
  chosen_rational_augmentation_unchanged=True,chosen_rational_augmentation_rank_unchanged=639,
  exact_comparison_cutoffs_do_not_replace_actual_augmentation=True,
  old_positive_signed_pivots_preserved=True,old_pivots_subtracted_from_new_dimension=False,
  old_signed_Schur_dimension_unchanged=637,
  head_metrics_or_new_complement_responses_evaluated=False,old_inverse_budgets_transferred=False,
  new_coupled_Schur_positive_certified=False,full_signed_gap_positive_certified=False,
  original_full_auxiliary_norm_below_one_certified=False,
  finite_eight_canonical_inverse_width_preserved='485647/1000000',
  Stage_I_closed=False,RH=False,F4=False,Lean=False,
  next_cursor='RC271: use the 582-source positive-complement canonical reduction for unshifted positivity, or the 608-source reduction for the 0.01 census; certify all effective head, inverse and cross terms before closure')

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
 if args.replay:assert result==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC270 VALIDATED: below 0.01 <=608; nonpositive <=582; Stage I open',flush=True)
