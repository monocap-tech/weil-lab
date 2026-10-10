#!/usr/bin/env python3
"""Integrate the actual seventh-weight high floor with the unchanged packet."""
import json,hashlib,argparse
from pathlib import Path
from fractions import Fraction as F
import certify_cc81_boundary_response_consumer as c
import certify_cc97_collective_signed_consumer as consumer
import certify_cc102_dne38_collective_consumer as prior

K=F(289,500)
def run(root):
 base=root.resolve().parents[1]
 # Recompute the old source audit and CC101 overlap instead of relying on
 # a saved CC102 conclusion. The old failure remains a historical control.
 old=prior.run(base/'notes/cc102-source',base/'notes/data',base/'notes/cc100-source')
 assert old['complete_source_entries_rechecked']==1568
 assert old['fresh_CC101_restriction_entries_matched']==882
 manifest,mh=consumer.rawread(root,'notes/data/RPB108_DNE39_CUSTODY_20261010.json')
 pins={x['path']:x for x in manifest['files']}
 for path,pin in pins.items():
  assert hashlib.sha256((root/path).read_bytes()).hexdigest()==pin['stored_sha256']
 def read(path):return consumer.rawread(root,path,pins[path]['stored_sha256'])
 hv,hvh=read('notes/data/RPB108_DNE39_HIGH_FLOOR_VALIDATION_20261010.json')
 freshpath=base/'notes/data/RPB108_CC103_FRESH_HIGH_FLOOR_AUDIT_20261010.json'
 assert freshpath.read_bytes()==(root/'notes/data/RPB108_DNE39_HIGH_FLOOR_VALIDATION_20261010.json').read_bytes()
 assert hv['status']=='PASS' and hv['exact_rational_checks']==96416
 assert hv['original_infinite_F112_floor']==str(K)
 high,highh=read('notes/data/RPB108_DNE39_PRIME_SCHUR_REPLAY_20261010.json')
 assert any(x['sha256']==highh for x in hv['rows'])
 assert F(high['rigorous_max_row_ratio_upper'])<F(21941,10000)
 raw=F(high['inherited_arch_minus_pole_strict_lower'])-F(21941,10000)
 assert raw>K and high['certified_original_F112_lower']==str(K)
 validation,vh=read('notes/data/RPB108_DNE39_SIGNED_SOURCE_VALIDATION_20261010.json')
 assert validation['status']=='PASS' and validation['high_floor_validation_sha256']==hvh
 rows=[]
 for parity in ['even','odd']:
  sp='notes/data/RPB108_DNE38_'+parity.upper()+'_JOINT_SOURCE_REPLAY_20261010.json.gz.b64'
  pin=next(x for x in manifest['reused_inputs'] if x['path']==sp)
  source,sh=consumer.rawread(base/'notes/cc102-source',sp,pin['stored_sha256'])
  assert sh==pin['decoded_sha256']
  comp,ch=read('notes/data/RPB108_DNE39_'+parity.upper()+'_SIGNED_COMPARISON_20261010.json')
  assert comp['original_high_floor']==str(K) and comp['input_sha256'][1]==sh
  assert comp['certified_joint_prefix_dimension']==28 and comp['full_joint_signed_budget_passed']
  Q=c.matrix(source['native_block']);G=c.matrix(source['original_projected_source_Gram'])
  H=[[c.sub(c.mul(c.iv(K),q),g) for q,g in zip(qr,gr)] for qr,gr in zip(Q,G)]
  nf=consumer.positive(comp['joint_native_positive_control'],Q)
  sf=consumer.positive(comp['positive_joint_prefix_certificate'],H)
  masses=list(map(F,source['exact_masses']));trace=sum(G[i][i][1] for i in range(28))
  gap=min(sf/K/(4*(sum(masses)+trace/K**2)),K/2)
  assert gap>F(1,10**38)
  v=list(map(F,comp['exact_failure_trial']));signed=c.quad(H,v)
  consumer.encloses(c.iv(comp['failure_trial_signed_budget']),signed);assert signed[0]>0
  inherited=next(x for x in validation['rows'] if x['parity']==parity)
  assert inherited['replay_sha256']==sh and inherited['comparison_sha256']==ch
  assert inherited['all_high_positive_retained_rank']==28
  rows.append(dict(parity=parity,retained_rank_inherited_from_DNE39=28,
   original_native_coefficient_floor_lower=c.pair(c.iv(nf))[0],
   signed_coefficient_floor_lower=c.pair(c.iv(sf))[0],
   all_high_physical_gap_lower=c.pair(c.iv(gap))[0],
   stored_trial_signed_budget=c.pair(signed),source_decoded_sha256=sh,comparison_sha256=ch))
 return dict(milestone='CC103',integration_parent='de026740e0186cd2f21d9dc40c99af04069fc1c1',
  read_only_DNE='f15eea0a2d0a4b527bf62d73c17efd940b6eb12f',DNE39_custody_sha256=mh,
  fresh_high_floor_replay_byte_identical=True,fresh_high_floor_rational_checks=96416,
  high_floor_audit_sha256=hvh,signed_source_validation_sha256=vh,
  complete_source_entries_freshly_rechecked=1568,fresh_CC101_restriction_entries_matched=882,
  original_high_floor=str(K),prime_norm_strict_upper='21941/10000',raw_high_strict_lower=str(raw),
  parity_checks=rows,current_collective_retained_rank=56,remaining_retained_dimension=56,
  all_high_physical_gap_guard='1/'+str(10**38),conditional_CC102_floor_target_now_discharged=True,
  original_source_integrations_and_rank_proofs_inherited=True,
  underlying_NF10_analytic_high_theorems_inherited=True,
  original_source_integrations_freshly_rerun_in_CC103=False,
  eighth_weight_probe_not_used_as_certified_operator_input=True,
  highest_certified_whole_aperture='21/20',whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('root',type=Path);p.add_argument('--output',type=Path,required=True)
 a=p.parse_args();d=run(a.root);a.output.write_text(json.dumps(d,indent=2)+'\n')
 print('CC103 PASS: actual 0.578 floor; 56 retained directions plus every original high vector')
