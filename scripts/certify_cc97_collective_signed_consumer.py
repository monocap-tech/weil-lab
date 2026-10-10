#!/usr/bin/env python3
"""Independent interval consumer of DNE35's complete collective source packet."""
import argparse,base64,gzip,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as rounded

K=F(11,25)
def rawread(root,path,sha=None):
 b=(root/path).read_bytes()
 if sha:assert hashlib.sha256(b).hexdigest()==sha
 if path.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
 return json.loads(b),hashlib.sha256(b).hexdigest()
def encloses(a,b):assert a[0]<=b[0]<=b[1]<=a[1]
def positive(proof,expected):
 stored=c.matrix(proof['original_matrix']);n=len(stored);U=[[F(x) for x in row] for row in proof['exact_congruence_U']]
 for i in range(n):
  assert U[i][i]!=0 and all(U[i][j]==0 for j in range(i))
  for j in range(n):encloses(stored[i][j],expected[i][j])
 ui=[[c.iv(x) for x in row] for row in U]
 # Fresh outward 80-significant-digit rational arithmetic, independent
 # of DNE's directed Decimal producer and its stored congruence result.
 computed=rounded.mm(c.transpose(ui),rounded.mm(stored,ui))
 margins=[computed[i][i][0]-sum(rounded.absmax(computed[i][j]) for j in range(n) if j!=i) for i in range(n)]
 assert min(margins)>0
 return min(margins)/sum(x*x for row in U for x in row)
