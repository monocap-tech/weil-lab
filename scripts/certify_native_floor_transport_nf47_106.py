#!/usr/bin/env python3
"""NF47: same-domain F112 floor, stored packet algebra, exact full-domain split.

This does not replace NF46's missing original-archive replay or certify the
remaining 53-direction Schur block. Historical files are read-only inputs.
"""
import argparse
import ast
import hashlib
import json
import re
import sys
from fractions import Fraction as F
from pathlib import Path

sys.set_int_max_str_digits(0)
import certify_native_prime8_complement_nf10_106 as floor
import certify_native_next_shell_nf46_106 as packet
import certify_native_remaining_background_nf31_106 as frame
import validate_native_next_shell_nf46_106 as packet_check

BASE = '6658ff2837838ab00b9b9c605fdd200d473c3293'
KAPPA = F(207, 1000)
MISSING = [
    ('nf24-inputs/Weil/native112_N720_K620.json.gz', 'f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81'),
    ('nf24-inputs/Weil/native_boundary_columns_112_113.json.gz', 'da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee'),
    ('nf24-inputs/Weil/native_boundary_114_115.json.gz', '0a8f4ebd0778fa5c90209b3021d22791bdb0d9b73e0f19df608e04ed9ba2bcad'),
]


def read(name):
    return json.loads(Path(name).read_bytes())


def data(suffix, milestone):
    return read(f'notes/data/RPB108_NF{milestone}_{suffix}_20261009.json')


def custody():
    # Exact immutable inputs needed here, including every module imported by
    # the historical algebra helpers. No off-repository archive is fabricated.
    names = set()
    pending = [Path(m.__file__) for m in [floor, packet, frame, packet_check]]
    while pending:
        path = pending.pop()
        name = 'scripts/' + path.name
        if name in names:
            continue
        names.add(name)
        for node in ast.walk(ast.parse(path.read_text())):
            modules = ([a.name for a in node.names] if isinstance(node, ast.Import)
                       else [node.module] if isinstance(node, ast.ImportFrom) else [])
            for module in modules:
                if module and Path('scripts', module+'.py').is_file():
                    pending.append(Path('scripts', module+'.py'))
    for path in Path('notes/data').glob('RPB108_NF*'):
        match = re.match(r'RPB108_NF(\d+)_', path.name)
        if match and 10 <= int(match[1]) <= 46:
            names.add(path.as_posix())
    return {p: hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in names
            if '_nf47_' not in p and '_NF47_' not in p}


def original_columns(idx):
    """NF35 physical columns followed by NF37's frozen high-only map.

    No native matrix or approximate source is needed to recover physical
    vectors. Their low projections stay exactly x,w,u after the high map.
    """
    target = data('COMPENSATED_SOURCE_TARGETS', 24)['authenticated_compensated_targets'][idx]
    y = data('FIXED_HIGH_CORRECTIONS', 26)['parities'][idx]
    w = list(map(F, data('RETAINED_COUPLING_CERTIFICATE', 27)['parity_certificates'][idx]['exact_rational_retained_response']))
    lift = data('LIFTED_RESPONSE_CERTIFICATE', 29)['parity_certificates'][idx]
    shared = data('FIXED_SHARED_REMAINING_LIFT', 33)['parities'][idx]
    expanded = data(('EVEN' if idx == 0 else 'ODD') + '_FIXED_EXPANDED_SHARED_LIFT', 34)
    ids = target['retained_indices']
    x = list(map(F, target['retained_coefficients']))
    u_all = list(map(F, shared['fixed_probe_coefficients']))
    u = u_all[:56]
    vi = ids + target['high_indices'] + y['high_indices']
    vc = list(map(F, target['retained_coefficients'] + target['exact_rational_high_compensation'])) + [-F(v) for v in y['rational_correction_coefficients']]
    ti = ids + lift['high_lift_indices']
    tc = w + [-F(v) for v in lift['fixed_rational_high_lift']]
    if idx == 0:
        extra = data('FIXED_EXPANDED_RESPONSE', 30)
        ti += extra['additional_high_indices']
        tc += [-F(v) for v in extra['fixed_rational_coefficients']]
    ui = ids + shared['high_indices'] + expanded['additional_high_indices']
    uc = u_all + [-F(v) for v in expanded['fixed_rational_additional_coefficients']]
    assert len(ui) == len(uc)
    z = data(('EVEN' if idx == 0 else 'ODD') + '_FIXED_COLLECTIVE_CORRECTION', 36)
    selected = data(('EVEN' if idx == 0 else 'ODD') + '_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE', 37)
    high = (z['correction_indices'], list(map(F, z['fixed_rational_correction_coefficients'])))
    lam = list(map(F, selected['selected_rational_functional']))
    columns = [packet.p.c.merge([col, high], [F(1), -v])
               for col, v in zip([(vi, vc), (ti, tc), (ui, uc)], lam)]
    trial38 = data(('EVEN' if idx == 0 else 'ODD') + '_FIXED_SECOND_HIGH_DIRECTION', 38)
    merged = packet.p.c.merge(columns, list(map(F, trial38['exact_moved_target_coefficients'])))
    assert merged == (trial38['merged_target_indices'], list(map(F, trial38['merged_target_coefficients'])))
    for (ii, cc), low in zip(columns, [x, w, u]):
        lookup = dict(zip(ii, cc))
        assert [lookup[j] for j in ids] == low
    return ids, [x, w, u], columns


