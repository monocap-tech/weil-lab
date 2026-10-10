#!/usr/bin/env python3
"""Exact Z44 to Native+paid-high transport with one new high residual."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,json,os,subprocess,sys,gzip,base64
import validate_cc105_selected_response as data
from certify_cc108_dne41_integration import rank
import certify_cc81_boundary_response_consumer as c
import certify_cc104_joint_response_rebase as response
BASE=Path(__file__).resolve().parents[1]
def sparse(col):return dict(zip(col['indices'],map(F,col['coefficients'])))
def pivots(rows):
 M=[list(x) for x in rows];out=[];n=0
 for i in range(len(M[0])):
  j=next((j for j in range(n,len(M)) if M[j][i]),None)
  if j is None:continue
  M[n],M[j]=M[j],M[n];v=M[n][i]
  for j in range(n+1,len(M)):
   if M[j][i]:
    a=M[j][i]/v;M[j]=[x-a*y for x,y in zip(M[j],M[n])]
  out.append(i);n+=1
  if n==len(M):break
 return out
def solve(A,R):
 n=len(A);M=[list(a)+list(b) for a,b in zip(A,R)]
 for k in range(n):
  j=next(j for j in range(k,n) if M[j][k]);M[k],M[j]=M[j],M[k];v=M[k][k];M[k]=[x/v for x in M[k]]
  for j in range(n):
   if j!=k and M[j][k]:
    a=M[j][k];M[j]=[x-a*y for x,y in zip(M[j],M[k])]
 return [x[n:] for x in M]
def run():
 checks=0;out=[]
 def check(v):
  nonlocal checks
  assert v;checks+=1
 frame,fh,_=data.read('notes/cc104-source/notes/data/RPB108_NF47_FLOOR_TRANSPORT_CERTIFICATE_20261009.json')
 standing,sh,_=data.read('notes/data/RPB108_CC111_RESPONSE_DEFICIT_GATE_20261010.json');check(standing['status']=='PASS' and standing['integrated_retained_rank']==85)
 env=dict(os.environ);env['PYTHONPATH']=str(BASE/'notes/cc110-source/scripts')+os.pathsep+str(BASE/'notes/cc101-source/scripts')
 for idx,p in enumerate(['even','odd']):
  up=p.upper();s,ss,_=data.read(f'notes/cc110-source/notes/data/RPB108_DNE44_{up}_JOINT_SOURCE_REPLAY_20261010.json.gz.b64');packet_path=BASE/'work'/f'cc112-{p}-packet.json'
  subprocess.run([sys.executable,str(BASE/'notes/cc110-source/scripts/materialize_dne44_joint_sources.py'),s['certificate_path'],str(packet_path)],cwd=BASE/'notes/cc101-source',env=env,check=True,capture_output=True)
  packet,ph,_=data.read(str(packet_path));check(ph==s['normalized_packet_sha256']);raw=[sparse(x) for x in packet['columns']]
  fr=frame['parity_frames'][idx];joined=[sparse(x) for x in fr['unchanged_joined_columns']];low=fr['retained_indices'];check(low==list(range(idx,112,2)))
  for i in range(3):
   for j in range(i):check(sum(joined[i].get(k,F(0))*joined[j].get(k,F(0)) for k in low)==0)
  mass=[sum(x.get(i,F(0))**2 for i in low) for x in joined];pv=fr['old_two_constraint_pivots']+[fr['old_free_coordinates'][fr['third_constraint_pivot_in_old_free_coordinates']]];free=[i for i in fr['old_free_coordinates'] if i!=pv[2]];check(len(free)==53)
  # Construct each retained-only constraint vector independently.
  A=[[x.get(low[i],F(0)) for i in pv] for x in joined];R=[[-x.get(low[i],F(0)) for i in free] for x in joined];sol=solve(A,R);remaining=[]
  for j,i in enumerate(free):
   col={low[i]:F(1)}
   for k,q in enumerate(pv):col[low[q]]=sol[k][j]
   remaining.append(col)
  native=joined+remaining
  hp,hph,_=data.read(f'notes/data/RPB108_CC105_{up}_PHYSICAL_PACKET_20261010.json');Y=[sparse(x) for x in hp['columns'][1:]];check(len(Y)==11-idx and all(min(x)>=112 for x in Y))
  ids=sorted({i for x in raw+native+Y for i in x if i>=112});C=[];residual=[]
  for col in raw:
   alpha=[sum(col.get(i,F(0))*x.get(i,F(0)) for i in low)/m for x,m in zip(joined,mass)]
   beta=[col.get(low[i],F(0))-sum(a*x.get(low[i],F(0)) for a,x in zip(alpha,joined)) for i in free];v=alpha+beta;C.append(v)
   for i in low:check(sum(a*x.get(i,F(0)) for a,x in zip(v,native))==col.get(i,F(0)))
   residual.append([col.get(i,F(0))-sum(a*x.get(i,F(0)) for a,x in zip(alpha,joined)) for i in ids])
  high=[[x.get(i,F(0)) for i in ids] for x in Y];r=rank(high);check(r==len(Y))
  first=next(i for i,x in enumerate(residual) if rank(high+[x])>r);v=residual[first];basis=high+[v];check(rank(basis+residual)==r+1)
  pp=pivots(basis);check(len(pp)==r+1);minor=[[row[i] for row in basis] for i in pp];rhs=[[row[i] for row in residual] for i in pp];coeff=solve(minor,rhs)
  for j,col in enumerate(residual):
   for i,value in enumerate(col):check(sum(basis[k][i]*coeff[k][j] for k in range(r+1))==value)
  mm=sum(x*x for x in v);scale=10**160;root=F(isqrt(mm.numerator*scale**2//mm.denominator)+1,scale);check(root**2>mm>0)
  h,hh,_=data.read(f'notes/cc104-source/notes/data/RPB108_NF52_{up}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64');paid,_,_=data.read('notes/data/RPB108_CC105_SELECTED_RESPONSE_VALIDATION_20261010.json');check(hh==paid['parity_checks'][idx]['original_NF52_certificate_decoded_sha256'])
  M,QY,GY,BN,SN=[c.matrix(h[key]) for key in ['enlarged_high_physical_Gram','enlarged_high_native_Gram','enlarged_high_complete_source_Gram','enlarged_joint_high_native_crosses','enlarged_joint_high_complete_source_crosses']];check(len(M)==len(QY)==len(GY)==r and len(BN)==len(SN)==56)
  for i,a in enumerate(Y):
   for j,b in enumerate(Y):
    exact=sum(x*b.get(k,F(0)) for k,x in a.items());check(M[i][j][0]<=exact<=M[i][j][1])
  k=F(603,1000);surplus=response.r.sub(QY,response.r.scale(M,k));denominator=response.r.sub(response.r.scale(GY,1/k),QY)
  try:
   _,cp=response.proof.proof(surplus);_,np=response.proof.proof(denominator);_,rho=response.inverse(denominator);high_status='PASS';high_controls=dict(surplus_proof=cp,denominator_proof=np,inverse_residual_upper=str(rho))
  except AssertionError:
   high_status='UNRESOLVED';high_controls={}
  # r is the high dimension here; the response module provides paid matrix products.
  CI=[[c.iv(x) for x in row] for row in C];DI=[[c.iv(coeff[i][j]) for i in range(r)] for j in range(44)]
  WK=response.r.sub(SN,response.r.scale(BN,k));HY=response.r.sub(GY,response.r.scale(QY,k));known=response.r.mm(CI,WK);add=response.r.mm(DI,HY);known=[[response.r.compact(c.add(a,b)) for a,b in zip(x,y)] for x,y in zip(known,add)]
  primary,primarysha,_=data.read(f'notes/data/RPB108_CC105_{up}_SOURCE_PRIMARY_20261010.json');replay,replaysha,_=data.read(f'notes/data/RPB108_CC105_{up}_SOURCE_REPLAY_20261010.json');pr=paid['parity_checks'][idx];check(primarysha==pr['primary_decoded_sha256'] and replaysha==pr['replay_decoded_sha256']);check(primary['normalized_packet_sha256']==replay['normalized_packet_sha256']==hph)
  native_rows=[]
  for src in [primary,replay]:
   values=[]
   for j in range(r):
    coords=list(map(c.iv,src['complete_source_coordinates'][j+1]));check(all((degree-idx)//2<len(coords) for degree,value in zip(ids,v) if value));approx=c.sumiv(c.mul(c.iv(value),coords[(degree-idx)//2]) for degree,value in zip(ids,v) if value);pay=F(src['source_L2_error_upper'][j+1])*root;values.append(c.add(approx,(-pay,pay)))
   native_rows.append(values)
  qv=native_rows[1]
  for a,b in zip(*native_rows):check(a[0]<=b[0]<=b[1]<=a[1])
  known=[[response.r.compact(c.sub(x,c.mul(c.iv(k*coeff[-1][i]),qv[j]))) for j,x in enumerate(row)] for i,row in enumerate(known)]
  out.append(dict(parity=p,DNE44_source_replay_sha256=ss,raw_physical_packet_sha256=ph,NF47_frame_sha256=fh,CC105_high_packet_sha256=hph,NF52_high_certificate_sha256=hh,CC105_primary_source_sha256=primarysha,CC105_replay_source_sha256=replaysha,recovered_native_residual_high_row=[c.pair(x) for x in qv],native_residual_high_primary_replay_containment_verified=True,current_floor_high_controls_status=high_status,current_floor_high_controls=high_controls,known_signed_response_cross_part=[[c.pair(x) for x in row] for row in known],known_part_includes_residual_native_crosses=True,Native_trial_dimension=56,paid_high_dimension=r,high_residual_augmented_rank=r+1,missing_high_dimension=1,first_outside_high_span_column=first,high_residual_indices=ids,exact_missing_high_coefficients=list(map(str,v)),exact_missing_high_mass_squared=str(mm),missing_high_physical_norm_upper=str(root),Native_trial_transport_C=[list(map(str,row)) for row in zip(*C)],paid_high_transport_D=[list(map(str,row)) for row in coeff[:-1]],missing_high_transport_row_t=list(map(str,coeff[-1])),exact_all_physical_columns_reconstructed=True,missing_native_cross_count=0,missing_complete_source_cross_count=r,missing_residual_self_source_needed=False,actual_response_credit_computed=False))
  print(p,'exact physical transport: 56 Native +',r,'paid high + one missing high;',r,'source crosses remain, native row recovered',flush=True)
 return dict(milestone='CC112',status='PASS',parent='052f9f57dad673c19b58364c04fef86530fec487',CC111_standing_sha256=sh,exact_physical_checks=checks,parity_checks=out,source_integrals_recomputed=False,actual_response_credit_computed=False,integrated_retained_rank=85,uncovered_retained_dimension=27,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();payload=(json.dumps(run(),indent=2)+'\n').encode();Path(a.output).write_bytes(base64.b64encode(gzip.compress(payload,mtime=0))+b'\n' if a.output.endswith('.gz.b64') else payload)
