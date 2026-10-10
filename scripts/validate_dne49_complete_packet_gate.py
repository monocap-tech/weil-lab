#!/usr/bin/env python3
"""Independent exact polynomial, native, chart, trial and obligation audit."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
import argparse,json
from certify_dne39_signed_comparison import read
from validate_dne34_source_block import boxes,mm,mul,add,neg,sum_box

def run(path,output):
 checks=0
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def enclose(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
 def exact_product(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
 c,ch=read(path);check(c['stage']=='DNE49' and c['parent']=='514386d14dcb1dc1bb2d469bc82a728d8de4b12d');inputs=[read(p) for p in c['input_paths']];check([h for _,h in inputs]==c['input_sha256']);s,sv,response,rv,nv=[x for x,h in inputs];check(sv['status']==rv['status']==nv['status']=='PASS');check(sv['replay_sha256']==inputs[0][1] and rv['certificate_sha256']==inputs[2][1]);check(rv['actual_certified_retained_dimension']==88 and rv['uncovered_retained_dimension']==24)
 rows=[]
 for z in c['rows']:
  par=z['parity'];cert,h=read(z['certificate_path']);check(h==z['certificate_sha256']==next(r['certificate_sha256'] for r in nv['rows'] if r['parity']==par));n,nh=read(cert['input_paths'][1]);f,fh=read(cert['input_paths'][2]);t,th=read(n['input_paths'][2]);check([nh,fh]==cert['input_sha256'][1:3] and th==n['input_sha256'][2]);check(z['input_sha256']==[h,nh,fh,th]);ids=n['retained_indices'];check(ids==list(range(0 if par=='even' else 1,112,2)))
  T=[{ids[0]:F(1)}]+[dict(zip(col['indices'],map(F,col['coefficients']))) for col in t['columns']];W=[list(map(F,r)) for r in zip(*n['exact_W_columns'])];U=[list(map(F,r)) for r in cert['exact_rational_congruence_U']];K=[list(map(F,r)) for r in f['frozen_original_projection_K']];WU=exact_product(W,U);KU=exact_product(K,U);scale=list(map(F,f['column_scales']));expected=[]
  for tt,a in zip(T,scale):expected.append({k:v*a for k,v in tt.items()})
  for j in range(52):
   p={k:WU[i][j] for i,k in enumerate(ids)}
   for i,tt in enumerate(T):
    for k,v in tt.items():p[k]=p.get(k,F(0))-v*KU[i][j]
   expected.append(p)
  check(len(z['columns'])==56)
  for col,p in zip(z['columns'],expected):
   check(col['indices']==sorted(p));v=list(map(F,col['coefficients']));check(v==[p[k] for k in sorted(p)]);mass=sum(x*x for x in v);check(mass==F(col['exact_mass_squared']) and F(col['norm_upper'])**2>mass)
  # Prove rank of [T,W], then [T*S,(W-T*K)*U] by invertible changes.
  gate=z['retained_rank_gate'];top=[[tt.get(k,F(0)) for tt in T] for k in ids[:4]];check(top==[list(map(F,r)) for r in gate['T4_pivot_matrix']]);det=F(0)
  for p in permutations(range(4)):
   sign=(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4));term=F(sign)
   for i in range(4):term*=top[i][p[i]]
   det+=term
  check(det==F(gate['T4_pivot_determinant']) and det!=0);check(all(a!=0 for a in scale));check(gate['W_identity_minor_rows']==list(range(4,56)))
  for i in range(52):
   for j in range(52):check(W[i+4][j]==F(i==j));check(i<=j or U[i][j]==0)
   check(U[i][i]!=0)
   for tt in T:check(sum(tt.get(k,F(0))*W[r][i] for r,k in enumerate(ids))==0)
  check(gate['rank']==56 and gate['orthogonality_exact'] and gate['U_upper_triangular_invertible'])
  # Independent unrounded interval assembly of original native border.
  A=boxes(cert['tightened_scaled_T4_native_matrix']);P=boxes(cert['tightened_scaled_T4_W52_border']);J=[[(F(x),F(x)) for x in r] for r in f['frozen_scaled_projection_J']];AJ=mm(A,J);E=[[add(p,neg(q)) for p,q in zip(r,ss)] for r,ss in zip(P,AJ)];UI=[[(x,x) for x in r] for r in U];border=mm(E,UI);C=boxes(cert['congruence_matrix']);N=boxes(z['native_matrix']);check(len(N)==56 and all(len(r)==56 for r in N))
  for i in range(56):
   for j in range(56):
    value=A[i][j] if i<4 and j<4 else border[i][j-4] if i<4 else border[j][i-4] if j<4 else C[i-4][j-4];enclose(N[i][j],value)
  prior=s if par=='even' else read('notes/data/RPB108_DNE44_ODD_JOINT_SOURCE_REPLAY_20261010.json.gz.b64')[0];check(z['prior_packet_sha256']==(read('notes/data/RPB108_DNE47_RESPONSE_TRIAL_GATE_20261010.json')[0]['normalized_packet_sha256'] if par=='even' else prior['normalized_packet_sha256']));check(z['native_matrix'][:44] and [r[:44] for r in z['native_matrix'][:44]]==prior['native_block']);
  pc=z['finite_native_positive_certificate'];check(pc['original_matrix_reference']=='native_matrix');O=N;V=[list(map(F,r)) for r in pc['exact_congruence_U']];check(O==N and len(V)==56 and all(len(r)==56 for r in V))
  for i in range(56):
   check(V[i][i]!=0)
   for j in range(i):check(V[i][j]==0)
  VI=[[(x,x) for x in r] for r in V];trans=list(map(list,zip(*VI)));Q=mm(trans,mm(N,VI));paid=boxes(pc['congruence_matrix']);margins=[]
  for i in range(56):
   for j in range(56):enclose(paid[i][j],Q[i][j])
   m=paid[i][i][0]-sum(max(abs(a),abs(b)) for j,(a,b) in enumerate(paid[i]) if i!=j);check(m==F(pc['Gershgorin_margins'][i]) and m>0);margins.append(m)
  floor=min(margins)/sum(x*x for r in V for x in r);check(floor==F(pc['coefficient_floor_lower']) and floor>0)
  src=z['columns'][:44]+z['high_trial_columns']+z['columns'][44:];check(z['source_column_labels']==z['column_labels'][:44]+(['Y0','Y1','Y2'] if par=='even' else [])+z['column_labels'][44:]);mapping=z['native_to_source'];check(len(mapping)==56 and len(set(mapping))==56)
  for i,j in enumerate(mapping):check(src[j]==z['columns'][i])
  old=z['reused_source_count'];count=len(src);check((old,count)==((47,59) if par=='even' else (44,56)));check(mapping==(list(range(44))+list(range(47,59)) if par=='even' else list(range(56))))
  expected_pairs=[[i,j] for i in range(count) for j in range(i,count) if j>=old];check(z['missing_source_upper_triangle']==expected_pairs);check(len(expected_pairs)==z['missing_source_correlation_count']==(642 if par=='even' else 606));check(len(set(map(tuple,expected_pairs)))==len(expected_pairs))
  if par=='even':
   # Authenticate unchanged trial polynomials directly against DNE47.
   trial,tsha=read('notes/data/RPB108_DNE47_RESPONSE_TRIAL_GATE_20261010.json');check(z['trial_source_indices']==[44,45,46] and tsha==s['joint_packet_input_sha256'][-2]);
   for j,col in enumerate(src[44:47]):
    tt=trial['physical_high_trial_columns'][j];check(all(col[k]==tt[k] for k in ('indices','coefficients','exact_mass_squared')) and col['norm_upper']=='1');check(all(k>=112 for k in col['indices']))
   coords=[dict(zip(s['trial_action_coordinate_indices'],[tuple(map(F,b)) for b in r])) for r in s['trial_rounded_action_coordinates']];gamma=list(map(F,s['source_L2_error_upper']));M=z['paid_full_trial_native_M'];check(len(M)==56 and all(len(r)==3 for r in M))
   for i,col in enumerate(z['columns']):
    for j in range(3):
     bounds=sum_box(mul((F(a),F(a)),coords[j][k]) for k,a in zip(col['indices'],col['coefficients']));pay=gamma[44+j]*F(col['norm_upper']);check(tuple(map(F,M[i][j]))==(bounds[0]-pay,bounds[1]+pay))
     if i<44:check(M[i][j]==response['trial_native_pairings'][j][i])
   check(z['new_trial_native_pairing_count']==36)
  else:check(z['trial_source_indices']==[])
  rows.append(dict(parity=par,retained_chart_rank=56,finite_native_positive=True,finite_native_coefficient_floor=str(floor),missing_source_correlations=len(expected_pairs)))
 check([r['parity'] for r in rows]==['even','odd']);check(c['complete_retained_packet_dimension']==112 and c['finite_native_packet_positive']);check(c['remaining_trial_native_pairings_paid']==36 and c['missing_source_correlation_count']==1248);check(c['actual_certified_all_high_retained_dimension']==88 and c['uncovered_retained_dimension']==24)
 for k in ('new_source_integrals_computed','complete_remaining_source_Gram_certified','full_remaining_response_budget_evaluated','true_high_inverse_evaluated','whole_aperture_positive','RH','Lean'):check(c[k] is False)
 out=dict(stage='DNE49',status='PASS',exact_rational_checks=checks,certificate_path=path,certificate_sha256=ch,input_sha256=c['input_sha256'],rows=rows,remaining_trial_native_pairings_paid=36,missing_source_correlations=1248,actual_certified_all_high_retained_dimension=88,uncovered_retained_dimension=24,new_source_integrals_computed=False,whole_aperture_positive=False,RH=False,Lean=False);Path(output).write_text(json.dumps(out,indent=2)+'\n');print('PASS',checks,'DNE49 exact checks',flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('--output',required=True);a=p.parse_args();run(a.input,a.output)
