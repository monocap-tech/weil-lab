"""RC269: exact integrated-contour coverage by 609 canonical moment sources."""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json
import validate_rpb108_rc268_two_pivot_schur_reduction as parent
import validate_rpb108_rc266_integrated_contour_augmentation as ellipse
ROOT=parent.ROOT; down=parent.down
PINS=dict(parent.PINS); HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc268_two_pivot_schur_reduction.json':'f1dc3240c5aaecd6eea34f2a60f4631774022657','notes/RPB108_RC268_TWO_PIVOT_SCHUR_REDUCTION_20261014.md':'3d6e2878e591e791b6ac63f1d2a1c52ee0862b69'})
HELPER_PINS['scripts/validate_rpb108_rc268_two_pivot_schur_reduction.py']='afc35a8d6a252eefdb63276f523331974660adfd'

def controls():
 # Polynomial moments of one parity have independent triangular leading terms.
 T=[[F(1)],[F(0),F(1)]]
 for n in range(1,12):
  v=[F(0)]+[2*c for c in T[n]]
  for j,c in enumerate(T[n-1]): v[j]-=c
  T.append(v)
 for j,t in enumerate(T):
  assert t[-1] == (1 if j==0 else 2**(j-1))
  assert all(c==0 for k,c in enumerate(t) if k%2!=j%2)
 # An exact coupled example: a strong complement does not certify the head.
 A=[[F(1),F(2)],[F(2),F(1)]]
 assert A[1][1]>F(1,100)
 assert A[0][0]-A[0][1]**2/A[1][1]==-3
 assert parent.inertia(A)==dict(positive=1,negative=1,zero=0)
 return dict(Chebyshev_parity_and_leading_coefficient_checked=True,
             coupled_positive_compressions_can_have_negative_Schur_complement=True,
             exact_complement_bound_does_not_close_head=True)

def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes()
  assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  if path.endswith('.json'): data[path]=json.loads(b)
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 old=get('112_parity_spectral_coverage'); ref=get('256_retained_band_inverse')
 kernel=get('115_rational_fourier_adjoint'); prior=get('268_two_pivot_schur_reduction')
 assert prior['both_actual_source_signed_pivots_positive']
 pi=F(kernel['rational_pi'])+F(kernel['rational_pi_error_upper'])
 rows=[]
 for parity,m in enumerate([474,745]):
  r=ref['retained_band_inverse_response_certificates'][parity]
  o=old['parity_coverage_certificates'][parity]
  gamma=F(r['original_canonical_reference_floor']); penalty=F(r['original_low_band_penalty'])
  U=F(r['rational_half_bandwidth'])
  assert gamma==F(o['reference_floor']) and penalty==F(o['low_band_penalty_upper'])
  assert U==F(o['frequency_cutoff_upper']) and F(o['high_frequency_reserve_lower'])>0
  candidates=[]; skipped=[]
  for k in sorted(range(120,181),reverse=reverse):
   radius=F(k,100); loglo,_,_=ellipse.coercive.log_interval(radius)
   gap=m*loglo-2*pi*ellipse.B*U*(radius-1/radius)/2
   if not 0<2*gap<100:
    skipped.append(dict(radius=str(radius),twice_gap_lower=str(2*gap),reason='outside positive exponential helper domain'))
    continue
   hs,proof=ellipse.contour(radius,m,parity,U,pi,reverse)
   assert proof['first_omitted_degree']==m
   # This exact comparison kernel annihilates the new moment complement.
   # It is not the chosen rational kernel and needs no finite-kernel error.
   candidates.append((hs,radius,proof))
  hs,radius,proof=min(candidates,key=lambda v:(v[0],v[1]))
  beta=down(gamma-penalty*hs); shifted=down(beta-F(1,100))
  degrees=list(range(parity,m,2)); rank=len(degrees)
  assert shifted>0 and rank<[248,391][parity]
  rows.append(dict(parity=o['parity'],rational_frequency_half_bandwidth=str(U),
   original_canonical_reference_floor=str(gamma),original_low_band_penalty_upper=str(penalty),
   exact_comparison_kernel_truncation_length=m,retained_native_Chebyshev_degrees=degrees,
   canonical_Riesz_moment_span_dimension=rank,largest_retained_native_degree=degrees[-1],
   finite_radius_grid_denominator=100,finite_radius_grid_numerators=list(range(120,181)),
   admissible_radius_count=len(candidates),skipped_radius_certificates=sorted(skipped,key=lambda v:F(v['radius'])),
   all_admissible_contour_certificates=[v[2] for v in sorted(candidates,key=lambda v:v[1])],
   selected_integrated_contour_certificate=proof,Fourier_restriction_squared_tail_upper=str(hs),
   original_canonical_complement_floor_lower=str(beta),shifted_complement_floor_at_one_hundredth_lower=str(shifted),
   original_strict_below_one_hundredth_count_lower=o['original_eigenvalues_strictly_below_one_hundredth_count_lower'],
   original_strict_below_one_hundredth_count_upper=rank,original_nonpositive_spectral_dimension_upper=rank,
   previous_coverage_dimension=o['parity_exceptional_dimension'],
   inherited_1250_effective_strong_dimension=625-rank))
  print('RC269 '+o['parity']+': rank '+str(rank)+'; canonical complement floor '+str(float(beta)),flush=True)
 count=sum(r['canonical_Riesz_moment_span_dimension'] for r in rows)
 assert count==609 and sum(r['inherited_1250_effective_strong_dimension'] for r in rows)==641
 floor=min(F(r['original_canonical_complement_floor_lower']) for r in rows)
 return dict(milestone='RC269',starting_commit='e6ad8ec50be23a3d7beab1922f6b15ad80744c78',
  input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,parity_coverage_certificates=rows,
  exact_controls=controls(),explicit_canonical_exceptional_space_dimension=count,
  original_floor_on_canonical_exceptional_orthogonal_complement=str(floor),
  original_eigenvalues_strictly_below_one_hundredth_count_lower=10,
  original_eigenvalues_strictly_below_one_hundredth_count_upper=count,
  original_nonpositive_spectral_dimension_upper=count,nonpositive_bound_includes_kernel_dimension=True,
  inherited_1250_effective_strong_dimension=641,
  previous_coverage_dimension=639,previous_nonpositive_dimension_upper=637,
  exact_kernel_comparison_not_actual_rational_augmentation=True,
  actual_canonical_Riesz_representatives_used=True,exceptional_space_invariance_claimed=False,
  minimum_possible_exceptional_dimension_claimed=False,
  old_positive_signed_pivots_preserved=True,old_pivots_subtracted_from_new_dimension=False,
  old_signed_Schur_dimension_unchanged=637,new_canonical_Schur_dimension=609,
  chosen_rational_augmentation_rank_unchanged=639,chosen_rational_augmentation_unchanged=True,
  new_canonical_head_metric_or_responses_evaluated=False,new_coupled_Schur_positive_certified=False,
  old_complement_inverse_budgets_transferred=False,full_signed_gap_positive_certified=False,
  original_full_auxiliary_norm_below_one_certified=False,
  finite_eight_canonical_inverse_width_preserved='485647/1000000',
  Stage_I_closed=False,RH=False,F4=False,Lean=False,
  next_cursor='RC270: exploit the 641-dimensional strong compression inside the inherited 1250 head, or construct the 609-source canonical Schur response; pay all head metrics, complement inverses, couplings and errors before positivity')

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
 if args.replay: assert result==json.loads(args.output.read_text())
 else: args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC269 VALIDATED: original canonical coverage 609; Stage I open',flush=True)
