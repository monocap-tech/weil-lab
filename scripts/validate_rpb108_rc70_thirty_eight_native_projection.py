"""RC70: certified 38-feature actual native projection and nested extension.

Uses RC67's actual 64-mode metric envelope, not a nominal projection.
No 38-feature source budget, Weil floor, or complement floor is claimed.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc59_twenty_two_native_projection import chebyshev_conversion,nearest

N=38;DIM=64;OLD=22;RHO=F(252,257)
def add(A,B,t=F(1)):return [[x+t*y for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(A,t):return [[t*x for x in a] for a in A]
def diag(d):return [[x*F(i==j) for j in range(len(d))] for i,x in enumerate(d)]
def sub(A,lo,hi):return [a[lo:hi] for a in A[lo:hi]]
def cong(C,A):return mm(mm(tr(C),A),C)
def positive_parity(A):
 assert A==tr(A)
 assert all(A[i][j]==0 for i in range(len(A)) for j in range(len(A)) if (i-j)%2)
 return all(psd([[A[i][j] for j in range(p,len(A),2)] for i in range(p,len(A),2)]) for p in [0,1])
def progress(s):print(s,file=sys.stderr,flush=True)

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];enriched,prior,leakage=map(json.loads,raw)
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert enriched['input_sha256'][1]==hashes[1]
 assert leakage['input_sha256'][:2]==hashes[:2]
 assert leakage['necessary_consecutive_native_head_count_for_this_budget_lower']==N
 G=matrix(enriched['recentered_nominal_metric_center']);mass=list(map(F,enriched['physical_mass']))
 delta=F(enriched['actual_recentered_metric_mass_error_upper']);D=diag(mass)
 assert len(G)==DIM and mass==[F(11,5*(2*i+1)) for i in range(DIM)]
 Gu=add(G,D,delta);Gl=add(G,D,-delta)
 assert positive_parity(add(Gl,D,-1))
 C,polys=chebyshev_conversion(N);Ci=inverse(C)
 assert sub(C,0,OLD)==matrix(prior['chebyshev_to_legendre'])
 X=[[mass[i]*C[i][j] if i<N else F(0) for j in range(N)] for i in range(DIM)]
 P=cong(C,diag(mass[:N]));Mu=scale(P,RHO)
 progress('exact 64-mode Ritz solves')
 Gi=inverse(G);Gui=inverse(Gu)
 exactV=mm(Gi,X);V=[[nearest(x,10**40) for x in row] for row in exactV]
 assert [a[:OLD] for a in V]==matrix(enriched['enriched_native_trial_coefficients'])
 A=mm(mm(tr(X),Gui),X);Ml,rounding=rounded_bound(A,-1,10**30)
 # Identical Ritz solve on the old columns; additional rows of rounding
 # are tiny but must be paid rather than asserting literal prefix equality.
 assert positive_parity(add(Mu,Ml,-1))
 LegLower=cong(Ci,Ml);LegMass=diag(mass[:N])
 low=F(0);high=RHO
 for _ in range(10):
  mid=(low+high)/2
  if positive_parity(add(LegLower,LegMass,-mid)):low=mid
  else:high=mid
 alpha=low;assert alpha>0 and positive_parity(add(Ml,P,-alpha))
 progress('38-feature Gram and physical inverse bounds certified')
 Pi=inverse(P);Id=diag([F(1)]*N)
 assert mm(P,Pi)==mm(Pi,P)==Id
 invlo=scale(Pi,1/RHO);invup=scale(Pi,1/alpha)
 T=cong(V,D);J=mm(tr(X),V);GT=cong(V,Gu)
 Ec,eround=rounded_bound(add(add(add(Mu,J,-1),tr(J),-1),GT),1,10**30)
 assert positive_parity(Ec);Ep=scale(Ec,RHO)
 # Exact physical Schur complement for the newly adjoined features.
 Paa=sub(P,0,OLD);Pab=[a[OLD:] for a in P[:OLD]];Pbb=sub(P,OLD,N)
 S=add(Pbb,mm(mm(tr(Pab),inverse(Paa)),Pab),-1)
 assert positive_parity(S) and all(S[i][i]>0 for i in range(N-OLD))
 Si=inverse(S);Slo=scale(S,alpha);Sup=scale(S,RHO)
 if replay:
  progress('independent direct polynomial and Ritz variational replay')
  direct=[[sum((x*y*F(11,5*(a+b+1)) for a,x in enumerate(polys[i]) for b,y in enumerate(polys[j]) if (a+b)%2==0),F(0)) for j in range(N)] for i in range(N)]
  assert direct==P
  # Reconstruct each conversion coefficient by Legendre orthogonality.
  from validate_rpb108_rc29_atom_reduction import legendre
  for k in range(N):
   pk=legendre(k)
   for j in range(N):
    v=sum((x*y*F(11,5*(a+b+1)) for a,x in enumerate(pk) for b,y in enumerate(polys[j]) if (a+b)%2==0),F(0))/mass[k]
    assert v==C[k][j]
  assert mm(G,exactV)==X
  Z=mm(Gui,X);assert mm(Gu,Z)==X
  assert cong(Z,Gu)==A
  assert positive_parity(add(A,Ml,-1))
  assert Pi==cong(tr(Ci),diag([1/x for x in mass[:N]]))
  # Residual physical polynomials q_new - q_old Paa^-1 Pab.
  B=mm(inverse(Paa),Pab)
  W=[[-B[i][j] if i<OLD else F(i-OLD==j) for j in range(N-OLD)] for i in range(N)]
  assert cong(W,direct)==S
  assert mm(S,Si)==diag([F(1)]*(N-OLD))
  # Expanded residual identity checked after Legendre congruence.
  assert positive_parity(add(cong(Ci,Ec),cong(Ci,add(add(add(Mu,J,-1),tr(J),-1),GT)),-1))
 progress('PASS')
 return dict(milestone='RC70',status='PASS',input_sha256=hashes,native_features_certified=list(range(N)),trial_dimension=DIM,
  chebyshev_to_legendre=serialize(C),physical_native_Gram=serialize(P),physical_native_Gram_inverse=serialize(Pi),
  actual_canonical_native_Gram_Loewner_lower=serialize(Ml),actual_canonical_native_Gram_Loewner_upper=serialize(Mu),
  actual_canonical_native_Gram_physical_lower_factor=str(alpha),actual_canonical_native_Gram_physical_upper_factor=str(RHO),
  physical_Gram_preconditioned_actual_metric_condition_number_upper=str(RHO/alpha),
  actual_native_Gram_inverse_Loewner_lower=serialize(invlo),actual_native_Gram_inverse_Loewner_upper=serialize(invup),
  Ritz_lower_rounding_diagonal_allowances=list(map(str,rounding)),native_trial_coefficients=serialize(V),physical_native_trial_Gram=serialize(T),
  actual_canonical_Riesz_error_Gram_Loewner_upper=serialize(Ec),actual_physical_Riesz_error_Gram_Loewner_upper=serialize(Ep),
  Riesz_error_rounding_diagonal_allowances=list(map(str,eround)),
  original_twenty_two_enriched_trial_columns_preserved_exactly=True,
  sharp_original_twenty_two_Riesz_error_bound_retained_by_input_certificate=True,
  old_and_new_Gram_enclosures_not_assumed_entrywise_identical=True,
  actual_orthogonal_projection_rank_certified=N,actual_nested_projection_increment_rank_certified=N-OLD,
  physical_extension_Schur_complement=serialize(S),actual_canonical_extension_Schur_Loewner_lower=serialize(Slo),actual_canonical_extension_Schur_Loewner_upper=serialize(Sup),
  actual_extension_Schur_inverse_Loewner_lower=serialize(scale(Si,1/RHO)),actual_extension_Schur_inverse_Loewner_upper=serialize(scale(Si,1/alpha)),
  actual_projection_characterization='Pi38 = R38 M38_inverse R38_star; kernel is first 38 physical native moments',
  nested_actual_projection_identity='Pi38 Pi22 = Pi22 Pi38 = Pi22; Pi38 - Pi22 is orthogonal rank 16',
  projected_source_residual_monotonicity='Gamma38 <= Gamma22 for the SAME fixed source input map; no 38-input bound follows',
  exact_actual_projection_coefficients_evaluated=False,thirty_eight_original_source_covariance_evaluated=False,
  thirty_eight_Weil_head_floor_certified=False,thirty_eight_complement_floor_certified=False,thirty_eight_source_budget_certified=False,
  whole_aperture_positivity_extended=False,RH=False,F4=False)

if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 defaults=[base/n for n in ['rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc69_enriched_complementary_leakage.json']]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True)==saved
  print('PASS: direct polynomial moments, orthogonality conversion, variational Ritz, physical inverse and extension Schur replay')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
