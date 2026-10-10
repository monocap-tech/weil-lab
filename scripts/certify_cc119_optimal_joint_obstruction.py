#!/usr/bin/env python3
"""If the joint gate fails, pay an upper bound for every trial coefficient choice."""
from pathlib import Path
from fractions import Fraction as F
import json,argparse
import validate_cc105_selected_response as data
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc101_next_source_packet as proof
K=F(647,1000)
def run(output):
 a,ah,_=data.read('notes/data/RPB108_CC119_JOINT_EVEN_RESPONSE_20261010.json');assert a['status']=='PASS' and a['sign']['status']=='REJECTED';N=c.matrix(a['joint_denominator']);W=c.matrix(a['complete_signed_response_rows']);mu,_=proof.proof(N,a['denominator_positive_proof']['frozen_rational_congruence']);z=list(map(F,a['sign']['witness']));H=[list(map(F,row)) for row in a['frozen_H']];y=[sum(row[j]*z[j] for j in range(56)) for row in H];e=[c.sumiv(c.mul(c.iv(z[j]),W[j][i]) for j in range(56)) for i in range(14)];residual=[c.sub(e[i],c.sumiv(c.mul(N[i][j],c.iv(y[j])) for j in range(14))) for i in range(14)];rsq=sum(r.absmax(v)**2 for v in residual);fixed=c.sub(c.mul(c.iv(2),c.sumiv(c.mul(v,c.iv(h)) for v,h in zip(e,y))),c.quad(N,y));upper=fixed[1]+rsq/mu
 cc,ch,_=data.read('notes/data/RPB108_CC117_COMPLETE_RESPONSE_GATE_20261010.json.gz.b64');assert ch==a['CC117_gate_decoded_sha256'];plain=c.quad(c.matrix(cc['parity_checks'][0]['paid_plain_comparison']),z);total=plain[1]+upper/K**2;proved=total<0
 out=dict(milestone='CC119',status='PASS',joint_certificate_sha256=ah,exact_failure_trial=list(map(str,z)),frozen_finite_solve_y=list(map(str,y)),denominator_coefficient_floor=str(mu),residual_norm_squared_upper=str(rsq),fixed_credit_numerator=c.pair(fixed),optimized_credit_numerator_upper=str(upper),plain_comparison_trial=c.pair(plain),optimal_joint_comparison_trial_upper=str(total),every_joint_coefficient_matrix_excluded=proved,actual_original_negative_form_claimed=False,true_infinite_inverse_evaluated=False,certified_inverse_evaluations=0,integrated_positive_retained_rank=111,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('CC119 optimal joint obstruction',proved,'upper',float(total),flush=True)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--output',required=True);run(a.parse_args().output)
