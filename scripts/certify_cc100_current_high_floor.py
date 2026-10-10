#!/usr/bin/env python3
"""Fresh band audit and collective import of DNE37; exact floor-demand brackets."""
import argparse,hashlib,json,os,sys
from pathlib import Path
from fractions import Fraction as F
import numpy as np
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc97_collective_signed_consumer as consumer
import certify_cc99_response_frontier as old

K=F(57,100)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def demand(Q,G,proof):
 U=[[F(x) for x in row] for row in proof['exact_congruence_U']]
 ui=[[c.iv(x) for x in row] for row in U]
 q=r.mm(c.transpose(ui),r.mm(Q,ui));g=r.mm(c.transpose(ui),r.mm(G,ui))
 qm=np.array([[float(sum(x)/2) for x in row] for row in q]);gm=np.array([[float(sum(x)/2) for x in row] for row in g])
 li=np.linalg.inv(np.linalg.cholesky((qm+qm.T)/2));gg=li@gm@li.T
 ev,evec=np.linalg.eigh((gg+gg.T)/2);grid=10**7
 lower=F(int(np.floor(ev[-1]*grid))-1,grid);upper=F(int(np.ceil(ev[-1]*grid))+1,grid)
 v=[F(round(F(float(x))*10**30),10**30) for x in li.T@evec[:,-1]]
 qv=c.quad(q,v);gv=c.quad(g,v)
 lowertrial=c.sub(c.mul(c.iv(lower),qv),gv);assert qv[0]>0 and lowertrial[1]<0
 h=r.sub(r.scale(q,upper),g);hm=np.array([[float(sum(x)/2) for x in row] for row in h])
 candidate=np.linalg.inv(np.linalg.cholesky((hm+hm.T)/2)).T
 V=[[F(round(F(float(x))*10**30),10**30) if j>=i else F(0) for j,x in enumerate(row)] for i,row in enumerate(candidate)]
 assert all(V[i][i]!=0 and all(V[i][j]==0 for j in range(i)) for i in range(20))
 vi=[[c.iv(x) for x in row] for row in V];paid=r.mm(c.transpose(vi),r.mm(h,vi))
 margins=[paid[i][i][0]-sum(r.absmax(paid[i][j]) for j in range(20) if j!=i) for i in range(20)]
 assert min(margins)>0 and upper-lower<=F(3,grid) and upper<K
 return dict(critical_uniform_floor_lower=str(lower),critical_uniform_floor_upper=str(upper),
  native_preconditioner='authenticated joint_native_positive_control.exact_congruence_U',
  lower_failure_vector_in_native_preconditioned_coordinates=list(map(str,v)),lower_signed_trial=c.pair(lowertrial),
  upper_frozen_rational_congruence=[list(map(str,row)) for row in V],upper_paid_Gershgorin_margin=c.pair(c.iv(min(margins)))[0],
  available_floor_minus_required_upper=str(K-upper))
