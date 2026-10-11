"""RC111 exact structural-coverage controls; no new Weil matrix entries.
Usage: python script.py [--replay] [--output PATH] CERT110 CERT107 CERT106 CERT103 CERT95 CERT77 CERT66
Replay uses determinant-ratio inertia in place of LDL inertia.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale
from validate_rpb108_rc97_additional_low_mode_coverage import pd
from validate_rpb108_rc107_original_compression_spectral_census import inertia

def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def block(Q,B,D): return [Q[i]+B[i] for i in range(len(Q))]+[tr(B)[i]+D[i] for i in range(len(D))]
def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];c110,c107,c106,c103,c95,c77,c66=map(json.loads,raw)
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [x['milestone'] for x in [c110,c107,c106,c103]]==['RC110','RC107','RC106','RC103']
 assert c110['input_sha256'][0]==hashes[1] and c110['input_sha256'][9]==hashes[4] and c110['input_sha256'][12]==hashes[6]
 assert c107['input_sha256'][0]==hashes[2] and c107['input_sha256'][6:9]==[hashes[6],hashes[5],hashes[4]]
 assert c106['input_sha256'][1]==hashes[3] and c103['input_sha256'][3:5]==[hashes[4],hashes[6]]
 assert c77['canonical_embedding_and_adjoint_compactness_analytic_proof_supplied']
 a=F(c95['inherited_1250_complement_floor']);t=F(1,100);assert a==F(247,2500)>t
 assert c110['certified_corrected_span_dimension']==12 and c110['original_operator_nonpositive_spectral_dimension_upper']==1238
 assert not c110['whole_aperture_positivity_extended']
 for row in c107['parity_spectral_compression_certificates']:
  q=next(x for x in row['spectral_census'] if F(x['threshold'])==t)
  assert q['exact_count_certified'] and q['compression_eigenvalues_strictly_below_threshold_count_lower']==5 and q['compression_eigenvalues_strictly_below_threshold_count_upper']==5
 tau=F(c95['rank_1250_canonical_tail_certificate']['canonical_complement_embedding_norm_upper']);rho=F(252,257)
 envelopes=[]
 for p,name in enumerate(['even','odd']):
  k=F(c66['complete_physical_operator_parity_norm_upper'][p]);loss=k*tau*tau;g=rho*tau*tau*k*k
  shift=t*g/(a*(a-t));needed=t+shift
  assert loss>1 and 1-loss<0 and needed>1
  envelopes.append(dict(parity=name,tail_norm_upper=str(tau),physical_K_norm_upper=str(k),absolute_K_tail_squared_sufficient_for_threshold=str((1-t)/k),inherited_tail_squared=str(tau*tau),absolute_K_strong_floor_lower=str(1-loss),absolute_K_envelope_cannot_certify_positive_floor=True,generic_B_squared_norm_upper=str(g),effective_strong_floor_sufficient_for_original_threshold_using_generic_B=str(needed),this_is_a_sufficient_budget_not_a_necessary_floor=True))
 # Nonidentity canonical metric and noncommuting physical blocks.
 M=[[F(2),F(1,3)],[F(1,3),F(1)]];ME=eye(2)
 Q=[[F(3),F(1,5)],[F(1,5),F(2)]];B=[[F(1,4),F(1,7)],[F(-1,6),F(1,5)]];D=[[F(2),F(1,4)],[F(1,4),F(1)]]
 I=eye(2);assert pd(M) and pd(add(D,scale(I,a),-1))
 Dt=add(D,scale(I,t),-1);R=tr(B);F0=add(Q,mm(mm(B,inverse(D)),R),-1)
 Ft=add(add(Q,scale(M,t),-1),mm(mm(B,inverse(Dt)),R),-1)
 G=mm(B,R);base=add(F0,scale(M,t),-1)
 assert psd(add(base,Ft,-1)) and psd(add(Ft,add(base,scale(G,t/(a*(a-t))),-1),-1))
 full=block(Q,B,D);metric=block(M,[[F(0)]*2 for _ in range(2)],ME)
 assert inertia(add(full,scale(metric,t),-1),replay)['negative']==inertia(Ft,replay)['negative']
 # Shifted correlated lift identity and both Loewner endpoints.
 Y=[[F(1,8),F(1,9)],[F(1,10),F(-1,11)]];r=add(R,mm(Dt,Y),-1)
 C=add(add(add(add(Q,scale(M,t),-1),mm(B,Y),-1),mm(tr(Y),R),-1),mm(mm(tr(Y),Dt),Y))
 assert Ft==add(C,mm(mm(tr(r),inverse(Dt)),r),-1)
 b=F(3);assert pd(add(scale(I,b),D,-1))
 assert psd(add(Ft,add(C,scale(mm(tr(r),r),1/(a-t)),-1),-1))
 assert psd(add(add(C,scale(mm(tr(r),r),1/(b-t)),-1),Ft,-1))
 # A rational example where substituting F-tI gives the wrong count.
 q=F(1,50);coupling=F(1,10);d=F(1);f=q-coupling*coupling/d
 wrong=f-t;correct=q-t-coupling*coupling/(d-t)
 assert wrong==0 and correct<0
 # Nonboundary example: zero-threshold F has floor above t, original has an eigenvalue below t.
 q=F(201,10000);wrong=q-coupling*coupling-t;correct=q-t-coupling*coupling/(1-t)
 assert wrong>0 and correct<0
 # Exact two-stage strong-block / exceptional completion control, signed correlations retained.
 beta=F(1,2);FS=F0[1][1];cross=F0[0][1]
 assert FS>beta and F0[0][0]-cross*cross/beta>0 and pd(F0) and pd(full)
 # Invisible omitted modes: same native compression, full native action, and E floor.
 low=[F(1,1000)]*10+[F(1,2)]*12
 counts=[]
 for m in [0,1,12,1228]:
  # Direct diagonal compact perturbation: omitted head entries are -1 (m) or 1.
  vals=low+[F(-1)]*m+[F(1)]*(1228-m)+[a]
  assert len(vals)==1251
  below=sum(v<t for v in vals);nonpos=sum(v<=0 for v in vals)
  assert below==10+m and nonpos==m
  assert all(vals[i]>0 for i in range(12)) and vals[-1]==a
  counts.append(dict(additional_invisible_modes=m,total_below_threshold=below,nonpositive_count=nonpos,native_compression_and_native_action_unchanged=True,infinite_complement_floor_preserved=True,abstract_not_original_Weil_arithmetic=True))
 return dict(milestone='RC111',status='structural stopping theorem and enclosure obstruction; arithmetic strong estimate open',aperture='11/10',input_sha256=hashes,arithmetic='exact fractions; LDL and independent determinant-ratio inertia controls',threshold=str(t),inherited_complement_floor=str(a),original_below_threshold_count_lower=10,original_below_threshold_count_upper=1250,inherited_nonpositive_count_upper=1238,inherited_corrected_positive_dimension=12,absolute_envelope_obstructions=envelopes,threshold_Feshbach_identity_control_verified=True,shifted_correlated_lift_sandwich_control_verified=True,actual_canonical_nonidentity_metric_used_in_controls=True,unshifted_effective_head_is_not_original_threshold_operator_control_verified=True,exact_two_stage_completion_control_verified=True,invisible_omitted_mode_controls=counts,structural_threshold_coverage_theorem_proved_in_note=True,compact_negative_part_counting_reduction_proved_in_note=True,original_strong_floor_outside_ten_candidates_certified=False,effective_strong_floor_outside_ten_candidates_certified=False,full_original_exceptional_count_certified=False,actual_shifted_arithmetic_lifts_computed=False,new_native_directions_added=0,new_source_integrals_evaluated=False,whole_aperture_positivity_extended=False,F4=False,RH=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output');p.add_argument('inputs',nargs=7);args=p.parse_args();out=run(args.inputs,args.replay)
 if args.replay:
  assert args.output and json.loads(Path(args.output).read_text())==out
 elif args.output:Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print('RC111 PASS: exact structural controls and inherited-envelope obstruction; original coverage remains open')
