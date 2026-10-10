#!/usr/bin/env python3
"""Audit DNE38's complete signed packet against CC101's fresh restriction."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
import certify_cc81_boundary_response_consumer as c
import certify_cc97_collective_signed_consumer as consumer
import certify_cc88_correlated_seventh_response as response
import certify_cc101_next_source_packet as selected
import sys
K=F(57,100)
def run(root,freshroot,floorroot):
 integration=root.resolve().parents[1]
 sys.path.insert(0,str(integration/'notes/cc101-source/scripts'))
 paidpath=integration/'notes/cc91-source/notes/data/RPB108_NF46_EVEN_NEXT_SHELL_CERTIFICATE_20261009.json'
 assert hashlib.sha256(paidpath.read_bytes()).hexdigest()=='4556f7f990a5ba9e7ec139e5f809b8b26b51203ca790f224b6f63f22299c69e7'
 paid=json.loads(paidpath.read_text())
 denominator=response.sub(response.scale(c.matrix(paid['eight_high_complete_source_Gram']),1/K),c.matrix(paid['eight_high_native_Gram']))
 _,rho,_=response.inverse(denominator)
 mp=root/'notes/data/RPB108_DNE38_CUSTODY_20261010.json'
 assert hashlib.sha256(mp.read_bytes()).hexdigest()=='669c386b7d89c6c1a45e14b07b023da6346e05fc6d52ee5bbec69234ae38351a'
 manifest=json.loads(mp.read_text());pins={x['path']:x for x in manifest['files']}
 def read(p):
  d,dh=consumer.rawread(root,p,pins[p]['stored_sha256'])
  if 'decoded_sha256' in pins[p]:assert dh==pins[p]['decoded_sha256']
  return d,dh
 validation,_=read('notes/data/RPB108_DNE38_SIGNED_SOURCE_VALIDATION_20261010.json');assert validation['status']=='PASS'
 high,_=consumer.rawread(floorroot,'notes/data/RPB108_DNE37_PRIME_SCHUR_REPLAY_20261010.json','d0d6ed5fd83b5f540c448f63cf47039a207327194052324348423628f87f4054')
 rawfloor=F(high['inherited_arch_minus_pole_strict_lower'])-F(high['rigorous_max_row_ratio_upper'])
 freshcert,_=consumer.rawread(freshroot,'RPB108_CC101_NEXT_SOURCE_PACKET_20261010.json')
 rows=[]
 for parity,n in [('even',27),('odd',28)]:
  source,sh=read('notes/data/RPB108_DNE38_'+parity.upper()+'_JOINT_SOURCE_REPLAY_20261010.json.gz.b64')
  d,dh=read('notes/data/RPB108_DNE38_'+parity.upper()+'_SIGNED_COMPARISON_20261010.json')
  assert source['columns']==list(range(28)) and source['regular_order']==400 and source['precision']==620
  assert source['reused_joint_dimension']==20 and source['reused_rounded_source_definition_unchanged']
  assert d['input_sha256'][1]==sh and d['original_high_floor']==str(K) and d['certified_joint_prefix_dimension']==n
  assert source['complete_original_source_action'] and source['exact_endpoint_logs'] and source['all_six_primes_both_orientations'] and not source['sampled_quadrature']
  Q=c.matrix(source['native_block']);G=c.matrix(source['original_projected_source_Gram'])
  whole=c.matrix(source['complete_rounded_source_Gram']);coords=c.matrix(source['retained_rounded_source_coordinates']);proj=c.matrix(source['projected_rounded_source_Gram'])
  errors=list(map(F,source['source_L2_error_upper']));roots=list(map(F,source['projected_source_norm_upper']));masses=list(map(F,source['exact_masses']));norms=list(map(F,source['physical_norm_upper']))
  eta=F(source['uniform_original_source_operator_error_upper'])
  assert eta>=2*F(53,50)*F(550,19)*F(106,125)**400+F(3,10**99)
  assert source['retained_projection_indices']==list(range(int(parity=='odd'),112,2))
  for i in range(28):
   assert norms[i]**2>=masses[i]>0 and len(coords[i])==56
   assert errors[i]>=eta*norms[i]+F(source['polynomial_rounding_source_L2_error_upper'][i]) and roots[i]**2>=proj[i][i][1]
   for j in range(28):
    assert G[i][j]==G[j][i]
    value=c.sub(whole[i][j],c.sumiv(c.mul(x,y) for x,y in zip(coords[i],coords[j])))
    assert value==proj[i][j]
    pay=F(source['source_Gram_error_payments'][i][j]);assert pay>=errors[i]*roots[j]+errors[j]*roots[i]+errors[i]*errors[j]
    assert G[i][j]==c.add(value,(-pay,pay))
  fresh,fh=consumer.rawread(freshroot,'RPB108_CC101_'+parity.upper()+'_REPLAY_20261010.json.gz.b64')
  assert fh==next(x for x in freshcert['parity_checks'] if x['parity']==parity)['replay_decoded_sha256']
  for key in ['native_block','original_projected_source_Gram','complete_rounded_source_Gram','projected_rounded_source_Gram','source_Gram_error_payments']:
   assert all(source[key][i][j]==fresh[key][i][j] for i in range(21) for j in range(21))
  assert source['retained_rounded_source_coordinates'][:21]==fresh['retained_rounded_source_coordinates']
  consumer.positive(d['joint_native_positive_control'],Q)
  H=[[c.sub(c.mul(c.iv(K),q),g) for q,g in zip(qr,gr)] for qr,gr in zip(Q,G)]
  hf=consumer.positive(d['positive_joint_prefix_certificate'],[r[:n] for r in H[:n]])
  gap=min(hf/K/(4*(sum(masses[:n])+sum(G[i][i][1] for i in range(n))/K**2)),K/2);assert gap>F(1,10**38)
  witness=list(map(F,d['exact_failure_trial']));q=c.quad(Q,witness);g=c.quad(G,witness);h=c.sub(c.mul(c.iv(K),q),g)
  assert q[0]>0
  consumer.encloses(c.iv(d['failure_trial_native_energy']),q);consumer.encloses(c.iv(d['failure_trial_source_energy']),g);consumer.encloses(c.iv(d['failure_trial_signed_budget']),h)
  assert F(d['raw_iterated_weight_floor'])==rawfloor
  rawsigned=c.sub(c.mul(c.iv(rawfloor),q),g);consumer.encloses(c.iv(d['raw_weight_floor_trial_signed_budget']),rawsigned)
  threshold=g[0]/q[1];assert threshold>=F(d['trial_required_uniform_floor_lower'])
  targetproof=None
  if parity=='even':
   assert h[1]<0 and rawsigned[1]<0 and threshold>F(577472,1000000)
   target=F(289,500)
   targetmatrix=[[c.sub(c.mul(c.iv(target),qq),gg) for qq,gg in zip(qr,gr)] for qr,gr in zip(Q,G)]
   _,targetproof=selected.proof(targetmatrix)
  else:assert h[0]>0 and d['full_joint_signed_budget_passed']
  inherited=next(x for x in validation['rows'] if x['parity']==parity)
  assert inherited['replay_sha256']==sh and inherited['comparison_sha256']==dh and inherited['all_high_positive_retained_rank']==n
  rows.append(dict(parity=parity,positive_retained_rank_inherited=n,physical_gap_lower=c.pair(c.iv(gap))[0],
   complete_source_entries_rechecked=784,fresh_CC101_twenty_one_column_source_restriction_exactly_matched=True,
   paid_trial_signed_budget=c.pair(h),unrounded_sixth_weight_floor_signed_trial=c.pair(rawsigned),
   necessary_uniform_floor_on_stored_trial_lower=c.pair(c.iv(threshold))[0],
   conditional_sufficient_uniform_floor='289/500' if parity=='even' else str(K),
   even_conditional_target_signed_positive_proof=targetproof,
   necessary_response_gain_on_failed_trial_lower=c.pair(c.iv(-h[1]/K))[0] if parity=='even' else '0'))
 return dict(milestone='CC102',integration_parent='995d7d239006d0ca1f9f1190f3593bb4eef6e2cd',
  read_only_DNE='ee48e0eb6b35987317354ee5fa82142528c108a6',parity_checks=rows,
  current_original_high_floor=str(K),current_collective_retained_rank=55,remaining_retained_dimension=57,
  original_all_high_physical_gap_guard='1/'+str(10**38),complete_source_entries_rechecked=1568,
  fresh_CC101_restriction_entries_matched=882,larger_packet_analytic_source_integrations_and_rank_proofs_inherited=True,
  next_even_response_packet_mixed_source_entries_for_existing_eight_high_family=224,
  eight_high_denominator_at_current_floor_freshly_verified=True,
  eight_high_denominator_inverse_residual_upper=c.pair(c.iv(rho))[1],
  conditional_full_even_packet_floor_target='289/500',
  sufficient_original_prime_norm_strict_upper_target='1097/500',
  target_original_high_floor_newly_proved=False,
  actual_even_response_rescue_proved=False,unrounded_sixth_weight_floor_insufficient=True,
  whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('source_root',type=Path);p.add_argument('fresh_root',type=Path);p.add_argument('floor_root',type=Path);p.add_argument('--output',type=Path,required=True)
 a=p.parse_args();d=run(a.source_root,a.fresh_root,a.floor_root);a.output.write_text(json.dumps(d,indent=2)+'\n')
 print('CC102 PASS: 1568 source entries, fresh 882-entry restriction match; 55 retained directions and paid even obstruction')
