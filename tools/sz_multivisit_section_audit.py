#!/usr/bin/env python3
"""GERM-68: fixed-section multi-visit return certificate.

New exclusion: 2h+kappa < e <= 3h-kappa. Inherited local formulas: e<=3h.
Recomputes the two-/three-layer maps directly from the paired source rows
using outward rational Gaussian elimination. Certifies nine full-return
blocks, a single rational cone chart, and exact first-return geometry.
Requires the pinned GERM-65 interval helper (and its SymPy import), plus the
pinned GERM-67 output as a regression fixture. Run without Python -O.
No sampled topology, floating-point sign, or large determinant is used.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sz_mixed_return_cone_audit as old

assert __debug__, 'Assertions are part of this verifier; do not use -O.'
ROOT = Path(__file__).resolve().parents[1]
PINS = {
    'tools/sz_mixed_return_cone_audit.py':
        'f43eaf0e86e823a2f7ebeb6580b8ea12fcf4587ad405f708c3b66d6939b2a6c0',
    'notes/_recurrence67_audit.json':
        'db2dcd27d30ca3199c444e449d7a2b93b674a7fe2b2d4cc764b38a9a863e0b09',
}
for path, expected in PINS.items():
    assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected, path

box, mat, mm = old.box, old.mat, old.mm
PAIRS = [(s, n) for n in (5, 6) for s in range(1, n)]


def mdet(b):
    return b[0][0]*b[1][1] - b[0][1]*b[1][0]


def inverse(b):
    # Direct interval determinant, not an assumed determinant-one identity.
    return old.inv2(b, mdet(b))


def scale(c, v):
    return [c*x for x in v]


def vadd(*vs):
    return [sum((v[j] for v in vs), box(0)) for j in range(len(vs[0]))]


def norm_inf(b):
    return max(sum(max(abs(x.lo), abs(x.hi)) for x in row) for row in b)


def interval_solve(b, rhs):
    """Outward Gauss-Jordan; every physical pivot is separated from zero."""
    n = len(b)
    v = [r[:] + s[:] for r, s in zip(b, rhs)]
    pivots = []
    for k in range(n):
        i = max(range(k, n), key=lambda i: abs(v[i][k].lo + v[i][k].hi))
        v[i], v[k] = v[k], v[i]
        p = v[k][k]
        assert p.lo > 0 or p.hi < 0, ('uncertified pivot', k)
        pivots.append(p)
        v[k] = [x/p for x in v[k]]
        v[k][k] = box(1)  # Exact physical cancellation, not midpoint rounding.
        for i in range(n):
            if i == k:
                continue
            multiplier = v[i][k]
            v[i] = vadd(v[i], scale(-multiplier, v[k]))
            v[i][k] = box(0)
    return [row[n:] for row in v], pivots


def layer(m, a, d, mu):
    """GERM-67 equations (2)-(4),(6), without expanding symbolic inverses."""
    g, delta = 1-a, 1-mu*mu
    f, alpha = d/(g*delta), a/d
    eye = mat([[int(i == j) for j in range(2*m)] for i in range(2*m)])
    aa, bb = eye[::2], eye[1::2]
    cc = [vadd(scale(mu, x), y) for x, y in zip(aa, bb)]
    dd = [vadd(x, scale(mu, y)) for x, y in zip(aa, bb)]
    zero = scale(0, aa[0])
    w = [[aa[i], scale(f, vadd(dd[i], scale(-alpha, dd[i-1] if i else zero)))]
         for i in range(m)]
    v = [[scale(f, vadd(cc[i], scale(-alpha, cc[i+1] if i+1 < m else zero))), bb[i]]
         for i in range(m)]
    # W_0=(X,Y), followed by the paired source constraints R_i=S_i=0.
    rows = [w[0][0], w[0][1]]
    for i in range(m-1):
        rows.extend([
            vadd(aa[i], scale(a, w[i+1][1]), scale(-d, w[i][1]), scale(-a*g/d*f, dd[i])),
            vadd(scale(a, v[i][0]), bb[i+1], scale(-d, v[i+1][0]), scale(-a*g/d*f, cc[i+1])),
        ])
    rhs = mat([[int(i == 0), int(i == 1)] for i in range(2*m)])
    seeds, pivots = interval_solve(rows, rhs)
    # Consistency check only; correctness of the solve uses the pivot argument.
    residual = mm(rows, seeds)
    for i in range(2*m):
        for j in range(2):
            assert residual[i][j].lo <= rhs[i][j].lo <= residual[i][j].hi
    ll = [mm(t, seeds) for t in w]
    pp = [mm(t, seeds) for t in v]
    last = mm([scale(f, dd[-1])], seeds)[0]
    ym = vadd(scale(-1/a, ll[-1][0]), scale(d/a, ll[-1][1]), scale(g/d, last))
    xm = vadd(scale(g/d, ym), scale(a*g/(d*d), last))
    ll.append([xm, ym])
    nn = [mm(ll[i+1], inverse(ll[i])) for i in range(m)]
    kk = [mm(pp[i], inverse(ll[i])) for i in range(m)]
    for b in ll + nn + kk:
        assert norm_inf(b) < 300 and norm_inf(inverse(b)) < 300
    return {'L': ll, 'N': nn, 'K': kk, 'pivots': pivots}


def rational_audit():
    l2, l3, l5 = old.log_box(2), old.log_box(3), old.log_box(5)
    mu = (l3/l2)/old.sqrt_box(3)
    beta = (l3/l2)*old.sqrt_box(F(2, 3))
    d = (l5/l2)/old.sqrt_box(5)
    a = (beta*mu)**2
    assert 0 < mu.lo and mu.hi < 1 and a.lo > 1 and d.lo > 0
    layers = {m: layer(m, a, d, mu) for m in (2, 3)}
    g = 1-a
    m = mat([[(2*a-1)/(d*a), g/a], [-g/a, d/a]])
    mi, j = inverse(m), mat([[0, 1], [1, 0]])
    returns = {}
    # GERM-67's already-derived six local words, not six arbitrary generators.
    for key in ('00+', '10+', '11+', '00-', '01-', '11-'):
        source_m, target_m = 2+int(key[0]), 2+int(key[1])
        wrap = int(key[-1] == '-')
        b = mm(mm(mm(mm(inverse(layers[target_m]['L'][-1]),
                       old.mpow(mi, 4+wrap-target_m)), j), layers[source_m]['N'][-1]), j)
        returns[key] = mm(b, layers[source_m]['K'][0])
        assert mdet(returns[key]).lo > 0
    fixture = json.loads((ROOT/'notes/_recurrence67_audit.json').read_text())
    for key, b in returns.items():
        printed = fixture['rational_audit']['three_layer_returns'][key]
        for i in range(2):
            for j0 in range(2):
                lo, hi = map(F, printed[i][j0])
                assert lo <= b[i][j0].lo <= b[i][j0].hi <= hi, (key, i, j0)
    # One fixed rational chart for ALL nine legal full-return words.
    chart = mat([[1, 1], [F(1, 2), 2]])
    chart_inv = mat([[F(4, 3), F(-2, 3)], [F(-1, 3), F(2, 3)]])
    ordinary, exit_, inside, entry = (returns[k] for k in ('00+', '10+', '11+', '01-'))
    certified = {}
    for s, n in PAIRS:
        b = mm(mm(mm(old.mpow(ordinary, n-s-1), exit_), old.mpow(inside, s-1)), entry)
        conjugate = mm(mm(chart_inv, b), chart)
        sign = 1 if s <= 2 else -1
        positive = [scale(sign, row) for row in conjugate]
        assert all(x.lo > 0 for row in positive for x in row), (s, n)
        det = mdet(positive)
        assert det.lo > 0 and det.lo <= 1 <= det.hi
        forward = min(positive[0][0].lo+positive[1][0].lo,
                      positive[0][1].lo+positive[1][1].lo)
        backward = min(positive[1][1].lo+positive[1][0].lo,
                       positive[0][1].lo+positive[0][0].lo)/det.hi
        assert forward > F(5, 4) and backward > F(5, 4), (s, n)
        certified[f'{s}/{n}'] = {
            'overlap_visits': s, 'total_rotation_steps': n,
            'chronological_word': ['01-']+['11+']*(s-1)+['10+']+['00+']*(n-s-1),
            'overall_sign': sign,
            'positive_conjugate': old.display_matrix(positive),
            'determinant_enclosure': old.display_matrix([[det]]),
            'forward_lower': old.outward_decimal(forward, 8),
            'backward_lower': old.outward_decimal(backward, 8),
        }
    # The old short two-visit excursion is still elliptic; it was not erased.
    short = mm(mm(exit_, inside), entry)
    trace = short[0][0]+short[1][1]
    assert F(18, 10) < trace.lo and trace.hi < F(19, 10)
    # Just above eta=lambda, a source-overlap wrap changes 01- to 11-.
    changed = mm(mm(exit_, old.mpow(inside, 4)), returns['11-'])
    changed = mm(mm(chart_inv, changed), chart)
    assert changed[0][0].hi < 0 and changed[0][1].lo > 0
    assert changed[1][0].hi < 0 and changed[1][1].hi < 0
    return {
        'local_source_recalculation': 'OUTWARD RATIONAL GAUSSIAN ELIMINATION',
        'layer_pivots': {str(m): old.display_matrix([b['pivots']]) for m, b in layers.items()},
        'local_maps_and_inverses_inf_bound': 300,
        'parent_six_matrix_enclosures': 'ALL RECOMPUTED ENCLOSURES CONTAINED IN PINNED BOXES',
        'chart': [['1', '1'], ['1/2', '2']],
        'common_forward_backward_factor': '5/4',
        'full_return_blocks': certified,
        'old_two_visit_elliptic_trace': old.display_matrix([[trace]]),
        'above_scope_changed_word': ['11-']+['11+']*4+['10+'],
        'above_scope_conjugate': old.display_matrix(changed),
        'above_scope_old_signed_quadrant_test': 'FAILS: MIXED ENTRY SIGNS',
    }


# Affine expressions in (r, eta, z), normalized by h; all coefficients rational.
def af(c=0, r=0, eta=0, z=0):
    return tuple(map(F, (c, r, eta, z)))


def add(x, y): return tuple(a+b for a, b in zip(x, y))
def sub(x, y): return tuple(a-b for a, b in zip(x, y))
def value(x, vertex): return x[0]+sum(a*b for a, b in zip(x[1:], vertex))


def exact_solve3(rows):
    a = [list(row[1:])+[-row[0]] for row in rows]
    for k in range(3):
        p = next((i for i in range(k, 3) if a[i][k]), None)
        if p is None: return None
        a[p], a[k] = a[k], a[p]
        pivot = a[k][k]
        a[k] = [x/pivot for x in a[k]]
        for i in range(3):
            if i == k: continue
            factor = a[i][k]
            a[i] = [x-factor*y for x, y in zip(a[i], a[k])]
    return tuple(row[-1] for row in a)


def vertices(constraints):
    answer = set()
    for rows in combinations(constraints, 3):
        vertex = exact_solve3(rows)
        if vertex is not None and all(value(row, vertex) >= 0 for row in constraints):
            answer.add(vertex)
    assert answer, 'Empty closed parameter polytope.'
    return sorted(answer)


def geometry_audit():
    kappa, h = old.KAP, old.H
    fixed = {
        'kappa_positive': kappa,
        'tau_positive': old.sub(h, old.mul(5, kappa)),
        'kappa_minus_tau_positive': old.sub(old.mul(6, kappa), h),
        'kappa_minus_2tau_positive': old.sub(old.mul(11, kappa), old.mul(2, h)),
    }
    assert all(old.prime_sign(v[:3]) > 0 for v in fixed.values())
    r, eta, z = af(r=1), af(eta=1), af(z=1)
    one, lam, tau = af(1), af(1, r=-1), af(1, r=-5)
    common = (af(F(-1, 6), r=1), af(F(1, 5), r=-1),
              sub(eta, r), sub(lam, eta), z, sub(r, z))
    result = {}
    for s, n in PAIRS:
        conditions = common+(sub(z, tau) if n == 5 else sub(tau, z),
                             sub(eta, af(r=s-1, z=1)), sub(af(r=s, z=1), eta))
        vv = vertices(conditions)
        points = [af(1, r=-1, z=1)]+[af(r=j-1, z=1) for j in range(1, n+1)]
        margins = []
        for j0, pt in enumerate(points):
            margins.extend((pt, sub(one, pt)))
            margins.append(sub(eta, pt) if 1 <= j0 <= s else sub(pt, eta))
            margins.append(sub(pt, lam) if j0 in (0, n) else sub(lam, pt))
        for margin in margins:
            values = [value(margin, v) for v in vv]
            assert min(values) >= 0 and max(values) > 0, (s, n, margin)
        assert sub(points[-1], lam) == (af(-1, r=5, z=1) if n == 5 else af(-1, r=6, z=1))
        item = {'parameter_vertices': len(vv), 'source_word_domains': 'PASS',
                'first_return_no_earlier_section_hit': 'PASS'}
        if (s, n) in ((4, 5), (5, 6)):
            end = vertices(conditions+(sub(eta, lam),))
            for margin in margins:
                values = [value(margin, v) for v in end]
                assert min(values) >= 0 and max(values) > 0
            item['eta_equals_lambda_face'] = 'PASS'
        result[f'{s}/{n}'] = item
    # Exact tiling under z -> z-tau mod r, independently of eta.
    images = [(sub(tau, tau), sub(r, tau)),
              (sub(r, tau), add(tau, sub(r, tau)))]
    assert images == [(af(), af(-1, r=6)), (af(-1, r=6), r)]
    # Above-scope guard: delta=eta-lambda, 0<z<delta<tau.
    # r>2tau is separately certified by prime powers above.
    delta = sub(eta, lam)
    guard = (af(F(2, 11)*-1, r=1), af(F(1, 5), r=-1),
             delta, sub(tau, delta), z, sub(delta, z))
    vv = vertices(guard)
    points = [af(1, r=-1, z=1)]+[af(r=j, z=1) for j in range(6)]
    for j0, pt in enumerate(points):
        margins = [pt, sub(one, pt), sub(eta, pt) if j0 < 6 else sub(pt, eta),
                   sub(pt, lam) if j0 in (0, 6) else sub(lam, pt)]
        for margin in margins:
            values = [value(margin, v) for v in vv]
            assert min(values) >= 0 and max(values) > 0, ('scope guard', j0)
    return {'fixed_prime_power_inequalities': 'PASS',
            'parameter_scope': 'kappa < eta <= lambda = h-kappa',
            'section': '(lambda,h)', 'section_coordinate': 't=lambda+z, 0<z<kappa',
            'return_time': '6 for z<tau; 5 for z>tau',
            'induced_map': 'z -> z-tau mod kappa',
            'image_tiling': 'EXACT; Lebesgue measure preserved',
            'all_nine_word_cells': result, 'endpoint_eta_equals_lambda': 'PASS',
            'above_scope_guard': '0<z<eta-lambda<tau; changed six-step word verified',
            'sampled_topology': False}


def main():
    endpoint = F(16, 3)*F(81, 80)**8/F(16, 15)
    assert endpoint == F(3**32, 2**32*5**7)
    out = {'pass': 'SZ-KERNEL-EDGE-GERM-68', 'standing': 'UNRATIFIED',
           'entry_commit': '1a2738cf539efb7d50644be1e47d64d94db66134',
           'inherited_formula_scope': '2h < e <= 3h',
           'new_exclusion_scope': '2h+kappa < e <= 3h-kappa',
           'experimental_endpoint': 'log(3^32/(2^32*5^7))',
           'endpoint_rational': str(endpoint), 'dependency_sha256': PINS,
           'rational_audit': rational_audit(), 'exact_geometry': geometry_audit(),
           'full_parent_symbolic_suite_rerun': False, 'old_large_determinants_rerun': False,
           'canonical_cursor': 'SZ-CROSS-COLLAR-3', 'canonical_effect': 'NONE'}
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
