#!/usr/bin/env python3
"""GERM-85: all-internal tenth visits; close the remaining eighth window.

Scope: rho9<b<=sigma8, b=e-e83. Four tenth source-bit maps on this
entire strip give eleven distinct complete eleventh words. One signed
rational cone chart certifies factor 5/2. The b=sigma8 endpoint is checked
from the inherited lower domains, not by continuity. Run without -O.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of the certificate; run without -O.'
ROOT=Path(__file__).resolve().parents[1]
PIN_PATH='tools/sz_post_psi7_ninth_double_visit_audit.py'
PIN_SHA='7bb3f91f9a99ff741438763e9c9541820f78afc0560cc828f105ca765ddb1558'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest()==PIN_SHA
import sz_post_psi7_ninth_double_visit_audit as parent
g83,g81,g77,g75,old=parent.parent,parent.g81,parent.g77,parent.g75,parent.old
product,det=parent.product,parent.det
# The pinned stack freshly recomputes on grid 10^120 with 400 log terms.
TENTH={'V0':['Q','R']+['S']*8, 'V1':['Q']+['S']*9,
       'U0':['Q','R']+['S']*9, 'U1':['Q']+['S']*10}
LOW={(i,n):['V1' if i else 'V0']+['U0']*(n-1)
     for n in (4,5) for i in (0,1)}
HIGH={(s,n):['V1']+['U0']*(n-s-1)+['U1']*s
      for n in (4,5) for s in range(n)}
assert len(LOW)==4 and len(HIGH)==9
assert len({tuple(w) for w in list(LOW.values())+list(HIGH.values())})==11
CHART=[[1,1],[F(-53,25),F(-199,100)]]
FACTOR=F(5,2)
GUARD=['V1','U1']  # GERM-81-local seventh maps, not the new tenth names.

def arithmetic():
    add,sub,mul=old.add,old.sub,old.mul
    h=(-4,4,-1);k=(4,-1,-1)
    kap=sub(k,mul(5,h));tau=sub(h,mul(5,kap));theta=sub(kap,mul(8,tau))
    alpha=sub(tau,mul(3,theta));beta=sub(theta,alpha);gamma=sub(alpha,beta)
    xi=sub(mul(5,gamma),beta);omega=sub(gamma,mul(19,xi))
    eta=sub(xi,omega);chi=sub(mul(2,omega),xi);psi=sub(eta,chi)
    sigma=sub(mul(3,psi),chi);rho=sub(psi,mul(3,sigma));c=sub(sigma,rho)
    om10=sub(sigma,mul(10,c));ell=sub(c,om10);om11=sub(c,mul(4,ell))
    cut=sub(ell,om11)
    L83=(12945856,-11378629,2191647);L84=add(L83,rho);L85=add(L84,c)
    assert L84==(36866988,-32403873,6241338)
    assert L85==add(L83,sigma)
    assert L85==add((193384,-169969,32737),sub(chi,psi))
    eh=add(mul(-874940,h),mul(168411,k))
    assert L85==add((4,-1,0),eh)
    assert add(rho,c)==sigma
    assert add(mul(4,cut),mul(5,om11))==c
    top=add((4,-1,0),mul(3,h))
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(v):return sum((n*l for n,l in zip(v,logs)),old.box(0))
    checks={'increment_c10_positive':c,'c11_positive':ell,'c10_gt_4c11':om11,
            'c10_lt_5c11':cut,'endpoint_below_seventh_formula_bound':psi,
            'next_guard_inside_seventh_scope':sub(psi,sigma),
            'endpoint_below_three_layers':sub(top,L85)}
    boxes={key:enc(v) for key,v in checks.items()}
    assert all(x.lo>0 for x in boxes.values())
    return {'rational_log_order_checks':{key:g77.show_box(x,38) for key,x in boxes.items()},
            'endpoint_prime_log_vector':L85,'endpoint_h_k_vector':[-874940,168411],
            'endpoint_decimal':g77.show_box(enc(L85),34),
            'increment_prime_log_vector':c,'increment_decimal':g77.show_box(enc(c),38),
            'c11_prime_log_vector':ell,'omega11_prime_log_vector':om11,
            'c11_decimal':g77.show_box(enc(ell),38),
            'omega11_decimal':g77.show_box(enc(om11),38),
            'remaining_three_layer_width':g77.show_box(enc(sub(top,L85)),38),
            'eighth_formula_window_remaining':'ZERO; endpoint included',
            'eleventh_tower_identity':'4(c11-omega11)+5omega11=c10'}

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
    counts6={}
    for key,(s,n) in g81.ATOMS.items():
        ow=g75.to_original(g75.sixth_word(s,n))
        assert legacy.determinant_exponent(ow)==0
        assert len(ow)==1654*n-297;counts6[key]=len(ow)
    seven={k:product(w,atoms) for k,w in g81.SEVENTH.items()}
    eight={k:product(w,seven) for k,w in g83.EIGHTH.items()}
    nine={k:product(w,eight) for k,w in parent.NINTH.items()}
    ten={k:product(w,nine) for k,w in TENTH.items()}
    c7={k:sum(counts6[x] for x in w) for k,w in g81.SEVENTH.items()}
    c8={k:sum(c7[x] for x in w) for k,w in g83.EIGHTH.items()}
    c9={k:sum(c8[x] for x in w) for k,w in parent.NINTH.items()}
    c10={k:sum(c9[x] for x in w) for k,w in TENTH.items()}
    assert c10=={'V0':12838933,'V1':12838933,'U0':14158226,'U1':14158226}
    for lib in (atoms,seven,eight,nine,ten):
        for B in lib.values():
            dd=det(B);assert dd.lo>0 and dd.lo<=1<=dd.hi
    assert TENTH['V0']==parent.HIGH[(8,10)]
    assert TENTH['U0']==parent.HIGH[(9,11)]
    assert TENTH['V1']==parent.GUARD
    atomdata={}
    for key,B in ten.items():
        tr=B[0][0]+B[1][1];dd=det(B);disc=tr*tr-4*dd
        assert disc.hi<0 if key.endswith('1') else disc.lo>0
        atomdata[key]={'ninth_word':TENTH[key],'matrix':old.display_matrix(B),
                       'trace':old.display_matrix([[tr]]),'discriminant':old.display_matrix([[disc]])}
    words={f'out/{n}':LOW[(0,n)] for n in (4,5)}
    words.update({f'{s}/{n}':w for (s,n),w in HIGH.items()})
    cert={}
    for key,w in words.items():
        n=len(w)
        if key.startswith('out'):sign=1
        else:
            s=int(key.split('/')[0]);sign=(-1)**(s+1) if s<n-1 else (-1)**(n+1)
        B=product(w,ten);item=g77.cone_test(B,CHART,sign,FACTOR)
        count=sum(c10[x] for x in w);assert count==12838933+(n-1)*14158226
        expanded=g81.expand(w,TENTH);direct=product(expanded,nine)
        for i in range(2):
            for j in range(2):
                assert max(B[i][j].lo,direct[i][j].lo)<=min(B[i][j].hi,direct[i][j].hi)
        item.update({'tenth_word':w,'ninth_word':expanded,'original_step_count':count,
                     'determinant_rho_exponent':0})
        cert[key]=item
    B=product(GUARD,seven);tr=B[0][0]+B[1][1];dd=det(B);disc=tr*tr-4*dd
    assert dd.lo>0 and dd.lo<=1<=dd.hi
    assert F(1466,100)<tr.lo<tr.hi<F(1467,100) and disc.lo>0
    return {'physical_recalculation':'FRESH PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
            'precision':{'grid':'10^120','log_series_terms':400},'layer_pivots':pivots,
            'GERM71_box_regression':'CONTAINED; not rounded numerical inputs',
            'tenth_maps':atomdata,'chart':[['1','1'],['-53/25','-199/100']],
            'common_forward_backward_factor':'5/2','eleven_complete_returns':cert,
            'distinct_temporal_words':11,'low_domain_cells':4,'high_domain_cells':9,
            'next_seventh_word':GUARD,'next_matrix_namespace':'GERM-81-local U1 V1',
            'next_trace':old.display_matrix([[tr]]),'next_determinant':old.display_matrix([[dd]]),
            'next_discriminant':old.display_matrix([[disc]])}

# Exact affine coordinates inherited from GERM-75 (gamma=1).
af,add,sub,val,vertices=parent.af,parent.add,parent.sub,parent.val,parent.vertices
scale,audit=parent.scale,parent.audit
seed,b,rho,c,sigma=parent.seed,parent.b,parent.rho,parent.c,parent.sigma
eps=sub(b,rho);ell=parent.cut;om11=sub(c,scale(4,ell));cut11=sub(ell,om11)
RANGE=parent.RANGE+(om11,cut11)
zero=af()

def tenth_req(key,y):
    n=10 if key[0]=='V' else 11;inside=key[-1]=='1'
    q=add(y,sub(sigma,scale(n,c)))
    return q,[('y>0',y),('y<c10',sub(c,y)),('q>0',q),('q<c10',sub(c,q)),
              ('lower_global_scope',eps),('upper_global_scope',sub(c,eps)),
              ('tenth_cut',sub(ell,y) if n==10 else sub(y,ell)),
              ('tenth_source_bit',sub(eps,y) if inside else sub(y,eps))]

def tenth_lift(key,y):
    q,m=tenth_req(key,y)
    target,lower=parent.tenth_lift(TENTH[key],y);assert target==q
    return q,m+[(f'ninth:{name}',v) for name,v in lower]

def eleventh_lift(word,y):
    n=len(word);pp=[y]+[add(y,sub(c,scale(j,ell))) for j in range(1,n+1)]
    q=pp[-1];m=[('y>0',y),('y<c11',sub(ell,y)),('q>0',q),('q<c11',sub(ell,q))]
    for j,key in enumerate(word):
        out,lower=tenth_req(key,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_eleventh_hit{j}',sub(out,ell) if j<n-1 else sub(ell,out)))
    return q,m

def geometry_audit():
    levels={}
    for label,lib,req,lift in (
        ('sixth',g81.ATOMS,g81.atom_req,g81.atom_lift),
        ('seventh',g81.SEVENTH,g81.seventh_req,g81.seventh_lift),
        ('eighth',g83.EIGHTH,g83.eighth_req,g83.eighth_lift),
        ('ninth',parent.NINTH,parent.ninth_req,parent.ninth_lift),
        ('tenth',TENTH,tenth_req,tenth_lift)):
        cells={}
        for key in lib:
            _,rr=req(key,seed);_,m=lift(key,seed)
            cond=RANGE+tuple(v for _,v in rr);item=audit(m,vertices(cond))
            if ((label=='eighth' and key in ('A','E')) or
                (label=='ninth' and key in ('Q','S')) or
                (label=='tenth' and key in ('V1','U1'))):
                item['eps_equals_c10_endpoint']=audit(m,vertices(cond+(sub(eps,c),sub(c,eps))))
            if label=='tenth' and key in ('V0','U0'):
                item['eps_equals_zero_entry']=audit(m,vertices(cond+(sub(zero,eps),)))
            cells[key]=item
        levels[label]=cells
    low={};high={}
    for (i,n),word in LOW.items():
        q,m=eleventh_lift(word,seed)
        cond=RANGE+(eps,sub(ell,eps),seed,sub(ell,seed),q,sub(ell,q),
                    sub(eps,seed) if i else sub(seed,eps))
        m.append(('low_upper_global_scope',sub(ell,eps)))
        item=audit(m,vertices(cond))
        if i:item['eps_equals_c11_junction']=audit(m,vertices(cond+(sub(eps,ell),)))
        low[f'{i}/{n}']=item
    for (s,n),word in HIGH.items():
        q,m=eleventh_lift(word,seed)
        cond=RANGE+(sub(eps,ell),sub(c,eps),seed,sub(ell,seed),q,sub(ell,q))
        cond += (sub(add(q,ell),eps),) if s==0 else (
            sub(eps,add(q,scale(s,ell))),sub(add(q,scale(s+1,ell)),eps))
        m += [('high_lower_global_scope',sub(eps,ell)),('high_upper_global_scope',sub(c,eps))]
        item=audit(m,vertices(cond))
        if s==0:item['eps_equals_c11_junction']=audit(m,vertices(cond+(sub(ell,eps),)))
        if s==n-1:item['eps_equals_c10_endpoint']=audit(m,vertices(cond+(sub(eps,c),)))
        high[f'{s}/{n}']=item
    assert add(cut11,om11)==ell
    assert sub(c,scale(4,ell))==om11
    assert sub(c,scale(5,ell))==scale(-1,cut11)
    assert add(scale(4,cut11),scale(5,om11))==c
    assert add(rho,c)==sigma
    # Immediately beyond the completed eighth formula endpoint, the two-step
    # eighth word switches to V1,U1 on 0<z<a<sigma8. U/V here are GERM-81-local.
    excess=sub(eps,c);chi,psi,t=g83.chi,g83.psi,g83.t
    assert excess==sub(t,sub(chi,psi))
    pp=[seed,add(seed,sub(chi,psi)),add(seed,sub(chi,scale(2,psi)))]
    margins=[('guard_source>0',seed),('guard_source<sigma',sub(sigma,seed))]
    for j,key in enumerate(GUARD):
        out,lower=g81.seventh_req(key,pp[j]);assert out==pp[j+1]
        margins += [(f'{j}:{name}',v) for name,v in lower]
        margins.append((f'guard_no_early_hit{j}',sub(out,psi) if j==0 else sub(psi,out)))
    guard=audit(margins,vertices(RANGE+(excess,sub(sigma,excess),seed,sub(excess,seed))))
    return {'parameter':'eps=b-rho9=e-e84','rechecked_lower_contracts':levels,
            'new_exclusion_scope':'0<eps<=c10, equivalently rho9<b<=sigma8',
            'physical_field':'W(t0+y); t0=h-beta+gamma-xi+2eta7',
            'eleventh_section':'0<y<c11; c11=c10-omega10',
            'eleventh_times':'4 for y<c11-omega11; 5 otherwise',
            'eleventh_map':'y -> y+omega11 mod c11',
            'eleventh_images':'(omega11,c11) and (0,omega11)',
            'low_cells':low,'high_cells':high,
            'upper_endpoint_words':['U1^3 V1','U1^4 V1'],
            'next_domain':'t=chi7-psi7+a; 0<z<a<sigma8',
            'next_seventh_word':GUARD,'next_guard':guard,'sampled_topology':False}

def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-85','standing':'UNRATIFIED',
         'entry_commit':'fe2e3a73749606d30e0e46a3b1512fafa495e250',
         'new_exclusion_scope':'rho9<b<=sigma8; L84<L<=L84+c10',
         'inherited_three_layer_formula_scope':'2h<e<=3h',
         'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
         'matrix_namespace':'P/Q/R/S are GERM-84-local; U/V are GERM-85-local tenth maps except the explicitly GERM-81-local next guard',
         'tenth_word_dictionary':TENTH,
         'low_eleventh_words':{f'{i}/{n}':w for (i,n),w in LOW.items()},
         'high_eleventh_words':{f'{s}/{n}':w for (s,n),w in HIGH.items()},
         'arithmetic':arithmetic(),'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
         'full_lower_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
         'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