def remaining_frame(idx):
    ids, retained, columns = original_columns(idx)
    x, w, u = retained
    masses = [sum(v*v for v in row) for row in retained]
    assert min(masses) > 0
    assert all(sum(a*b for a, b in zip(retained[i], retained[j])) == 0
               for i in range(3) for j in range(i))
    t54, p, q, free = frame.complement(x, w)
    e = [sum(a*b for a, b in zip(u, col)) for col in zip(*t54)]
    pivot = max(range(54), key=lambda j: abs(e[j]))
    assert e[pivot] != 0
    remaining = [j for j in range(54) if j != pivot]
    t53 = [[row[j] - e[j]/e[pivot]*row[pivot] for j in remaining] for row in t54]
    assert all(sum(a*b for a, b in zip(r, col)) == 0
               for r in retained for col in zip(*t53))
    # Identity free rows prove rank 53 without numerical rank or conditioning.
    assert [[t53[free[j]][k] for k in range(53)] for j in remaining] == [
        [F(int(j == k)) for k in range(53)] for j in range(53)]
    return dict(parity=['even', 'odd'][idx], retained_indices=ids,
                retained_masses=list(map(str, masses)),
                old_two_constraint_pivots=[p, q], old_free_coordinates=free,
                third_constraint_pivot_in_old_free_coordinates=pivot,
                third_constraint_coordinates=list(map(str, e)),
                basis_rule='T53_j=T54_j-(u*T54_j)/(u*T54_pivot)*T54_pivot, j != pivot',
                exact_remaining_dimension=53, exact_constraints_and_free_row_identity=True,
                unchanged_joined_columns=[dict(indices=ii, coefficients=list(map(str, cc))) for ii, cc in columns],
                exact_retained_projection_masses_match_NF37=True,
                full_original_domain_decomposition='f=P alpha+T53 beta+h; h in F112, alpha determined by orthogonal retained projections')


def stored_packet(idx):
    suffix = 'EVEN_NEXT_SHELL_CERTIFICATE' if idx == 0 else 'ODD_INVERSE_WITNESS_CERTIFICATE'
    cert = data(suffix, 46 if idx == 0 else 45)
    old = data(('EVEN' if idx == 0 else 'ODD') + '_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE', 37)
    count = 'eight' if idx == 0 else 'seven'
    arrays = [packet.p.prev.matrix(cert[key]) for key in [
        count+'_high_physical_Gram', count+'_high_native_Gram', count+'_high_complete_source_Gram',
        'joined_'+count+'_high_native_crosses', 'joined_'+count+'_high_source_crosses']]
    g = packet.p.prev.matrix(old['original_selected_complete_source_Gram'])
    q = packet.p.prev.matrix(old['original_selected_native_energy_Gram'])
    _, _, _, _, _, response, cp, np = packet.inverse_packet(*arrays, g)
    assert packet.p.prev.ends(response) == cert['conditional_'+count+'_high_joined_inverse_upper_matrix']
    assert cp == cert[count+'_high_surplus_positive_proof']
    assert np == cert[count+'_high_inverse_denominator_positive_proof']
    lower = packet.symmetry(packet.c.add(q, packet.c.scale(response, -1)))
    assert packet.p.prev.ends(lower) == cert['conditional_'+count+'_high_joined_Schur_lower_matrix']
    leading = lower[0][0]*lower[1][1] - packet.n.sq(lower[0][1])
    margin = lower[2][2] - (lower[1][1]*packet.n.sq(lower[0][2]) - 2*lower[0][1]*lower[0][2]*lower[1][2] + lower[0][0]*packet.n.sq(lower[1][2]))/leading
    det = packet.p.c.parent.det3(lower)
    assert min(lower[0][0].l, leading.l, margin.l, det.l) > 0
    assert margin.ends() == cert['conditional_joined_condensed_margin']
    assert det.ends() == cert['conditional_joined_determinant']
    extra = packet_check.exact_algebra(cert) if idx == 0 else {}
    return dict(parity=['even', 'odd'][idx], high_columns=8 if idx == 0 else 7,
                stored_inverse_and_sign_replayed_exactly=True,
                condensed_margin=margin.ends(), determinant=det.ends(),
                fresh_original_source_replay=False, exact_eight_vs_seven_algebra=extra,
                original_source_custody='authenticated historical NF45/NF46 PASS; fresh replay requires the three original native archives')


