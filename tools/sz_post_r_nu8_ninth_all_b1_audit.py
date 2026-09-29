#!/usr/bin/env python3
"""GERM-94: all-B1 ninth returns controlled through epsilon=rho9.

Four ninth formulas hold on 0<epsilon<=sigma8, epsilon=e-e93. Four low
and nineteen high tenth cells (21 distinct words) have two parameter-fixed
rational cone charts with common factor 7. Every intermediate source is
checked. No eleventh induction or extra retained coordinate is used.
Run with assertions enabled, without -O. Unratified scalar-source work.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of the certificate; run without -O.'
ROOT=Path(__file__).resolve().parents[1]
PIN_PATH='tools/sz_post_b_nu8_eighth_two_step_audit.py'
PIN_SHA='d21672ee25dbdd5181f0c43b5f4423027ca92c9762c7a8b05b1d343f27857776'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest()==PIN_SHA
import sz_post_b_nu8_eighth_two_step_audit as parent
g91,g75,g77,old=parent.g91,parent.g75,parent.g77,parent.old
product,det=parent.product,parent.det
# Eighth inputs are GERM-93-local; P/Q/R/S below are GERM-94-local.
NINTH={'P':['A1','B0','B1'],'Q':['A1','B1','B1'],
       'R':['A1','B0','B1','B1'],'S':['A1','B1','B1','B1']}
LOW={(i,n):[('Q' if i else 'P')]+['R']*(n-1) for n in (10,11) for i in (0,1)}
HIGH={(s,n):['Q']+['R']*(n-s-1)+['S']*s for n in (10,11) for s in range(n-1)}
CHART_LOW=[[1,1],[1,2]]
CHART_HIGH=[[1,-1],[1,F(-2,5)]]
FACTOR=F(7)
NEXT=['Q']+['S']*9


def arithmetic():
    add,sub,mul=old.add,old.sub,old.mul
    h,k=(-4,4,-1),(4,-1,-1)
    kap=sub(k,mul(5,h));tau=sub(h,mul(5,kap));th=sub(kap,mul(8,tau))
    alpha=sub(tau,mul(3,th));beta=sub(th,alpha);gamma=sub(alpha,beta)
    xi=sub(mul(5,gamma),beta);om=sub(gamma,mul(19,xi))
    eta=sub(xi,om);chi=sub(mul(2,om),xi);psi=sub(eta,chi)
    sigma=sub(mul(3,psi),chi);nu=sub(chi,mul(2,psi))
    rho=sub(psi,mul(3,sigma));c=sub(sigma,rho)
    om10=sub(sigma,mul(10,c));ell=sub(c,om10)
    L93=(8924844,-7844400,1510916);L94=add(L93,rho)
    top=add((4,-1,0),mul(3,h));formula_top=add(L93,sigma)
    assert rho==(23921132,-21025244,4049691)
    assert L94==(32845976,-28869644,5560607)
    assert L94==add((4,-1,0),add(mul(-6886050,h),mul(1325443,k)))
    assert formula_top==(152396,-133943,25798)
    assert sub(formula_top,L94)==c
    assert nu==add(mul(2,sigma),rho) and add(nu,sigma)==psi
    assert add(c,rho)==sigma and add(mul(3,c),mul(4,rho))==psi
    assert add(ell,om10)==c and add(mul(10,ell),mul(11,om10))==sigma
    assert rho==add(mul(9,c),om10) and sub(mul(10,c),rho)==ell
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(v):return sum((n*l for n,l in zip(v,logs)),old.box(0))
    checks={'c_positive':c,'rho_positive':rho,'rho_gt_c':sub(rho,c),
            'sigma_gt_10c':om10,'sigma_lt_11c':ell,
            'formula_margin_after_new_exclusion':c,
            'formula_endpoint_below_three_layers':sub(top,formula_top)}
    boxes={k:enc(v) for k,v in checks.items()};assert all(v.lo>0 for v in boxes.values())
    return {'rational_log_order_checks':{k:g77.show_box(v,38) for k,v in boxes.items()},
            'endpoint_prime_log_vector':L94,'endpoint_h_k_vector':[-6886050,1325443],
            'endpoint_decimal':g77.show_box(enc(L94),38),
            'increment':'rho9=psi7-3sigma8','increment_prime_log_vector':rho,
            'increment_decimal':g77.show_box(enc(rho),38),
            'formula_endpoint_prime_log_vector':formula_top,
            'remaining_parent_formula_width':g77.show_box(enc(c),38),
            'remaining_three_layer_width':g77.show_box(enc(sub(top,L94)),38),
            'tower_identities':['3c10+4rho9=psi7','10(c10-omega10)+11omega10=sigma8']}


def rational_audit():
    original,pivots=g75.parent.parent.parent.parent.recalculate_returns()
    legacy=g75.parent.parent.parent
    first={k:product(w,original) for k,w in legacy.FIRST.items()}
    second={k:product(w,first) for k,w in legacy.SECOND.items()}
    boxes=json.loads((ROOT/'notes/_recurrence71_audit.json').read_text())['audit']['rational_audit']['second_section_maps']
    for k,m in second.items():
        for i in range(2):
            for j in range(2):
                lo,hi=map(F,boxes[k][i][j]);assert lo<=m[i][j].lo<=m[i][j].hi<=hi
    third={k:product(w,second) for k,w in g75.THIRD.items()}
    fourth={k:product(w,third) for k,w in g75.FOURTH.items()}
    fifth={k:product(w,fourth) for k,w in g75.FIFTH.items()}
    atoms={k:product(g75.sixth_word(*pair),fifth) for k,pair in g91.ATOMS.items()}
    count6={}
    for k,pair in g91.ATOMS.items():
        ow=g75.to_original(g75.sixth_word(*pair))
        assert legacy.determinant_exponent(ow)==0 and len(ow)==1654*pair[1]-297
        count6[k]=len(ow)
    seven={k:product(w,atoms) for k,w in g91.SEVENTH.items()}
    count7={k:sum(count6[a] for a in w) for k,w in g91.SEVENTH.items()}
    eight={k:product(w,seven) for k,w in parent.EIGHTH.items()}
    count8={k:sum(count7[a] for a in w) for k,w in parent.EIGHTH.items()}
    nine={k:product(w,eight) for k,w in NINTH.items()}
    count9={k:sum(count8[a] for a in w) for k,w in NINTH.items()}
    assert count9=={'P':965296,'Q':965296,'R':1319293,'S':1319293}
    assert NINTH['P']==parent.HIGH[1,3] and NINTH['R']==parent.HIGH[2,4]
    assert NINTH['Q']==parent.NEXT
    spectra={}
    for k,m in nine.items():
        dd=det(m);tr=m[0][0]+m[1][1];disc=tr*tr-4*dd
        assert dd.lo>0 and dd.lo<=1<=dd.hi
        assert disc.hi<0 if k in ('Q','S') else disc.lo>0
        spectra[k]={'trace':old.display_matrix([[tr]]),'discriminant':old.display_matrix([[disc]])}
    for C,expected in ((CHART_LOW,F(1)),(CHART_HIGH,F(3,5))):
        assert F(C[0][0])*F(C[1][1])-F(C[0][1])*F(C[1][0])==expected
    cert={}
    for label,lib,C in (('low',LOW,CHART_LOW),('high',HIGH,CHART_HIGH)):
        rows={}
        for pair,w in lib.items():
            m=product(w,nine);tr=m[0][0]+m[1][1]
            assert tr.lo>0 or tr.hi<0
            sign=1 if tr.lo>0 else -1 # certified exact/outward sign, not a floating decision
            item=g77.cone_test(m,C,sign,FACTOR)
            dd=det(m);assert (tr*tr-4*dd).lo>0
            count=sum(count9[x] for x in w);assert count==965296+(pair[1]-1)*1319293
            item.update({'ninth_word':w,'original_step_count':count,'determinant_rho_exponent':0})
            rows[f'{pair[0]}/{pair[1]}']=item
        cert[label]=rows
    distinct={tuple(w) for w in list(LOW.values())+list(HIGH.values())};assert len(distinct)==21
    for n in (10,11):assert LOW[1,n]==HIGH[0,n]
    m=product(NEXT,nine);tr=m[0][0]+m[1][1];dd=det(m);disc=tr*tr-4*dd
    assert dd.lo>0 and dd.lo<=1<=dd.hi and disc.hi<0
    assert F(15,100)<tr.lo<tr.hi<F(16,100)
    return {'physical_recalculation':'FRESH PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
            'precision':{'grid':'10^120','log_series_terms':400},'layer_pivots':pivots,
            'GERM71_box_regression':'CONTAINED; not rounded proof inputs',
            'ninth_spectra':spectra,
            'charts':{k:[[str(x) for x in row] for row in C] for k,C in (('low',CHART_LOW),('high',CHART_HIGH))},
            'chart_determinants':['1','3/5'],'sign_rule':'certified sign of each complete matrix trace',
            'common_forward_backward_factor':'7','twenty_three_chart_tests':cert,
            'distinct_temporal_words':21,'shared_words':2,
            'next_ninth_word':NEXT,'next_matrix':'S^9 Q, GERM-94-local ninth maps',
            'next_trace':old.display_matrix([[tr]]),'next_determinant':old.display_matrix([[dd]]),
            'next_discriminant':old.display_matrix([[disc]]),'next_status':'ELLIPTIC COMPLETE TEN-STEP TENTH RETURN',
            'eleventh_or_deeper_induction_used':False,'new_retained_coordinates':0}


# Exact affine coordinates inherited from GERM-93; gamma=1.
af,add,sub,vertices=parent.af,parent.add,parent.sub,parent.vertices
scale,audit=parent.scale,parent.audit
seed,r,psi,sigma,nu,rho,c=parent.seed,parent.r,parent.psi,parent.sigma,parent.nu,parent.rho,parent.c
zero=af();eps=sub(r,nu);om=sub(sigma,scale(10,c));ell=sub(c,om)
RANGE=parent.RANGE+(om,ell)


def ninth_req(key,y):
    small=key in ('P','Q');inside=key in ('Q','S')
    q=add(y,rho) if small else sub(y,c)
    m=[('y>0',y),('y<sigma',sub(sigma,y)),('q>0',q),('q<sigma',sub(sigma,q)),
       ('ninth_lower_global_scope',eps),('ninth_upper_global_scope',sub(sigma,eps)),
       ('ninth_cut',sub(c,y) if small else sub(y,c)),
       ('last_internal_visit',sub(eps,y) if inside else sub(y,eps))]
    return q,m


def ninth_lift(key,y):
    q,m=ninth_req(key,y);out,lower=parent.ninth_word_lift(NINTH[key],y);assert out==q
    return q,m+[(f'eighth:{name}',v) for name,v in lower]


def tenth_lift(word,y):
    n=len(word);assert n in (10,11)
    pp=[y]+[add(y,sub(sigma,scale(j,c))) for j in range(1,n+1)]
    q=pp[-1]
    m=[('y>0',y),('y<c',sub(c,y)),('q>0',q),('q<c',sub(c,q)),
       ('tenth_cut',sub(ell,y) if n==10 else sub(y,ell))]
    for j,k in enumerate(word):
        out,lower=ninth_req(k,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_tenth_hit_{j}',sub(out,c) if j<n-1 else sub(c,out)))
    return q,m


def geometry_audit():
    lower=parent.geometry_audit() # includes sixth/fifth, seventh/sixth, eighth/seventh and endpoints
    cells9={}
    for k in NINTH:
        _,rr=ninth_req(k,seed);_,m=ninth_lift(k,seed)
        cond=RANGE+tuple(v for _,v in rr);item=audit(m,vertices(cond))
        if k in ('P','R'):item['epsilon_zero_entry']=audit(m,vertices(cond+(sub(zero,eps),)))
        if k in ('Q','S'):item['epsilon_sigma_formula_endpoint']=audit(m,vertices(cond+(sub(eps,sigma),)))
        cells9[k]=item
    low={}
    for (i,n),w in LOW.items():
        q,m=tenth_lift(w,seed)
        cond=RANGE+(eps,sub(c,eps),seed,sub(c,seed),q,sub(c,q),
                    sub(eps,seed) if i else sub(seed,eps))
        item=audit(m,vertices(cond))
        if i==0:item['epsilon_zero_entry']=audit(m,vertices(cond+(sub(zero,eps),)))
        if i==1:item['epsilon_c_junction']=audit(m,vertices(cond+(sub(eps,c),)))
        low[f'{i}/{n}']=item
    high={}
    for (s,n),w in HIGH.items():
        q,m=tenth_lift(w,seed)
        cond=RANGE+(sub(eps,c),sub(rho,eps),seed,sub(c,seed),q,sub(c,q))
        cond += (sub(add(q,c),eps),) if s==0 else (
            sub(eps,add(q,scale(s,c))),sub(add(q,scale(s+1,c)),eps))
        item=audit(m,vertices(cond))
        if s==0:item['epsilon_c_junction']=audit(m,vertices(cond+(sub(c,eps),)))
        if s==n-2:item['epsilon_rho_exclusion_endpoint']=audit(m,vertices(cond+(sub(eps,rho),)))
        j=s+1
        if j<=9:
            face=scale(j,c)
            item[f'epsilon_{j}c_junction']=audit(m,vertices(cond+(sub(eps,face),sub(face,eps))))
        high[f'{s}/{n}']=item
    assert add(nu,sigma)==psi and add(c,rho)==sigma
    assert add(scale(3,c),scale(4,rho))==psi
    assert add(ell,om)==c and add(scale(10,ell),scale(11,om))==sigma
    assert rho==add(scale(9,c),om) and sub(scale(10,c),rho)==ell
    excess=sub(eps,rho);q,m=tenth_lift(NEXT,seed)
    assert q==add(seed,om)
    guard=audit(m,vertices(RANGE+(excess,sub(ell,excess),seed,sub(excess,seed))))
    return {'parameter':'epsilon=r-nu8=e-e93; r=e-e92',
            'ninth_formula_scope':'0<epsilon<=sigma8; inherited eighth/parent endpoint included',
            'new_exclusion_scope':'0<epsilon<=rho9','rechecked_parent_geometry':lower,
            'four_ninth_formula_cells':cells9,'four_low_tenth_cells':low,'nineteen_high_tenth_cells':high,
            'tenth_map':'y -> y+omega10 mod c10','images':'(omega10,c10) and (0,omega10)',
            'physical_field':'W(t0+y); t0=h-beta+gamma-xi+2eta7',
            'exclusion_endpoint_words':['S^8 R Q','S^9 R Q'],
            'formula_endpoint_maps':['Q','S'],
            'next_domain':'epsilon=rho9+excess; 0<y<excess<c10-omega10',
            'next_ninth_word':NEXT,'next_guard':guard,'sampled_topology':False}


def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-94','standing':'UNRATIFIED',
         'entry_commit':'c76f96460918447b17162cb492acbbc30b9551c7',
         'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
         'matrix_namespace':'A0/A1/B0/B1 are GERM-93-local; P/Q/R/S are GERM-94-local',
         'ninth_word_dictionary':NINTH,
         'low_tenth_words':{f'{i}/{n}':w for (i,n),w in LOW.items()},
         'high_tenth_words':{f'{s}/{n}':w for (s,n),w in HIGH.items()},
         'arithmetic':arithmetic(),'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
         'full_lower_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
         'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
