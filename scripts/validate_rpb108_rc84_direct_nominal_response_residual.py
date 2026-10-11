"""RC84: direct complete signed residual of the RC83 canonical response.

Nominal source stays q+K_nom V64. Compute F_nom-L_nom Z, then pay the
actual canonical-operator correction. Original-source uncertainty is not
attached here, and the retained actual Riesz head remains rank 38.
"""
from fractions import Fraction as F
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
import json,hashlib,sys
from validate_rpb108_rc30_interval_metric import I
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc31_trial_riesz import mm,tr,psd
from validate_rpb108_rc35_enriched_residuals import transformed,polyadd
from validate_rpb108_rc42_native_signed_pole_head import outward,rational_interval
from validate_rpb108_rc43_native_prime_head import shift
from validate_rpb108_rc48_prime_source_covariance import geometry
from validate_rpb108_rc52_complete_source_covariance import primitives
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,entries,rows
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,block,relative
from validate_rpb108_rc68_enriched_original_source_covariance import source_forms,init_worker,base_worker,cross_worker,exponential_worker
from validate_rpb108_rc81_direct_enriched_riesz_residuals import build_forms
N=22;DIM=64;R=F(11,5);B=R/2;RHO=F(252,257)
def progress(s):print(s,file=sys.stderr,flush=True)

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths]
 response,source,enriched,native,precision,prime,arch=map(json.loads,raw)
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert response['milestone']=='RC83' and response['physical_canonical_trial_dimension']==DIM
 assert response['actual_Riesz_projection_head_rank_retained']==38
 assert [response['input_sha256'][i] for i in [1,2,3,4,5,6]]==[hashes[i] for i in [2,3,4,5,6,1]]
 assert [source['input_sha256'][i] for i in [0,1,2,3,5]]==[hashes[i] for i in [2,3,4,5,6]]
 assert source['native_features_certified']==list(range(N))
 V=matrix(enriched['enriched_native_trial_coefficients']);Z=matrix(response['nominal_source_canonical_trial_response_coefficients'])
 assert (len(Z),len(Z[0]))==(DIM,N)
 source_base,mom,trials,targets=source_forms(enriched,native,arch,precision)
 operator_forms,operator_mom,r,eps=build_forms(Z,F(precision['constant_midpoint']))
 assert r==R and all(a.l==b.l and a.h==b.h for ma,mb in zip(mom,operator_mom) for a,b in zip(ma,mb))
 # build_forms(Z) returns P_j-L_nom Z_j. Remove its auxiliary Legendre
 # target; retain the native target already present in source_base.
 forms=[]
 for j,((A,L,M),(a,l,m)) in enumerate(zip(source_base,operator_forms)):
  forms.append((polyadd(polyadd(A,a),[I(x) for x in transformed(legendre(j))],-1),polyadd(L,l),polyadd(M,m)))
 LP=[legendre(n) for n in range(DIM)]
 polys=[[sum((V[n][j]*(LP[n][k] if k<=n else 0) for n in range(DIM)),F(0)) for k in range(DIM)] for j in range(N)]
 terms,segments=geometry(prime);assert len(terms)==14 and len(segments)==15
 # Prime source and pole coefficients stay exactly those of RC68.
 translated=[[[a*2**k for k,a in enumerate(shift([I(x) for x in poly],term['offset']-1))] for poly in polys] for term in terms]
 cross_data=[];cache={}
 for ln,rn,left,right,active in segments:
  for name,t in [(ln,left),(rn,right)]:
   if name not in cache:cache[name]=primitives((t+1)/2,319,0 if name=='left' else 1 if name=='right' else None)
  moments=[[cache[rn][kind][k]-cache[ln][kind][k] for k in range(320)] for kind in range(3)]
  sy=[[sum((terms[h]['coefficient']*translated[h][j][k] for h in active),I(0)) for k in range(DIM)] for j in range(N)]
  cross_data.append((moments,sy))
 jobs=[(i,j) for i in range(N) for j in range(i,N) if (i-j)%2==0]
 zero={(i,j):(F(0),F(0)) for i in range(N) for j in range(i,N) if (i-j)%2}
 old={} if saved is None else {name:entries(saved[name]) for name in ['nominal_base_response_residual_Gram_entries','nominal_symmetrized_base_residual_prime_cross_entries','nominal_symmetrized_residual_pole_cross_entries','nominal_complete_physical_response_residual_Gram_entries']}
 def accept(name,key,value):
  if saved is None:return value
  a,b=old[name][key];assert a<=value[0]<=value[1]<=b,(name,key);return a,b
 U0={}
 with ProcessPoolExecutor(max_workers=8,initializer=init_worker,initargs=((forms,mom,replay),)) as pool:
  for i,j,value in pool.map(base_worker,jobs):
   U0[i,j]=accept('nominal_base_response_residual_Gram_entries',(i,j),value);progress('base residual Gram '+str((i,j))+' checked')
 U0.update(zero)
 ordered={}
 with ProcessPoolExecutor(max_workers=8,initializer=init_worker,initargs=((forms,cross_data,replay),)) as pool:
  for i,value in pool.map(cross_worker,range(N)):ordered[i]=value;progress('mixed residual-prime row '+str(i)+' checked')
 cross={}
 for i,j in jobs:cross[i,j]=accept('nominal_symmetrized_base_residual_prime_cross_entries',(i,j),outward(ordered[i][j]+ordered[j][i],10**20))
 cross.update(zero)
 z0=[]
 with ProcessPoolExecutor(max_workers=8,initializer=init_worker,initargs=((forms,mom,U0,replay),)) as pool:
  for j,value in pool.map(exponential_worker,range(N)):
   if saved is not None:
    a,b=map(F,saved['nominal_base_residual_exponential_moments'][j]);assert a<=value[0]<=value[1]<=b;value=(a,b)
   z0.append(value);progress('base residual pole moment '+str(j)+' checked')
 UP=entries(source['nominal_prime_source_Gram_entries']);PO=entries(source['nominal_pole_source_Gram_entries'])
 mi=[rational_interval(*map(F,row)) for row in source['nominal_trial_exponential_moments']]
 zp=[rational_interval(*map(F,row)) for row in source['nominal_prime_exponential_moments']]
 U={};XPO={}
 for i,j in jobs:
  x=2*(-1)**i*(mi[j]*(rational_interval(*z0[i])+zp[i])+mi[i]*(rational_interval(*z0[j])+zp[j]))
  XPO[i,j]=accept('nominal_symmetrized_residual_pole_cross_entries',(i,j),outward(x,10**20))
  # Add certified component intervals, preserving every signed cross term.
  total=sum((rational_interval(*v) for v in [U0[i,j],UP[i,j],cross[i,j],PO[i,j],XPO[i,j]]),I(0))
  U[i,j]=accept('nominal_complete_physical_response_residual_Gram_entries',(i,j),outward(total,10**20))
 U.update(zero);XPO.update(zero)
 Q=[[F(0)]*N for _ in range(N)];allow=[F(0)]*N
 for (i,j),(a,b) in U.items():
  Q[i][j]=Q[j][i]=(a+b)/2;half=(b-a)/2;allow[i]+=half
  if i!=j:allow[j]+=half
 Uup=[[Q[i][j]+F(i==j)*allow[i] for j in range(N)] for i in range(N)];assert psd(Uup)
 mass=list(map(F,enriched['physical_mass']));D=[[mass[i]*F(i==j) for j in range(DIM)] for i in range(DIM)]
 if replay:T=[[sum((mass[k]*Z[k][i]*Z[k][j] for k in range(DIM)),F(0)) for j in range(N)] for i in range(N)]
 else:T=mm(mm(tr(Z),D),Z)
 delta=2*F(precision['constant_radius'])+eps;t=F(1,65536)
 Bactual,br=rounded_bound(add(scale(Uup,1+t),T,(1+1/t)*delta**2),1,10**24)
 Ec=scale(Bactual,RHO);assert psd(Ec)
 oldEc=matrix(response['actual_canonical_nominal_source_trial_response_error_Gram_Loewner_upper'])
 assert psd(add(oldEc,Ec,-1))
 Mlo=matrix(enriched['enriched_actual_native_Gram_Loewner_lower']);parity=[]
 for p in range(2):
  lam=relative(block(Ec,p),block(Mlo,p));assert psd(add(scale(block(Mlo,p),lam),block(Ec,p),-1))
  parity.append(dict(parity='even' if p==0 else 'odd',actual_canonical_nominal_source_response_error_relative_input_Gram_upper=str(lam)))
 diagnostics=[dict(feature=j,RC83_response_error_squared_upper=str(oldEc[j][j]),direct_response_error_squared_upper=str(Ec[j][j]),diagonal_upper_bound_improvement_factor=str(oldEc[j][j]/Ec[j][j])) for j in range(N)]
 progress('direct complete residual covariance and canonical transport checked')
 return dict(milestone='RC84',status='PASS',input_sha256=hashes,canonical_trial_dimension=DIM,source_input_features=list(range(N)),actual_Riesz_projection_head_rank_retained=38,
  nominal_source_definition=response['nominal_source_definition'],physical_residual_definition='r_nom=F_nom-L_nom Z; Z is the unchanged RC83 canonical trial response',
  original_Riesz_trials_unchanged=True,RC83_response_coefficients_unchanged=True,
  nominal_base_response_residual_Gram_entries=rows(U0),nominal_symmetrized_base_residual_prime_cross_entries=rows(cross),nominal_base_residual_exponential_moments=[list(map(str,v)) for v in z0],
  prime_Gram_and_pole_Gram_and_prime_pole_moments_reused_from_RC68=True,
  nominal_symmetrized_residual_pole_cross_entries=rows(XPO),nominal_complete_physical_response_residual_Gram_entries=rows(U),
  nominal_complete_physical_response_residual_Gram_Loewner_upper=serialize(Uup),physical_interval_rounding_row_allowances=list(map(str,allow)),
  canonical_operator_remainder_upper=str(eps),actual_canonical_operator_correction_norm_upper=str(delta),Young_parameter=str(t),physical_response_Gram=serialize(T),
  actual_physical_nominal_source_response_operator_residual_Gram_Loewner_upper=serialize(Bactual),operator_transport_rounding_row_allowances=list(map(str,br)),
  actual_canonical_nominal_source_response_error_Gram_Loewner_upper=serialize(Ec),parity_response_error_certificates=parity,diagonal_response_error_comparisons=diagnostics,
  whole_Loewner_response_error_improvement_over_RC83_certified=True,all_complete_signed_response_residual_correlations_retained=True,
  actual_original_source_uncertainty_attached=False,actual_rank_38_projected_response_evaluated=False,RC82_rank_38_source_bound_retained_unchanged=True,
  required_scalar_source_budget_certified=False,actual_rank_38_scalar_budget_failure_proved=False,
  enlarged_Weil_floor_certified=False,enlarged_complement_floor_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 names=['rpb108_rc83_nominal_source_canonical_response.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc56_precision_attached_head.json','rpb108_rc43_native_prime_head.json','rpb108_rc46_native_archimedean_head.json']
 defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True,saved)==saved
  print('PASS: reflected base residual covariance and prime cross moments, independent pole moments, exact physical transport and canonical Loewner improvement')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
