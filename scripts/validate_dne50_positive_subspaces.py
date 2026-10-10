#!/usr/bin/env python3
"""Independent paid inertia, retained chart, old-span and physical gap audit."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json
from certify_dne39_signed_comparison import read
from validate_dne34_source_block import boxes,mm,mul,neg

def run(path,output):
 checks=0
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def enclose(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
 def positive(pc,M):
  O=boxes(pc['original_matrix']);U=[list(map(F,r)) for r in pc['exact_congruence_U']];n=len(M);check(len(O)==len(U)==n and all(len(r)==n for r in O+U))
  for i in range(n):
   check(U[i][i]!=0)
   for j in range(n):check(i<=j or U[i][j]==0);enclose(O[i][j],M[i][j])
  UI=[[(x,x) for x in r] for r in U];K=mm(list(map(list,zip(*UI))),mm(O,UI));S=boxes(pc['congruence_matrix']);m=[]
  for i in range(n):
   for j in range(n):enclose(S[i][j],K[i][j])
   d=S[i][i][0]-sum(max(abs(a),abs(b)) for j,(a,b) in enumerate(S[i]) if i!=j);check(d==F(pc['Gershgorin_margins'][i]) and d>0);m.append(d)
  floor=min(m)/sum(x*x for r in U for x in r);check(floor==F(pc['coefficient_floor_lower']) and floor>0);return floor
 def compress(H,B):
  BI=[[(x,x) for x in r] for r in B];return mm(list(map(list,zip(*BI))),mm(H,BI))
 c,ch=read(path);check(c['stage']=='DNE50' and c['parent']=='bb68642b1384d50d6b9fea517db9691e924fe5a5');inp=[read(p) for p in c['input_paths']];check([h for x,h in inp]==c['input_sha256']);r,v=[x for x,h in inp];check(v['status']=='PASS' and v['certificate_sha256']==inp[0][1]);k=F(c['original_high_floor']);check(k==F(r['original_high_floor'])==F(647,1000));rows=[]
 for z in c['rows']:
  rr=next(x for x in r['rows'] if x['parity']==z['parity']);H=boxes(rr['paid_response_budget']);B=[list(map(F,row)) for row in z['positive_embedding_B']];D=[list(map(F,row)) for row in z['negative_comparison_embedding_D']];rank=z['positive_retained_rank'];nr=56-rank;check(44<=rank<=56 and len(B)==len(D)==56 and all(len(x)==rank for x in B) and all(len(x)==nr for x in D))
  for i in range(56):
   for j in range(44):check(B[i][j]==F(i==j))
  W=[list(map(F,row)) for row in z['bottom_full_chart']];check(len(W)==12 and all(len(row)==12 for row in W))
  for i in range(12):check(W[i]==B[44+i][44:]+D[44+i])
  Gram=[[(sum(W[t][i]*W[t][j] for t in range(12)),)*2 for j in range(12)] for i in range(12)];positive(z['bottom_chart_Gram_positive_certificate'],Gram);d=positive(z['positive_comparison_certificate'],compress(H,B))
  if nr:positive(z['negative_comparison_certificate'],[[neg(x) for x in row] for row in compress(H,D)])
  else:check(z['negative_comparison_certificate'] is None)
  check(z['comparison_inertia']==[rank,nr,0] and z['prior_44_direction_span_contained'])
  source,sh=read(rr['source_path']);check(sh==rr['source_sha256']);mapn=rr['native_to_source'];mass=sum(F(source['exact_masses'][i]) for i in mapn);G=boxes(rr['projected_native_source_Gram']);trace=sum(G[i][i][1] for i in range(56));bf=sum(x*x for row in B for x in row);check(F(z['embedding_Frobenius_squared'])==bf>0);check(F(z['original_packet_physical_mass'])==mass>0 and F(z['original_projected_source_trace_upper'])>=trace>0);saved=F(z['original_projected_source_trace_upper']);mu=mass*bf;tu=saved*bf;check(F(z['physical_packet_mass_upper'])==mu and F(z['projected_source_trace_upper'])==tu);sf=d/k;gap=min(sf/(4*(mu+tu/k**2)),k/2);check(F(z['Schur_coefficient_floor'])==sf and F(z['all_high_physical_gap_lower'])==gap>0);rows.append(dict(parity=z['parity'],positive_retained_rank=rank,comparison_inertia=[rank,nr,0],all_high_physical_gap_lower=str(gap),prior_44_direction_span_contained=True))
 check([x['parity'] for x in rows]==['even','odd']);rank=sum(x['positive_retained_rank'] for x in rows);check(c['actual_certified_all_high_retained_dimension']==rank and c['uncovered_retained_dimension']==112-rank and c['prior_88_direction_span_contained']);check(c['whole_aperture_positive']==(rank==112) and c['true_high_inverse_evaluated'] is False and c['RH'] is False and c['Lean'] is False)
 gap=min(F(x['all_high_physical_gap_lower']) for x in rows);out=dict(stage='DNE50',status='PASS',exact_rational_checks=checks,certificate_path=path,certificate_sha256=ch,input_sha256=c['input_sha256'],rows=rows,actual_certified_all_high_retained_dimension=rank,uncovered_retained_dimension=112-rank,prior_88_direction_span_contained=True,original_high_floor=str(k),all_high_physical_gap_lower=str(gap),whole_aperture_positive=rank==112,true_high_inverse_evaluated=False,RH=False,Lean=False);Path(output).write_text(json.dumps(out,indent=2)+'\n');print('PASS',checks,'positive-subspace checks; retained',rank,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('--output',required=True);a=p.parse_args();run(a.input,a.output)
