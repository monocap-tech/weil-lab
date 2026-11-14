#!/usr/bin/env python3
"""NF509 independently audit authentic native selected-leverage cell receipts.

Exact-rational geometry, source SHA custody, per-index interval decisions,
selected-pair disjointness and total 242D trace accounting. No independent
original 4096-bit re-integration, and no response-energy e_j computation.
"""
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAM='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
FRAME='18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e'
NF505='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
TH=F(27,29)

def read(p):
    raw=Path(p).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()

def interval(raw):
    a,b=map(F,raw);assert a<=b
    return a,b

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--native',required=True)
    ap.add_argument('--prior',required=True)
    ap.add_argument('--output',required=True)
    o=ap.parse_args()
    now,sha=read(o.native)
    prior,old_sha=read(o.prior)
    assert old_sha==NF505==now['original_nf505_raw_sha256']
    assert now['pass']=='NF509-original-source-leverage-native'
    assert prior['pass']=='NF504-native'
    assert now['original_nf407_source_sha256']==prior['source_original_NF407_sha256']==SRC
    assert now['original_nf406_seam_sha256']==prior['source_original_NF406_sha256']==SEAM
    assert now['original_selected_D_frame_sha256']==prior['original_original_D_frame_SHA256']==FRAME
    assert now['original_selected_dimension']==242
    assert now['original_microcell_count']==4096
    assert F(now['original_total_pair_half_width'])==F(549,500*4096)
    assert now['original_exterior_W_selected_fit_equation_residual']
    lo,hi=interval(now['original_exterior_W_selected_fit_equation_residual'])
    assert lo>=0 and hi<F('1e-30')
    oldR=interval(prior['original_original_saturated_exterior_residual_outward'])
    newR=interval(now['original_full_exterior_W_optimal_residual_reconstructed'])
    assert max(oldR[0],newR[0])<=min(oldR[1],newR[1])
    assert len(now['original_exterior_original_W_242D_optimal_fit_D_coefficients_outward'])==242
    for x in now['original_exterior_original_W_242D_optimal_fit_D_coefficients_outward']:
        interval(x)
    indices=now['original_sampled_cell_indices']
    rows=now['original_source_real_microcell_leverage_measurements']
    assert indices==sorted(set(indices)) and len(rows)==len(indices)
    assert len(indices)>=2
    total_hi=F(0)
    statuses=[]
    for k,(index,row) in enumerate(zip(indices,rows)):
        assert isinstance(index,int) and 0<=index<4096
        assert row['j']==index
        assert F(row['half_left'])==F(index*549,500*4096)
        assert F(row['half_right'])==F((index+1)*549,500*4096)
        assert F(row['mirrored_pair_total_width'])==F(1098,500*4096)
        l,h=interval(row['true_original_J242_selected_leverage_outward'])
        assert 0<l<=h<242
        status=row['leverage_vs_NF508_theta']
        expected=('CERTIFIED_LEVERAGE_LT_27_29' if h<TH else
                  'CERTIFIED_LEVERAGE_GE_27_29' if l>=TH else
                  'LEVERAGE_THRESHOLD_INDETERMINATE')
        assert status==expected
        total_hi+=h
        statuses.append(status)
    # Sum on all disjoint sampled genuine cells cannot exceed total trace
    # 242; this is a useful numerical cross-check, not an independent
    # recomputation of original analytic cell Grams.
    assert total_hi<242
    assert now['original_W_minus_Ja_local_energy_integrated'] is False
    assert now['individual_local_support_acceptance_certified'] is False
    assert now['original_weil_multiplier_image_graph_domain']=='OPEN'
    assert now['W_ODD_NEG']==now['RH']=='OPEN'
    result={
        'pass':'NF509-independent-exact-source-custody',
        'scope':'Exact source SHA/frame/rational mirrored-cell leverage receipt check; original W local energy, second Gram integration, Weil source/domain OPEN',
        'original_nf505_sha256':old_sha,'native_nf509_sha256':sha,
        'sampled_mirrored_microcells':indices,
        'leverage_below_27over29':sum(x=='CERTIFIED_LEVERAGE_LT_27_29' for x in statuses),
        'leverage_ge_27over29':sum(x=='CERTIFIED_LEVERAGE_GE_27_29' for x in statuses),
        'leverage_indeterminate':sum(x=='LEVERAGE_THRESHOLD_INDETERMINATE' for x in statuses),
        'all_samples_disjoint_sum_leverage_upper_lt_242':True,
        'original_source_242D_inverse_reused':True,
        'original_microcell_J_Grams_reintegrated_independently':False,
        'original_local_W_energy_e_j':'OPEN','local_patch_NF404_verdict':'OPEN',
        'Weil_multiplier_image_graph_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN',
    }
    Path(o.output).write_text(json.dumps(result,indent=2)+'\n')
    print('NF509 exact Fraction source identity + mirrored 242D microcell leverage audit PASS')
    print('tau<27/29:',result['leverage_below_27over29'],
          'tau>=27/29:',result['leverage_ge_27over29'],
          'unknown:',result['leverage_indeterminate'])
    print('Original local e_j not computed: no individual patch sign or RH promoted')

if __name__=='__main__':main()
