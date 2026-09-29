#!/usr/bin/env python3
"""GERM-90: post-t=chi7 seventh-wrap transfer and direct seventh exclusion.

Three seventh matrices have a signed common cone for chi7<t<=eta7.
The sixth endpoint t=eta7 is checked against the fifth source contracts.
No eighth or deeper induction is used. Run with assertions enabled.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of the certificate; run without -O.'
ROOT = Path(__file__).resolve().parents[1]
PIN_PATH = 'tools/sz_post_2psi7_eighth_map_audit.py'
PIN_SHA = '68404e3d6426f4346793f966eebc42000e8ebf7a5f821fbc133ef61693d451f6'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest() == PIN_SHA
import sz_post_2psi7_eighth_map_audit as parent
g81, g77, g75, old = parent.g81, parent.g77, parent.g75, parent.old
product, det = parent.product, parent.det
SEVENTH = {'U': ['E20','E20','E19'],
           'V0': ['E20','E20','E19','E20','A19'],
           'V1': ['E20','E20','E19','E20','E19']}
SIGNS = {'U': -1, 'V0': -1, 'V1': 1}
CHART = [[1,-1],[F(-21,10),F(7,3)]]
FACTOR = F(9,5)
NEXT_PAIR = (16,20)


def arithmetic():
    add, sub, mul = old.add, old.sub, old.mul
    h, k = (-4,4,-1), (4,-1,-1)
    kap = sub(k,mul(5,h)); tau = sub(h,mul(5,kap)); th = sub(kap,mul(8,tau))
    alpha = sub(tau,mul(3,th)); beta = sub(th,alpha); gamma = sub(alpha,beta)
    xi = sub(mul(5,gamma),beta); omega = sub(gamma,mul(19,xi))
    eta = sub(xi,omega); chi = sub(mul(2,omega),xi); psi = sub(eta,chi)
    L80 = (193384,-169969,32737); L89 = add(L80,chi); L90 = add(L80,eta)
    top = add((4,-1,0),mul(3,h))
    assert L89 == (1777196,-1562045,300866)
    assert L90 == (-619016,544082,-104797)
    assert sub(L90,L89) == psi == (-2396212,2106127,-405663)
    assert L90 == add((4,-1,0),sub(mul(129776,h),mul(24979,k)))
    assert add(chi,psi) == eta
    assert add(mul(3,sub(chi,psi)),mul(5,psi)) == xi
    logs = [old.log_box(n) for n in (2,3,5)]
    def enc(v): return sum((n*l for n,l in zip(v,logs)),old.box(0))
    checks = {'psi_positive': psi, 'chi_gt_psi': sub(chi,psi),
              'next_guard_r_lt_omega': sub(omega,psi),
              'sixth_section_exterior_at_endpoint': sub(gamma,mul(16,xi)),
              'sixth_section_exterior_on_next_guard': sub(sub(gamma,mul(16,xi)),psi),
              'beta_box_lower': sub(mul(157,beta),mul(777,gamma)),
              'beta_box_upper': sub(mul(1069,gamma),mul(216,beta)),
              'endpoint_below_three_layers': sub(top,L90)}
    bounds = {key: enc(v) for key,v in checks.items()}
    assert all(v.lo > 0 for v in bounds.values())
    return {'rational_log_order_checks': {k:g77.show_box(v,38) for k,v in bounds.items()},
            'endpoint_prime_log_vector': L90, 'endpoint_h_k_vector': [129776,-24979],
            'endpoint_decimal': g77.show_box(enc(L90),38),
            'increment_prime_log_vector': psi, 'increment_decimal': g77.show_box(enc(psi),38),
            'remaining_sixth_formula_width': 'ZERO',
            'remaining_three_layer_width': g77.show_box(enc(sub(top,L90)),38),
            'tower_identity': '3(chi7-psi7)+5psi7=xi'}


def rational_audit():
    original, pivots = g75.parent.parent.parent.parent.recalculate_returns()
    legacy = g75.parent.parent.parent
    first = {k:product(w,original) for k,w in legacy.FIRST.items()}
    second = {k:product(w,first) for k,w in legacy.SECOND.items()}
    boxes = json.loads((ROOT/'notes/_recurrence71_audit.json').read_text())['audit']['rational_audit']['second_section_maps']
    for key,b in second.items():
        for i in range(2):
            for j in range(2):
                lo, hi = map(F,boxes[key][i][j]); assert lo <= b[i][j].lo <= b[i][j].hi <= hi
    third = {k:product(w,second) for k,w in g75.THIRD.items()}
    fourth = {k:product(w,third) for k,w in g75.FOURTH.items()}
    fifth = {k:product(w,fourth) for k,w in g75.FIFTH.items()}
    atoms = {k:product(g75.sixth_word(s,n),fifth) for k,(s,n) in g81.ATOMS.items()}
    counts6 = {}
    for key,(s,n) in g81.ATOMS.items():
        ow = g75.to_original(g75.sixth_word(s,n))
        assert legacy.determinant_exponent(ow) == 0
        assert len(ow) == 1654*n-297; counts6[key] = len(ow)
    seven = {k:product(w,atoms) for k,w in SEVENTH.items()}
    assert SEVENTH['U'] == g81.SEVENTH['U1']
    assert SEVENTH['V0'] == g81.SEVENTH['V1']
    assert SEVENTH['V1'] == parent.NEXT
    chart_det = F(CHART[0][0])*F(CHART[1][1])-F(CHART[0][1])*F(CHART[1][0])
    assert chart_det == F(7,30)
    chart_box = det(g75.mat(CHART))
    assert 0 < chart_box.lo <= chart_det <= chart_box.hi
    counts7 = {k:sum(counts6[x] for x in w) for k,w in SEVENTH.items()}
    assert counts7 == {'U':96695,'V0':160607,'V1':160607}
    cert = {}
    for key,b in seven.items():
        dd = det(b); tr = b[0][0]+b[1][1]; disc = tr*tr-4*dd
        assert dd.lo > 0 and dd.lo <= 1 <= dd.hi and disc.lo > 0
        item = g77.cone_test(b,CHART,SIGNS[key],FACTOR)
        item.update({'sixth_word':SEVENTH[key], 'original_step_count':counts7[key],
                     'trace':old.display_matrix([[tr]]), 'discriminant':old.display_matrix([[disc]])})
        cert[key] = item
    nw = g75.sixth_word(*NEXT_PAIR)
    assert nw == ['00+']*3+['01+']+['11+']*15+['10-']
    ow = g75.to_original(nw); assert legacy.determinant_exponent(ow) == 0 and len(ow) == 32783
    b = product(nw,fifth); dd = det(b); tr = b[0][0]+b[1][1]; disc = tr*tr-4*dd
    assert dd.lo > 0 and dd.lo <= 1 <= dd.hi
    assert F(-4,5) < tr.lo < tr.hi < F(-79,100) and disc.hi < 0
    return {'physical_recalculation':'FRESH PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
            'precision':{'grid':'10^120','log_series_terms':400}, 'layer_pivots':pivots,
            'GERM71_box_regression':'CONTAINED; not rounded proof inputs',
            'chart':[['1','-1'],['-21/10','7/3']], 'chart_determinant':'7/30',
            'common_forward_backward_factor':'9/5', 'three_seventh_cone_certificates':cert,
            'eighth_or_deeper_induction_used':False, 'new_retained_coordinates':0,
            'next_sixth_atom':'B16,20', 'next_fifth_word':nw,
            'next_trace':old.display_matrix([[tr]]), 'next_determinant':old.display_matrix([[dd]]),
            'next_discriminant':old.display_matrix([[disc]]),
            'next_status':'ELLIPTIC NEW SIXTH ATOM; NO EXCLUSION ABOVE t=eta7'}


# Exact affine coordinates inherited from GERM-75, with gamma normalized to 1.
af, add, sub, vertices = parent.af, parent.add, parent.sub, parent.vertices
scale, audit = parent.scale, parent.audit
seed, t, chi, psi = parent.seed, parent.t, parent.chi, parent.psi
eta, xi, omega, RANGE = g81.eta, g81.xi, g81.omega, parent.RANGE
r = sub(t,chi); zero = af()


def seventh_req(key,z):
    wrap = key != 'U'; q = add(z,sub(chi,psi)) if wrap else sub(z,psi)
    m = [('z>0',z),('z<chi',sub(chi,z)),('target>0',q),('target<chi',sub(chi,q)),
         ('lower_global_scope',r),('upper_global_scope',sub(psi,r)),
         ('seventh_cut',sub(psi,z) if wrap else sub(z,psi))]
    if key == 'V0': m.append(('last_sixth_source_exterior',sub(z,r)))
    if key == 'V1': m.append(('last_sixth_source_interior',sub(r,z)))
    return q,m


def seventh_lift(key,z):
    q,m = seventh_req(key,z); w = SEVENTH[key]
    pp = g77.g76.seventh_positions(len(w),z)
    assert pp[-1] == add(scale(2,eta),q)
    for j,k in enumerate(w):
        out,lower = g81.atom_req(k,pp[j]); assert out == pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_seventh_hit{j}',sub(scale(2,eta),out) if j<len(w)-1 else sub(out,scale(2,eta))))
    return q,m


def geometry_audit():
    atoms = {}
    for key in g81.ATOMS:
        _,rr = g81.atom_req(key,seed); _,m = g81.atom_lift(key,seed)
        cond = RANGE+tuple(v for _,v in rr)
        item = audit(m,vertices(cond))
        if key in ('E19','E20'):
            item['t_equals_eta7_endpoint'] = audit(m,vertices(cond+(sub(t,eta),sub(eta,t))))
        atoms[key] = item
    cells = {}
    for key in SEVENTH:
        _,rr = seventh_req(key,seed); _,m = seventh_lift(key,seed)
        cond = RANGE+tuple(v for _,v in rr)
        item = audit(m,vertices(cond))
        if key in ('U','V0'):
            item['r_equals_zero_entry'] = audit(m,vertices(cond+(sub(zero,r),)))
        if key in ('U','V1'):
            item['r_equals_psi7_endpoint'] = audit(m,vertices(cond+(sub(r,psi),sub(psi,r))))
        cells[key] = item
    assert add(chi,psi) == eta
    assert add(scale(3,sub(chi,psi)),scale(5,psi)) == xi
    assert g75.zeta == add(t,add(scale(14,xi),omega))
    assert sub(add(eta,add(scale(14,xi),omega)),scale(15,xi)) == zero
    # Next source strip: t=eta+d, eta<y<eta+d, 0<d<psi.
    excess = sub(t,eta); q,m = g75.sixth_lift(*NEXT_PAIR,seed)
    assert q == sub(seed,eta)
    m += [('sixteenth_visit',sub(excess,q)),('not_seventeenth',sub(add(q,xi),excess))]
    cond = RANGE+(excess,sub(psi,excess),sub(seed,eta),sub(add(eta,excess),seed))
    guard = audit(m,vertices(cond))
    return {'parameter':'r=t-chi7=e-e89', 'new_exclusion_scope':'0<r<=psi7; chi7<t<=eta7',
            'rechecked_sixth_contracts':atoms, 'three_seventh_contracts':cells,
            'section':'2eta7<y<xi; coordinate 0<z<chi7',
            'seventh_map':'z -> z-psi7 mod chi7',
            'images':'(chi7-psi7,chi7) and (0,chi7-psi7)',
            'endpoint_sixth_atoms':['E19','E20'], 'endpoint_seventh_maps':['U','V1'],
            'completed_window':'GERM-81 sixth source window through t=eta7, endpoint proved from fifth contracts',
            'physical_field':'W(t0+z); t0=h-beta+gamma-xi+2eta7',
            'next_domain':'t=eta7+d; 0<d<psi7; eta7<y<eta7+d',
            'next_atom':'B16,20', 'next_guard':guard, 'sampled_topology':False}


def main():
    out = {'pass':'SZ-KERNEL-EDGE-GERM-90', 'standing':'UNRATIFIED',
           'entry_commit':'adf21cb4e4af55e00ddf02775b133a7db8aaa8c7',
           'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
           'new_exclusion_scope':'chi7<t<=eta7, t=e-e80; L89<L<=L80+eta7',
           'matrix_namespace':'Sixth atoms are GERM-81-local; U/V are GERM-90-local seventh maps',
           'seventh_word_dictionary':SEVENTH,
           'arithmetic':arithmetic(), 'rational_audit':rational_audit(), 'exact_geometry':geometry_audit(),
           'full_lower_symbolic_suites_rerun':False, 'old_large_determinants_rerun':False,
           'canonical_cursor':'SZ-CROSS-COLLAR-3', 'canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))


if __name__ == '__main__': main()
