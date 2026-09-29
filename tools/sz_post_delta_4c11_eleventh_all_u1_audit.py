#!/usr/bin/env python3
"""GERM-96: all-U1 eleventh control and closure of the sixth formula window.

Proves 0<b<=omega11, b=e-e95. Three eleventh maps and four complete
12th returns share one signed rational chart with factor 2000. All
intermediate sources and the full parent endpoint are checked. No
13th induction or additional retained coordinate is used. Run without -O.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of the certificate; run without -O.'
ROOT=Path(__file__).resolve().parents[1]
PIN_PATH='tools/sz_post_eps_rho9_tenth_all_s_audit.py'
PIN_SHA='ba86da8cf1213d210e7c8fe52b6865919dfcf11af8cfdbc0d68e8502ccd9d348'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest()==PIN_SHA
import sz_post_eps_rho9_tenth_all_s_audit as parent
g94,g93,g91,g75,g77,old=parent.parent,parent.g93,parent.g91,parent.g75,parent.g77,parent.old
product,det=parent.product,parent.det
# U/V inputs are GERM-95-local tenth maps. A/D/E below are GERM-96-local.
ELEVENTH={'A':['V1']+['U1']*3, 'D':['V1','U0']+['U1']*3, 'E':['V1']+['U1']*4}
TWELFTH={(key,n):['A']*(n-1)+[key] for n in (10,11) for key in ('D','E')}
CHART=[[1,1],[-1,3]]
FACTOR=F(2000)
NEXT_PAIR=(16,19)


def arithmetic():
    add,sub,mul=old.add,old.sub,old.mul
    h,k=(-4,4,-1),(4,-1,-1)
    kap=sub(k,mul(5,h));tau=sub(h,mul(5,kap));th=sub(kap,mul(8,tau))
    alpha=sub(tau,mul(3,th));beta=sub(th,alpha);gamma=sub(alpha,beta)
    xi=sub(mul(5,gamma),beta);omega=sub(gamma,mul(19,xi))
    eta=sub(xi,omega);chi=sub(mul(2,omega),xi);psi=sub(eta,chi)
    sigma=sub(mul(3,psi),chi);rho=sub(psi,mul(3,sigma));c=sub(sigma,rho)
    om10=sub(sigma,mul(10,c));ell=sub(c,om10);w=sub(c,mul(4,ell))
    r12=sub(ell,mul(10,w));om12=sub(w,r12)
    L95=(-1370581752,1204659372,-232030517);L96=add(L95,w)
    top=add((4,-1,0),mul(3,h))
    assert L96==(152396,-133943,25798)
    assert L96==add((4,-1,0),add(mul(-31948,h),mul(6150,k)))
    assert L96==add((-619016,544082,-104797),omega)
    assert w==(1370734148,-1204793315,232056315)
    assert r12==(-14058198412,12356315404,-2379960931)
    assert om12==(15428932560,-13561108719,2612017246)
    assert add(mul(4,ell),w)==c and add(mul(10,w),r12)==ell
    assert add(mul(10,om12),mul(11,r12))==ell
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(v):return sum((a*l for a,l in zip(v,logs)),old.box(0))
    checks={'omega11_positive':w,'10omega11_lt_c11':r12,'c11_lt_11omega11':om12,
            'guard_width_below_sixth_cut':sub(eta,w),
            'guard_exterior_separation':sub(sub(sub(gamma,mul(16,xi)),omega),w),
            'endpoint_below_three_layers':sub(top,L96)}
    boxes={k:enc(v) for k,v in checks.items()};assert all(x.lo>0 for x in boxes.values())
    return {'rational_log_order_checks':{k:g77.show_box(v,38) for k,v in boxes.items()},
            'endpoint_prime_log_vector':L96,'endpoint_h_k_vector':[-31948,6150],
            'endpoint_decimal':g77.show_box(enc(L96),38),'increment':'omega11',
            'increment_prime_log_vector':w,'increment_decimal':g77.show_box(enc(w),38),
            'rho12_prime_log_vector':r12,'omega12_prime_log_vector':om12,
            'completed_parent_formula_width':'ZERO',
            'remaining_three_layer_width':g77.show_box(enc(sub(top,L96)),38),
            'tower_identity':'10(omega11-rho12)+11rho12=c11'}


def rational_audit():
    assert old.SCALE==10**120
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
    counts={}
    for k,pair in g91.ATOMS.items():
        ow=g75.to_original(g75.sixth_word(*pair))
        assert legacy.determinant_exponent(ow)==0
        counts[k]=len(ow);assert counts[k]==1654*pair[1]-297
    maps=atoms
    for words in (g91.SEVENTH,g93.EIGHTH,g94.NINTH,parent.TENTH,ELEVENTH):
        maps={k:product(w,maps) for k,w in words.items()}
        counts={k:sum(counts[a] for a in w) for k,w in words.items()}
        for m in maps.values():
            dd=det(m);assert dd.lo>0 and dd.lo<=1<=dd.hi
    assert counts=={'A':55313611,'D':69471837,'E':69471837}
    assert ELEVENTH['A']==parent.HIGH[3,4]
    assert ELEVENTH['D']==parent.HIGH[3,5] and ELEVENTH['E']==parent.NEXT
    spectra={}
    for k,m in maps.items():
        tr=m[0][0]+m[1][1];disc=tr*tr-4*det(m)
        assert disc.hi<0 if k=='E' else disc.lo>0
        spectra[k]={'trace':old.display_matrix([[tr]]),'discriminant':old.display_matrix([[disc]])}
    assert F(CHART[0][0])*CHART[1][1]-F(CHART[0][1])*CHART[1][0]==4
    cert={}
    for (key,n),w in TWELFTH.items():
        m=product(w,maps);tr=m[0][0]+m[1][1]
        item=g77.cone_test(m,CHART,(-1)**(n+1),FACTOR)
        assert (tr*tr-4*det(m)).lo>0
        count=sum(counts[a] for a in w);assert count==55313611*(n-1)+69471837
        item.update({'eleventh_word':w,'original_step_count':count,'determinant_rho_exponent':0})
        cert[f'{key}/{n}']=item
    nw=g75.sixth_word(*NEXT_PAIR);m=product(nw,fifth)
    ow=g75.to_original(nw);assert legacy.determinant_exponent(ow)==0 and len(ow)==31129
    tr=m[0][0]+m[1][1];dd=det(m);disc=tr*tr-4*dd
    assert dd.lo>0 and dd.lo<=1<=dd.hi and disc.hi<0 and F(-89,100)<tr.lo<tr.hi<F(-88,100)
    return {'physical_recalculation':'FRESH PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
            'precision':{'grid':'10^120','log_series_terms':400},'layer_pivots':pivots,
            'GERM71_box_regression':'CONTAINED; not rounded proof inputs','eleventh_spectra':spectra,
            'chart':CHART,'chart_determinant':'4','sign_rule':'(-1)^(N+1)',
            'common_forward_backward_factor':'2000','four_twelfth_certificates':cert,
            'next_sixth_atom':'B16,19','next_fifth_word':nw,
            'next_trace':old.display_matrix([[tr]]),'next_determinant':old.display_matrix([[dd]]),
            'next_discriminant':old.display_matrix([[disc]]),
            'next_status':'ELLIPTIC NEW SIXTH SOURCE ATOM; NO EXCLUSION BEYOND PARENT WINDOW'}


# Exact affine coordinates, gamma=1, inherited from the source-domain stack.
af,add,sub,vertices=parent.af,parent.add,parent.sub,parent.vertices
scale,audit=parent.scale,parent.audit
seed,delta,ell,w,cut11=parent.seed,parent.delta,parent.ell,parent.om11,parent.cut11
zero=af();b=sub(delta,scale(4,ell));r12=sub(ell,scale(10,w));om12=sub(w,r12)
RANGE=parent.RANGE+(r12,om12)


def eleventh_req(key,y):
    small=key=='A';q=add(y,w) if small else sub(y,cut11)
    m=[('y>0',y),('y<c11',sub(ell,y)),('q>0',q),('q<c11',sub(ell,q)),
       ('eleventh_lower_global_scope',b),('eleventh_upper_global_scope',sub(w,b)),
       ('eleventh_cut',sub(cut11,y) if small else sub(y,cut11))]
    if key!='A':m.append(('first_later_bit',sub(b,q) if key=='E' else sub(q,b)))
    return q,m


def eleventh_lift(key,y):
    q,m=eleventh_req(key,y);out,lower=parent.eleventh_lift(ELEVENTH[key],y);assert out==q
    return q,m+[(f'tenth:{name}',v) for name,v in lower]


def twelfth_lift(key,n,y):
    word=TWELFTH[key,n];pp=[add(y,scale(j,w)) for j in range(n)]
    q=sub(add(y,scale(n,w)),ell);pp.append(q)
    m=[('y>0',y),('y<omega11',sub(w,y)),('q>0',q),('q<omega11',sub(w,q)),
       ('twelfth_cut',sub(y,r12) if n==10 else sub(r12,y))]
    for j,k in enumerate(word):
        out,lower=eleventh_req(k,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_twelfth_hit{j}',sub(out,w) if j<n-1 else sub(w,out)))
    return q,m


def geometry_audit():
    lower=parent.geometry_audit() # rechecks lower contracts and their complete formula endpoints
    cells11={}
    for key in ELEVENTH:
        _,rr=eleventh_req(key,seed);_,m=eleventh_lift(key,seed)
        cond=RANGE+tuple(v for _,v in rr);item=audit(m,vertices(cond))
        if key in ('A','D'):item['b_zero_entry']=audit(m,vertices(cond+(sub(zero,b),)))
        if key in ('A','E'):item['b_omega11_endpoint']=audit(m,vertices(cond+(sub(b,w),)))
        cells11[key]=item
    cells12={}
    for key,n in TWELFTH:
        q,m=twelfth_lift(key,n,seed)
        cond=RANGE+(b,sub(w,b),seed,sub(w,seed),q,sub(w,q),
                    sub(b,q) if key=='E' else sub(q,b))
        item=audit(m,vertices(cond))
        face=sub(b,w) if key=='E' else sub(zero,b)
        item['b_omega11_endpoint' if key=='E' else 'b_zero_entry']=audit(m,vertices(cond+(face,)))
        if (key,n) in (('E',10),('D',11)):
            item['b_omega12_junction']=audit(m,vertices(cond+(sub(b,om12),sub(om12,b))))
        cells12[f'{key}/{n}']=item
    assert add(scale(4,ell),w)==parent.c
    assert add(scale(10,w),r12)==ell and add(om12,r12)==w
    assert add(scale(10,om12),scale(11,r12))==ell
    assert sub(g91.d,g91.omega)==sub(b,w)
    # New sixth atom immediately beyond the completed parent window.
    excess=sub(b,w);q,m=g75.sixth_lift(*NEXT_PAIR,seed)
    assert q==add(seed,g91.omega)
    assert sub(g75.zeta,scale(15,g91.xi))==g91.d
    cond=RANGE+(excess,sub(w,excess),seed,sub(excess,seed))
    guard=audit(m,vertices(cond))
    return {'parameter':'b=delta-4c11=e-e95; delta=e-e94',
            'new_exclusion_scope':'0<b<=omega11','rechecked_parent_geometry':lower,
            'three_eleventh_cells':cells11,'four_twelfth_cells':cells12,
            'twelfth_section':'(0,omega11) in the eleventh circle',
            'twelfth_map':'y -> y-rho12 mod omega11',
            'twelfth_images':'(0,omega12) and (omega12,omega11)',
            'tower_identity':'10omega12+11rho12=c11',
            'physical_field':'W(t0+y); t0=h-beta+gamma-xi+2eta7',
            'endpoint_words':['E A^9','E A^10'],
            'completed_parent_window':'GERM91 d=omega, GERM93 r=psi7, GERM94 epsilon=sigma8, GERM95 delta=c10',
            'next_domain':'GERM91 d=omega+excess; 0<y<excess<omega11',
            'next_sixth_atom':'B16,19','next_guard':guard,'sampled_topology':False}


def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-96','standing':'UNRATIFIED',
         'entry_commit':'f9b087a2289ee52be4c13e5f8a3677d756c21e37',
         'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
         'matrix_namespace':'tenth U/V are GERM-95-local; eleventh A/D/E are GERM-96-local',
         'eleventh_word_dictionary':ELEVENTH,
         'twelfth_word_dictionary':{f'{key}/{n}':v for (key,n),v in TWELFTH.items()},
         'arithmetic':arithmetic(),'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
         'thirteenth_or_deeper_induction_used':False,'new_retained_coordinates':0,
         'full_lower_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
         'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
