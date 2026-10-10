#!/usr/bin/env python3
"""Paid complete source/native comparison, with inherited even high trials."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,gzip,base64,numpy as np
from certify_dne39_signed_comparison import read,matrix,positive,quadratic
from certify_dne32_native_remainder import I,mm,tr
PARENT='bb68642b1384d50d6b9fea517db9691e924fe5a5'

def run(output):
 vp='notes/data/RPB108_DNE50_COMPLETE_SOURCE_VALIDATION_20261010.json';sv,svh=read(vp);gp='notes/data/RPB108_DNE49_COMPLETE_PACKET_GATE_20261010.json.gz.b64';g,gh=read(gp);gvp='notes/data/RPB108_DNE49_COMPLETE_PACKET_VALIDATION_20261010.json';gv,gvh=read(gvp);hp='notes/data/RPB108_DNE46_HIGH_FLOOR_VALIDATION_20261010.json';hv,hvh=read(hp);rp='notes/data/RPB108_DNE48_RESIDUAL_RESPONSE_20261010.json.gz.b64';old,oh=read(rp);rvp='notes/data/RPB108_DNE48_RESIDUAL_RESPONSE_VALIDATION_20261010.json';rv,rvh=read(rvp)
 assert sv['status']==gv['status']==hv['status']==rv['status']=='PASS' and gv['certificate_sha256']==gh and rv['certificate_sha256']==oh; k=F(hv['original_infinite_F112_floor']);assert k==F(647,1000);rows=[]
 def bb(X):return [[x.box() for x in row] for row in X]
 for par in ('even','odd'):
  p=f'notes/data/RPB108_DNE50_{par.upper()}_COMPLETE_SOURCE_REPLAY_20261010.json.gz.b64';s,sh=read(p);audit=next(v for v in sv['rows'] if v['parity']==par);assert audit['replay_sha256']==sh;mapn=s['native_to_source'];S=matrix(s['original_projected_source_Gram']);N=matrix(s['native_block']);G=[[S[i][j] for j in mapn] for i in mapn];H=[[I(k)*n-gg for n,gg in zip(nr,gr)] for nr,gr in zip(N,G)];z=dict(parity=par,source_path=p,source_sha256=sh,native_to_source=mapn,original_native_matrix=bb(N),projected_native_source_Gram=bb(G),trial_response_used=par=='even')
  if par=='even':
   ys=s['trial_source_indices'];B=[[S[i][j] for j in ys] for i in mapn];D=[[S[i][j] for j in ys] for i in ys];r=next(r for r in g['rows'] if r['parity']=='even');M=matrix(r['paid_full_trial_native_M']);A=matrix(old['original_native_A']);E=[[b-I(k)*m for b,m in zip(br,mr)] for br,mr in zip(B,M)];W=[[d-I(k)*a for d,a in zip(dr,ar)] for dr,ar in zip(D,A)];wp=positive(W);assert wp is not None
   mid=lambda X:np.array([[float((v.l+v.h)/2) for v in row] for row in X]);j=np.linalg.solve(mid(W),mid(E).T);J=[[F(round(float(v)*10**25),10**25) for v in r] for r in j];JI=[[I(v) for v in r] for r in J];EJ=mm(E,JI);JWJ=mm(tr(JI),mm(W,JI));C=[[EJ[i][j]+EJ[j][i]-JWJ[i][j] for j in range(56)] for i in range(56)];H=[[h+c for h,c in zip(hr,cr)] for hr,cr in zip(H,C)];z.update(original_native_M=bb(M),original_native_A=bb(A),residual_E=bb(E),residual_W=bb(W),residual_W_positive_certificate=wp,exact_trial_coefficients_J=[list(map(str,r)) for r in J],response_credit_numerator=bb(C))
  pc=positive(H);z.update(paid_response_budget=bb(H),full_response_budget_passed=pc is not None,full_response_positive_certificate=pc)
  if pc is not None:
   mass=sum(F(s['exact_masses'][i]) for i in mapn);trace=sum(G[i][i].h for i in range(56));sf=F(pc['coefficient_floor_lower'])/k;gap=min(sf/(4*(mass+trace/k**2)),k/2);z.update(positive_retained_rank=56,physical_packet_mass=str(mass),projected_source_trace_upper=str(trace),Schur_coefficient_floor=str(sf),all_high_physical_gap_lower=str(gap));print(par,'FULL56 PASS',float(gap),flush=True)
  else:
   mid=np.array([[float((v.l+v.h)/2) for v in row] for row in H]);vv,ee=np.linalg.eigh((mid+mid.T)/2);v=[F(round(float(x)*10**20),10**20) for x in ee[:,0]];q=quadratic(H,v);z.update(positive_retained_rank=44,exact_comparison_failure_trial=list(map(str,v)),comparison_failure_trial_budget=q.box(),comparison_failure_proved=q.h<0);print(par,'full56 sufficient budget fails; exact negative comparison',q.h<0,flush=True)
  rows.append(z)
 rank=sum(z['positive_retained_rank'] for z in rows);whole=rank==112;gap=min(F(z['all_high_physical_gap_lower']) for z in rows) if whole else None
 paths=[vp,gp,gvp,hp,rp,rvp];out=dict(stage='DNE50',parent=PARENT,input_paths=paths,input_sha256=[svh,gh,gvh,hvh,oh,rvh],original_high_floor=str(k),rows=rows,actual_certified_all_high_retained_dimension=rank,uncovered_retained_dimension=112-rank,original_aperture='53/50',all_high_physical_gap_lower=str(gap) if whole else None,response_upper_established=True,true_high_inverse_evaluated=False,whole_aperture_positive=whole,RH=False,Lean=False)
 b=(json.dumps(out,indent=2)+'\n').encode();Path(output).write_bytes(base64.b64encode(gzip.compress(b,mtime=0))+b'\n')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);run(p.parse_args().output)
