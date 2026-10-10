#!/usr/bin/env python3
"""Authenticate DNE43 floor replay and freshly pay both complete packets."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
import validate_cc105_selected_response as data
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc101_next_source_packet as proof
BASE=Path(__file__).resolve().parents[1];K=F(603,1000)
def read(p):return data.read(p)
def run():
 checks=0;rows=[]
 def check(v):
  nonlocal checks
  assert v;checks+=1
 custody=json.loads((BASE/'notes/cc109-source/input_custody.json').read_bytes())
 for pin in custody['files']:check(hashlib.sha256((BASE/'notes/cc109-source'/pin['path']).read_bytes()).hexdigest()==pin['stored_sha256'])
 high,hh,_=read('notes/data/RPB108_CC109_FRESH_HIGH_FLOOR_AUDIT_20261010.json');published,ph,_=read('notes/cc109-source/notes/data/RPB108_DNE43_HIGH_FLOOR_VALIDATION_20261010.json');check(high=={k:v for k,v in published.items() if k!='certificate_hash_encoding'});check(published['certificate_hash_encoding']=='decoded JSON bytes; gzip base64 roundtrip verified');check(high['status']=='PASS' and high['original_infinite_F112_floor']==str(K))
 for row in high['rows']:check(read('notes/cc109-source/'+row['path'])[1]==row['sha256'])
 standing,sh,_=read('notes/data/RPB108_CC108_DNE41_INTEGRATION_20261010.json');check(standing['integrated_retained_rank']==69 and standing['original_high_floor']=='73/125')
 transfer,th,_=read('notes/cc109-source/notes/data/RPB108_DNE43_FULL_PACKET_VALIDATION_20261010.json');check(transfer['status']=='PASS' and transfer['all_high_positive_retained_dimension']==72 and transfer['original_infinite_F112_floor']==str(K))
 for path,h in zip(transfer['input_paths'],transfer['input_sha256']):
  root='notes/cc109-source/' if 'DNE43' in path else 'notes/cc108-source/';check(read(root+path)[1]==h)
 for idx,p in enumerate(['even','odd']):
  up=p.upper();s,sourcehash,_=read(f'notes/cc108-source/notes/data/RPB108_DNE40_{up}_JOINT_SOURCE_REPLAY_20261010.json.gz.b64');check(sourcehash==standing['parity_checks'][idx]['source_replay_sha256'])
  target,targethash,_=read(f'notes/cc108-source/notes/data/RPB108_DNE42_{up}_UNIFORM_FLOOR_TARGET_20261010.json');old,oldhash,_=read(f'notes/cc108-source/notes/data/RPB108_DNE40_{up}_SIGNED_COMPARISON_20261010.json');check(target['input_sha256'][:2]==[sourcehash,oldhash])
  tr=next(x for x in transfer['rows'] if x['parity']==p);check(tr['target_certificate_sha256']==targethash and tr['positive_retained_rank']==36)
  Q=c.matrix(s['native_block']);G=c.matrix(s['original_projected_source_Gram']);check(len(Q)==len(G)==36);u=F(target['critical_uniform_floor_upper']);check(u<K)
  native_d,native_proof=proof.proof(Q,old['joint_native_positive_control']['exact_congruence_U']);check(native_d>0)
  H=r.sub(r.scale(Q,K),G);d,pc=proof.proof(H);check(d>0)
  masses=list(map(F,s['exact_masses']));mass=sum(masses);trace=sum(G[i][i][1] for i in range(36));check(mass==F(target['conditional_physical_mass']) and trace>0);gap=min((d/K)/(4*(mass+trace/K**2)),K/2);check(gap>F(1,10**40))
  c41,ch,_=read(f'notes/cc108-source/notes/data/RPB108_DNE41_{up}_POSITIVE_SUBSPACE_20261010.json');check(ch==standing['parity_checks'][idx]['DNE41_certificate_sha256']);check(len(c41['positive_embedding_B'])==36 and c41['positive_retained_rank']+c41['negative_comparison_rank']==36)
  # CC108 checked exact full rank of (B,D) and physical rank/containment.
  check(standing['parity_checks'][idx]['prior_CC103_span_contained'])
  rows.append(dict(parity=p,positive_retained_rank=36,source_replay_sha256=sourcehash,DNE42_target_certificate_sha256=targethash,fresh_native_positive_proof=native_proof,fresh_complete_comparison_positive_proof=pc,physical_mass_sum=str(mass),complete_source_trace_upper=str(trace),all_high_physical_gap_lower=str(gap),prior_69_direction_span_contained=True))
  print(p,'complete rank 36 positive; physical gap',float(gap),flush=True)
 minimum=min(F(x['all_high_physical_gap_lower']) for x in rows);guard=F(1,10**40)
 while guard*10<minimum:guard*=10
 check(guard<minimum)
 return dict(milestone='CC109',parent='b4d4224fe95935166e01db50a47d7e0cde235904',read_only_DNE='5ec8aeeb73fa67eff670e0716a1a752f5d3e64b3',original_high_floor=str(K),fresh_high_floor_validation_sha256=hh,published_high_floor_validation_sha256=ph,exact_high_floor_mathematical_fields_reproduced=True,fresh_high_floor_rational_checks=high['exact_rational_checks'],new_integration_rational_checks=checks,DNE43_full_packet_validation_sha256=th,CC108_standing_sha256=sh,parity_checks=rows,integrated_retained_rank=72,uncovered_retained_dimension=40,all_high_physical_gap_guard=str(guard),prior_69_direction_guard_preserved=standing['all_high_physical_gap_guard'],source_integrals_recomputed=False,physical_domain_and_full_packet_rank_attachment_inherited=True,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();Path(a.output).write_text(json.dumps(run(),indent=2)+'\n')
