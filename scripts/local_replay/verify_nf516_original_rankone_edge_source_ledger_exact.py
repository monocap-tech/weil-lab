#!/usr/bin/env python3
"""NF516 independent exact Fraction audit of original source-local rank-one receipt.

Validates committed outward inputs against source-authenticated NF514/NF515
global selected witnesses and NF511/NF513 actual W² receipts. This is
a receipt audit, NOT a second NF494 H400/U400 re-integration; the two
complete original-source integrators are in the separate local proof pack.
"""
import argparse, hashlib, json, sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
S494='39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181'
S505='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
S514='b45b834bfebfdf7b8e3475e668e526d561c8cddb05a19bcfc4e98f9b945b4194'
S515='3ff6a14a0d850dc23a3965ca651a4b1229ba4d82881c4373061b7483f07d289f'
S511='9e80c5bf05d9242b078f407c10009fa2c036b8abc1f8a5add24c1fe4e58aaed1'
S513='7c6aaf2374a7e58ab0749955b15083719f555182e5d6dd8e723fa1fc31ead495'
def read(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def iv(x):
    a,b=map(F,x)
    assert a<=b
    return a,b
def overlap(a,b):return max(a[0],b[0])<=min(a[1],b[1])
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):
    v=[x*y for x in a for y in b]
    return min(v),max(v)
def sq(a):
    return (F(0) if a[0]<=0<=a[1] else min(a[0]**2,a[1]**2),
            max(a[0]**2,a[1]**2))
def scale(a,b):
    return (a[0]*b,a[1]*b) if b>=0 else (a[1]*b,a[0]*b)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--ledger',default='notes/data/provisional/NF516_original_J8_two_cell_globally_fitted_rankone_source_exact_custody.json')
    for name in ('nf515','nf514','nf511','nf513','output'):
        p.add_argument('--'+name,required=True)
    a=p.parse_args()
    j,ledger_sha=read(a.ledger);n515,sha515=read(a.nf515)
    n514,sha514=read(a.nf514);n511,sha511=read(a.nf511)
    n513,sha513=read(a.nf513)
    assert j['pass']=='NF516-original-source-J8-two-cell-globally-fitted-rankone-local-exact'
    assert (sha515,sha514,sha511,sha513)==(S515,S514,S511,S513)
    assert j['original_nf494_H400_U400_raw_SHA256']==S494
    assert j['original_nf505_full_J242_raw_SHA256']==S505
    assert j['original_nf515_global_source_witness_bridge_SHA256']==sha515
    assert j['original_nf514_selected_23D_integer_seed_SHA256']==n514['witness_seed_SHA256']
    assert j['original_nf407_source_SHA256']==n515['source_original_NF407_SHA256']
    assert j['original_nf406_prime_seam_SHA256']==n515['source_original_NF406_SHA256']
    assert n514['pass']=='NF514-authentic-original-selected-23D-subspace-leverage-lower-exact'
    assert n515['pass']=='NF515-original-source-global-exterior-v23-witness-moment-exact'
    assert n514['original_NF505_native_SHA256']==n515['source_original_NF505_SHA256']==S505
    assert n511['pass'] in ('NF511-source-local-W-square-exact','NF511-original-source-exact-local-W-pole-panel')
    assert n513['pass'] in ('NF513-source-local-W-square-exact','NF513-original-source-J8-H4094-local-W-pole-exact')
    assert j['original_selected_dimension']==242
    assert j['actual_original_selected_rank_one_witness_source_generators']==23
    assert j['physical_mirror_pair_cells']==[4094,4095]
    assert F(j['physical_two_cells_fraction_of_original_exterior_measure'])==F(1,2048)
    nm=iv(n515['original_true_exterior_O_W_witness_moment_outward'])
    nn=iv(n515['original_selected_v23_full_exterior_norm_squared'])
    assert nm[1]<0 and nn[0]>0
    beta=(nm[0]/nn[0],nm[1]/nn[1])
    assert beta[1]<0
    total_E=total_b=total_R=(F(0),F(0))
    records=[]
    for idx,prior in ((4094,n513),(4095,n511)):
        row=j['source_integral_intervals_from_independent_44jet_analytic_exact_decimal'][f'H{idx}']
        E=iv(row['original_W2'])
        b=iv(row['original_W_times_selected_v'])
        R=iv(row['original_globally_fitted_rankone_residual_squared'])
        prior_E=iv(prior['original_cell_full_W_sq_outward']
                   if 'original_cell_full_W_sq_outward' in prior
                   else prior['local_E_H_original_full_W_squared'])
        assert overlap(E,prior_E)
        assert E[0]>0 and b[1]<0 and R[0]>0
        ratios=n514['original_selected_subspace_rayleigh_leverage_lower_by_named_cell'][f'H{idx}']
        rv=iv([ratios['lower'],ratios['upper']])
        assert rv[0]>0
        v2=mul(rv,nn)
        assert b[0]**2<=E[1]*v2[1]
        reconstructed=plus(plus(E,scale(mul(beta,b),-2)),mul(sq(beta),v2))
        assert overlap(reconstructed,R),('rank-one source identity mismatch',idx)
        threshold=F(7,10) if idx==4094 else F(63,100)
        assert 1-R[1]/E[0]>threshold
        total_E=plus(total_E,E)
        total_b=plus(total_b,b)
        total_R=plus(total_R,R)
        records.append({'original_cell':idx,
                        'energy_removed_fraction_strict_lower':str(1-R[1]/E[0]),
                        'energy_removed_fraction_upper':str(1-R[0]/E[1]),
                        'original_NF511_or_NF513_source_W2_overlap':True})
    union=j['source_integral_intervals_from_independent_44jet_analytic_exact_decimal']['union']
    E=iv(union['original_W2']);b=iv(union['original_W_times_selected_v'])
    R=iv(union['original_globally_fitted_rankone_residual_squared'])
    assert overlap(E,total_E) and overlap(b,total_b) and overlap(R,total_R)
    assert 1-R[1]/E[0]>F(65,100)
    signed=(b[1]/nm[0],b[0]/nm[1])
    assert F(95,100)<signed[0]<=signed[1]<1
    complement=(nm[0]-b[1],nm[1]-b[0])
    assert complement[1]<0
    assert j['original_complete_J242_globally_fitted_local_eH']=='OPEN'
    assert j['original_NF404_named_physical_support_gate']=='OPEN'
    assert j['original_Weil_multiplier_image_graph_domain']==j['W_ODD_NEG']==j['RH']=='OPEN'
    out={'pass':'NF516-committed-original-source-exact-ledger-audit',
         'original_NF516_outward_ledger_sha256':ledger_sha,
         'original_NF515_global_source_bridge_SHA256':sha515,
         'original_NF514_selected_witness_certificate_SHA256':sha514,
         'original_NF511_source_cell_SHA256':sha511,
         'original_NF513_source_cell_SHA256':sha513,
         'original_local_exact_rankone_energy_removed':records,
         'two_cells_union_energy_removed_fraction_strict_lower':str(1-R[1]/E[0]),
         'two_cells_union_NET_SIGNED_source_Wv_fraction_strict_lower':str(signed[0]),
         'original_full_242D_globally_fitted_local_eH':'OPEN',
         'Weil_source_image_graph_domain':'OPEN',
         'W_ODD_NEG':'OPEN','RH':'OPEN'}
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
    print('NF516 committed original source-ledger exact Fraction acceptance PASS')
    print('Original globally fitted single selected mode removes >65% local W²;')
    print('two edge cells carry >95% net signed original selected source coupling')
    print('Complete J242 local residual and RH remain OPEN')
if __name__=='__main__':main()
