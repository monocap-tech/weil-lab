#!/usr/bin/env python3
"""Independent unrounded rational six-trial response and physical-gap audit."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json
from validate_dne51_response_extension import read,add,sub,mul,total,boxes,mm,tr,quadratic,div

def run(path,output):
 checks=0
 def ck(v):
  nonlocal checks
  assert v;checks+=1
 def enclose(a,b):ck(F(a[0])<=b[0]<=b[1]<=F(a[1]))
 def positive(pc,M):
  O=boxes(pc['original_matrix']);U=[list(map(F,row)) for row in pc['exact_congruence_U']];n=len(M);ck(len(O)==len(U)==n and all(len(r)==n for r in O+U));
  for i in range(n):
   ck(U[i][i]!=0)
   for j in range(n):ck(i<=j or U[i][j]==0);enclose(O[i][j],M[i][j])
  UI=[[(x,x) for x in row] for row in U];K=mm(tr(UI),mm(O,UI));T=boxes(pc['congruence_matrix']);margins=[]
  for i in range(n):
   for j in range(n):enclose(T[i][j],K[i][j])
   d=T[i][i][0]-sum(max(abs(a),abs(b)) for j,(a,b) in enumerate(T[i]) if j!=i);ck(d==F(pc['Gershgorin_margins'][i]) and d>0);margins.append(d)
  ck(F(pc['coefficient_floor_lower'])==min(margins)/sum(x*x for row in U for x in row))
 c,ch=read(path);ck(c['stage']=='DNE53' and c['parent']=='7d0d03400f78a3bf0d91d01c52a1b6d6a33e4bd4');inp=[read(p) for p in c['input_paths']];ck([h for x,h in inp]==c['input_sha256']);sv,s,r,b,bv,hv,gv=[x for x,h in inp];ck(sv['status']==bv['status']==hv['status']==gv['status']=='PASS');ck(sv['replay_sha256']==inp[1][1] and bv['certificate_sha256']==inp[3][1]);ck(gv['certificate_sha256']==s['input_sha256'][0] and gv['rows'][0]['retained_chart_rank']==56 and gv['rows'][0]['finite_native_positive']);k=F(hv['original_infinite_F112_floor']);ck(k==F(c['original_high_floor'])==F(647,1000));ck(c['trial_dimension']==6 and c['source_dimension']==62);ns=s['native_to_source'];ys=s['trial_source_indices'];ck(c['native_to_source']==ns and c['trial_source_indices']==ys and len(ns)==56 and ys==[44,45,46,59,60,61]);N=boxes(s['native_block']);S=boxes(s['original_projected_source_Gram']);G=[[S[i][j] for j in ns] for i in ns];B=[[S[i][j] for j in ys] for i in ns];D=[[S[i][j] for j in ys] for i in ys];old=r['rows'][0];reuse,rh=read(s['reused_source_path']);ck(rh==s['reused_source_sha256']);errors=list(map(F,s['source_L2_error_upper']));action=boxes(s['new_rounded_action_coordinates']);oldaction=boxes(reuse['trial_rounded_action_coordinates']);at={n:i for i,n in enumerate(s['new_action_coordinate_indices'])}
 def paid(v,e):return v[0]-e,v[1]+e
 def intersection(a,b):
  v=max(a[0],b[0]),min(a[1],b[1]);ck(v[0]<=v[1]);return v
 A=[[(F(0),F(0)) for j in range(6)] for i in range(6)];oldA=boxes(old['original_native_A']);
 for i in range(3):
  for j in range(3):A[i][j]=oldA[i][j]
  for u,n in enumerate((112,114,116)):A[i][3+u]=A[3+u][i]=paid(oldaction[i][at[n]],errors[44+i])
 self2=boxes(b['reused_native_self_Gram'])
 for u in range(3):
  for v in range(u,3):
   z=intersection(paid(action[u][at[112+2*v]],errors[59+u]),paid(action[v][at[112+2*u]],errors[59+v]));
   if u<2 and v<2:intersection(z,self2[u][v]);z=self2[u][v]
   A[3+u][3+v]=A[3+v][3+u]=z
 M=boxes(old['original_native_M']);reuseM=boxes(b['reused_native_pairings_Z_to_e112_e114'])
 for i,src in enumerate(ns):
  col=s['columns'][src];z=total(mul((F(v),F(v)),action[2][at[n]]) for n,v in zip(col['indices'],col['coefficients']));z=paid(z,errors[61]*F(col['norm_upper']));M[i]+=reuseM[i]+[z]
 for name,X in [('original_native_matrix',N),('projected_native_source_Gram',G),('original_native_A',A),('original_native_M',M)]:
  for i,row in enumerate(X):
   for j,v in enumerate(row):enclose(c[name][i][j],v)
 # Rebuild with the certificate's wider paid native boxes; this audits every
 # load-bearing downstream payment without relying on producer arithmetic.
 A=boxes(c['original_native_A']);M=boxes(c['original_native_M']);N=boxes(c['original_native_matrix']);G=boxes(c['projected_native_source_Gram']);E=[[sub(x,mul((k,k),y)) for x,y in zip(br,mr)] for br,mr in zip(B,M)];W=[[sub(x,mul((k,k),y)) for x,y in zip(dr,ar)] for dr,ar in zip(D,A)]
 for name,X in [('residual_E',E),('residual_W',W)]:
  for i,row in enumerate(X):
   for j,v in enumerate(row):enclose(c[name][i][j],v)
 W=boxes(c['residual_W']);E=boxes(c['residual_E']);positive(c['residual_W_positive_certificate'],W);J=[list(map(F,row)) for row in c['exact_trial_coefficients_J']];ck(len(J)==6 and all(len(row)==56 for row in J));JI=[[(x,x) for x in row] for row in J];EJ=mm(E,JI);JWJ=mm(tr(JI),mm(W,JI));H0=[[sub(mul((k,k),N[i][j]),G[i][j]) for j in range(56)] for i in range(56)];H=[[sub(add(add(H0[i][j],EJ[i][j]),EJ[j][i]),JWJ[i][j]) for j in range(56)] for i in range(56)]
 for i in range(56):
  for j in range(56):enclose(c['paid_response_budget'][i][j],H[i][j])
 passed=c['full_even_response_budget_passed'];ck(passed==(c['full_even_response_positive_certificate'] is not None));rank=112 if passed else 111
 if passed:
  pc=c['full_even_response_positive_certificate'];positive(pc,boxes(c['paid_response_budget']));mass=sum(F(s['exact_masses'][i]) for i in ns);trace=sum(v[i][1] for i,v in enumerate(G));sf=F(pc['coefficient_floor_lower'])/k;gap=min(sf/(4*(mass+trace/k**2)),k/2);ck(F(c['physical_packet_mass'])==mass and F(c['projected_source_trace_upper'])==trace and F(c['Schur_coefficient_floor'])==sf);ck(F(c['even_all_high_physical_gap_lower'])==gap>0);ck(F(c['combined_physical_gap_lower'])==min(gap,F(b['physical_guard'])))
 else:
  v=list(map(F,c['exact_comparison_failure_trial']));ck(len(v)==56 and any(v));q=quadratic(boxes(c['paid_response_budget']),v);enclose(c['comparison_failure_trial_budget'],q);ck(q[1]<0 and c['comparison_failure_proved']);ck(F(c['combined_physical_gap_lower'])==F(b['physical_guard']));
  if 'optimal_trial_budget' in c:
   e=[total(mul((v[i],v[i]),E[i][j]) for i in range(56)) for j in range(6)];L=[[(F(i==j),F(i==j)) for j in range(6)] for i in range(6)];ds=[]
   for i in range(6):
    d=sub(W[i][i],total(mul(mul(L[i][j],L[i][j]),ds[j]) for j in range(i)));ck(d[0]>0);enclose(c['LDL_positive_pivots'][i],d);ds.append(d)
    for j in range(i+1,6):L[j][i]=div(sub(W[j][i],total(mul(mul(L[j][t],L[i][t]),ds[t]) for t in range(i))),d)
   u=[]
   for i in range(6):u.append(sub(e[i],total(mul(L[i][j],u[j]) for j in range(i))))
   credit=total(div(mul(x,x),d) for x,d in zip(u,ds));base=quadratic(H0,v);optimal=add(base,credit);enclose(c['base_trial_budget'],base);enclose(c['optimal_credit_trial'],credit);enclose(c['optimal_trial_budget'],optimal);ck(F(c['optimal_trial_budget'][1])>=optimal[1]);
   if F(c['optimal_trial_budget'][1])<0:ck(optimal[1]<0)
  y=list(map(F,c['exact_inverse_trial_y']));ck(len(y)==6);e=[total(mul((v[i],v[i]),E[i][j]) for i in range(56)) for j in range(6)];res=[sub(e[i],total(mul(W[i][j],(y[j],y[j])) for j in range(6))) for i in range(6)];
  for i,x in enumerate(res):enclose(c['inverse_trial_residual'][i],x)
  r2=sum(max(abs(a),abs(z))**2 for a,z in res);mu=F(c['inverse_trial_denominator_floor']);ck(mu==F(c['residual_W_positive_certificate']['coefficient_floor_lower'])>0 and F(c['inverse_trial_residual_squared_upper'])>=r2);vc=add(sub(mul((F(2),F(2)),total(mul(x,(z,z)) for x,z in zip(e,y))),quadratic(W,y)),(F(c['inverse_trial_residual_squared_upper'])/mu,)*2);vq=add(quadratic(H0,v),vc);enclose(c['variational_credit_upper'],vc);enclose(c['variational_optimal_budget'],vq);allfail=F(c['variational_optimal_budget'][1])<0 or F(c.get('optimal_trial_budget',['0','0'])[1])<0;ck(c['no_coefficient_matrix_J_closes_full_even_budget']==allfail);
  if F(c['variational_optimal_budget'][1])<0:ck(vq[1]<0)
 ck(c['actual_certified_all_high_retained_dimension']==rank and c['uncovered_retained_dimension']==112-rank);ck(c['CC117_odd56_inherited'] and c['DNE52_rank111_preserved'] and b['integrated_positive_retained_rank']==111);ck(c['response_upper_established'] and c['whole_aperture_positive']==passed and c['original_aperture']=='53/50')
 for key in ('true_high_inverse_evaluated','RH','Lean'):ck(c[key] is False)
 out=dict(stage='DNE53',status='PASS',exact_rational_checks=checks,certificate_path=path,certificate_sha256=ch,input_sha256=c['input_sha256'],trial_dimension=6,source_dimension=62,full_even_response_budget_passed=passed,actual_certified_all_high_retained_dimension=rank,uncovered_retained_dimension=112-rank,combined_physical_gap_lower=c['combined_physical_gap_lower'],no_coefficient_matrix_J_closes_full_even_budget=c.get('no_coefficient_matrix_J_closes_full_even_budget',False),whole_aperture_positive=passed,RH=False,Lean=False);Path(output).write_text(json.dumps(out,indent=2)+'\n');print('PASS',checks,'response checks; rank',rank,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('--output',required=True);a=p.parse_args();run(a.input,a.output)
