#!/usr/bin/env python3
"""GERM-78: eighth-return internal visits through delta=2*psi7.

Inherits the four seventh maps on 0<delta<chi7. Certifies four complete
first-return words on psi7<delta<=2psi7, in one signed rational cone chart.
All proof inequalities are outward rational or exact affine-polytope tests.
Run without -O. The direct GERM-77 helper and transitive bytes are pinned.
No full earlier symbolic suite, large determinant inventory, or Lean run.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of this certificate; do not use -O.'
ROOT = Path(__file__).resolve().parents[1]
PIN_PATH = 'tools/sz_seventh_section_self_overlap_audit.py'
PIN_SHA = '3b1f9d6316677668889d315beb171ffd79e8a3489c8c91c15b227d6344fe8431'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest() == PIN_SHA
import sz_seventh_section_self_overlap_audit as parent
old, g75 = parent.old, parent.g75
old.SCALE = 10**60
product, det = parent.product, parent.det
WORDS = {
    '2/0': ['V1','U0'],
    '2/1': ['V1','U1'],
    '3/00': ['V1','U0','U0'],
    '3/01': ['V1','U0','U1'],
}
CHART = [[1,5],[0,F(-40,3)]]
GUARD = ['V1','U1','U1']

def arithmetic():
    # Prime-log vectors: addition is exact, avoiding cancellation in floats.
    h, k = (-4,4,-1), (4,-1,-1)
    psi = (-2396212,2106127,-405663)
    assert psi == old.sub(old.mul(502358,h),old.mul(96695,k))
    L76 = (-1390428,1222107,-235392)
    L77 = old.add(L76,psi)
    L78 = old.add(L77,psi)
    assert L77 == (-3786640,3328234,-641055)
    assert L78 == (-6182852,5434361,-1046718)
    assert L78 == old.add((4,-1,0),old.sub(old.mul(1296216,h),old.mul(249498,k)))
    logs = [old.log_box(n) for n in (2,3,5)]
    def enc(v): return sum((c*l for c,l in zip(v,logs)),old.box(0))
    end3 = old.add((4,-1,0),old.mul(3,h))
    assert enc(psi).lo > 0 and enc(old.sub(end3,L78)).lo > 0
    inherited = parent.prime_data()  # Exact prime-power order/range checks.
    return {
        'inherited_prime_power_checks':inherited['prime_power_checks'],
        'endpoint_prime_log_vector':L78,'endpoint_h_k_vector':[1296216,-249498],
        'endpoint_decimal':parent.show_box(enc(L78),24),
        'increment_psi7':parent.show_box(enc(psi),30),
        'remaining_three_layer_width':parent.show_box(enc(old.sub(end3,L78)),28),
        'endpoint_order':'L77<L78<log(16/3)+3h; certified rational log bounds',
    }

def rational_audit():
    original,pivots = g75.parent.parent.parent.parent.recalculate_returns()
    legacy = g75.parent.parent.parent
    first = {k:product(w,original) for k,w in legacy.FIRST.items()}
    second = {k:product(w,first) for k,w in legacy.SECOND.items()}
    boxes = json.loads((ROOT/'notes/_recurrence71_audit.json').read_text())['audit']['rational_audit']['second_section_maps']
    for key,b in second.items():
        for i in range(2):
            for j in range(2):
                lo,hi = map(F,boxes[key][i][j])
                assert lo<=b[i][j].lo<=b[i][j].hi<=hi
    third = {k:product(w,second) for k,w in g75.THIRD.items()}
    fourth = {k:product(w,third) for k,w in g75.FOURTH.items()}
    fifth = {k:product(w,fourth) for k,w in g75.FIFTH.items()}
    atoms = {k:product(g75.sixth_word(s,n),fifth) for k,(s,n) in parent.ATOMS.items()}
    counts = {}
    for key,(s,n) in parent.ATOMS.items():
        ow = g75.to_original(g75.sixth_word(s,n))
        assert legacy.determinant_exponent(ow) == 0
        counts[key] = len(ow)
        assert counts[key] == 1654*n-297
    seventh = {k:product(w,atoms) for k,w in parent.SEVENTH.items()}
    seventh_counts = {k:sum(counts[x] for x in w) for k,w in parent.SEVENTH.items()}
    assert seventh_counts == {'U0':96695,'U1':96695,'V0':160607,'V1':160607}
    cert = {}
    for key,w in WORDS.items():
        b = product(w,seventh)
        item = parent.cone_test(b,CHART,-1,F(3,2))
        tr = b[0][0]+b[1][1]; dd = det(b)
        assert tr.hi < -2 and (tr*tr-4*dd).lo > 0
        item.update({'seventh_word':w,'original_step_count':sum(seventh_counts[x] for x in w),
                     'trace':old.display_matrix([[tr]])})
        cert[key] = item
    # The first newly active all-internal three-step word really is elliptic.
    b = product(GUARD,seventh)
    tr = b[0][0]+b[1][1]; dd = det(b); disc = tr*tr-4*dd
    assert F(109,100)<tr.lo<tr.hi<F(110,100) and dd.lo>0 and disc.hi<0
    return {
        'physical_recalculation':'FRESH OUTWARD RATIONAL PAIRED-SOURCE SOLVES',
        'grid':'10^60','layer_pivots':pivots,'GERM71_box_regression':'CONTAINED',
        'seventh_maps':{k:old.display_matrix(v) for k,v in seventh.items()},
        'chart':[['1','5'],['0','-40/3']], 'overall_sign_all_words':-1,
        'common_forward_backward_factor':'3/2','four_eighth_returns':cert,
        'above_scope_word':GUARD,'above_scope_trace':old.display_matrix([[tr]]),
        'above_scope_determinant':old.display_matrix([[dd]]),
        'above_scope_discriminant':old.display_matrix([[disc]]),
        'above_scope_status':'DETERMINANT ONE; GENUINELY ELLIPTIC',
    }

af,add,sub,val,vertices = parent.af,parent.add,parent.sub,parent.val,parent.vertices
scale = parent.scale
psi,chi,delta,seed = parent.psi,parent.chi,parent.delta,parent.seed
nu,sigma = parent.nu,parent.sigma

def geometry_audit():
    # Replay all four seventh-map composition contracts on their FULL scope.
    # Their sixth-atom contracts are inherited from the successful GERM-77
    # entry replay, not inferred from endpoint bits or interval overlap.
    seven = {}
    for key in parent.SEVENTH:
        _,req = parent.seventh_req(key,seed)
        _,m = parent.seventh_lift(key,seed)
        seven[key] = parent.audit(m,vertices(parent.RANGE+tuple(a for _,a in req)))
    base = parent.RANGE+(sub(delta,psi),sub(scale(2,psi),delta),seed,sub(psi,seed))
    cells = {}
    for key,word in WORDS.items():
        n = len(word)
        cond = base+(sub(sigma,seed) if n==2 else sub(seed,sigma),)
        points = [seed]+[add(seed,sub(chi,scale(j,psi))) for j in range(1,n+1)]
        for j,letter in enumerate(word):
            cond += (sub(delta,points[j]) if letter[-1]=='1' else sub(points[j],delta),)
        target,m = parent.eighth_lift(word,n,seed)
        m += [('new_lower_global_scope',sub(delta,psi)),
              ('new_upper_global_scope',sub(scale(2,psi),delta))]
        item = parent.audit(m,vertices(cond))
        if key in ('2/1','3/01'):
            face = cond+(sub(delta,scale(2,psi)),)
            item['delta_equals_2psi_endpoint'] = parent.audit(m,vertices(face))
        if key in ('2/0','3/01'):
            junction = sub(chi,psi)
            face = cond+(sub(delta,junction),sub(junction,delta))
            item['delta_equals_chi_minus_psi_junction'] = parent.audit(m,vertices(face))
        cells[key] = item
    # Completeness: on a three-step branch the first intermediate point
    # is strictly above 2psi, so its letter is ALWAYS U0 in this scope.
    q1 = add(seed,sub(chi,psi))
    assert sub(q1,scale(2,psi)) == sub(seed,sigma)
    assert add(nu,sigma) == psi
    assert sub(chi,scale(2,psi)) == nu
    assert sub(chi,scale(3,psi)) == scale(-1,sigma)
    # Two-step intermediate q1 and three-step intermediate q2 are each
    # split by delta; the binary comparisons exhaust their intervals.
    # The return images (nu,psi) and (0,nu) tile the same bottom section.
    # Parameter equality and seed-null seams are handled separately.
    extra = sub(delta,scale(2,psi))
    guard_cond = parent.RANGE+(extra,sub(nu,extra),sub(seed,sigma),sub(add(sigma,extra),seed))
    target,m = parent.eighth_lift(GUARD,3,seed)
    guard = parent.audit(m,vertices(guard_cond))
    return {
        'normalization':'gamma=1; inherited 777/157<beta/gamma<1069/216',
        'seventh_formula_scope':'0<delta<chi7','rechecked_four_seventh_cells':seven,
        'exclusion_scope':'psi7<delta<=2psi7','four_eighth_cells':cells,
        'completeness':'Initial V1 always. Two-step intermediate splits U0/U1. Three-step first intermediate >2psi7, hence U0; second splits U0/U1.',
        'section':'0<z<psi7; physical W(t0+z), t0=h-beta+gamma-xi+2eta7',
        'return_times':'2 when z<sigma8; 3 when z>sigma8',
        'return_map':'z -> z+nu8 mod psi7',
        'image_tiling':'(nu8,psi7) and (0,nu8)',
        'above_scope_domain':'delta=2psi7+a; 0<a<nu8; sigma8<z<sigma8+a',
        'above_scope_cell':guard,'sampled_topology':False,
    }

def main():
    out = {
        'pass':'SZ-KERNEL-EDGE-GERM-78','standing':'UNRATIFIED',
        'entry_commit':'8f8478a055b628f9cdcacd7fd6921cce438be4c1',
        'new_exclusion_scope':'L77<L<=L76+2psi7',
        'experimental_endpoint':'log(3^5434361/(2^6182852*5^1046718))',
        'inherited_three_layer_formula_scope':'2h<e<=3h',
        'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
        'seventh_word_dictionary':parent.SEVENTH,'eighth_word_dictionary':WORDS,
        'arithmetic':arithmetic(),'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
        'full_parent_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
        'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE',
    }
    print(json.dumps(out,indent=2))

if __name__ == '__main__': main()
