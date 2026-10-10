#!/usr/bin/env python3
"""Pay the complete plain deficit Schur gate; do not invent response crosses."""
from pathlib import Path
from fractions import Fraction as F
import json,argparse,os,subprocess,sys
import validate_cc105_selected_response as data
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc104_joint_response_rebase as response
from certify_cc108_dne41_integration import compress,rank
import certify_cc101_next_source_packet as proof
K=F(603,1000);BASE=Path(__file__).resolve().parents[1]
def run():
 standing,sh,_=data.read('notes/data/RPB108_CC110_EXTENDED_PACKET_INTEGRATION_20261010.json');assert standing['status']=='PASS' and standing['integrated_retained_rank']==85 and standing['original_high_floor']==str(K)
 rows=[];checks=0
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def cross(M,B,D):return r.mm(c.transpose([[c.iv(x) for x in row] for row in B]),r.mm(M,[[c.iv(x) for x in row] for row in D]))
 for idx,p in enumerate(['even','odd']):
  root='notes/cc110-source/notes/data/RPB108_DNE44_'+p.upper()
  s,ss,_=data.read(root+'_JOINT_SOURCE_REPLAY_20261010.json.gz.b64');cert,ch,_=data.read(root+'_POSITIVE_SUBSPACE_20261010.json.gz.b64');old=standing['parity_checks'][idx]
  check(ss==old['source_replay_sha256'] and ch==old['positive_subspace_certificate_sha256'])
  Q=c.matrix(s['native_block']);G=c.matrix(s['original_projected_source_Gram']);H=r.sub(r.scale(Q,K),G)
  B=[list(map(F,row)) for row in cert['positive_embedding_B']];D=[list(map(F,row)) for row in cert['negative_comparison_embedding_D']];n=len(B[0]);z=len(D[0]);check((n,z)==[(42,2),(43,1)][idx] and rank([b+d for b,d in zip(B,D)])==44)
  # Reproduce the immutable raw physical packet, rather than mixing Native frames.
  packet_path=BASE/'work'/f'cc111-{p}-packet.json';packet_path.parent.mkdir(exist_ok=True)
  env=dict(os.environ);env['PYTHONPATH']=str(BASE/'notes/cc110-source/scripts')+os.pathsep+str(BASE/'notes/cc101-source/scripts')
  subprocess.run([sys.executable,str(BASE/'notes/cc110-source/scripts/materialize_dne44_joint_sources.py'),s['certificate_path'],str(packet_path)],cwd=BASE/'notes/cc101-source',env=env,check=True,capture_output=True)
  packet,ps,_=data.read(str(packet_path));packet_path.unlink();check(ps==s['normalized_packet_sha256'])
  raw=[dict(zip(col['indices'],map(F,col['coefficients']))) for col in packet['columns']];check(len(raw)==44 and rank([[col.get(i,F(0)) for i in range(idx,112,2)] for col in raw])==44)
  for j in range(n):check([sum(raw[t].get(i,F(0))*B[t][j] for t in range(44)) for i in cert['physical_indices']]==list(map(F,cert['exact_physical_columns'][j])))
  A=compress(H,B);E=cross(H,B,D);FDD=compress(H,D)
  d,ap=proof.proof(A,cert['positive_comparison_certificate']['exact_congruence_U']);check(d>0)
  AI,rho=response.inverse(A);check(rho<1)
  mixed=r.mm(c.transpose(E),r.mm(AI,E));S=r.sub(FDD,mixed)
  # Symmetric enclosure pays independently rounded transpose entries.
  S=[[(min(S[i][j][0],S[j][i][0]),max(S[i][j][1],S[j][i][1])) for j in range(z)] for i in range(z)]
  minus=r.scale(S,F(-1));nd,np=proof.proof(minus);check(nd>0)
  threshold=max(sum(r.absmax(x) for x in row) for row in minus);check(threshold>0)
  target=threshold+F(1,10**12);test=[[c.add(v,c.iv(target if i==j else 0)) for j,v in enumerate(row)] for i,row in enumerate(S)];td,tp=proof.proof(test);check(td>0)
  naive=[FDD[i][i][1]<0 for i in range(z)];check(all(naive))
  rows.append(dict(parity=p,source_replay_sha256=ss,subspace_certificate_sha256=ch,fresh_raw_physical_packet_sha256=ps,fresh_raw_packet_retained_rank=44,fresh_positive_physical_columns_reconstructed=True,positive_dimension=n,deficit_dimension=z,positive_block_proof=ap,positive_block_inverse_residual_upper=str(rho),plain_mixed_block=[[c.pair(x) for x in row] for row in E],plain_negative_block=[[c.pair(x) for x in row] for row in FDD],mixed_Schur_payment=[[c.pair(x) for x in row] for row in mixed],complete_plain_deficit_gate=[[c.pair(x) for x in row] for row in S],negative_gate_proof=np,necessary_response_rank_lower=z,necessary_response_form_credit_on_each_D_column_lower=[str(-FDD[i][i][1]/K) for i in range(z)],hypothetical_zero_cross_comparison_credit_threshold_upper=str(threshold),hypothetical_verified_comparison_credit=str(target),hypothetical_gate_positive_proof=tp,hypothetical_credit_is_actual_response=False,minimal_high_dimension=z,full_packet_new_source_moments_at_minimal_rank=44*z+z*(z+1)//2,full_packet_new_native_moments_at_minimal_rank=44*z+z*(z+1)//2,complete_same_frame_response_crosses_available=False))
  print(p,'paid negative gate',z,'threshold',float(threshold),'inverse residual',float(rho),flush=True)
 return dict(milestone='CC111',status='PASS',parent='9c66aec88a55cee9dfa6a9e1c699dc280e9ed799',CC110_standing_sha256=sh,original_high_floor=str(K),exact_consumer_checks=checks,parity_checks=rows,same_frame_full_response_gate_reduced=True,actual_response_credit_computed=False,strict_collective_response_separation_proved=False,computational_saving_proved=False,integrated_retained_rank=85,uncovered_retained_dimension=27,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();Path(a.output).write_text(json.dumps(run(),indent=2)+'\n')
