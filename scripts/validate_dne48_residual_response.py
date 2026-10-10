#!/usr/bin/env python3
"""Independent exact native-pairing, mixed-response and positivity audit."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json
from certify_dne39_signed_comparison import read
from materialize_dne48_trial_sources import run as materialize
from validate_dne34_source_block import add,mul,neg,boxes,mm,sum_box

def run(path,output):
 checks=0
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def enclose(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
 def positive(c,M):
  O=boxes(c['original_matrix']);U=[list(map(F,row)) for row in c['exact_congruence_U']];n=len(M);check(len(O)==len(U)==n and all(len(row)==n for row in O+U))
  for i in range(n):
   check(U[i][i]!=0)
   for j in range(n):check(i<=j or U[i][j]==0);enclose(O[i][j],M[i][j])
  UI=[[(x,x) for x in row] for row in U];K=mm([list(x) for x in zip(*UI)],mm(O,UI));S=boxes(c['congruence_matrix']);m=[]
  for i in range(n):
   for j in range(n):enclose(S[i][j],K[i][j])
   d=S[i][i][0]-sum(max(abs(x),abs(y)) for j,(x,y) in enumerate(S[i]) if i!=j);check(d==F(c['Gershgorin_margins'][i]) and d>0);m.append(d)
  d=min(m)/sum(x*x for row in U for x in row);check(d==F(c['coefficient_floor_lower']) and d>0);return d
 c,ch=read(path);check(c['stage']=='DNE48' and c['parent']=='da5b09e3b72b8e05e3daab5e37e6b3398a5558f8' and c['parity']=='even');inputs=[read(p) for p in c['input_paths']];check([h for _,h in inputs]==c['input_sha256']);s,sv,h,prior,pv=[x for x,_ in inputs];check(sv['status']==h['status']==pv['status']=='PASS');check(sv['replay_sha256']==inputs[0][1]);pr=next(r for r in pv['rows'] if r['parity']=='even');check(pr['certificate_sha256']==inputs[3][1] and prior['positive_retained_rank']==43);hc,hch=read(h['certificate_path']);check(hch==h['certificate_sha256']);check(hc['certified_original_F112_lower']==h['original_infinite_F112_floor']==c['original_high_floor']=='647/1000');k=F(c['original_high_floor'])
 pp=output+'.packet';materialize(s['certificate_path'],pp);packet,ph=read(pp);Path(pp).unlink();check(ph==c['packet_sha256']==s['normalized_packet_sha256']==sv['packet_sha256']);cols=packet['columns'];check(len(cols)==47);ids=s['trial_action_coordinate_indices'];tc=boxes(s['trial_rounded_action_coordinates']);errors=list(map(F,s['source_L2_error_upper']));P=boxes(c['trial_native_pairings']);check(len(P)==3 and all(len(row)==47 for row in P));exact=[]
 for j in range(3):
  coords=dict(zip(ids,tc[j]));row=[]
  for i,col in enumerate(cols):
   value=sum_box(mul((F(x),F(x)),coords[n]) for n,x in zip(col['indices'],col['coefficients']));pay=errors[44+j]*F(col['norm_upper']);value=(value[0]-pay,value[1]+pay);check(value==P[j][i]);row.append(value)
  exact.append(row)
 M=boxes(c['original_native_M']);A=boxes(c['original_native_A']);check(len(M)==44 and all(len(row)==3 for row in M));check(len(A)==3 and all(len(row)==3 for row in A))
 for i in range(44):
  for j in range(3):enclose(M[i][j],P[j][i])
 for i in range(3):
  for j in range(3):
   intersection=(max(P[i][44+j][0],P[j][44+i][0]),min(P[i][44+j][1],P[j][44+i][1]));check(intersection[0]<=intersection[1]);enclose(A[i][j],intersection)
 S=boxes(s['original_projected_source_Gram']);G=[row[:44] for row in S[:44]];B=[row[44:] for row in S[:44]];D=[row[44:] for row in S[44:]];N=boxes(s['native_block']);check(len(N)==44 and all(len(row)==44 for row in N));E=boxes(c['residual_E']);W=boxes(c['residual_W'])
 for i in range(44):
  for j in range(3):enclose(E[i][j],add(B[i][j],neg(mul((k,k),M[i][j]))))
 for i in range(3):
  for j in range(3):enclose(W[i][j],add(D[i][j],neg(mul((k,k),A[i][j]))))
 positive(c['residual_W_positive_certificate'],W);J=[list(map(F,row)) for row in c['exact_trial_coefficients_J']];check(len(J)==3 and all(len(row)==44 for row in J));JI=[[(x,x) for x in row] for row in J];JT=list(map(list,zip(*JI)));EJ=mm(E,JI);JWJ=mm(JT,mm(W,JI));C=boxes(c['response_credit_numerator']);H=boxes(c['paid_response_budget']);check(len(C)==len(H)==44 and all(len(row)==44 for row in C+H))
 for i in range(44):
  for j in range(44):
   enclose(C[i][j],add(add(EJ[i][j],EJ[j][i]),neg(JWJ[i][j])));expected=add(add(mul((k,k),N[i][j]),neg(G[i][j])),C[i][j]);enclose(H[i][j],expected)
 passed=c['full_response_budget_passed'];check(isinstance(passed,bool));gap=None
 if passed:
  d=positive(c['full_response_positive_certificate'],H);mass=sum(map(F,s['exact_masses'][:44]));trace=sum(G[i][i][1] for i in range(44));saved=F(c['projected_source_trace_upper']);check(saved>=trace>0 and mass==F(c['physical_packet_mass'])>0);sf=d/k;gap=min(sf/(4*(mass+saved/k**2)),k/2);check(sf==F(c['Schur_coefficient_floor']) and gap==F(c['all_high_physical_gap_lower'])>0);check(c['positive_retained_rank']==44 and c['actual_certified_retained_dimension']==88 and c['uncovered_retained_dimension']==24 and c['prior_87_direction_span_contained'] is True)
  # Retained rank follows from the authenticated DNE46 invertible [B,D] chart.
  check(prior['uniform_comparison_inertia']==[43,1,0] and pr['uniform_comparison_positive_dimension_maximal']);check(next(r for r in pv['rows'] if r['parity']=='odd')['positive_retained_rank']==44)
 else:
  check(c['full_response_positive_certificate'] is None);v=list(map(F,c['exact_response_failure_trial']));check(len(v)==44 and any(v));budget=sum_box(mul((x*y,x*y),H[i][j]) for i,x in enumerate(v) for j,y in enumerate(v));saved=tuple(map(F,c['response_failure_trial_budget']));enclose(saved,budget);check(c['response_budget_failure_proved']==(saved[1]<0));check(c['positive_retained_rank']==43 and c['actual_certified_retained_dimension']==87 and c['uncovered_retained_dimension']==25)
 check(c['new_source_integrals_computed'] and c['response_upper_established'])
 for key in ('prior_source_entries_reintegrated','true_high_inverse_evaluated','whole_aperture_positive','RH','Lean'):check(c[key] is False)
 out=dict(stage='DNE48',status='PASS',exact_rational_checks=checks,certificate_path=path,certificate_sha256=ch,input_sha256=c['input_sha256'],original_infinite_F112_floor=str(k),response_upper_established=True,full_even_response_budget_passed=passed,positive_even_retained_rank=c['positive_retained_rank'],actual_certified_retained_dimension=c['actual_certified_retained_dimension'],uncovered_retained_dimension=c['uncovered_retained_dimension'],all_high_physical_gap_lower=str(gap) if gap is not None else None,source_integrals_recomputed=True,prior_source_entries_reintegrated=False,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('PASS',checks,'response checks; full even',passed,'retained',c['actual_certified_retained_dimension'],flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('--output',required=True);a=ap.parse_args();run(a.input,a.output)
