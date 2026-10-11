"""RC104: eight-mode Rayleigh ceiling after the certified six-mode span.

Candidate selection is not acceptance. All fixed coefficients, intervals,
metric independence, Rayleigh ceilings and degree tests use exact Fractions.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys
from validate_rpb108_rc31_trial_riesz import mm,tr,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,root,entries
from validate_rpb108_rc65_parity_projected_residual_refinement import cong,add,scale
from validate_rpb108_rc93_targeted_weak_source_capture import contract_interval,dot
from validate_rpb108_rc92_signed_weak_head_reconstruction import bil
from validate_rpb108_rc99_signed_source_projection_bounds import upper
from validate_rpb108_rc90_continuous_source_balance_and_method_floor import relative40
from validate_rpb108_rc97_additional_low_mode_coverage import pd
from validate_rpb108_rc63_twenty_two_weak_floor_obstruction import up,down
from validate_rpb108_rc103_complement_inverse_lift import chebyshev
FIXED=[{'parity': 'even', 'vectors': [['497734472977/1000000000000', '0', '-1', '0', '808418863059/1000000000000', '0', '-262993318733/500000000000', '0', '137230875113/500000000000', '0', '-114100900451/1000000000000', '0', '9348580513/250000000000', '0', '-4744238801/500000000000', '0', '56260113/31250000000', '0', '-118091321/500000000000', '0', '8500101/500000000000', '0'], ['444650425243/1000000000000', '0', '-139738023231/250000000000', '0', '-35863053147/100000000000', '0', '1', '0', '-194470939043/200000000000', '0', '72993615047/125000000000', '0', '-15016123613/62500000000', '0', '69181487789/1000000000000', '0', '-13514168167/1000000000000', '0', '791373823/500000000000', '0', '-66636023/1000000000000', '0'], ['-2168781821/5000000000', '0', '174736080729/1000000000000', '0', '7504536889/8000000000', '0', '-243113128257/500000000000', '0', '-27088765043/40000000000', '0', '1', '0', '-595007080731/1000000000000', '0', '194517281267/1000000000000', '0', '-780691323/25000000000', '0', '-85501659/125000000000', '0', '45730099/40000000000', '0'], ['-543505928947/1000000000000', '0', '-73513081/244140625', '0', '1', '0', '443182128497/500000000000', '0', '-634371033223/1000000000000', '0', '-99050843357/125000000000', '0', '852933291373/1000000000000', '0', '-235128285833/1000000000000', '0', '-32466335087/1000000000000', '0', '5718344741/200000000000', '0', '3416028193/1000000000000', '0']]}, {'parity': 'odd', 'vectors': [['0', '312456204167/1000000000000', '0', '-861099899179/1000000000000', '0', '1', '0', '-382219722129/500000000000', '0', '422151778263/1000000000000', '0', '-86929013691/500000000000', '0', '2150165969/40000000000', '0', '-614887549/50000000000', '0', '992121803/500000000000', '0', '-1585773/8000000000', '0', '7567901/1000000000000'], ['0', '235634327809/500000000000', '0', '-906218556747/1000000000000', '0', '5668070771/40000000000', '0', '202918334563/250000000000', '0', '-1', '0', '622229084347/1000000000000', '0', '-240765268711/1000000000000', '0', '14688826947/250000000000', '0', '-3811640653/500000000000', '0', '-95205489/1000000000000', '0', '91093527/500000000000'], ['0', '712850912121/1000000000000', '0', '-705577452761/1000000000000', '0', '-894005067191/1000000000000', '0', '134887074417/200000000000', '0', '171085092651/250000000000', '0', '-1', '0', '31067058789/62500000000', '0', '-100186377007/1000000000000', '0', '-2121762371/200000000000', '0', '1337390707/125000000000', '0', '-1738827507/1000000000000'], ['0', '-2074086799/200000000000', '0', '-312097751/4000000000', '0', '-71374764451/1000000000000', '0', '32664032321/250000000000', '0', '177502387201/500000000000', '0', '60493038669/500000000000', '0', '-525608518661/1000000000000', '0', '-22019526013/100000000000', '0', '1', '0', '-843536788359/1000000000000', '0', '351628791797/1000000000000']]}]
RHO=F(252,257)
def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];prior,completion,odd,even,tail,weak,enriched,native,source,residual,norm,compact=map(json.loads,raw);h=[hashlib.sha256(x).hexdigest() for x in raw]
 assert prior['milestone']=='RC103' and prior['input_sha256']==[h[i] for i in [1,2,3,4,10]]
 assert completion['input_sha256'][4:7]==h[6:9] and completion['input_sha256'][8]==h[10]
 assert odd['input_sha256'][5:8]==h[5:8] and odd['input_sha256'][11:13]==h[8:10] and odd['input_sha256'][15]==h[10]
 assert even['input_sha256']==odd['input_sha256'][1:] and odd['six_mode_corrected_positivity_certified']
 assert source['input_sha256'][:2]==h[6:8] and source['input_sha256'][6]==h[10]
 assert residual['input_sha256'][2:4]==h[6:8]
 assert compact['milestone']=='RC77' and compact['canonical_embedding_and_adjoint_compactness_analytic_proof_supplied']
 V=matrix(enriched['enriched_native_trial_coefficients']);C=matrix(native['chebyshev_to_legendre']);G0=matrix(enriched['recentered_nominal_metric_center']);mass=list(map(F,enriched['physical_mass']));M=matrix(enriched['enriched_actual_native_Gram_Loewner_lower'])
 T=cong(V,[[mass[i]*F(i==j) for j in range(64)] for i in range(64)]);X=[[mass[i]*C[i][j] if i<22 else F(0) for j in range(22)] for i in range(64)]
 H=matrix(source['nominal_original_trial_source_pairing_center']);Rh=matrix(source['nominal_original_trial_source_pairing_halfwidths']);Q0=add(add(cong(V,G0),H),tr(mm(tr(X),V)),-1)
 Q0=[[(Q0[i][j]+Q0[j][i])/2 for j in range(22)] for i in range(22)];Rh=[[(Rh[i][j]+Rh[j][i])/2 for j in range(22)] for i in range(22)]
 ER=entries(residual['nominal_Legendre_residual_Gram_entry_enclosures']);U=entries(source['nominal_complete_original_source_Gram_entries']);delta=F(source['actual_source_approximation_operator_error_upper']);deltaL=F(residual['actual_operator_correction_norm_upper']);dg=F(enriched['actual_recentered_metric_mass_error_upper']);nu=F(1,65536);blocks=[]
 for p,name in enumerate(['even','odd']):
  vs=[list(map(F,x)) for x in FIXED[p]['vectors']];assert len(vs)==4 and all(v[k]==0 for v in vs for k in range(22) if k%2!=p)
  zs=tr(mm(C,tr(vs)));tw=[[dot(v,T,w,replay) for w in vs] for v in vs];ml=[[bil(v,M,w,replay) for w in vs] for v in vs];assert pd(ml)
  ec=[[F(0)]*4 for _ in range(4)];er=[[F(0)]*4 for _ in range(4)]
  for i in range(4):
   for j in range(i,4):ec[i][j],er[i][j]=contract_interval(zs[i],ER,zs[j],replay);ec[j][i]=ec[i][j];er[j][i]=er[i][j]
  Ep=scale(add(scale(upper(ec,er,[F(1)]*4,replay),1+nu),tw,(1+1/nu)*deltaL**2),RHO**2)
  sn=[]
  for v,t in zip(vs,range(4)):
   u,r=contract_interval(v,U,v,replay);sn.append(up(root(u+r,10**40)+delta*root(tw[t][t],10**40),10**40))
  k=F(norm['complete_physical_operator_parity_norm_upper'][p]);qc=[[F(0)]*4 for _ in range(4)];qr=[[F(0)]*4 for _ in range(4)];rows=[]
  for i in range(4):
   for j in range(i,4):
    center=bil(vs[i],Q0,vs[j],replay);trial=bil(list(map(abs,vs[i])),Rh,list(map(abs,vs[j])),replay)+(delta+dg)*root(tw[i][i]*tw[j][j],10**40)
    linear=root(Ep[i][i],10**40)*sn[j]+root(Ep[j][j],10**40)*sn[i];physical=k*root(Ep[i][i]*Ep[j][j],10**40);can=Ep[i][i]/RHO if i==j else root(Ep[i][i]*Ep[j][j],10**40)/RHO
    lo=down(center-trial-linear-physical-can,10**40);hi=up(center+trial+linear+physical+(can if i!=j else 0),10**40)
    qc[i][j]=qc[j][i]=(lo+hi)/2;qr[i][j]=qr[j][i]=(hi-lo)/2;rows.append(dict(i=i,j=j,actual_original_Weil_entry_enclosure=[str(lo),str(hi)]))
  Qup=upper(qc,qr,[F(1)]*4,replay);eta=relative40(scale(Qup,10**6),ml)/10**6;assert 0<eta<F(1,1000) and psd(add(scale(ml,eta),Qup,-1))
  ip=prior['parity_inverse_lift_certificates'][p];a=F(ip['complement_spectral_lower']);b=F(ip['complement_spectral_upper']);c=(b+a)/(b-a);lam=F(ip['generic_correction_relative_weak_lower_upper']);n=1
  while lam/chebyshev(n,c,replay)**2>eta/8:n+=1
  assert lam/chebyshev(n,c)**2<=eta/8 and (n==1 or lam/chebyshev(n-1,c)**2>eta/8)
  VG=matrix(completion['parity_completion_certificates'][p]['corrected_source_norm_transport_Gram_upper']);L=matrix([even,odd][p]['corrected_'+name+'_three_mode_Loewner_lower'])
  assert psd(add(scale(L,eta/8),scale(VG,1/chebyshev(n,c,replay)**2),-1))
  assert n>1 and not psd(add(scale(L,eta/8),scale(VG,1/chebyshev(n-1,c,replay)**2),-1))
  excluded=[t['hypothetical_strong_floor'] for t in ip['degree_budget_certificates'] if F(t['hypothetical_strong_floor'])>eta]
  blocks.append(dict(parity=name,fixed_rational_native_coefficients=FIXED[p]['vectors'],actual_subspace_dimension=4,actual_canonical_Gram_Loewner_lower=serialize(ml),targeted_actual_physical_Riesz_error_Gram_upper=serialize(Ep),signed_actual_original_Weil_entry_enclosures=rows,actual_original_Weil_Loewner_upper=serialize(Qup),whole_subspace_actual_canonical_Rayleigh_upper=str(eta),certified_weak_parity_dimension=3,canonical_strong_intersection_dimension_lower=1,exact_effective_strong_floor_upper=str(eta),scalar_floor_effective_strong_floor_upper=str(eta),RC103_hypothetical_strong_targets_ruled_out=excluded,minimum_RC103_uniform_residual_degree_at_this_parity_floor_ceiling=n,preceding_degree_fails_exact_uniform_matrix_budget=True,degree_lower_bound_scope='only the inherited G, L and uniform Chebyshev residual allowance, not actual inverse difficulty'))
 out=dict(milestone='RC104',status='PASS',input_sha256=h,arithmetic='exact Fraction; no floating acceptance',candidate_search_is_not_acceptance=True,new_source_integrals_evaluated=0,actual_test_span_dimension=8,known_corrected_positive_span_dimension=6,original_operator_nonpositive_spectral_dimension_upper=1244,parity_low_subspace_certificates=blocks,original_operator_eigenvalues_at_or_below_reported_ceiling_count_lower=8,eight_mode_actual_canonical_Rayleigh_upper=str(max(F(b['whole_subspace_actual_canonical_Rayleigh_upper']) for b in blocks)),additional_low_strong_directions_dimension_lower=2,uniform_exact_effective_strong_floor_upper=str(min(F(b['exact_effective_strong_floor_upper']) for b in blocks)),dimension_intersection_and_compact_minmax_analytic_proofs_supplied=True,actual_canonical_projection_onto_certified_six_span_approximated=False,actual_negative_or_null_direction_certified=False,strong_head_block_lower_certified=False,complete_nonpositive_mode_coverage_certified=False,actual_lifted_response_Gram_certified=False,matrix_Schur_positivity_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
 if saved is not None:assert out==saved
 return out
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates';names=['rpb108_rc103_complement_inverse_lift.json','rpb108_rc102_six_response_completion_boundary.json','rpb108_rc101_odd_three_mode_jump_tail.json','rpb108_rc100_even_three_mode_jump_tail.json','rpb108_rc95_jump_aware_even_source_tail.json','rpb108_rc63_twenty_two_weak_floor_obstruction.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc81_direct_enriched_riesz_residuals.json','rpb108_rc66_arch_multiplier_transport.json','rpb108_rc77_canonical_adjoint_tail.json'];defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()));print('PASS: fixed rational spans, reordered signed contractions, exact metric rank and Rayleigh ceilings, independent Chebyshev degree replay')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
