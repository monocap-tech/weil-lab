"""RC75: weighted Schur bound for complete paired-prime translations.

A full physical operator improvement, plus a physical finite-rank tail
nondecay witness. The latter is NOT a canonical source obstruction.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,sys
from validate_rpb108_rc30_interval_metric import I
from validate_rpb108_rc42_native_signed_pole_head import outward,rational_interval
from validate_rpb108_rc48_prime_source_covariance import geometry
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,block,cong,relative
N=22;B=F(11,10);RHO=F(252,257)
def diag(x):return [[v*F(i==j) for j in range(len(x))] for i,v in enumerate(x)]
def progress(s):print(s,file=sys.stderr,flush=True)

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];previous,polecert,residual,source,enriched,head,native,prime=map(json.loads,raw)
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert previous['input_sha256'][:7]==hashes[1:]
 assert head['actual_orthogonal_projection_rank_certified']==38
 terms,segs=geometry(prime);rows={x['n']:x for x in prime['active_prime_powers']}
 assert len(terms)==14 and len(segs)==15 and sorted(rows)==[2,3,4,5,7,8,9]
 # Use the previously certified rational parameter boxes for both passes.
 boxes=[];endpoints={'left':(F(-1),F(-1)),'right':(F(1),F(1))}
 for term in terms:
  row=rows[term['n']];el,eh=F(row['translation_lower'])/B,F(row['translation_upper'])/B
  cl,ch=F(row['coefficient_lower']),F(row['coefficient_upper'])
  dl,dh=(el,eh) if term['sign']==1 else (-eh,-el)
  assert I(dl).l<=term['offset'].l<=term['offset'].h<=I(dh).h
  assert I(cl).l<=(-term['coefficient']).l<=(-term['coefficient']).h<=I(ch).h
  boxes.append((rational_interval(cl,ch),rational_interval(dl,dh)))
  if term['sign']==1:endpoints[str(term['n'])+'+']=(1-eh,1-el)
  else:endpoints[str(term['n'])+'-']=(-1+el,-1+eh)
 order=[segs[0][0]]+[s[1] for s in segs]
 assert all(endpoints[a][1]<endpoints[z][0] for a,z in zip(order,order[1:]))
 def controls(a,k,segment):
  ln,rn,_,_,active=segment;l=endpoints[ln][0];r=endpoints[rn][1]
  den=[F(1)+a*l*l,F(1)+a*l*r,F(1)+a*r*r];assert min(den)>0
  if replay:
   out=[I(k*x) for x in den]
   for h in active:
    c,d=boxes[h];shifted=[1+a*(I(l)+d)*(I(l)+d),1+a*(I(l)+d)*(I(r)+d),1+a*(I(r)+d)*(I(r)+d)]
    out=[v-c*w for v,w in zip(out,shifted)]
  else:
   c0=I(k);c1=I(0);c2=I(k*a)
   for h in active:
    c,d=boxes[h];c0-=c*(1+a*d*d);c1-=2*a*c*d;c2-=a*c
   out=[c0+c1*l+c2*l*l,c0+c1*F(l+r,2)+c2*l*r,c0+c1*r+c2*r*r]
  return out
 def valid(a,k):return all(min(x.l for x in controls(a,k,s))>=0 for s in segs)
 profiles=[]
 for index,a in enumerate([F(0),F(1,4),F(5,16),F(3,8),F(7,16),F(1,2),F(3,4),F(1)]):
  hi=F(1)
  while not valid(a,hi):hi*=2
  lo=hi/2
  for _ in range(14):
   mid=(lo+hi)/2
   if valid(a,mid):hi=mid
   else:lo=mid
  assert valid(a,hi);proof=[]
  for s in segs:
   out=controls(a,hi,s);enc=[]
   for q,x in enumerate(out):
    if saved is None:value=outward(x,10**20)
    else:
     value=tuple(map(F,saved['weighted_Schur_profile_certificates'][index]['segment_Bernstein_certificates'][len(proof)]['nonnegative_control_enclosures'][q]))
     assert I(value[0]).l<=x.l<=x.h<=I(value[1]).h
    assert value[0]>=0;enc.append(list(map(str,value)))
   proof.append(dict(left_knot=s[0],right_knot=s[1],enlarged_physical_scaled_interval=[str(endpoints[s[0]][0]),str(endpoints[s[1]][1])],active_translation_indices=s[4],nonnegative_control_enclosures=enc))
  profiles.append(dict(weight_profile='h(t)=1+a*t^2',a=str(a),complete_paired_prime_physical_operator_norm_upper=str(hi),segment_Bernstein_certificates=proof))
 best=min(profiles,key=lambda x:F(x['complete_paired_prime_physical_operator_norm_upper']));kp=F(best['complete_paired_prime_physical_operator_norm_upper'])
 oldkp=F(prime['full_paired_prime_physical_operator_norm_upper']);assert kp<oldkp
 progress('weighted full prime norm '+str(kp)+' profile a='+best['a'])
 # Localized orthonormal high-frequency physical inputs: only n=2,3
 # translations intersect the aperture; all four output pieces are disjoint.
 eps=F(1,10000);ell={n:(F(x['translation_lower']),F(x['translation_upper'])) for n,x in rows.items()}
 assert ell[3][1]+eps<B and min(ell[n][0] for n in rows if n>=4)-eps>B
 pieces=[(-ell[3][1]-eps,-ell[3][0]+eps),(-ell[2][1]-eps,-ell[2][0]+eps),(ell[2][0]-eps,ell[2][1]+eps),(ell[3][0]-eps,ell[3][1]+eps)]
 assert all(-B<l<r<B for l,r in pieces) and all(x[1]<y[0] for x,y in zip(pieces,pieces[1:]))
 physical_tail_lower2=2*sum((F(rows[n]['coefficient_lower'])**2 for n in [2,3]),F(0));assert physical_tail_lower2>1
 # Propagate the improved full norm through the unchanged actual projection.
 arch=F(previous['projected_arch_physical_to_canonical_norm_upper_divided_by_sqrt_rho']);beta=[F(x['projected_physical_to_canonical_pole_norm_upper_divided_by_sqrt_rho']) for x in polecert['signed_pole_range_projection_certificates']]
 effective=[arch+kp+x for x in beta];Ep=matrix(enriched['enriched_actual_physical_Riesz_error_Gram_Loewner_upper']);V=matrix(enriched['enriched_native_trial_coefficients']);mass=list(map(F,enriched['physical_mass']))
 if replay:
  T=[[sum((mass[q]*V[q][i]*V[q][j] for q in range(64)),F(0)) for j in range(N)] for i in range(N)];rawE=cong(diag([effective[i%2] for i in range(N)]),Ep)
 else:T=cong(V,diag(mass));rawE=[[effective[i%2]*effective[j%2]*Ep[i][j] for j in range(N)] for i in range(N)]
 nu=F(1,65536);delta=F(source['actual_source_approximation_operator_error_upper'])
 E=rounded_bound(add(scale(rawE,1+nu),T,(1+1/nu)*delta**2),1,10**24)[0];Ecan=scale(E,RHO)
 Eold=matrix(previous['projected_transfer_equivalent_Gram_divided_by_rho']);assert psd(E) and psd(add(Eold,E,-1))
 W=matrix(residual['residual_certificates'][1]['nominal_physical_polynomial_residual_Gram_Loewner_upper']);Mlo=matrix(enriched['enriched_actual_native_Gram_Loewner_lower'])
 oldA=matrix(previous['refined_actual_rank_38_projected_old_source_Gram_Loewner_upper']);oldt=[F(x['Young_parameter']) for x in previous['parity_residual_certificates']]
 def upper(ts):return rounded_bound([[RHO*((1+ts[i%2])*W[i][j]+(1+1/ts[i%2])*E[i][j]) for j in range(N)] for i in range(N)],1,10**24)[0]
 baseline=upper(oldt);assert psd(add(oldA,baseline,-1))
 selected=[];parity=[]
 for p in [0,1]:
  tests=[]
  for t in [F(1,2),F(5,8),F(3,4),F(7,8),F(1),F(9,8)]:
   Ap=scale(add(scale(block(W,p),1+t),block(E,p),1+1/t),RHO);tests.append((relative(Ap,block(Mlo,p)),t))
  lam,t=min(tests);selected.append(t);parity.append(dict(parity='even' if p==0 else 'odd',Young_parameter=str(t),candidate_certificates=[dict(Young_parameter=str(q),upper=str(l)) for l,q in tests]))
 A=upper(selected);assert psd(A)
 for p in [0,1]:
  lam=relative(block(A,p),block(Mlo,p));parity[p]['actual_rank_38_residual_relative_original_canonical_input_Gram_upper']=str(lam)
  if replay:
   Ci=inverse(block(matrix(native['chebyshev_to_legendre']),p));assert psd(cong(Ci,add(scale(block(Mlo,p),lam),block(A,p),-1)))
 bound=max(F(x['actual_rank_38_residual_relative_original_canonical_input_Gram_upper']) for x in parity);prior=F(previous['actual_rank_38_relative_bound_for_existing_22_source_inputs']);assert bound<prior
 return dict(milestone='RC75',status='PASS',input_sha256=hashes,source_input_features=list(range(N)),actual_projection_target_features=list(range(38)),
  weighted_Schur_profile_certificates=profiles,selected_weighted_Schur_certificate=best,
  prior_full_prime_physical_operator_norm_upper=str(oldkp),complete_paired_prime_physical_operator_norm_upper=str(kp),
  full_prime_operator_norm_improved=True,projection_specific_prime_norm_decay_certified=False,
  physical_noncompact_tail_certificate=dict(input_halfwidth=str(eps),orthonormal_sequence='u_j(x)=1_{[-eps,eps]} exp(i*pi*j*x/eps)/sqrt(2*eps)',active_output_prime_powers=[2,3],disjoint_output_interval_enclosures=[[str(x),str(y)] for x,y in pieces],any_finite_rank_physical_projection_tail_operator_norm_squared_lower=str(physical_tail_lower2),scope='physical L2 polynomial projection; NOT the canonical adjoint or actual source leakage'),
  physical_noncompactness_is_canonical_source_obstruction=False,
  projected_canonical_source_transfer_Gram_Loewner_upper=serialize(Ecan),projected_transfer_equivalent_Gram_divided_by_rho=serialize(E),projected_transfer_Loewner_improves_RC74=True,
  unchanged_Young_parameters_residual_upper=serialize(baseline),unchanged_parameters_whole_residual_Loewner_improvement_certified=True,
  refined_actual_rank_38_projected_old_source_Gram_Loewner_upper=serialize(A),parity_residual_certificates=parity,
  actual_rank_38_relative_bound_for_existing_22_source_inputs=str(bound),prior_RC74_relative_bound=str(prior),certified_fractional_upper_bound_reduction=str(1-bound/prior),
  required_scalar_source_budget_certified=False,actual_rank_38_scalar_budget_failure_proved=False,thirty_eight_source_input_covariance_evaluated=False,
  enlarged_Weil_floor_certified=False,analytic_Schur_lemma_Lean_formalized=False,whole_aperture_positivity_extended=False,RH=False,F4=False)

if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 defaults=[base/n for n in ['rpb108_rc74_projected_arch_transfer.json','rpb108_rc73_projected_pole_transfer.json','rpb108_rc71_thirty_eight_projected_old_source.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc70_thirty_eight_native_projection.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc43_native_prime_head.json']]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True,saved)==saved
  print('PASS: independent shifted-weight Bernstein controls, support geometry, physical tail intervals and canonical transfer comparisons')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
