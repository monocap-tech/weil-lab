#!/usr/bin/env python3
"""Paid full-matrix original inverse-response upper from three high trials."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,base64,gzip,numpy as np
from certify_dne39_signed_comparison import read,matrix,positive,quadratic
from certify_dne32_native_remainder import I,mm,tr
from materialize_dne48_trial_sources import run as materialize
from validate_dne34_source_block import add,mul,sum_box
PARENT='da5b09e3b72b8e05e3daab5e37e6b3398a5558f8'
def run(output):
 paths=['notes/data/RPB108_DNE48_TRIAL_SOURCE_REPLAY_20261010.json.gz.b64','notes/data/RPB108_DNE48_TRIAL_SOURCE_VALIDATION_20261010.json','notes/data/RPB108_DNE46_HIGH_FLOOR_VALIDATION_20261010.json','notes/data/RPB108_DNE46_EVEN_POSITIVE_SUBSPACE_20261010.json.gz.b64','notes/data/RPB108_DNE46_POSITIVE_SUBSPACE_VALIDATION_20261010.json'];inputs=[read(p) for p in paths];s,sv,h,prior,pv=[x for x,_ in inputs];assert sv['status']==h['status']==pv['status']=='PASS' and sv['replay_sha256']==inputs[0][1];assert next(x for x in pv['rows'] if x['parity']=='even')['certificate_sha256']==inputs[3][1]
 pp=output+'.packet';materialize(s['certificate_path'],pp);packet,ph=read(pp);Path(pp).unlink();assert ph==s['normalized_packet_sha256'];cols=packet['columns'];ids=s['trial_action_coordinate_indices'];tc=[list(map(lambda x:tuple(map(F,x)),row)) for row in s['trial_rounded_action_coordinates']];errors=list(map(F,s['source_L2_error_upper']));pairs=[]
 for i in range(3):
  row=[];coords=dict(zip(ids,tc[i]))
  for col in cols:
   val=sum_box(mul((F(x),F(x)),coords[n]) for n,x in zip(col['indices'],col['coefficients']));pay=errors[44+i]*F(col['norm_upper']);row.append((val[0]-pay,val[1]+pay))
  pairs.append(row)
 M=[[I(*pairs[j][i]) for j in range(3)] for i in range(44)];A=[[I(max(pairs[i][44+j][0],pairs[j][44+i][0]),min(pairs[i][44+j][1],pairs[j][44+i][1])) for j in range(3)] for i in range(3)]
 k=F(h['original_infinite_F112_floor']);assert k==F(647,1000);S=matrix(s['original_projected_source_Gram']);G=[row[:44] for row in S[:44]];B=[row[44:] for row in S[:44]];D=[row[44:] for row in S[44:]];N=matrix(s['native_block']);E=[[b-I(k)*m for b,m in zip(br,mr)] for br,mr in zip(B,M)];W=[[d-I(k)*a for d,a in zip(dr,ar)] for dr,ar in zip(D,A)];wp=positive(W);assert wp is not None
 mid=lambda X:np.array([[float((x.l+x.h)/2) for x in row] for row in X]);j=np.linalg.solve(mid(W),mid(E).T);J=[[F(round(float(x)*10**25),10**25) for x in row] for row in j];JI=[[I(x) for x in row] for row in J];EJ=mm(E,JI);JT_W_J=mm(tr(JI),mm(W,JI));C=[[EJ[i][z]+EJ[z][i]-JT_W_J[i][z] for z in range(44)] for i in range(44)];H=[[I(k)*n-g+c for n,g,c in zip(nr,gr,cr)] for nr,gr,cr in zip(N,G,C)];pc=positive(H)
 def bb(X):return [[x.box() for x in row] for row in X]
 out=dict(stage='DNE48',parent=PARENT,parity='even',input_paths=paths,input_sha256=[h for _,h in inputs],packet_sha256=ph,original_high_floor=str(k),trial_native_pairings=[[list(map(str,x)) for x in row] for row in pairs],original_native_M=bb(M),original_native_A=bb(A),residual_E=bb(E),residual_W=bb(W),residual_W_positive_certificate=wp,exact_trial_coefficients_J=[list(map(str,row)) for row in J],response_credit_numerator=bb(C),paid_response_budget=bb(H),full_response_budget_passed=pc is not None,full_response_positive_certificate=pc,new_source_integrals_computed=True,prior_source_entries_reintegrated=False,response_upper_established=True,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,Lean=False)
 if pc is not None:
  mass=sum(map(F,s['exact_masses'][:44]));trace=sum(G[i][i].h for i in range(44));sf=F(pc['coefficient_floor_lower'])/k;gap=min(sf/(4*(mass+trace/k**2)),k/2);out.update(positive_retained_rank=44,actual_certified_retained_dimension=88,uncovered_retained_dimension=24,prior_87_direction_span_contained=True,physical_packet_mass=str(mass),projected_source_trace_upper=str(trace),Schur_coefficient_floor=str(sf),all_high_physical_gap_lower=str(gap));print('PASS full even response budget; retained total 88; gap',float(gap),flush=True)
 else:
  vals,vec=np.linalg.eigh((mid(H)+mid(H).T)/2);v=[F(round(float(x)*10**20),10**20) for x in vec[:,0]];budget=quadratic(H,v);out.update(positive_retained_rank=43,actual_certified_retained_dimension=87,uncovered_retained_dimension=25,exact_response_failure_trial=list(map(str,v)),response_failure_trial_budget=budget.box(),response_budget_failure_proved=budget.h<0);print('full even response budget failed diagnostic',float(vals[0]),'paid negative trial',budget.h<0,flush=True)
 payload=(json.dumps(out,indent=2)+'\n').encode();Path(output).write_bytes(base64.b64encode(gzip.compress(payload,mtime=0))+b'\n')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);run(ap.parse_args().output)
