#!/usr/bin/env python3
"""Certify one 111-dimensional chart, preserving DNE50's complete positive span."""
from pathlib import Path
from fractions import Fraction as F
import json,argparse
import validate_cc105_selected_response as data
import certify_cc81_boundary_response_consumer as c
import certify_cc101_next_source_packet as proof
import certify_cc88_correlated_seventh_response as r
import certify_cc104_joint_response_rebase as response
from certify_cc108_dne41_integration import compress,rank
K=F(647,1000)
def run(output,gate,replay=None):
 g,gh,_=data.read(gate);assert g['status']=='PASS' and g['original_high_floor']==str(K)
 old,oh,_=data.read('notes/cc117-source/notes/data/RPB108_DNE50_POSITIVE_SUBSPACES_20261010.json.gz.b64');v,vh,_=data.read('notes/cc117-source/notes/data/RPB108_DNE50_POSITIVE_SUBSPACE_VALIDATION_20261010.json');assert v['status']=='PASS' and v['certificate_sha256']==oh and old['actual_certified_all_high_retained_dimension']==109
 dne,dh,_=data.read('notes/cc117-source/notes/data/RPB108_DNE50_FULL_RESPONSE_20261010.json.gz.b64');dv,dvh,_=data.read('notes/cc117-source/notes/data/RPB108_DNE50_FULL_RESPONSE_VALIDATION_20261010.json');assert dv['status']=='PASS' and dv['certificate_sha256']==dh
 frozen,_,_=data.read(replay) if replay else (None,None,None);rows=[]
 for idx,p in enumerate(['even','odd']):
  z=g['parity_checks'][idx];CCM=c.matrix(z['paid_response_comparison']);M=r.scale(c.matrix(dne['rows'][0]['paid_response_budget']),1/K) if idx==0 else CCM;prior=old['rows'][idx];PB=[list(map(F,row)) for row in prior['positive_embedding_B']]
  B=PB if p=='even' else [[F(i==j) for j in range(56)] for i in range(56)];dim=len(B[0]);assert dim==[55,56][idx]
  if idx==0:assert rank([row[44:] for row in B[44:]])==11
  else:
   for i in range(56):assert all(sum(B[i][k]*PB[k][j] for k in range(56))==PB[i][j] for j in range(54))
  U=frozen['parity_checks'][idx]['positive_proof']['frozen_rational_congruence'] if frozen else (prior['positive_comparison_certificate']['exact_congruence_U'] if idx==0 else None);d,pc=proof.proof(compress(M,B),U)
  bf=sum(x*x for row in B for x in row);mass=F(prior['original_packet_physical_mass'] if idx==0 else z['physical_packet_mass'])*bf;trace=F(prior['original_projected_source_trace_upper'] if idx==0 else z['projected_source_trace_upper'])*bf;gap=min(d/(4*(mass+trace/K**2)),K/2);assert gap>0
  row=dict(parity=p,positive_embedding_B=[list(map(str,row)) for row in B],retained_rank=dim,exact_retained_embedding_rank_verified=True,DNE50_positive_span_contained=True,positive_proof=pc,coefficient_floor=str(d),embedding_Frobenius_squared=str(bf),physical_packet_mass_upper=str(mass),projected_source_trace_upper=str(trace),physical_gap_lower=str(gap))
  row['comparison_used']='DNE50_three_trial_even' if idx==0 else 'CC117_ten_trial_odd'
  if idx==0:
   # Different response families need not order each other's fixed comparisons.
   fail=response.sign(compress(CCM,B));assert fail['status']=='REJECTED';row['CC_even_restriction_to_DNE50_positive_span']=fail
  if idx==1:
   # This exact vector rejects the same packet's remaining-source comparison.
   trial=[F(row[0]) for row in prior['negative_comparison_embedding_D']];plain=c.quad(c.matrix(z['paid_plain_comparison']),trial);refined=c.quad(M,trial);assert plain[1]<0 and refined[0]>0
   row.update(strict_collective_separation_trial=list(map(str,trial)),remaining_source_trial_value=c.pair(plain),CC_response_trial_value=c.pair(refined),full_collective_response_positive=True)
  if frozen:assert gap>=F(frozen['parity_checks'][idx]['physical_gap_lower']) and row['positive_embedding_B']==frozen['parity_checks'][idx]['positive_embedding_B']
  rows.append(row);print(p,'rank',dim,'gap',float(gap),flush=True)
 guard=F(1,10**39);assert min(F(x['physical_gap_lower']) for x in rows)>guard
 out=dict(milestone='CC117',status='PASS',gate_decoded_sha256=gh,DNE50_positive_subspaces_decoded_sha256=oh,DNE50_positive_validation_sha256=vh,DNE50_full_response_decoded_sha256=dh,DNE50_full_response_validation_sha256=dvh,parity_checks=rows,integrated_positive_retained_rank=111,uncovered_retained_dimension=1,DNE50_109_span_contained=True,prior_88_guard_preserved=True,physical_guard=str(guard),whole_aperture_positive=False,strict_collective_separation_from_remaining_source_bound=True,CC_fixed_family_dominates_DNE50_even_family=False,computational_cost_dominance_proved=False,RH=False,F4=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--output',required=True);a.add_argument('--gate',required=True);a.add_argument('--replay');x=a.parse_args();run(x.output,x.gate,x.replay)
