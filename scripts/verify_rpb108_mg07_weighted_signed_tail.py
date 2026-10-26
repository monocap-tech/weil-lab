#!/usr/bin/env python3
"""Replay weighted signed tails from a SHA-pinned accepted GH artifact.

No low-frequency integration. SI10 geometry is recomputed from repository
source. Inherited Fourier, support-cutoff, domain and pole proofs remain
analytic assumptions; this check certifies the rational composition only.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from validate_rpb108_si10_complement_positivity import protected_inner_cover

CANONICAL_JSON_SHA256 = 'ded28038988836dfa9cdb0ceeb0036d6efebc9c32f83faef5e904e598e155b83'
RUN = 40251400717
ARTIFACT = 12620838774
SOURCE_SHA = 'bf56f5ca1a17305671f58c8a5b785898a1843d55'


def verify(path):
    raw = Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == CANONICAL_JSON_SHA256
    data = json.loads(raw)
    assert data['status'] == 'EXACT_ORIGINAL_SIGNED_STOPPING_RAY_7168CELL_CERTIFICATE'
    assert data['signed_frequency_cells'] == 7168
    assert data['entire_whole_real_Knegative_high12_paid'] is True
    assert data['original_signed_multiplier_all_seven_prime_powers'] is True
    assert data['original_quarter_digamma_source'] is True
    assert data['exact_original_J_membership']['both_rays_exact_original_J_membership'] is True
    assert data['exact_original_J_membership']['original_SM35_J_source_dim'] == 470
    clusters, width, mass, leaves, accepted = protected_inner_cover()
    assert len(clusters) == 107 and leaves == 973 and accepted > 0
    assert mass == F(1203060883, 32000000)
    assert all(0 <= a < b <= 896 and m >= 0 for a, b, m in clusters)
    assert all(clusters[i][1] < clusters[i+1][0] for i in range(106))
    assert all(not (a < 12 < b) for a, b, m in clusters)
    tail = [(a, b, m) for a, b, m in clusters if a >= 12]
    assert len(tail) == 94
    tail_mass = sum((m for a, b, m in tail), F(0))
    assert tail_mass == F(502297951, 32000000)
    weighted = sum((m / a**2 for a, b, m in tail), F(0))
    assert 0 < weighted < F(423, 25000) < tail_mass / 144
    labels = ['direct_Knegative_selected', 'SM40_cap_selected']
    assert [r['ray'] for r in data['true_rays']] == labels
    assert [r['ray'] for r in data['high_negative_tail']] == labels
    rows = []
    for r, t, target in zip(data['true_rays'], data['high_negative_tail'],
                            [F('25772.048'), F('1691.180')]):
        low = F(r['signed_low0_12_original_multiplier_lower'])
        assert low == sum((F(p['ray_signed_lower_contributions'][r['ray']])
                           for p in data['frequency_regions']), F(0))
        pole = F(r['genuine_original_pole_payment_upper'])
        old_tail = F(r['signed_high12_negative_action_upper'])
        old_lower = F(r['complete_original_signed_Q_odd_lower'])
        assert low - pole - old_tail == old_lower > 0
        beta = F(t['true_Fourier_xi_times_amplitude_upper_high12'])
        new_tail = beta**2 * weighted
        new_lower = low - pole - new_tail
        assert 0 < new_tail < old_tail
        assert new_lower == old_lower + old_tail - new_tail > target
        rows.append(dict(ray=r['ray'], unchanged_lowband=str(low),
                         unchanged_pole=str(pole), beta=str(beta),
                         previous_tail_upper=str(old_tail), previous_lower=str(old_lower),
                         weighted_tail_upper=str(new_tail), signed_lower=str(new_lower),
                         strict_display_lower=str(target)))
    assert data['signed_odd_operator_positive_ON_ALL_HILBERT_SPACE'] == 'OPEN'
    assert data['even_CC27_Weil_RH'] == 'OPEN'
    return dict(status='EXACT_WEIGHTED_SIGNED_TWO_RAY_COMPOSITION_PASS',
                canonical_run_id=RUN, canonical_artifact_id=ARTIFACT,
                canonical_source_sha=SOURCE_SHA, canonical_json_sha256=CANONICAL_JSON_SHA256,
                si10_replayed_clusters=107, si10_replayed_leaves=leaves,
                high12_clusters=94, high12_two_sided_mass=str(tail_mass),
                high12_weighted_inverse_square=str(weighted), strict_weighted_upper='423/25000',
                low_frequency_integration_repeated=False, extra_reflection_factor=False,
                rays=rows, inherited_analytic_assumptions_reproved=False,
                whole_original_odd_positivity='OPEN', even_CC27_Weil_RH='OPEN')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--canonical', required=True)
    parser.add_argument('--output', default='artifacts/mg07_weighted_signed_tail.json')
    args = parser.parse_args()
    result = verify(args.canonical)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + '\n')
    print('Weighted signed tail PASS:', float(F(result['high12_weighted_inverse_square'])))
    for row in result['rays']:
        print(row['ray'], 'Q >', row['strict_display_lower'])
