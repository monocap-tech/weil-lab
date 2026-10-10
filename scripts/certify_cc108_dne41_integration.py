#!/usr/bin/env python3
"""Fresh rational compression, source-payment and physical-gap integration."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
import validate_cc105_selected_response as data
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc101_next_source_packet as proof
BASE=Path(__file__).resolve().parents[1];ROOT='notes/cc108-source/';K=F(73,125)
def read(p):return data.read(ROOT+p)
def compress(M,B):
 BI=[[c.iv(x) for x in row] for row in B];return r.mm(c.transpose(BI),r.mm(M,BI))
def rank(M):
 M=[list(row) for row in M];n=0
 for i in range(len(M[0])):
  k=next((j for j in range(n,len(M)) if M[j][i]),None)
  if k is None:continue
  M[n],M[k]=M[k],M[n];pivot=M[n][i]
  for j in range(n+1,len(M)):
   if M[j][i]:
    z=M[j][i]/pivot;M[j]=[a-z*b for a,b in zip(M[j],M[n])]
  n+=1
  if n==len(M):break
 return n

def run():
 checks=0;rows=[]
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def enclose(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
 custody=json.loads((BASE/ROOT/'input_custody.json').read_bytes())
 for pin in custody['files']:check(hashlib.sha256((BASE/ROOT/pin['path']).read_bytes()).hexdigest()==pin['stored_sha256'])
 audit,ah,_=read('notes/data/RPB108_DNE41_POSITIVE_SUBSPACE_VALIDATION_20261010.json');sourceaudit,sah,_=read('notes/data/RPB108_DNE40_SIGNED_SOURCE_VALIDATION_20261010.json');targetaudit,tah,_=read('notes/data/RPB108_DNE42_UNIFORM_FLOOR_TARGET_VALIDATION_20261010.json')
 check(audit['status']==sourceaudit['status']==targetaudit['status']=='PASS');check(audit['all_high_positive_retained_dimension']==69)
 floor,fh,_=data.read('notes/data/RPB108_CC106_HIGH_FLOOR_VALIDATION_20261010.json');check(floor['status']=='PASS' and floor['original_infinite_F112_floor']==str(K))
 for row in floor['rows']:check(hashlib.sha256((BASE/row['path']).read_bytes()).hexdigest()==row['sha256'])
 for idx,p in enumerate(['even','odd']):
  up=p.upper();cert,ch,_=read(f'notes/data/RPB108_DNE41_{up}_POSITIVE_SUBSPACE_20261010.json');report=next(x for x in audit['rows'] if x['parity']==p);check(ch==report['certificate_sha256'])
  inputs=[read(q) for q in cert['input_paths']];check([h for _,h,_ in inputs]==cert['input_sha256']==report['input_sha256']);s,old,v=[x for x,_,_ in inputs]
  sa=next(x for x in sourceaudit['rows'] if x['parity']==p);check(sa['replay_sha256']==inputs[0][1] and sa['comparison_sha256']==inputs[1][1]);check(v==sourceaudit)
  check(s['complete_joint_source_Gram_certified'] and s['complete_original_source_action'] and s['exact_endpoint_logs'] and s['all_six_primes_both_orientations'] and not s['sampled_quadrature'])
  Q=c.matrix(s['native_block']);G=c.matrix(s['original_projected_source_Gram']);check(len(Q)==len(G)==36)
  full=c.matrix(s['complete_rounded_source_Gram']);coords=c.matrix(s['retained_rounded_source_coordinates']);proj=c.matrix(s['projected_rounded_source_Gram']);errors=list(map(F,s['source_L2_error_upper']));norms=list(map(F,s['projected_source_norm_upper']))
  for i in range(36):
   check(norms[i]**2>proj[i][i][1]);check(F(s['physical_norm_upper'][i])**2>F(s['exact_masses'][i]))
   for j in range(36):
    check(G[i][j]==G[j][i]);raw=c.sub(full[i][j],c.sumiv(c.mul(x,y) for x,y in zip(coords[i],coords[j])));check(raw==proj[i][j]);pay=F(s['source_Gram_error_payments'][i][j]);check(pay>=errors[i]*norms[j]+errors[j]*norms[i]+errors[i]*errors[j]);check(G[i][j]==c.add(raw,(-pay,pay)))
  oldsource,osh,_=data.read(f'notes/cc102-source/notes/data/RPB108_DNE38_{up}_JOINT_SOURCE_REPLAY_20261010.json.gz.b64');check(s['reused_source_sha256']==osh and s['reused_joint_dimension']==28 and s['reused_rounded_source_definition_unchanged'])
  check(s['certificate_sha256']==oldsource['certificate_sha256'] and s['exact_masses'][:28]==oldsource['exact_masses'] and s['column_labels'][:28]==oldsource['column_labels'])
  for key in ['native_block','original_projected_source_Gram']:
   check([row[:28] for row in c.matrix(s[key])[:28]]==c.matrix(oldsource[key]))
  B=[list(map(F,row)) for row in cert['positive_embedding_B']];D=[list(map(F,row)) for row in cert['negative_comparison_embedding_D']];dim=cert['positive_retained_rank'];n=cert['prior_positive_prefix_dimension'];check((dim,n)==[(34,29),(35,33)][idx]);check(rank([a+b for a,b in zip(B,D)])==36)
  for i in range(36):
   for j in range(n):check(B[i][j]==F(i==j))
  phys=[list(map(F,col)) for col in cert['exact_physical_columns']];ids=cert['physical_indices'];check(len(phys)==dim and all(len(x)==len(ids) for x in phys));check(rank([[x[j] for j,i in enumerate(ids) if i<112] for x in phys])==dim)
  masses=[sum(x*x for x in col) for col in phys];check(masses==list(map(F,cert['exact_physical_masses_squared'])))
  H=r.sub(r.scale(Q,K),G);HB=compress(H,B);d,pc=proof.proof(HB)
  BG=compress(G,B);trace=sum(BG[i][i][1] for i in range(dim));check(trace>0);gap=min((d/K)/(4*(sum(masses)+trace/K**2)),K/2);check(gap>F(1,10**38))
  target,th,_=read(f'notes/data/RPB108_DNE42_{up}_UNIFORM_FLOOR_TARGET_20261010.json');ta=next(x for x in targetaudit['rows'] if x['parity']==p);check(th==ta['certificate_sha256']);check(target['input_sha256']==ta['input_sha256']==[inputs[0][1],inputs[1][1],sah,ah])
  z=list(map(F,target['exact_trial']));q=c.quad(Q,z);g=c.quad(G,z);check(q[0]>0);ratio=g[0]/q[1];check(ratio>K);budget=c.sub(c.mul(c.iv(K),q),g);check(budget[1]<0)
  rows.append(dict(parity=p,positive_retained_rank=dim,prior_CC103_span_contained=True,DNE41_certificate_sha256=ch,source_replay_sha256=inputs[0][1],fresh_positive_comparison_certificate=pc,physical_column_mass_sum=str(sum(masses)),compressed_source_trace_upper=str(trace),all_high_physical_gap_lower=str(gap),full_packet_uniform_trial_ratio_lower=str(ratio),full_packet_uniform_trial_budget=c.pair(budget),full_packet_uniform_criterion_rejected=True,DNE42_target_upper=target['critical_uniform_floor_upper']))
  print(p,'integrated rank',dim,'physical gap',float(gap),'full-packet trial threshold',float(ratio),flush=True)
 return dict(milestone='CC108',parent='ed28f6d022338b718774625519f090c7119bacda',read_only_DNE='b6b5cbe5a9f59dbf9f03ae931083289dbf11bf13',original_high_floor=str(K),exact_rational_checks=checks,parity_checks=rows,DNE41_validation_sha256=ah,DNE40_source_validation_sha256=sah,DNE42_validation_sha256=tah,CC106_high_floor_validation_sha256=fh,integrated_retained_rank=69,uncovered_retained_dimension=43,all_high_physical_gap_guard=str(F(1,10**38)),earlier_CC103_guard_preserved_on_earlier_span=True,source_integrals_recomputed=False,physical_materialization_validation_inherited=True,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();Path(a.output).write_text(json.dumps(run(),indent=2)+'\n')
