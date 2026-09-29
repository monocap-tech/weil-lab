#!/usr/bin/env python3
"""GERM-92: double-F20 nonwrap controlled by three complete eighth returns.

Proves 0<b<=nu8, b=e-e91, using GERM-91-local U1/U2/V3. All three
new eighth maps have a signed rational cone with factor 5. No ninth
induction or additional state coordinate is used. Run without -O.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of the certificate; run without -O.'
ROOT = Path(__file__).resolve().parents[1]
PIN_PATH = 'tools/sz_post_t_eta7_sixteenth_visit_audit.py'
PIN_SHA = '909435197072a187936ec43799a2475bc6263b276d0f3f7c1c68fa307fcbef5a'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest() == PIN_SHA
import sz_post_t_eta7_sixteenth_visit_audit as parent
g75, g77, old = parent.g75, parent.g77, parent.old
product, det = parent.product, parent.det
EIGHTH = {'A': ['V3','U1'], 'D': ['V3','U1','U1'], 'E': ['V3','U1','U2']}
SIGNS = {'A': 1, 'D': -1, 'E': 1}
CHART = [[1,F(-3,2)],[F(3,10),2]]
FACTOR = F(5)
NEXT = ['V3','U2']


def arithmetic():
    add, sub, mul = old.add, old.sub, old.mul
    h, k = (-4,4,-1), (4,-1,-1)
    kap=sub(k,mul(5,h)); tau=sub(h,mul(5,kap)); th=sub(kap,mul(8,tau))
    alpha=sub(tau,mul(3,th)); beta=sub(th,alpha); gamma=sub(alpha,beta)
    xi=sub(mul(5,gamma),beta); om=sub(gamma,mul(19,xi))
    eta=sub(xi,om); chi=sub(mul(2,om),xi); psi=sub(eta,chi)
    sigma=sub(mul(3,psi),chi); nu=sub(chi,mul(2,psi))
    L91=(-3827628,3364260,-647994); L92=add(L91,nu)
    top=add((4,-1,0),mul(3,h)); formula_top=add((-619016,544082,-104797),om)
    assert nu==(6376236,-5604330,1079455)
    assert L92==(2548608,-2240070,431461)
    assert L92==add((4,-1,0),add(mul(-534306,h),mul(102845,k)))
    assert L92==add((-619016,544082,-104797),mul(2,chi))
    assert sub(formula_top,L92)==psi
    assert add(sigma,nu)==psi
    assert add(mul(2,sigma),mul(3,nu))==chi
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(v): return sum((n*l for n,l in zip(v,logs)),old.box(0))
    checks={'sigma_positive':sigma,'nu_positive':nu,
            'parent_formula_margin_at_new_endpoint':psi,
            'new_endpoint_below_three_layers':sub(top,L92)}
    boxes={name:enc(v) for name,v in checks.items()}
    assert all(v.lo>0 for v in boxes.values())
    return {'rational_log_order_checks':{name:g77.show_box(v,38) for name,v in boxes.items()},
            'endpoint_prime_log_vector':L92,'endpoint_h_k_vector':[-534306,102845],
            'endpoint_decimal':g77.show_box(enc(L92),38),
            'increment':'nu8=chi7-2psi7','increment_prime_log_vector':nu,
            'increment_decimal':g77.show_box(enc(nu),38),
            'remaining_parent_formula_width':g77.show_box(enc(psi),38),
            'remaining_three_layer_width':g77.show_box(enc(sub(top,L92)),38),
            'tower_identity':'2sigma8+3nu8=chi7; sigma8+nu8=psi7'}


def rational_audit():
    original,pivots=g75.parent.parent.parent.parent.recalculate_returns()
    legacy=g75.parent.parent.parent
    first={key:product(w,original) for key,w in legacy.FIRST.items()}
    second={key:product(w,first) for key,w in legacy.SECOND.items()}
    boxes=json.loads((ROOT/'notes/_recurrence71_audit.json').read_text())['audit']['rational_audit']['second_section_maps']
    for key,m in second.items():
        for i in range(2):
            for j in range(2):
                lo,hi=map(F,boxes[key][i][j]); assert lo<=m[i][j].lo<=m[i][j].hi<=hi
    third={key:product(w,second) for key,w in g75.THIRD.items()}
    fourth={key:product(w,third) for key,w in g75.FOURTH.items()}
    fifth={key:product(w,fourth) for key,w in g75.FIFTH.items()}
    atoms={key:product(g75.sixth_word(*pair),fifth) for key,pair in parent.ATOMS.items()}
    count6={}
    for key,pair in parent.ATOMS.items():
        w=g75.to_original(g75.sixth_word(*pair))
        assert legacy.determinant_exponent(w)==0
        assert len(w)==1654*pair[1]-297
        count6[key]=len(w)
    seven={key:product(w,atoms) for key,w in parent.SEVENTH.items()}
    count7={key:sum(count6[a] for a in w) for key,w in parent.SEVENTH.items()}
    assert count7['U1']==count7['U2']==96695 and count7['V3']==160607
    eight={key:product(w,seven) for key,w in EIGHTH.items()}
    exact_chart_det=F(CHART[0][0])*F(CHART[1][1])-F(CHART[0][1])*F(CHART[1][0])
    assert exact_chart_det==F(49,20)
    cert={}
    for key,m in eight.items():
        dd=det(m); tr=m[0][0]+m[1][1]; disc=tr*tr-4*dd
        assert dd.lo>0 and dd.lo<=1<=dd.hi and disc.lo>0
        item=g77.cone_test(m,CHART,SIGNS[key],FACTOR)
        count=sum(count7[a] for a in EIGHTH[key])
        assert count==(257302 if key=='A' else 353997)
        item.update({'seventh_word':EIGHTH[key],'original_step_count':count,
                     'trace':old.display_matrix([[tr]]),'discriminant':old.display_matrix([[disc]])})
        cert[key]=item
    u=seven['U2']; utr=u[0][0]+u[1][1]
    assert (utr*utr-4*det(u)).hi<0
    m=product(NEXT,seven); tr=m[0][0]+m[1][1]; dd=det(m); disc=tr*tr-4*dd
    assert dd.lo>0 and dd.lo<=1<=dd.hi and disc.hi<0
    return {'physical_recalculation':'FRESH PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
            'precision':{'grid':'10^120','log_series_terms':400},'layer_pivots':pivots,
            'GERM71_box_regression':'CONTAINED; not rounded proof inputs',
            'chart':[[str(x) for x in row] for row in CHART],'chart_determinant':str(exact_chart_det),
            'common_forward_backward_factor':'5','three_eighth_cone_tests':cert,
            'input_U2_status':'ELLIPTIC; no individual expanding cone claimed',
            'next_matrix':'U2 V3, GERM-91-local seventh inputs','next_seventh_word':NEXT,
            'next_trace':old.display_matrix([[tr]]),'next_determinant':old.display_matrix([[dd]]),
            'next_discriminant':old.display_matrix([[disc]]),'next_status':'ELLIPTIC NEW TWO-STEP EIGHTH WORD',
            'ninth_or_deeper_induction_used':False,'new_retained_coordinates':0}


# Exact affine coordinates inherited from GERM-91, normalized by gamma.
af,add,sub,vertices=parent.af,parent.add,parent.sub,parent.vertices
scale,audit=parent.scale,parent.audit
seed,psi,chi,eta,omega=parent.seed,parent.psi,parent.chi,parent.eta,parent.omega
RANGE=parent.RANGE; zero=af(); b=sub(parent.d,parent.limit)
sigma=sub(scale(3,psi),chi); nu=sub(chi,scale(2,psi))


def eighth_req(key,z):
    q=add(z,nu) if key=='A' else sub(z,sigma)
    m=[('z>0',z),('z<psi',sub(psi,z)),('q>0',q),('q<psi',sub(psi,q)),
       ('eighth_lower_global_scope',b),('eighth_upper_global_scope',sub(nu,b)),
       ('eighth_cut',sub(sigma,z) if key=='A' else sub(z,sigma))]
    if key=='D': m.append(('second_nonwrap_exterior',sub(z,add(sigma,b))))
    elif key=='E': m.append(('second_nonwrap_interior',sub(add(sigma,b),z)))
    else: assert key=='A'
    return q,m


def eighth_word_lift(word,z):
    n=len(word); assert n in (2,3)
    pp=[z]+[add(z,sub(chi,scale(j,psi))) for j in range(1,n+1)]
    q=pp[-1]
    m=[('z>0',z),('z<psi',sub(psi,z)),('q>0',q),('q<psi',sub(psi,q))]
    for j,key in enumerate(word):
        out,lower=parent.seventh_req(key,pp[j]); assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_eighth_hit{j}',sub(out,psi) if j<n-1 else sub(psi,out)))
    return q,m


def eighth_lift(key,z):
    q,m=eighth_req(key,z); out,lower=eighth_word_lift(EIGHTH[key],z)
    assert out==q
    return q,m+[(f'seventh:{name}',v) for name,v in lower]


def geometry_audit():
    # Recheck the source contracts on which the typed substitutions depend.
    lower=parent.geometry_audit()
    selected={}
    for key in ('U1','U2','V3'):
        _,rr=parent.seventh_req(key,seed); _,m=parent.seventh_lift(key,seed)
        cond=RANGE+(b,sub(nu,b))+tuple(v for _,v in rr)
        selected[key]=audit(m,vertices(cond))
    cells={}
    for key in EIGHTH:
        _,rr=eighth_req(key,seed); _,m=eighth_lift(key,seed)
        cond=RANGE+tuple(v for _,v in rr); item=audit(m,vertices(cond))
        if key in ('A','D'): item['b_zero_entry']=audit(m,vertices(cond+(sub(zero,b),)))
        if key in ('A','E'): item['b_nu_endpoint']=audit(m,vertices(cond+(sub(b,nu),)))
        cells[key]=item
    assert add(sigma,nu)==psi
    assert add(scale(2,sigma),scale(3,nu))==chi
    assert sub(omega,add(parent.limit,nu))==psi
    # Beyond b=nu: the first nonwrap in the two-step return changes to U2.
    excess=sub(b,nu); q,m=eighth_word_lift(NEXT,seed)
    assert q==add(seed,nu)
    cond=RANGE+(excess,sub(sigma,excess),seed,sub(excess,seed))
    guard=audit(m,vertices(cond))
    return {'parameter':'b=e-e91=d-(eta7+psi7)','new_exclusion_scope':'0<b<=nu8',
            'parent_source_contract_recheck':lower,'selected_seventh_cells':selected,
            'three_eighth_contracts':cells,'section':'0<z<psi7',
            'eighth_map':'z -> z-sigma8 mod psi7','images':'(nu8,psi7) and (0,nu8)',
            'tower_identity':'2sigma8+3nu8=chi7',
            'physical_field':'W(t0+z); t0=h-beta+gamma-xi+2eta7',
            'entry_maps':['A','D'],'endpoint_maps':['A','E'],
            'next_domain':'b=nu8+excess; 0<z<excess<sigma8',
            'next_seventh_word':NEXT,'next_guard':guard,'sampled_topology':False}


def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-92','standing':'UNRATIFIED',
         'entry_commit':'23c019e7e9caf103d5ccc3f8b6f38f0b9f8eceec',
         'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
         'matrix_namespace':'U1/U2/V3 are GERM-91-local seventh maps; A/D/E are GERM-92-local eighth maps',
         'eighth_word_dictionary':EIGHTH,'new_exclusion_scope':'0<b<=nu8, b=e-e91',
         'arithmetic':arithmetic(),'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
         'full_lower_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
         'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
