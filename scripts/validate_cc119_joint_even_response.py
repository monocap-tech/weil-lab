#!/usr/bin/env python3
"""Independent joint denominator, fixed-trial replay and whole-packet audit."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json
import validate_cc105_selected_response as data
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc101_next_source_packet as proof
import certify_cc104_joint_response_rebase as response
K=F(647,1000)
def run(output):
 checks=0
 def check(x):
  nonlocal checks
  assert x;checks+=1
 def contain(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
 a,ah,_=data.read('notes/data/RPB108_CC119_JOINT_EVEN_RESPONSE_20261010.json');b,bh,_=data.read('notes/data/RPB108_CC119_JOINT_EVEN_RESPONSE_REPLAY_20261010.json');check(a['status']==b['status']=='PASS' and b['producer_certificate_sha256']==ah and b['independent_entrywise_response_replay'])
 sv,svh,_=data.read('notes/data/RPB108_CC119_MIXED_SOURCE_VALIDATION_20261010.json');src,sh,_=data.read('notes/data/RPB108_CC119_EVEN_SOURCE_REPLAY_20261010.json');check(sv['status']=='PASS' and svh==a['mixed_source_validation_sha256'] and sh==a['mixed_source_replay_sha256']==sv['rows'][1]['source_decoded_sha256'])
 iv,ivh,_=data.read('notes/data/RPB108_CC118_JOINT_RESPONSE_VALIDATION_20261010.json');frame,fh,_=data.read('notes/data/RPB108_CC118_JOINT_RESPONSE_INTERFACE_20261010.json');check(iv['status']=='PASS' and ivh==a['CC118_validation_sha256'] and iv['certificate_sha256']==fh==a['CC118_certificate_sha256']);check(frame['exact_joint_high_rank']==14)
 U=[[c.iv(src['original_projected_source_Gram'][i][11+j]) for j in range(3)] for i in range(11)];T=c.matrix(frame['paid_mixed_native_matrix']);X=r.sub(r.scale(U,1/K),T);check(X==c.matrix(a['mixed_native_source_denominator_block']));N=response.block(c.matrix(frame['CC_denominator_block']),X,c.matrix(frame['DNE_denominator_block']));check(N==c.matrix(a['joint_denominator']) and N==c.transpose(N));d,np=proof.proof(N,a['denominator_positive_proof']['frozen_rational_congruence']);check(d>=F(a['denominator_positive_proof']['coefficient_floor_lower']))
 W=[[r.compact(v) for v in x+y] for x,y in zip(c.matrix(frame['CC_complete_signed_response_rows']),c.matrix(frame['DNE_complete_signed_response_rows']))];check(W==c.matrix(a['complete_signed_response_rows']));H=[list(map(F,row)) for row in a['frozen_H']];check(a['frozen_H']==b['frozen_H'] and len(H)==14 and all(len(row)==56 for row in H));check(a['joint_denominator']==b['joint_denominator'] and a['complete_signed_response_rows']==b['complete_signed_response_rows'])
 cc,ch,_=data.read('notes/data/RPB108_CC117_COMPLETE_RESPONSE_GATE_20261010.json.gz.b64');cv,cvh,_=data.read('notes/data/RPB108_CC117_COMPLETE_RESPONSE_VALIDATION_20261010.json');check(cv['status']=='PASS' and cv['gate_decoded_sha256']==ch==a['CC117_gate_decoded_sha256']);plain=c.matrix(cc['parity_checks'][0]['paid_plain_comparison']);credit=c.matrix(a['paid_response_credit']);recredit=c.matrix(b['paid_response_credit']);M=c.matrix(a['paid_full_comparison']);RM=c.matrix(b['paid_full_comparison'])
 for i in range(56):
  for j in range(56):
   contain(credit[i][j],recredit[i][j]);contain(M[i][j],c.add(plain[i][j],credit[i][j]));contain(M[i][j],RM[i][j]);check(M[i][j]==M[j][i])
 if a['sign']['status']=='POSITIVE':
  sf,sp=proof.proof(M,a['sign']['proof']['frozen_rational_congruence']);check(sf>=F(a['sign']['floor']));rf,rp=proof.proof(RM,b['sign']['proof']['frozen_rational_congruence']);check(rf>=sf);mass=F(cc['parity_checks'][0]['physical_packet_mass']);trace=F(cc['parity_checks'][0]['projected_source_trace_upper']);gap=min(sf/(4*(mass+trace/K**2)),K/2);check(gap>=F(a['physical_gap_lower']) and mass==F(a['physical_packet_mass']) and trace==F(a['projected_source_trace_upper']))
  # The odd whole packet and all 112 original retained chart ranks are
  # inherited through CC117/CC116's authenticated audits. Replay its saved
  # exact congruence here so the whole physical guard is directly reviewable.
  odd=cc['parity_checks'][1];os=c.matrix(odd['paid_response_comparison']);od,op=proof.proof(os,odd['full_response_sign']['proof']['frozen_rational_congruence']);og=min(od/(4*(F(odd['physical_packet_mass'])+F(odd['projected_source_trace_upper'])/K**2)),K/2);check(og>=F(odd['physical_gap_lower']));common=min(gap,og);rank=112;whole=True
 else:
  z=list(map(F,a['sign']['witness']));check(c.quad(M,z)[1]<0 and c.quad(RM,z)[1]<0);common=F(frame['physical_guard']);rank=111;whole=False
  path='notes/data/RPB108_CC119_OPTIMAL_JOINT_OBSTRUCTION_20261010.json';opt,oph,_=data.read(path);check(opt['status']=='PASS' and opt['joint_certificate_sha256']==ah and opt['exact_failure_trial']==a['sign']['witness']);y=list(map(F,opt['frozen_finite_solve_y']));e=[c.sumiv(c.mul(c.iv(z[j]),W[j][i]) for j in range(56)) for i in range(14)];res=[c.sub(e[i],c.sumiv(c.mul(N[i][j],c.iv(y[j])) for j in range(14))) for i in range(14)];rsq=sum(r.absmax(x)**2 for x in res);fixed=c.sub(c.mul(c.iv(2),c.sumiv(c.mul(x,c.iv(t)) for x,t in zip(e,y))),c.quad(N,y));mu=F(opt['denominator_coefficient_floor']);check(0<mu<=d and rsq==F(opt['residual_norm_squared_upper']));upper=fixed[1]+rsq/mu;check(upper==F(opt['optimized_credit_numerator_upper']));total=c.quad(plain,z)[1]+upper/K**2;check(total==F(opt['optimal_joint_comparison_trial_upper']) and (total<0)==opt['every_joint_coefficient_matrix_excluded'])
 check(a['integrated_positive_retained_rank']==rank and a['uncovered_retained_dimension']==112-rank and a['whole_aperture_positive']==whole);check(a['certified_inverse_evaluations']==0 and not a['true_infinite_inverse_evaluated']);check(not a['RH'] and not a['F4'] and not a['Lean'])
 out=dict(milestone='CC119',status='PASS',exact_rational_checks=checks,producer_certificate_sha256=ah,entrywise_replay_sha256=bh,mixed_source_validation_sha256=svh,independent_credit_entries_reassembled=3136,joint_denominator_positive=True,joint_even_comparison_sign=a['sign']['status'],integrated_positive_retained_rank=rank,uncovered_retained_dimension=112-rank,all_high_physical_gap_lower=str(common),whole_aperture_positive=whole,original_analytic_source_domain_high_floor_theorems_inherited=True,computational_cost_dominance_proved=False,RH=False,F4=False,Lean=False)
 if not whole:out.update(optimal_joint_obstruction_sha256=oph,every_joint_coefficient_matrix_excluded=opt['every_joint_coefficient_matrix_excluded'],optimal_joint_trial_upper=str(total))
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('CC119 response audit PASS',checks,'checks; rank',rank,'whole',whole,flush=True)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--output',required=True);run(a.parse_args().output)
