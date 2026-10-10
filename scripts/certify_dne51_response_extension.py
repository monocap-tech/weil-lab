#!/usr/bin/env python3
"""Optimal fixed-trial obstruction and exact new high-frame source gate."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from math import isqrt
import argparse,json,gzip,base64,numpy as np
from certify_dne39_signed_comparison import read,matrix,positive,quadratic
from certify_dne32_native_remainder import I,mm,tr

PARENT='3c61708f807b42ddffcff7d0a8516ea6a9e45cf1'
PATHS=['notes/data/RPB108_DNE50_FULL_RESPONSE_20261010.json.gz.b64',
 'notes/data/RPB108_DNE50_FULL_RESPONSE_VALIDATION_20261010.json',
 'notes/data/RPB108_DNE50_POSITIVE_SUBSPACES_20261010.json.gz.b64',
 'notes/data/RPB108_DNE50_POSITIVE_SUBSPACE_VALIDATION_20261010.json',
 'notes/data/RPB108_DNE49_COMPLETE_PACKET_GATE_20261010.json.gz.b64',
 'notes/data/RPB108_DNE47_RESPONSE_TRIAL_GATE_20261010.json',
 'notes/data/RPB108_DNE50_COMPLETE_SOURCE_VALIDATION_20261010.json']
def box(M):return [[v.box() for v in row] for row in M]
def mid(M):return np.array([[float((v.l+v.h)/2) for v in row] for row in M])
def inv3(W):
 def minor(i,j):
  a=[x for x in range(3) if x!=i];b=[x for x in range(3) if x!=j]
  return (W[a[0]][b[0]]*W[a[1]][b[1]]-W[a[0]][b[1]]*W[a[1]][b[0]])*((-1)**(i+j))
 C=[[minor(i,j) for j in range(3)] for i in range(3)]
 det=sum((W[0][j]*C[0][j] for j in range(3)),I(0));assert det.l>0
 reciprocal=I(1/det.h,1/det.l)
 return [[C[j][i]*reciprocal for j in range(3)] for i in range(3)]
def exact_inverse(A):
 n=len(A);R=[row[:]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
 for j in range(n):
  p=next(i for i in range(j,n) if R[i][j]);R[j],R[p]=R[p],R[j];v=R[j][j];R[j]=[x/v for x in R[j]]
  for i in range(n):
   if i!=j:
    v=R[i][j];R[i]=[x-v*y for x,y in zip(R[i],R[j])]
 return [row[n:] for row in R]
def sparse(c):return {n:F(v) for n,v in zip(c['indices'],c['coefficients']) if F(v)}
def gram(cols):
 raw=[sparse(c) for c in cols]
 return [[I(sum(v*b.get(n,F(0)) for n,v in a.items())) for b in raw] for a in raw]
def run(output):
 inp=[read(p) for p in PATHS];r,rv,sub,sv,packet,old,srcv=[x for x,h in inp]
 assert rv['status']==sv['status']==srcv['status']=='PASS'
 assert rv['certificate_sha256']==inp[0][1] and sv['certificate_sha256']==inp[2][1]
 assert sv['actual_certified_all_high_retained_dimension']==109 and sv['uncovered_retained_dimension']==3
 z=r['rows'][0];N=matrix(z['original_native_matrix']);G=matrix(z['projected_native_source_Gram']);M=matrix(z['original_native_M']);A=matrix(z['original_native_A']);s,sh=read(z['source_path'])
 assert sh==z['source_sha256']==srcv['rows'][0]['replay_sha256'] and s['joint_packet_input_sha256'][0]==inp[4][1]
 S=matrix(s['original_projected_source_Gram']);B=[[S[i][j] for j in s['trial_source_indices']] for i in s['native_to_source']];D=[[S[i][j] for j in s['trial_source_indices']] for i in s['trial_source_indices']]
 rows=[]
 for t in (F(647,1000),F(669,1000),F(69,100)):
  E=[[b-I(t)*m for b,m in zip(br,mr)] for br,mr in zip(B,M)];W=[[d-I(t)*a for d,a in zip(dr,ar)] for dr,ar in zip(D,A)];wp=positive(W);assert wp
  ideal=mid(E)@np.linalg.solve(mid(W),mid(E).T);Hm=float(t)*mid(N)-mid(G)+ideal;vv,ee=np.linalg.eigh((Hm+Hm.T)/2);v=[F(round(float(x)*10**20),10**20) for x in ee[:,0]]
  base=quadratic([[I(t)*n-g for n,g in zip(nr,gr)] for nr,gr in zip(N,G)],v)
  e=[sum((I(v[i])*E[i][j] for i in range(56)),I(0)) for j in range(3)];wi=inv3(W);credit=sum((e[i]*wi[i][j]*e[j] for i in range(3) for j in range(3)),I(0));q=base+credit;assert q.h<0
  rows.append(dict(hypothetical_high_floor=str(t),residual_W=box(W),W_positive_certificate=wp,exact_failure_trial=list(map(str,v)),base_trial_budget=base.box(),optimal_credit_trial=credit.box(),optimal_trial_budget=q.box(),no_coefficient_matrix_J_closes_full_even_budget=True));print('all-J obstruction',t,float(q.h),flush=True)
 # A sharp hypothetical sufficient upper: this does not establish an actual floor.
 t=F(691,1000);E=[[b-I(t)*m for b,m in zip(br,mr)] for br,mr in zip(B,M)];W=[[d-I(t)*a for d,a in zip(dr,ar)] for dr,ar in zip(D,A)];candidate=np.linalg.solve(mid(W),mid(E).T);J=[[F(round(float(v)*10**25),10**25) for v in row] for row in candidate];JI=[[I(v) for v in row] for row in J];EJ=mm(E,JI);JWJ=mm(tr(JI),mm(W,JI));H=[[I(t)*N[i][j]-G[i][j]+EJ[i][j]+EJ[j][i]-JWJ[i][j] for j in range(56)] for i in range(56)];pc=positive(H);assert pc
 upper=dict(hypothetical_high_floor=str(t),exact_trial_coefficients_J=[list(map(str,row)) for row in J],full_budget_positive_certificate=pc,actual_high_floor_established=False)
 # All old even packet tails are exactly recycled from the old three trials.
 Y=old['physical_high_trial_columns'];raw=[sparse(c) for c in Y];ids=sorted(set().union(*[set(a) for a in raw]));piv=None
 for ns in combinations(ids,3):
  try:V=exact_inverse([[c.get(n,F(0)) for c in raw] for n in ns]);piv=list(ns);break
  except StopIteration:pass
 assert piv
 even=packet['rows'][0];coeff=[]
 for c in even['columns']:
  h={n:v for n,v in sparse(c).items() if n>=112};a=[sum(V[i][j]*h.get(piv[j],F(0)) for j in range(3)) for i in range(3)]
  assert all(h.get(n,F(0))==sum(a[j]*raw[j].get(n,F(0)) for j in range(3)) for n in set(h)|set(ids));coeff.append(list(map(str,a)))
 recycle=dict(pivot_degrees=piv,exact_packet_tail_coefficients=coeff,all_56_packet_high_tails_in_old_trial_span=True)
 # Genuine extensions: three lowest even high modes, and three odd tested tails.
 evennew=[dict(indices=[n],coefficients=['1'],exact_mass_squared='1',kind='physical_Legendre') for n in (112,114,116)];odd=[]
 for i,c in enumerate(packet['rows'][1]['columns'][1:4],1):
  h={n:v for n,v in sparse(c).items() if n>=112};mass=sum(v*v for v in h.values());q=10**60;rt=isqrt((mass*q*q).numerator//(mass*q*q).denominator)+1;scale=F(rt,q);assert scale*scale>mass>0;values=[v/scale for v in h.values()]
  odd.append(dict(parent_packet_column=i,indices=list(h),coefficients=list(map(str,values)),original_high_mass_squared=str(mass),rational_normalization=str(scale),exact_mass_squared=str(sum(v*v for v in values))))
 frames=[]
 for par,oldcols,newcols,size in [('even',Y,evennew,59),('odd',[],odd,56)]:
  cols=oldcols+newcols;GG=gram(cols);gc=positive(GG);assert gc
  count=len(newcols);manifest=[[i,j] for j in range(size,size+count) for i in range(j+1)]
  frames.append(dict(parity=par,reused_source_dimension=size,reused_trial_count=len(oldcols),new_trial_columns=newcols,all_trial_columns=cols,physical_Gram=box(GG),physical_Gram_positive_certificate=gc,physical_trial_dimension=len(cols),new_source_upper_triangle=manifest,new_source_correlation_count=len(manifest),original_new_trial_sources_certified=False,new_response_credit_established=False))
 out=dict(stage='DNE51',parent=PARENT,input_paths=PATHS,input_sha256=[h for x,h in inp],original_aperture='53/50',actual_original_high_floor='647/1000',fixed_even_trial_obstructions=rows,hypothetical_even_sufficient_upper=upper,positive_region_shell_route_ceiling_upper=old['positive_region_shell_route_ceiling_upper'],fixed_even_trial_required_floor_lower='69/100',fixed_even_trial_sufficient_floor_upper='691/1000',old_even_trial_space_exhausted=True,even_packet_tail_recycling=recycle,proposed_source_extensions=frames,new_source_correlations_required=sum(x['new_source_correlation_count'] for x in frames),actual_certified_all_high_retained_dimension=109,uncovered_retained_dimension=3,source_integrals_recomputed=False,new_original_positivity_established=False,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,Lean=False)
 b=(json.dumps(out,indent=2)+'\n').encode();Path(output).write_bytes(base64.b64encode(gzip.compress(b,mtime=0))+b'\n');print('extension correlations',out['new_source_correlations_required'],flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);run(p.parse_args().output)
