#!/usr/bin/env python3
"""Independent scalar reuse bridge, odd congruence, and convex-route audit."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json
from validate_dne51_response_extension import read,boxes,add,sub,mul,total,mm,tr,quadratic

def run(path,output):
 checks=0
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def enclose(a,b):check(F(a[0])<=b[0]<=b[1]<=F(a[1]))
 def proof(pc,M):
  O=boxes(pc['original_matrix']);U=[list(map(F,row)) for row in pc['exact_congruence_U']];n=len(M);check(len(U)==len(O)==n)
  for i in range(n):
   for j in range(n):enclose(O[i][j],M[i][j]);check(i<=j or U[i][j]==0)
  UI=[[(x,x) for x in row] for row in U];Q=mm(tr(UI),mm(O,UI));m=[]
  for i in range(n):
   for j in range(n):enclose(pc['congruence_matrix'][i][j],Q[i][j])
   row=boxes(pc['congruence_matrix'])[i];d=row[i][0]-sum(max(abs(a),abs(b)) for j,(a,b) in enumerate(row) if i!=j);check(d==F(pc['Gershgorin_margins'][i])>0);m.append(d)
  f=min(m)/sum(x*x for row in U for x in row);check(f==F(pc['coefficient_floor_lower']));return f
 c,ch=read(path);check(c['stage']=='DNE52' and c['parent']=='3e022ead0c400a5098946dc57da789592183bd5e');inp=[read(p) for p in c['input_paths']];check(c['input_sha256']==[h for x,h in inp]);g,gv,p,t,tv,nf,physical,dne,old,previous,pv=[x for x,h in inp];check(gv['status']==tv['status']==pv['status']=='PASS');check(gv['gate_decoded_sha256']==inp[0][1] and gv['positive_packet_sha256']==inp[2][1]);check(tv['certificate_decoded_sha256']==inp[3][1] and pv['certificate_sha256']==inp[9][1]);check(p['DNE50_positive_subspaces_decoded_sha256']==inp[8][1] and p['DNE50_full_response_decoded_sha256']==inp[7][1]);K=F(c['actual_high_floor']);check(K==F(647,1000));z=t['parity_checks'][0];x=z['exact_transport'];check(z['NF52_high_decoded_sha256']==inp[5][1] and x['CC105_high_packet_sha256']==inp[6][1]);check(c['reused_source_native_map']==z['source_native_map']==dne['rows'][0]['native_to_source'])
 for j,n in [(2,112),(3,114)]:
  col=physical['columns'][1+j];check(col['indices']==[n] and col['coefficients']==['1'] and col['exact_mass_squared']=='1')
 C=[list(map(F,row)) for row in x['Native_trial_transport_C']];D=[list(map(F,row)) for row in x['paid_high_transport_D']];tt=list(map(F,x['missing_high_transport_row_t']));BN=boxes(nf['enlarged_joint_high_native_crosses']);QY=boxes(nf['enlarged_high_native_Gram']);GY=boxes(nf['enlarged_high_complete_source_Gram']);qv=[tuple(map(F,a)) for a in x['recovered_native_residual_high_row']];W=boxes(z['complete_signed_response_rows']);check(len(C)==56 and len(D)==11 and len(tt)==56)
 for i in range(56):
  for u,j in enumerate((2,3)):
   q=total([mul((C[a][i],)*2,BN[a][j]) for a in range(56)]+[mul((D[a][i],)*2,QY[a][j]) for a in range(11)]+[mul((tt[i],)*2,qv[j])]);enclose(c['reused_native_pairings_Z_to_e112_e114'][i][u],q);ss=add(W[i][j],mul((K,K),q));enclose(c['reused_projected_source_pairings_Z_to_e112_e114'][i][u],ss)
 for i,a in enumerate((2,3)):
  for j,b in enumerate((2,3)):enclose(c['reused_native_self_Gram'][i][j],QY[a][b]);enclose(c['reused_projected_source_self_Gram'][i][j],GY[a][b])
 # New even manifest is the exact complement of 112 transported native
 # pairs and three high self/mutual pairs in DNE51's 183-pair manifest.
 manifest=next(x['new_source_upper_triangle'] for x in previous['proposed_source_extensions'] if x['parity']=='even');mapping=c['reused_source_native_map'];reused={(i,j) for j in (59,60) for i in mapping}|{(59,59),(59,60),(60,60)};missing={tuple(v) for v in c['new_even_source_upper_triangle']};check(len(reused)==115 and len(missing)==68 and not reused&missing and reused|missing==set(map(tuple,manifest)));check(c['reused_source_correlation_count']==115 and c['new_even_source_correlation_count']==68 and c['odd_new_source_correlations_required']==0)
 # Recheck the complete original odd response sign with a separate
 # unrounded rational congruence, without the CC proof implementation.
 odd=g['parity_checks'][1];P=boxes(odd['paid_response_comparison']);op=p['parity_checks'][1];U=[list(map(F,row)) for row in op['positive_proof']['frozen_rational_congruence']];check(len(U)==56 and all(len(row)==56 for row in U));UI=[[(a,a) for a in row] for row in U];R=mm(tr(UI),mm(P,UI));margins=[]
 for i in range(56):
  for j in range(56):check(P[i][j]==P[j][i])
  d=R[i][i][0]-sum(max(abs(a),abs(b)) for j,(a,b) in enumerate(R[i]) if j!=i);check(d>0);margins.append(d)
 floor=min(margins)/sum(a*a for row in U for a in row);check(floor>=F(op['coefficient_floor']));mass=F(op['physical_packet_mass_upper']);trace=F(op['projected_source_trace_upper']);gap=min(floor/(4*(mass+trace/K**2)),K/2);guard=F(c['physical_guard']);check(gap>guard==F(1,10**39));check(op['positive_embedding_B']==[[str(F(i==j)) for j in range(56)] for i in range(56)])
 for i in range(56):
  for j in range(54):check(sum(F(op['positive_embedding_B'][i][k])*F(old['rows'][1]['positive_embedding_B'][k][j]) for k in range(56))==F(old['rows'][1]['positive_embedding_B'][i][j]))
 check(p['parity_checks'][0]['positive_embedding_B']==old['rows'][0]['positive_embedding_B']);check(p['integrated_positive_retained_rank']==c['integrated_positive_retained_rank']==111 and c['uncovered_retained_dimension']==1 and c['DNE50_109_span_preserved'] and c['even_old_response_certificate_preserved'])
 f=c['common_even_failure'];v=list(map(F,f['exact_trial']));check(len(v)==56 and any(v));DD=[[mul(a,(1/K,1/K)) for a in row] for row in boxes(dne['rows'][0]['paid_response_budget'])];dq=quadratic(DD,v);enclose(f['DNE_trial_budget'],dq);check(dq[1]<0);N=[[sub(mul(a,(1/K,1/K)),b) for a,b in zip(gr,qr)] for gr,qr in zip(GY,QY)];mu=proof(f['CC_denominator_positive_certificate'],N);e=[total(mul((v[i],)*2,W[i][j]) for i in range(56)) for j in range(11)];y=list(map(F,f['CC_inverse_trial']));check(len(y)==11);res=[sub(ee,total(mul(nn,(a,a)) for nn,a in zip(row,y))) for ee,row in zip(e,N)];r2=sum(max(abs(a),abs(b))**2 for a,b in res);check(F(f['CC_residual_squared_upper'])>=r2);credit=add(sub(mul(total(mul((a,a),ee) for a,ee in zip(y,e)),(F(2),F(2))),quadratic(N,y)),(F(0),F(f['CC_residual_squared_upper'])/mu));cq=add(quadratic(boxes(g['parity_checks'][0]['paid_plain_comparison']),v),mul(credit,(1/K**2,1/K**2)));check(cq[1]<0 and F(f['CC_optimal_budget_upper'][1])>=cq[1] and f['every_convex_average_with_any_CC_coefficients_fails'])
 for k in ('new_even_positivity_established','whole_aperture_positive','RH','F4','Lean'):check(c[k] is False)
 check(c['new_source_integrations']==0 and c['odd_complete_response_inherited'])
 out=dict(stage='DNE52',status='PASS',exact_rational_checks=checks,certificate_path=path,certificate_sha256=ch,input_sha256=c['input_sha256'],integrated_positive_retained_rank=111,uncovered_retained_dimension=1,physical_guard=str(guard),fresh_full_odd_congruence_rechecked=True,even_source_pairs_reused=115,new_even_source_correlations_required=68,odd_new_source_correlations_required=0,common_even_DNE_budget_upper=str(F((dq[1]*10**80).__ceil__(),10**80)),common_even_optimal_CC_budget_upper=str(F((cq[1]*10**80).__ceil__(),10**80)),new_even_positivity_established=False,whole_aperture_positive=False,RH=False,F4=False,Lean=False);Path(output).write_text(json.dumps(out,indent=2)+'\n');print('DNE52 PASS',checks,'exact checks; rank111; 68 source pairs remain',flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('--output',required=True);a=p.parse_args();run(a.input,a.output)
