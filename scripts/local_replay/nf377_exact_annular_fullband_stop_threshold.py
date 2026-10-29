#!/usr/bin/env python3
"""NF377 exact-rational full-frequency sign-box decision threshold.

This is arithmetic about a prospective sufficient-method STOP, not a signed
pairing evaluation or theorem transfer. Uses the original NF375 JSON.
"""
import argparse
import json
from fractions import Fraction as F
from pathlib import Path

RANK_SHA = '9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
SOURCE_SHA = 'abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770'
NATIVE_SHA = 'a725a6da6bf29ce21b1955df8f4d0b35b87ff8f003d09cdff13581d1b82f7559'

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--nf375', required=True)
    p.add_argument('--report', required=True)
    args = p.parse_args()
    j = json.loads(Path(args.nf375).read_text())
    assert j['source_sha256'] == SOURCE_SHA
    assert j['native_report_sha256'] == NATIVE_SHA
    assert j['measured_original_lowband'] is False
    assert len(j['directions']) == 4
    d = j['directions'][3]
    assert d['direction'] == 4
    window = next(x for x in d['dyadic_cutoff_options'] if x['cutoff'] == 2**20)
    assert window['log2_cutoff'] == 20 and window['exact_squared_original_individual_gate']
    beta = F(window['highband_upper'])
    h4 = F(window['chosen_future_lowband_target'])
    assert h4 == F(3, 2*10**13)
    assert beta == F(2850389356588036711829238471476032212853080316741097,
                     1572864 * 10**58)
    critical = h4 + beta
    explicit_upper = F(3313,10**16)
    assert F(3312, 10**16) < critical < explicit_upper
    B=F(11,10); n=492; step=B/n; strict_fraction=F(49,100)
    assert n == 2*(242+4)
    assert strict_fraction < F(1,2)
    assert step == F(11,4920)
    # For a selected q=(I-P_S)delta, ||q||^2 <= ||delta||^2 = step.
    # A strictly certified |W(u4,q)|^2 > critical^2 * step would suffice
    # to establish |I4(q;2^20)|/||q|| > h4, PROVIDED the whole-frequency
    # source identity and the highband bound both apply to that q.
    absolute_square_sufficient = critical * critical * step
    # Explicit (slightly looser) pure-rational threshold.
    absolute_square_display = explicit_upper * explicit_upper * step
    assert absolute_square_sufficient < absolute_square_display
    result = {
        'standing':'EXACT_RATIONAL_CONDITIONAL_FULLBAND_METHOD_STOP_DECISION_THRESHOLD_ONLY',
        'original_selected_count':242,
        'original_fitted_four_count':4,
        'rank_original_sha256':RANK_SHA,
        'source_original_sha256':SOURCE_SHA,
        'nf375_native_report_sha256':NATIVE_SHA,
        'cutoff':2**20,
        'annuli':n,
        'annulus_physical_squared_norm':str(step),
        'theoretical_maximum_residual_squared_fraction_lower':'1/2',
        'native_selector_strict_accepted_fraction':str(strict_fraction),
        'direction_four_highband_L2_norm_upper':str(beta),
        'direction_four_lowband_sufficient_target':str(h4),
        'conditional_normalized_fullband_stop_threshold':str(critical),
        'strict_easy_normalized_upper_to_threshold':str(explicit_upper),
        'sufficient_absolute_fullband_pairing_squared_threshold':str(absolute_square_sufficient),
        'strict_easy_absolute_pairing_squared_upper':str(absolute_square_display),
        'fullband_identity_with_original_signbox_pole_domain_proved':False,
        'selected_annulus_native_certified':False,
        'full_frequency_signed_pairing_measured':False,
        'original_lowband_signed_dual_measured':False,
        'NF375_method_stopped':False,
        'W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    dest=Path(args.report); dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('PASS exact NF375 highband + annular fullband conditional STOP threshold; NO signed measurement')

if __name__=='__main__':
    main()
