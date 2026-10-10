#!/usr/bin/env python3
"""Audit source payments, independent response replay and the mixed positive chart."""
from pathlib import Path
from fractions import Fraction as F
import json,argparse
import validate_cc105_selected_response as data
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc101_next_source_packet as proof
from certify_cc108_dne41_integration import compress,rank
K=F(647,1000)
def run(output):
 checks=0
 def check(x):
  nonlocal checks
  assert x;checks+=1
 def contains(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
 gp='notes/data/RPB108_CC117_COMPLETE_RESPONSE_GATE_20261010.json.gz.b64';rp='notes/data/RPB108_CC117_COMPLETE_RESPONSE_REPLAY_20261010.json.gz.b64';bp='notes/data/RPB108_CC117_POSITIVE_PACKET_20261010.json'
 a,ah,_=data.read(gp);b,bh,_=data.read(rp);positive,ph,_=data.read(bp);check(a['status']==b['status']==positive['status']=='PASS');check(b['producer_decoded_sha256']==ah and b['independent_entrywise_reassembly']);check(positive['gate_decoded_sha256']==ah)
 sv,svh,_=data.read('notes/cc117-source/notes/data/RPB108_DNE50_COMPLETE_SOURCE_VALIDATION_20261010.json');check(sv['status']=='PASS' and svh==a['DNE50_source_validation_sha256'])
 packet,pkh,_=data.read('notes/cc116-source/notes/data/RPB108_DNE49_COMPLETE_PACKET_GATE_20261010.json.gz.b64');check(pkh==a['DNE49_packet_decoded_sha256'])
 old,oh,_=data.read('notes/cc117-source/notes/data/RPB108_DNE50_POSITIVE_SUBSPACES_20261010.json.gz.b64');ov,ovh,_=data.read('notes/cc117-source/notes/data/RPB108_DNE50_POSITIVE_SUBSPACE_VALIDATION_20261010.json');check(ov['status']=='PASS' and ov['certificate_sha256']==oh==positive['DNE50_positive_subspaces_decoded_sha256'] and ovh==positive['DNE50_positive_validation_sha256'])
 dne,dh,_=data.read('notes/cc117-source/notes/data/RPB108_DNE50_FULL_RESPONSE_20261010.json.gz.b64');dv,dvh,_=data.read('notes/cc117-source/notes/data/RPB108_DNE50_FULL_RESPONSE_VALIDATION_20261010.json');check(dv['status']=='PASS' and dv['certificate_sha256']==dh==positive['DNE50_full_response_decoded_sha256'] and dvh==positive['DNE50_full_response_validation_sha256'])
 tr,th,_=data.read('notes/data/RPB108_CC116_COMPLETE_RESPONSE_TRANSPORT_20261010.json.gz.b64');tv,tvh,_=data.read('notes/data/RPB108_CC116_COMPLETE_RESPONSE_VALIDATION_20261010.json');check(tv['status']=='PASS' and tv['certificate_decoded_sha256']==th==a['CC116_decoded_sha256'] and tvh==a['CC116_validation_sha256'])
 hi,hih,_=data.read('notes/data/RPB108_CC113_FRESH_HIGH_FLOOR_AUDIT_20261010.json');check(hi['status']=='PASS' and hih==a['current_high_floor_audit_sha256'] and F(hi['original_infinite_F112_floor'])>=K)
 rows=[]
 for idx,p in enumerate(['even','odd']):
  z=a['parity_checks'][idx];re=b['parity_checks'][idx];pos=positive['parity_checks'][idx];src,sh,_=data.read(f'notes/cc117-source/notes/data/RPB108_DNE50_{p.upper()}_COMPLETE_SOURCE_20261010.json.gz.b64');check(sh==sv['rows'][idx]['primary_sha256']==z['source_decoded_sha256']);check(src['parity']==p and z['parity']==p)
  mapping=src['native_to_source'];check(mapping==z['native_to_source']==tr['parity_checks'][idx]['source_native_map']);check(src['native_block']==packet['rows'][idx]['native_matrix']);check(src['retained_projection_indices']==list(range(idx,112,2)))
  full=c.matrix(src['complete_rounded_source_Gram']);coords=c.matrix(src['retained_rounded_source_coordinates']);proj=c.matrix(src['projected_rounded_source_Gram']);G=c.matrix(src['original_projected_source_Gram']);n=len(full);check(n==59-3*idx and all(len(row)==56 for row in coords));errors=list(map(F,src['source_L2_error_upper']));roots=list(map(F,src['projected_source_norm_upper']))
  eta=F(src['uniform_original_source_operator_error_upper']);check(eta>=2*F(53,50)*F(550,19)*F(106,125)**src['regular_order']+F(3,10**99));sq=F(src['physical_interval_sqrt_upper']);ln=F(src['complete_log_norm_upper']);check(sq*sq>=F(53,25) and ln*ln>=F(src['complete_log_squared_norm'][1]))
  for i in range(n):
   check(roots[i]**2>proj[i][i][1]);rounding=F(src['polynomial_rounding_source_L2_error_upper'][i]);check(rounding>=sq*max(map(F,src['panel_regular_polynomial_sup_error_upper'][i]))+ln*F(src['logarithmic_polynomial_sup_error_upper'][i])/2);check(errors[i]>=eta*F(src['physical_norm_upper'][i])+rounding)
   for j in range(n):
    check(G[i][j]==G[j][i] and full[i][j]==full[j][i]);raw=c.sub(full[i][j],c.sumiv(c.mul(x,y) for x,y in zip(coords[i],coords[j])));check(raw==proj[i][j]);pay=F(src['source_Gram_error_payments'][i][j]);check(pay>=errors[i]*roots[j]+errors[j]*roots[i]+errors[i]*errors[j]);check(G[i][j]==c.add(raw,(-pay,pay)))
  for i,s in enumerate(mapping):
   col=packet['rows'][idx]['columns'][i];mass=sum(F(x)**2 for x in col['coefficients']);check(mass==F(src['exact_masses'][s])==F(col['exact_mass_squared']));check(F(src['physical_norm_upper'][s])**2>mass)
  Q=c.matrix(src['native_block']);GG=[[G[i][j] for j in mapping] for i in mapping];plain=r.sub(Q,r.scale(GG,1/K));check(plain==c.matrix(z['paid_plain_comparison']))
  for key in ['frozen_H','high_decoded_sha256','source_decoded_sha256','native_to_source','matrix_dimension','trial_dimension']:check(z[key]==re[key])
  for X,Y in zip(c.matrix(z['paid_response_credit']),c.matrix(re['paid_response_credit'])):
   for x,y in zip(X,Y):contains(x,y)
  S=c.matrix(z['paid_response_comparison']);RS=c.matrix(re['paid_response_comparison'])
  for i in range(56):
   for j in range(56):check(S[i][j]==S[j][i]);contains(S[i][j],RS[i][j]);contains(S[i][j],c.add(plain[i][j],c.iv(z['paid_response_credit'][i][j])))
  B=[list(map(F,row)) for row in pos['positive_embedding_B']];dim=len(B[0]);check(dim==[55,56][idx]);prior=[list(map(F,row)) for row in old['rows'][idx]['positive_embedding_B']]
  if idx==0:
   check(B==prior and rank([row[44:] for row in B[44:]])==11);M=r.scale(c.matrix(dne['rows'][idx]['paid_response_budget']),1/K)
   failure=pos['CC_even_restriction_to_DNE50_positive_span'];v=list(map(F,failure['witness']));check(c.quad(compress(S,B),v)[1]<0)
   vec=list(map(F,z['full_response_sign']['witness']));check(c.quad(S,vec)[1]<0 and c.quad(RS,vec)[1]<0)
  else:
   check(B==[[F(i==j) for j in range(56)] for i in range(56)]);M=S;f,fp=proof.proof(S,z['full_response_sign']['proof']['frozen_rational_congruence']);check(f>=F(z['full_response_sign']['floor']));v=list(map(F,pos['strict_collective_separation_trial']));check(c.quad(plain,v)[1]<0 and c.quad(S,v)[0]>0)
   check(all(sum(B[i][k]*prior[k][j] for k in range(56))==prior[i][j] for i in range(56) for j in range(54)))
  d,pc=proof.proof(compress(M,B),pos['positive_proof']['frozen_rational_congruence']);check(d>=F(pos['coefficient_floor']));bf=sum(x*x for row in B for x in row);check(bf==F(pos['embedding_Frobenius_squared']));mass=F(old['rows'][idx]['original_packet_physical_mass']) if idx==0 else sum(F(src['exact_masses'][i]) for i in mapping);trace=F(old['rows'][idx]['original_projected_source_trace_upper']) if idx==0 else sum(GG[i][i][1] for i in range(56));check(mass*bf==F(pos['physical_packet_mass_upper']) and trace*bf==F(pos['projected_source_trace_upper']));gap=min(d/(4*bf*(mass+trace/K**2)),K/2);check(gap>=F(pos['physical_gap_lower'])>F(positive['physical_guard']));rows.append(dict(parity=p,positive_retained_rank=dim,source_payment_entries_rechecked=n*n,physical_gap_lower=str(gap)))
 check(positive['integrated_positive_retained_rank']==111 and positive['uncovered_retained_dimension']==1 and not positive['whole_aperture_positive'])
 out=dict(milestone='CC117',status='PASS',exact_rational_checks=checks,gate_decoded_sha256=ah,entrywise_replay_decoded_sha256=bh,positive_packet_sha256=ph,parity_checks=rows,source_payment_entries_rechecked=59**2+56**2,independent_response_credit_entries=2*56**2,integrated_positive_retained_rank=111,uncovered_retained_dimension=1,physical_guard=positive['physical_guard'],whole_aperture_positive=False,original_analytic_source_domain_high_floor_theorems_inherited=True,source_integrals_recomputed=False,RH=False,F4=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('CC117 PASS',checks,'exact acceptance checks',flush=True)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--output',required=True);run(a.parse_args().output)
