#!/usr/bin/env python3
"""Recheck the stored native 84-vector interval matrix; finite restriction only."""
import argparse
import hashlib
import json
from pathlib import Path

from certify_native_legendre_small_window import F, I, positive_pivots

SOURCE_BLOB = '513b970b3d7d521c6d9f8b8f6551d550c99584d7'
SOURCE_PATH = 'notes/data/RPB108_PRIME5_MATRIX84_081_CERTIFICATE_20261005.json'


def certify(path):
    raw = Path(path).read_bytes()
    blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    if blob != SOURCE_BLOB:
        raise ValueError('Source Git blob hash mismatch')
    source = json.loads(raw)
    assert source['aperture'] == '81/100'
    assert source['physical_degrees'] == list(range(84))
    assert source['prime_terms'] == [2, 3, 4, 5]
    assert F(source['raw_physical_coercivity_lower_bound']) == F(1, 10**28)
    entries = source['matrix_intervals']
    assert len(entries) == 84 and all(len(row) == 84 for row in entries)
    I.grid = 10**60
    matrix = []
    checked = 0
    for i, row in enumerate(entries):
        target = []
        for j, entry in enumerate(row):
            lo, hi = map(F, entry)
            assert lo <= hi
            assert entry == entries[j][i]
            if (i-j) % 2:
                assert lo == hi == 0
            interval = I(lo, hi)
            assert interval.lo <= lo <= hi <= interval.hi
            target.append(interval)
            checked += 1
        matrix.append(target)

    def shifted_blocks(tau):
        blocks = []
        for parity in range(2):
            indices = list(range(parity, 84, 2))
            block = [[matrix[i][j] - (I(tau) if i == j else I(0))
                      for j in indices] for i in indices]
            blocks.append((indices, block))
        return blocks

    tau = F(1, 10**18)
    pivots = []
    for indices, block in shifted_blocks(tau):
        bounds = positive_pivots(block)
        pivots.append({'degrees': indices,
                       'shifted_pivot_lower_bounds': [str(p.lo) for p in bounds]})
    rejected = []
    for exponent in (16, 17):
        try:
            for _, block in shifted_blocks(F(1, 10**exponent)):
                positive_pivots(block)
        except ArithmeticError:
            rejected.append(str(F(1, 10**exponent)))
    control = [[I(-1), I(0)], [I(0), I(1)]]
    try:
        positive_pivots(control)
    except ArithmeticError:
        control_rejected = True
    else:
        raise AssertionError('Indefinite control accepted')
    return {
        'status': 'certified stronger native 84-vector finite restriction only',
        'source_path': SOURCE_PATH,
        'source_git_blob_sha': blob,
        'source_sha256': hashlib.sha256(raw).hexdigest(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'aperture': '81/100', 'physical_degrees': list(range(84)),
        'prime_terms': [2, 3, 4, 5],
        'physical_basis': source['physical_basis'],
        'interval_grid_digits': 60, 'outward_inclusions_checked': checked,
        'exact_symmetry_checked': True, 'exact_reflection_parity_checked': True,
        'previous_finite_coercivity_lower_bound': str(F(1, 10**28)),
        'finite_coercivity_lower_bound': str(tau), 'improvement_factor': 10**10,
        'parity_block_pivots': pivots,
        'larger_shifts_not_certified': rejected,
        'failed_shift_interpretation': 'No negativity or optimality conclusion.',
        'negative_control_rejected': control_rejected,
        'whole_domain_bound_updated': False,
        'existing_whole_domain_physical_bound': str(F(1, 202*10**29)),
        'positivity_frontier': '81/100',
        'actual_selected_source_packet_attached': False,
        'f4_entry_closed': False, 'full_transport_closed': False,
        'lean_formalized': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', default=str(Path(__file__).resolve().parents[1] / SOURCE_PATH))
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    result = certify(args.input)
    Path(args.output).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ('status', 'finite_coercivity_lower_bound',
                                           'improvement_factor', 'outward_inclusions_checked')}))
