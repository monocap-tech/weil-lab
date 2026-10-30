#!/usr/bin/env python3
"""NF404 independent exact Fraction receipt for TRUE original selected trace.

Accepts no original full-response norm or lowband upper, never treats
selected-trace as full multiplier action. No python-flint dependency.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib,sys
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
NATIVE='644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515'
FRAME='18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e'

def load(path):
    a=Path(path).read_bytes()
    return json.loads(a),hashlib.sha256(a).hexdigest()
def interval(a):
    assert len(a)==2
    lo,hi=map(F,a)
    assert lo<=hi
    return lo,hi
def max_abs(i):return max(abs(i[0]),abs(i[1]))
def min_abs(i):return F(0) if i[0]<=0<=i[1] else min(abs(i[0]),abs(i[1]))
def run(args):
    a,sha=load(args.native)
    selected,selsha=load(args.selected)
    cert,certsha=load(args.acceptance)
    assert selsha==NATIVE==a['parent_nf401_native_sha256']
    assert cert['native_sha256']==NATIVE
    assert a['parent_nf401_independent_acceptance_sha256']==certsha
    assert a['original_physical_frame_sha256']==FRAME
    assert a['original_rank']==242
    assert a['all_original_selected_raw_moments_interval_reproduced'] is True
    assert a['new_signed_kernel_cells']==0 and a['real_multiplier_pole_restored'] is True
    assert a['original_endpoint_trace_is_not_full_multiplier_response_trace'] is True
    for k in ('original_full_supported_multiplier_scalar_norm_upper_computed',
              'original_J_perpendicular_full_action_upper_computed',
              'original_lowband_upper_computed',
              'original_operator_domain_independently_audited'):
        assert a[k] is False
    assert a['W_ODD_NEG']==a['RH']=='OPEN'
    v=interval(a['original_selected_endpoint_value_interval'])
    der=interval(a['original_selected_endpoint_derivative_interval'])
    dv=interval(a['original_selected_endpoint_eval_dual_squared_interval'])
    dd=interval(a['original_selected_endpoint_derivative_dual_squared_interval'])
    p2=interval(a['native_reconstructed_selected_power_interval'])
    assert dv[0]>0 and dd[0]>0 and p2[0]>0
    # Certified endpoint and derivative traces satisfy the Hilbert
    # Riesz evaluation inequalities independently in exact Fraction.
    assert min_abs(v)**2 <= p2[1]*dv[1]
    assert min_abs(der)**2 <= p2[1]*dd[1]
    known_lo,known_hi=interval(selected['original_projected_norm_interval_outward'])
    assert p2[0]<=known_hi**2 and p2[1]>=known_lo**2
    assert a['accepted_original_selected_projection_norm_interval']==selected['original_projected_norm_interval_outward']
    out={
       'pass':'NF404',
       'standing':'INDEPENDENT EXACT ORIGINAL J242 SELECTED ENDPOINT TRACE RECEIPT ONLY',
       'original_native_endpoint_report_sha256':sha,
       'original_nf401_selected_native_sha256':selsha,
       'original_nf401_exact_acceptance_sha256':certsha,
       'selected_endpoint_value_outward_interval':a['original_selected_endpoint_value_interval'],
       'selected_endpoint_derivative_outward_interval':a['original_selected_endpoint_derivative_interval'],
       'selected_endpoint_strict_nonzero':min_abs(v)>0,
       'selected_endpoint_abs_lower_exact':str(min_abs(v)),
       'selected_endpoint_abs_upper_exact':str(max_abs(v)),
       'selected_endpoint_derivative_abs_lower_exact':str(min_abs(der)),
       'selected_endpoint_derivative_abs_upper_exact':str(max_abs(der)),
       'independent_original_selected_projected_norm_overlap':True,
       'independent_original_selected_trace_cauchy_bounds_pass':True,
       'original_full_supported_multiplier_response_norm_upper':False,
       'original_lowband_upper':False,
       'W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2)+'\n')
    print('NF404 independent source-native endpoint certificate PASS; selected trace nonzero:',out['selected_endpoint_strict_nonzero'])
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--native',required=True)
    p.add_argument('--selected',default='notes/data/provisional/NF401_original_242D_selected_column_source_native.json')
    p.add_argument('--acceptance',default='notes/data/provisional/NF401_original_242D_selected_column_independent_acceptance.json')
    p.add_argument('--output',required=True)
    run(p.parse_args())
