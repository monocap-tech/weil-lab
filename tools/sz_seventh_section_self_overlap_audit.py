#!/usr/bin/env python3
"""GERM-77: four retyped seventh maps and four eighth-return certificates.

New exclusion: L76 < L <= L76+psi7. Formula domain: 0<delta<chi7,
where delta=d-eta7 and d=zeta-14xi. Inherit, do not retype, the corrected
GERM-75 source contracts. Check every intermediate source at each new
composition. All certificate tests are exact or outward rational.
Run without -O. Only the explicitly listed local/domain tests are replayed;
no full earlier symbolic suite or large determinant inventory is run.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of this certificate; do not use -O.'
ROOT = Path(__file__).resolve().parents[1]
PIN_PATH = 'tools/sz_fifteen_visit_forced_neighbor_audit.py'
PIN_SHA = 'f823d55f9bc9f27b00c89d6d766c526fa44cc4c1ed11cc897ffd2758328a6bbc'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest() == PIN_SHA
import sz_fifteen_visit_forced_neighbor_audit as g76
g75 = g76.parent
old = g76.old
old.SCALE = 10**60
product, mat, mm = g75.product, g75.mat, g75.mm
inverse, det = g75.inverse, g75.det
cone_test = g75.parent.parent.cone_test

ATOMS = dict(g76.ATOMS)
SEVENTH = {
    'U0': ['A20','E20','A19'],
    'U1': ['E20','E20','A19'],
    'V0': ['A20','E20','A19','E20','A19'],
    'V1': ['E20','E20','A19','E20','A19'],
}
EIGHTH = {f'{i}/{n}': [f'V{i}']+['U0']*(n-1) for i in (0,1) for n in (2,3)}
CHART = [[1,4],[F(-9,4),-11]]
GUARD = ['V1','U0','U1']

def scale(n,a): return tuple(n*x for x in a)
def show_box(x, places=20):
    return [old.outward_decimal(x.lo,places), old.outward_decimal(x.hi,places,True)]

def prime_data():
    h = (-4,4,-1); k = (4,-1,-1)
    sub, mul = old.sub, old.mul
    kap = sub(k,mul(5,h)); tau = sub(h,mul(5,kap))
    theta = sub(kap,mul(8,tau)); alpha = sub(tau,mul(3,theta))
    beta = sub(theta,alpha); gamma = sub(alpha,beta)
    xi = sub(mul(5,gamma),beta); omega = sub(gamma,mul(19,xi))
    eta = sub(xi,omega); chi = sub(mul(2,omega),xi); psi = sub(eta,chi)
    endpoint76 = (-1390428,1222107,-235392)
    endpoint77 = old.add(endpoint76,psi)
    assert endpoint77 == (-3786640,3328234,-641055)
    assert endpoint77 == old.add((4,-1,0),sub(mul(793858,h),mul(152803,k)))
    end3 = old.add((4,-1,0),mul(3,h))
    checks = {
        'psi_positive': psi,
        'chi_gt_2psi': sub(chi,mul(2,psi)),
        'chi_lt_3psi': sub(mul(3,psi),chi),
        'beta_gamma_lower': sub(mul(157,beta),mul(777,gamma)),
        'beta_gamma_upper': sub(mul(1069,gamma),mul(216,beta)),
        'endpoint_below_3h': sub(end3,endpoint77),
    }
    def prime_sign(v):
        num=den=1
        for prime,exponent in zip((2,3,5),v):
            if exponent>=0: num*=prime**exponent
            else: den*=prime**(-exponent)
        return (num>den)-(num<den)
    assert all(prime_sign(x)>0 for x in checks.values())
    logs = [old.log_box(n) for n in (2,3,5)]
    def enclose(v): return sum((c*l for c,l in zip(v,logs)),old.box(0))
    return {
        'prime_power_checks': {key:'PASS' for key in checks},
        'endpoint_prime_log_vector': endpoint77,
        'endpoint_h_k_vector': [793858,-152803],
        'endpoint_decimal': show_box(enclose(endpoint77)),
        'remaining_three_layer_width': show_box(enclose(sub(end3,endpoint77))),
        'corrected_GERM76_residual_decimals': {
            'eta7':show_box(enclose(eta),28),
            'chi7':show_box(enclose(chi),28),
            'psi7':show_box(enclose(psi),28)},
        'increment_psi7': show_box(enclose(psi),28),
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
    atoms = {k:product(g75.sixth_word(s,n),fifth) for k,(s,n) in ATOMS.items()}
    counts = {}
    for key,(s,n) in ATOMS.items():
        ow = g75.to_original(g75.sixth_word(s,n))
        assert legacy.determinant_exponent(ow)==0
        assert len(ow)==1654*n-297
        counts[key] = len(ow)
    seventh = {k:product(w,atoms) for k,w in SEVENTH.items()}
    elliptic = {}
    for key in ('U1','V1'):
        b = seventh[key]; tr = b[0][0]+b[1][1]; dd = det(b)
        discr = tr*tr-4*dd
        assert dd.lo>0 and discr.hi<0
        elliptic[key] = {'trace':old.display_matrix([[tr]]), 'discriminant':old.display_matrix([[discr]])}
    seventh_counts = {k:sum(counts[x] for x in w) for k,w in SEVENTH.items()}
    assert seventh_counts == {'U0':96695,'U1':96695,'V0':160607,'V1':160607}
    cert = {}
    for key,w in EIGHTH.items():
        b = product(w,seventh)
        sign = 1 if key[0]=='0' else -1
        item = cone_test(b,CHART,sign,F(17))
        n = int(key[-1]); n_original = sum(seventh_counts[x] for x in w)
        assert n_original == 160607+(n-1)*96695
        item.update({'seventh_word':w,'original_step_count':n_original})
        cert[key] = item
    b = product(GUARD,seventh); tr = b[0][0]+b[1][1]; dd = det(b)
    disc = tr*tr-4*dd
    qb = mm(mm(inverse(mat(CHART)),b),mat(CHART))
    assert all(x.hi<0 for x in qb[0]) and all(x.lo>0 for x in qb[1])
    assert disc.lo>0 and F(-42)<tr.lo<tr.hi<F(-41)
    return {
        'physical_source_recalculation':'FRESH OUTWARD RATIONAL PAIRED-SOURCE SOLVES',
        'grid':'10^60','layer_pivots':pivots,
        'GERM71_box_regression':'CONTAINED',
        'seventh_maps':{k:old.display_matrix(b) for k,b in seventh.items()},
        'seventh_elliptic_maps':elliptic,
        'chart':[['1','4'],['-9/4','-11']],
        'common_forward_backward_factor':'17','four_eighth_returns':cert,
        'above_scope_word':GUARD, 'above_scope_chart':old.display_matrix(qb),
        'above_scope_trace':old.display_matrix([[tr]]),
        'above_scope_determinant':old.display_matrix([[dd]]),
        'above_scope_discriminant':old.display_matrix([[disc]]),
        'above_scope_status':'HYPERBOLIC; NEITHER OVERALL SIGN PRESERVES THE PRESENT QUADRANT',
    }

# gamma=1, affine variables (beta/gamma,zeta/gamma,seed/gamma).
af,add,sub,val,vertices = g75.af,g75.add,g75.sub,g75.val,g75.vertices
zero = af(); beta = g75.beta; zeta = g75.zeta; seed = g75.seed
xi,omega,eta,chi,psi = g76.xi,g76.omega,g76.eta7,g76.chi7,g76.psi7
delta = sub(g76.d,eta)
nu = sub(chi,scale(2,psi))
sigma = sub(scale(3,psi),chi)
RANGE = (sub(beta,af(F(777,157))),sub(af(F(1069,216)),beta))

def audit(margins,vv):
    assert vv, 'No closed cell vertices.'
    weak = []
    for name,a in margins:
        vs = [val(a,v) for v in vv]
        assert min(vs)>=0,(name,a,min(vs))
        if max(vs)==0:
            assert name.endswith('global_scope'),(name,a)
            weak.append(name)
    return {'vertices':len(vv),'checked_margins':len(margins),'weak_global':weak}

def atom_req(key,y):
    target = add(y,omega) if key=='A19' else sub(y,eta)
    rr = [('y>0',y),('y<xi',sub(xi,y)),('target>0',target),('target<xi',sub(xi,target)),
          ('delta>0',delta),('sixth_global_scope',sub(chi,delta))]
    if key=='A19': rr += [('N19_cut',sub(eta,y))]
    else:
        rr += [('N20_cut',sub(y,eta)),
               ('fifteenth_visit',sub(add(scale(2,eta),delta),y) if key=='E20'
                else sub(y,add(scale(2,eta),delta)))]
    return target,rr

def seventh_req(key,z):
    wrap = key[0]=='V'; interior = key[1]=='1'
    target = add(z,sub(chi,psi)) if wrap else sub(z,psi)
    return target,[('z>0',z),('z<chi',sub(chi,z)),('target>0',target),('target<chi',sub(chi,target)),
        ('seventh_cut',sub(psi,z) if wrap else sub(z,psi)),
        ('active_source_bit',sub(delta,z) if interior else sub(z,delta)),
        ('delta>0',delta),('seventh_global_scope',sub(chi,delta))]

def seventh_lift(key,z):
    target,m = seventh_req(key,z)
    pp = g76.seventh_positions(5 if key[0]=='V' else 3,z)
    assert pp[-1] == add(scale(2,eta),target)
    for j,a in enumerate(SEVENTH[key]):
        q,lower = atom_req(a,pp[j]); assert q==pp[j+1]
        m += [(f'{j}:{name}',x) for name,x in lower]
        m += [(f'no_earlier_seventh_hit{j}',sub(scale(2,eta),q)
               if j<len(SEVENTH[key])-1 else sub(q,scale(2,eta)))]
    return target,m

def eighth_lift(word,n,z):
    pp = [z]+[add(z,sub(chi,scale(j,psi))) for j in range(1,n+1)]
    m = [('source>0',z),('source<psi',sub(psi,z)),('return>0',pp[-1]),('return<psi',sub(psi,pp[-1]))]
    for j,key in enumerate(word):
        q,lower = seventh_req(key,pp[j]); assert q==pp[j+1]
        m += [(f'{j}:{name}',x) for name,x in lower]
        m += [(f'no_earlier_eighth_hit{j}',sub(q,psi) if j<n-1 else sub(psi,q))]
    return pp[-1],m

def geometry_audit():
    levels = {}
    # Recheck the three sixth atoms, with their full inherited fifth contracts,
    # over the broader formula domain 0<delta<chi; not just the new proof strip.
    for key,(s,n) in ATOMS.items():
        target,req = atom_req(key,seed)
        q,m = g75.sixth_lift(s,n,seed); assert q==target
        levels[key] = audit(m,vertices(RANGE+tuple(a for _,a in req)))
    seven = {}
    for key in SEVENTH:
        _,req = seventh_req(key,seed)
        _,m = seventh_lift(key,seed)
        seven[key] = audit(m,vertices(RANGE+tuple(a for _,a in req)))
    eight = {}
    base = RANGE+(delta,sub(psi,delta),seed,sub(psi,seed))
    for key,w in EIGHTH.items():
        i,n = map(int,key.split('/'))
        cond = base+(sub(sigma,seed) if n==2 else sub(seed,sigma),
                     sub(delta,seed) if i else sub(seed,delta))
        target,m = eighth_lift(w,n,seed)
        m.append(('eighth_global_scope',sub(psi,delta)))
        out = audit(m,vertices(cond))
        if i==1:
            face = vertices(cond+(sub(delta,psi),))
            out['delta_equals_psi_endpoint'] = audit(m,face)
        eight[key] = out
    # Exact image tiling: z<sigma -> z+nu; z>sigma -> z-sigma.
    assert add(sigma,nu)==psi
    assert sub(chi,scale(2,psi))==nu
    assert sub(chi,scale(3,psi))==scale(-1,sigma)
    # Immediate new complete word, after delta exceeds psi.
    extra = sub(delta,psi)
    cond = RANGE+(extra,sub(sigma,extra),sub(nu,extra),sub(seed,sigma),sub(add(sigma,extra),seed))
    target,m = eighth_lift(GUARD,3,seed)
    guard = audit(m,vertices(cond))
    # The seventh first-return towers have total base-circle length xi.
    assert add(scale(3,sub(chi,psi)),scale(5,psi))==xi
    return {
        'normalization':'gamma=1; 777/157<beta/gamma<1069/216',
        'sixth_atom_cells':levels,'seventh_formula_scope':'0<delta<chi7',
        'four_seventh_map_cells':seven,
        'eighth_section':'0<z<psi7 in the seventh coordinate',
        'physical_section':'h-beta+gamma-xi+2eta7<t<h-beta+gamma-xi+2eta7+psi7',
        'eighth_return_times':'2 if z<sigma; 3 if z>sigma; sigma=3psi7-chi7',
        'eighth_map':'z -> z+nu mod psi7; nu=chi7-2psi7',
        'eighth_image_tiling':'(nu,psi7) and (0,nu)',
        'new_exclusion_scope':'0<delta<=psi7','four_eighth_cells':eight,
        'above_scope_domain':'delta=psi7+a; 0<a<min(sigma,nu); sigma<z<sigma+a',
        'above_scope_cell':guard,
        'seventh_tower_total_length':'3(chi7-psi7)+5psi7=xi',
        'sampled_topology':False,
    }

def main():
    out = {
        'pass':'SZ-KERNEL-EDGE-GERM-77','standing':'UNRATIFIED',
        'entry_commit':'dd887fa208fd91c7fa14284d2c3e4740fad6624f',
        'new_exclusion_scope':'L76<L<=L76+psi7',
        'inherited_three_layer_formula_scope':'2h<e<=3h',
        'experimental_endpoint':'log(3^3328234/(2^3786640*5^641055))',
        'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
        'sixth_atom_dictionary':ATOMS,'seventh_word_dictionary':SEVENTH,'eighth_word_dictionary':EIGHTH,
        'arithmetic':prime_data(),'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
        'full_parent_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
        'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE',
    }
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
