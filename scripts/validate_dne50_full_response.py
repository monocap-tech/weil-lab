#!/usr/bin/env python3
"""Independent exact mixed response, full budget and physical aperture audit."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json
from certify_dne39_signed_comparison import read
from validate_dne34_source_block import boxes,mm,add,mul,neg,sum_box

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
  UI=[[(x,x) for x in r] for r in U];Q=mm(list(map(list,zip(*UI))),mm(O,UI));S=boxes(pc['congruence_matrix']);ds=[]
  for i in range(n):
   for j in range(n):enclose(S[i][j],Q[i][j])
   d=S[i][i][0]-sum(max(abs(a),abs(b)) for j,(a,b) in enumerate(S[i]) if j!=i);check(d==F(pc['Gershgorin_margins'][i]) and d>0);ds.append(d)
  floor=min(ds)/sum(x*x for r in U for x in r);check(floor==F(pc['coefficient_floor_lower']) and floor>0);return floor
 c,ch=read(path);check(c['stage']=='DNE50' and c['parent']=='bb68642b1384d50d6b9fea517db9691e924fe5a5');inp=[read(p) for p in c['input_paths']];check([h for x,h in inp]==c['input_sha256']);sv,g,gv,hv,old,rv=[x for x,h in inp];check(sv['status']==gv['status']==hv['status']==rv['status']=='PASS');check(gv['certificate_sha256']==inp[1][1] and rv['certificate_sha256']==inp[4][1]);check(rv['actual_certified_retained_dimension']==88 and rv['uncovered_retained_dimension']==24);k=F(c['original_high_floor']);check(k==F(hv['original_infinite_F112_floor'])==F(647,1000));hc,hch=read(hv['certificate_path']);check(hch==hv['certificate_sha256'] and hc['certified_original_F112_lower']=='647/1000');rows=[]
 for z in c['rows']:
  par=z['parity'];s,sh=read(z['source_path']);v=next(v for v in sv['rows'] if v['parity']==par);gr=next(r for r in g['rows'] if r['parity']==par);check(sh==z['source_sha256']==v['replay_sha256']);check(v['complete_remaining_source_Gram_certified']);mapn=s['native_to_source'];check(z['native_to_source']==gr['native_to_source']==mapn and len(mapn)==56);check(next(r for r in gv['rows'] if r['parity']==par)['retained_chart_rank']==56);N=boxes(z['original_native_matrix']);G=boxes(z['projected_native_source_Gram']);S=boxes(s['original_projected_source_Gram']);check(len(N)==len(G)==56 and all(len(r)==56 for r in N+G));check(s['native_block']==gr['native_matrix'])
  for i in range(56):
   for j in range(56):enclose(N[i][j],tuple(map(F,s['native_block'][i][j])));enclose(G[i][j],S[mapn[i]][mapn[j]])
  base=[[add(mul((k,k),n),neg(gg)) for n,gg in zip(nr,gg)] for nr,gg in zip(N,G)]
  check(z['trial_response_used']==(par=='even'))
  if par=='even':
   ys=s['trial_source_indices'];check(ys==[44,45,46]);B=[[S[i][j] for j in ys] for i in mapn];D=[[S[i][j] for j in ys] for i in ys];M=boxes(z['original_native_M']);A=boxes(z['original_native_A']);check(len(M)==56 and all(len(r)==3 for r in M));check(z['original_native_A']==old['original_native_A']);E=boxes(z['residual_E']);W=boxes(z['residual_W']);check(len(E)==56 and all(len(r)==3 for r in E) and len(W)==3 and all(len(r)==3 for r in W))
   for i in range(56):
    for j in range(3):enclose(M[i][j],tuple(map(F,gr['paid_full_trial_native_M'][i][j])));enclose(E[i][j],add(B[i][j],neg(mul((k,k),M[i][j]))))
   for i in range(3):
    for j in range(3):enclose(W[i][j],add(D[i][j],neg(mul((k,k),A[i][j]))))
   positive(z['residual_W_positive_certificate'],W);J=[list(map(F,r)) for r in z['exact_trial_coefficients_J']];check(len(J)==3 and all(len(r)==56 for r in J));JI=[[(x,x) for x in r] for r in J];EJ=mm(E,JI);JWJ=mm(list(map(list,zip(*JI))),mm(W,JI));C=boxes(z['response_credit_numerator']);check(len(C)==56 and all(len(r)==56 for r in C))
   for i in range(56):
    for j in range(56):enclose(C[i][j],add(add(EJ[i][j],EJ[j][i]),neg(JWJ[i][j])));base[i][j]=add(base[i][j],C[i][j])
  H=boxes(z['paid_response_budget']);check(len(H)==56 and all(len(r)==56 for r in H))
  for i in range(56):
   for j in range(56):enclose(H[i][j],base[i][j])
  passed=z['full_response_budget_passed'];check(isinstance(passed,bool));gap=None
  if passed:
   d=positive(z['full_response_positive_certificate'],H);mass=sum(F(s['exact_masses'][i]) for i in mapn);trace=sum(G[i][i][1] for i in range(56));saved=F(z['projected_source_trace_upper']);check(saved>=trace>0 and F(z['physical_packet_mass'])==mass>0);sf=d/k;gap=min(sf/(4*(mass+saved/k**2)),k/2);check(sf==F(z['Schur_coefficient_floor']) and gap==F(z['all_high_physical_gap_lower'])>0 and z['positive_retained_rank']==56)
  else:
   check(z['full_response_positive_certificate'] is None);v=list(map(F,z['exact_comparison_failure_trial']));check(len(v)==56 and any(v));q=sum_box(mul((a*b,a*b),H[i][j]) for i,a in enumerate(v) for j,b in enumerate(v));saved=tuple(map(F,z['comparison_failure_trial_budget']));enclose(saved,q);check(z['comparison_failure_proved']==(saved[1]<0) and z['positive_retained_rank']==44)
  rows.append(dict(parity=par,full_response_budget_passed=passed,positive_retained_rank=z['positive_retained_rank'],all_high_physical_gap_lower=str(gap) if gap is not None else None))
 check([r['parity'] for r in rows]==['even','odd']);rank=sum(r['positive_retained_rank'] for r in rows);whole=rank==112;check(c['actual_certified_all_high_retained_dimension']==rank and c['uncovered_retained_dimension']==112-rank);check(c['whole_aperture_positive']==whole and c['original_aperture']=='53/50');check(c['response_upper_established'] is True and c['true_high_inverse_evaluated'] is False and c['RH'] is False and c['Lean'] is False)
 gap=min(F(r['all_high_physical_gap_lower']) for r in rows) if whole else None;check(c['all_high_physical_gap_lower']==(str(gap) if gap is not None else None))
 out=dict(stage='DNE50',status='PASS',exact_rational_checks=checks,certificate_path=path,certificate_sha256=ch,input_sha256=c['input_sha256'],rows=rows,actual_certified_all_high_retained_dimension=rank,uncovered_retained_dimension=112-rank,original_aperture='53/50',original_infinite_F112_floor=str(k),all_high_physical_gap_lower=str(gap) if gap is not None else None,response_upper_established=True,true_high_inverse_evaluated=False,whole_aperture_positive=whole,RH=False,Lean=False);Path(output).write_text(json.dumps(out,indent=2)+'\n');print('PASS',checks,'full response checks; retained',rank,'whole aperture',whole,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('--output',required=True);a=p.parse_args();run(a.input,a.output)
