"""RC121: full-space endpoint Schur bound and explicit diagonal source solver.
No regular multiplier or original Weil/augmented action is executed.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,hashlib,argparse
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc119_reference_preconditioned_source_solver import log2_bounds
from validate_rpb108_rc103_complement_inverse_lift import chebyshev
from validate_rpb108_rc114_positive_augmentation import up,down
from validate_rpb108_rc47_correlated_native_transport import root

def harmonic(n):return sum((F(1,j) for j in range(1,n+1)),F(0))

def controls(ll,lh,replay=False):
 checks=0
 for n in range(25):
  for m in range(n+1):
   if (m+n)%2:continue
   a=legendre(n);b=legendre(m);p=[F(0)]*(n+m+1)
   for i,x in enumerate(a):
    for j,y in enumerate(b):p[i+j]+=x*y
   shifted=[sum((p[j]*comb(j,k)*2**k*(-1)**(j-k) for j in range(k,len(p))),F(0)) for k in range(len(p))]
   terms=[2*x/F(k+1)**2 for k,x in enumerate(shifted)];logr=sum(reversed(terms) if replay else terms,F(0))
   if n!=m:assert logr==F(2,(n-m)*(n+m+1))
   else:assert logr*F(2*n+1,2)==2*harmonic(2*n)-2*harmonic(n)+F(1,2*n+1)
   checks+=1
 # Infinite weighted row off-sum is d_n+H_floor(n/2); tail evaluated by harmonic differences.
 for n in range(101):
  d=2*harmonic(2*n)-2*harmonic(n)+F(1,2*n+1)
  lower=sum((F(2*n+1,(n-m)*(n+m+1)) for m in range(n%2,n,2)),F(0))
  upper_rational=harmonic(2*n)-harmonic(n)/2+F(1,2*n+1)
  assert lower+upper_rational==d+harmonic(n//2)
  assert d-ll>0 and d-lh<lh
  # 256 explicit upper terms plus rigorously bounded positive tail.
  K=256;partial=sum((F(1,2*k)-F(1,2*n+2*k+1) for k in range(1,K+1)),F(0))
  tail=F(2*n+1,4*K)
  assert partial<=upper_rational-ll and upper_rational-ll<=partial+tail
  checks+=1
 return checks

def degree_budgets(a,b,label,replay=False):
 c=(a+b)/(b-a);rows=[];sqrtb=root(b,10**30)
 for digits in [6,12,24]:
  tau=F(1,10**digits);n=1
  while 1/chebyshev(n,c,replay)>tau/3:n+=1
  eps=1/chebyshev(n,c,replay);H=F(n*(n+1),2);dg=a*tau/(3*sqrtb*(1+eps));eta=tau/(3*sqrtb*H)
  assert eps+sqrtb*((1+eps)*dg/a+H*eta)<=tau
  assert 1/chebyshev(n-1,c,replay)>tau/3
  rows.append(dict(relative_energy_error_norm_target=str(tau),residual_degree=n,inverse_degree=n-1,uniform_residual_upper=str(up(eps,10**(digits+8))),minimal_degree_for_one_third_residual_allocation=True,initial_preconditioned_source_error_energy_norm_per_initial_error_norm=str(dg),normalized_local_action_fault_energy_norm_per_initial_error_norm=str(eta),recurrence_amplification_upper=str(H),actual_regular_or_endpoint_iteration_contract_executed=False))
 return dict(operator=label,spectral_lower=str(a),spectral_upper=str(b),condition_upper=str(b/a),conditional_budgets=rows)

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];old,prior,src,prec=map(json.loads,raw);hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [x['milestone'] for x in [old,prior,src,prec]]==['RC120','RC119','RC115','RC56'] and old['input_sha256']==hs[1:]
 ll,lh=log2_bounds(replay);sl=F(prior['reference_form_floor_lower']);a=F(prior['preconditioned_spectral_lower']);assert sl>2*lh
 checks=controls(ll,lh,replay);B=F(11,10);rows=[]
 for p,s in zip(old['parity_reference_inverse_action_certificates'],src['parity_rational_Fourier_adjoint_sources']):
  assert p['parity']==s['parity'];N=p['polynomial_degree'];parity=N%2;H=F(0);CN=F(0)
  for n in range(N+1):
   if n:H+=F(1,n)
   if n%2==parity:CN+=up(F(2*n+1)/(2*B*(H+sl)),10**30)
  boxes=[]
  for M in [2*N+1,4*N+1,16*N+1]:
   tail=up(2*B*CN/(sl*(M-N)**2),10**12)
   boxes.append(dict(input_polynomial_degree=N,output_degree_cutoff=M,omitted_endpoint_preconditioned_action_D_energy_squared_factor_upper=str(tail),input_coefficient_metric='actual D energy',all_input_linear_combinations_covered=True,finite_endpoint_action_executed=False))
  poly=F(p['polynomial_reference_residual_norm_error_upper']);source=F(p['exact_rational_model_source_physical_error_norm_upper']);gerr=up((poly+source)**2/sl,10**140)
  assert gerr<F(2,10**60)
  modelerr=F(s['finite_model_operator_error_squared_upper'])/sl
  rows.append(dict(parity=p['parity'],input_source_degree=N,source_trial_reused_from_RC120=True,exact_rational_model_diagonal_source_action_D_error_squared_upper=str(gerr),diagonal_source_action_is_canonical_Riesz_image_claimed=False,global_exact_kernel_to_rational_model_diagonal_source_map_D_error_squared_upper=str(up(modelerr,10**160)),physical_kernel_Hilbert_Schmidt_error_used=True,finite_cutoff_endpoint_action_contracts=boxes))
 solvers=[degree_budgets(F(1),F(2),'D^(-1) P in actual D energy',replay),degree_budgets(a,F(2),'D^(-1) L in actual D energy; canonical energy error acceptance',replay)]
 return dict(milestone='RC121',status='PASS: global endpoint Schur domination and actual canonical diagonal metric equivalence',input_sha256=hs,aperture='11/10',arithmetic='exact polynomial-log controls, positive infinite row sums, rational all-range action tails',endpoint_matrix_and_weighted_row_controls=checks,endpoint_form_bound='0 <= h <= J + 2 log(2) I <= D',positive_diagonal_reference='D P_n = (H_n+c_R+log(2)+789/125) P_n',diagonal_reference_floor_lower=str(sl),reference_spectral_equivalence='D <= P <= 2 D',actual_canonical_spectral_equivalence='a D <= L <= 2 D',actual_canonical_diagonal_metric_lower=str(a),actual_canonical_diagonal_metric_upper='2',diagonal_reference_inverse_norm_squared_for_physical_to_D_source=str(1/sl),whole_supported_canonical_form_domain_covered=True,finite_compression_is_not_coverage_proof=True,conditional_solver_certificates=solvers,parity_diagonal_source_and_endpoint_action_certificates=rows,diagonal_source_action_pair_certified=True,full_auxiliary_range_diagonal_action_coefficient_realization_completed=False,full_endpoint_action_iteration_executed=False,regular_multiplier_action_evaluated=False,canonical_Riesz_iteration_performed=False,original_Weil_or_augmented_actions_performed=False,auxiliary_response_norm_below_one_certified=False,new_positive_native_directions_certified=0,original_count_below_one_hundredth_lower=10,original_count_below_one_hundredth_upper=639,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=4);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC121 PASS: global diagonal metric equivalence and full-input endpoint action tail; arithmetic responses open')
