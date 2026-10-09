#!/usr/bin/env python3
"""Rationally paid matrix source budgets and explicit failure witnesses."""
from pathlib import Path
from fractions import Fraction as F
import argparse,base64,gzip,hashlib,json
import numpy as np
from certify_dne32_native_remainder import I,precondition,mm,tr
from certify_dne34_source_block import root

def read(p):
 b=Path(p).read_bytes()
 if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
 return json.loads(b),hashlib.sha256(b).hexdigest()
def matrix(boxes):return [[I(*v) for v in row] for row in boxes]
def quadratic(M,v):return sum((I(x)*M[i][j]*I(y) for i,x in enumerate(v) for j,y in enumerate(v)),I(0))
def certify(C,G,r):
 H=[[I(r)*c-g for c,g in zip(a,b)] for a,b in zip(C,G)]
 try:U=precondition(H)
 except AssertionError:return None
 K=mm(tr(U),mm(H,U));margins=[K[i][i].l-sum(max(abs(K[i][j].l),abs(K[i][j].h)) for j in range(len(C)) if j!=i) for i in range(len(C))]
 if min(margins)<=0:return None
 return dict(source_ratio_upper=str(r),source_budget_matrix=[[v.box() for v in row] for row in H],exact_congruence_U=[list(map(str,row)) for row in U],budget_congruence_matrix=[[v.box() for v in row] for row in K],budget_Gershgorin_margins=list(map(str,margins)))
def run(primary_path,replay_path,output):
 a,ah=read(primary_path);b,bh=read(replay_path);native,nh=read(b['certificate_path']);C=matrix(b['native_block']);G=matrix(b['original_projected_source_Gram']);count=len(C);credit=F(b['source_credit']);dual=F(native['native_mixed_dual_border_squared_upper']);eps=root(dual);kappa=F(11,25)
 # Floating point only selects exact rational comparison trials.
 Cm=np.array([[float((v.l+v.h)/2) for v in row] for row in C]);Gm=np.array([[float((v.l+v.h)/2) for v in row] for row in G]);L=np.linalg.cholesky(Cm);Li=np.linalg.inv(L);R=Li@Gm@Li.T;vals,vec=np.linalg.eigh((R+R.T)/2);trial=Li.T@vec[:,-1];v=[F(round(float(x)*10**16),10**16) for x in trial];qe=quadratic(C,v);qg=quadratic(G,v)
 controls=[]
 for r in (credit/2,credit):
  q=quadratic([[I(r)*c-g for c,g in zip(rowC,rowG)] for rowC,rowG in zip(C,G)],v)
  controls.append(dict(source_budget=str(r),exact_trial=list(map(str,v)),native_energy=qe.box(),source_energy=qg.box(),budget_quadratic=q.box(),failure_proved=q.h<0))
 block=certify(C,G,credit/2);chosen='half_credit'
 if block is None:
  r=F(int(np.ceil(vals[-1]*10**6))+2,10**6)
  if r+kappa*eps<credit:block=certify(C,G,r);chosen='paid_reallocation'
 largest=0;prefix=None
 for n in range(1,count+1):
  cc=[row[:n] for row in C[:n]];gg=[row[:n] for row in G[:n]];cm=Cm[:n,:n];gm=Gm[:n,:n];ll=np.linalg.cholesky(cm);ii=np.linalg.inv(ll);rr=ii@gm@ii.T;ev=np.linalg.eigvalsh((rr+rr.T)/2)[-1];r=credit/2
  p=certify(cc,gg,r)
  if p is None:
   r=F(int(np.ceil(ev*10**6))+2,10**6)
   p=certify(cc,gg,r) if r+kappa*eps<credit else None
  if p is not None:largest=n;prefix=p
 assert largest>=1 and prefix is not None
 selected=block if block is not None else prefix;n=count if block is not None else largest;r=F(selected['source_ratio_upper']);schur=(credit-r)/kappa-eps;assert schur>0
 standalone=certify(C,G,kappa);assert standalone is not None
 out=dict(standalone_remainder_uniform_floor_certificate=standalone,stage='DNE34',parity=b['parity'],input_paths=[primary_path,replay_path],input_sha256=[ah,bh],native_certificate_sha256=nh,source_columns=b['columns'],source_budget_controls=controls,native_dual_border_squared_upper=str(dual),native_dual_border_upper=str(eps),original_high_floor=str(kappa),tested_source_credit=str(credit),complete_requested_block_budget_passed=block is not None,comparison_route=chosen if block else 'largest_certified_prefix',certified_prefix_count=n,source_budget_certificate=selected,Schur_energy_lower=str(schur),all_high_positive_retained_rank=4+n,complete_remaining_source_Gram_certified=False,whole_aperture_positive=False,RH=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print(b['parity'],'source max diagnostic',vals[-1],'prefix',n,'half failure',controls[0]['failure_proved'],'full credit failure',controls[1]['failure_proved'])
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('primary');p.add_argument('replay');p.add_argument('--output',required=True);a=p.parse_args();run(a.primary,a.replay,a.output)
