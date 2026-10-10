#!/usr/bin/env python3
"""Independently pay the missing original source star and complete response gate."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,ast
import validate_cc105_selected_response as data
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc104_joint_response_rebase as response
import certify_cc101_next_source_packet as proof
from certify_cc108_dne41_integration import compress,rank
BASE=Path(__file__).resolve().parents[1];K=F(603,1000)
def run():
 checks=0;rows=[]
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def enclose(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
 # Preserve the already audited exact signed convolution algorithm.
 def astfn(p,name):return ast.dump(next(x for x in ast.parse((BASE/p).read_text()).body if isinstance(x,ast.FunctionDef) and x.name==name),include_attributes=False)
 check(astfn('scripts/certify_cc113_missing_source_star.py','packed_conv')==astfn('notes/cc110-source/scripts/certify_dne44_joint_source_Gram.py','packed_conv'))
 check(hashlib.sha256((BASE/'notes/cc101-source/scripts/dne23_dne16_source_input.py').read_bytes()).hexdigest()=='e4539b941f3768f177a469c68f58d34b11d3ea863247c14c1a6a59d81b2f91d8')
 sys_path=str(BASE/'notes/cc110-source/scripts')
 import sys
 if sys_path not in sys.path:sys.path.insert(0,sys_path)
 from dne44_integer_moment_dot import integer_dot
 for coeff in [[1,-2,3],[-7,0,5],[0,0,0]]:
  moments=[(-3,2),(7,11),(-13,-8)];check(integer_dot(coeff,moments)==(sum(min(z*x,z*y) for z,(x,y) in zip(coeff,moments)),sum(max(z*x,z*y) for z,(x,y) in zip(coeff,moments))))
 tr,th,_=data.read('notes/data/RPB108_CC112_PHYSICAL_RESPONSE_TRANSPORT_20261010.json.gz.b64');check(tr['status']=='PASS')
 fresh,fh,_=data.read('notes/data/RPB108_CC113_FRESH_HIGH_FLOOR_AUDIT_20261010.json');published,phigh,_=data.read('notes/cc113-source/notes/data/RPB108_DNE46_HIGH_FLOOR_VALIDATION_20261010.json');check({k:v for k,v in fresh.items() if k!='certificate_path'}=={k:v for k,v in published.items() if k!='certificate_path'});check(fresh['status']=='PASS' and F(fresh['original_infinite_F112_floor'])>=K)
 route,rh,_=data.read('notes/cc112-source/notes/data/RPB108_DNE45_SCALAR_ROUTE_LIMIT_20261010.json.gz.b64');routeaudit,_,_=data.read('notes/data/RPB108_CC112_SCALAR_ROUTE_CONSUMER_20261010.json');check(rh==routeaudit['DNE45_certificate_sha256'])
 for idx,p in enumerate(['even','odd']):
  up=p.upper();old=tr['parity_checks'][idx];packet,ph,_=data.read(f'notes/data/RPB108_CC113_{up}_PHYSICAL_PACKET_20261010.json');hp,hph,_=data.read(f'notes/data/RPB108_CC105_{up}_PHYSICAL_PACKET_20261010.json');cols=packet['columns'];n=len(cols)
  check(packet['input_sha256']==[th,hph] and hph==old['CC105_high_packet_sha256']);check(cols[1:]==hp['columns'][1:] and n==12-idx)
  v=dict(zip(old['high_residual_indices'],map(F,old['exact_missing_high_coefficients'])));check(dict(zip(cols[0]['indices'],map(F,cols[0]['coefficients'])))=={i:x for i,x in v.items() if x})
  pp=f'notes/data/RPB108_CC113_{up}_SOURCE_PRIMARY_20261010.json';rp=f'notes/data/RPB108_CC113_{up}_SOURCE_REPLAY_20261010.json';a,ah,_=data.read(pp);s,ss,_=data.read(rp)
  check((a['regular_order'],a['precision'],s['regular_order'],s['precision'])==(360,760,400,800))
  for src in [a,s]:
   check(src['stage']=='CC113' and src['certificate_sha256']==src['normalized_packet_sha256']==ph and src['joint_packet_input_sha256']==packet['input_sha256']);check(src['complete_original_source_action'] and src['exact_endpoint_logs'] and src['all_six_primes_both_orientations'] and src['complete_missing_source_star_and_diagonals_certified'] and not src['sampled_quadrature']);check(src['retained_projection_indices']==list(range(idx,112,2)))
   eta=F(src['uniform_original_source_operator_error_upper']);check(eta>=2*F(53,50)*F(550,19)*F(106,125)**src['regular_order']+F(3,10**99));sq=F(src['physical_interval_sqrt_upper']);ln=F(src['complete_log_norm_upper']);check(sq**2>=2*F(53,50) and ln**2>=F(src['complete_log_squared_norm'][1]))
   coords=c.matrix(src['retained_rounded_source_coordinates']);errors=list(map(F,src['source_L2_error_upper']));norms=list(map(F,src['projected_source_norm_upper']))
   for i,col in enumerate(cols):
    mass=sum(F(x)**2 for x in col['coefficients']);pn=F(col['norm_upper']);check(mass==F(src['exact_masses'][i])==F(col['exact_mass_squared']) and pn==F(src['physical_norm_upper'][i]) and pn**2>mass);check(len(coords[i])==56)
    pe=list(map(F,src['panel_regular_polynomial_sup_error_upper'][i]));check(len(pe)==7);rounding=F(src['polynomial_rounding_source_L2_error_upper'][i]);check(rounding>=sq*max(pe)+F(src['logarithmic_polynomial_sup_error_upper'][i])*ln/2);check(errors[i]>=eta*pn+rounding)
    for j in range(n):
     if i!=0 and j!=0 and i!=j:
      check(src['original_projected_source_Gram'][i][j] is None);continue
     whole=c.iv(src['complete_rounded_source_Gram'][i][j]);raw=c.sub(whole,c.sumiv(c.mul(x,y) for x,y in zip(coords[i],coords[j])));check(raw==c.iv(src['projected_rounded_source_Gram'][i][j]));payment=F(src['source_Gram_error_payments'][i][j]);check(payment>=errors[i]*norms[j]+errors[j]*norms[i]+errors[i]*errors[j]);check(c.add(raw,(-payment,payment))==c.iv(src['original_projected_source_Gram'][i][j]));check(norms[i]**2>F(src['projected_rounded_source_Gram'][i][i][1]))
  for i in range(n):
   for j in range(n):
    if i==0 or j==0 or i==j:enclose(c.iv(a['original_projected_source_Gram'][i][j]),c.iv(s['original_projected_source_Gram'][i][j]))
  h,hh,_=data.read(f'notes/cc104-source/notes/data/RPB108_NF52_{up}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64');check(hh==old['NF52_high_certificate_sha256']);M,QY,GY=[c.matrix(h[key]) for key in ['enlarged_high_physical_Gram','enlarged_high_native_Gram','enlarged_high_complete_source_Gram']]
  for j in range(n-1):check(c.overlap(c.iv(s['original_projected_source_Gram'][j+1][j+1]),GY[j][j]))
  C=r.sub(QY,r.scale(M,K));N=r.sub(r.scale(GY,1/K),QY);_,cp=proof.proof(C,old['current_floor_high_controls']['surplus_proof']['frozen_rational_congruence']);_,np=proof.proof(N,old['current_floor_high_controls']['denominator_proof']['frozen_rational_congruence']);NI,rho=response.inverse(N);check(rho<1)
  known=c.matrix(old['known_signed_response_cross_part']);t=list(map(F,old['missing_high_transport_row_t']));gv=list(map(c.iv,s['original_projected_source_Gram'][0][1:]));W=[[r.compact(c.add(x,c.mul(c.iv(t[i]),gv[j]))) for j,x in enumerate(row)] for i,row in enumerate(known)]
  original,os,_=data.read(f'notes/cc110-source/notes/data/RPB108_DNE44_{up}_JOINT_SOURCE_REPLAY_20261010.json.gz.b64');check(os==old['DNE44_source_replay_sha256']);Q=c.matrix(original['native_block']);G=c.matrix(original['original_projected_source_Gram']);plain=r.sub(Q,r.scale(G,1/K));gain=r.scale(r.mm(r.mm(W,NI),c.transpose(W)),1/K**2);lower=[[r.compact(c.add(x,y)) for x,y in zip(a,b)] for a,b in zip(plain,gain)];lower=[[(min(lower[i][j][0],lower[j][i][0]),max(lower[i][j][1],lower[j][i][1])) for j in range(44)] for i in range(44)]
  try:sign=response.sign(lower)
  except AssertionError:sign=dict(status='UNRESOLVED',reason='midpoint-positive proposal did not yield a paid positive congruence')
  cert,ch,_=data.read(f'notes/cc110-source/notes/data/RPB108_DNE44_{up}_POSITIVE_SUBSPACE_20261010.json.gz.b64');B=[list(map(F,row)) for row in cert['positive_embedding_B']];D=[list(map(F,row)) for row in cert['negative_comparison_embedding_D']];J=[b+d for b,d in zip(B,D)];joined=compress(lower,J);nb=len(B[0]);z=len(D[0]);gate_status='UNRESOLVED';gate=[];gate_proof=None
  try:
   AP=[row[:nb] for row in joined[:nb]];_,ap=proof.proof(AP);AI,arho=response.inverse(AP);E=[row[nb:] for row in joined[:nb]];FD=[row[nb:] for row in joined[nb:]];gate=r.sub(FD,r.mm(c.transpose(E),r.mm(AI,E)));gate_sign=response.sign(gate);gate_status=gate_sign['status'];gate_proof=gate_sign
  except AssertionError:pass
  trials=[]
  candidates=[('D'+str(j),[D[i][j] for i in range(44)]) for j in range(z)]
  rr=next(x for x in route['rows'] if x['parity']==p);plain_trial=list(map(F,rr['exact_trial']));plain_rejection=c.sub(c.quad(Q,plain_trial),c.mul(c.quad(G,plain_trial),c.iv(1/K)));candidates.append(('DNE45_full_plain_trial',plain_trial))
  if 'witness' in sign:candidates.append(('full_midpoint_probe',list(map(F,sign['witness']))))
  for label,x in candidates:
   q=c.quad(Q,x);g=c.quad(G,x);wx=c.mm([[c.iv(v) for v in x]],W);credit=c.mul(c.mm(c.mm(wx,NI),c.transpose(wx))[0][0],c.iv(1/K**2));pv=c.sub(q,c.mul(g,c.iv(1/K)));rv=c.add(pv,credit);status='POSITIVE' if rv[0]>0 else 'REJECTED' if rv[1]<0 else 'UNRESOLVED';trials.append(dict(label=label,exact_trial=list(map(str,x)),plain_value=c.pair(pv),response_credit=c.pair(credit),response_value=c.pair(rv),response_status=status))
  check(rank([list(map(F,row)) for row in old['Native_trial_transport_C']])==44)
  mass=sum(map(F,original['exact_masses']));trace=sum(G[i][i][1] for i in range(44));check(mass>0 and trace>0);gap=None
  if sign['status']=='POSITIVE':
   d=F(sign['floor']);gap=min(d/(4*(mass+trace/K**2)),K/2);check(gap>F(1,10**37))
  rows.append(dict(parity=p,physical_packet_sha256=ph,source_primary_sha256=ah,source_replay_sha256=ss,NF52_high_certificate_sha256=hh,original_DNE44_source_sha256=os,CC112_transport_sha256=th,high_surplus_proof=cp,high_denominator_proof=np,inverse_residual_upper=str(rho),missing_complete_source_row=[c.pair(x) for x in gv],complete_signed_response_rows=[[c.pair(x) for x in row] for row in W],full_plain_trial_value=c.pair(plain_rejection),full_plain_criterion_rejected=plain_rejection[1]<0,full_response_sign=sign,direct_deficit_gate_interval_status=gate_status,deficit_gate_positive_by_full_packet_congruence=sign['status']=='POSITIVE',paid_direct_deficit_gate=[[c.pair(x) for x in row] for row in gate],direct_deficit_gate_proof=gate_proof,trials=trials,fresh_exact_retained_rank=44,exact_physical_mass_sum=str(mass),complete_source_trace_upper=str(trace),all_high_physical_gap_lower=str(gap) if gap else None,full_packet_response_positive=sign['status']=='POSITIVE',strict_same_floor_full_packet_separation_proved=sign['status']=='POSITIVE' and plain_rejection[1]<0,actual_original_negative_form_claimed=False))
  print(p,'full response',sign['status'],'gate',gate_status,'trials',[(x['label'],x['response_status']) for x in trials],flush=True)
 return dict(milestone='CC113',status='PASS',parent='ae22b710d37cdac6e4c8c60d387b0f2e6ee1b2a0',original_high_floor=str(K),fresh_current_high_floor_audit_sha256=fh,certified_current_original_high_floor=fresh['original_infinite_F112_floor'],exact_rational_consumer_checks=checks,parity_checks=rows,fresh_complete_missing_source_integrations=True,complete_collective_response_arithmetic_fresh=True,strict_full_packet_collective_separation_proved=any(x['strict_same_floor_full_packet_separation_proved'] for x in rows),integrated_retained_rank=88 if all(x['full_packet_response_positive'] for x in rows) else None,uncovered_retained_dimension=24 if all(x['full_packet_response_positive'] for x in rows) else None,all_high_physical_gap_guard=str(F(1,10**37)) if all(x['full_packet_response_positive'] for x in rows) else None,prior_DNE46_87_direction_span_contained=all(x['full_packet_response_positive'] for x in rows),computational_saving_proved=False,physical_domain_attachment_inherited=True,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--floor',choices=['603/1000','647/1000'],default='603/1000');a=p.parse_args();K=F(a.floor);Path(a.output).write_text(json.dumps(run(),indent=2)+'\n')
