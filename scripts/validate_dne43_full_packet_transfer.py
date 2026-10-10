#!/usr/bin/env python3
"""Authenticate the new high floor and discharge DNE42's conditional gate."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json
from certify_dne39_signed_comparison import read

def run(output):
    paths=['notes/data/RPB108_DNE43_HIGH_FLOOR_VALIDATION_20261010.json','notes/data/RPB108_DNE42_UNIFORM_FLOOR_TARGET_VALIDATION_20261010.json','notes/data/RPB108_DNE41_POSITIVE_SUBSPACE_VALIDATION_20261010.json','notes/data/RPB108_DNE43_PRIME_SCHUR_20261010.json.gz.b64','notes/data/RPB108_DNE43_PRIME_SCHUR_REPLAY_20261010.json.gz.b64']
    inputs=[read(p) for p in paths];high,target,prior,primary,replay=[d for d,_ in inputs];checks=0
    def check(v):
        nonlocal checks
        assert v;checks+=1
    check(high['status']==target['status']==prior['status']=='PASS');check(high['stage']=='DNE43' and target['stage']=='DNE42' and prior['stage']=='DNE41')
    check([r['sha256'] for r in high['rows']]==[inputs[3][1],inputs[4][1]])
    k=F(high['original_infinite_F112_floor']);check(k==F(603,1000));check(primary['certified_original_F112_lower']==replay['certified_original_F112_lower']==str(k));check(primary['weight_power']==replay['weight_power']==17)
    check(F(high['arch_minus_pole_strict_lower'])-F(replay['certified_prime_norm_strict_upper'])>k)
    check(prior['all_high_positive_retained_dimension']==69);check(prior['uncovered_retained_dimension']==43);check(target['actual_certified_retained_dimension']==69);check(target['conditional_retained_dimension_if_target_established']==72)
    rows=[]
    for row in target['rows']:
        p=f"notes/data/RPB108_DNE42_{row['parity'].upper()}_UNIFORM_FLOOR_TARGET_20261010.json";c,ch=read(p);check(ch==row['certificate_sha256']);check(row['full_packet_target_positive']);u=F(row['critical_uniform_floor_upper']);check(u==F(c['critical_uniform_floor_upper'])<k)
        check(c['packet_dimension']==36);pr=next(r for r in prior['rows'] if r['parity']==row['parity']);check(pr['positive_retained_rank']+pr['negative_uniform_comparison_rank']==36);check(c['input_sha256'][0]==pr['input_sha256'][0]);check(c['input_sha256'][1]==pr['input_sha256'][1])
        old_gap=F(row['conditional_all_high_physical_gap_lower']);check(old_gap==F(c['conditional_all_high_physical_gap_lower'])>0)
        native,nh=read(c['input_paths'][1]);check(nh==c['input_sha256'][1]);dn=F(native['joint_native_positive_control']['coefficient_floor_lower']);du=F(c['full_packet_target_certificate']['coefficient_floor_lower']);check(dn>0 and du>0)
        d=du+(k-u)*dn;mass=F(c['conditional_physical_mass']);trace=F(c['conditional_source_trace_upper']);gap=min((d/k)/(4*(mass+trace/k**2)),k/2);check(gap>old_gap)
        rows.append(dict(parity=row['parity'],target_certificate_path=p,target_certificate_sha256=ch,used_high_floor=str(u),established_original_high_floor=str(k),positive_retained_rank=36,inherited_native_coefficient_floor=str(dn),inherited_target_coefficient_floor=str(du),actual_comparison_coefficient_floor=str(d),native_comparison_path=c['input_paths'][1],native_comparison_sha256=nh,all_high_physical_gap_lower=str(gap),prior_positive_span_contained=True))
    check({r['parity'] for r in rows}=={'even','odd'});total=sum(r['positive_retained_rank'] for r in rows);check(total==72)
    guard=F(1,10**40);check(guard<min(F(r['all_high_physical_gap_lower']) for r in rows))
    out=dict(stage='DNE43',parent='b6b5cbe5a9f59dbf9f03ae931083289dbf11bf13',status='PASS',new_transfer_rational_checks=checks,new_high_floor_rational_checks=high['exact_rational_checks'],input_paths=paths,input_sha256=[h for _,h in inputs],rows=rows,original_infinite_F112_floor=str(k),all_high_positive_retained_dimension=total,uncovered_retained_dimension=112-total,all_high_physical_gap_guard=str(guard),prior_69_direction_physical_guard=str(F(1,10**39)),source_integrals_recomputed=False,true_high_inverse_evaluated=False,complete_remaining_source_Gram_certified=False,whole_aperture_positive=False,RH=False,Lean=False)
    Path(output).write_text(json.dumps(out,indent=2)+'\n');print('PASS',checks,'transfer checks; actual retained rank',total,'guard',str(guard),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();run(a.output)
