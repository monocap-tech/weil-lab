#!/usr/bin/env python3
"""Joint signed uniform-high-floor comparison and exact obstruction controls."""
from pathlib import Path
from fractions import Fraction as F
import argparse,base64,gzip,hashlib,json
import numpy as np
from certify_dne32_native_remainder import I,precondition,mm,tr

def read(p):
 b=Path(p).read_bytes()
 if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
 return json.loads(b),hashlib.sha256(b).hexdigest()
def matrix(boxes):return [[I(*v) for v in row] for row in boxes]
def quadratic(M,v):return sum((I(x)*M[i][j]*I(y) for i,x in enumerate(v) for j,y in enumerate(v)),I(0))
def positive(M):
 try:U=precondition(M)
 except AssertionError:return None
 K=mm(tr(U),mm(M,U));margins=[K[i][i].l-sum(max(abs(K[i][j].l),abs(K[i][j].h)) for j in range(len(M)) if j!=i) for i in range(len(M))]
 if min(margins)<=0:return None
 return dict(original_matrix=[[x.box() for x in row] for row in M],exact_congruence_U=[list(map(str,row)) for row in U],congruence_matrix=[[x.box() for x in row] for row in K],Gershgorin_margins=list(map(str,margins)),coefficient_floor_lower=str(min(margins)/sum(x*x for row in U for x in row)))
def run(primary_path,replay_path,output):
 high_path='notes/data/RPB108_DNE37_PRIME_SCHUR_REPLAY_20261010.json';high,hh=read(high_path);assert high['certified_original_F112_lower']=='57/100'
 a,ah=read(primary_path);b,bh=read(replay_path);Q=matrix(b['native_block']);G=matrix(b['original_projected_source_Gram']);kappa=F(57,100);H=[[I(kappa)*x-y for x,y in zip(q,g)] for q,g in zip(Q,G)];native=positive(Q);assert native is not None
 Qm=np.array([[float((x.l+x.h)/2) for x in row] for row in Q]);Gm=np.array([[float((x.l+x.h)/2) for x in row] for row in G]);L=np.linalg.cholesky(Qm);Li=np.linalg.inv(L);R=Li@Gm@Li.T;vals,vec=np.linalg.eigh((R+R.T)/2);v=[F(round(float(x)*10**16),10**16) for x in (Li.T@vec[:,-1])];qt=quadratic(Q,v);gt=quadratic(G,v);ht=quadratic(H,v);full=positive(H)
 largest=4;prefix=None
 for n in range(4,29):
  candidate=positive([row[:n] for row in H[:n]])
  if candidate is not None:largest=n;prefix=candidate
 assert prefix is not None and largest>=({'even':18,'odd':17}[b['parity']])
 raw_floor=F(high['inherited_arch_minus_pole_strict_lower'])-F(high['rigorous_max_row_ratio_upper']);raw_trial=I(raw_floor)*qt-gt;required_floor_lower=gt.l/qt.h
 first_failure=None
 if largest<28:
  n=largest+1;Qp=[r[:n] for r in Q[:n]];Gp=[r[:n] for r in G[:n]];Hp=[r[:n] for r in H[:n]]
  qm=Qm[:n,:n];gm=Gm[:n,:n];li=np.linalg.inv(np.linalg.cholesky(qm));rr=li@gm@li.T;vv,ee=np.linalg.eigh((rr+rr.T)/2);w=[F(round(float(x)*10**16),10**16) for x in li.T@ee[:,-1]];q=quadratic(Qp,w);g=quadratic(Gp,w);h=quadratic(Hp,w)
  assert q.l>0 and h.h<0
  first_failure=dict(joint_dimension=n,remainder_dimension=n-4,exact_trial=list(map(str,w)),native_energy=q.box(),source_energy=g.box(),signed_budget=h.box(),uniform_floor_failure_proved=True)
 out=dict(stage='DNE38',parent='f11f94dcd72c2d1a8438bdfbc7e7890b47902088',parity=b['parity'],input_paths=[primary_path,replay_path],input_sha256=[ah,bh],original_high_floor=str(kappa),high_certificate_path=high_path,high_certificate_sha256=hh,raw_iterated_weight_floor=str(raw_floor),trial_required_uniform_floor_lower=str(required_floor_lower),raw_weight_floor_trial_signed_budget=raw_trial.box(),raw_weight_floor_trial_failure_proved=raw_trial.h<0,joint_native_positive_control=native,exact_failure_trial=list(map(str,v)),failure_trial_native_energy=qt.box(),failure_trial_source_energy=gt.box(),failure_trial_signed_budget=ht.box(),joint_uniform_floor_failure_proved=ht.h<0,first_failing_joint_prefix=first_failure,full_joint_signed_budget_passed=full is not None,certified_joint_prefix_dimension=largest,certified_remainder_prefix_dimension=largest-4,positive_joint_prefix_certificate=prefix,all_high_positive_retained_rank=largest,complete_joint_source_Gram_certified=True,complete_remaining_source_Gram_certified=False,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print(b['parity'],'joint ratio diagnostic',vals[-1],'full pass',full is not None,'failure',ht.h<0,'prefix',largest)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('primary');p.add_argument('replay');p.add_argument('--output',required=True);a=p.parse_args();run(a.primary,a.replay,a.output)
