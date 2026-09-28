#!/usr/bin/env python3
"""GERM-84: post-psi7 double visits, through b=rho9.

Inherits GERM-83's A/D/E source equations, not older namesakes. Four
ninth maps on 0<b<=sigma8 yield 21 distinct complete tenth words on
0<b<=rho9. Two fixed-parameter rational charts certify factor 5. Every
intermediate source is checked. Run with assertions enabled, without -O.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of this certificate; run without -O.'
ROOT=Path(__file__).resolve().parents[1]
PIN_PATH='tools/sz_post_psi7_eighth_map_audit.py'
PIN_SHA='77d3aa03a9cd6b92d1203b746aba6c1c55ed02adcfcdffa86d33b54349609708'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest()==PIN_SHA
import sz_post_psi7_eighth_map_audit as parent
g81,g77,g75,old=parent.g81,parent.g77,parent.g75,parent.old
product,det=parent.product,parent.det
# The pinned stack freshly recomputes on grid 10^120 with 400 log terms.
NINTH={'P':['A','D','E'],'Q':['A','E','E'],
       'R':['A','D','E','E'],'S':['A','E','E','E']}
LOW={(i,n):[('Q' if i else 'P')]+['R']*(n-1)
     for n in (10,11) for i in (0,1)}
HIGH={(s,n):['Q']+['R']*(n-s-1)+['S']*s
      for n in (10,11) for s in range(n-1)}
assert len(LOW)==4 and len(HIGH)==19
assert len({tuple(w) for w in list(LOW.values())+list(HIGH.values())})==21
CLO=[[1,1],[F(-97,50),F(-19,10)]]
CHI=[[1,-1],[F(-97,50),F(199,100)]]
FACTOR=F(5)
GUARD=['Q']+['S']*9


def arithmetic():
    add,sub,mul=old.add,old.sub,old.mul
    h=(-4,4,-1);k=(4,-1,-1)
    kap=sub(k,mul(5,h));tau=sub(h,mul(5,kap));theta=sub(kap,mul(8,tau))
    alpha=sub(tau,mul(3,theta));beta=sub(theta,alpha);gamma=sub(alpha,beta)
    xi=sub(mul(5,gamma),beta);omega=sub(gamma,mul(19,xi))
    eta=sub(xi,omega);chi=sub(mul(2,omega),xi);psi=sub(eta,chi)
    sigma=sub(mul(3,psi),chi);rho=sub(psi,mul(3,sigma));c=sub(sigma,rho)
    om=sub(sigma,mul(10,c));cut=sub(c,om)
    L83=(12945856,-11378629,2191647);L84=add(L83,rho)
    assert L84==(36866988,-32403873,6241338)
    assert L84==add((4,-1,0),add(mul(-7729042,h),mul(1487704,k)))
    top=add((4,-1,0),mul(3,h));formula_top=add(L83,sigma)
    assert sub(formula_top,L84)==c
    assert add(mul(10,cut),mul(11,om))==sigma
    assert rho==add(mul(9,c),om)
    assert sub(mul(10,c),rho)==cut
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(v):return sum((n*l for n,l in zip(v,logs)),old.box(0))
    checks={'c10_positive':c,'sigma_gt_10c':om,'sigma_lt_11c':cut,
            'increment_rho_positive':rho,'high_parameter_range_nonempty':sub(rho,c),
            'endpoint_below_eighth_formula_bound':c,
            'eighth_formula_bound_below_seventh_bound':psi,
            'endpoint_below_three_layers':sub(top,L84)}
    boxes={name:enc(v) for name,v in checks.items()}
    assert all(v.lo>0 for v in boxes.values())
    return {'outward_rational_log_order_checks':{k:g77.show_box(v,36) for k,v in boxes.items()},
            'endpoint_prime_log_vector':L84,'endpoint_h_k_vector':[-7729042,1487704],
            'increment_prime_log_vector':rho,
            'endpoint_decimal':g77.show_box(enc(L84),32),
            'increment_decimal':g77.show_box(enc(rho),36),
            'remaining_eighth_formula_width':g77.show_box(enc(c),36),
            'remaining_three_layer_width':g77.show_box(enc(sub(top,L84)),36),
            'tenth_tower_identity':'10(c10-omega10)+11omega10=sigma8'}


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
    seventh={k:product(w,atoms) for k,w in g81.SEVENTH.items()}
    c7={k:sum(c6[x] for x in w) for k,w in g81.SEVENTH.items()}
    eighth={k:product(w,seventh) for k,w in parent.EIGHTH.items()}
    c8={k:sum(c7[x] for x in w) for k,w in parent.EIGHTH.items()}
    ninth={k:product(w,eighth) for k,w in NINTH.items()}
    c9={k:sum(c8[x] for x in w) for k,w in NINTH.items()}
    assert c9=={'P':965296,'Q':965296,'R':1319293,'S':1319293}
    for lib in (atoms,seventh,eighth,ninth):
        for B in lib.values():
            dd=det(B);assert dd.lo>0 and dd.lo<=1<=dd.hi
    # The new Q is GERM-83's elliptic stopping word, not its old namesakes.
    assert NINTH['Q']==parent.GUARD
    Q=ninth['Q'];qt=Q[0][0]+Q[1][1];qd=qt*qt-4*det(Q)
    assert qd.hi<0
    tests={}
    for label,words,chart in (('low',LOW,CLO),('high',HIGH,CHI)):
        cert={}
        for (s,n),w in words.items():
            B=product(w,ninth)
            sign=(-1 if s==0 else 1) if label=='low' else (-1)**(s//2)
            item=g77.cone_test(B,chart,sign,FACTOR)
            count=sum(c9[x] for x in w);assert count==965296+(n-1)*1319293
            w8=g81.expand(w,NINTH);direct=product(w8,eighth)
            # Regression only. Literal substitution establishes exact equality.
            for i in range(2):
                for j in range(2):
                    assert max(B[i][j].lo,direct[i][j].lo)<=min(B[i][j].hi,direct[i][j].hi)
            item.update({'ninth_word':w,'eighth_word':w8,'original_step_count':count,
                         'determinant_rho_exponent':0})
            cert[f'{s}/{n}']=item
        tests[label]=cert
    # First word beyond b=rho is Q,S,...,S, with nine S steps.
    B=product(GUARD,ninth);tr=B[0][0]+B[1][1];dd=det(B);disc=tr*tr-4*dd
    assert dd.lo>0 and dd.lo<=1<=dd.hi
    assert F(172,100)<tr.lo<tr.hi<F(173,100) and disc.hi<0
    return {'physical_recalculation':'FRESH OUTWARD RATIONAL PAIRED-SOURCE SOLVES',
            'precision':{'grid':'10^120','log_series_terms':400},'layer_pivots':pivots,
            'GERM71_box_regression':'CONTAINED; not rounded numerical inputs',
            'ninth_maps':{k:old.display_matrix(B) for k,B in ninth.items()},
            'entry_Q_discriminant':old.display_matrix([[qd]]),
            'low_chart':[['1','1'],['-97/50','-19/10']],
            'high_chart':[['1','-1'],['-97/50','199/100']],
            'common_forward_backward_factor':'5','cone_tests':tests,
            'distinct_temporal_words':21,'cone_chart_tests':23,
            'next_tenth_ninth_word':GUARD,'next_trace':old.display_matrix([[tr]]),
            'next_determinant':old.display_matrix([[dd]]),
            'next_discriminant':old.display_matrix([[disc]])}


# Inherited affine coordinates (beta/gamma,zeta/gamma,seed/gamma).
af,add,sub,val,vertices=parent.af,parent.add,parent.sub,parent.val,parent.vertices
scale,audit=parent.scale,parent.audit
zero=af();seed=parent.seed;t=parent.t;psi=parent.psi;chi=parent.chi
sigma,rho,c=parent.sigma,parent.rho,parent.c
om=sub(sigma,scale(10,c));cut=sub(c,om)
b=sub(parent.a,parent.amax)
RANGE=parent.RANGE+(om,sub(c,om))


def ninth_req(key,y):
    small=key in ('P','Q');inside=key in ('Q','S')
    target=add(y,rho) if small else sub(y,c)
    return target,[('y>0',y),('y<sigma',sub(sigma,y)),('target>0',target),
                   ('target<sigma',sub(sigma,target)),('lower_global_scope',b),
                   ('ninth_formula_global_scope',sub(sigma,b)),
                   ('ninth_cut',sub(c,y) if small else sub(y,c)),
                   ('ninth_source_bit',sub(b,y) if inside else sub(y,b))]


def ninth_lift(key,y):
    target,m=ninth_req(key,y)
    s,n={'P':(1,3),'Q':(2,3),'R':(2,4),'S':(3,4)}[key]
    assert NINTH[key]==['A']+['D']*(n-s-1)+['E']*s
    q,lower=parent.ninth_lift(s,n,y);assert target==q
    return target,m+[(f'eighth:{name}',v) for name,v in lower]


def tenth_lift(word,y):
    n=len(word)
    pp=[y]+[add(y,sub(sigma,scale(j,c))) for j in range(1,n+1)]
    q=pp[-1]
    m=[('y>0',y),('y<c',sub(c,y)),('q>0',q),('q<c',sub(c,q))]
    for j,key in enumerate(word):
        target,lower=ninth_req(key,pp[j]);assert target==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_tenth_hit{j}',sub(target,c) if j<n-1 else sub(c,target)))
    return q,m


def geometry_audit():
    levels={}
    for label,lib,req,lift in (
        ('sixth',g81.ATOMS,g81.atom_req,g81.atom_lift),
        ('seventh',g81.SEVENTH,g81.seventh_req,g81.seventh_lift),
        ('eighth',parent.EIGHTH,parent.eighth_req,parent.eighth_lift),
        ('ninth',NINTH,ninth_req,ninth_lift)):
        cells={}
        for key in lib:
            _,rr=req(key,seed);_,m=lift(key,seed)
            cond=RANGE+tuple(v for _,v in rr);item=audit(m,vertices(cond))
            if label=='eighth' and key in ('A','E'):
                item['upper_formula_face']=audit(m,vertices(cond+(sub(t,sub(chi,psi)),)))
            if label=='ninth' and key in ('Q','S'):
                item['b_equals_sigma_formula_face']=audit(m,vertices(cond+(sub(b,sigma),)))
            if label=='ninth' and key in ('P','R'):
                item['b_equals_zero_entry_face']=audit(m,vertices(cond+(sub(zero,b),)))
            cells[key]=item
        levels[label]=cells
    low={};high={}
    for (i,n),word in LOW.items():
        q,m=tenth_lift(word,seed)
        cond=RANGE+(b,sub(c,b),seed,sub(c,seed),q,sub(c,q),
                    sub(b,seed) if i else sub(seed,b))
        m.append(('low_upper_global_scope',sub(c,b)))
        item=audit(m,vertices(cond))
        if i:item['b_equals_c_junction']=audit(m,vertices(cond+(sub(b,c),)))
        low[f'{i}/{n}']=item
    for (s,n),word in HIGH.items():
        q,m=tenth_lift(word,seed)
        cond=RANGE+(sub(b,c),sub(rho,b),seed,sub(c,seed),q,sub(c,q))
        cond += (sub(add(q,c),b),) if s==0 else (
            sub(b,add(q,scale(s,c))),sub(add(q,scale(s+1,c)),b))
        m += [('high_lower_global_scope',sub(b,c)),('high_upper_global_scope',sub(rho,b))]
        item=audit(m,vertices(cond))
        if s==0:item['b_equals_c_junction']=audit(m,vertices(cond+(sub(c,b),)))
        if s==n-2:item['b_equals_rho_endpoint']=audit(m,vertices(cond+(sub(b,rho),)))
        high[f'{s}/{n}']=item
    assert add(cut,om)==c
    assert sub(sigma,scale(10,c))==om
    assert sub(sigma,scale(11,c))==scale(-1,cut)
    assert add(scale(10,cut),scale(11,om))==sigma
    assert rho==add(scale(9,c),om) and sub(scale(10,c),rho)==cut
    # Just above b=rho: 0<y<epsilon<cut; the ten-step word is Q,S^9.
    eps=sub(b,rho);q,m=tenth_lift(GUARD,seed)
    cond=RANGE+(eps,sub(cut,eps),seed,sub(eps,seed))
    assert q==add(seed,om)
    guard=audit(m,vertices(cond))
    return {'parameter':'b=t-(2psi7-2sigma8)=e-e83',
            'rechecked_lower_contracts':levels,
            'ninth_formula_scope':'0<b<=sigma8; includes directly checked formula endpoint',
            'new_exclusion_scope':'0<b<=rho9=sigma8-c10',
            'physical_field':'W(t0+y); t0=h-beta+gamma-xi+2eta7',
            'tenth_section':'(0,c10)','tenth_times':'10 for y<c10-omega10; 11 otherwise',
            'tenth_map':'y -> y+omega10 mod c10','images':'(omega10,c10) and (0,omega10)',
            'low_cells':low,'high_cells':high,
            'upper_endpoint_words':['S^8 R Q','S^9 R Q'],
            'next_domain':'b=rho9+eps; 0<y<eps<c10-omega10',
            'next_guard':guard,'sampled_topology':False}


def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-84','standing':'UNRATIFIED',
         'entry_commit':'6ad58be47a9861dd495ce45168d0e6c2055b3795',
         'new_exclusion_scope':'0<b<=rho9, b=e-e83; L83<L<=L83+rho9',
         'inherited_three_layer_formula_scope':'2h<e<=3h',
         'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
         'matrix_namespace':'A/D/E are GERM-83-local; P/Q/R/S and tenth words are GERM-84-local',
         'ninth_word_dictionary':NINTH,
         'arithmetic':arithmetic(),'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
         'full_lower_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
         'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
