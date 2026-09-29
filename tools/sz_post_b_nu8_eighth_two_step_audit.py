#!/usr/bin/env python3
"""GERM-93: post-b=nu8 two-step transfer, direct ninth exclusion.

New exclusion 0<r<=nu8, r=e-e92. Four eighth formulas hold on the larger
0<r<=psi7 domain. Four low and five high ninth cells (seven distinct words)
have two fixed-parameter rational cone charts with common factor 7/2.
Every intermediate source is checked. Run with assertions enabled.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of the certificate; run without -O.'
ROOT=Path(__file__).resolve().parents[1]
PIN_PATH='tools/sz_seventh_double_f20_nonwrap_audit.py'
PIN_SHA='54e831e0db0573252b48b1aec1ca758f223dd0cf1e83a447610478551f22bd42'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest()==PIN_SHA
import sz_seventh_double_f20_nonwrap_audit as parent
g91,g75,g77,old=parent.parent,parent.g75,parent.g77,parent.old
product,det=parent.product,parent.det
# Seventh inputs are GERM-91-local. Eighth labels below are GERM-93-local.
EIGHTH={'A0':['V3','U1'], 'A1':['V3','U2'],
        'B0':['V3','U1','U2'], 'B1':['V3','U2','U2']}
LOW={(i,n):[f'A{i}']+['B0']*(n-1) for n in (3,4) for i in (0,1)}
HIGH={(s,n):['A1']+['B0']*(n-s-1)+['B1']*s
      for s,n in ((0,3),(1,3),(0,4),(1,4),(2,4))}
CHART_LOW=[[1,1],[-4,-3]]
CHART_HIGH=[[1,1],[-4,5]]
FACTOR=F(7,2)
NEXT=['A1','B1','B1']


def arithmetic():
    add,sub,mul=old.add,old.sub,old.mul
    h,k=(-4,4,-1),(4,-1,-1)
    kap=sub(k,mul(5,h));tau=sub(h,mul(5,kap));th=sub(kap,mul(8,tau))
    alpha=sub(tau,mul(3,th));beta=sub(th,alpha);gamma=sub(alpha,beta)
    xi=sub(mul(5,gamma),beta);om=sub(gamma,mul(19,xi))
    eta=sub(xi,om);chi=sub(mul(2,om),xi);psi=sub(eta,chi)
    sigma=sub(mul(3,psi),chi);nu=sub(chi,mul(2,psi))
    rho=sub(psi,mul(3,sigma));c=sub(sigma,rho)
    L92=(2548608,-2240070,431461);L93=add(L92,nu)
    top=add((4,-1,0),mul(3,h));formula_top=add(L92,psi)
    assert L93==(8924844,-7844400,1510916)
    assert L93==add((4,-1,0),add(mul(-1871063,h),mul(360147,k)))
    assert formula_top==(152396,-133943,25798)
    assert sub(formula_top,L93)==sigma
    assert nu==(6376236,-5604330,1079455)
    assert add(sigma,nu)==psi and add(mul(2,sigma),mul(3,nu))==chi
    assert add(c,rho)==sigma and add(mul(3,c),mul(4,rho))==psi
    assert nu==add(mul(2,sigma),rho)
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(v):return sum((n*l for n,l in zip(v,logs)),old.box(0))
    checks={'sigma_positive':sigma,'rho_positive_3sigma_lt_psi':rho,
            'c_positive_psi_lt_4sigma':c,'nu_gt_sigma':sub(nu,sigma),
            'formula_endpoint_below_three_layers':sub(top,formula_top),
            'formula_margin_at_exclusion_endpoint':sigma}
    boxes={k:enc(v) for k,v in checks.items()};assert all(v.lo>0 for v in boxes.values())
    return {'rational_log_order_checks':{k:g77.show_box(v,38) for k,v in boxes.items()},
            'endpoint_prime_log_vector':L93,'endpoint_h_k_vector':[-1871063,360147],
            'endpoint_decimal':g77.show_box(enc(L93),38),
            'increment':'nu8=chi7-2psi7','increment_prime_log_vector':nu,
            'increment_decimal':g77.show_box(enc(nu),38),
            'formula_endpoint_prime_log_vector':formula_top,
            'remaining_parent_formula_width':g77.show_box(enc(sigma),38),
            'remaining_three_layer_width':g77.show_box(enc(sub(top,L93)),38),
            'tower_identities':['2sigma8+3nu8=chi7','3c10+4rho9=psi7']}


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
    eight={k:product(w,seven) for k,w in EIGHTH.items()}
    count8={k:sum(count7[a] for a in w) for k,w in EIGHTH.items()}
    assert count8=={'A0':257302,'A1':257302,'B0':353997,'B1':353997}
    assert EIGHTH['A0']==parent.EIGHTH['A'] and EIGHTH['B0']==parent.EIGHTH['E']
    assert EIGHTH['A1']==parent.NEXT
    for m in eight.values():
        dd=det(m);assert dd.lo>0 and dd.lo<=1<=dd.hi
    a1=eight['A1'];tr=a1[0][0]+a1[1][1];assert (tr*tr-4*det(a1)).hi<0
    for C,expected in ((CHART_LOW,F(1)),(CHART_HIGH,F(9))):
        assert F(C[0][0])*F(C[1][1])-F(C[0][1])*F(C[1][0])==expected
    cert={}
    for label,lib,C in (('low',LOW,CHART_LOW),('high',HIGH,CHART_HIGH)):
        rows={}
        for pair,w in lib.items():
            m=product(w,eight);sign=(-1 if pair[0]==1 else 1) if label=='low' else -1
            item=g77.cone_test(m,C,sign,FACTOR)
            dd=det(m);tr=m[0][0]+m[1][1];assert (tr*tr-4*dd).lo>0
            count=sum(count8[x] for x in w);assert count==257302+(pair[1]-1)*353997
            item.update({'eighth_word':w,'original_step_count':count,'determinant_rho_exponent':0})
            rows[f'{pair[0]}/{pair[1]}']=item
        cert[label]=rows
    distinct={tuple(w) for w in list(LOW.values())+list(HIGH.values())};assert len(distinct)==7
    for n in (3,4):assert LOW[1,n]==HIGH[0,n]
    m=product(NEXT,eight);tr=m[0][0]+m[1][1];dd=det(m);disc=tr*tr-4*dd
    assert dd.lo>0 and dd.lo<=1<=dd.hi and disc.hi<0
    assert F(-1)<tr.lo<tr.hi<F(-9,10)
    return {'physical_recalculation':'FRESH PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
            'precision':{'grid':'10^120','log_series_terms':400},'layer_pivots':pivots,
            'GERM71_box_regression':'CONTAINED; not rounded proof inputs',
            'charts':{'low':CHART_LOW,'high':CHART_HIGH},'chart_determinants':['1','9'],
            'common_forward_backward_factor':'7/2','nine_chart_tests':cert,
            'distinct_temporal_words':7,'shared_words':2,
            'input_A1_status':'ELLIPTIC; retained in complete ninth returns',
            'next_eighth_word':NEXT,'next_matrix':'B1^2 A1, GERM-93-local eighth maps',
            'next_trace':old.display_matrix([[tr]]),'next_determinant':old.display_matrix([[dd]]),
            'next_discriminant':old.display_matrix([[disc]]),'next_status':'ELLIPTIC COMPLETE THREE-STEP NINTH RETURN',
            'tenth_or_deeper_induction_used':False,'new_retained_coordinates':0}


# Exact affine coordinates normalized by gamma, inherited from GERM-91.
af,add,sub,vertices=parent.af,parent.add,parent.sub,parent.vertices
scale,audit=parent.scale,parent.audit
seed,psi,chi,sigma,nu=parent.seed,parent.psi,parent.chi,parent.sigma,parent.nu
RANGE=parent.RANGE;zero=af();r=sub(parent.b,nu)
rho=sub(psi,scale(3,sigma));c=sub(sigma,rho)


def eighth_req(key,z):
    n=2 if key.startswith('A') else 3;q=add(z,sub(chi,scale(n,psi)))
    m=[('z>0',z),('z<psi',sub(psi,z)),('q>0',q),('q<psi',sub(psi,q)),
       ('eighth_lower_global_scope',r),('eighth_upper_global_scope',sub(psi,r)),
       ('eighth_cut',sub(sigma,z) if n==2 else sub(z,sigma)),
       ('first_intermediate_bit',sub(r,z) if key.endswith('1') else sub(z,r))]
    return q,m


def eighth_lift(key,z):
    q,m=eighth_req(key,z);w=EIGHTH[key];n=len(w)
    pp=[z]+[add(z,sub(chi,scale(j,psi))) for j in range(1,n+1)]
    assert pp[-1]==q
    for j,k in enumerate(w):
        out,lower=g91.seventh_req(k,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_eighth_hit_{j}',sub(out,psi) if j<n-1 else sub(psi,out)))
    return q,m


def ninth_word_lift(word,y):
    n=len(word);assert n in (3,4)
    pp=[y]+[add(y,sub(psi,scale(j,sigma))) for j in range(1,n+1)]
    q=pp[-1]
    m=[('y>0',y),('y<sigma',sub(sigma,y)),('q>0',q),('q<sigma',sub(sigma,q)),
       ('ninth_cut',sub(c,y) if n==3 else sub(y,c))]
    for j,k in enumerate(word):
        out,lower=eighth_req(k,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_ninth_hit_{j}',sub(out,sigma) if j<n-1 else sub(sigma,out)))
    return q,m


def geometry_audit():
    lower=g91.geometry_audit() # includes sixth/fifth and all seven seventh formulas, endpoints
    restricted={}
    for k in ('U1','U2','V3'):
        _,rr=g91.seventh_req(k,seed);_,m=g91.seventh_lift(k,seed)
        cond=RANGE+(r,sub(psi,r))+tuple(v for _,v in rr)
        item=audit(m,vertices(cond))
        if k in ('U2','V3'):item['r_psi_formula_endpoint']=audit(m,vertices(cond+(sub(r,psi),)))
        restricted[k]=item
    cells8={}
    for k in EIGHTH:
        _,rr=eighth_req(k,seed);_,m=eighth_lift(k,seed)
        cond=RANGE+tuple(v for _,v in rr);item=audit(m,vertices(cond))
        if k in ('A0','B0'):item['r_zero_entry']=audit(m,vertices(cond+(sub(zero,r),)))
        if k in ('A1','B1'):item['r_psi_formula_endpoint']=audit(m,vertices(cond+(sub(r,psi),)))
        cells8[k]=item
    cells_low={}
    for (i,n),w in LOW.items():
        _,m=ninth_word_lift(w,seed)
        cond=RANGE+(r,sub(sigma,r),seed,sub(sigma,seed),
                    sub(r,seed) if i else sub(seed,r),sub(c,seed) if n==3 else sub(seed,c))
        item=audit(m,vertices(cond))
        if i==0:item['r_zero_entry']=audit(m,vertices(cond+(sub(zero,r),)))
        if i==1:item['r_sigma_junction']=audit(m,vertices(cond+(sub(r,sigma),)))
        cells_low[f'{i}/{n}']=item
    cells_high={}
    for (s,n),w in HIGH.items():
        q,m=ninth_word_lift(w,seed)
        cond=RANGE+(sub(r,sigma),sub(nu,r),seed,sub(sigma,seed),q,sub(sigma,q),
                    sub(c,seed) if n==3 else sub(seed,c))
        cond += (sub(add(q,sigma),r),) if s==0 else (
            sub(r,add(q,scale(s,sigma))),sub(add(q,scale(s+1,sigma)),r))
        item=audit(m,vertices(cond))
        if s==0:item['r_sigma_junction']=audit(m,vertices(cond+(sub(sigma,r),)))
        if (s,n) in ((1,3),(2,4)):item['r_nu_exclusion_endpoint']=audit(m,vertices(cond+(sub(r,nu),)))
        if s==1:item['r_2sigma_junction']=audit(m,vertices(cond+(sub(r,scale(2,sigma)),sub(scale(2,sigma),r))))
        cells_high[f'{s}/{n}']=item
    assert add(sigma,nu)==psi and add(scale(2,sigma),scale(3,nu))==chi
    assert add(c,rho)==sigma and add(scale(3,c),scale(4,rho))==psi
    assert nu==add(scale(2,sigma),rho)
    assert sub(g91.omega,add(g91.limit,add(nu,r)))==sub(psi,r)
    # First newly active all-B1 three-step return, within the licensed formula domain.
    excess=sub(r,nu);q,m=ninth_word_lift(NEXT,seed)
    assert q==add(seed,rho)
    cond=RANGE+(excess,sub(c,excess),seed,sub(excess,seed))
    guard=audit(m,vertices(cond))
    return {'parameter':'r=b-nu8=e-e92, b=e-e91',
            'eighth_formula_scope':'0<r<=psi7; inherited sixth/seventh endpoint included',
            'new_exclusion_scope':'0<r<=nu8','rechecked_parent_geometry':lower,
            'three_restricted_seventh_cells':restricted,'four_eighth_formula_cells':cells8,
            'four_low_ninth_cells':cells_low,'five_high_ninth_cells':cells_high,
            'ninth_map':'y -> y+rho9 mod sigma8','images':'(rho9,sigma8) and (0,rho9)',
            'physical_field':'W(t0+y); t0=h-beta+gamma-xi+2eta7',
            'exclusion_endpoint_words':['B1 B0 A1','B1^2 B0 A1'],
            'formula_endpoint_maps':['A1','B1'],
            'next_domain':'r=nu8+excess; 0<y<excess<c10','next_eighth_word':NEXT,
            'next_guard':guard,'sampled_topology':False}


def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-93','standing':'UNRATIFIED',
         'entry_commit':'632fde680e614faf9601942e84e09e27bcea10b6',
         'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
         'matrix_namespace':'U1/U2/V3 are GERM-91-local; A0/A1/B0/B1 are GERM-93-local',
         'eighth_word_dictionary':EIGHTH,
         'low_ninth_words':{f'{i}/{n}':w for (i,n),w in LOW.items()},
         'high_ninth_words':{f'{s}/{n}':w for (s,n),w in HIGH.items()},
         'arithmetic':arithmetic(),'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
         'full_lower_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
         'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