def run(root,priorroot,audit_output):
 root=root.resolve();priorroot=priorroot.resolve();audit_output=audit_output.resolve()
 mp=root/'notes/data/RPB108_DNE37_CUSTODY_20261010.json'
 assert digest(mp)=='91c5b2d359b460789d61af8cf867a77f47a2cfdf14152cb871c95c8bf013b5d9'
 manifest=json.loads(mp.read_text())
 for pin in manifest['files']:
  p=root/pin['path'];assert p.stat().st_size==pin['bytes'] and digest(p)==pin['stored_sha256']
 helper=root/'scripts/dne17_nf10_complement_input.py'
 assert digest(helper)=='207037efc8a824f40a8585f18b63c4e1e92270cd6a41d9414d577ae2510f24b1'
 # Unchanged independent DNE recurrence runner; its relative helper path is resolved in the source root.
 sys.path.insert(0,str(root/'scripts'))
 import validate_dne37_high_floor as floor
 wd=Path.cwd()
 try:
  os.chdir(root)
  floor.run(['notes/data/RPB108_DNE37_PRIME_SCHUR_20261010.json','notes/data/RPB108_DNE37_PRIME_SCHUR_REPLAY_20261010.json'],str(audit_output))
 finally:os.chdir(wd)
 fresh=json.loads(audit_output.read_text());stored=json.loads((root/'notes/data/RPB108_DNE37_HIGH_FLOOR_VALIDATION_20261010.json').read_text())
 assert fresh==stored and fresh['status']=='PASS' and fresh['exact_rational_checks']==62272
 previous=old.run(priorroot)
 validation=json.loads((root/'notes/data/RPB108_DNE37_SIGNED_SOURCE_VALIDATION_20261010.json').read_text())
 assert validation['status']=='PASS' and validation['high_floor_validation_sha256']==digest(audit_output)
 rows=[]
 for parity in ['even','odd']:
  source,sh=consumer.rawread(priorroot,'notes/data/RPB108_DNE36_'+parity.upper()+'_JOINT_SOURCE_REPLAY_20261010.json.gz.b64')
  path=root/('notes/data/RPB108_DNE37_'+parity.upper()+'_SIGNED_COMPARISON_20261010.json');d=json.loads(path.read_text())
  assert d['input_sha256'][1]==sh and d['original_high_floor']==str(K)
  assert d['high_certificate_sha256']==digest(root/d['high_certificate_path'])
  assert d['certified_joint_prefix_dimension']==20 and d['full_joint_signed_budget_passed'] and not d['joint_uniform_floor_failure_proved']
  Q=c.matrix(source['native_block']);G=c.matrix(source['original_projected_source_Gram'])
  H=[[c.sub(c.mul(c.iv(K),q),g) for q,g in zip(qrow,grow)] for qrow,grow in zip(Q,G)]
  consumer.positive(d['joint_native_positive_control'],Q)
  hf=consumer.positive(d['positive_joint_prefix_certificate'],H)
  mass=sum(map(F,source['exact_masses']));trace=sum(G[i][i][1] for i in range(20))
  gap=min(hf/K/(4*(mass+trace/K**2)),K/2);assert gap>F(1,10**37)
  vr=next(x for x in validation['rows'] if x['parity']==parity)
  assert vr['replay_sha256']==sh and vr['comparison_sha256']==digest(path) and vr['all_high_positive_retained_rank']==20
  rows.append(dict(parity=parity,retained_rank_inherited=20,physical_gap_lower=c.pair(c.iv(gap))[0],
   signed_floor_demand=demand(Q,G,d['joint_native_positive_control'])))
 return dict(milestone='CC100',integration_parent='5cd101e1826149782a4c2ff5aeafc1ba582bc325',
  read_only_DNE='f11f94dcd72c2d1a8438bdfbc7e7890b47902088',custody_sha256=digest(mp),
  fresh_high_floor_validation_sha256=digest(audit_output),fresh_high_floor_exact_checks=62272,
  unchanged_high_floor_validator_output_byte_identical=True,complete_source_entries_rechecked=previous['source_entries_rechecked'],
  current_original_high_floor=str(K),parity_checks=rows,current_collective_retained_rank=40,remaining_retained_dimension=72,
  all_high_physical_gap_guard='1/'+str(10**37),historical_CC99_failure_witnesses_rechecked=True,
  response_cross_integrations_needed_for_current_twenty_packets=False,expensive_original_source_integrations_rerun=False,
  high_band_recurrence_and_arch_pole_arithmetic_freshly_replayed=True,analytic_arch_Bessel_and_weight_theorems_inherited=True,
  retained_trial_rank_proofs_inherited=True,complete_remaining_source_Gram_certified=False,
  whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('source_root',type=Path);ap.add_argument('prior_source_root',type=Path)
 ap.add_argument('--audit-output',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
 a=ap.parse_args();d=run(a.source_root,a.prior_source_root,a.audit_output);a.output.write_text(json.dumps(d,indent=2)+'\n')
 print('CC100 PASS: fresh 62272-check high-floor replay; 40 retained directions plus all F112; exact floor-demand brackets')
