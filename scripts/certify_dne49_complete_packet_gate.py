#!/usr/bin/env python3
"""Complete frozen packet, finite native certificate and paid trial pairings."""
from pathlib import Path
from fractions import Fraction as F
import json,base64,gzip,argparse
from certify_dne39_signed_comparison import read,matrix,positive
from certify_dne32_native_remainder import I,mm
from materialize_dne44_joint_sources import run as prefix
from materialize_dne32_normalized_sources import run as remainder
from materialize_dne48_trial_sources import run as trial_packet
from validate_dne34_source_block import sum_box,mul
PARENT='514386d14dcb1dc1bb2d469bc82a728d8de4b12d'

def determinant(A):
 B=[r[:] for r in A];d=F(1);n=len(B)
 for i in range(n):
  p=next(j for j in range(i,n) if B[j][i])
  if p!=i:B[p],B[i]=B[i],B[p];d=-d
  pivot=B[i][i];d*=pivot
  for j in range(i+1,n):
   r=B[j][i]/pivot
   for k in range(i,n):B[j][k]-=r*B[i][k]
 return d

def packet(parity,tmp):
 cp=f'notes/data/RPB108_DNE32_{parity.upper()}_NATIVE_REMAINDER_CERTIFICATE_20261009.json.gz.b64'
 prefix(cp,tmp);old,oh=read(tmp);remainder(cp,tmp);rem,rh=read(tmp);Path(tmp).unlink();c,ch=read(cp);native,nh=read(c['input_paths'][1]);frame,fh=read(c['input_paths'][2]);selected,sh=read(native['input_paths'][2]);assert [nh,fh]==c['input_sha256'][1:3] and sh==native['input_sha256'][2]
 A=matrix(c['tightened_scaled_T4_native_matrix']);P=matrix(c['tightened_scaled_T4_W52_border']);J=[list(map(F,r)) for r in frame['frozen_scaled_projection_J']];U=[list(map(F,r)) for r in c['exact_rational_congruence_U']];AJ=mm(A,J);E=[[p-q for p,q in zip(r,s)] for r,s in zip(P,AJ)];cross=mm(E,U);C=matrix(c['congruence_matrix']);N=[[I(0) for j in range(56)] for i in range(56)]
 for i in range(4):
  for j in range(4):N[i][j]=A[i][j]
  for j in range(52):N[i][j+4]=N[j+4][i]=cross[i][j]
 for i in range(52):
  for j in range(52):N[i+4][j+4]=C[i][j]
 cols=old['columns'][:4]+rem['columns'];assert cols[:44]==old['columns'];assert [[x.box() for x in r[:44]] for r in N[:44]]==old['native_matrix']
 return dict(parity=parity,certificate_path=cp,certificate_sha256=ch,prior_packet_sha256=oh,remainder_packet_sha256=rh,input_sha256=[ch,nh,fh,sh],columns=cols,column_labels=old['column_labels']+[f'X{i}' for i in range(40,52)],native_matrix=[[x.box() for x in r] for r in N]),(native,frame,selected,c)

