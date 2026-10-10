#!/usr/bin/env python3
"""Authenticate full Z56 and pay all response rows at the actual floor."""
from pathlib import Path
from fractions import Fraction as F
import sys,os,json,argparse,gzip,base64,hashlib
import validate_cc105_selected_response as data
import certify_cc81_boundary_response_consumer as c
import certify_cc101_next_source_packet as proof
import certify_cc88_correlated_seventh_response as r
from cc116_response_transport import transport,signed_rows
BASE=Path(__file__).resolve().parents[1];K=F(647,1000)
def run():
 checks=0;rows=[]
 def check(v):
  nonlocal checks
  assert v;checks+=1
 dne,dh,_=data.read('notes/cc116-source/notes/data/RPB108_DNE49_COMPLETE_PACKET_GATE_20261010.json.gz.b64');audit,ah,_=data.read('notes/cc116-source/notes/data/RPB108_DNE49_COMPLETE_PACKET_VALIDATION_20261010.json');check(audit['status']=='PASS' and audit['certificate_sha256']==dh)
 old,oh,_=data.read('notes/data/RPB108_CC115_CORRECTED_647_RESPONSE_20261010.json');check(old['status']=='PASS' and old['original_high_floor']==str(K));floor,fh,_=data.read('notes/data/RPB108_CC113_FRESH_HIGH_FLOOR_AUDIT_20261010.json');check(floor['status']=='PASS' and F(floor['original_infinite_F112_floor'])>=K)
 # Independent packet expansion from the original frozen DNE32 inputs.
 sys.path.insert(0,str(BASE/'notes/cc101-source/scripts'))
 from materialize_cc116_complete_packet import run as materialize
 saved=Path.cwd()
 for idx,p in enumerate(['even','odd']):
  output=BASE/'work'/f'cc116-{p}-packet.json';os.chdir(BASE/'notes/cc101-source')
  try:materialize(f'notes/data/RPB108_DNE32_{p.upper()}_NATIVE_REMAINDER_CERTIFICATE_20261009.json.gz.b64',str(output))
  finally:os.chdir(saved)
  packet,ph,_=data.read(str(output));row=dne['rows'][idx];check(row['parity']==p and packet['columns']==row['columns']);check(packet['native_matrix']==row['native_matrix']);check(packet['input_sha256'][:4]==row['input_sha256']);check(len(packet['columns'])==56 and packet['column_labels']==row['column_labels'])
  z45,z45h,_=data.read(f'notes/data/RPB108_CC115_{p.upper()}_PHYSICAL_PACKET_20261010.json.gz.b64');check(packet['columns'][:45]==z45['columns']);check([x[:45] for x in packet['native_matrix'][:45]]==z45['native_matrix'])
  q=c.matrix(packet['native_matrix']);d,qp=proof.proof(q,row['finite_native_positive_certificate']['exact_congruence_U']);check(d>0)
  tr,th=transport(p,packet);check(tr['fresh_retained_rank']==56 and tr['exact_prefix_preserved']);high,hh,_=data.read(f'notes/cc104-source/notes/data/RPB108_NF52_{p.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64');check(hh==old['parity_checks'][idx]['high_decoded_sha256'])
  W=signed_rows(p,K,high,tr);check([[c.pair(x) for x in row] for row in W[:44]]==old['parity_checks'][idx]['signed_response_rows']);check(len(W)==56 and all(len(x)==11-idx for x in W))
  N=r.sub(r.scale(c.matrix(high['enlarged_high_complete_source_Gram']),1/K),c.matrix(high['enlarged_high_native_Gram']));_,np=proof.proof(N,old['parity_checks'][idx]['denominator_positive_proof']['frozen_rational_congruence'])
  # Separately reconstruct each newly paid signed entry from exact coefficients.
  C=c.matrix(tr['Native_trial_transport_C']);D=c.matrix(tr['paid_high_transport_D']);t=list(map(F,tr['missing_high_transport_row_t']));BN,SN,QY,GY=[c.matrix(high[k]) for k in ['enlarged_joint_high_native_crosses','enlarged_joint_high_complete_source_crosses','enlarged_high_native_Gram','enlarged_high_complete_source_Gram']];v,_,_=data.read(f'notes/data/RPB108_CC113_{p.upper()}_SOURCE_REPLAY_20261010.json');gv=list(map(c.iv,v['original_projected_source_Gram'][0][1:]));qv=list(map(c.iv,tr['recovered_native_residual_high_row']))
  for i in range(44,56):
   for j in range(11-idx):
    direct=c.sumiv([c.mul(C[a][i],c.sub(SN[a][j],c.mul(c.iv(K),BN[a][j]))) for a in range(56)]+[c.mul(D[a][i],c.sub(GY[a][j],c.mul(c.iv(K),QY[a][j]))) for a in range(11-idx)]+[c.mul(c.iv(t[i]),c.sub(gv[j],c.mul(c.iv(K),qv[j])))])
    check(W[i][j][0]<=direct[0]<=direct[1]<=W[i][j][1])
  mapping=list(range(44))+list(range(47,59)) if idx==0 else list(range(56));check(mapping==row['native_to_source']);expected=[[i,j] for i in range(59-3*idx) for j in range(i,59-3*idx) if j>=47-3*idx];check(expected==row['missing_source_upper_triangle']);check(len(expected)==642-36*idx)
  rows.append(dict(parity=p,DNE49_decoded_sha256=dh,physical_packet_decoded_sha256=ph,NF52_high_decoded_sha256=hh,CC112_transport_decoded_sha256=th,exact_transport=tr,complete_signed_response_rows=[[c.pair(x) for x in row] for row in W],signed_response_floor=str(K),full_retained_rank=56,finite_native_positive_proof=qp,response_denominator_positive_proof=np,source_native_map=mapping,DNE50_missing_source_correlation_count=len(expected),fresh_new_response_entries=12*(11-idx),literal_corrected44_response_prefix_preserved=True,independent_entrywise_new_response_reassembly_passed=True))
 return dict(milestone='CC116',status='PASS',parent='31d3052d312b2c017d452df99d07376cb7d4f47d',DNE49_validation_sha256=ah,CC115_corrected_certificate_sha256=oh,current_high_floor_validation_sha256=fh,exact_rational_acceptance_checks=checks,parity_checks=rows,full_exact_retained_chart_rank=112,complete_current_family_response_rows_paid=True,new_response_entries=252,new_source_integrations=0,complete_original_G56_certified=False,final_whole_response_gate_evaluated=False,integrated_positive_retained_rank=88,uncovered_retained_dimension=24,physical_guard=str(F(1,10**37)),whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--output',required=True);args=a.parse_args();raw=(json.dumps(run(),indent=2)+'\n').encode();Path(args.output).write_bytes(base64.b64encode(gzip.compress(raw,mtime=0))+b'\n')
