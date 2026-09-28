#!/usr/bin/env python3
"""GERM-70: sixth-visit control and its forced-neighbor continuation.

New exclusion: 3h-kappa+5tau < e <= 3h-tau. Inherited formulas: e<=3h.
Three second-section words plus sixteen third-section words are certified.
All proof inequalities use outward rational arithmetic and affine polytopes.
Requires the pinned GERM-69/68/65 helpers and their GERM-67 fixture; SymPy
is imported by the oldest helper. Run with assertions enabled, without -O.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Run without -O; assertions are part of the certificate.'
ROOT = Path(__file__).resolve().parents[1]
PINS = {
    'tools/sz_overlapping_section_audit.py':
        '0283a3412d0ef9d029e690693b472ad656602ca817e3d730d7c48234361602e4',
    'tools/sz_multivisit_section_audit.py':
        '16517b40a62f46ec32e439a42fe70e6a52cf5d665138f0c93be0ed25a6c31bb7',
    'tools/sz_mixed_return_cone_audit.py':
        'f43eaf0e86e823a2f7ebeb6580b8ea12fcf4587ad405f708c3b66d6939b2a6c0',
    'notes/_recurrence67_audit.json':
        'db2dcd27d30ca3199c444e449d7a2b93b674a7fe2b2d4cc764b38a9a863e0b09',
}
for path, sha in PINS.items():
    assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == sha, path

import sz_overlapping_section_audit as parent
old = parent.old
mat, mm, product = old.mat, old.mm, parent.product
inverse, mdet = parent.inverse, parent.mdet
af, add, sub, val, vertices = parent.af, parent.add, parent.sub, parent.val, parent.verts


def scale(c, a):
    return tuple(c*x for x in a)


def substitute_y(a, y):
    """Substitute an affine y for the last variable, keeping r and nu."""
    return add(af(a[0], r=a[1], eta=a[2]), scale(a[3], y))


LOW = [(5, 8), (5, 9), (6, 9)]
# Keys label the final overlap count and the number of initial higher-count
# nonwrap steps. Items are chronological (s,N) second-section word labels.
HIGH = {}
for ell in (3, 4):
    for b in (6, 7):
        for m in range(ell):
            HIGH[f'{b}:{m}/{ell}'] = [(b, 8)]*m + [(b-1, 8)]*(ell-m-1) + [(b, 9)]
    HIGH[f'8:end/{ell}'] = [(7, 8)]*(ell-1) + [(8, 9)]
assert len(HIGH) == 16


def check_positive(b, chart, sign, factor):
    conjugate = mm(mm(inverse(chart), b), chart)
    pos = [[sign*x for x in row] for row in conjugate]
    assert all(x.lo > 0 for row in pos for x in row), old.display_matrix(pos)
    det = mdet(pos)
    assert det.lo > 0 and det.lo <= 1 <= det.hi
    fw = min(pos[0][0].lo+pos[1][0].lo, pos[0][1].lo+pos[1][1].lo)
    bw = min(pos[1][1].lo+pos[1][0].lo, pos[0][1].lo+pos[0][0].lo)/det.hi
    assert fw > factor and bw > factor, (fw, bw, factor)
    return {
        'overall_sign': sign,
        'positive_conjugate': old.display_matrix(pos),
        'determinant_enclosure': old.display_matrix([[det]]),
        'forward_lower': old.outward_decimal(fw, 8),
        'backward_lower': old.outward_decimal(bw, 8),
    }


def rational_audit():
    returns, pivots = parent.recalculate_returns()
    fw = parent.first_words()
    first = {k: product(w, returns) for k, w in fw.items()}
    used = set(LOW)
    for w in HIGH.values(): used.update(w)
    second = {key: product(parent.nested_word(*key), first) for key in sorted(used)}
    clo = mat([[1, F(1, 2)], [-2, 10]])
    chi = mat([[1, 1], [F(-13, 8), 2]])
    low = {}
    for s, n in LOW:
        sign = -1 if (s, n) == (5, 9) else 1
        low[f'{s}/{n}'] = check_positive(second[s, n], clo, sign, F(3, 2))
    high = {}
    for key, w in HIGH.items():
        b = product(w, second)
        ell = len(w)
        if key.startswith('6:'):
            m = sum(s == 6 for s, _ in w[:-1]); sign = (-1)**m
        else:
            sign = (-1)**(ell+1)
        item = check_positive(b, chi, sign, F(7, 5))
        section_word = [x for k in w for x in parent.nested_word(*k)]
        original_word = [x for k in section_word for x in fw[k]]
        assert len(section_word) == 8*ell+1
        assert len(original_word) == 41*ell+5
        direct = product(original_word, returns)
        # Enclosure overlap is a regression, not a proof of an identity.
        # The identity itself follows from substituting chronological words.
        for i in range(2):
            for j in range(2):
                assert max(b[i][j].lo, direct[i][j].lo) <= min(b[i][j].hi, direct[i][j].hi)
        item.update({'second_section_words': [f'{s}/{n}' for s, n in w],
                     'first_section_step_count': len(section_word),
                     'original_rotation_step_count': len(original_word),
                     'original_word_sha256': hashlib.sha256(json.dumps(original_word, separators=(',', ':')).encode()).hexdigest()})
        high[key] = item
    # The individual six-visit nonwrap matrix is elliptic; it is not
    # relabeled as expanding. The neighboring products above are used.
    b = second[6, 8]
    trace = b[0][0]+b[1][1]
    assert F(-19, 10) < trace.lo < trace.hi < F(-17, 10)
    disc = trace*trace-4
    assert disc.hi < 0
    return {
        'local_source_recalculation': 'PINNED PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
        'six_original_return_boxes': 'RECALCULATED; CONTAINED IN PINNED GERM-67 BOXES',
        'layer_pivots': pivots,
        'low_chart': [['1', '1/2'], ['-2', '10']],
        'low_common_factor': '3/2', 'low_three_words': low,
        'high_chart': [['1', '1'], ['-13/8', '2']],
        'high_common_factor': '7/5', 'high_sixteen_words': high,
        'six_visit_nonwrap_trace': old.display_matrix([[trace]]),
        'six_visit_nonwrap_discriminant': old.display_matrix([[disc]]),
    }


def audit_margins(margins, vv):
    zeros = []
    for name, a in margins:
        values = [val(a, v) for v in vv]
        assert min(values) >= 0, (name, a, min(values))
        if max(values) == 0:
            # At nu=kappa-tau the OPEN old section and overlap only touch.
            # The actual source point is strictly inside the section.
            assert name.endswith('section_disjoint'), (name, a)
            zeros.append(name)
    return {'checked_margins': len(margins), 'vertices': len(vv),
            'permitted_weak_section_separation': zeros}


def interval_margins(s, n, y):
    return [(name, substitute_y(a, y)) for name, a in parent.geometry_margins(s, n)]


def geometry_audit():
    h, kap = old.H, old.KAP
    tau = old.sub(h, old.mul(5, kap))
    theta = old.sub(kap, old.mul(8, tau))
    fixed = {
        '4theta_gt_tau': old.sub(old.mul(4, theta), tau),
        '3theta_lt_tau': old.sub(tau, old.mul(3, theta)),
        'new_endpoint_lt_3h': tau,
        'new_endpoint_gt_old': old.sub(kap, old.mul(6, tau)),
    }
    assert all(old.prime_sign(x[:3]) > 0 for x in fixed.values())
    # Normalize tau=1; r=kappa/tau, nu remains the section-overlap width.
    r, nu, y, one = af(r=1), af(eta=1), af(z=1), af(1)
    theta = af(-8, r=1)
    common_r = (af(F(-33, 4), r=1), af(F(25, 3), r=-1))
    low_base = common_r+(sub(nu, af(5)), sub(af(-3, r=1), nu), y, sub(one, y))
    low = {}
    for s, n in LOW:
        q = af(-n, r=1, z=1)
        cond = low_base+(q, sub(one, q), sub(nu, add(q, af(s-1))), sub(add(q, af(s)), nu))
        margins = parent.geometry_margins(s, n)
        result = audit_margins(margins, vertices(cond))
        if (s, n) in ((5, 8), (6, 9)):
            face = cond+(sub(nu, af(-3, r=1)),)
            result['upper_endpoint_face'] = audit_margins(margins, vertices(face))
        low[f'{s}/{n}'] = result
    # High interval: 5+theta <= nu <= 7+theta = r-1.
    high_base = common_r+(sub(nu, af(-3, r=1)), sub(af(-1, r=1), nu),
                          y, sub(theta, y))
    alpha = sub(one, scale(3, theta))
    high = {}
    for key, word in HIGH.items():
        ell = len(word)
        points = [add(y, scale(j, theta)) for j in range(ell)]
        points.append(sub(add(y, scale(ell, theta)), one))
        cond = high_base+(sub(y, alpha) if ell == 3 else sub(alpha, y),)
        margins = []
        for j, (s, n) in enumerate(word):
            q = points[j+1]
            cond += (q, sub(one, q), sub(nu, add(q, af(s-1))), sub(add(q, af(s)), nu))
            assert n == (9 if j == ell-1 else 8)
            expected_q = substitute_y(af(-n, r=1, z=1), points[j])
            assert q == expected_q
            margins.extend((f'step{j}:{name}', a) for name, a in interval_margins(s, n, points[j]))
            margins.append((f'third_no_earlier_hit{j}', sub(q, theta) if j < ell-1 else sub(theta, q)))
        vv = vertices(cond)
        result = audit_margins(margins, vv)
        if key.startswith('8:end'):
            face = cond+(sub(nu, af(-1, r=1)),)
            result['nu_equals_kappa_minus_tau_face'] = audit_margins(margins, vertices(face))
        if key.startswith('6:0/'):
            face = cond+(sub(af(-3, r=1), nu),)
            result['nu_equals_5tau_plus_theta_face'] = audit_margins(margins, vertices(face))
        high[key] = result
    # Exact first-return translation tiling on G=(0,theta).
    # y<alpha: y+4theta-1; y>alpha: y+3theta-1.
    image_low = sub(scale(4, theta), one)
    assert image_low == sub(theta, alpha)
    assert sub(add(alpha, scale(4, theta)), one) == theta
    assert sub(add(alpha, scale(3, theta)), one) == af()
    # Completeness of high library by four parameter bands. Within a band,
    # increasing nonwrap targets make the higher visit count an initial run.
    assert len(HIGH) == sum(2*ell+1 for ell in (3, 4))
    # Above the new endpoint a source-overlap wrap in the FIRST section
    # can stay inside. Check a concrete affine strip, not a numerical orbit.
    # nu=r-1+zeta, 0<zeta<theta; zeta>z>0 in old z coordinate.
    z = y
    guard = common_r+(sub(nu, af(-1, r=1)), sub(af(-9, r=2), nu),
                      z, sub(sub(nu, af(-1, r=1)), z))
    eta, hh, lam = af(1, r=4, eta=1), af(1, r=5), af(1, r=4)
    physical = [add(lam, z)]+[add(z, af(r=j)) for j in range(6)]
    guard_margins = []
    for j, point in enumerate(physical):
        guard_margins += [(f'guard{j}>0', point), (f'guard{j}<h', sub(hh, point)),
                          (f'guard{j}inside_overlap', sub(eta, point))]
        guard_margins += [(f'guard{j}section', sub(point, lam) if j in (0,6) else sub(lam, point))]
    actual_word = ['11-']+['11+']*5
    assert len(actual_word) == 6
    guard_result = audit_margins(guard_margins, vertices(guard))
    return {
        'exact_prime_power_checks': {key:'PASS' for key in fixed},
        'normalization': 'tau=1; 33/4<r=kappa/tau<25/3; theta=r-8',
        'low_scope': '5tau<nu<=5tau+theta', 'low_cells': low,
        'high_scope': '5tau+theta<=nu<=kappa-tau', 'high_cells': high,
        'high_completeness_bands': ['[5tau+theta,6tau]', '[6tau,6tau+theta]',
                                    '[6tau+theta,7tau]', '[7tau,kappa-tau]'],
        'third_section': '0<y<theta inside second-section coordinate; physically (h-tau,h-tau+theta)',
        'third_return_times': '4 when y<tau-3theta; 3 when y>tau-3theta',
        'third_induced_map': 'y -> y-(tau-3theta) mod theta',
        'third_image_tiling': '(theta-alpha,theta) and (0,theta-alpha), alpha=tau-3theta',
        'old_section_and_overlap_open_endpoint': 'MAY TOUCH; ACTUAL SOURCE MARGINS STRICT',
        'above_scope_new_word': actual_word,
        'above_scope_domain': 'nu=kappa-tau+zeta; 0<z<zeta<theta',
        'above_scope_guard': guard_result,
        'sampled_topology': False,
    }


def main():
    # 3h-tau=2h+5kappa=5k-23h.
    endpoint = F(16,3)*F(16,15)**5/F(81,80)**23
    assert endpoint == F(2**116*5**18,3**98)
    old_endpoint = F(3**577, 2**652*5**112)
    third_layer_endpoint = F(16,3)*F(81,80)**3
    assert old_endpoint < endpoint < third_layer_endpoint
    # Independent evaluation via kappa and tau as rational logarithmic arguments.
    kap_arg = F(16,15)/F(81,80)**5
    tau_arg = F(81,80)/kap_arg**5
    assert endpoint == F(16,3)*F(81,80)**3/tau_arg
    out = {
        'pass':'SZ-KERNEL-EDGE-GERM-70', 'standing':'UNRATIFIED',
        'entry_commit':'8aff3f5bca9d887e4f11542594fe98ae3c09db6f',
        'inherited_formula_scope':'2h<e<=3h',
        'new_exclusion_scope':'3h-kappa+5tau<e<=3h-tau',
        'experimental_endpoint':'log(2^116*5^18/3^98)',
        'dependency_sha256':PINS,
        'rational_audit':rational_audit(), 'exact_geometry':geometry_audit(),
        'full_parent_symbolic_suite_rerun':False,'old_large_determinants_rerun':False,
        'canonical_cursor':'SZ-CROSS-COLLAR-3', 'canonical_effect':'NONE',
    }
    print(json.dumps(out, indent=2))

if __name__ == '__main__': main()
