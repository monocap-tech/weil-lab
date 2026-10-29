#!/usr/bin/env python3
"""NF380 independently replay native original unfitted response with exact Fractions.

The pinned native interval result is a source-adapted scalar W_odd(u4,q_512^perp),
NOT the full exterior Schur or a signed-form positivity/negativity result.
"""
import argparse, hashlib, json, sys
from fractions import Fraction as Q
from pathlib import Path
sys.set_int_max_str_digits(0)

REPORT_SHA = '9d4b07fb2ca42c14ed995ddcd69811201eacb6f13f9f795a70c4b64889e9f83b'
ZIP_SHA = 'a22ebb68982d783d88b22c3d18f3309f725d4840b2cb645ea90c5fc0a87a1eed'
PARENT_ARCHIVE_SHA = 'f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0'
SELECTED_SHA = '33b52b01e813982bd1a73b9bb81b0ca79f76e4bfd5af0821c4e13b4360bb40fa'
MIXED_SHA = '19356d4be60ee492896083c1bf6be18cd8ce2da058ff60008181f56a4c3ccc23'
SOURCE_SHA = 'abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770'
RANK_SHA = '9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
FRAME_SHA = '18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e'


def run(path):
    p = Path(path)
    b = p.read_bytes()
    assert hashlib.sha256(b).hexdigest() == REPORT_SHA, 'Original native output has changed'
    j = json.loads(b)
    expected = {
        'parent_original_archive_sha256': PARENT_ARCHIVE_SHA,
        'archive_original_signed_matrix_sha256': SELECTED_SHA,
        'archive_original_mixed_sha256': MIXED_SHA,
        'original_frame_sha256': FRAME_SHA,
        'original_rank_sha256': RANK_SHA,
        'original_source_sha256': SOURCE_SHA,
        'selected_rank': 242, 'critical_count': 4, 'unfitted_n': 512,
        'original_physical_16_Gram_overlaps': True,
        'original_signed_32_CE_BP_overlaps': True,
        'actual_new_signed_J_v_cells': 242,
        'actual_new_signed_basis_v_cells': 33,
        'original_WJJ_WJF_archived_cells_reused': 30371,
        'method_specific_sufficient_residual_obstructed': False,
        'original_lowband_integral_computed': False,
        'entire_exterior_inverse_computed': False,
        'analytic_domain_review': 'OPEN',
        'W_ODD_NEG': 'OPEN', 'RH': 'OPEN',
    }
    for key, value in expected.items():
        assert j[key] == value, (key, j[key])
    assert 'FULL SIGNED ONE-WITNESS RESPONSE' in j['standing']
    def pair(field):
        v = [Q(s) for s in j[field]]
        assert len(v) == 2 and v[0] <= v[1], field
        return v
    raw = pair('physical_q_norm2_interval')
    g = pair('outside_E4_norm2_interval')
    align = pair('relative_outside_E4_mass_interval')
    b = pair('complete_original_signed_u4_qperp_interval')
    assert raw[0] > Q(1) and g[0] > Q(1), 'No robust physical witness'
    assert 0 < g[0] <= g[1] <= raw[1], 'invalid outside-subspace geometry'
    assert align[0] > Q(99,100) and align[1] < 1, 'original orientation claim missing'
    assert align[0] <= g[1]/raw[0] and align[1] >= g[0]/raw[1], 'inconsistent interval ratio'
    assert b[0] > 0, 'original signed coupling is not proven positive'
    assert b[0] > Q(13,10**14) and b[1] < Q(14,10**14), 'point response scale changed'
    low = b[0]**2/g[1]
    up = b[1]**2/g[0]
    native_lower = Q(j['dual_squared_strict_lower'])
    budget = Q(j['original_direction_four_squared_residual_budget'])
    assert budget == Q(2401,2*10**28), 'inherited NF370 budget mismatch'
    assert 0 < native_lower <= low <= up < budget, 'witness method verdict not grounded'
    assert up/budget < Q(3,20), 'new witness is not well below the budget'
    assert low/budget > Q(1,7), 'new response is not quantitatively retained'
    out = {
      'standing':'INDEPENDENT EXACT FRACTION REPLAY OF ORIGINAL NF380 NATIVE ONE-WITNESS RESPONSE',
      'source_native_json_sha256': REPORT_SHA,
      'source_original_action_artifact_sha256': ZIP_SHA,
      'original_selected_count': 242,
      'original_unfitted_witness_n': 512,
      'actual_original_signed_source_orientations': 1,
      'source_16_physical_32_complete_signed_overlap_pass': True,
      'signed_coupling_strictly_positive': True,
      'physical_outside_fitted_four_relative_mass_strictly_above_99_percent': True,
      'normalized_squared_response_as_fraction_of_budget_strictly_above_1over7': True,
      'normalized_squared_response_as_fraction_of_budget_strictly_below_3over20': True,
      'actual_fixed_direction_four_method_obstruction_by_this_witness': False,
      'original_signed_lowband_integral_computed': False,
      'whole_original_exterior_strong_residual_upper_certified': False,
      'W_ODD_NEG':'OPEN', 'RH':'OPEN',
      'checks':'parent SHA, frame/source/archive, original 16+32 checks, fixed n512 and 275 new signed cells, actual physical norms, actual signed interval, dual lower/upper and unchanged NF370 residual budget'
    }
    return out

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--native', required=True)
    parser.add_argument('--output', required=True)
    args=parser.parse_args()
    result=run(args.native)
    Path(args.output).parent.mkdir(exist_ok=True,parents=True)
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print('PASS native actual signed response; squared budget ratio strictly (1/7,3/20), no method obstruction, RH OPEN',flush=True)