def run():
    fresh = floor.certificate()
    saved = read('notes/data/RPB108_NF10_COMPLEMENT106_CERTIFICATE_20261008.json')
    assert fresh['aperture'] == saved['aperture'] == '53/50'
    assert fresh['full_prime_powers'] == saved['active_prime_powers'] == [2, 3, 4, 5, 7, 8]
    assert fresh['prime_interval_upper'] == saved['prime_operator_enclosure_6000']['upper']
    assert F(fresh['raw_complement_lower']) == F(saved['physical_complement_raw_lower_rounded'])
    assert fresh['masses_upper'] == saved['integrated_low_frequency_mass_uppers']
    lower = F(fresh['raw_complement_lower']) + F(13, 5) - F(fresh['prime_interval_upper'])
    assert lower > KAPPA
    rows = [remaining_frame(i) for i in range(2)]
    for i, row in enumerate(rows):
        cert37 = data(('EVEN' if i == 0 else 'ODD') + '_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE', 37)
        assert row['retained_masses'] == data(('EVEN' if i == 0 else 'ODD') + '_JOINED_WITNESSES_CERTIFICATE', 35)['inherited_retained_masses']
        assert cert37['kappa'] == str(KAPPA)
    return dict(milestone='NF47', base_commit=BASE, aperture='53/50',
                classification='same-domain infinite F112 floor audited; stored fixed packet algebra replayed; exact remaining-53 transport specified',
                background_floor=dict(kappa=str(KAPPA), strict_rebuilt_lower=str(lower),
                    strict_rational_surplus=str(lower-KAPPA), fresh_NF10_computation=fresh,
                    target='unshifted original Weil form on F112 = E112 physical L2 orthogonal complement, canonical supported logarithmic form domain',
                    source_approximation_shift_or_projection_off_high_columns=False,
                    applies_to_both_NF45_and_NF46_inverse_comparisons=True,
                    analytic_basis='NF10 high-frequency archimedean and signed-pole inequalities plus finite positive-region Bessel iteration and full infinite tail; no finite-matrix-to-floor inference'),
                parity_frames=rows, stored_packet_algebra=[stored_packet(i) for i in range(2)],
                literal_NF46_reproduction=dict(status='BLOCKED_MISSING_ORIGINAL_NATIVE_ARCHIVES',
                    archives=[dict(path=p, uncompressed_sha256=s, present=Path(p).exists()) for p, s in MISSING],
                    historical_committed_validation_status=data('NEXT_SHELL_VALIDATION', 46)['status'],
                    no_fresh_original_source_PASS_claimed=True),
                full_transport=dict(high_operator='A=Q restricted to F112', P='three unchanged lifted NF37 physical columns',
                    T='exact 53-dimensional retained constraint frame per parity', R='PF112 L P', G='PF112 L T',
                    exact_schur_blocks=dict(S='Q(P,P)-R* A^-1 R', D='Q(T,T)-G* A^-1 G', B='Q(T,P)-G* A^-1 R'),
                    exact_whole_nonnegativity_gate='D-B S^-1 B* >= 0 (S>0 is supplied by fixed packet and same-domain floor)',
                    strict_sufficient_gate='D-B S^-1 B* > 0',
                    missing_paid_source_entries_per_parity=dict(G_Gram_symmetric=1431, R_G_signed=159,
                        T_native_Gram_symmetric=1431, T_P_native_signed=159,
                        G_U_signed_even=424, G_U_signed_odd=371),
                    finite_native_gap_is_not_high_condensed_gap=True,
                    infinite_remainders_must_use_complete_L2_sources_and_uniform_operator_error=True),
                input_sha256=custody(), unconditional_F112_floor=True,
                fixed_joined_floor_hypothesis_discharged=True,
                fixed_joined_original_source_replay_newly_completed=False,
                complete_remaining_transport_certified=False, whole_aperture_positive=False,
                highest_certified_whole_aperture='21/20', RH=False, F4=False, Lean=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    Path(args.output).write_text(json.dumps(run(), indent=2, sort_keys=True)+'\n')
