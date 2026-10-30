#!/usr/bin/env python3
"""NF404 independent ROOT-FREE exact-rational acceptance of true original
selected 242D j* Fourier tail: a scoped full-line SURROGATE METHOD STOP.

Does NOT infer the original supported lowband physical residual from tail.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,argparse,sys
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
ORIGINAL_ENDPOINT_SHA='a09b22f7f653e5eb2af516a6e6104d2d1e27b525c9cdc8bc0074c212b6982c94'
ORIGINAL_SELECTED_SHA='644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515'
ORIGINAL_NF398_SHA='bae006e4fb542c4b0c6d184ae8cfbc2e7c924d45c89092ebda89cf0c6057c877'
LAM=2**24
B=F(11,10)
def load(p):
    b=Path(p).read_bytes()
    return json.loads(b),hashlib.sha256(b).hexdigest()
def ii(v):
    assert len(v)==2
    a,b=map(F,v)
    assert a<=b
    return a,b
def abslo(v):
    a,b=ii(v)
    return F(0) if a<=0<=b else min(abs(a),abs(b))
def abshi(v):
    a,b=ii(v)
    return max(abs(a),abs(b))
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--native',required=True)
    p.add_argument('--endpoint',default='notes/data/provisional/NF404_original_selected_endpoint_native.json')
    p.add_argument('--selected',default='notes/data/provisional/NF401_original_242D_selected_column_source_native.json')
    p.add_argument('--nf398',default='notes/data/provisional/NF398_original_j387_selected_signed_native.json')
    p.add_argument('--output',required=True)
    a=p.parse_args()
    n,nsha=load(a.native)
    end,endsha=load(a.endpoint)
    selected,selsha=load(a.selected)
    nf398,nf398sha=load(a.nf398)
    assert endsha==n['original_frozen_nf404_endpoint_parent_sha256']==ORIGINAL_ENDPOINT_SHA
    assert selsha==n['parent_nf401_native_sha256']==ORIGINAL_SELECTED_SHA
    assert nf398sha==ORIGINAL_NF398_SHA
    assert n['original_rank']==242 and n['original_highband_cutoff']==LAM
    assert n['all_original_selected_raw_moments_interval_reproduced'] is True
    assert n['original_J242_closed_under_second_derivative'] is True
    assert n['new_signed_kernel_cells']==0
    for k in ('original_full_supported_multiplier_scalar_norm_upper_computed',
              'original_J_perpendicular_full_action_upper_computed',
              'original_lowband_upper_computed',
              'original_operator_domain_independently_audited',
              'original_supported_physical_lowband_complement_upper_measured'):
        assert n[k] is False
    assert n['W_ODD_NEG']==n['RH']==nf398['W_ODD_NEG']==nf398['RH']=='OPEN'
    assert n['original_source_selected_highband_tail_gt_1e_minus_6'] is True
    assert n['original_wholeline_fourier_primal_lowband_upper_METHOD_STOP_for_any_candidate_in_NF401_ball'] is True

    e=abslo(n['original_selected_endpoint_value_interval'])
    d=abshi(n['original_selected_endpoint_derivative_interval'])
    m=ii(n['selected_second_derivative_physical_norm_interval'])[1]
    assert e>0 and d>=0 and m>=0
    assert n['original_selected_endpoint_value_interval']==end['original_selected_endpoint_value_interval']
    assert n['original_selected_endpoint_derivative_interval']==end['original_selected_endpoint_derivative_interval']
    # On [L,2L] original Fourier leading norm >=e sqrt(K),
    # K=(L/2-1/(12B))/(32 L^2)>1/(65 L) for L=2^24.
    # sqrt(65)<9, sqrt(L)=4096, so main >e/(9*4096).
    assert (F(LAM,2)-F(1,12*B))/(32*LAM*LAM)>F(1,65*LAM)
    assert 65<9*9
    # Full two-sided highband derivative remainder:
    # (2d+sqrt(2B)m)/36 * sqrt(2/(3L^3))
    # < (2d+3m/2)/(36 L sqrt(L)).
    assert 2*B<F(3,2)**2
    assert F(2,3)<1
    radical_free_lower=e/F(9*4096)-(2*d+F(3,2)*m)/F(36*LAM*4096)
    assert radical_free_lower>F(1,10**6), 'certified original tail threshold NOT met'
    assert ii(n['original_source_certified_selected_highband_tail_norm_lower_interval'])[0]>F(1,10**6)
    H=F(nf398['original_NF375_fourth_highband_action_norm_upper'])
    tau=F(nf398['original_NF375_fourth_lowband_future_target'])
    rho=H+tau
    assert n['original_candidate_ball_radius_rho']==str(rho)
    assert H==F(n['original_source_highband_H'])
    # For every original j in J242 within rho of original j*,
    # ||B_high j||>1e-6-rho. Thus full-line original source mismatch
    # is >1e-6-rho-H >tau, but this remains only a FULL-LINE
    # sufficient method STOP, not physical mismatch lower.
    assert F(1,10**6)-rho-H>tau
    out={
       'pass':'NF404',
       'standing':'EXACT ORIGINAL J242 ENDPOINT FOURIER TAIL LOWER; WHOLE-LINE-ONLY METHOD STOP',
       'original_selected_endpoint_native_sha256':endsha,
       'original_selected_fourier_tail_native_sha256':nsha,
       'original_nf401_complete_selected_sha256':selsha,
       'original_nf398_highband_sha256':nf398sha,
       'physical_selected_endpoint_abs_lower':str(e),
       'physical_selected_derivative_abs_upper':str(d),
       'physical_selected_second_derivative_L2_upper':str(m),
       'independent_rational_fourier_tail_lower':str(radical_free_lower),
       'certified_true_original_selected_jstar_Fourier_tail_strict_lower':'1/1000000',
       'all_NF401_candidate_ball_whole_line_mismatch_strictly_above_target':True,
       'full_line_fourier_primal_sufficient_method_STOP':True,
       'original_supported_physical_lowband_candidate_STOP':False,
       'original_strong_full_multiplier_scalar_upper':False,
       'W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print('NF404 exact original selected Fourier-tail >1e-6; full-line sufficient-method STOP, supported physical OPEN')
if __name__=='__main__':main()
