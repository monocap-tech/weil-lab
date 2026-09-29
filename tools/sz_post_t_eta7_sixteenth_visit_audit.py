#!/usr/bin/env python3
"""GERM-91: sixteenth sixth-visit transfer and four direct seventh cones.

New exclusion: 0<d<=eta7+psi7, d=t-eta7=e-e90. Three sixth atoms and
seven seventh formulas are licensed on the larger interval 0<d<=omega.
Six hyperbolic seventh maps, with four fixed-parameter rational charts,
cover the exclusion interval. The next double-F20 nonwrap is elliptic.
Run with assertions enabled. No lower full symbolic suite is rerun.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of the certificate; run without -O.'
ROOT = Path(__file__).resolve().parents[1]
PIN_PATH = 'tools/sz_post_t_chi7_seventh_wrap_audit.py'
PIN_SHA = '9c643f44d12669776cb07cd6acea7ef8e3485f5c7643ed987173d72c4eedcc79'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest() == PIN_SHA
import sz_post_t_chi7_seventh_wrap_audit as parent
g81, g77, g75, old = parent.g81, parent.g77, parent.g75, parent.old
product, det = parent.product, parent.det
ATOMS = {'E19': (15,19), 'E20': (15,20), 'F20': (16,20)}
# Chronological sixth words; products act rightmost first.
SEVENTH = {
    'U0': ['E20','E20','E19'],
    'U1': ['E20','F20','E19'],
    'U2': ['F20','F20','E19'],
    'V0': ['E20','E20','E19','E20','E19'],
    'V1': ['E20','F20','E19','E20','E19'],
    'V2': ['E20','F20','E19','F20','E19'],
    'V3': ['F20','F20','E19','F20','E19'],
}
CHARTS = {
    'I': parent.CHART,
    'II': [[1,-2],[F(-109,50),F(114,25)]],
    'III': [[1,F(-1,4)],[F(-23,10),F(1,2)]],
    'IV': [[1,F(1,6)],[F(-93,40),F(-8,15)]],
}
KEYS = {'I': ('U0','V0','V1'), 'II': ('U0','U1','V1'),
        'III': ('U1','V1','V2'), 'IV': ('U1','V2','V3')}
SIGNS = {'U0': -1, 'U1': -1, 'V0': 1, 'V1': 1, 'V2': 1, 'V3': -1}
FACTOR = F(4,3)


def arithmetic():
    add, sub, mul = old.add, old.sub, old.mul
    h, k = (-4,4,-1), (4,-1,-1)
    kap=sub(k,mul(5,h)); tau=sub(h,mul(5,kap)); th=sub(kap,mul(8,tau))
    alpha=sub(tau,mul(3,th)); beta=sub(th,alpha); gamma=sub(alpha,beta)
    xi=sub(mul(5,gamma),beta); omega=sub(gamma,mul(19,xi))
    eta=sub(xi,omega); chi=sub(mul(2,omega),xi); psi=sub(eta,chi)
    increment=add(eta,psi); L90=(-619016,544082,-104797)
    L91=add(L90,increment); top=add((4,-1,0),mul(3,h))
    formula_top=add(L90,omega)
    assert add(chi,psi)==eta and add(eta,omega)==xi
    assert sub(omega,increment)==sub(chi,psi)
    assert add(mul(3,sub(chi,psi)),mul(5,psi))==xi
    assert L91==(-3827628,3364260,-647994)
    assert L91==add((4,-1,0),sub(mul(802451,h),mul(154457,k)))
    assert formula_top==(152396,-133943,25798)
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(v): return sum((n*l for n,l in zip(v,logs)),old.box(0))
    checks={'psi_positive':psi, 'chi_gt_psi':sub(chi,psi),
            'eta_gt_chi':sub(eta,chi), 'omega_gt_eta_plus_psi':sub(omega,increment),
            'sixth_exterior_gap_through_formula_endpoint':sub(sub(gamma,mul(16,xi)),omega),
            'beta_box_lower':sub(mul(157,beta),mul(777,gamma)),
            'beta_box_upper':sub(mul(1069,gamma),mul(216,beta)),
            'formula_endpoint_below_three_layers':sub(top,formula_top)}
    boxes={name:enc(v) for name,v in checks.items()}
    assert all(v.lo>0 for v in boxes.values())
    return {'rational_log_order_checks':{k:g77.show_box(v,38) for k,v in boxes.items()},
            'endpoint_prime_log_vector':L91, 'endpoint_h_k_vector':[802451,-154457],
            'endpoint_decimal':g77.show_box(enc(L91),38),
            'increment':'eta7+psi7', 'increment_prime_log_vector':increment,
            'increment_decimal':g77.show_box(enc(increment),38),
            'formula_endpoint_prime_log_vector':formula_top,
            'remaining_sixth_seventh_formula_width':g77.show_box(enc(sub(omega,increment)),38),
            'remaining_three_layer_width':g77.show_box(enc(sub(top,L91)),38)}


def rational_audit():
    original,pivots=g75.parent.parent.parent.parent.recalculate_returns()
    legacy=g75.parent.parent.parent
    first={k:product(w,original) for k,w in legacy.FIRST.items()}
    second={k:product(w,first) for k,w in legacy.SECOND.items()}
    boxes=json.loads((ROOT/'notes/_recurrence71_audit.json').read_text())['audit']['rational_audit']['second_section_maps']
    for key,b in second.items():
        for i in range(2):
            for j in range(2):
                lo,hi=map(F,boxes[key][i][j]); assert lo<=b[i][j].lo<=b[i][j].hi<=hi
    third={k:product(w,second) for k,w in g75.THIRD.items()}
    fourth={k:product(w,third) for k,w in g75.FOURTH.items()}
    fifth={k:product(w,fourth) for k,w in g75.FIFTH.items()}
    atoms={k:product(g75.sixth_word(*pair),fifth) for k,pair in ATOMS.items()}
    count6={}
    for key,pair in ATOMS.items():
        ow=g75.to_original(g75.sixth_word(*pair))
        assert legacy.determinant_exponent(ow)==0
        assert len(ow)==1654*pair[1]-297
        count6[key]=len(ow)
    assert ATOMS['F20']==parent.NEXT_PAIR
    assert SEVENTH['U0']==parent.SEVENTH['U']
    assert SEVENTH['V0']==parent.SEVENTH['V1']
    seven={k:product(w,atoms) for k,w in SEVENTH.items()}
    spectra={}
    for key,b in seven.items():
        dd=det(b); tr=b[0][0]+b[1][1]; disc=tr*tr-4*dd
        assert dd.lo>0 and dd.lo<=1<=dd.hi
        assert disc.hi<0 if key=='U2' else disc.lo>0
        count=sum(count6[a] for a in SEVENTH[key])
        assert count==(96695 if key.startswith('U') else 160607)
        spectra[key]={'trace':old.display_matrix([[tr]]),'discriminant':old.display_matrix([[disc]]),
                      'original_step_count':count}
    f=atoms['F20']; tr=f[0][0]+f[1][1]
    assert (tr*tr-4*det(f)).hi<0
    expected_dets={'I':F(7,30),'II':F(1,5),'III':F(-3,40),'IV':F(-7,48)}
    cert={}
    for label,C in CHARTS.items():
        exact=F(C[0][0])*F(C[1][1])-F(C[0][1])*F(C[1][0])
        assert exact==expected_dets[label]
        cc=det(g75.mat(C)); assert cc.lo<=exact<=cc.hi and cc.lo*cc.hi>0
        cert[label]={key:g77.cone_test(seven[key],C,SIGNS[key],FACTOR) for key in KEYS[label]}
    return {'physical_recalculation':'FRESH PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
            'precision':{'grid':'10^120','log_series_terms':400},'layer_pivots':pivots,
            'GERM71_box_regression':'CONTAINED; not rounded proof inputs',
            'charts':{k:[[str(x) for x in row] for row in C] for k,C in CHARTS.items()},
            'chart_determinants':{k:str(v) for k,v in expected_dets.items()},
            'common_forward_backward_factor':'4/3','twelve_chart_tests':cert,
            'seven_matrix_spectra':spectra,
            'formula_map_count':7,'excluded_range_distinct_maps':6,
            'next_matrix':'U2=E19 F20^2', 'next_status':'ELLIPTIC; NOT IN THE CERTIFIED CONE LIBRARY',
            'eighth_or_deeper_induction_used':False,'new_retained_coordinates':0}


# Exact affine coordinates: gamma=1; variables beta/gamma, zeta/gamma, seed/gamma.
af,add,sub,vertices=parent.af,parent.add,parent.sub,parent.vertices
scale,audit=parent.scale,parent.audit
seed,t,eta,chi,psi,xi,omega=parent.seed,parent.t,parent.eta,parent.chi,parent.psi,parent.xi,parent.omega
RANGE=parent.RANGE; zero=af(); d=sub(t,eta); limit=add(eta,psi)


def atom_req(key,y):
    is19=key=='E19'; q=add(y,omega) if is19 else sub(y,eta)
    m=[('y>0',y),('y<xi',sub(xi,y)),('q>0',q),('q<xi',sub(xi,q)),
       ('sixth_lower_global_scope',d),('sixth_upper_global_scope',sub(omega,d)),
       ('sixth_cut',sub(eta,y) if is19 else sub(y,eta))]
    if not is19:
        m.append(('sixteenth_visit_bit',sub(add(eta,d),y) if key=='F20' else sub(y,add(eta,d))))
    return q,m


def atom_lift(key,y):
    q,m=atom_req(key,y); out,lower=g75.sixth_lift(*ATOMS[key],y)
    assert out==q
    return q,m+[(f'fifth:{name}',v) for name,v in lower]


def seventh_req(key,z):
    wrap=key.startswith('V'); q=add(z,sub(chi,psi)) if wrap else sub(z,psi)
    m=[('z>0',z),('z<chi',sub(chi,z)),('q>0',q),('q<chi',sub(chi,q)),
       ('seventh_lower_global_scope',d),('seventh_upper_global_scope',sub(omega,d)),
       ('seventh_cut',sub(psi,z) if wrap else sub(z,psi))]
    # Necessary and sufficient source intervals. High sixth sources are
    # ordered eta+z < omega+z < 2eta+z on the wrap branch.
    if key in ('U0','V0'): m.append(('before_first_F',sub(z,d)))
    elif key=='U1': m += [('after_first_F',sub(d,z)),('before_initial_F',sub(add(eta,z),d))]
    elif key=='U2': m.append(('after_initial_F',sub(d,add(eta,z))))
    elif key=='V1': m += [('after_first_F',sub(d,z)),('before_fourth_F',sub(add(chi,z),d))]
    elif key=='V2': m += [('after_fourth_F',sub(d,add(chi,z))),('before_initial_F',sub(add(eta,z),d))]
    elif key=='V3': m.append(('after_initial_F',sub(d,add(eta,z))))
    else: raise AssertionError(key)
    return q,m


def seventh_lift(key,z):
    q,m=seventh_req(key,z); w=SEVENTH[key]
    pp=g77.g76.seventh_positions(len(w),z)
    assert pp[-1]==add(scale(2,eta),q)
    for j,k in enumerate(w):
        out,lower=atom_req(k,pp[j]); assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_hit{j}',sub(scale(2,eta),out) if j<len(w)-1 else sub(out,scale(2,eta))))
    return q,m


def geometry_audit():
    sixth={}
    for key in ATOMS:
        _,rr=atom_req(key,seed); _,m=atom_lift(key,seed)
        cond=RANGE+tuple(v for _,v in rr); item=audit(m,vertices(cond))
        if key in ('E19','E20'): item['d_zero_entry']=audit(m,vertices(cond+(sub(zero,d),)))
        if key in ('E19','F20'): item['d_omega_formula_endpoint']=audit(m,vertices(cond+(sub(d,omega),)))
        sixth[key]=item
    seventh={}
    for key in SEVENTH:
        _,rr=seventh_req(key,seed); _,m=seventh_lift(key,seed)
        cond=RANGE+tuple(v for _,v in rr); item=audit(m,vertices(cond))
        if key in ('U0','V0'): item['d_zero_entry']=audit(m,vertices(cond+(sub(zero,d),)))
        if key in ('U2','V3'): item['d_omega_formula_endpoint']=audit(m,vertices(cond+(sub(d,omega),)))
        seventh[key]=item
    regimes={'I':(zero,psi),'II':(psi,chi),'III':(chi,eta),'IV':(eta,limit)}
    cells={}
    survivors={psi:('U0','V1'),chi:('U1','V1'),eta:('U1','V2'),limit:('U1','V3')}
    for label,(low,high) in regimes.items():
        checked={}
        for key in KEYS[label]:
            _,rr=seventh_req(key,seed); _,m=seventh_lift(key,seed)
            cond=RANGE+(sub(d,low),sub(high,d))+tuple(v for _,v in rr)
            item=audit(m,vertices(cond))
            for face in (low,high):
                if face in survivors and key in survivors[face]:
                    item['face_'+str(face)]=audit(m,vertices(cond+(sub(d,face),sub(face,d))))
            checked[key]=item
        cells[label]=checked
    assert add(chi,psi)==eta and add(eta,omega)==xi
    assert add(scale(3,sub(chi,psi)),scale(5,psi))==xi
    assert g75.zeta==add(scale(15,xi),d)
    # First U2 after the claimed endpoint, but inside the proved formula scope.
    b=sub(d,limit); _,m=seventh_lift('U2',seed)
    cond=RANGE+(b,sub(sub(chi,psi),b),sub(seed,psi),sub(add(psi,b),seed))
    guard=audit(m,vertices(cond))
    return {'parameter':'d=t-eta7=e-e90','new_exclusion_scope':'0<d<=eta7+psi7',
            'sixth_seventh_formula_scope':'0<d<=omega',
            'three_sixth_contracts':sixth,'seven_seventh_contracts':seventh,
            'regime_intervals':{'I':'0<d<=psi7','II':'psi7<=d<=chi7',
                                'III':'chi7<=d<=eta7','IV':'eta7<=d<=eta7+psi7'},
            'twelve_parameter_chart_cells':cells,
            'section':'2eta7<y<xi; coordinate 0<z<chi7',
            'seventh_map':'z -> z-psi7 mod chi7',
            'tower_identity':'3(chi7-psi7)+5psi7=xi',
            'physical_field':'W(t0+z); t0=h-beta+gamma-xi+2eta7',
            'exclusion_endpoint_maps':['U1','V3'],
            'formula_endpoint_maps':['U2','V3'],
            'next_domain':'d=eta7+psi7+b; 0<b<chi7-psi7; psi7<z<psi7+b',
            'next_sixth_word':SEVENTH['U2'],'next_guard':guard,'sampled_topology':False}


def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-91','standing':'UNRATIFIED',
         'entry_commit':'c936e8684502dcdc475c1261858da9eb655afd29',
         'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
         'matrix_namespace':'E19/E20 retain GERM-81 definitions; F20=B16,20; U0/U1/U2/V0/V1/V2/V3 are GERM-91-local',
         'sixth_atoms':ATOMS,'seventh_word_dictionary':SEVENTH,
         'arithmetic':arithmetic(),'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
         'full_lower_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
         'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
