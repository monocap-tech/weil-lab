#!/usr/bin/env python3
"""Independent rational embedding, inertia, retained rank and physical-gap audit."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json
from certify_dne39_signed_comparison import read
from materialize_dne44_joint_sources import run as materialize
from validate_dne34_source_block import add,mul,neg,boxes,mm

def run(paths,output):
 checks=0;rows=[]
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def enclose(x,y):check(x[0]<=y[0]<=y[1]<=x[1])
 def compress(M,B):
  BI=[[(x,x) for x in row] for row in B];return mm([list(x) for x in zip(*BI)],mm(M,BI))
 def positive(c,expected):
  O=boxes(c['original_matrix']);U=[[F(x) for x in row] for row in c['exact_congruence_U']];n=len(expected);check(len(U)==n)
  for i in range(n):
   check(U[i][i]!=0)
   for j in range(n):check(i<=j or U[i][j]==0);enclose(O[i][j],expected[i][j])
  C=compress(O,U);S=boxes(c['congruence_matrix']);m=[]
  for i in range(n):
   for j in range(n):enclose(S[i][j],C[i][j])
   margin=S[i][i][0]-sum(max(abs(x),abs(y)) for j,(x,y) in enumerate(S[i]) if i!=j);check(margin==F(c['Gershgorin_margins'][i]) and margin>0);m.append(margin)
  d=min(m)/sum(x*x for row in U for x in row);check(d==F(c['coefficient_floor_lower']) and d>0);return d
 def rank(M):
  M=[list(row) for row in M];r=0
  for i in range(len(M[0])):
   pivot=next((j for j in range(r,len(M)) if M[j][i]),None)
   if pivot is None:continue
   M[r],M[pivot]=M[pivot],M[r];check(M[r][i]!=0)
   for j in range(r+1,len(M)):
    if M[j][i]:
     a=M[j][i]/M[r][i];M[j]=[x-a*y for x,y in zip(M[j],M[r])]
   r+=1
   if r==len(M):break
  return r
 for path in paths:
  c,ch=read(path);check(c['stage']=='DNE44' and c['parent']=='5ec8aeeb73fa67eff670e0716a1a752f5d3e64b3');inputs=[read(p) for p in c['input_paths']];check([h for _,h in inputs]==c['input_sha256']);s,prior,v=[x for x,_ in inputs];check(v['status']==prior['status']=='PASS');check(prior['original_infinite_F112_floor']=='603/1000');check(prior['input_sha256'][0]==v['high_floor_validation_sha256']);audit=next(r for r in v['rows'] if r['parity']==c['parity']);check(audit['replay_sha256']==inputs[0][1] and audit['packet_sha256']==s['normalized_packet_sha256']);check(s['parity']==c['parity']);k=F(c['original_high_floor']);check(k==F(603,1000)==F(prior['original_infinite_F112_floor']));Q=boxes(s['native_block']);G=boxes(s['original_projected_source_Gram']);H=[[add(mul((k,k),q),neg(g)) for q,g in zip(qr,gr)] for qr,gr in zip(Q,G)]
  B=[list(map(F,row)) for row in c['positive_embedding_B']];D=[list(map(F,row)) for row in c['negative_comparison_embedding_D']];n=c['prior_positive_prefix_dimension'];r=c['positive_retained_rank'];z=c['negative_comparison_rank'];check(n==36 and next(row for row in prior['rows'] if row['parity']==c['parity'])['positive_retained_rank']==36);check(len(B)==len(D)==44 and all(len(x)==r for x in B) and all(len(x)==z for x in D));check(r+z==44)
  for i in range(44):
   for j in range(n):check(B[i][j]==F(i==j))
  check(rank([a+b for a,b in zip(B,D)])==44);positive(c['joint_native_positive_control'],Q);HB=compress(H,B);d=positive(c['positive_comparison_certificate'],HB);
  if z:HD=compress(H,D);positive(c['negative_comparison_certificate'],[[neg(x) for x in row] for row in HD])
  else:check(c['negative_comparison_certificate'] is None)
  check(c['uniform_comparison_inertia']==[r,z,0]);check(c['prior_positive_span_contained'])
  pp=output+'.packet';materialize(s['certificate_path'],pp);packet,ph=read(pp);Path(pp).unlink();check(ph==s['normalized_packet_sha256']);cols=packet['columns'];raw=[dict(zip(x['indices'],map(F,x['coefficients']))) for x in cols];low=int(c['parity']=='odd');check(rank([[row.get(i,F(0)) for i in range(low,112,2)] for row in raw])==44);ids=sorted({i for x in raw for i in x});check(c['physical_indices']==ids);mass=[]
  for j in range(r):
   phys=[sum(raw[t].get(i,F(0))*B[t][j] for t in range(44)) for i in ids];check(phys==list(map(F,c['exact_physical_columns'][j])));m=sum(x*x for x in phys);check(m==F(c['exact_physical_masses_squared'][j]) and m>0);mass.append(m)
  BG=compress(G,B);trace=sum(BG[i][i][1] for i in range(r));saved_trace=F(c['projected_source_trace_upper']);check(saved_trace>=trace and trace>0);trace=saved_trace;sf=d/k;gap=min(sf/(4*(sum(mass)+trace/k**2)),k/2);check(sf==F(c['Schur_coefficient_floor']));check(gap==F(c['all_high_physical_gap_lower']) and gap>0)
  for key in ('prior_source_Gram_entries_reintegrated','true_high_inverse_evaluated','whole_aperture_positive','RH','Lean'):check(c[key] is False)
  check(c['new_source_integrals_computed'] is True)
  rows.append(dict(parity=c['parity'],certificate_sha256=ch,input_sha256=c['input_sha256'],positive_retained_rank=r,negative_uniform_comparison_rank=z,prior_positive_prefix_dimension=n,prior_positive_span_contained=True,uniform_comparison_positive_dimension_maximal=True,Schur_coefficient_floor=str(sf),all_high_physical_gap_lower=str(gap)))
 total=sum(r['positive_retained_rank'] for r in rows);minimum=min(F(r['all_high_physical_gap_lower']) for r in rows);guard=F(1,10**100)
 while guard*10<minimum:guard*=10
 check(0<guard<minimum)
 out=dict(stage='DNE44',status='PASS',exact_rational_checks=checks,rows=rows,all_high_positive_retained_dimension=total,uncovered_retained_dimension=112-total,all_high_physical_gap_guard=str(guard),new_source_integrals_computed=True,prior_source_Gram_entries_reintegrated=False,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('PASS',checks,'checks; retained rank',total,'guard',str(guard))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('inputs',nargs=2);p.add_argument('--output',required=True);a=p.parse_args();run(a.inputs,a.output)
