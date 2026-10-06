#!/usr/bin/env python3
"""Export a small outward enclosure of the hash-pinned complete residual Gram."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

GRAM_SHA256 = '32f664f3e4a686dd220755c18f8aa38b790955b9c6b1a08e99fb8c5ac3a1615c'


def export(path):
    raw = Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest() != GRAM_SHA256:
        raise ValueError('Original complete Gram hash mismatch')
    original = json.loads(raw)
    result = {k:v for k,v in original.items()
              if k not in ('residual_gram_surrogate','shifted_pivot_lower_bounds')}
    entries = original['residual_gram_surrogate']
    grid = 10**80
    triangle = []
    max_width = F(0)
    for i in range(84):
        for j in range(i+1):
            assert entries[i][j] == entries[j][i]
            lo, hi = map(F, entries[i][j])
            assert lo <= hi
            lower = (lo*grid).__floor__()
            upper = (hi*grid).__ceil__()
            assert F(lower,grid) <= lo <= hi <= F(upper,grid)
            triangle.append([str(lower),str(upper)])
            max_width = max(max_width,F(upper-lower,grid))
    result.update(compact_enclosure=True, original_complete_gram_sha256=GRAM_SHA256,
                  compact_grid_digits=80, lower_triangle_row_major=triangle,
                  original_surrogate_trace_upper=str(sum((F(entries[i][i][1]) for i in range(84)),F(0))),
                  outward_triangle_inclusions_checked=len(triangle),
                  compact_enclosure_not_lossless=True,
                  status='outward compact enclosure of the pinned complete residual Gram',
                  original_interval_grid_digits=original['interval_grid_digits'],
                  original_maximum_entry_width=original['maximum_entry_width'],
                  interval_grid_digits=80, maximum_entry_width=str(max_width),
                  maximum_entry_width_display=float(max_width),
                  residual_interval_encoding='row-major lower triangle integer endpoints on grid 10^-80',
                  original_sign_fields_inherited=True)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',required=True)
    parser.add_argument('--output',required=True)
    args = parser.parse_args()
    Path(args.output).write_text(json.dumps(export(args.input),indent=2)+'\n')