def run(output):
 deps=['notes/data/RPB108_DNE48_TRIAL_SOURCE_REPLAY_20261010.json.gz.b64','notes/data/RPB108_DNE48_TRIAL_SOURCE_VALIDATION_20261010.json','notes/data/RPB108_DNE48_RESIDUAL_RESPONSE_20261010.json.gz.b64','notes/data/RPB108_DNE48_RESIDUAL_RESPONSE_VALIDATION_20261010.json','notes/data/RPB108_DNE32_NATIVE_REMAINDER_VALIDATION_20261009.json'];inp=[read(p) for p in deps];s,sv,response,rv,nv=[x for x,h in inp];assert sv['status']==rv['status']==nv['status']=='PASS' and sv['replay_sha256']==inp[0][1] and rv['certificate_sha256']==inp[2][1]
 rows=[]
 for parity in ['even','odd']:
  z,(n,frame,selected,c)=packet(parity,output+'.tmp');proof=positive(matrix(z['native_matrix']));assert proof is not None
  proof.pop('original_matrix');proof['original_matrix_reference']='native_matrix';z['finite_native_positive_certificate']=proof
  ids=n['retained_indices'];T=[{ids[0]:F(1)}]+[dict(zip(col['indices'],map(F,col['coefficients']))) for col in selected['columns']];W=[list(map(F,col)) for col in n['exact_W_columns']]
  # Orthogonal complement has a literal 52x52 identity minor.
  for i in range(52):
   assert all(W[j][4+i]==F(i==j) for j in range(52))
  for t in T:
   assert all(sum(t.get(k,F(0))*v for k,v in zip(ids,w))==0 for w in W)
  # The first four coordinates of T4 have a nonsingular exact minor.
  top=[[t.get(k,F(0)) for t in T] for k in ids[:4]]
  td=determinant(top);assert td!=0
  U=[list(map(F,r)) for r in c['exact_rational_congruence_U']];assert all(U[i][i]!=0 and all(U[i][j]==0 for j in range(i)) for i in range(52))
  z['retained_rank_gate']=dict(rank=56,T4_pivot_matrix=[list(map(str,r)) for r in top],T4_pivot_determinant=str(td),W_identity_minor_rows=list(range(4,56)),orthogonality_exact=True,U_upper_triangular_invertible=True)
  if parity=='even':
   trial_packet(s['certificate_path'],output+'.tmp');tp,th=read(output+'.tmp');Path(output+'.tmp').unlink();assert th==s['normalized_packet_sha256'];z['source_columns']=tp['columns']+z['columns'][44:];z['reused_source_count']=47;z['native_to_source']=list(range(44))+list(range(47,59));z['trial_source_indices']=[44,45,46]
   coords=[dict(zip(s['trial_action_coordinate_indices'],[tuple(map(F,b)) for b in r])) for r in s['trial_rounded_action_coordinates']];errors=list(map(F,s['source_L2_error_upper']));M=[]
   for col in z['columns']:
    row=[]
    for j in range(3):
     v=sum_box(mul((F(a),F(a)),coords[j][k]) for k,a in zip(col['indices'],col['coefficients']));pay=errors[44+j]*F(col['norm_upper']);row.append([str(v[0]-pay),str(v[1]+pay)])
    M.append(row)
   assert M[:44]==[[response['trial_native_pairings'][j][i] for j in range(3)] for i in range(44)];z['paid_full_trial_native_M']=M;z['new_trial_native_pairing_count']=36
  else:
   z['source_columns']=z['columns'];z['reused_source_count']=44;z['native_to_source']=list(range(56));z['trial_source_indices']=[]
  count=len(z['source_columns']);old=z['reused_source_count'];z['missing_source_upper_triangle']=[[i,j] for i in range(count) for j in range(i,count) if j>=old];z['missing_source_correlation_count']=len(z['missing_source_upper_triangle']);z['source_column_labels']=[z['column_labels'][i] for i in range(44)]+(['Y0','Y1','Y2'] if parity=='even' else [])+z['column_labels'][44:];z['high_trial_columns']=z['source_columns'][44:47] if parity=='even' else [];z.pop('source_columns');rows.append(z);print(parity,'native56 PASS; missing source correlations',z['missing_source_correlation_count'],flush=True)
 out=dict(stage='DNE49',parent=PARENT,input_paths=deps,input_sha256=[h for x,h in inp],rows=rows,complete_retained_packet_dimension=112,finite_native_packet_positive=True,remaining_trial_native_pairings_paid=36,missing_source_correlation_count=sum(r['missing_source_correlation_count'] for r in rows),actual_certified_all_high_retained_dimension=88,uncovered_retained_dimension=24,new_source_integrals_computed=False,complete_remaining_source_Gram_certified=False,full_remaining_response_budget_evaluated=False,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,Lean=False)
 b=(json.dumps(out,indent=2)+'\n').encode();Path(output).write_bytes(base64.b64encode(gzip.compress(b,mtime=0))+b'\n')
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--output',required=True);run(a.parse_args().output)
