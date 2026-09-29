#!/usr/bin/env python3
"""GERM-89: post-2psi7 eighth transfer and direct ninth exclusion.

Proves 2psi7<t<=chi7, t=e-e80. Three eighth maps and seven complete
ninth words share a constant rational chart with factor 30. The formerly
open seventh endpoint t=chi7 is rechecked against sixth source contracts.
No tenth induction or new state coordinate is used. Run without -O.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of this certificate; run without -O.'
ROOT=Path(__file__).resolve().parents[1]
PIN_PATH='tools/sz_post_omega10_ten_step_audit.py'
PIN_SHA='2568c96ed8880132dc7a8d8996f6088040afa0f26f652b2f39155bb7244594b3'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest()==PIN_SHA
import sz_post_omega10_ten_step_audit as parent
g86,g81,g77,g75,old=parent.g86,parent.g81,parent.g77,parent.g75,parent.old
product,det=parent.product,parent.det
# A/D/E are GERM-89-local eighth maps; U/V inputs are GERM-81-local.
EIGHTH={'A':['V1','U1'],'D':['V1','U0','U1'],'E':['V1','U1','U1']}
WORDS={(s,n):['A']+['D']*(n-s-1)+['E']*s for n in (3,4) for s in range(n)}
CHART=[[1,1],[F(-21,10),0]]
FACTOR=F(30)
NEXT=['E20','E20','E19','E20','E19']  # sixth atoms, GERM-81-local


def arithmetic():
    add,sub,mul=old.add,old.sub,old.mul
    h=(-4,4,-1);k=(4,-1,-1)
    kap=sub(k,mul(5,h));tau=sub(h,mul(5,kap));theta=sub(kap,mul(8,tau))
    alpha=sub(tau,mul(3,theta));beta=sub(theta,alpha);gamma=sub(alpha,beta)
    xi=sub(mul(5,gamma),beta);omega=sub(gamma,mul(19,xi))
    eta=sub(xi,omega);chi=sub(mul(2,omega),xi);psi=sub(eta,chi)
    sigma=sub(mul(3,psi),chi);rho=sub(psi,mul(3,sigma));c=sub(sigma,rho)
    nu=sub(chi,mul(2,psi))
    L80=(193384,-169969,32737);L88=add(L80,mul(2,psi));L89=add(L80,chi)
    top=add((4,-1,0),mul(3,h))
    assert L88==(-4599040,4042285,-778589)
    assert L89==(1777196,-1562045,300866)
    assert sub(L89,L88)==nu==sub(psi,sigma)
    assert sub(eta,chi)==psi
    assert add(mul(3,c),mul(4,rho))==psi
    assert add(mul(3,sub(chi,psi)),mul(5,psi))==xi
    # Independent h/k form of e80+chi7, not an accumulated decimal.
    assert L89==add((4,-1,0),add(mul(-372582,h),mul(71716,k)))
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(v):return sum((n*l for n,l in zip(v,logs)),old.box(0))
    checks={'increment_nu8_positive':nu,'3sigma8_lt_psi7':rho,
            'psi7_lt_4sigma8':c,'endpoint_below_sixth_bound':sub(eta,chi),
            'endpoint_below_three_layers':sub(top,L89)}
    bounds={key:enc(v) for key,v in checks.items()}
    assert all(v.lo>0 for v in bounds.values())
    return {'rational_log_order_checks':{k:g77.show_box(v,38) for k,v in bounds.items()},
            'endpoint_prime_log_vector':L89,'endpoint_h_k_vector':[-372582,71716],
            'endpoint_decimal':g77.show_box(enc(L89),38),
            'increment_prime_log_vector':nu,'increment_decimal':g77.show_box(enc(nu),38),
            'remaining_seventh_formula_width':'ZERO',
            'remaining_three_layer_width':g77.show_box(enc(sub(top,L89)),38),
            'tower_identities':'3c10+4rho9=psi7; 3(chi7-psi7)+5psi7=xi'}


def rational_audit():
    original,pivots=g75.parent.parent.parent.parent.recalculate_returns()
    legacy=g75.parent.parent.parent
    first={k:product(w,original) for k,w in legacy.FIRST.items()}
    second={k:product(w,first) for k,w in legacy.SECOND.items()}
    boxes=json.loads((ROOT/'notes/_recurrence71_audit.json').read_text())['audit']['rational_audit']['second_section_maps']
    for key,b in second.items():
        for i in range(2):
            for j in range(2):
                lo,hi=map(F,boxes[key][i][j]);assert lo<=b[i][j].lo<=b[i][j].hi<=hi
    third={k:product(w,second) for k,w in g75.THIRD.items()}
    fourth={k:product(w,third) for k,w in g75.FOURTH.items()}
    fifth={k:product(w,fourth) for k,w in g75.FIFTH.items()}
    atoms={k:product(g75.sixth_word(s,n),fifth) for k,(s,n) in g81.ATOMS.items()}
    counts6={}
    for key,(s,n) in g81.ATOMS.items():
        w=g75.to_original(g75.sixth_word(s,n))
        assert legacy.determinant_exponent(w)==0
        counts6[key]=len(w)
    seven={k:product(w,atoms) for k,w in g81.SEVENTH.items()}
    eight={k:product(w,seven) for k,w in EIGHTH.items()}
    counts7={k:sum(counts6[x] for x in w) for k,w in g81.SEVENTH.items()}
    counts8={k:sum(counts7[x] for x in w) for k,w in EIGHTH.items()}
    assert counts8=={'A':257302,'D':353997,'E':353997}
    assert EIGHTH['A']==g86.EIGHTH['A1'] and EIGHTH['D']==g86.EIGHTH['B']
    assert EIGHTH['E']==parent.NEXT
    # At entry no-E ninth maps equal the preceding Q/S by literal words.
    for n,key in ((3,'Q'),(4,'S')):
        assert g81.expand(WORDS[0,n],EIGHTH)==g81.expand(g86.NINTH[key],g86.EIGHTH)
    for lib in (atoms,seven,eight):
        for b in lib.values():
            dd=det(b);assert dd.lo>0 and dd.lo<=1<=dd.hi
    cert={}
    for (s,n),w in WORDS.items():
        b=product(w,eight);item=g77.cone_test(b,CHART,(-1)**(n+1),FACTOR)
        tr=b[0][0]+b[1][1];disc=tr*tr-4*det(b);assert disc.lo>0
        count=sum(counts8[x] for x in w);assert count==257302+(n-1)*353997
        item.update({'eighth_word':w,'seventh_word':g81.expand(w,EIGHTH),
                     'original_step_count':count,'determinant_rho_exponent':0})
        cert[f'{s}/{n}']=item
    b=product(NEXT,atoms);tr=b[0][0]+b[1][1];dd=det(b);disc=tr*tr-4*dd
    assert dd.lo>0 and dd.lo<=1<=dd.hi
    assert F(3)<tr.lo<tr.hi<F(4) and disc.lo>0
    return {'physical_recalculation':'FRESH PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
            'precision':{'grid':'10^120','log_series_terms':400},'layer_pivots':pivots,
            'GERM71_box_regression':'CONTAINED; not rounded proof inputs',
            'eighth_maps':{k:old.display_matrix(b) for k,b in eight.items()},
            'chart':[['1','1'],['-21/10','0']],'common_forward_backward_factor':'30',
            'seven_complete_ninth_returns':cert,'all_ninth_discriminants':'POSITIVE',
            'tenth_induction_used':False,'new_retained_coordinates':0,
            'next_seventh_sixth_word':NEXT,'next_trace':old.display_matrix([[tr]]),
            'next_determinant':old.display_matrix([[dd]]),'next_discriminant':old.display_matrix([[disc]]),
            'next_status':'HYPERBOLIC CHANGED FIVE-STEP SEVENTH SOURCE WORD; NO EXCLUSION ABOVE t=chi7'}


# Exact affine coordinates inherited from GERM-75, gamma=1.
af,add,sub,val,vertices=parent.af,parent.add,parent.sub,parent.val,parent.vertices
scale,audit=parent.scale,parent.audit
seed,t,chi,psi,sigma=g86.seed,g86.t,g86.chi,g86.psi,g86.sigma
rho,c,RANGE=g86.rho,g86.c,parent.RANGE
nu=sub(chi,scale(2,psi));d=sub(t,scale(2,psi));zero=af()


def eighth_req(key,z):
    n=2 if key=='A' else 3;q=add(z,sub(chi,scale(n,psi)))
    m=[('z>0',z),('z<psi',sub(psi,z)),('q>0',q),('q<psi',sub(psi,q)),
       ('lower_global_scope',d),('upper_global_scope',sub(nu,d)),
       ('eighth_cut',sub(sigma,z) if n==2 else sub(z,sigma))]
    if key=='D':m.append(('first_intermediate_exterior',sub(z,add(sigma,d))))
    if key=='E':m.append(('first_intermediate_interior',sub(add(sigma,d),z)))
    return q,m


def eighth_lift(key,z):
    q,m=eighth_req(key,z);w=EIGHTH[key];n=len(w)
    pp=[z]+[add(z,sub(chi,scale(j,psi))) for j in range(1,n+1)]
    assert pp[-1]==q
    for j,k in enumerate(w):
        out,lower=g81.seventh_req(k,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_eighth_hit_{j}',sub(out,psi) if j<n-1 else sub(psi,out)))
    return q,m


def ninth_req(s,n,y):
    q=add(y,sub(psi,scale(n,sigma)))
    m=[('y>0',y),('y<sigma',sub(sigma,y)),('q>0',q),('q<sigma',sub(sigma,q)),
       ('lower_global_scope',d),('upper_global_scope',sub(nu,d)),
       ('ninth_cut',sub(c,y) if n==3 else sub(y,c))]
    if s==0:m.append(('no_E_source',sub(q,d)))
    else:m += [('last_E_source',sub(d,add(q,scale(s-1,sigma)))),
               ('first_D_source',sub(add(q,scale(s,sigma)),d))]
    return q,m


def ninth_lift(s,n,y):
    q,m=ninth_req(s,n,y);w=WORDS[s,n]
    pp=[y]+[add(y,sub(psi,scale(j,sigma))) for j in range(1,n+1)]
    assert pp[-1]==q
    for j,k in enumerate(w):
        out,lower=eighth_req(k,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_ninth_hit_{j}',sub(out,sigma) if j<n-1 else sub(sigma,out)))
    return q,m


def geometry_audit():
    lower_levels={}
    # The seventh upper face t=chi is proved from sixth equations here.
    for label,lib,req,lift in (
        ('sixth',g81.ATOMS,g81.atom_req,g81.atom_lift),
        ('seventh',g81.SEVENTH,g81.seventh_req,g81.seventh_lift)):
        cells={}
        for key in lib:
            _,rr=req(key,seed);_,m=lift(key,seed)
            cond=RANGE+tuple(v for _,v in rr)
            item=audit(m,vertices(cond))
            if label=='sixth' or key in ('U1','V1'):
                item['t_equals_chi7_endpoint']=audit(m,vertices(cond+(sub(t,chi),sub(chi,t))))
            cells[key]=item
        lower_levels[label]=cells
    cells8={}
    for key in EIGHTH:
        _,rr=eighth_req(key,seed);_,m=eighth_lift(key,seed)
        cond=RANGE+tuple(v for _,v in rr);item=audit(m,vertices(cond))
        if key in ('A','D'):
            item['d_equals_zero_entry']=audit(m,vertices(cond+(sub(zero,d),)))
        if key in ('A','E'):
            item['d_equals_nu8_endpoint']=audit(m,vertices(cond+(sub(d,nu),)))
        cells8[key]=item
    cells9={}
    for s,n in WORDS:
        _,rr=ninth_req(s,n,seed);_,m=ninth_lift(s,n,seed)
        cond=RANGE+tuple(v for _,v in rr);item=audit(m,vertices(cond))
        if s==0:item['d_equals_zero_entry']=audit(m,vertices(cond+(sub(zero,d),)))
        if s==n-1:item['d_equals_nu8_endpoint']=audit(m,vertices(cond+(sub(d,nu),)))
        if s in (1,2):
            item[f'd_equals_{s}_sigma8_junction']=audit(m,vertices(cond+(sub(d,scale(s,sigma)),sub(scale(s,sigma),d))))
        cells9[f'{s}/{n}']=item
    assert add(c,rho)==sigma and add(scale(3,c),scale(4,rho))==psi
    assert nu==sub(psi,sigma) and add(scale(3,sub(chi,psi)),scale(5,psi))==g81.xi
    # Above t=chi, a later N=19 sixth source changes A19 -> E19.
    excess=sub(t,chi);pp=g77.g76.seventh_positions(5,seed);m=[]
    for j,key in enumerate(NEXT):
        out,lower=g81.atom_req(key,pp[j]);assert out==pp[j+1]
        m += [(f'next{j}:{name}',v) for name,v in lower]
        m.append((f'next_no_early_seventh_hit_{j}',sub(scale(2,g81.eta),out) if j<4 else sub(out,scale(2,g81.eta))))
    q=sub(pp[-1],scale(2,g81.eta));assert q==add(seed,sub(chi,psi))
    m += [('next_target_low',q),('next_target_high',sub(chi,q))]
    cond=RANGE+(excess,sub(psi,excess),seed,sub(excess,seed))
    guard=audit(m,vertices(cond))
    return {'parameter':'d=e-e88=t-2psi7','new_exclusion_scope':'0<d<=nu8, equivalently 2psi7<t<=chi7',
            'rechecked_lower_contracts':lower_levels,'three_eighth_cells':cells8,
            'seven_ninth_cells':cells9,'ninth_map':'y -> y+rho9 mod sigma8',
            'images':'(rho9,sigma8) and (0,rho9)',
            'endpoint_seventh_maps':['U1','V1; GERM-81-local'],
            'endpoint_eighth_maps':['A','E; GERM-89-local'],
            'endpoint_ninth_words':['E^2 A','E^3 A; GERM-89-local'],
            'physical_field':'W(t0+y); t0=h-beta+gamma-xi+2eta7',
            'next_domain':'t=chi7+excess; 0<z<excess<psi7',
            'next_seventh_sixth_word':NEXT,'next_guard':guard,'sampled_topology':False}


def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-89','standing':'UNRATIFIED',
         'entry_commit':'71199c7def07f58da2785ed5c2e97772805fdfb1',
         'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
         'new_exclusion_scope':'2psi7<t<=chi7, t=e-e80; L88<L<=L80+chi7',
         'matrix_namespace':'A/D/E are GERM-89-local; input U/V and sixth atoms are GERM-81-local',
         'eighth_word_dictionary':EIGHTH,
         'ninth_word_dictionary':{f'{s}/{n}':w for (s,n),w in WORDS.items()},
         'arithmetic':arithmetic(),'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
         'full_lower_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
         'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
