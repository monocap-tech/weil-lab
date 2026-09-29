#!/usr/bin/env python3
"""GERM-95: all-S tenth control through delta=4c11, delta=e-e94.

Four tenth formulas hold on 0<delta<=c10. Ten distinct eleventh words
have fourteen chart tests across three fixed-parameter regimes. Every
intermediate source is checked. The next all-U1 five-step word is elliptic.
Run with assertions enabled, without -O. Unratified scalar-source work.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of the certificate; run without -O.'
ROOT=Path(__file__).resolve().parents[1]
PIN_PATH='tools/sz_post_r_nu8_ninth_all_b1_audit.py'
PIN_SHA='dcf1a50ba7a3cfa794a871d0bc4e5d900158866659a43f2b63e2d0e9b4ba0766'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest()==PIN_SHA
import sz_post_r_nu8_ninth_all_b1_audit as parent
g93,g91,g75,g77,old=parent.parent,parent.g91,parent.g75,parent.g77,parent.old
product,det=parent.product,parent.det
# Ninth P/Q/R/S retain GERM-94 definitions; tenth U/V are GERM-95-local.
TENTH={'V0':['Q','R']+['S']*8, 'V1':['Q']+['S']*9,
       'U0':['Q','R']+['S']*9, 'U1':['Q']+['S']*10}
LOW={(i,n):[f'V{i}']+['U0']*(n-1) for n in (4,5) for i in (0,1)}
MIDDLE={(s,n):['V1']+['U0']*(n-s-1)+['U1']*s
        for n in (4,5) for s in range(n-1)}
HIGH={(s,n):['V1']+['U0']*(n-s-1)+['U1']*s for s,n in ((2,4),(3,4),(3,5))}
CHARTS={'low':[[1,0],[-20,-1]],
        'middle':[[1,F(-1,8)],[F(-23,5),F(18,5)]],
        'high':[[1,F(3,4)],[-6,6]]}
FACTOR=F(2)
NEXT=['V1']+['U1']*4


def arithmetic():
    add,sub,mul=old.add,old.sub,old.mul
    h,k=(-4,4,-1),(4,-1,-1)
    kap=sub(k,mul(5,h));tau=sub(h,mul(5,kap));th=sub(kap,mul(8,tau))
    alpha=sub(tau,mul(3,th));beta=sub(th,alpha);gamma=sub(alpha,beta)
    xi=sub(mul(5,gamma),beta);om=sub(gamma,mul(19,xi))
    eta=sub(xi,om);chi=sub(mul(2,om),xi);psi=sub(eta,chi)
    sigma=sub(mul(3,psi),chi);rho=sub(psi,mul(3,sigma));c=sub(sigma,rho)
    om10=sub(sigma,mul(10,c));ell=sub(c,om10);om11=sub(c,mul(4,ell));cut=sub(ell,om11)
    L94=(32845976,-28869644,5560607);L95=add(L94,mul(4,ell))
    formula_top=add(L94,c);top=add((4,-1,0),mul(3,h))
    assert ell==(-350856932,308382254,-59397781)
    assert om11==(1370734148,-1204793315,232056315)
    assert L95==(-1370581752,1204659372,-232030517)
    assert L95==add((4,-1,0),add(mul(287337978,h),mul(-55307461,k)))
    assert formula_top==(152396,-133943,25798) and sub(formula_top,L95)==om11
    assert add(mul(3,ell),om11)==om10 and add(mul(4,ell),om11)==c
    assert add(mul(4,cut),mul(5,om11))==c
    assert add(mul(10,ell),mul(11,om10))==sigma
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(v):return sum((a*l for a,l in zip(v,logs)),old.box(0))
    checks={'c11_positive':ell,'omega11_positive':om11,'omega11_lt_c11':cut,
            'middle_range_nonempty':sub(om10,ell),'high_range_nonempty':sub(mul(4,ell),om10),
            'remaining_parent_formula_width':sub(formula_top,L95),
            'formula_endpoint_below_three_layers':sub(top,formula_top)}
    boxes={k:enc(v) for k,v in checks.items()};assert all(v.lo>0 for v in boxes.values())
    return {'rational_log_order_checks':{k:g77.show_box(v,38) for k,v in boxes.items()},
            'endpoint_prime_log_vector':L95,'endpoint_h_k_vector':[287337978,-55307461],
            'endpoint_decimal':g77.show_box(enc(L95),38),'increment':'4c11',
            'increment_prime_log_vector':mul(4,ell),'increment_decimal':g77.show_box(enc(mul(4,ell)),38),
            'formula_endpoint_prime_log_vector':formula_top,'c11_prime_log_vector':ell,
            'omega11_prime_log_vector':om11,'remaining_parent_formula_width':g77.show_box(enc(om11),38),
            'remaining_three_layer_width':g77.show_box(enc(sub(top,L95)),38),
            'tower_identities':['10c11+11omega10=sigma8','4(c11-omega11)+5omega11=c10']}


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
    eight={k:product(w,seven) for k,w in g93.EIGHTH.items()}
    count8={k:sum(count7[a] for a in w) for k,w in g93.EIGHTH.items()}
    nine={k:product(w,eight) for k,w in parent.NINTH.items()}
    count9={k:sum(count8[a] for a in w) for k,w in parent.NINTH.items()}
    ten={k:product(w,nine) for k,w in TENTH.items()}
    count10={k:sum(count9[a] for a in w) for k,w in TENTH.items()}
    assert count10=={'V0':12838933,'V1':12838933,'U0':14158226,'U1':14158226}
    assert TENTH['V0']==parent.HIGH[8,10] and TENTH['U0']==parent.HIGH[9,11]
    assert TENTH['V1']==parent.NEXT
    spectra={}
    for k,m in ten.items():
        dd=det(m);tr=m[0][0]+m[1][1];disc=tr*tr-4*dd
        assert dd.lo>0 and dd.lo<=1<=dd.hi
        assert disc.hi<0 if k.endswith('1') else disc.lo>0
        spectra[k]={'trace':old.display_matrix([[tr]]),'discriminant':old.display_matrix([[disc]])}
    for label,expected in (('low',F(-1)),('middle',F(121,40)),('high',F(21,2))):
        C=CHARTS[label];assert F(C[0][0])*F(C[1][1])-F(C[0][1])*F(C[1][0])==expected
    cert={}
    for label,lib in (('low',LOW),('middle',MIDDLE),('high',HIGH)):
        rows={}
        for pair,w in lib.items():
            m=product(w,ten);tr=m[0][0]+m[1][1];dd=det(m)
            assert tr.lo>0 or tr.hi<0
            sign=1 if tr.lo>0 else -1
            item=g77.cone_test(m,CHARTS[label],sign,FACTOR)
            assert (tr*tr-4*dd).lo>0
            count=sum(count10[k] for k in w);assert count==12838933+(pair[1]-1)*14158226
            item.update({'tenth_word':w,'original_step_count':count,'determinant_rho_exponent':0})
            rows[f'{pair[0]}/{pair[1]}']=item
        cert[label]=rows
    distinct={tuple(w) for lib in (LOW,MIDDLE,HIGH) for w in lib.values()};assert len(distinct)==10
    assert len(LOW)+len(MIDDLE)+len(HIGH)==14
    m=product(NEXT,ten);tr=m[0][0]+m[1][1];dd=det(m);disc=tr*tr-4*dd
    assert dd.lo>0 and dd.lo<=1<=dd.hi and disc.hi<0
    assert F(176,100)<tr.lo<tr.hi<F(177,100)
    return {'physical_recalculation':'FRESH PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
            'precision':{'grid':'10^120','log_series_terms':400},'layer_pivots':pivots,
            'GERM71_box_regression':'CONTAINED; not rounded proof inputs','tenth_spectra':spectra,
            'charts':{k:[[str(x) for x in row] for row in C] for k,C in CHARTS.items()},
            'chart_determinants':['-1','121/40','21/2'],'sign_rule':'certified sign of each complete trace',
            'common_forward_backward_factor':'2','fourteen_chart_tests':cert,'distinct_temporal_words':10,
            'next_tenth_word':NEXT,'next_matrix':'U1^4 V1, GERM-95-local tenth maps',
            'next_trace':old.display_matrix([[tr]]),'next_determinant':old.display_matrix([[dd]]),
            'next_discriminant':old.display_matrix([[disc]]),'next_status':'ELLIPTIC COMPLETE FIVE-STEP ELEVENTH RETURN',
            'twelfth_or_deeper_induction_used':False,'new_retained_coordinates':0}


# Exact affine coordinates inherited from GERM-94; gamma=1.
af,add,sub,vertices=parent.af,parent.add,parent.sub,parent.vertices
scale,audit=parent.scale,parent.audit
seed,eps,sigma,rho,c,ell=parent.seed,parent.eps,parent.sigma,parent.rho,parent.c,parent.ell
zero=af();delta=sub(eps,rho);om10=parent.om;om11=sub(c,scale(4,ell));cut11=sub(ell,om11)
RANGE=parent.RANGE+(om11,cut11)


def tenth_req(key,y):
    n=10 if key[0]=='V' else 11;inside=key[-1]=='1'
    q=add(y,sub(sigma,scale(n,c)))
    return q,[('y>0',y),('y<c10',sub(c,y)),('q>0',q),('q<c10',sub(c,q)),
              ('tenth_lower_global_scope',delta),('tenth_upper_global_scope',sub(c,delta)),
              ('tenth_cut',sub(ell,y) if n==10 else sub(y,ell)),
              ('first_later_source_bit',sub(delta,y) if inside else sub(y,delta))]


def tenth_lift(key,y):
    q,m=tenth_req(key,y);target,lower=parent.tenth_lift(TENTH[key],y);assert target==q
    return q,m+[(f'ninth:{name}',v) for name,v in lower]


def eleventh_lift(word,y):
    n=len(word);assert n in (4,5)
    pp=[y]+[add(y,sub(c,scale(j,ell))) for j in range(1,n+1)]
    q=pp[-1];m=[('y>0',y),('y<c11',sub(ell,y)),('q>0',q),('q<c11',sub(ell,q)),
                 ('eleventh_cut',sub(cut11,y) if n==4 else sub(y,cut11))]
    for j,k in enumerate(word):
        target,lower=tenth_req(k,pp[j]);assert target==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_eleventh_hit{j}',sub(target,ell) if j<n-1 else sub(ell,target)))
    return q,m


def geometry_audit():
    lower=parent.geometry_audit() # includes inherited sixth/fifth through ninth/eighth and endpoints
    cells10={}
    for k in TENTH:
        _,rr=tenth_req(k,seed);_,m=tenth_lift(k,seed)
        cond=RANGE+tuple(v for _,v in rr);item=audit(m,vertices(cond))
        if k.endswith('0'):item['delta_zero_entry']=audit(m,vertices(cond+(sub(zero,delta),)))
        if k.endswith('1'):item['delta_c10_formula_endpoint']=audit(m,vertices(cond+(sub(delta,c),)))
        cells10[k]=item
    low={}
    for (i,n),w in LOW.items():
        q,m=eleventh_lift(w,seed)
        cond=RANGE+(delta,sub(ell,delta),seed,sub(ell,seed),q,sub(ell,q),
                    sub(delta,seed) if i else sub(seed,delta))
        item=audit(m,vertices(cond))
        if i==0:item['delta_zero_entry']=audit(m,vertices(cond+(sub(zero,delta),)))
        if i==1:item['delta_c11_junction']=audit(m,vertices(cond+(sub(delta,ell),)))
        low[f'{i}/{n}']=item
    regimes={}
    for label,lib,lo,hi in (('middle',MIDDLE,ell,om10),('high',HIGH,om10,scale(4,ell))):
        cells={}
        for (s,n),w in lib.items():
            q,m=eleventh_lift(w,seed)
            cond=RANGE+(sub(delta,lo),sub(hi,delta),seed,sub(ell,seed),q,sub(ell,q))
            cond += (sub(add(q,ell),delta),) if s==0 else (
                sub(delta,add(q,scale(s,ell))),sub(add(q,scale(s+1,ell)),delta))
            item=audit(m,vertices(cond))
            if label=='middle' and s==0:
                item['delta_c11_junction']=audit(m,vertices(cond+(sub(ell,delta),)))
            if (s,n) in ((2,4),(3,5)):
                item['delta_omega10_junction']=audit(m,vertices(cond+(sub(delta,om10),sub(om10,delta))))
            if label=='middle' and s in (1,2):
                face=scale(s+1,ell)
                item[f'delta_{s+1}c11_junction']=audit(m,vertices(cond+(sub(delta,face),sub(face,delta))))
            if label=='high' and (s,n) in ((3,4),(3,5)):
                face=scale(4,ell)
                item['delta_4c11_exclusion_endpoint']=audit(m,vertices(cond+(sub(delta,face),)))
            cells[f'{s}/{n}']=item
        regimes[label]=cells
    assert add(ell,om10)==c and add(scale(3,ell),om11)==om10
    assert add(scale(4,ell),om11)==c and add(scale(4,cut11),scale(5,om11))==c
    # At delta=4ell+b, the all-internal N=5 word enters for cut11<y<cut11+b.
    excess=sub(delta,scale(4,ell));q,m=eleventh_lift(NEXT,seed)
    assert q==sub(seed,cut11)
    guard=audit(m,vertices(RANGE+(excess,sub(om11,excess),sub(seed,cut11),sub(add(cut11,excess),seed))))
    return {'parameter':'delta=epsilon-rho9=e-e94; epsilon=e-e93',
            'tenth_formula_scope':'0<delta<=c10; parent formula endpoint included',
            'new_exclusion_scope':'0<delta<=4c11','rechecked_parent_geometry':lower,
            'four_tenth_formula_cells':cells10,'four_low_eleventh_cells':low,
            'seven_middle_eleventh_cells':regimes['middle'],'three_high_eleventh_cells':regimes['high'],
            'eleventh_map':'y -> y+omega11 mod c11','images':'(omega11,c11) and (0,omega11)',
            'physical_field':'W(t0+y); t0=h-beta+gamma-xi+2eta7',
            'exclusion_endpoint_words':['U1^3 V1','U1^3 U0 V1'],
            'formula_endpoint_maps':['V1','U1'],
            'next_domain':'delta=4c11+b; 0<b<omega11; c11-omega11<y<c11-omega11+b',
            'next_tenth_word':NEXT,'next_guard':guard,'sampled_topology':False}


def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-95','standing':'UNRATIFIED',
         'entry_commit':'811e573aedbd311567491720dac72e309b63df83',
         'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
         'matrix_namespace':'P/Q/R/S are GERM-94-local; tenth U/V are GERM-95-local',
         'tenth_word_dictionary':TENTH,
         'eleventh_words':{label:{f'{i}/{n}':w for (i,n),w in lib.items()}
                           for label,lib in (('low',LOW),('middle',MIDDLE),('high',HIGH))},
         'arithmetic':arithmetic(),'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
         'full_lower_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
         'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
