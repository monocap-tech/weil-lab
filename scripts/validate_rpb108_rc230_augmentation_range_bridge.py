"""RC230: chosen rational augmentation range and D-energy operator bridge.

Analytic range/domain arguments are in the accompanying note. Exact controls
do not constitute actual original Weil actions or an auxiliary norm gate.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json, math
import validate_rpb108_rc229_stage_I_interface_audit as parent
p=parent.p
ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS); HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({
 'certificates/rpb108_rc229_stage_I_interface_audit.json':'8812dd8abf986b1e972931cf27402e0d2e2786f8',
 'certificates/rpb108_rc115_rational_fourier_adjoint.json':'92189b6472cdb9ae82bf4812e70fdd0072b06bc8'})
HELPER_PINS['scripts/validate_rpb108_rc229_stage_I_interface_audit.py']='ceda4aefa76126b4bf50b7236432c4c247c6a75e'
GRID=10**60
def down(x): return F(x.numerator*GRID//x.denominator,GRID)
def up(x): return -down(-x)
def rootup(x):
 n=math.isqrt(x.numerator*GRID**2//x.denominator)
 if F(n*n,GRID**2)<x:n+=1
 return F(n,GRID)
def digest_fraction(x):
 chunks=[]
 for v in [x.numerator,x.denominator]:
  b=v.to_bytes((v.bit_length()+7)//8,'big');chunks.extend([len(b).to_bytes(8,'big'),b])
 return hashlib.sha256(b''.join(chunks)).hexdigest()
def polynomial_budgets(mu,nu,source_bound,lam):
 """Outward recurrence encloses T_n(c); exact actions are conditional."""
 c=(nu+mu)/(nu-mu); assert c>1
 cur=(down(c),up(c)); diff=(down(c-1),up(c-1)); results=[]
 for n in range(1,10001):
  assert cur[0]>0
  if n<=24:
   exact=sum(F(math.comb(n,2*k))*c**(n-2*k)*(c*c-1)**k for k in range(n//2+1))
   assert cur[0]<=exact<=cur[1]
  eps=up(1/cur[0]); correction=up(lam*source_bound*eps**2/mu)
  target=F(1,10**(6 if not results else 12))
  if correction<=target:
   results.append(dict(response_correction_allowance=str(target),residual_polynomial_degree=n,inverse_polynomial_degree=n-1,Chebyshev_T_lower=str(cur[0]),relative_source_residual_upper=str(eps),response_correction_upper=str(correction),requires_exact_augmented_N_actions=True))
   if len(results)==2:return results
  # Positive coupled recurrence avoids artificial interval blow-up from
  # subtracting correlated T_(n-1) enclosures.
  diff=(down(diff[0]+2*(c-1)*cur[0]),up(diff[1]+2*(c-1)*cur[1]))
  cur=(down(cur[0]+diff[0]),up(cur[1]+diff[1]))
 raise AssertionError('degree ceiling')
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  raw=(ROOT/path).read_bytes()
  assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==sha,(path,'pin')
  data[path]=json.loads(raw) if path.endswith('.json') else raw.decode()
 get=lambda name:data['certificates/rpb108_rc'+name+'.json']
 old=get('229_stage_I_interface_audit'); kernel=get('115_rational_fourier_adjoint'); aug=get('114_positive_augmentation'); coverage=get('112_parity_spectral_coverage')
 assert old['accepted_gate_exactly_rechecked'] and old['accepted_eight_source_inverse_width']=='485647/1000000'
 assert kernel['rational_kernel_positive_augmentation_certified'] and kernel['Taylor_degree']==2400
 assert not kernel['rational_kernel_augmentation_identical_to_RC114_exact_kernel_claimed']
 rho=F(252,257); a=F(32125,230953); B=F(11,10)
 sl=F(get('129_four_vector_joint_moment')['actual_D_Gram_entry_lower'][0][0])/(2*B); assert sl>0
 pi=F(kernel['rational_pi']); assert pi>0
 rows=[]
 for parity in ['even','odd']:
  src=next(r for r in kernel['parity_rational_Fourier_adjoint_sources'] if r['parity']==parity)
  cov=next(r for r in coverage['parity_coverage_certificates'] if r['parity']==parity)
  oa=next(r for r in aug['parity_positive_augmentation_certificates'] if r['parity']==parity)
  op=next(r for r in oa['positive_augmentation_certificates'] if r['Young_parameter']=='1/4')
  offset=0 if parity=='even' else 1
  indices=list(range(offset,cov['maximum_native_degree']+1,2))
  assert len(indices)==src['retained_native_count']==cov['parity_exceptional_dimension']
  assert indices[-1]<=src['Taylor_degree']==2400
  zhalf=pi*B*F(src['rational_frequency_half_bandwidth']); assert zhalf>0
  coeff=F(1); diagonals=[]
  for j in range(indices[-1]+1):
   if j:coeff=coeff*zhalf/j
   if j in indices:
    lead=coeff*(1 if j==0 else 2); assert lead>0
    # No string conversion of the very large exact integers is needed.
    diagonals.append(dict(native_index=j,first_nonzero_monomial_degree=j,positive=True,numerator_bit_length=lead.numerator.bit_length(),denominator_bit_length=lead.denominator.bit_length(),leading_coefficient_sha256=digest_fraction(lead)))
  # The old exact-kernel H bounds A_Q above because its augmentation is
  # positive. Add the chosen rational augmentation afresh; never transfer
  # the old upper by an unproved identification of frequency bands.
  delta2=F(src['finite_model_squared_J_approximation_error_upper']); delta=rootup(delta2)
  x2=up((rootup(rho)+delta)**2); f2=up((1+delta)**2)
  lam=F(src['polynomial_model_augmentation_coefficient']); eta=F(src['polynomial_model_positive_augmentation_floor_lower'])
  bold=F(op['positive_augmented_operator_upper']); bhat=up(bold+lam*x2)
  mu=down(eta*a); nu=2*bhat; source=up(f2/sl)
  assert 0<mu<nu and lam>0
  rows.append(dict(parity=parity,rank=len(indices),retained_native_indices=indices,maximum_physical_polynomial_degree=indices[-1],positive_triangular_diagonal_controls=diagonals,rational_frequency_half_bandwidth=src['rational_frequency_half_bandwidth'],Taylor_degree=2400,chosen_canonical_augmentation_floor=str(eta),chosen_canonical_factor_squared_norm_upper=str(x2),chosen_physical_factor_squared_norm_upper=str(f2),inherited_exact_kernel_H_upper=str(bold),fresh_rational_H_upper=str(bhat),fresh_H_upper_derivation='A_Q <= H_RC114 <= b_old I; Hhat <= (b_old + lambda ||Xhat||^2) I',augmentation_coefficient=str(lam),D_energy_augmented_N_lower=str(mu),D_energy_augmented_N_upper=str(nu),D_energy_source_operator_squared_norm_upper=str(source),conditional_exact_action_inverse_budgets=polynomial_budgets(mu,nu,source,lam)))
 # Exact noncommuting control in actual physical, canonical and D metrics.
 D=[[F(2),F(0)],[F(0),F(3)]]; L=[[F(3),F(1,3)],[F(1,3),F(5)]]
 K=[[-F(1,2),F(1,5)],[F(1,5),-F(1,3)]]; FF=[[F(1),F(1,2)],[F(1,3),F(2,3)]]; lam=F(9,4)
 Di=p.inv(D); Li=p.inv(L); Ft=p.trans(FF)
 G=p.add(p.add(L,K),p.scale(lam,p.mm(Ft,FF))); M=p.mm(Di,L); N=p.mm(Di,G); H=p.mm(Li,G)
 assert p.psd(p.add(L,p.scale(a,D),-1)) and p.psd(p.add(p.scale(F(2),D),L,-1)) and p.psd(G)
 assert p.mm(M,H)==N and p.mm(M,N)!=p.mm(N,M)
 response=p.mm(p.inv(H),p.mm(Li,Ft)); direct=p.mm(p.inv(N),p.mm(Di,Ft))
 assert response==direct==p.mm(p.inv(G),Ft)
 exact=p.mm(FF,direct); Y=[[F(1,7),-F(1,9)],[F(2,11),F(1,13)]]
 residual=p.add(p.mm(Di,Ft),p.mm(N,Y),-1)
 center=p.add(p.add(p.mm(FF,Y),p.mm(p.trans(Y),Ft)),p.mm(p.trans(Y),p.mm(G,Y)),-1)
 correction=p.mm(p.trans(residual),p.mm(D,p.mm(p.inv(N),residual)))
 assert exact==p.add(center,correction) and p.psd(correction)
 assert exact!=p.add(center,correction,-1)
 assert sum(r['rank'] for r in rows)==639
 return dict(milestone='RC230',starting_commit='83ac4f6b37176c9ecc3b9b3085e0294819a01368',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,chosen_augmentation='RC115 rational polynomial Fourier kernel Hhat=A_Q+lambda Xhat*Xhat, separately in each parity',canonical_embedding_squared_norm_upper=str(rho),canonical_metric_D_equivalence_lower=str(a),physical_D_floor_lower=str(sl),parity_source_range_and_bridge_certificates=rows,full_chosen_augmentation_rank=639,exact_full_source_range_specified=True,range_Xhat_adjoint='actual canonical native moment/Riesz span W639, even 248 plus odd 391',range_Fhat_adjoint='physical Chebyshev polynomial spans of the retained parity indices',range_D_inverse_Fhat_adjoint='same finite parity polynomial spans, represented in D energy',bridge_identities=['N=M Hhat','Hhat^-1 Xhat*=N^-1 D^-1 Fhat*','Bhat=lambda Fhat N^-1 D^-1 Fhat*'],bridge_requires_commuting_M_and_N=False,bridge_form_domain_and_metric_proof_in_note=True,residual_correction_sign='added',residual_identity='Bhat/lambda = Fhat Y + Y* Fhat* - Y* D N Y + e* D N^-1 e; e=D^-1 Fhat* - N Y',residual_sandwich='(e* D e)/nu <= e* D N^-1 e <= (e* D e)/mu',physical_source_rounding_rule='||D^-1 delta_q||_D^2 <= ||delta_q||_physical^2 / s_lower',noncommuting_exact_control=dict(D=p.ser(D),L=p.ser(L),K=p.ser(K),Fhat=p.ser(FF),lambda_value=str(lam),M=p.ser(M),N=p.ser(N),Hhat=p.ser(H),trial=p.ser(Y),exact_response_without_lambda=p.ser(exact),center=p.ser(center),added_correction=p.ser(correction),all_bridge_and_residual_identities_verified=True,is_actual_Weil_action=False),finite_eight_source_gate_preserved='485647/1000000',exact_factorization_through_eight_channels_exhausts_chosen_augmentation=False,dense_639_Gram_or_639_solves_required=False,numerical_frequency_Gram_conditioning_certified=False,full_frequency_Gram_evaluated=False,actual_original_Weil_actions_performed=False,actual_augmented_N_actions_performed=False,actual_augmented_inverse_responses_computed=False,original_augmented_response_norm_below_one_certified=False,remaining_obligations=['actual original K and rational augmentation action contracts in D energy, both parities','actual residual/error bounds for a full-range augmented inverse representation','actual auxiliary metric or equivalent uniform frequency operator bound','full Bhat norm strictly below one and Stage I assembly'],Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC231: realize a paid original K/rational augmentation action interface for D-energy polynomial sources; the exact range is now specified but the full augmented response norm remains open')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
 if args.replay:assert result==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC230 PASS: exact chosen rank 639 and noncommuting D-energy bridge; actual augmented response gate open',flush=True)
