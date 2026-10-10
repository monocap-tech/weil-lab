#!/usr/bin/env python3
"""Six-trial whole-high response comparison at the actual original floor."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,gzip,base64,numpy as np
from certify_dne39_signed_comparison import read,matrix,positive,quadratic
from certify_dne32_native_remainder import I,mm,tr
PARENT='7d0d03400f78a3bf0d91d01c52a1b6d6a33e4bd4'
PATHS=['notes/data/RPB108_DNE53_EVEN_SOURCE_VALIDATION_20261010.json','notes/data/RPB108_DNE53_EVEN_SOURCE_REPLAY_20261010.json.gz.b64','notes/data/RPB108_DNE50_FULL_RESPONSE_20261010.json.gz.b64','notes/data/RPB108_DNE52_CC117_INGESTION_20261010.json','notes/data/RPB108_DNE52_CC117_INGESTION_VALIDATION_20261010.json','notes/data/RPB108_DNE46_HIGH_FLOOR_VALIDATION_20261010.json','notes/data/RPB108_DNE49_COMPLETE_PACKET_VALIDATION_20261010.json']
def bb(M):return [[x.box() for x in r] for r in M]
def mid(M):return np.array([[float((v.l+v.h)/2) for v in row] for row in M])
def native_extensions(s,old,bridge):
 reuse,rh=read(s['reused_source_path']);errors=list(map(F,s['source_L2_error_upper']));action=matrix(s['new_rounded_action_coordinates']);oldaction=matrix(reuse['trial_rounded_action_coordinates']);ids=s['new_action_coordinate_indices'];at={n:i for i,n in enumerate(ids)}
 def paid(x,e):return I(x.l-e,x.h+e)
 def intersection(a,b):return I(max(a.l,b.l),min(a.h,b.h))
 A=[[I(0) for j in range(6)] for i in range(6)];oldA=matrix(old['original_native_A']);A[:3]=[r+[I(0)]*3 for r in oldA]
 for i in range(3):
  for u,n in enumerate((112,114,116)):A[i][3+u]=A[3+u][i]=paid(oldaction[i][at[n]],errors[44+i])
 self2=matrix(bridge['reused_native_self_Gram'])
 for u in range(3):
  for v in range(u,3):
   x=paid(action[u][at[112+2*v]],errors[59+u]);y=paid(action[v][at[112+2*u]],errors[59+v]);z=intersection(x,y)
   if u<2 and v<2:
    intersection(z,self2[u][v]);z=self2[u][v]
   A[3+u][3+v]=A[3+v][3+u]=z
 M=matrix(old['original_native_M']);reuseM=matrix(bridge['reused_native_pairings_Z_to_e112_e114']);cols=[s['columns'][i] for i in s['native_to_source']]
 for i,c in enumerate(cols):
  z=sum((I(F(v))*action[2][at[n]] for n,v in zip(c['indices'],c['coefficients'])),I(0));z=paid(z,errors[61]*F(c['norm_upper']));M[i]=M[i]+reuseM[i]+[z]
 return A,M

def invquad(W,e):
 # Independent interval LDL elimination, with exact outward rational pivots.
 n=len(W);L=[[I(i==j) for j in range(n)] for i in range(n)];ds=[]
 def div(a,b):assert b.l>0;return a*I(1/b.h,1/b.l)
 for i in range(n):
  d=W[i][i]-sum((L[i][k]*L[i][k]*ds[k] for k in range(i)),I(0));assert d.l>0;ds.append(d)
  for j in range(i+1,n):L[j][i]=div(W[j][i]-sum((L[j][k]*L[i][k]*ds[k] for k in range(i)),I(0)),d)
 u=[]
 for i in range(n):u.append(e[i]-sum((L[i][k]*u[k] for k in range(i)),I(0)))
 return sum((div(x*x,d) for x,d in zip(u,ds)),I(0)),[x.box() for x in ds]

def run(output):
 inp=[read(p) for p in PATHS];sv,s,r,b,bv,hv,gv=[x for x,h in inp];assert sv['status']==bv['status']==hv['status']==gv['status']=='PASS';assert sv['replay_sha256']==inp[1][1] and bv['certificate_sha256']==inp[3][1];assert gv['certificate_sha256']==s['input_sha256'][0] and gv['rows'][0]['retained_chart_rank']==56;k=F(hv['original_infinite_F112_floor']);assert k==F(647,1000);old=r['rows'][0];A,M=native_extensions(s,old,b);S=matrix(s['original_projected_source_Gram']);ns=s['native_to_source'];ys=s['trial_source_indices'];N=matrix(s['native_block']);G=[[S[i][j] for j in ns] for i in ns];B=[[S[i][j] for j in ys] for i in ns];D=[[S[i][j] for j in ys] for i in ys];E=[[v-I(k)*q for v,q in zip(br,mr)] for br,mr in zip(B,M)];W=[[v-I(k)*q for v,q in zip(dr,ar)] for dr,ar in zip(D,A)];wp=positive(W);assert wp
 j=np.linalg.solve(mid(W),mid(E).T);J=[[F(round(float(v)*10**25),10**25) for v in row] for row in j];JI=[[I(x) for x in row] for row in J];EJ=mm(E,JI);JWJ=mm(tr(JI),mm(W,JI));H0=[[I(k)*N[i][j]-G[i][j] for j in range(56)] for i in range(56)];H=[[H0[i][j]+EJ[i][j]+EJ[j][i]-JWJ[i][j] for j in range(56)] for i in range(56)];pc=positive(H);extra={}
 if pc:
  mass=sum(F(s['exact_masses'][i]) for i in ns);trace=sum(G[i][i].h for i in range(56));sf=F(pc['coefficient_floor_lower'])/k;gap=min(sf/(4*(mass+trace/k**2)),k/2);guard=min(gap,F(b['physical_guard']));extra.update(physical_packet_mass=str(mass),projected_source_trace_upper=str(trace),Schur_coefficient_floor=str(sf),even_all_high_physical_gap_lower=str(gap),combined_physical_gap_lower=str(guard));rank=112;print('FULL EVEN56 PASS',float(gap),flush=True)
 else:
  vals,vects=np.linalg.eigh((mid(H)+mid(H).T)/2);v=[F(round(float(x)*10**20),10**20) for x in vects[:,0]];q=quadratic(H,v);assert q.h<0;extra.update(exact_comparison_failure_trial=list(map(str,v)),comparison_failure_trial_budget=q.box(),comparison_failure_proved=True)
  e=[sum((I(v[i])*E[i][j] for i in range(56)),I(0)) for j in range(6)];base=quadratic(H0,v)
  try:
   credit,piv=invquad(W,e);optimal=base+credit;extra.update(base_trial_budget=base.box(),optimal_credit_trial=credit.box(),optimal_trial_budget=optimal.box(),LDL_positive_pivots=piv,no_coefficient_matrix_J_closes_full_even_budget=optimal.h<0)
  except AssertionError:extra['no_coefficient_matrix_J_closes_full_even_budget']=False
  # A second all-coefficient upper uses the paid W floor and an exact
  # rational finite-solve proposal, without relying on interval elimination.
  em=np.array([float((x.l+x.h)/2) for x in e]);ym=np.linalg.solve(mid(W),em);y=[F(round(float(x)*10**25),10**25) for x in ym];yi=[I(x) for x in y];res=[e[i]-sum((W[i][j]*yi[j] for j in range(6)),I(0)) for i in range(6)];mu=F(wp['coefficient_floor_lower']);res2=sum(max(abs(x.l),abs(x.h))**2 for x in res);vc=2*sum((x*z for x,z in zip(e,yi)),I(0))-quadratic(W,y)+I(res2/mu);vq=base+vc;extra.update(exact_inverse_trial_y=list(map(str,y)),inverse_trial_residual=[x.box() for x in res],inverse_trial_residual_squared_upper=str(res2),inverse_trial_denominator_floor=str(mu),variational_credit_upper=vc.box(),variational_optimal_budget=vq.box());extra['no_coefficient_matrix_J_closes_full_even_budget']=extra['no_coefficient_matrix_J_closes_full_even_budget'] or vq.h<0
  rank=111;extra['combined_physical_gap_lower']=b['physical_guard'];print('EVEN56 comparison fails',float(q.h),'all-J',extra['no_coefficient_matrix_J_closes_full_even_budget'],flush=True)
 out=dict(stage='DNE53',parent=PARENT,input_paths=PATHS,input_sha256=[h for x,h in inp],original_aperture='53/50',original_high_floor=str(k),trial_dimension=6,source_dimension=62,native_to_source=ns,trial_source_indices=ys,original_native_matrix=bb(N),projected_native_source_Gram=bb(G),original_native_M=bb(M),original_native_A=bb(A),residual_E=bb(E),residual_W=bb(W),residual_W_positive_certificate=wp,exact_trial_coefficients_J=[list(map(str,row)) for row in J],paid_response_budget=bb(H),full_even_response_budget_passed=pc is not None,full_even_response_positive_certificate=pc,CC117_odd56_inherited=True,DNE52_rank111_preserved=True,actual_certified_all_high_retained_dimension=rank,uncovered_retained_dimension=112-rank,response_upper_established=True,true_high_inverse_evaluated=False,whole_aperture_positive=rank==112,RH=False,Lean=False,**extra);raw=(json.dumps(out,indent=2)+'\n').encode();Path(output).write_bytes(base64.b64encode(gzip.compress(raw,mtime=0))+b'\n')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);run(p.parse_args().output)