def run(root):
 manifest,_=rawread(root,'notes/data/RPB108_DNE35_CUSTODY_20261009.json','bc10e925b59df8fc97bde3b4f5370cbb827c63a1fbed1e474444ca8cd39f460a')
 pins={x['path']:x for x in manifest['files']}
 def read(path):
  pin=pins[path];data,sha=rawread(root,path,pin['stored_sha256'])
  if 'decoded_sha256' in pin:assert sha==pin['decoded_sha256']
  return data,sha
 validation,_=read('notes/data/RPB108_DNE35_SIGNED_SOURCE_VALIDATION_20261009.json');assert validation['status']=='PASS'
 rows=[];entries=0
 for parity in ['even','odd']:
  source,sourcehash=read('notes/data/RPB108_DNE35_'+parity.upper()+'_JOINT_SOURCE_REPLAY_20261009.json.gz.b64')
  comparison,comphash=read('notes/data/RPB108_DNE35_'+parity.upper()+'_SIGNED_COMPARISON_20261009.json')
  assert source['regular_order']==400 and source['precision']==620 and source['columns']==list(range(12))
  assert comparison['original_high_floor']=='11/25' and comparison['input_sha256'][1]==sourcehash
  assert comparison['certified_joint_prefix_dimension']==12 and comparison['full_joint_signed_budget_passed']
  assert source['complete_original_source_action'] and source['complete_joint_source_Gram_certified']
  assert source['exact_endpoint_logs'] and source['all_six_primes_both_orientations'] and not source['sampled_quadrature']
  assert source['retained_projection_indices']==list(range(int(parity=='odd'),112,2))
  Q=c.matrix(source['native_block']);G=c.matrix(source['original_projected_source_Gram'])
  whole=c.matrix(source['complete_rounded_source_Gram']);coords=c.matrix(source['retained_rounded_source_coordinates']);projected=c.matrix(source['projected_rounded_source_Gram'])
  errors=list(map(F,source['source_L2_error_upper']));roots=list(map(F,source['projected_source_norm_upper']))
  masses=list(map(F,source['exact_masses']));norms=list(map(F,source['physical_norm_upper']))
  assert len(masses)==12 and len(coords)==12 and all(len(row)==56 for row in coords)
  eta=F(source['uniform_original_source_operator_error_upper'])
  assert eta>=2*F(53,50)*F(550,19)*F(106,125)**400+F(3,10**99)
  for i in range(12):
   assert masses[i]>0 and norms[i]**2>=masses[i]
   assert errors[i]>=eta*norms[i]+F(source['polynomial_rounding_source_L2_error_upper'][i])
   assert roots[i]>0 and roots[i]**2>=projected[i][i][1]
   for j in range(12):
    assert G[i][j]==G[j][i] and whole[i][j]==whole[j][i]
    recon=c.sub(whole[i][j],c.sumiv(c.mul(x,y) for x,y in zip(coords[i],coords[j])))
    assert recon==projected[i][j]
    pay=F(source['source_Gram_error_payments'][i][j]);assert pay>=errors[i]*roots[j]+errors[j]*roots[i]+errors[i]*errors[j]
    assert G[i][j]==c.add(recon,(-pay,pay));entries+=1
  H=[[c.sub(c.mul(c.iv(K),Q[i][j]),G[i][j]) for j in range(12)] for i in range(12)]
  nativefloor=positive(comparison['joint_native_positive_control'],Q)
  signedfloor=positive(comparison['positive_joint_prefix_certificate'],H)
  schur=signedfloor/K;mass=sum(masses);trace=sum(G[i][i][1] for i in range(12));assert trace>0
  gap=min(schur/(4*(mass+trace/K**2)),K/2)
  inherited=next(r for r in validation['rows'] if r['parity']==parity)
  assert inherited['replay_sha256']==sourcehash and inherited['comparison_sha256']==comphash
  assert inherited['all_high_positive_retained_rank']==12
  guard=F(1,10**37);assert gap>guard
  rows.append(dict(parity=parity,complete_signed_source_entries_rechecked=144,
   native_coefficient_floor_lower=c.pair(c.iv(nativefloor))[0],signed_coefficient_floor_lower=c.pair(c.iv(signedfloor))[0],
   original_all_high_physical_gap_lower=c.pair(c.iv(gap))[0],retained_rank_inherited_from_independent_DNE35_validation=12))
 replay,replaysha=rawread(root,'notes/data/RPB108_NF48_ORIGINAL_NF46_REPLAY_20261009.json','fb4c9ac456e2e07890bd46caabeed7eaf27c395de671702960bbb270a2d1a26c')
 native,nativesha=rawread(root,'notes/data/RPB108_NF48_REMAINING_NATIVE_VALIDATION_20261009.json','4e7af1bcb9566d8a1da97d2ab3b0a451c1864350066b91e758aaa1e1ccd0cc20')
 assert replay['status']=='PASS' and replay['NF48_independent_native_validation_sha256']==nativesha and native['status']=='PASS'
 stages=replay['unchanged_historical_runner_report']['fresh_NF46_replay'];assert [r['stage'] for r in stages]==['selection','certification','independent_validation']
 assert all(r['status']=='PASS_BYTE_IDENTICAL' for r in stages)
 assert stages[1]['output_sha256']=='4556f7f990a5ba9e7ec139e5f809b8b26b51203ca790f224b6f63f22299c69e7'
 assert stages[2]['output_sha256']=='22984c0fc5a716c61e649e7334b97e0bcf9b30eeb3af4979f7e546563ac93a37'
 return dict(milestone='CC97',integration_parent='0433db37dbf63c6f0f2d1a64890cc87c8c352c0b',
  read_only_DNE='2154898d5d346883cfb201d3a846f19758ac72da',read_only_Native_Source='6847ef8c2501682d60d497043f510987dd70d93b',
  parity_checks=rows,complete_source_entries_rechecked=entries,current_collective_retained_rank=24,
  remaining_uncovered_retained_dimension=88,original_all_high_physical_gap_guard='1/'+str(10**37),
  NF48_source_replay_blocker_resolved_upstream=True,NF48_replay_manifest_sha256=replaysha,
  NF48_finite_native_validation_sha256=nativesha,NF48_finite_remaining_sign_inherited=True,
  original_source_integrations_freshly_rerun_in_CC=False,source_trial_rank_proof_inherited=True,
  different_certified_subspace_gaps_not_added=True,complete_retained_matrix_certified=False,
  whole_aperture_positive=False,highest_certified_whole_aperture='21/20')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('source_root',type=Path);ap.add_argument('--output',type=Path,required=True)
 a=ap.parse_args();d=run(a.source_root);a.output.write_text(json.dumps(d,indent=2)+'\n')
 print('CC97 PASS: 288 signed source entries and both collective congruences; 24 retained directions plus all F')
