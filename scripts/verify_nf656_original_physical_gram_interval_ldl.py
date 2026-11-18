#!/usr/bin/env python3
"""NF656: exact outward-rounded LDL^T pivot test for the original 15-source H block.

Input: NF631 widened physical entry balls, with source and checksum custody
provided by the retained NF631 widening manifest. Every arithmetic operation
after reading source integers is integer-exact and rounded OUTWARDS at 10^-160.
This proves strict positivity for every real symmetric matrix inside the
specified 120 input entry intervals. It does NOT establish analytic containment
of the physical H entries (separate NF655 Lean obligation), nor Lean positivity.
"""
import argparse, gzip, hashlib, json, sys
from pathlib import Path

sys.set_int_max_str_digits(0)
Q = 10 ** 2600
S = 10 ** 160
INDICES = list(range(14)) + [241]
N = len(INDICES)
LOC = {i: k for k, i in enumerate(INDICES)}

def sha(b):
    return hashlib.sha256(b).hexdigest()

def ceildiv(a, b):
    assert b > 0
    return -((-a) // b)

def add(a, b):
    return a[0] + b[0], a[1] + b[1]

def neg(a):
    return -a[1], -a[0]

def sub(a, b):
    return add(a, neg(b))

def mul(a, b):
    p = [x * y for x in a for y in b]
    return min(p) // S, ceildiv(max(p), S)

def div(a, b):
    assert b[0] > 0
    corners = [(x * S, y) for x in a for y in b]
    return min(x // y for x, y in corners), max(ceildiv(x, y) for x, y in corners)

def enclosure(mid, rad):
    assert rad >= 0
    return (mid - rad) * S // Q, ceildiv((mid + rad) * S, Q)

def interval_ldl(a):
    n = len(a)
    assert n == N and all(len(row) == n for row in a)
    assert all(a[i][j] == a[j][i] for i in range(n) for j in range(n))
    L = [[None] * n for _ in range(n)]
    D = []
    for k in range(n):
        v = a[k][k]
        for j in range(k):
            v = sub(v, mul(mul(L[k][j], L[k][j]), D[j]))
        if v[0] <= 0:
            raise AssertionError(f"Nonpositive or unresolved LDL pivot {k}")
        D.append(v)
        for i in range(k + 1, n):
            t = a[i][k]
            for j in range(k):
                t = sub(t, mul(mul(L[i][j], L[k][j]), D[j]))
            L[i][k] = div(t, v)
    return D

def source_matrix(entries, summary):
    meta = json.loads(summary.read_text())
    raw = entries.read_bytes()
    assert meta['schema'] == 'NF631-reference-widening-v1'
    assert sha(raw) == meta['widened_entry_sha256']
    assert len(meta['input_sha256']) == 8
    A = [[None] * N for _ in range(N)]
    originals = {}
    with gzip.open(entries, 'rt') as f:
        head = json.loads(next(f))
        assert head['schema'] == 'NF622-original-physical-entry-balls-v1'
        assert head['scale'] == '10^2600'
        assert head['original_entry_sha256'] == meta['original_entry_sha256']
        for i, line in enumerate(f):
            row = json.loads(line)
            assert row['row'] == i and len(row['H_lower']) == i + 1
            if i not in LOC:
                continue
            for j in INDICES:
                if j > i:
                    continue
                mid, rad = map(int, row['H_lower'][j])
                x = enclosure(mid, rad)
                A[LOC[i]][LOC[j]] = A[LOC[j]][LOC[i]] = x
                originals[(i, j)] = mid, rad
    assert len(originals) == N * (N + 1) // 2 == 120
    assert all(all(v is not None for v in row) for row in A)
    return A, originals, meta

def sci(a, digits=19):
    # Presentation only; the certificate uses the entire integer a.
    if a == 0:
        return "0"
    sign = "-" if a < 0 else ""
    v = str(abs(a))
    exponent = len(v) - 1 - 160
    return f"{sign}{v[0]}.{v[1:digits].ljust(digits - 1, '0')}e{exponent:+d}"

def self_test():
    # Test outward inclusion against exact rational multiplication/division.
    from fractions import Fraction as F
    tests = [((-8, 7), (-13, -2)), ((0, 13), (-4, 4)), ((-25, -10), (1, 24))]
    for a, b in tests:
        am = (F(a[0], S), F(a[1], S))
        bm = (F(b[0], S), F(b[1], S))
        prod = mul(a, b)
        corners = [x * y for x in am for y in bm]
        assert F(prod[0], S) <= min(corners) and F(prod[1], S) >= max(corners)
    assert ceildiv(-1, 3) == 0 and ceildiv(1, 3) == 1
    assert enclosure(-Q // 3, 1)[0] <= -S // 3
    print("NF656 signed outward rounding self-test PASS")

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--entries', type=Path)
    p.add_argument('--summary', type=Path)
    p.add_argument('--output', type=Path)
    p.add_argument('--self-test', action='store_true')
    a = p.parse_args()
    if a.self_test:
        self_test()
        return
    assert a.entries and a.summary and a.output
    A, originals, manifest = source_matrix(a.entries, a.summary)
    pivots = interval_ldl(A)
    report = {
        'schema': 'NF656-original-physical-gram-interval-ldl-v1',
        'source_schema': manifest['schema'],
        'widened_entry_sha256': manifest['widened_entry_sha256'],
        'original_entry_sha256': manifest['original_entry_sha256'],
        'indices': INDICES,
        'shape': [N, N],
        'lower_triangle_input_intervals': len(originals),
        'fixedpoint_denominator': '10^160',
        'original_entry_denominator': '10^2600',
        'positive_lower_pivots': sum(d[0] > 0 for d in pivots),
        'pivots': [
            {
                'index': i,
                'lower_integer': str(d[0]),
                'upper_integer': str(d[1]),
                'lower_scientific': sci(d[0]),
                'upper_scientific': sci(d[1]),
                'width_scientific': sci(d[1] - d[0]),
            }
            for i, d in enumerate(pivots)
        ],
        'min_lower_pivot': min((d[0], i) for i, d in enumerate(pivots))[1],
        'max_input_radius_units_at_2600': str(max(r for _, r in originals.values())),
        'conditional_claim': (
            'Every real symmetric 15x15 matrix with all 120 lower-triangle '
            'entries in the retained NF631 entry intervals is positive definite'
        ),
        'remaining_lean_premises': [
            'The 120 actual physical H containment theorems',
            'Symmetry of the original physical H block',
            'Formal validation of fixedpoint interval LDL and Sylvester transfer',
        ],
        'scope': 'exact external integer proof search; no new Lean acceptance',
    }
    assert len(pivots) == 15 and all(d[0] > 0 for d in pivots)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(report, indent=2) + '\n')
    print("NF656 all 15 rigorously outward-rounded positive LDL pivots PASS")
    print("NF656 minimum lower pivot:", report['pivots'][report['min_lower_pivot']]['lower_scientific'])
    print("NF656 positive matrix interval conditional on Lean H enclosures")

if __name__ == '__main__':
    main()
