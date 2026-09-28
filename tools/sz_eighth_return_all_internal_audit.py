#!/usr/bin/env python3
"""GERM-79: all-internal eighth visits controlled by five ninth returns.

New exclusion: 2psi7 < delta <= 3psi7-2sigma8, sigma8=3psi7-chi7.
Three eighth-map formulas are proved throughout 2psi7<delta<chi7. Each
higher word checks every intermediate lower domain, not just endpoints.
All proof signs are outward rational; all source tests are affine/exact.
Run without -O. Pinned GERM-78 and transitive helpers require SymPy.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of this certificate; do not use -O.'
ROOT = Path(__file__).resolve().parents[1]
PIN_PATH = 'tools/sz_eighth_return_internal_visit_audit.py'
PIN_SHA = '92e0a7fb61bb0122037d6c0d46239725dc81ad7384aad69a70b611089176d7ae'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest() == PIN_SHA
import sz_eighth_return_internal_visit_audit as parent
g77, g75, old = parent.parent, parent.g75, parent.old
old.SCALE = 10**60
product, det = parent.product, parent.det

# All dictionaries are chronological; matrix products act rightmost first.
EIGHTH = {'A':['V1','U1'], 'D':['V1','U0','U1'], 'E':['V1','U1','U1']}
PAIRS = [(0,3),(1,3),(0,4),(1,4),(2,4)]
def ninth_word(s,n): return ['A']+['D']*(n-s-1)+['E']*s
NINTH = {f'{s}/{n}':ninth_word(s,n) for s,n in PAIRS}
CHART = [[1,4],[-2,F(-23,2)]]
GUARD = ['A','E','E']

def arithmetic():
    h,k = (-4,4,-1),(4,-1,-1)
    mul, sub, add = old.mul, old.sub, old.add
    kap=sub(k,mul(5,h)); tau=sub(h,mul(5,kap)); theta=sub(kap,mul(8,tau))
    alpha=sub(tau,mul(3,theta)); beta=sub(theta,alpha); gamma=sub(alpha,beta)
    xi=sub(mul(5,gamma),beta); omega=sub(gamma,mul(19,xi))
    eta=sub(xi,omega); chi=sub(mul(2,omega),xi); psi=sub(eta,chi)
    sigma=sub(mul(3,psi),chi); rho9=sub(psi,mul(3,sigma))
    amax=sub(psi,mul(2,sigma)); increment=amax
    L78=(-6182852,5434361,-1046718); L79=add(L78,increment)
    assert L79==(8965832,-7880426,1517855)
    end3=add((4,-1,0),mul(3,h))
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(v): return sum((c*l for c,l in zip(v,logs)),old.box(0))
    checks={'sigma_positive':sigma, 'psi_gt_3sigma':rho9,
            'psi_lt_4sigma':sub(mul(4,sigma),psi),
            'positive_new_increment':increment,
            'endpoint_inside_seventh_scope':sub(chi,add(mul(2,psi),amax)),
            'endpoint_below_3h':sub(end3,L79)}
    # Exact integer prime-power comparisons, independent of decimal displays.
    def prime_sign(v):
        pos=neg=1
        for prime,e in zip((2,3,5),v):
            if e>=0: pos*=prime**e
            else: neg*=prime**(-e)
        return (pos>neg)-(pos<neg)
    assert all(prime_sign(v)>0 for v in checks.values())
    assert add(sigma,rho9)==amax
    assert sub(chi,add(mul(2,psi),amax))==sigma
    # Independent h,k endpoint and prime-log identities.
    eh=1296216+502358-2*(3*502358-(-332041))
    ek=-249498-96695-2*(3*(-96695)-63912)
    assert L79==add((4,-1,0),add(mul(eh,h),mul(ek,k)))
    return {'exact_prime_power_checks':{k:'PASS' for k in checks},
        'sigma8_prime_log_vector':sigma,'rho9_prime_log_vector':rho9,
        'new_increment_prime_log_vector':increment,
        'endpoint_prime_log_vector':L79,'endpoint_h_k_vector':[eh,ek],
        'endpoint_decimal':g77.show_box(enc(L79),26),
        'increment_decimal':g77.show_box(enc(increment),30),
        'sigma8_decimal':g77.show_box(enc(sigma),30),
        'rho9_decimal':g77.show_box(enc(rho9),30),
        'remaining_three_layer_width':g77.show_box(enc(sub(end3,L79)),30),
        'unexcluded_seventh_formula_width':'sigma8',
        'order':'L78<L79<log(16/3)+3h; 2psi7<delta79<chi7'}

def rational_audit():
    original,pivots=g75.parent.parent.parent.parent.recalculate_returns()
    legacy=g75.parent.parent.parent
    first={k:product(w,original) for k,w in legacy.FIRST.items()}
    second={k:product(w,first) for k,w in legacy.SECOND.items()}
    fixture=json.loads((ROOT/'notes/_recurrence71_audit.json').read_text())
    boxes=fixture['audit']['rational_audit']['second_section_maps']
    for key,b in second.items():
        for i in range(2):
            for j in range(2):
                lo,hi=map(F,boxes[key][i][j]); assert lo<=b[i][j].lo<=b[i][j].hi<=hi
    third={k:product(w,second) for k,w in g75.THIRD.items()}
    fourth={k:product(w,third) for k,w in g75.FOURTH.items()}
    fifth={k:product(w,fourth) for k,w in g75.FIFTH.items()}
    atoms={k:product(g75.sixth_word(s,n),fifth) for k,(s,n) in g77.ATOMS.items()}
    counts={}
    for key,(s,n) in g77.ATOMS.items():
        ow=g75.to_original(g75.sixth_word(s,n))
        assert legacy.determinant_exponent(ow)==0
        assert len(ow)==1654*n-297; counts[key]=len(ow)
    seventh={k:product(w,atoms) for k,w in g77.SEVENTH.items()}
    c7={k:sum(counts[a] for a in w) for k,w in g77.SEVENTH.items()}
    eighth={k:product(w,seventh) for k,w in EIGHTH.items()}
    c8={k:sum(c7[a] for a in w) for k,w in EIGHTH.items()}
    assert c8=={'A':257302,'D':353997,'E':353997}
    for b in list(seventh.values())+list(eighth.values()):
        dd=det(b); assert dd.lo>0 and dd.lo<=1<=dd.hi
    all_internal=eighth['E']; tr=all_internal[0][0]+all_internal[1][1]
    disc=tr*tr-4*det(all_internal); assert disc.hi<0
    cert={}
    for s,n in PAIRS:
        word=ninth_word(s,n); b=product(word,eighth)
        item=g77.cone_test(b,CHART,(-1)**(n+s),F(20))
        w7=[v for k in word for v in EIGHTH[k]]
        # Literal substitution establishes product identity; enclosure overlap
        # is a regression only, never a proof of word legality or equality.
        direct=product(w7,seventh)
        for i in range(2):
            for j in range(2):
                assert max(b[i][j].lo,direct[i][j].lo)<=min(b[i][j].hi,direct[i][j].hi)
        count=sum(c8[k] for k in word)
        assert count==257302+(n-1)*353997
        item.update({'eighth_word':word,'seventh_word':w7,'original_step_count':count,
                     'determinant_rho_exponent':0})
        cert[f'{s}/{n}']=item
    b=product(GUARD,eighth); tr=b[0][0]+b[1][1]; dd=det(b); disc=tr*tr-4*dd
    assert F(-58,100)<tr.lo<tr.hi<F(-57,100) and dd.lo>0 and disc.hi<0
    return {'physical_recalculation':'FRESH OUTWARD RATIONAL PAIRED-SOURCE SOLVES',
        'grid':'10^60','layer_pivots':pivots,'GERM71_box_regression':'CONTAINED',
        'eighth_maps':{k:old.display_matrix(b) for k,b in eighth.items()},
        'eighth_all_internal_atom':'E=U1^2 V1; discriminant still strictly negative',
        'chart':[['1','4'],['-2','-23/2']], 'common_forward_backward_factor':'20',
        'five_ninth_returns':cert,'above_scope_word':GUARD,
        'above_scope_trace':old.display_matrix([[tr]]),
        'above_scope_determinant':old.display_matrix([[dd]]),
        'above_scope_discriminant':old.display_matrix([[disc]]),
        'above_scope_status':'E^2 A; exact determinant one; genuinely elliptic'}

# Inherited affine variables: gamma=1, (beta/gamma,zeta/gamma,seed/gamma).
af,add,sub,val,vertices=parent.af,parent.add,parent.sub,parent.val,parent.vertices
scale=parent.scale
psi,chi,delta,seed=parent.psi,parent.chi,parent.delta,parent.seed
nu,sigma=parent.nu,parent.sigma
rho9=sub(psi,scale(3,sigma)); cut=sub(sigma,rho9)
a=sub(delta,scale(2,psi)); amax=sub(psi,scale(2,sigma))
RANGE=g77.RANGE+(rho9,sub(sigma,rho9))

def eighth_req(key,z):
    target=add(z,nu) if key=='A' else sub(z,sigma)
    req=[('z>0',z),('z<psi',sub(psi,z)),('target>0',target),('target<psi',sub(psi,target)),
         ('a>0',a),('eighth_global_scope',sub(nu,a))]
    if key=='A': req.append(('two_step_cut',sub(sigma,z)))
    else:
        req += [('three_step_cut',sub(z,sigma)),
                ('internal_visit_cut',sub(add(sigma,a),z) if key=='E' else sub(z,add(sigma,a)))]
    return target,req

def eighth_lift(key,z):
    target,m=eighth_req(key,z); word=EIGHTH[key]
    actual,lower=g77.eighth_lift(word,len(word),z); assert actual==target
    return target,m+[(f'seventh:{name}',x) for name,x in lower]

def ninth_lift(s,n,y):
    points=[y]+[add(y,sub(psi,scale(j,sigma))) for j in range(1,n+1)]
    q=points[-1]; word=ninth_word(s,n)
    margins=[('y>0',y),('y<sigma',sub(sigma,y)),('q>0',q),('q<sigma',sub(sigma,q))]
    for j,key in enumerate(word):
        target,lower=eighth_req(key,points[j]); assert target==points[j+1]
        margins += [(f'{j}:{name}',x) for name,x in lower]
        margins.append((f'no_earlier_ninth_hit{j}',sub(target,sigma) if j<n-1 else sub(sigma,target)))
    return q,margins

def geometry_audit():
    seven={}
    for key in g77.SEVENTH:
        _,req=g77.seventh_req(key,seed); _,m=g77.seventh_lift(key,seed)
        seven[key]=g77.audit(m,vertices(g77.RANGE+tuple(x for _,x in req)))
    eight={}
    for key in EIGHTH:
        _,req=eighth_req(key,seed); _,m=eighth_lift(key,seed)
        eight[key]=g77.audit(m,vertices(RANGE+tuple(x for _,x in req)))
    cells={}
    base=RANGE+(a,sub(amax,a),seed,sub(sigma,seed))
    for s,n in PAIRS:
        q,m=ninth_lift(s,n,seed)
        cond=base+(sub(cut,seed) if n==3 else sub(seed,cut),q,sub(sigma,q))
        cond += (sub(q,a),) if s==0 else (sub(a,add(q,scale(s-1,sigma))),sub(add(q,scale(s,sigma)),a))
        m += [('new_lower_global_scope',a),('new_upper_global_scope',sub(amax,a))]
        item=g77.audit(m,vertices(cond))
        if (s,n) in ((1,3),(2,4)):
            item['a_equals_amax_endpoint']=g77.audit(m,vertices(cond+(sub(a,amax),)))
        if (s,n) in ((1,3),(1,4)):
            item['a_equals_sigma_junction']=g77.audit(m,vertices(cond+(sub(a,sigma),sub(sigma,a))))
        cells[f'{s}/{n}']=item
    assert add(cut,rho9)==sigma
    assert sub(psi,scale(3,sigma))==rho9
    assert sub(psi,scale(4,sigma))==scale(-1,cut)
    # Exact tower measure: 3*cut + 4*rho9 = psi.
    assert add(scale(3,cut),scale(4,rho9))==psi
    # At the first new parameter: n=3, both post-wrap visits are internal.
    extra=sub(a,amax)
    cond=RANGE+(extra,sub(cut,extra),seed,sub(extra,seed))
    q,m=ninth_lift(2,3,seed)
    assert q==add(seed,rho9)
    guard=g77.audit(m,vertices(cond))
    return {'normalization':'gamma=1; inherited beta/gamma box intersected with 3sigma8<psi7<4sigma8',
        'rechecked_four_seventh_contracts':seven,
        'three_eighth_formula_scope':'2psi7<delta<chi7, equivalently 0<a<nu8',
        'three_eighth_contracts':eight,
        'ninth_section':'0<y<sigma8 in eighth coordinate; physical W(t0+y)',
        'physical_origin':'t0=h-beta+gamma-xi+2eta7 (unchanged)',
        'ninth_return_times':'3 for y<sigma8-rho9; 4 for y>sigma8-rho9',
        'ninth_rotation':'y -> y+rho9 mod sigma8',
        'image_tiling':'(rho9,sigma8) and (0,rho9)',
        'tower_total_length':'3(sigma8-rho9)+4rho9=psi7',
        'new_exclusion_scope':'0<a<=psi7-2sigma8; a=delta-2psi7',
        'five_ninth_cells':cells,
        'completeness':'Descending sources: final consecutive E run. n=3 permits s=0,1; n=4 permits s=0,1,2. Endpoint leaves (1,3),(2,4).',
        'above_scope_domain':'a=psi7-2sigma8+b; 0<y<b<sigma8-rho9',
        'above_scope_guard':guard,'sampled_topology':False}

def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-79','standing':'UNRATIFIED',
        'entry_commit':'c0b870e1dc14bd8d8db85d64ff133a2a5ba1c4e5',
        'new_exclusion_scope':'L78<L<=L78+psi7-2sigma8',
        'experimental_endpoint':'log(2^8965832*5^1517855/3^7880426)',
        'inherited_three_layer_formula_scope':'2h<e<=3h',
        'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
        'eighth_word_dictionary':EIGHTH,'ninth_word_dictionary':NINTH,
        'arithmetic':arithmetic(),'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
        'full_parent_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
        'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
