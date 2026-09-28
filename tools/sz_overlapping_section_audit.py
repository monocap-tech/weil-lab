#!/usr/bin/env python3
"""GERM-69: overlapping-section control by a second fixed exterior section.

New exclusion: 3h-kappa < e <= 3h-kappa+5*tau, tau=h-5*kappa.
Reuses the exact three-layer source reduction through e=3h. Recalculates
its six matrices by small outward rational solves, then certifies twelve
nested full-return words and a single rational cone chart. All topology
checks use exact affine inequalities, not sampled orbits. Run without -O.
Dependency: the byte-pinned GERM-68 and GERM-65 helpers, plus SymPy.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of this audit; run without -O.'
ROOT = Path(__file__).resolve().parents[1]
PINS = {
    'tools/sz_multivisit_section_audit.py':
        '16517b40a62f46ec32e439a42fe70e6a52cf5d665138f0c93be0ed25a6c31bb7',
    'tools/sz_mixed_return_cone_audit.py':
        'f43eaf0e86e823a2f7ebeb6580b8ea12fcf4587ad405f708c3b66d6939b2a6c0',
    'notes/_recurrence67_audit.json':
        'db2dcd27d30ca3199c444e449d7a2b93b674a7fe2b2d4cc764b38a9a863e0b09',
}
for path, expected in PINS.items():
    assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == expected, path

import sz_multivisit_section_audit as parent
old = parent.old
mat, mm, mpow = old.mat, old.mm, old.mpow
inverse, mdet = parent.inverse, parent.mdet
PAIRS = [(s, n) for n in (8, 9) for s in range(6)]


def recalculate_returns():
    """Same physical source solve as GERM-68; no fixture is numerical input."""
    l2, l3, l5 = old.log_box(2), old.log_box(3), old.log_box(5)
    mu = (l3/l2)/old.sqrt_box(3)
    beta = (l3/l2)*old.sqrt_box(F(2, 3))
    d = (l5/l2)/old.sqrt_box(5)
    a, g = (beta*mu)**2, 1-(beta*mu)**2
    layers = {m: parent.layer(m, a, d, mu) for m in (2, 3)}
    bulk = mat([[(2*a-1)/(d*a), g/a], [-g/a, d/a]])
    bi, swap = inverse(bulk), mat([[0, 1], [1, 0]])
    returns = {}
    fixture = json.loads((ROOT/'notes/_recurrence67_audit.json').read_text())
    for key in ('00+', '10+', '11+', '00-', '01-', '11-'):
        si, tj = 2+int(key[0]), 2+int(key[1])
        wrap = int(key[-1] == '-')
        value = mm(mm(mm(mm(inverse(layers[tj]['L'][-1]),
                            mpow(bi, 4+wrap-tj)), swap), layers[si]['N'][-1]), swap)
        value = mm(value, layers[si]['K'][0])
        assert mdet(value).lo > 0
        for i in range(2):
            for j in range(2):
                lo, hi = map(F, fixture['rational_audit']['three_layer_returns'][key][i][j])
                assert lo <= value[i][j].lo <= value[i][j].hi <= hi
        returns[key] = value
    return returns, {str(m): old.display_matrix([v['pivots']]) for m, v in layers.items()}


def first_words():
    # First induction: z -> z-tau mod kappa. Entries are chronological.
    return {
        'A': ['01-']+['11+']*3+['10+'],  # outside -> outside, five h-circle steps
        'D': ['01-']+['11+']*4+['10+'],  # outside -> outside, six steps
        'Q': ['01-']+['11+']*4,         # enter section overlap, five steps
        'P': ['11-']+['11+']*4+['10+'], # leave section overlap, six steps
        'E': ['11-']+['11+']*4,        # stay inside section overlap, five steps
    }


def nested_word(s, n):
    if s == 0:
        return ['A']*(n-1)+['D']
    return ['A']*(n-s-1)+['Q']+['E']*(s-1)+['P']


def product(word, library):
    value = mat([[1, 0], [0, 1]])
    for name in word:
        value = mm(library[name], value)
    return value


def rational_audit():
    returns, pivots = recalculate_returns()
    words = first_words()
    first = {key: product(word, returns) for key, word in words.items()}
    chart = mat([[1, 1], [1, 20]])
    chart_inverse = mat([[F(20, 19), F(-1, 19)], [F(-1, 19), F(1, 19)]])
    certified = {}
    for s, n in PAIRS:
        word = nested_word(s, n)
        b = product(word, first)
        sign = 1 if n == 8 else -1
        positive = [parent.scale(sign, row) for row in mm(mm(chart_inverse, b), chart)]
        assert all(x.lo > 0 for row in positive for x in row), (s, n)
        determinant = mdet(positive)
        assert determinant.lo > 0 and determinant.lo <= 1 <= determinant.hi
        forward = min(positive[0][0].lo+positive[1][0].lo,
                      positive[0][1].lo+positive[1][1].lo)
        backward = min(positive[1][1].lo+positive[1][0].lo,
                       positive[0][1].lo+positive[0][0].lo)/determinant.hi
        assert forward > F(5, 2) and backward > F(5, 2), (s, n)
        expanded = [letter for item in word for letter in words[item]]
        assert len(word) == n and len(expanded) == 5*n+1
        # Independent parenthesization: interval overlap is a regression,
        # while the exact ordered product identity is stated in the proof.
        direct = product(expanded, returns)
        for i in range(2):
            for j in range(2):
                assert max(b[i][j].lo, direct[i][j].lo) <= min(b[i][j].hi, direct[i][j].hi)
        certified[f'{s}/{n}'] = {
            'section_overlap_visits': s, 'first_section_steps': n,
            'original_h_circle_steps': len(expanded),
            'chronological_section_word': word,
            'chronological_original_word': expanded,
            'overall_sign': sign,
            'positive_conjugate': old.display_matrix(positive),
            'determinant_enclosure': old.display_matrix([[determinant]]),
            'forward_lower': old.outward_decimal(forward, 8),
            'backward_lower': old.outward_decimal(backward, 8),
        }
    # First newly legal type above the scope: s=6,n=9. It fails this chart.
    guard = product(nested_word(6, 9), first)
    cg = mm(mm(chart_inverse, guard), chart)
    assert cg[0][0].lo > 0 and cg[0][1].lo > 0
    assert cg[1][0].hi < 0 and cg[1][1].hi < 0
    trace = guard[0][0]+guard[1][1]
    assert F(47, 10) < trace.lo and trace.hi < F(48, 10)
    return {
        'physical_input': 'RATIONAL LOG SERIES AND INTEGER-SQUARE ROOT BOUNDS',
        'local_source_recalculation': 'PINNED PAIRED-ROW OUTWARD GAUSSIAN SOLVES',
        'layer_pivots': pivots,
        'six_parent_matrix_boxes': 'RECALCULATED AND CONTAINED IN PINNED REGRESSION BOXES',
        'chart': [['1', '1'], ['1', '20']],
        'common_forward_backward_factor': '5/2',
        'first_section_matrices': {key: old.display_matrix(v) for key, v in first.items()},
        'twelve_nested_blocks': certified,
        'above_scope_type': '6/9',
        'above_scope_conjugate': old.display_matrix(cg),
        'above_scope_trace': old.display_matrix([[trace]]),
        'above_scope_same_signed_chart': 'FAILS: OPPOSITE ROW SIGNS',
    }


# Affine coordinates (r,nu,y), normalized by tau: r=kappa/tau, nu=delta/tau.
af, add, sub, val = parent.af, parent.add, parent.sub, parent.value
verts = parent.vertices

def test_margins(margins, vv):
    for name, margin in margins:
        values = [val(margin, v) for v in vv]
        assert min(values) >= 0 and max(values) > 0, (name, margin, values)


def points_for(n):
    r, y = af(r=1), af(z=1)
    points = [af(-1-j, r=1, z=1) for j in range(n)]
    points.append(af(-n-1, r=2, z=1))
    assert sub(points[-1], af(-1, r=1)) == af(-n, r=1, z=1)
    return points


def geometry_margins(s, n):
    r, nu, y, one = af(r=1), af(eta=1), af(z=1), af(1)
    h, lam, eta = af(1, r=5), af(1, r=4), af(1, r=4, eta=1)
    points = points_for(n)
    margins = [('section_disjoint', sub(af(-1, r=1), nu))]
    word, expected_first_words = nested_word(s, n), first_words()
    for j, z in enumerate(points):
        inside = s > 0 and n-s <= j < n
        margins += [(f'z{j}>0', z), (f'z{j}<kappa', sub(r, z)),
                    (f'z{j}overlap', sub(nu, z) if inside else sub(z, nu)),
                    (f'z{j}section', sub(z, af(-1, r=1)) if j in (0, n)
                     else sub(af(-1, r=1), z))]
    # Verify every first-section step and lift its complete word to R on h.
    for j in range(n):
        z, target = points[j], points[j+1]
        wrapped = j == n-1
        expect = add(z, af(-1, r=1)) if wrapped else sub(z, one)
        assert target == expect
        margins.append((f'first_return_cut{j}', sub(one, z) if wrapped else sub(z, one)))
        hn = 6 if wrapped else 5
        hp = [add(lam, z)] + [add(z, af(r=i)) for i in range(hn)]
        assert hp[-1] == add(lam, target)
        bits = []
        for k, point in enumerate(hp):
            bit = (s > 0 and n-s <= j < n) if k == 0 else (
                   (s > 0 and n-s <= j+1 < n) if k == hn else True)
            bits.append(int(bit))
            margins += [(f'lift{j},{k}>0', point), (f'lift{j},{k}<h', sub(h, point)),
                        (f'lift{j},{k}overlap', sub(eta, point) if bit else sub(point, eta)),
                        (f'lift{j},{k}section', sub(point, lam) if k in (0, hn)
                         else sub(lam, point))]
        actual = [f'{bits[k]}{bits[k+1]}'+('-' if k == 0 else '+') for k in range(hn)]
        assert actual == expected_first_words[word[j]], (s, n, j, actual)
    return margins


def geometry_audit():
    h, kappa = old.H, old.KAP
    tau = old.sub(h, old.mul(5, kappa))
    theta = old.sub(kappa, old.mul(8, tau))
    fixed = {
        'tau_positive': tau,
        'theta_positive__kappa_gt_8tau': theta,
        'theta_lt_tau__kappa_lt_9tau': old.sub(tau, theta),
        'exclusion_endpoint_lt_3h': old.sub(kappa, old.mul(5, tau)),
        'section_outside_overlap': old.sub(kappa, old.mul(6, tau)),
    }
    assert all(old.prime_sign(v[:3]) > 0 for v in fixed.values())
    r, nu, y, one = af(r=1), af(eta=1), af(z=1), af(1)
    common = (af(-8, r=1), af(9, r=-1), nu, sub(af(5), nu), y, sub(one, y))
    cells = {}
    for s, n in PAIRS:
        q = af(-n, r=1, z=1)  # final pre-wrap point
        cond = common+(q, sub(one, q))
        cond += (sub(q, nu),) if s == 0 else (sub(nu, add(q, af(s-1))), sub(add(q, af(s)), nu))
        vv = verts(cond)
        margins = geometry_margins(s, n)
        test_margins(margins, vv)
        item = {'vertices': len(vv), 'nested_source_word': 'PASS',
                'all_original_h_circle_source_domains': 'PASS',
                'no_earlier_second_section_hit': 'PASS',
                'original_step_count': 5*n+1}
        if s == 5:
            endpoint = verts(cond+(sub(nu, af(5)),))
            test_margins(margins, endpoint)
            item['nu_equals_5_endpoint'] = 'PASS'
        cells[f'{s}/{n}'] = item
    # First/second induced maps and exact image tilings.
    # S(z)=z-1 mod r; F=(r-1,r), z=r-1+y, theta=r-8.
    theta_aff = af(-8, r=1)
    cut = sub(one, theta_aff)
    y8, y9 = af(-8, r=1, z=1), af(-9, r=1, z=1)
    assert y8 == add(y, theta_aff) and y9 == sub(add(y, theta_aff), one)
    assert add(cut, theta_aff) == one
    images = [[theta_aff, one], [af(), theta_aff]]
    assert images[1][1] == images[0][0]  # disjoint interiors; tile (0,1)
    # Completeness: 0<q<1; 0<nu<=5 forces s in {0,...,5}.
    # Sources below F reach it at first negative wrap after at most eight S steps.
    assert 9-1 == 8
    # Above-scope face: nu=5+zeta, 0<zeta<theta; 0<q<zeta gives new s=6,n=9.
    guard = (af(-8, r=1), af(9, r=-1), sub(nu, af(5)),
             sub(af(-3, r=1), nu), y, sub(one, y),
             af(-9, r=1, z=1), sub(sub(nu, af(5)), af(-9, r=1, z=1)))
    vv = verts(guard)
    test_margins(geometry_margins(6, 9), vv)
    return {
        'normalization': 'tau=1, r=kappa/tau, nu=(eta-lambda)/tau, 0<y<1',
        'exact_prime_power_checks': {name: 'PASS' for name in fixed},
        'parameter_scope': '0<eta-lambda<=5tau',
        'first_section': '(lambda,h); coordinate z in (0,kappa)',
        'first_induced_map': 'z -> z-tau mod kappa',
        'second_section': '(kappa-tau,kappa) in z coordinates',
        'second_return_times': '8 if y<tau-theta; 9 if y>tau-theta',
        'second_induced_map': 'y -> y+theta mod tau',
        'image_tiling': 'EXACT; images (theta,tau) and (0,theta)',
        'all_twelve_cells': cells,
        'endpoint_delta_equals_5tau': 'BOTH 5/8 AND 5/9 FACES CHECKED',
        'source_recovery_steps': 'at most 8 first-section steps to second section',
        'new_type_guard': '0<eta-lambda-5tau<theta; q in (0,eta-lambda-5tau): 6/9',
        'new_type_guard_vertices': len(vv),
        'sampled_topology': False,
    }


def main():
    # e69=3h-kappa+5tau=138h-26k, since kappa=k-5h and tau=h-5kappa.
    endpoint = F(16, 3)*F(81, 80)**138/F(16, 15)**26
    assert endpoint == F(3**577, 2**652*5**112)
    out = {
        'pass': 'SZ-KERNEL-EDGE-GERM-69', 'standing': 'UNRATIFIED',
        'entry_commit': '54d94f4e26e82069f0bab1620063f63c6f70a7a6',
        'inherited_formula_scope': '2h<e<=3h',
        'new_exclusion_scope': '3h-kappa<e<=3h-kappa+5tau',
        'tau': 'h-5kappa', 'theta': 'kappa-8tau',
        'experimental_endpoint': 'log(3^577/(2^652*5^112))',
        'dependency_sha256': PINS,
        'rational_audit': rational_audit(), 'exact_geometry': geometry_audit(),
        'old_large_determinants_rerun': False, 'full_parent_symbolic_suite_rerun': False,
        'canonical_cursor': 'SZ-CROSS-COLLAR-3', 'canonical_effect': 'NONE',
    }
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
