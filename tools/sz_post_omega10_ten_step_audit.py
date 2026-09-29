#!/usr/bin/env python3
"""GERM-88: direct tenth-return control of the complete post-c10 window.

Proves c10<a<=sigma8, a=e-e85, including the GERM-87 overlap and the new
range c10+omega10<a<=sigma8. Twenty-one legal tenth words share the exact
GERM-86 chart. No eleventh induction is used. Each intermediate source is
checked. Coefficients and signs are outward rational; domains are exact.
Run without -O. GERM-87's restored bundle bytes are pinned, not its corrupt
entry-commit copy. The old remainder-width annotation is corrected here.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of the certificate; run without -O.'
ROOT = Path(__file__).resolve().parents[1]
PINS = {
    'tools/sz_post_c10_tenth_map_audit.py': '7194b18fbfd427038f4fe5b73f5adcc46038f0cc8d89da82ae9c7d88025ea18f',
    'tools/sz_post_chi_minus_psi_eighth_map_audit.py': '97fd7d30a211e4bf0ae464df0c3f8dd41aab92d0e25be1de41343a6f4c6dae48',
}
for path, sha in PINS.items():
    assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == sha
import sz_post_c10_tenth_map_audit as g87
g86 = g87.parent
g81, g77, g75, old = g86.g81, g86.g77, g86.g75, g86.old
product, det = g86.product, g86.det
WORDS = {(s,n): ['Q']+['R']*(n-s-1)+['S']*s for n in (10,11) for s in range(n)}
CHART = g86.CHART
FACTOR = F(4)
NEXT = ['V1','U1','U1']  # GERM-81-local seventh matrices, not later namesakes.


def sign_for(s, n):
    if n == 10:
        return -(-1)**(s//2)
    assert n == 11
    return -1 if s == 0 else (-1)**((s-1)//2)


def arithmetic():
    add, sub, mul = old.add, old.sub, old.mul
    h=(-4,4,-1); k=(4,-1,-1)
    kap=sub(k,mul(5,h)); tau=sub(h,mul(5,kap)); theta=sub(kap,mul(8,tau))
    alpha=sub(tau,mul(3,theta)); beta=sub(theta,alpha); gamma=sub(alpha,beta)
    xi=sub(mul(5,gamma),beta); omega=sub(gamma,mul(19,xi))
    eta=sub(xi,omega); chi=sub(mul(2,omega),xi); psi=sub(eta,chi)
    sigma=sub(mul(3,psi),chi); rho=sub(psi,mul(3,sigma)); c=sub(sigma,rho)
    omt=sub(sigma,mul(10,c)); ell=sub(c,omt); nu=sub(chi,mul(2,psi))
    L80=(193384,-169969,32737)
    L85=add(L80,sub(chi,psi)); L86=add(L85,c); L87=add(L86,omt)
    L88=add(L85,sigma); top=add((4,-1,0),mul(3,h))
    assert L87==(289643180,-254579024,49034692)
    assert L88==(-4599040,4042285,-778589)
    assert L88==add(L80,mul(2,psi))
    assert L88==add((4,-1,0),add(mul(964175,h),mul(-185586,k)))
    inc=sub(L88,L87)
    assert inc==sub(rho,omt)==(-294242220,258621309,-49813281)
    assert sub(L88,L86)==rho
    assert add(mul(10,ell),mul(11,omt))==sigma
    assert add(mul(3,c),mul(4,rho))==psi
    logs=[old.log_box(p) for p in (2,3,5)]
    def enc(v): return sum((n*l for n,l in zip(v,logs)),old.box(0))
    checks={'omega10_positive':omt,'c11_positive':ell,'rho9_positive':rho,
            'new_increment_positive':inc,'endpoint_below_three_layers':sub(top,L88),
            'eighth_endpoint_strictly_below_seventh_bound':nu,
            'ninth_endpoint_above_two_c10':sub(sigma,mul(2,c))}
    boxes={key:enc(v) for key,v in checks.items()}
    assert all(x.lo>0 for x in boxes.values())
    return {'rational_log_order_checks':{k:g77.show_box(v,38) for k,v in boxes.items()},
            'endpoint_prime_log_vector':L88,'endpoint_h_k_vector':[964175,-185586],
            'endpoint_decimal':g77.show_box(enc(L88),38),
            'new_increment_from_GERM87_vector':inc,'new_increment_from_GERM87':g77.show_box(enc(inc),38),
            'corrected_GERM87_eighth_remainder':g77.show_box(enc(inc),38),
            'previous_mislabeled_GERM87_remainder':g77.show_box(enc(rho),38),
            'remaining_eighth_formula_width':'ZERO',
            'remaining_three_layer_width':g77.show_box(enc(sub(top,L88)),38),
            'tower_identity':'10*c11+11*omega10=sigma8'}


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
    atoms={k:product(g75.sixth_word(s,n),fifth) for k,(s,n) in g81.ATOMS.items()}
    counts6={}
    for key,(s,n) in g81.ATOMS.items():
        w=g75.to_original(g75.sixth_word(s,n))
        assert legacy.determinant_exponent(w)==0
        assert len(w)==1654*n-297
        counts6[key]=len(w)
    seven={k:product(w,atoms) for k,w in g81.SEVENTH.items()}
    eight={k:product(w,seven) for k,w in g86.EIGHTH.items()}
    nine={k:product(w,eight) for k,w in g86.NINTH.items()}
    counts7={k:sum(counts6[x] for x in w) for k,w in g81.SEVENTH.items()}
    counts8={k:sum(counts7[x] for x in w) for k,w in g86.EIGHTH.items()}
    counts9={k:sum(counts8[x] for x in w) for k,w in g86.NINTH.items()}
    assert counts9=={'P':965296,'Q':965296,'R':1319293,'S':1319293}
    for lib in (atoms,seven,eight,nine):
        for b in lib.values():
            dd=det(b); assert dd.lo>0 and dd.lo<=1<=dd.hi
    assert WORDS[0,10]==g87.TENTH['V']
    assert WORDS[0,11]==g87.TENTH['U0']
    assert WORDS[1,11]==g87.TENTH['U1']
    assert WORDS[1,10]==g87.NEXT  # the changed ten-step word is retained literally
    cert={}
    for (s,n),w in WORDS.items():
        b=product(w,nine); item=g77.cone_test(b,CHART,sign_for(s,n),FACTOR)
        tr=b[0][0]+b[1][1]; disc=tr*tr-4*det(b); assert disc.lo>0
        count=sum(counts9[x] for x in w); assert count==965296+(n-1)*1319293
        item.update({'ninth_word':w,'original_step_count':count,'determinant_rho_exponent':0})
        cert[f'{s}/{n}']=item
    b=product(NEXT,seven); tr=b[0][0]+b[1][1]; dd=det(b); disc=tr*tr-4*dd
    assert dd.lo>0 and dd.lo<=1<=dd.hi and F(-33)<tr.lo<tr.hi<F(-32) and disc.lo>0
    return {'physical_recalculation':'FRESH PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
            'precision':{'grid':'10^120','log_series_terms':400},'layer_pivots':pivots,
            'GERM71_box_regression':'CONTAINED; not rounded proof inputs',
            'same_chart_as_GERM86_87':True,'chart':[['1','1'],['-11/5','-8/5']],
            'common_forward_backward_factor':'4','twenty_one_complete_returns':cert,
            'distinct_temporal_words':21,'all_tenth_discriminants':'POSITIVE',
            'next_eighth_seventh_word':NEXT,'next_matrix_namespace':'GERM-81-local seventh U1^2 V1',
            'next_trace':old.display_matrix([[tr]]),'next_discriminant':old.display_matrix([[disc]]),
            'next_status':'HYPERBOLIC NEW EIGHTH SOURCE WORD; NO EXCLUSION BEYOND t=2psi7'}


# Exact affine coordinates from the already-proved GERM-86 source system.
af,add,sub,val,vertices=g86.af,g86.add,g86.sub,g86.val,g86.vertices
scale,audit=g86.scale,g86.audit
seed,a,sigma,c,ell=g86.seed,g86.a,g86.sigma,g86.c,g86.ell
omt=sub(sigma,scale(10,c)); a87=add(c,omt)
RANGE=g86.RANGE


def tenth_req(s,n,y):
    q=add(y,sub(sigma,scale(n,c)))
    margins=[('source_low',y),('source_high',sub(c,y)),('target_low',q),('target_high',sub(c,q)),
             ('lower_global_scope',sub(a,c)),('upper_global_scope',sub(sigma,a)),
             ('return_cut',sub(ell,y) if n==10 else sub(y,ell))]
    if s==0:
        margins.append(('no_internal_later_source',sub(add(q,c),a)))
    else:
        margins += [('last_internal_source',sub(a,add(q,scale(s,c)))),
                    ('first_exterior_source',sub(add(q,scale(s+1,c)),a))]
    return q,margins


def tenth_lift(s,n,y):
    q,m=tenth_req(s,n,y)
    pp=[y]+[add(y,sub(sigma,scale(j,c))) for j in range(1,n+1)]
    assert pp[-1]==q
    for j,key in enumerate(WORDS[s,n]):
        target,lower=g86.ninth_req(key,pp[j]); assert target==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_tenth_hit_{j}',sub(target,c) if j<n-1 else sub(c,target)))
    return q,m


def geometry_audit():
    levels={}
    for label,lib,req,lift in (
        ('sixth',g81.ATOMS,g81.atom_req,g81.atom_lift),
        ('seventh',g81.SEVENTH,g81.seventh_req,g81.seventh_lift),
        ('eighth',g86.EIGHTH,g86.eighth_req,g86.eighth_lift),
        ('ninth',g86.NINTH,g86.ninth_req,g86.ninth_lift)):
        cells={}
        for key in lib:
            _,rr=req(key,seed); _,m=lift(key,seed)
            cond=RANGE+tuple(v for _,v in rr)
            item=audit(m,vertices(cond))
            if (label=='eighth' and key in ('A1','B')) or (label=='ninth' and key in ('Q','S')):
                item['a_equals_sigma8_endpoint']=audit(m,vertices(cond+(sub(a,sigma),)))
            cells[key]=item
        levels[label]=cells
    cells={}
    for (s,n),word in WORDS.items():
        _,rr=tenth_req(s,n,seed); _,m=tenth_lift(s,n,seed)
        cond=RANGE+tuple(v for _,v in rr)
        item=audit(m,vertices(cond))
        if s==0:
            item['a_equals_c10_overlap_entry']=audit(m,vertices(cond+(sub(c,a),)))
        if s==n-1:
            item['a_equals_sigma8_endpoint']=audit(m,vertices(cond+(sub(a,sigma),)))
        if (s,n) in ((0,10),(1,11)):
            item['a_equals_GERM87_endpoint']=audit(m,vertices(cond+(sub(a,a87),sub(a87,a))))
        # Integer-c junction faces are not silently dropped.
        junctions={}
        # At a=j*c and 0<q<c the unique generic visit count is s=j-1.
        if 1 <= s <= 9:
            j=s+1
            face=vertices(cond+(sub(a,scale(j,c)),sub(scale(j,c),a)))
            junctions[str(j)]=audit(m,face)
        item['nonempty_integer_c10_faces']=junctions
        if (s,n)!=(0,11):
            item['strictly_new_parameter_strip']=audit(m,vertices(cond+(sub(a,a87),)))
        else:
            q=add(seed,sub(sigma,scale(11,c)))
            assert sub(add(q,c),a87)==sub(seed,c)
            item['strictly_new_parameter_strip']='EMPTY: a>=c+omega10 and q<omega10 contradict a<q+c'
        cells[f'{s}/{n}']=item
    assert add(ell,omt)==c
    assert add(scale(10,ell),scale(11,omt))==sigma
    # At t=2psi7+d, a=sigma8+d, the three-step eighth branch changes.
    excess=sub(a,sigma); psi=g86.psi; chi=g86.chi; nu=sub(chi,scale(2,psi))
    pp=[seed]+[add(seed,sub(chi,scale(j,psi))) for j in range(1,4)]
    margins=[]
    for j,key in enumerate(NEXT):
        target,lower=g81.seventh_req(key,pp[j]); assert target==pp[j+1]
        margins += [(f'next{j}:{name}',v) for name,v in lower]
        margins.append((f'next_first_return_{j}',sub(target,psi) if j<2 else sub(psi,target)))
    cond=RANGE+(excess,sub(nu,excess),sub(seed,sigma),sub(add(sigma,excess),seed))
    assert pp[-1]==sub(seed,sigma)
    guard=audit(margins,vertices(cond))
    return {'parameter':'a=e-e85; t=e-e80',
            'direct_exclusion_range':'c10<a<=sigma8',
            'new_range':'c10+omega10<a<=sigma8; overlaps GERM87 below its endpoint',
            'rechecked_lower_contracts':levels,'twenty_one_tenth_cells':cells,
            'tenth_map':'y -> y+omega10 mod c10','images':'(omega10,c10) and (0,omega10)',
            'endpoint_words':['S^9 Q','S^10 Q, GERM-86-local'],
            'eleventh_induction_used':False,
            'next_domain':'a=sigma8+d; 0<d<nu8; sigma8<z<sigma8+d',
            'next_eighth_seventh_word':NEXT,'next_guard':guard,'sampled_topology':False}


def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-88','standing':'UNRATIFIED',
         'entry_commit':'37d28daff273ff5bccfc96e225b759408682c5e7',
         'direct_dependency_sha256':PINS,
         'new_exclusion_scope':'L87<L<=L85+sigma8; direct proof also covers L86<L<=L85+sigma8',
         'matrix_namespace':'P/Q/R/S are GERM-86-local; next U/V are GERM-81-local seventh matrices',
         'arithmetic':arithmetic(),'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
         'full_lower_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
         'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
