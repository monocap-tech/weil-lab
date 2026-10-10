#!/usr/bin/env python3
"""Independent witness, physical chart, native payment and block-interface audit."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json
import validate_cc105_selected_response as data
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc101_next_source_packet as proof
from certify_cc108_dne41_integration import rank
K=F(647,1000)
def run(path,output):
 a,ah,_=data.read(path);checks=0
 def check(x):
  nonlocal checks
  assert x;checks+=1
 def contain(x,y):check(x[0]<=y[0]<=y[1]<=x[1])
 cc,ch,_=data.read('notes/data/RPB108_CC117_COMPLETE_RESPONSE_GATE_20261010.json.gz.b64');cv,cvh,_=data.read('notes/data/RPB108_CC117_COMPLETE_RESPONSE_VALIDATION_20261010.json');old,oh,_=data.read('notes/data/RPB108_CC117_POSITIVE_PACKET_20261010.json');check(cv['status']=='PASS' and cv['gate_decoded_sha256']==ch==a['CC117_gate_decoded_sha256'] and cvh==a['CC117_validation_sha256']);check(oh==cv['positive_packet_sha256']==a['CC117_positive_packet_sha256'] and old['integrated_positive_retained_rank']==111)
 dn,dh,_=data.read('notes/cc117-source/notes/data/RPB108_DNE50_FULL_RESPONSE_20261010.json.gz.b64');dv,dvh,_=data.read('notes/cc117-source/notes/data/RPB108_DNE50_FULL_RESPONSE_VALIDATION_20261010.json');check(dv['status']=='PASS' and dv['certificate_sha256']==dh==a['DNE50_response_decoded_sha256'] and dvh==a['DNE50_response_validation_sha256'])
 rec,rh,_=data.read('notes/cc118-source/notes/data/RPB108_DNE51_RESPONSE_EXTENSION_20261010.json.gz.b64');rv,rvh,_=data.read('notes/cc118-source/notes/data/RPB108_DNE51_RESPONSE_EXTENSION_VALIDATION_20261010.json');check(rv['status']=='PASS' and rv['certificate_sha256']==rh==a['DNE51_extension_decoded_sha256'] and rvh==a['DNE51_validation_sha256']);check(rec['old_even_trial_space_exhausted'] and not rec['new_original_positivity_established'])
 gate,gh,_=data.read('notes/cc116-source/notes/data/RPB108_DNE49_COMPLETE_PACKET_GATE_20261010.json.gz.b64');hp,hph,_=data.read('notes/data/RPB108_CC105_EVEN_PHYSICAL_PACKET_20261010.json');check(gh==a['DNE49_packet_decoded_sha256']==cc['DNE49_packet_decoded_sha256'] and hph==a['CC105_physical_packet_sha256']);check(a['joint_high_columns']==hp['columns'][1:]+gate['rows'][0]['high_trial_columns']);cols=a['joint_high_columns'];raw=[dict(zip(x['indices'],map(F,x['coefficients']))) for x in cols];ids=sorted(set().union(*(set(x) for x in raw)));check(ids==a['high_support_degrees'] and all(i>=112 and i%2==0 for i in ids));matrix=[[x.get(i,F(0)) for i in ids] for x in raw];check(rank(matrix)==14==a['exact_joint_high_rank']);minor=[[x.get(i,F(0)) for i in a['physical_rank_pivot_degrees']] for x in raw];check(rank(minor)==14)
 gram=c.matrix(a['physical_joint_high_Gram'])
 for i in range(14):
  for j in range(14):contain(gram[i][j],c.iv(sum(v*raw[j].get(degree,F(0)) for degree,v in raw[i].items())))
 gf,gp=proof.proof(gram,a['physical_joint_Gram_positive_proof']['frozen_rational_congruence']);check(gf>=F(a['physical_joint_Gram_coefficient_floor']))
 z=list(map(F,a['common_fixed_comparison_failure_trial']));check(len(z)==56);A=c.matrix(cc['parity_checks'][0]['paid_response_comparison']);B=r.scale(c.matrix(dn['rows'][0]['paid_response_budget']),1/K)
 # Reassemble the quadratic as a signed upper triangle, independently of
 # the producer's dense quadratic summation.
 def quadratic(M):return c.sumiv([c.mul(c.iv(z[i]*z[i]),M[i][i]) for i in range(56)]+[c.mul(c.iv(z[i]*z[j]),c.add(M[i][j],M[j][i])) for i in range(56) for j in range(i+1,56)])
 qa,qb=quadratic(A),quadratic(B);contain(c.iv(a['CC_fixed_trial_value']),qa);contain(c.iv(a['DNE_fixed_trial_value']),qb);check(qa[1]<0 and qb[1]<0);bound=F(a['every_convex_mixture_trial_upper']);check(max(qa[1],qb[1])<=bound<0)
 # Endpoint control is the exact linear identity for every real t in [0,1].
 mixture_controls=[]
 for t in [F(0),F(1,7),F(1,2),F(23,25),F(1)]:
  value=c.add(c.mul(c.iv(1-t),qa),c.mul(c.iv(t),qb));check(value[1]<=bound);mixture_controls.append(dict(t=str(t),trial_upper=str(value[1])))
 prior,prh,_=data.read('notes/data/RPB108_CC105_SELECTED_RESPONSE_VALIDATION_20261010.json');check(prh==a['CC105_validation_sha256'] and prior['all_original_infinite_source_tails_paid']);native=[]
 for idx,label in enumerate(['PRIMARY','REPLAY']):
  src,sh,_=data.read(f'notes/data/RPB108_CC105_EVEN_SOURCE_{label}_20261010.json');saved=a['mixed_native_primary_replay'][idx];check(sh==saved['source_decoded_sha256']==prior['parity_checks'][0]['primary_decoded_sha256' if idx==0 else 'replay_decoded_sha256']);check(src['normalized_packet_sha256']==hph and src['complete_source_coordinates_indices']==list(range(0,245,2)));Q=c.matrix(saved['mixed_native_matrix']);coord=c.matrix(src['complete_source_coordinates']);err=list(map(F,src['source_L2_error_upper']));check(len(Q)==11 and all(len(row)==3 for row in Q))
  for i in range(11):
   for j in range(3):
    vector=raw[11+j];norm=F(cols[11+j]['norm_upper']);check(norm*norm>sum(x*x for x in vector.values()));value=c.iv(0)
    for degree,coeff in vector.items():value=c.add(value,c.mul(c.iv(coeff),coord[i+1][degree//2]))
    payment=err[i+1]*norm;check(payment==F(saved['whole_source_native_error_payments'][i][j]));contain(Q[i][j],c.add(value,(-payment,payment)))
  native.append(Q)
 for i in range(11):
  for j in range(3):contain(native[0][i][j],native[1][i][j])
 check(a['paid_mixed_native_matrix']==a['mixed_native_primary_replay'][1]['mixed_native_matrix'] and a['mixed_native_entries_paid']==33)
 high,hh,_=data.read('notes/cc104-source/notes/data/RPB108_NF52_EVEN_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64');check(hh==a['NF52_even_decoded_sha256']==prior['parity_checks'][0]['original_NF52_certificate_decoded_sha256'] and hph==prior['parity_checks'][0]['physical_packet_decoded_sha256']);NC=r.sub(r.scale(c.matrix(high['enlarged_high_complete_source_Gram']),1/K),c.matrix(high['enlarged_high_native_Gram']));ND=r.scale(c.matrix(dn['rows'][0]['residual_W']),1/K);check(NC==c.matrix(a['CC_denominator_block']) and ND==c.matrix(a['DNE_denominator_block']));proof.proof(NC,a['CC_denominator_positive_proof']['frozen_rational_congruence']);proof.proof(ND,a['DNE_denominator_positive_proof']['frozen_rational_congruence'])
 tr,trh,_=data.read('notes/data/RPB108_CC116_COMPLETE_RESPONSE_TRANSPORT_20261010.json.gz.b64');check(trh==cc['CC116_decoded_sha256']);check(a['CC_complete_signed_response_rows']==tr['parity_checks'][0]['complete_signed_response_rows']);check(a['DNE_complete_signed_response_rows']==dn['rows'][0]['residual_E']);expected=[[i,j] for i in range(14) for j in range(i,14) if i<11<=j];check(a['missing_mixed_projected_source_entries']==expected and len(expected)==a['missing_source_entry_count']==33);check(14*15//2-11*12//2-3*4//2==33)
 # Independent nonorthogonal high-frame countercontrol. L=2I, k=1,
 # f=e1, Y=(e1,e1+e2), retained native q=3/8. Correct mixed N is 2.
 q=F(3,8);n11,n12,n22=F(2),F(2),F(4);w1=w2=F(1);det=n11*n22-n12*n12;check(det>0);joint=(n22*w1*w1-2*n12*w1*w2+n11*w2*w2)/det;separate=w1*w1/n11+w2*w2/n22;actual=q-F(1,2);jointbound=q-1+joint;falsebound=q-1+separate;check(jointbound==actual<F(0)<falsebound);check(joint==F(1,2) and separate==F(3,4));counter=dict(high_operator='2I',high_vectors=[[1,0],[1,1]],native_q=str(q),mixed_denominator_entry=str(n12),joint_credit=str(joint),illegally_added_separate_credits=str(separate),actual_Schur_value=str(actual),correct_joint_bound=str(jointbound),false_zero_cross_bound=str(falsebound),independent_physical_vectors=True)
 check(not a['joint_denominator_certified'] and not a['joint_response_credit_evaluated'] and not a['source_integrals_recomputed']);check(a['integrated_positive_retained_rank']==111 and a['uncovered_retained_dimension']==1 and a['physical_guard']==old['physical_guard']);check(not a['whole_aperture_positive'] and not a['RH'] and not a['F4'] and not a['Lean'])
 out=dict(milestone='CC118',status='PASS',certificate_sha256=ah,exact_rational_checks=checks,common_CC_trial_upper=str(qa[1]),common_DNE_trial_upper=str(qb[1]),every_convex_mixture_upper=str(bound),convex_mixture_controls=mixture_controls,joint_physical_high_rank=14,mixed_native_entries_paid=33,missing_mixed_source_entries=33,nonorthogonal_double_credit_countercontrol=counter,original_analytic_source_domain_high_floor_theorems_inherited=True,integrated_positive_retained_rank=111,uncovered_retained_dimension=1,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('CC118 audit PASS',checks,'exact checks',flush=True)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('certificate');a.add_argument('--output',required=True);x=a.parse_args();run(x.certificate,x.output)
