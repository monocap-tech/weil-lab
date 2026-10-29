#!/usr/bin/env python3
"""NF376 exact rational information-sufficiency screen on actual native fifth quotient.

Checks original GH Actions native report, no operator or lowband integration claim.
Positive physical independence is distinguished from useful out-of-fit orientation.
"""
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path

ORIGINAL_NATIVE_REPORT_SHA256 = 'da7f72f3e68005d1afe2225dffd3379c3b21cd1dfd813744b0f227130274f515'
ORIGINAL_NATIVE_ARTIFACT_ZIP_SHA256 = '05b2e0309d59dda9916808487e0bf6cb9b5f3d5010cc4d35caa3b7a576e553b9'
FITTED_FOUR_PARENT_SHA256 = '1b22cd77dd555749b8dcc41f92ddd91d982f2eca23ebf3a7638e512147b39d18'

def run(path):
    b=Path(path).read_bytes()
    assert hashlib.sha256(b).hexdigest()==ORIGINAL_NATIVE_REPORT_SHA256, 'Original native report modified'
    o=json.loads(b)
    assert o['status']=='CERTIFIED_ORIGINAL_QWITNESS_AND_SIGNED_LOWBAND_POINT_SAMPLES_ONLY'
    assert o['working_precision_bits']==4096 and o['original_selected_count']==242
    assert o['original_rank_sha256']=='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
    assert o['parent_16_original_physical_quotient_ball_overlap']
    assert o['original_nf369_fields_sha256']=='3e73a12bbd70158a461d9722dc8fc499eee8d17baf0afc9090bac5d10165e7e8'
    assert o['diagnostic_is_new_selected_source'] is False
    qlo,qhi=map(int,o['new_q_squared_norm_units_1e320'])
    elo,ehi=map(int,o['new_q_mod_E4_squared_norm_units_1e320'])
    assert qlo>0 and elo>0 and qhi>=qlo and ehi>=elo
    ratio_lower=F(elo,qhi)
    ratio_upper=F(ehi,qlo)
    # Certified normalized out-of-fit physical mass is ~2.82424e-20.
    assert F(28,10**21)<ratio_lower<=ratio_upper<F(3,10**20)
    # Equivalently, less than 2e-10 of physical norm is genuinely outside E4.
    assert ratio_upper < F(4,10**20)
    knots=o['actual_original_signed_point_samples']
    assert [x['frequency'] for x in knots]==['1/4','1/2','1','2','4','8','15','16','24','32']
    signs=[x['signed_cross_integrand_strict_sign'] for x in knots]
    assert set(signs)=={'positive','negative'} and signs.count('positive')==2 and signs.count('negative')==8
    assert o['original_lowband_integrated_signed_coupling_computed'] is False
    assert o['j_i_in_J242_constructed_for_lowband'] is False
    assert o['full_original_lowband_H_i_norm_computed'] is False
    assert o['W_ODD_NEG']==o['RH']=='OPEN'
    return {
      'status':'CERTIFIED_FINITE_SHADOW_INFORMATION_GATE_NOT_WEIL_OPERATOR_ACCEPTANCE',
      'native_report_sha256':ORIGINAL_NATIVE_REPORT_SHA256,
      'original_native_actions_zip_sha256':ORIGINAL_NATIVE_ARTIFACT_ZIP_SHA256,
      'native_github_actions_run':'40793727503',
      'old_fitted_four_parent_json_sha256':FITTED_FOUR_PARENT_SHA256,
      'physical_q5_norm_sq_lower_strict_positive':True,
      'physical_out_of_fitted_E4_norm_sq_lower_strict_positive':True,
      'normalized_out_of_E4_mass_ratio_interval_exact':[str(ratio_lower),str(ratio_upper)],
      'normalized_out_of_E4_mass_ratio_gt':'28/1000000000000000000000',
      'normalized_out_of_E4_mass_ratio_lt':'3/100000000000000000000',
      'normalized_out_of_E4_norm_ratio_lt':'2/10000000000',
      'signed_knot_positive_count':2,'signed_knot_negative_count':8,
      'positive_independence_does_not_certify_residual_obstruction':True,
      'signed_lowband_integral':'OPEN',
      'lowband_H4_residual':'OPEN',
      'whole_infinite_schur':'OPEN',
      'W_ODD_NEG':'OPEN','RH':'OPEN',
      'next_gate':'Require signed interval integral of m*uhat*conj(qhat) against true independent exterior q (or q_perp); compare > h4*norm(q) for necessary-condition STOP. Use verified alignment ratio before choosing additional probes.'
    }

def main():
    p=argparse.ArgumentParser();p.add_argument('--native',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    out=run(a.native)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
    print('PASS NF376: genuinely new q5 orientation has less than 3e-20 of physical squared mass outside fitted E4; 10 original signed knots not an integral')
if __name__=='__main__':main()
