#!/usr/bin/env python3
"""Common fixed-comparison obstruction and paid joint-frame native interface."""
from pathlib import Path
from fractions import Fraction as F
import json,argparse,numpy as np
import validate_cc105_selected_response as data
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc101_next_source_packet as proof
from certify_cc112_physical_response_transport import sparse,pivots
K=F(647,1000)
def run(output):
 checks=0
 def check(v):
  nonlocal checks
  assert v;checks+=1
 cc,ch,_=data.read('notes/data/RPB108_CC117_COMPLETE_RESPONSE_GATE_20261010.json.gz.b64');cv,cvh,_=data.read('notes/data/RPB108_CC117_COMPLETE_RESPONSE_VALIDATION_20261010.json');standing,sth,_=data.read('notes/data/RPB108_CC117_POSITIVE_PACKET_20261010.json');check(cv['status']=='PASS' and cv['gate_decoded_sha256']==ch and cv['positive_packet_sha256']==sth and standing['integrated_positive_retained_rank']==111)
 dn,dh,_=data.read('notes/cc117-source/notes/data/RPB108_DNE50_FULL_RESPONSE_20261010.json.gz.b64');dv,dvh,_=data.read('notes/cc117-source/notes/data/RPB108_DNE50_FULL_RESPONSE_VALIDATION_20261010.json');check(dv['status']=='PASS' and dv['certificate_sha256']==dh)
 gate,gh,_=data.read('notes/cc116-source/notes/data/RPB108_DNE49_COMPLETE_PACKET_GATE_20261010.json.gz.b64');Yd=gate['rows'][0]['high_trial_columns'];check(len(Yd)==3 and gh==cc['DNE49_packet_decoded_sha256'])
 hp,hph,_=data.read('notes/data/RPB108_CC105_EVEN_PHYSICAL_PACKET_20261010.json');Yc=hp['columns'][1:];check(len(Yc)==11);cols=Yc+Yd;raw=[sparse(x) for x in cols];ids=sorted(set().union(*(set(x) for x in raw)));check(all(i>=112 and i%2==0 for i in ids));basis=[[x.get(i,F(0)) for i in ids] for x in raw];pivot=pivots(basis);check(len(pivot)==14)
 gram=[[r.compact(c.iv(sum(x*b.get(i,F(0)) for i,x in a.items()))) for b in raw] for a in raw];gf,gp=proof.proof(gram)
 A=c.matrix(cc['parity_checks'][0]['paid_response_comparison']);B=r.scale(c.matrix(dn['rows'][0]['paid_response_budget']),1/K);mid=lambda M:np.array([[float(sum(x)/2) for x in row] for row in M]);t=F(23,25);C=(1-float(t))*mid(A)+float(t)*mid(B);vals,vec=np.linalg.eigh((C+C.T)/2);z=[F(round(float(x)*10**40),10**40) for x in vec[:,0]];qa,qb=c.quad(A,z),c.quad(B,z);check(qa[1]<0 and qb[1]<0);upper=max(qa[1],qb[1]);check(upper<0)
 # The CC105 high actions have all coordinates through degree244, sufficient
 # for the independently frozen DNE3 high vectors (maximum degree180).
 prior,prh,_=data.read('notes/data/RPB108_CC105_SELECTED_RESPONSE_VALIDATION_20261010.json');check(prior['all_original_infinite_source_tails_paid'] and prior['fresh_analytic_source_reconstructions'])
 recovered,rh,_=data.read('notes/cc118-source/notes/data/RPB108_DNE51_RESPONSE_EXTENSION_20261010.json.gz.b64');recoveredv,rvh,_=data.read('notes/cc118-source/notes/data/RPB108_DNE51_RESPONSE_EXTENSION_VALIDATION_20261010.json');check(recoveredv['status']=='PASS' and recoveredv['certificate_sha256']==rh and recovered['old_even_trial_space_exhausted']);native=[];sourcepins=[]
 for run in ['PRIMARY','REPLAY']:
  src,sh,_=data.read(f'notes/data/RPB108_CC105_EVEN_SOURCE_{run}_20261010.json');row=prior['parity_checks'][0];check(sh==row['primary_decoded_sha256' if run=='PRIMARY' else 'replay_decoded_sha256']);check(src['normalized_packet_sha256']==hph and len(src['complete_source_coordinates'])==12 and src['complete_source_coordinates_indices']==list(range(0,245,2)));coords=c.matrix(src['complete_source_coordinates']);errs=list(map(F,src['source_L2_error_upper']));matrix=[];payments=[]
  for j,col in enumerate(Yc,1):
   rr=[];pp=[]
   for old in Yd:
    check(all(degree//2<len(coords[j]) for degree in old['indices']));approx=c.sumiv(c.mul(c.iv(value),coords[j][degree//2]) for degree,value in zip(old['indices'],old['coefficients']));mass=sum(F(x)**2 for x in old['coefficients']);norm=F(old['norm_upper']);check(norm*norm>mass);pay=errs[j]*norm;rr.append(c.add(approx,(-pay,pay)));pp.append(str(pay))
   matrix.append(rr);payments.append(pp)
  native.append(dict(run=run,source_decoded_sha256=sh,mixed_native_matrix=[[c.pair(x) for x in row] for row in matrix],whole_source_native_error_payments=payments));sourcepins.append(sh)
 primary,replay=[c.matrix(x['mixed_native_matrix']) for x in native]
 for ar,br in zip(primary,replay):
  for a,b in zip(ar,br):check(a[0]<=b[0]<=b[1]<=a[1])
 high,hh,_=data.read('notes/cc104-source/notes/data/RPB108_NF52_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64');check(hh==cc['parity_checks'][0]['high_decoded_sha256']==prior['parity_checks'][0]['original_NF52_certificate_decoded_sha256'] and hph==prior['parity_checks'][0]['physical_packet_decoded_sha256']);NC=r.sub(r.scale(c.matrix(high['enlarged_high_complete_source_Gram']),1/K),c.matrix(high['enlarged_high_native_Gram']));ND=r.scale(c.matrix(dn['rows'][0]['residual_W']),1/K);_,ncp=proof.proof(NC,cc['parity_checks'][0]['denominator_positive_proof']['frozen_rational_congruence']);_,ndp=proof.proof(ND)
 manifest=[[i,11+j] for i in range(11) for j in range(3)];check(len(manifest)==33 and len({tuple(x) for x in manifest})==33)
 Wc=cc['parity_checks'][0]['matrix_dimension'];check(Wc==56 and len(dn['rows'][0]['residual_E'])==56)
 out=dict(milestone='CC118',status='PASS',parent='8d3b66127af94d0dba06389b14579f5b79e9a6d6',exact_rational_acceptance_checks=checks,CC117_gate_decoded_sha256=ch,CC117_validation_sha256=cvh,CC117_positive_packet_sha256=sth,DNE50_response_decoded_sha256=dh,DNE50_response_validation_sha256=dvh,DNE49_packet_decoded_sha256=gh,DNE51_extension_decoded_sha256=rh,DNE51_validation_sha256=rvh,CC105_physical_packet_sha256=hph,CC105_validation_sha256=prh,NF52_even_decoded_sha256=hh,original_high_floor=str(K),common_fixed_comparison_failure_trial=list(map(str,z)),CC_fixed_trial_value=c.pair(qa),DNE_fixed_trial_value=c.pair(qb),every_convex_mixture_trial_upper=str(upper),every_convex_mixture_rejected=True,mixture_proposal_parameter=str(t),joint_high_columns=cols,high_support_degrees=ids,exact_joint_high_rank=14,physical_rank_pivot_degrees=[ids[i] for i in pivot],physical_joint_high_Gram=[[c.pair(x) for x in row] for row in gram],physical_joint_Gram_positive_proof=gp,physical_joint_Gram_coefficient_floor=str(gf),mixed_native_primary_replay=native,paid_mixed_native_matrix=native[1]['mixed_native_matrix'],mixed_native_entries_paid=33,CC_denominator_block=[[c.pair(x) for x in row] for row in NC],DNE_denominator_block=[[c.pair(x) for x in row] for row in ND],CC_denominator_positive_proof=ncp,DNE_denominator_positive_proof=ndp,CC_complete_signed_response_rows=data.read('notes/data/RPB108_CC116_COMPLETE_RESPONSE_TRANSPORT_20261010.json.gz.b64')[0]['parity_checks'][0]['complete_signed_response_rows'],DNE_complete_signed_response_rows=dn['rows'][0]['residual_E'],missing_mixed_projected_source_entries=manifest,missing_source_entry_count=33,joint_denominator_certified=False,joint_response_credit_evaluated=False,source_integrals_recomputed=False,integrated_positive_retained_rank=111,uncovered_retained_dimension=1,physical_guard=standing['physical_guard'],original_analytic_source_domain_high_floor_theorems_inherited=True,computational_cost_dominance_proved=False,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('CC118',checks,'checks; all convex mixtures rejected, high rank14, native33 paid, source33 missing',flush=True)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--output',required=True);run(a.parse_args().output)
