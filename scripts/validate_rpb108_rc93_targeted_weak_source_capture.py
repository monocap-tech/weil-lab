"""RC93: weak-span source capture through 64 physical Legendre modes.

Interval contraction precedes row bounds. The actual Riesz heads are
nested; no dense 64-head Weil evaluation or 64-complement Weil floor.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,prod
import json,hashlib,sys
from validate_rpb108_rc30_interval_metric import I,PI
from validate_rpb108_rc42_native_signed_pole_head import outward
from validate_rpb108_rc31_trial_riesz import mm,tr,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,entries,root
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,cong
from validate_rpb108_rc88_multiband_canonical_tail_transport import ceilgrid,logbounds
from validate_rpb108_rc90_continuous_source_balance_and_method_floor import relative40,sqrtfloor
RHO=F(252,257);B=F(11,10);M=64

def dot(v,A,w,replay):
 if replay:return sum((sum((v[i]*A[i][j]*w[j] for i in range(len(v))),F(0)) for j in range(len(w))),F(0))
 return mm(mm([v],A),tr([w]))[0][0]
def contract_interval(v,A,w,replay):
 n=len(v)
 if replay:
  terms=[(v[i]*w[i],A[i,i]) for i in range(n)]+[(v[i]*w[j]+v[j]*w[i],A[i,j]) for i in range(n) for j in range(i+1,n)]
 else:terms=[(v[i]*w[j],A[tuple(sorted((i,j)))]) for i in range(n) for j in range(n)]
 center=sum((c*(a+b)/2 for c,(a,b) in terms),F(0))
 # Separate ordered terms for a conservative common radius in both replays.
 radius=sum((abs(v[i]*w[j])*(A[tuple(sorted((i,j)))][1]-A[tuple(sorted((i,j)))][0])/2 for i in range(n) for j in range(n)),F(0))
 return center,radius

def upper(center,radius,d):
 row=[sum((radius[i][j]*d[j]/d[i] for j in range(2)),F(0)) for i in range(2)]
 result=[[center[i][j]+F(i==j)*row[i] for j in range(2)] for i in range(2)]
 assert psd(result)
 return result

def tail(replay):
 elo,ehi=outward(I(1).exp(),10**30);pilo,pihi=outward(PI,10**30);df=prod(range(1,2*M+2,2));energy=F(1);prev=F(0);rows=[]
 if replay:assert df==F(factorial(2*M+1),2**M*factorial(M))
 for k in range(1,451):
  cut=F(k,50);z=2*pihi*B*cut;r=z*z/F(2*M+3)**2;assert r<1
  theta=4*B*cut*z**(2*M)/(F(df)**2*(1-r));th=min(F(1),ceilgrid(theta,10**50));q=(ehi+cut)/(ehi+prev);lo,hi=outward(I(q).log(),10**40)
  if replay:
   a,b=logbounds(q);assert lo<=a<=b<=hi
  term=lo*(1-th);energy+=term
  rows.append(dict(cut=str(cut),low_frequency_energy_fraction_upper=str(th),weight_increment_lower=str(lo),energy_contribution=str(term)));prev=cut
  if th==1:break
 assert th==1
 if replay:assert energy==1+sum((F(x['weight_increment_lower']) for x in rows),F(0))-sum((F(x['weight_increment_lower'])*F(x['low_frequency_energy_fraction_upper']) for x in rows),F(0))
 tau=root(1/energy,10**30);assert tau*tau*energy>=1
 return tau,dict(head_degree_count=M,frequency_step='1/50',odd_double_factorial=str(df),e_enclosure=list(map(str,[elo,ehi])),pi_enclosure=list(map(str,[pilo,pihi])),layers=rows,canonical_energy_relative_physical_lower=str(energy),canonical_complement_embedding_norm_upper=str(tau))

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];head,prior,weak,native,enriched,source,direct,pairings,transport=map(json.loads,raw);h=[hashlib.sha256(x).hexdigest() for x in raw]
 assert head['input_sha256'][0]==h[1] and head['input_sha256'][1:6]==[h[i] for i in [2,4,3,5,6]]
 assert prior['input_sha256'][1:]==[h[i] for i in [2,4,3]]
 assert source['input_sha256'][:2]==[h[4],h[3]] and direct['input_sha256'][2:4]==[h[4],h[3]]
 assert pairings['input_sha256'][1:3]==[h[4],h[3]] and pairings['input_sha256'][6]==h[5]
 assert transport['input_sha256'][2]==h[6] and transport['input_sha256'][4:6]==[h[5],h[4]]
 C=matrix(native['chebyshev_to_legendre']);V=matrix(enriched['enriched_native_trial_coefficients']);mass=list(map(F,enriched['physical_mass']));D=[[mass[i]*F(i==j) for j in range(M)] for i in range(M)];T=cong(V,D)
 U=entries(source['nominal_complete_original_source_Gram_entries']);ER=entries(direct['nominal_Legendre_residual_Gram_entry_enclosures'])
 H=[[tuple(map(F,z)) for z in row] for row in pairings['nominal_physical_Legendre_source_pairing_enclosures']];assert len(H)==M and pairings['first_38_pairing_enclosures_preserved_exactly']
 assert all(mass[n]==2*B/F(2*n+1) for n in range(M))
 tau,tailcert=tail(replay);assert tailcert['e_enclosure']==transport['e_enclosure'] and tailcert['pi_enclosure']==transport['pi_enclosure'];oldtau=F(transport['canonical_complement_embedding_norm_upper']);assert tau<oldtau
 effective=F(transport['projected_arch_physical_to_canonical_norm_upper_divided_by_sqrt_rho'])+F(transport['projected_prime_physical_to_canonical_norm_upper_divided_by_sqrt_rho'])
 poles=list(map(F,transport['projected_pole_norm_uppers_divided_by_sqrt_rho']));delta=F(source['actual_source_approximation_operator_error_upper']);deltaL=F(direct['actual_operator_correction_norm_upper']);nu=F(1,65536);alpha=F(prior['inherited_1250_complement_floor']);blocks=[];directions=[]
 for p,name in enumerate(['even','odd']):
  selected=[a for a in weak['fixed_rational_direction_certificates'] if a['parity']==name and a['role'].startswith('weak')];vs=[list(map(F,a['coefficients'])) for a in selected];W=tr(vs);Z=mm(C,W);zs=tr(Z);d=[F(100 if p==0 else 80),F(1)]
  tw=[[dot(v,T,w,replay) for w in vs] for v in vs];hc=[[sum((vs[j][i]*(H[n][i][0]+H[n][i][1])/2 for i in range(22)),F(0)) for j in range(2)] for n in range(M)];hr=[[sum((abs(vs[j][i])*(H[n][i][1]-H[n][i][0])/2 for i in range(22)),F(0)) for j in range(2)] for n in range(M)]
  wc=[[F(0)]*2 for _ in range(2)];wr=[[F(0)]*2 for _ in range(2)];ec=[[F(0)]*2 for _ in range(2)];er=[[F(0)]*2 for _ in range(2)]
  for i in range(2):
   for j in range(i,2):
    u,ur=contract_interval(vs[i],U,vs[j],replay);cap=sum((hc[n][i]*hc[n][j]/mass[n] for n in range(M)),F(0));cr=sum(((abs(hc[n][i])*hr[n][j]+abs(hc[n][j])*hr[n][i])/mass[n] for n in range(M)),F(0))
    wc[i][j]=wc[j][i]=u-cap;wr[i][j]=wr[j][i]=ur+cr
    ec[i][j],er[i][j]=contract_interval(zs[i],ER,zs[j],replay);ec[j][i]=ec[i][j];er[j][i]=er[i][j]
  wu=upper(wc,wr,d);eu=upper(ec,er,d)
  ep=scale(add(scale(eu,1+nu),tw,(1+1/nu)*deltaL**2),RHO**2);assert psd(ep)
  k=(tau/oldtau)*(effective+poles[p])
  transfer=add(scale(ep,RHO*(1+nu)*k*k),tw,(1+1/nu)*delta**2*tau**2);nominal=scale(wu,tau*tau);assert psd(transfer) and psd(nominal)
  qlo=matrix(head['known_weak_head_blocks'][p]['actual_original_weak_head_Loewner_lower']);ref=matrix(prior['full_weak_mode_block_certificates'][p]['weak_input_canonical_Gram_Loewner_lower'])
  tests=[]
  for t in [F(k,64) for k in range(1,129)]+[F(3),F(4),F(8),F(16)]:
   A=add(scale(nominal,1+t),transfer,1+1/t);lam=relative40(A,qlo);tests.append((lam,t))
  lam,t=min(tests);A=add(scale(nominal,1+t),transfer,1+1/t);assert psd(add(scale(qlo,lam),A,-1))
  corrected=add(qlo,A,-1/alpha);ideal=add(qlo,transfer,-1/alpha);ideal_positive=ideal[0][0]>0 and ideal[0][0]*ideal[1][1]-ideal[0][1]**2>0;oldA=matrix(prior['full_weak_mode_block_certificates'][p]['actual_rank_38_weak_source_coupling_Gram_Loewner_upper']);improves=psd(add(oldA,A,-1))
  rel=relative40(scale(A,F(10**15)),ref)/10**15
  blocks.append(dict(parity=name,weak_roles=['weak_0','weak_1'],physical_polynomial_subtraction_coefficients=serialize([[hc[n][j]/mass[n] for j in range(2)] for n in range(M)]),targeted_nominal_physical_residual_center=serialize(wc),targeted_nominal_physical_residual_halfwidths=serialize(wr),targeted_nominal_physical_residual_Gram_upper=serialize(wu),targeted_operator_residual_center=serialize(ec),targeted_operator_residual_halfwidths=serialize(er),targeted_physical_Riesz_error_Gram_upper=serialize(ep),nominal_projected_Gram_upper=serialize(nominal),actual_projected_transfer_Gram_upper=serialize(transfer),Young_parameter=str(t),interval_balancing_scales=list(map(str,d)),actual_rank_64_weak_source_coupling_Gram_upper=serialize(A),actual_rank_1250_weak_source_coupling_Gram_upper_via_nesting=serialize(A),source_relative_weak_input_Gram_upper=str(rel),source_relative_RC92_weak_head_lower_upper=str(lam),whole_weak_block_improves_RC91=improves,hypothetical_zero_nominal_residual_weak_lower_positive_definite=ideal_positive,hypothetical_zero_nominal_residual_is_actual_certificate=False,corrected_weak_block_Loewner_lower=serialize(corrected),corrected_weak_block_positive_definite=corrected[0][0]>0 and corrected[0][0]*corrected[1][1]-corrected[0][1]**2>0))
  for i,a in enumerate(selected):
   qlower=F(head['known_weak_direction_certificates'][2*p+i]['actual_original_Weil_quadratic_lower']);qhi=F(head['known_weak_direction_certificates'][2*p+i]['actual_original_Weil_quadratic_upper']);margin=qlower-A[i][i]/alpha
   n=nominal[i][i];e=transfer[i][i];familylower=n+e+2*sqrtfloor(n*e)
   directions.append(dict(parity=name,role=a['role'],actual_rank_64_coupling_squared_upper=str(A[i][i]),prior_rank_38_coupling_squared_upper=str(oldA[i][i]),upper_bound_fractional_reduction=str(1-A[i][i]/oldA[i][i]),actual_head_quadratic_lower=str(qlower),actual_head_quadratic_upper=str(qhi),directional_Schur_lower=str(margin),directional_Schur_positivity_certified=margin>0,all_positive_scalar_Young_family_enclosure_diagonal_lower=str(familylower),family_diagonal_lower_exceeds_head_lower_budget=familylower>alpha*qlower,family_diagonal_lower_exceeds_head_upper_budget=familylower>alpha*qhi))
 assert all(a['family_diagonal_lower_exceeds_head_upper_budget'] for a in directions)
 result=dict(milestone='RC93',status='PASS',input_sha256=h,weak_target_dimension_per_parity=2,physical_polynomial_subtraction_degree_count=M,actual_projection_rank_bounded=64,complement_floor_projection_rank=1250,inherited_1250_complement_floor=str(alpha),rank_64_canonical_tail_certificate=tailcert,weak_source_block_certificates=blocks,weak_direction_certificates=directions,actual_projection_nesting_analytic_proof_supplied=True,rank_64_Weil_head_evaluated=False,rank_64_Weil_complement_floor_claimed=False,complete_1250_head_evaluated=False,actual_coupling_lower_certified=False,all_positive_Young_family_enclosure_obstructed_on_all_four_directions=True,enclosure_family_lower_is_not_actual_leakage_lower=True,known_weak_Schur_blocks_certified=all(b['corrected_weak_block_positive_definite'] for b in blocks),complete_weak_mode_coverage_certified=False,strong_head_block_certified=False,weak_strong_cross_block_certified=False,matrix_Schur_positivity_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
 if saved is not None:assert result==saved
 return result
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates';names=['rpb108_rc92_signed_weak_head_reconstruction.json','rpb108_rc91_weak_mode_coupling_alignment.json','rpb108_rc63_twenty_two_weak_floor_obstruction.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc81_direct_enriched_riesz_residuals.json','rpb108_rc83_nominal_source_canonical_response.json','rpb108_rc89_frequency_weighted_arch_transfer.json'];defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()));print('PASS: symmetric triangle interval centers, column-first trial contractions, factorial Fourier tails, rational log replay and telescoping coercivity; weak source capture and Schur comparisons')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
