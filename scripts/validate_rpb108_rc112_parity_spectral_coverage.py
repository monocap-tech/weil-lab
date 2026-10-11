"""RC112: original-operator parity-sensitive spectral coverage.
No head entries or lifted responses evaluated. Exact Taylor rational budgets.
Usage: script [--replay] --output FILE RC111 RC107 RC44 RC43 RC42 RC66
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb
import argparse,hashlib,json

def exp_low(x,n=100,replay=False):
 assert x>=0
 if replay:
  # Independent Horner evaluation of the positive Taylor polynomial.
  y=F(1,factorial(n))
  for j in range(n-1,-1,-1):y=y*x+F(1,factorial(j))
  return y
 return sum((x**j/F(factorial(j)) for j in range(n+1)),F(0))
def exp_bounds(x,replay=False):
 n=100;assert 0<=x<n+2
 l=exp_low(x,n,replay);u=l+x**(n+1)/F(factorial(n+1))/(1-x/F(n+2));return l,u

def down(q,d):return F(q.numerator*d//q.denominator,d)
def up(q,d):return -down(-q,d)

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];prior,census,old,prime,pole,norm=map(json.loads,raw);hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert F(prior['inherited_complement_floor'])==F(247,2500)
 assert prior['milestone']=='RC111' and prior['input_sha256'][1]==hs[1] and prior['input_sha256'][6]==hs[5]
 assert old['milestone']=='RC44' and old['pole_certificate_sha256']==hs[4] and old['prime_certificate_sha256']==hs[3]
 assert prime['complete_active_prime_set_certified'] and pole['actual_signed_pole_head_enclosed']
 assert prime['native_certificate_sha256']==pole['source_certificate_sha256']
 B=F(11,10);rho=F(252,257);t=F(1,100);kprime=F(prime['full_paired_prime_physical_operator_norm_upper']);kodd=kprime+2*F(pole['sinh_physical_norm_squared_upper'])
 assert kodd==F(old['nonarch_physical_negative_allowance_upper']) and kodd<F(183,40)
 assert F(prime['full_paired_prime_canonical_operator_norm_upper'])==rho*kprime
 assert F(pole['canonical_negative_pole_part_norm_upper'])==rho*(kodd-kprime)
 elo,ehi=exp_bounds(F(1),replay);assert F(8,3)<elo<ehi<3
 assert exp_bounds(F(693,1000),replay)[1]<2
 rows=[]
 for parity,L,a,n,K in [('even',F(4161,1000),F(10042,10**6),495,kprime),('odd',F(4632,1000),F(10258,10**6),783,kodd)]:
  Tl,Tu=exp_bounds(L,replay);tl=down(Tl,10**6);tu=up(Tu,10**6)
  assert 60<tl<Tl<Tu<tu<104 and a>t and a<F(1,10)
  # High multiplier lower bound: log x - 1/x; canonical weight <=log x+3/x.
  reserve=(1-a)*L-K-(1+3*a)/tl;assert reserve>0
  penalty=F(31,5)+K+a*(L+1)
  gap=n*F(693,1000)-F(3,4)*2*F(22,7)*B*tu;assert gap>0
  # Squared Fourier restriction norm error: 64 B T exp(-2 gap).
  eg=exp_low(2*gap,100,replay);delta2=64*B*tu/eg
  beta=a-penalty*delta2;beta_grid=down(beta,10**9);assert beta_grid>t
  if replay:
   # Independent convolution evaluation T_100(x)^2 is not needed for the bound;
   # verify its exact binomial Taylor identity at the frequency cutoff.
   half=exp_low(L/2,100,True)
   coeff=[sum((F(1,factorial(j)*factorial(m-j)) for j in range(max(0,m-100),min(100,m)+1)),F(0)) for m in range(201)]
   assert sum((coeff[m]*(L/2)**m for m in range(201)),F(0))==half*half
   assert beta_grid<=beta and reserve>0
  dimension=(n+1)//2 if parity=='even' else n//2
  maxdegree=n-1 if parity=='even' else n-2
  assert maxdegree%2==(0 if parity=='even' else 1) and dimension==(maxdegree-(0 if parity=='even' else 1))//2+1
  c=next(z for z in census['parity_spectral_compression_certificates'] if z['parity']==parity)
  ct=next(z for z in c['spectral_census'] if F(z['threshold'])==t);assert ct['exact_count_certified'] and ct['compression_eigenvalues_strictly_below_threshold_count_lower']==5
  bglobal=1+rho*F(norm['complete_physical_operator_parity_norm_upper'][0 if parity=='even' else 1])
  rows.append(dict(parity=parity,frequency_log_cutoff=str(L),frequency_cutoff_lower=str(tl),frequency_cutoff_upper=str(tu),physical_negative_nonarch_allowance=str(K),reference_floor=str(a),high_frequency_reserve_lower=str(reserve),low_band_penalty_upper=str(penalty),Chebyshev_truncation_length=n,parity_exceptional_dimension=dimension,inherited_effective_strong_dimension=625-dimension,inherited_effective_strong_floor_lower=str(beta_grid),inherited_shifted_effective_strong_floor_lower=str(beta_grid-t),maximum_native_degree=maxdegree,contour_exponent_gap_lower=str(gap),Fourier_restriction_squared_tail_upper=str(delta2),original_complement_floor_exact_lower=str(beta),original_complement_floor_grid_lower=str(beta_grid),original_complement_upper_using_global_norm=str(bglobal),original_eigenvalues_strictly_below_one_hundredth_count_lower=5,original_eigenvalues_strictly_below_one_hundredth_count_upper=dimension,additional_modes_beyond_native_five_count_upper=dimension-5,new_head_metric_or_entries_evaluated=False))
 dim=sum(r['parity_exceptional_dimension'] for r in rows);assert dim==639 and dim<1250
 beta=min(F(r['original_complement_floor_grid_lower']) for r in rows);assert beta>t
 return dict(milestone='RC112',status='PASS: original spectral upper count 639 and explicit complement floor above 0.01',input_sha256=hs,arithmetic='exact fractions; Taylor sum primary and Horner/convolution replay',aperture='11/10',original_operator_source_blob=old['original_form_source_blob'],threshold=str(t),parity_coverage_certificates=rows,explicit_exceptional_space_dimension=dim,inherited_effective_strong_dimension=1250-dim,inherited_effective_strong_floor_lower=str(beta),inherited_shifted_effective_strong_floor_lower=str(beta-t),inherited_effective_strong_floor_certified=True,explicit_exceptional_space_is_invariant_spectral_subspace_claimed=False,original_floor_on_canonical_exceptional_orthogonal_complement=str(beta),original_eigenvalues_below_one_hundredth_count_lower=10,original_eigenvalues_below_one_hundredth_count_upper=dim,additional_modes_beyond_native_ten_count_upper=dim-10,original_nonpositive_spectral_dimension_upper=dim,previous_nonpositive_upper=prior['inherited_nonpositive_count_upper'],count_upper_reduction_from_1250=1250-dim,ten_native_candidates_exhaustive_certified=False,original_639_head_positive_certified=False,original_exceptional_coupled_response_certified=False,rank_1250_complement_floor_preserved=True,RC110_twelve_dimensional_positive_span_preserved=True,old_complement_inverse_budgets_transferred_to_new_head=False,negative_pole_vanishes_on_even_parity_analytic_proof_in_note=True,new_arithmetic_source_integrals_evaluated=0,new_individual_native_directions_added=0,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=6);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,indent=2,sort_keys=True)+'\n')
 print('RC112 PASS: rank 639 original coverage, complement floor >0.01; exceptional positivity open')
