#!/usr/bin/env python3
"""GERM-83: post-psi7 eighth transfer using the unchanged GERM-82 chart.

Three new eighth maps on psi7<t<=chi7-psi7; five complete ninth words
certify psi7<t<=2psi7-2sigma8. Literal source-domain compositions are
checked at every intermediate point. No deeper section is introduced.
Run without -O. All proof inequalities are exact or outward rational.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of the certificate; run without -O.'
ROOT = Path(__file__).resolve().parents[1]
PIN_PATH = 'tools/sz_post_sigma8_ninth_map_audit.py'
PIN_SHA = 'd1aef82e5dfc3673867f327b7fbcaff788f6c93f6cdbf099f38d10c8dc35e164'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest() == PIN_SHA
import sz_post_sigma8_ninth_map_audit as parent
g81, g77, g75, old = parent.parent, parent.g77, parent.g75, parent.old
product, det = parent.product, parent.det
# Inherited precision is freshly recomputed: grid 10^120, 400 log terms.
EIGHTH = {'A':['V1','U0'], 'D':['V1','U0','U0'], 'E':['V1','U0','U1']}
PAIRS = ((0,3),(1,3),(0,4),(1,4),(2,4))
NINTH = {f'{s}/{n}':['A']+['D']*(n-s-1)+['E']*s for s,n in PAIRS}
CHART = parent.CHART  # Same rational chart, not a new optimized choice.
FACTOR = F(13)
GUARD = ['A','E','E']
assert EIGHTH['A'] == g81.EIGHTH['A1']
assert EIGHTH['D'] == g81.EIGHTH['B1']
assert EIGHTH['E'] == parent.GUARD


def arithmetic():
    add,sub,mul = old.add,old.sub,old.mul
    h=(-4,4,-1); k=(4,-1,-1)
    kap=sub(k,mul(5,h)); tau=sub(h,mul(5,kap)); theta=sub(kap,mul(8,tau))
    alpha=sub(tau,mul(3,theta)); beta=sub(theta,alpha); gamma=sub(alpha,beta)
    xi=sub(mul(5,gamma),beta); omega=sub(gamma,mul(19,xi))
    eta=sub(xi,omega); chi=sub(mul(2,omega),xi); psi=sub(eta,chi)
    sigma=sub(mul(3,psi),chi); rho=sub(psi,mul(3,sigma)); c=sub(sigma,rho)
    nu=sub(psi,sigma); increment=sub(psi,mul(2,sigma))
    L80=(193384,-169969,32737); L82=add(L80,psi)
    L83=add(L82,increment); top=add((4,-1,0),mul(3,h))
    assert L82==(-2202828,1936158,-372926)
    assert L83==(12945856,-11378629,2191647)
    assert L83==add((4,-1,0),add(mul(-2714055,h),mul(522408,k)))
    assert increment==(15148684,-13314787,2564573)
    assert increment==add(sigma,rho)
    assert sub(sub(chi,psi),mul(2,nu))==sigma
    assert sub(nu,increment)==sigma
    assert add(mul(3,c),mul(4,rho))==psi
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(v):return sum((n*l for n,l in zip(v,logs)),old.box(0))
    checks={'sigma_positive':sigma,'3sigma_lt_psi':rho,'psi_lt_4sigma':c,
            'increment_positive':increment,'new_endpoint_below_eighth_formula_bound':sigma,
            'eighth_formula_bound_below_seventh_bound':psi,
            'endpoint_below_three_layers':sub(top,L83)}
    boxes={key:enc(v) for key,v in checks.items()}
    assert all(v.lo>0 for v in boxes.values())
    return {'rational_log_order_checks':{k:g77.show_box(v,34) for k,v in boxes.items()},
            'endpoint_prime_log_vector':L83,'endpoint_h_k_vector':[-2714055,522408],
            'increment_prime_log_vector':increment,'increment':'psi7-2sigma8=sigma8+rho9',
            'endpoint_decimal':g77.show_box(enc(L83),32),
            'increment_decimal':g77.show_box(enc(increment),36),
            'remaining_three_layer_width':g77.show_box(enc(sub(top,L83)),36),
            'ninth_tower_identity':'3c10+4rho9=psi7'}


def rational_audit():
    original,pivots=g75.parent.parent.parent.parent.recalculate_returns()
    legacy=g75.parent.parent.parent
    first={k:product(w,original) for k,w in legacy.FIRST.items()}
    second={k:product(w,first) for k,w in legacy.SECOND.items()}
    boxes=json.loads((ROOT/'notes/_recurrence71_audit.json').read_text())['audit']['rational_audit']['second_section_maps']
    for key,B in second.items():
        for i in range(2):
            for j in range(2):
                lo,hi=map(F,boxes[key][i][j]);assert lo<=B[i][j].lo<=B[i][j].hi<=hi
    third={k:product(w,second) for k,w in g75.THIRD.items()}
    fourth={k:product(w,third) for k,w in g75.FOURTH.items()}
    fifth={k:product(w,fourth) for k,w in g75.FIFTH.items()}
    atoms={k:product(g75.sixth_word(s,n),fifth) for k,(s,n) in g81.ATOMS.items()}
    c6={}
    for key,(s,n) in g81.ATOMS.items():
        ow=g75.to_original(g75.sixth_word(s,n))
        assert legacy.determinant_exponent(ow)==0
        assert len(ow)==1654*n-297;c6[key]=len(ow)
    seven={k:product(w,atoms) for k,w in g81.SEVENTH.items()}
    eight={k:product(w,seven) for k,w in EIGHTH.items()}
    c7={k:sum(c6[x] for x in w) for k,w in g81.SEVENTH.items()}
    c8={k:sum(c7[x] for x in w) for k,w in EIGHTH.items()}
    assert c8=={'A':257302,'D':353997,'E':353997}
    for lib in (atoms,seven,eight):
        for B in lib.values():
            dd=det(B);assert dd.lo>0 and dd.lo<=1<=dd.hi
    cert={}
    for key,w in NINTH.items():
        s,n=map(int,key.split('/')); B=product(w,eight)
        item=g77.cone_test(B,CHART,(-1)**s,FACTOR)
        count=sum(c8[x] for x in w);assert count==257302+(n-1)*353997
        w7=g81.expand(w,EIGHTH);direct=product(w7,seven)
        for i in range(2):
            for j in range(2):
                # A regression only. Identity follows from literal substitution.
                assert max(B[i][j].lo,direct[i][j].lo)<=min(B[i][j].hi,direct[i][j].hi)
        tr=B[0][0]+B[1][1];disc=tr*tr-4*det(B);assert disc.lo>0
        item.update({'eighth_word':w,'seventh_word':w7,'original_step_count':count,
                     'determinant_rho_exponent':0,'trace':old.display_matrix([[tr]])})
        cert[key]=item
    # Boundary words with no E recover the GERM-82 upper endpoint literally.
    for n in (3,4):
        assert g81.expand(NINTH[f'0/{n}'],EIGHTH)==g81.expand(parent.NINTH[f'{n-1}/{n}'],g81.EIGHTH)
    B=product(GUARD,eight);tr=B[0][0]+B[1][1];dd=det(B);disc=tr*tr-4*dd
    assert dd.lo>0 and dd.lo<=1<=dd.hi
    assert F(34,100)<tr.lo<tr.hi<F(35,100) and disc.hi<0
    return {'physical_recalculation':'FRESH PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
            'precision':{'grid':'10^120','log_series_terms':400},'layer_pivots':pivots,
            'GERM71_box_regression':'CONTAINED; not rounded numerical inputs',
            'eighth_maps':{k:old.display_matrix(B) for k,B in eight.items()},
            'chart':[['1','-1'],['-12/5','21/10']], 'same_chart_as_GERM82':True,
            'common_forward_backward_factor':'13','five_ninth_returns':cert,
            'entry_word_regression':'A D^(n-1) equals GERM-82 B1^(n-1) A1 by literal substitution',
            'tenth_induction_used':False,'new_retained_coordinates':0,
            'next_eighth_word':GUARD,'next_trace':old.display_matrix([[tr]]),
            'next_determinant':old.display_matrix([[dd]]),'next_discriminant':old.display_matrix([[disc]]),
            'next_status':'ELLIPTIC COMPLETE NINTH RETURN; NO EXCLUSION ABOVE NEW ENDPOINT'}


# Exact affine coordinates inherited from GERM-75, gamma=1.
af,add,sub,val,vertices=parent.af,parent.add,parent.sub,parent.val,parent.vertices
scale,audit=parent.scale,parent.audit
seed,t,psi,sigma,chi=parent.seed,parent.t,parent.psi,parent.sigma,parent.chi
rho,c,RANGE=parent.rho,parent.c,parent.RANGE
nu=sub(psi,sigma);a=sub(t,psi);amax=sub(psi,scale(2,sigma))


def eighth_req(key,z):
    n=2 if key=='A' else 3
    q=add(z,sub(chi,scale(n,psi)))
    m=[('z>0',z),('z<psi',sub(psi,z)),('q>0',q),('q<psi',sub(psi,q)),
       ('lower_global_scope',sub(t,psi)),('upper_global_scope',sub(sub(chi,psi),t)),
       ('eighth_cut',sub(sigma,z) if n==2 else sub(z,sigma))]
    if key=='D':m.append(('last_source_exterior',sub(add(z,nu),t)))
    if key=='E':m.append(('last_source_interior',sub(t,add(z,nu))))
    return q,m


def eighth_lift(key,z):
    q,m=eighth_req(key,z);word=EIGHTH[key];n=len(word)
    pp=[z]+[add(z,sub(chi,scale(j,psi))) for j in range(1,n+1)]
    assert pp[-1]==q
    for j,k in enumerate(word):
        out,lower=g81.seventh_req(k,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_eighth_hit{j}',sub(out,psi) if j<n-1 else sub(psi,out)))
    return q,m


def ninth_req(s,n,y):
    q=add(y,sub(psi,scale(n,sigma)))
    m=[('y>0',y),('y<sigma',sub(sigma,y)),('q>0',q),('q<sigma',sub(sigma,q)),
       ('lower_global_scope',a),('upper_formula_global_scope',sub(nu,a)),
       ('ninth_cut',sub(c,y) if n==3 else sub(y,c))]
    if s==0:m.append(('no_E_source',sub(q,a)))
    else:m += [('last_E_source',sub(a,add(q,scale(s-1,sigma)))),
               ('first_D_source',sub(add(q,scale(s,sigma)),a))]
    return q,m


def ninth_lift(s,n,y):
    q,m=ninth_req(s,n,y);w=['A']+['D']*(n-s-1)+['E']*s
    pp=[y]+[add(y,sub(psi,scale(j,sigma))) for j in range(1,n+1)]
    assert pp[-1]==q
    for j,k in enumerate(w):
        out,lower=eighth_req(k,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_ninth_hit{j}',sub(out,sigma) if j<n-1 else sub(sigma,out)))
    return q,m


def geometry_audit():
    lower_levels={}
    for label,lib,req,lift in (
        ('sixth',g81.ATOMS,g81.atom_req,g81.atom_lift),
        ('seventh',g81.SEVENTH,g81.seventh_req,g81.seventh_lift)):
        cells={}
        for key in lib:
            _,rr=req(key,seed);_,m=lift(key,seed)
            cells[key]=audit(m,vertices(RANGE+tuple(v for _,v in rr)))
        lower_levels[label]=cells
    cells8={}
    for key in EIGHTH:
        _,rr=eighth_req(key,seed);_,m=eighth_lift(key,seed)
        cond=RANGE+tuple(v for _,v in rr);item=audit(m,vertices(cond))
        if key in ('A','D'):
            item['t_equals_psi_entry_face']=audit(m,vertices(cond+(sub(psi,t),)))
        if key in ('A','E'):
            item['t_equals_chi_minus_psi_formula_face']=audit(m,vertices(cond+(sub(t,sub(chi,psi)),)))
        cells8[key]=item
    cells9={}
    for s,n in PAIRS:
        _,rr=ninth_req(s,n,seed);_,m=ninth_lift(s,n,seed)
        cond=RANGE+tuple(v for _,v in rr)+(sub(amax,a),)
        item=audit(m,vertices(cond))
        if s==0:item['a_equals_zero_entry_face']=audit(m,vertices(cond+(sub(af(),a),)))
        if s==1:item['a_equals_sigma_junction']=audit(m,vertices(cond+(sub(a,sigma),sub(sigma,a))))
        if (s,n) in ((1,3),(2,4)):
            item['a_equals_amax_endpoint']=audit(m,vertices(cond+(sub(a,amax),)))
        cells9[f'{s}/{n}']=item
    assert add(c,rho)==sigma and add(scale(3,c),scale(4,rho))==psi
    assert amax==add(sigma,rho) and sub(nu,amax)==sigma
    # First new three-step ninth word A,E,E: 0<y<b<c, a=amax+b.
    b=sub(a,amax);q,m=ninth_lift(2,3,seed)
    cond=RANGE+(b,sub(c,b),seed,sub(b,seed))
    assert q==add(seed,rho)
    guard=audit(m,vertices(cond))
    return {'normalization':'GERM-75 exact affine coordinates and inherited rational beta/gamma box',
            'parameter':'t=e-e80; a=t-psi7=e-e82',
            'rechecked_lower_contracts':lower_levels,'three_eighth_cells':cells8,
            'eighth_formula_scope':'psi7<t<=chi7-psi7, equivalently 0<a<=nu8',
            'five_ninth_cells':cells9,'new_exclusion_scope':'psi7<t<=2psi7-2sigma8',
            'ninth_map':'y -> y+rho9 mod sigma8','ninth_images':'(rho9,sigma8) and (0,rho9)',
            'physical_field':'W(t0+y); t0=h-beta+gamma-xi+2eta7',
            'upper_endpoint_words':['A D E','A D E E'],'tenth_induction_used':False,
            'next_domain':'a=amax+b; 0<y<b<c10','next_eighth_word':GUARD,
            'next_guard':guard,'sampled_topology':False}


def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-83','standing':'UNRATIFIED',
         'entry_commit':'d0d9a9258a5c33defcce9d3430ab4b628ebbfe99',
         'new_exclusion_scope':'psi7<t<=2psi7-2sigma8, t=e-e80; L82<L<=L82+psi7-2sigma8',
         'experimental_endpoint':'log(2^12945856*5^2191647/3^11378629)',
         'inherited_three_layer_formula_scope':'2h<e<=3h',
         'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
         'matrix_namespace':'U_i,V_i are GERM-81-local; A,D,E and ninth words are GERM-83-local',
         'eighth_word_dictionary':EIGHTH,'ninth_word_dictionary':NINTH,
         'arithmetic':arithmetic(),'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
         'full_lower_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
         'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
