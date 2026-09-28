#!/usr/bin/env python3
"""GERM-86: post-(chi7-psi7) eighth transfer through excess a=c10.

Three eighth and four ninth formulas hold on 0<a<=sigma8. Four new tenth
maps on 0<a<=c10 yield eleven complete eleventh words in one signed chart.
Every intermediate lower domain is checked. All proof signs are exact or
outward rational. Run without -O. This is unratified source-equation work.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of this certificate; run without -O.'
ROOT=Path(__file__).resolve().parents[1]
PIN_PATH='tools/sz_post_psi7_tenth_all_internal_audit.py'
PIN_SHA='d1eaaed262ca98036d43743b52c927f04385a541d91dcb1aa073951a7a9c204c'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest()==PIN_SHA
import sz_post_psi7_tenth_all_internal_audit as parent
g84,g83,g81,g77,g75,old=parent.parent,parent.g83,parent.g81,parent.g77,parent.g75,parent.old
product,det=parent.product,parent.det
# The pinned stack recomputes at grid 10^120 with 400 logarithm terms.
# All eighth/ninth/tenth matrix labels in this file are GERM-86-local.
EIGHTH={'A0':['V1','U0'], 'A1':['V1','U1'], 'B':['V1','U0','U1']}
NINTH={'P':['A0','B','B'], 'Q':['A1','B','B'],
       'R':['A0','B','B','B'], 'S':['A1','B','B','B']}
TENTH={'V0':['P']+['R']*9, 'V1':['Q']+['R']*9,
       'U0':['P']+['R']*10, 'U1':['Q']+['R']*10}
LOW={(i,n):['V1' if i else 'V0']+['U0']*(n-1) for n in (4,5) for i in (0,1)}
HIGH={(s,n):['V1']+['U0']*(n-s-1)+['U1']*s for n in (4,5) for s in range(n)}
WORDS={f'out/{n}':LOW[0,n] for n in (4,5)}
WORDS.update({f'{s}/{n}':w for (s,n),w in HIGH.items()})
assert len(WORDS)==11
assert {tuple(w) for w in WORDS.values()}=={tuple(w) for w in list(LOW.values())+list(HIGH.values())}
CHART=[[1,1],[F(-11,5),F(-8,5)]]
FACTOR=F(5,2)
GUARD=['Q']+['R']*9+['S']


def arithmetic():
    add,sub,mul=old.add,old.sub,old.mul
    h=(-4,4,-1);k=(4,-1,-1)
    kap=sub(k,mul(5,h));tau=sub(h,mul(5,kap));theta=sub(kap,mul(8,tau))
    alpha=sub(tau,mul(3,theta));beta=sub(theta,alpha);gamma=sub(alpha,beta)
    xi=sub(mul(5,gamma),beta);omega=sub(gamma,mul(19,xi))
    eta=sub(xi,omega);chi=sub(mul(2,omega),xi);psi=sub(eta,chi)
    sigma=sub(mul(3,psi),chi);rho=sub(psi,mul(3,sigma));c=sub(sigma,rho)
    omt=sub(sigma,mul(10,c));ell=sub(c,omt);om11=sub(c,mul(4,ell));cut11=sub(ell,om11)
    L80=(193384,-169969,32737);L85=add(L80,sub(chi,psi));L86=add(L85,c)
    assert L85==(4173408,-3668172,706529)
    assert c==(-32693580,28735701,-5534809)
    assert L86==(-28520172,25067529,-4828280)
    assert L86==add((4,-1,0),add(mul(5979162,h),mul(-1150882,k)))
    formula_end=add(L80,mul(2,psi));top=add((4,-1,0),mul(3,h))
    assert sub(formula_end,L86)==rho
    assert add(mul(3,c),mul(4,rho))==psi
    assert add(mul(10,ell),mul(11,omt))==sigma
    assert add(mul(4,cut11),mul(5,om11))==c
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(v):return sum((n*l for n,l in zip(v,logs)),old.box(0))
    checks={'sigma_positive':sigma,'rho_positive':rho,'c10_positive':c,
            '10c10_lt_sigma8':omt,'sigma8_lt_11c10':ell,
            '4c11_lt_c10':om11,'c10_lt_5c11':cut11,
            'eighth_upper_bound_inside_seventh':sub(chi,mul(2,psi)),
            'next_guard_below_ninth_upper_bound':sub(sigma,mul(2,c)),
            'new_endpoint_below_eighth_formula_endpoint':rho,
            'endpoint_below_three_layers':sub(top,L86)}
    boxes={key:enc(v) for key,v in checks.items()}
    assert all(x.lo>0 for x in boxes.values())
    return {'rational_log_order_checks':{key:g77.show_box(x,38) for key,x in boxes.items()},
            'endpoint_prime_log_vector':L86,'endpoint_h_k_vector':[5979162,-1150882],
            'endpoint_decimal':g77.show_box(enc(L86),34),
            'increment_prime_log_vector':c,'increment_decimal':g77.show_box(enc(c),38),
            'remaining_new_eighth_formula_width':g77.show_box(enc(rho),38),
            'remaining_three_layer_width':g77.show_box(enc(sub(top,L86)),38),
            'tower_identities':'3c10+4rho9=psi7; 10c11+11omega10=sigma8; 4(c11-omega11)+5omega11=c10'}


def rational_audit():
    original,pivots=g75.parent.parent.parent.parent.recalculate_returns()
    legacy=g75.parent.parent.parent
    first={k:product(w,original) for k,w in legacy.FIRST.items()}
    second={k:product(w,first) for k,w in legacy.SECOND.items()}
    fixture=json.loads((ROOT/'notes/_recurrence71_audit.json').read_text())
    boxes=fixture['audit']['rational_audit']['second_section_maps']
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
    nine={k:product(w,eight) for k,w in NINTH.items()}
    ten={k:product(w,nine) for k,w in TENTH.items()}
    c7={k:sum(c6[x] for x in w) for k,w in g81.SEVENTH.items()}
    c8={k:sum(c7[x] for x in w) for k,w in EIGHTH.items()}
    c9={k:sum(c8[x] for x in w) for k,w in NINTH.items()}
    c10={k:sum(c9[x] for x in w) for k,w in TENTH.items()}
    assert c8=={'A0':257302,'A1':257302,'B':353997}
    assert c9=={'P':965296,'Q':965296,'R':1319293,'S':1319293}
    assert c10=={'V0':12838933,'V1':12838933,'U0':14158226,'U1':14158226}
    for lib in (atoms,seven,eight,nine,ten):
        for B in lib.values():
            dd=det(B);assert dd.lo>0 and dd.lo<=1<=dd.hi
    # Exact source-word regressions at a=0; no continuity inference.
    assert EIGHTH['A1']==parent.GUARD
    assert EIGHTH['A0']==g83.EIGHTH['A'] and EIGHTH['B']==g83.EIGHTH['E']
    for newkey,oldkey in (('P','Q'),('R','S')):
        assert g81.expand(NINTH[newkey],EIGHTH)==g81.expand(g84.NINTH[oldkey],g83.EIGHTH)
    for newkey,oldkey in (('V0','V1'),('U0','U1')):
        new7=g81.expand(g81.expand(TENTH[newkey],NINTH),EIGHTH)
        old7=g81.expand(g81.expand(parent.TENTH[oldkey],g84.NINTH),g83.EIGHTH)
        assert new7==old7
    classification={}
    for label,lib in (('eighth',eight),('ninth',nine),('tenth',ten)):
        classification[label]={}
        for key,B in lib.items():
            tr=B[0][0]+B[1][1];disc=tr*tr-4*det(B)
            elliptic=(label=='eighth' and key=='A0') or (label=='ninth' and key in ('P','R')) or (label=='tenth' and key in ('V0','U0'))
            assert disc.hi<0 if elliptic else disc.lo>0
            classification[label][key]={'matrix':old.display_matrix(B),'trace':old.display_matrix([[tr]]),
                'discriminant':old.display_matrix([[disc]]),'type':'ELLIPTIC' if elliptic else 'HYPERBOLIC'}
    cert={}
    for key,w in WORDS.items():
        n=len(w);sign=(-1)**(n+1) if key.startswith('out') else (-1)**n
        B=product(w,ten);item=g77.cone_test(B,CHART,sign,FACTOR)
        count=sum(c10[x] for x in w);assert count==12838933+(n-1)*14158226
        expanded=g81.expand(w,TENTH);direct=product(expanded,nine)
        for i in range(2):
            for j in range(2):
                # Numerical regression only; equality is licensed by literal substitution.
                assert max(B[i][j].lo,direct[i][j].lo)<=min(B[i][j].hi,direct[i][j].hi)
        item.update({'tenth_word':w,'ninth_word':expanded,'original_step_count':count,
                     'determinant_rho_exponent':0})
        cert[key]=item
    B=product(GUARD,nine);tr=B[0][0]+B[1][1];dd=det(B);disc=tr*tr-4*dd
    assert dd.lo>0 and dd.lo<=1<=dd.hi
    assert F(7901)<tr.lo<tr.hi<F(7903) and disc.lo>0
    return {'physical_recalculation':'FRESH PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
            'precision':{'grid':'10^120','log_series_terms':400},'layer_pivots':pivots,
            'GERM71_box_regression':'CONTAINED; not rounded numerical inputs',
            'map_classification':classification,'chart':[['1','1'],['-11/5','-8/5']],
            'common_forward_backward_factor':'5/2','eleven_complete_returns':cert,
            'distinct_temporal_words':11,'low_domain_cells':4,'high_domain_cells':9,
            'entry_regression':'new P/R=GERM84 Q/S; new V0/U0=GERM85 V1/U1 by literal substitution',
            'next_ninth_word':GUARD,'next_matrix':'S R^9 Q, GERM-86-local',
            'next_trace':old.display_matrix([[tr]]),'next_determinant':old.display_matrix([[dd]]),
            'next_discriminant':old.display_matrix([[disc]])}


# Exact affine coordinates inherited from GERM-75; gamma=1.
af,add,sub,val,vertices=parent.af,parent.add,parent.sub,parent.val,parent.vertices
scale,audit=parent.scale,parent.audit
seed,t,chi,psi,sigma=g83.seed,g83.t,g83.chi,g83.psi,g83.sigma
rho,c,ell=g83.rho,g83.c,parent.ell
omt=sub(sigma,scale(10,c));om11=sub(c,scale(4,ell));cut11=sub(ell,om11)
a=sub(t,sub(chi,psi));RANGE=parent.RANGE;zero=af()


def eighth_req(key,z):
    n=3 if key=='B' else 2;q=add(z,sub(chi,scale(n,psi)))
    m=[('z>0',z),('z<psi',sub(psi,z)),('q>0',q),('q<psi',sub(psi,q)),
       ('lower_global_scope',a),('upper_global_scope',sub(sigma,a)),
       ('eighth_cut',sub(z,sigma) if n==3 else sub(sigma,z))]
    if n==2:m.append(('two_step_bit',sub(a,z) if key=='A1' else sub(z,a)))
    return q,m


def eighth_lift(key,z):
    q,m=eighth_req(key,z);w=EIGHTH[key];n=len(w)
    pp=[z]+[add(z,sub(chi,scale(j,psi))) for j in range(1,n+1)]
    assert pp[-1]==q
    for j,k in enumerate(w):
        out,lower=g81.seventh_req(k,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_eighth_hit{j}',sub(out,psi) if j<n-1 else sub(psi,out)))
    return q,m


def ninth_req(key,y):
    n=3 if key in ('P','Q') else 4;inside=key in ('Q','S')
    q=add(y,sub(psi,scale(n,sigma)))
    return q,[('y>0',y),('y<sigma',sub(sigma,y)),('q>0',q),('q<sigma',sub(sigma,q)),
              ('lower_global_scope',a),('upper_global_scope',sub(sigma,a)),
              ('ninth_cut',sub(c,y) if n==3 else sub(y,c)),
              ('ninth_source_bit',sub(a,y) if inside else sub(y,a))]


def ninth_lift(key,y):
    q,m=ninth_req(key,y);w=NINTH[key];n=len(w)
    pp=[y]+[add(y,sub(psi,scale(j,sigma))) for j in range(1,n+1)]
    assert pp[-1]==q
    for j,k in enumerate(w):
        out,lower=eighth_req(k,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_ninth_hit{j}',sub(out,sigma) if j<n-1 else sub(sigma,out)))
    return q,m


def tenth_word_lift(w,y):
    n=len(w);pp=[y]+[add(y,sub(sigma,scale(j,c))) for j in range(1,n+1)]
    q=pp[-1];m=[('y>0',y),('y<c10',sub(c,y)),('q>0',q),('q<c10',sub(c,q))]
    for j,k in enumerate(w):
        out,lower=ninth_req(k,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_tenth_hit{j}',sub(out,c) if j<n-1 else sub(c,out)))
    return q,m


def tenth_req(key,y):
    n=10 if key[0]=='V' else 11;inside=key[-1]=='1';q=add(y,sub(sigma,scale(n,c)))
    return q,[('y>0',y),('y<c10',sub(c,y)),('q>0',q),('q<c10',sub(c,q)),
              ('lower_global_scope',a),('upper_global_scope',sub(c,a)),
              ('tenth_cut',sub(ell,y) if n==10 else sub(y,ell)),
              ('tenth_source_bit',sub(a,y) if inside else sub(y,a))]


def tenth_lift(key,y):
    q,m=tenth_req(key,y);out,lower=tenth_word_lift(TENTH[key],y);assert out==q
    return q,m+[(f'ninth:{name}',v) for name,v in lower]


def eleventh_lift(w,y):
    n=len(w);pp=[y]+[add(y,sub(c,scale(j,ell))) for j in range(1,n+1)]
    q=pp[-1];m=[('y>0',y),('y<c11',sub(ell,y)),('q>0',q),('q<c11',sub(ell,q))]
    for j,k in enumerate(w):
        out,lower=tenth_req(k,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_eleventh_hit{j}',sub(out,ell) if j<n-1 else sub(ell,out)))
    return q,m


def geometry_audit():
    levels={}
    for label,lib,req,lift in (
        ('sixth',g81.ATOMS,g81.atom_req,g81.atom_lift),
        ('seventh',g81.SEVENTH,g81.seventh_req,g81.seventh_lift),
        ('eighth',EIGHTH,eighth_req,eighth_lift),
        ('ninth',NINTH,ninth_req,ninth_lift),
        ('tenth',TENTH,tenth_req,tenth_lift)):
        cells={}
        for key in lib:
            _,rr=req(key,seed);_,m=lift(key,seed)
            cond=RANGE+tuple(v for _,v in rr);item=audit(m,vertices(cond))
            if ((label=='eighth' and key in ('A1','B')) or (label=='ninth' and key in ('Q','S'))):
                item['a_equals_sigma_formula_endpoint']=audit(m,vertices(cond+(sub(a,sigma),sub(sigma,a))))
            if label=='tenth' and key in ('V1','U1'):
                item['a_equals_c10_endpoint']=audit(m,vertices(cond+(sub(a,c),sub(c,a))))
            if ((label=='eighth' and key in ('A0','B')) or
                (label=='ninth' and key in ('P','R')) or (label=='tenth' and key in ('V0','U0'))):
                item['a_equals_zero_entry']=audit(m,vertices(cond+(sub(zero,a),)))
            cells[key]=item
        levels[label]=cells
    low={};high={}
    for (i,n),w in LOW.items():
        q,m=eleventh_lift(w,seed)
        cond=RANGE+(a,sub(ell,a),seed,sub(ell,seed),q,sub(ell,q),sub(a,seed) if i else sub(seed,a))
        item=audit(m,vertices(cond))
        if i:item['a_equals_c11_junction']=audit(m,vertices(cond+(sub(a,ell),)))
        else:item['a_equals_zero_entry']=audit(m,vertices(cond+(sub(zero,a),)))
        low[f'{i}/{n}']=item
    for (s,n),w in HIGH.items():
        q,m=eleventh_lift(w,seed)
        cond=RANGE+(sub(a,ell),sub(c,a),seed,sub(ell,seed),q,sub(ell,q))
        cond += (sub(add(q,ell),a),) if s==0 else (sub(a,add(q,scale(s,ell))),sub(add(q,scale(s+1,ell)),a))
        item=audit(m,vertices(cond))
        if s==0:item['a_equals_c11_junction']=audit(m,vertices(cond+(sub(ell,a),)))
        if s==n-1:item['a_equals_c10_endpoint']=audit(m,vertices(cond+(sub(a,c),)))
        high[f'{s}/{n}']=item
    assert sub(add(chi,scale(-1,psi)),add(psi,scale(-1,sigma)))==psi
    assert add(sub(c,omt),omt)==c and ell==sub(c,omt)
    assert sub(c,scale(4,ell))==om11 and sub(c,scale(5,ell))==scale(-1,cut11)
    assert add(scale(4,cut11),scale(5,om11))==c
    # Beyond a=c10, the last ninth source on an eleven-step tenth return
    # enters the active interval. Ninth formulas still apply on this strip.
    excess=sub(a,c);q,m=tenth_word_lift(GUARD,seed)
    cond=RANGE+(excess,sub(omt,excess),sub(seed,ell),sub(add(ell,excess),seed))
    assert q==sub(seed,ell)
    guard=audit(m,vertices(cond))
    return {'parameter':'a=t-(chi7-psi7)=e-e85; t=e-e80',
            'rechecked_level_contracts':levels,
            'formula_scopes':{'eighth':'0<a<=sigma8','ninth':'0<a<=sigma8','tenth':'0<a<=c10'},
            'new_exclusion_scope':'0<a<=c10','physical_field':'W(t0+y); t0=h-beta+gamma-xi+2eta7',
            'eleventh_section':'0<y<c11; c11=c10-omega10',
            'eleventh_map':'y -> y+omega11 mod c11',
            'eleventh_images':'(omega11,c11) and (0,omega11)',
            'low_cells':low,'high_cells':high,'upper_endpoint_words':['U1^3 V1','U1^4 V1, all GERM-86-local'],
            'next_domain':'a=c10+eps; 0<eps<omega10; c11<y<c11+eps',
            'next_ninth_word':GUARD,'next_guard':guard,'sampled_topology':False}


def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-86','standing':'UNRATIFIED',
         'entry_commit':'6fc35f3e58f9299ea09fa645713fc2e467cb2630',
         'new_exclusion_scope':'0<a<=c10, a=e-e85; L85<L<=L85+c10',
         'inherited_three_layer_formula_scope':'2h<e<=3h',
         'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
         'matrix_namespace':'seventh U/V are GERM-81-local; eighth A0/A1/B, ninth P/Q/R/S and tenth U/V are GERM-86-local',
         'eighth_word_dictionary':EIGHTH,'ninth_word_dictionary':NINTH,'tenth_word_dictionary':TENTH,
         'low_eleventh_words':{f'{i}/{n}':w for (i,n),w in LOW.items()},
         'high_eleventh_words':{f'{s}/{n}':w for (s,n),w in HIGH.items()},
         'arithmetic':arithmetic(),'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
         'full_lower_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
         'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
