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
 manifest,_=rawread(root,'notes/data/RPB108_DNE36_CUSTODY_20261010.json','083921a6231c5a7d70c612e2124cae174d732c98ec801c947b825c5a663af966')
 pins={x['path']:x for x in manifest['files']}
 def read(path):
  pin=pins[path];data,sha=rawread(root,path,pin['stored_sha256'])
  if 'decoded_sha256' in pin:assert sha==pin['decoded_sha256']
  return data,sha
 validation,_=read('notes/data/RPB108_DNE36_SIGNED_SOURCE_VALIDATION_20261010.json')
 assert validation['status']=='PASS'
 rows=[]
 for parity,n in [('even',18),('odd',17)]:
  source,sha=read('notes/data/RPB108_DNE36_'+parity.upper()+'_JOINT_SOURCE_REPLAY_20261010.json.gz.b64')
  d,dh=read('notes/data/RPB108_DNE36_'+parity.upper()+'_SIGNED_COMPARISON_20261010.json')
  assert d['input_sha256'][1]==sha and d['original_high_floor']=='11/25'
  assert source['columns']==list(range(20)) and source['regular_order']==400 and source['precision']==620
  assert source['complete_original_source_action'] and source['complete_joint_source_Gram_certified']
  assert source['exact_endpoint_logs'] and source['all_six_primes_both_orientations'] and not source['sampled_quadrature']
  assert source['retained_projection_indices']==list(range(int(parity=='odd'),112,2))
  Q=c.matrix(source['native_block']);G=c.matrix(source['original_projected_source_Gram'])
  whole=c.matrix(source['complete_rounded_source_Gram']);coords=c.matrix(source['retained_rounded_source_coordinates']);proj=c.matrix(source['projected_rounded_source_Gram'])
  errors=list(map(F,source['source_L2_error_upper']));roots=list(map(F,source['projected_source_norm_upper']))
  masses=list(map(F,source['exact_masses']));norms=list(map(F,source['physical_norm_upper']))
  eta=F(source['uniform_original_source_operator_error_upper'])
  assert eta>=2*F(53,50)*F(550,19)*F(106,125)**400+F(3,10**99)
  for i in range(20):
   assert masses[i]>0 and norms[i]**2>=masses[i] and len(coords[i])==56
   assert errors[i]>=eta*norms[i]+F(source['polynomial_rounding_source_L2_error_upper'][i])
   assert roots[i]**2>=proj[i][i][1]
   for j in range(20):
    assert G[i][j]==G[j][i]
    recon=c.sub(whole[i][j],c.sumiv(c.mul(x,y) for x,y in zip(coords[i],coords[j])))
    assert recon==proj[i][j]
    pay=F(source['source_Gram_error_payments'][i][j])
    assert pay>=errors[i]*roots[j]+errors[j]*roots[i]+errors[i]*errors[j]
    assert G[i][j]==c.add(recon,(-pay,pay))
  H=[[c.sub(c.mul(c.iv(K),Q[i][j]),G[i][j]) for j in range(20)] for i in range(20)]
  nf=positive(d['joint_native_positive_control'],Q)
  hf=positive(d['positive_joint_prefix_certificate'],[r[:n] for r in H[:n]])
  gap=min(hf/K/(4*(sum(masses[:n])+sum(G[i][i][1] for i in range(n))/K**2)),K/2)
  assert gap>F(1,10**38)
  failures=[]
  first=d['first_failing_joint_prefix']
  assert first['joint_dimension']==n+1 and d['certified_joint_prefix_dimension']==n
  for dim,v,qn,gn,hn in [(20,d['exact_failure_trial'],d['failure_trial_native_energy'],d['failure_trial_source_energy'],d['failure_trial_signed_budget']),
   (n+1,first['exact_trial'],first['native_energy'],first['source_energy'],first['signed_budget'])]:
   v=list(map(F,v));assert len(v)==dim and any(v)
   q=c.quad([r[:dim] for r in Q[:dim]],v);g=c.quad([r[:dim] for r in G[:dim]],v);h=c.sub(c.mul(c.iv(K),q),g)
   encloses(c.iv(qn),q);encloses(c.iv(gn),g);encloses(c.iv(hn),h)
   assert q[0]>0 and h[1]<0
   # Necessary correction along this vector: kappa^-2 v*W N^-1 W*v > -h/kappa.
   failures.append(dict(dimension=dim,signed_budget=c.pair(h),
    required_response_gain_lower=c.pair(c.iv(-h[1]/K))[0]))
  vr=next(x for x in validation['rows'] if x['parity']==parity)
  assert vr['replay_sha256']==sha and vr['comparison_sha256']==dh and vr['all_high_positive_retained_rank']==n
  rows.append(dict(parity=parity,retained_rank_inherited=n,source_entries_rechecked=400,
   native_coefficient_floor_lower=c.pair(c.iv(nf))[0],physical_gap_lower=c.pair(c.iv(gap))[0],failures=failures))
 # Exact same-floor strict separation: A=1, kappa=.44, R=1, Q=1.5, paid high vector H=1.
 q=F(3,2);a=F(1);r=F(1);hh=F(1)
 denominator=hh*hh*(a*a/K-a);w=r*(a-K)*hh
 plain=q-r*r/K;corrected=plain+w*w/(K*K*denominator)
 assert denominator>0 and plain<0 and corrected==F(1,2)
 return dict(milestone='CC99',read_only_DNE='b45a73dd626380d87940d72fcee22208c1ff182f',
  parity_checks=rows,source_entries_rechecked=800,collective_retained_rank=35,remaining_retained_dimension=77,
  all_high_physical_gap_guard='1/'+str(10**38),same_floor_strict_separation={'plain':str(plain),'response':str(corrected)},
  first_failing_packet_additional_mixed_source_entries=19*8+18*7,full_twenty_packets_additional_mixed_source_entries=20*8+20*7,
  actual_DNE36_response_crosses_available=False,actual_DNE36_response_rescue_proved=False,
  original_source_integrations_freshly_rerun_in_CC=False,retained_rank_proof_inherited=True,
  complete_remaining_source_Gram_certified=False,whole_aperture_positive=False,RH=False,Lean=False)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('source_root',type=Path);ap.add_argument('--output',type=Path,required=True)
 a=ap.parse_args();d=run(a.source_root);a.output.write_text(json.dumps(d,indent=2)+'\n')
 print('CC99 PASS: 800 source entries, positive prefixes and exact uniform-floor failures; same-floor strict separation')
