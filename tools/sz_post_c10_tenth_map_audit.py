#!/usr/bin/env python3
"""GERM-87: post-c10 tenth-map transfer through epsilon=omega10.

Inherits GERM-86's eighth/ninth source equations.  For
0<epsilon<=omega10, epsilon=a-c10=e-e86, the ten-step tenth map stays
R^9 Q, while the eleven-step branch splits into R^10 Q and S R^9 Q.
Nine complete eleventh returns admit one signed rational cone chart.
Every intermediate lower-domain contract is checked exactly/outward rational.
Run with assertions enabled, without -O.  Unratified research only.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib, json

assert __debug__, 'Assertions are part of the certificate; run without -O.'
ROOT=Path(__file__).resolve().parents[1]
PIN_PATH='tools/sz_post_chi_minus_psi_eighth_map_audit.py'
PIN_SHA='97fd7d30a211e4bf0ae464df0c3f8dd41aab92d0e25be1de41343a6f4c6dae48'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest()==PIN_SHA
import sz_post_chi_minus_psi_eighth_map_audit as parent
g83,g81,g77,g75,old=parent.g83,parent.g81,parent.g77,parent.g75,parent.old
product,det=parent.product,parent.det

# GERM-86-local ninth matrices P/Q/R/S are retained literally.
# New tenth labels are GERM-87-local.
TENTH={'V':['Q']+['R']*9,
       'U0':['Q']+['R']*10,
       'U1':['Q']+['R']*9+['S']}
WORDS={(s,n):['V']+['U0']*(n-s-1)+['U1']*s
       for n in (4,5) for s in range(n)}
CHART=parent.CHART
FACTOR=F(100)
NEXT=['Q']+['R']*8+['S']


def arithmetic():
    add,sub,mul=old.add,old.sub,old.mul
    h=(-4,4,-1);k=(4,-1,-1)
    kap=sub(k,mul(5,h));tau=sub(h,mul(5,kap));theta=sub(kap,mul(8,tau))
    alpha=sub(tau,mul(3,theta));beta=sub(theta,alpha);gamma=sub(alpha,beta)
    xi=sub(mul(5,gamma),beta);omega=sub(gamma,mul(19,xi))
    eta=sub(xi,omega);chi=sub(mul(2,omega),xi);psi=sub(eta,chi)
    sigma=sub(mul(3,psi),chi);rho=sub(psi,mul(3,sigma));c=sub(sigma,rho)
    om10=sub(sigma,mul(10,c));ell=sub(c,om10);om11=sub(c,mul(4,ell));cut11=sub(ell,om11)
    L86=(-28520172,25067529,-4828280);L87=add(L86,om10)
    assert om10==(318163352,-279646553,53862972)
    assert L87==(289643180,-254579024,49034692)
    assert L87==add((4,-1,0),add(mul(-60722743,h),mul(11688051,k)))
    top=add((4,-1,0),mul(3,h))
    assert add(ell,om10)==c
    assert add(mul(4,cut11),mul(5,om11))==c
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(v):return sum((n*l for n,l in zip(v,logs)),old.box(0))
    checks={'omega10_positive':om10,'ell_positive':ell,'4c11_lt_c10':om11,
            'c10_lt_5c11':cut11,'new_endpoint_inside_eighth_formula':rho,
            'endpoint_below_three_layers':sub(top,L87)}
    boxes={k:enc(v) for k,v in checks.items()};assert all(x.lo>0 for x in boxes.values())
    return {'rational_log_order_checks':{k:g77.show_box(v,38) for k,v in boxes.items()},
            'endpoint_prime_log_vector':L87,'endpoint_h_k_vector':[-60722743,11688051],
            'endpoint_decimal':g77.show_box(enc(L87),35),
            'increment_prime_log_vector':om10,'increment_decimal':g77.show_box(enc(om10),38),
            'remaining_eighth_formula_width':g77.show_box(enc(rho),38),
            'remaining_three_layer_width':g77.show_box(enc(sub(top,L87)),38),
            'tower_identities':'ell+omega10=c10; 4(c11-omega11)+5omega11=c10'}


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
    seven={k:product(w,atoms) for k,w in g81.SEVENTH.items()}
    eight={k:product(w,seven) for k,w in parent.EIGHTH.items()}
    nine={k:product(w,eight) for k,w in parent.NINTH.items()}
    ten={k:product(w,nine) for k,w in TENTH.items()}
    # determinant and literal boundary regressions
    for lib in (atoms,seven,eight,nine,ten):
        for B in lib.values():
            d=det(B);assert d.lo>0 and d.lo<=1<=d.hi
    assert TENTH['V']==parent.TENTH['V1']
    assert TENTH['U0']==parent.TENTH['U1']
    counts9={'P':965296,'Q':965296,'R':1319293,'S':1319293}
    counts10={k:sum(counts9[x] for x in w) for k,w in TENTH.items()}
    assert counts10=={'V':12838933,'U0':14158226,'U1':14158226}
    cert={}
    for (s,n),w in WORDS.items():
        B=product(w,ten);sign=(-1)**(s+n)
        item=g77.cone_test(B,CHART,sign,FACTOR)
        count=sum(counts10[x] for x in w)
        assert count==12838933+(n-1)*14158226
        item.update({'tenth_word':w,'original_step_count':count,'overall_sign':sign})
        cert[f'{s}/{n}']=item
    B=product(NEXT,nine);tr=B[0][0]+B[1][1];d=det(B);disc=tr*tr-4*d
    assert d.lo>0 and d.lo<=1<=d.hi
    assert F(-8008)<tr.lo<tr.hi<F(-8006) and disc.lo>0
    return {'physical_recalculation':'FRESH PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
            'precision':{'grid':'10^120','log_series_terms':400},'layer_pivots':pivots,
            'GERM71_box_regression':'CONTAINED; not rounded proof inputs',
            'tenth_word_dictionary':TENTH,'chart':[['1','1'],['-11/5','-8/5']],
            'common_forward_backward_factor':'100','nine_complete_returns':cert,
            'distinct_temporal_words':9,
            'entry_regression':'new V=GERM86 V1; new U0=GERM86 U1 by literal substitution',
            'next_tenth_word':NEXT,'next_matrix':'S R^8 Q, GERM-87-local',
            'next_trace':old.display_matrix([[tr]]),'next_determinant':old.display_matrix([[d]]),
            'next_discriminant':old.display_matrix([[disc]]),
            'next_status':'HYPERBOLIC NEW TEN-STEP TENTH SOURCE WORD'}


# Exact affine coordinates inherited from GERM-86.
af,add,sub,val,vertices=parent.af,parent.add,parent.sub,parent.val,parent.vertices
scale,audit=parent.scale,parent.audit
seed,a,sigma,c,ell=parent.seed,parent.a,parent.sigma,parent.c,parent.ell
omt=sub(sigma,scale(10,c));om11=sub(c,scale(4,ell));cut11=sub(ell,om11)
eps=sub(a,c);RANGE=parent.RANGE;zero=af()


def tenth_req(key,y):
    n=10 if key=='V' else 11;q=add(y,sub(sigma,scale(n,c)))
    m=[('y>0',y),('y<c10',sub(c,y)),('q>0',q),('q<c10',sub(c,q)),
       ('lower_global_scope',eps),('upper_global_scope',sub(omt,eps)),
       ('tenth_cut',sub(ell,y) if n==10 else sub(y,ell))]
    if key=='U0':m.append(('last_source_exterior',sub(y,add(ell,eps))))
    if key=='U1':m.append(('last_source_interior',sub(add(ell,eps),y)))
    return q,m


def tenth_word_lift(word,y):
    n=len(word);pp=[y]+[add(y,sub(sigma,scale(j,c))) for j in range(1,n+1)]
    q=pp[-1];m=[('y>0',y),('y<c10',sub(c,y)),('q>0',q),('q<c10',sub(c,q))]
    for j,k in enumerate(word):
        out,lower=parent.ninth_req(k,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_tenth_hit{j}',sub(out,c) if j<n-1 else sub(c,out)))
    return q,m


def tenth_lift(key,y):
    q,m=tenth_req(key,y);out,lower=tenth_word_lift(TENTH[key],y);assert out==q
    return q,m+[(f'ninth:{name}',v) for name,v in lower]


def eleventh_lift(word,y):
    n=len(word);pp=[y]+[add(y,sub(c,scale(j,ell))) for j in range(1,n+1)]
    q=pp[-1];m=[('y>0',y),('y<c11',sub(ell,y)),('q>0',q),('q<c11',sub(ell,q)),
                 ('eleventh_cut',sub(cut11,y) if n==4 els`sub(cut11,y))]
    for j,key in enumerate(word):
        out,lower=tenth_lift(key,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lower]
        m.append((f'no_early_eleventh_hit{j}',sub(out,ell) if j<n-1 els`sub(ell,out)))
    return q,m


def geometry_audit():
    levels={}
    # Recheck the inherited eighth/ninth contracts on the new parameter strip.
    for label,lib,req,lift in (
        ('eighth',parent.EIGHTH,parent.eighth_req,parent.eighth_lift),
        ('ninth',{k:v for k,v in parent.NINTH.items() if k in ('Q','R','S')},parent.ninth_req,parent.ninth_lift)):
        cells={}
        for key in lib:
            _,rr=req(key,seed);_,m=lift(key,seed)
            cond=RANGE+(eps,sub(omt,eps))+tuple(v for _,v in rr)
            cells[key]=audit(m,vertices(cond))
        levels[label]=cells
    tenth={}
    for key in TENTH:
        _,rr=tenth_req(key,seed);_,m=tenth_lift(key,seed)
        cond=RANGE+tuple(v for _,v in rr);item=audit(m,vertices(cond))
        if key in ('V','U1'):
            item['epsilon_equals_omega10_endpoint']=audit(m,vertices(cond+(sub(eps,omt),sub(omt,eps))))
        if key in ('V','U0'):
            item['epsilon_equals_zero_entry']=audit(m,vertices(cond+(sub(zero,eps),)))
        tenth[key]=item
    cells={}
    for (s,n),w in WORDS.items():
        q,m=eleventh_lift(w,seed)
        cond=RANGE+(eps,sub(omt,eps),seed,sub(ell,seed),q,sub(ell,q))
        cond += (sub(q,eps),) if s==0 else (sub(eps,add(q,scale(s-1,ell))),sub(add(q,scale(s,ell)),eps))
        item=audit(m,vertices(cond))
        if s==0:item['epsilon_equals_zero_entry']=audit(m,vertices(cond+(sub(zero,eps),)))
        if s==n-1:item['epsilon_equals_omega10_endpoint']=audit(m,vertices(cond+(sub(eps,omt),sub(omt,eps))))
        cells[f'{s}/{n}']=item
    # Exact return geometry.
    assert add(ell,omt)==c and sub(c,scale(4,ell))==om11
    assert add(scale(4,cut11),scale(5,om11))==c
    # Next strip: after epsilon=omega10 the final N=10 pre-return source changes R -> S.
    excess=sub(eps,omt);q,m=tenth_word_lift(NEXT,seed)
    cond=RANGE+(excess,sub(ell,excess),seed,sub(excess,seed))
    assert q==sub(seed,sub(c,omt))
    guard=audit(m,vertices(cond))
    return {'parameter':'epsilon=a-c10=e-e86','formula_scope':'0<epsilon<=omega10',
            'rechecked_lower_contracts':levels,'new_tenth_contracts':tenth,
            'eleventh_section':'0<y<c11','eleventh_map':'y -> y+omega11 mod c11',
            'new_exclusion_scope':'0<epsilon<=omega10','nine_eleventh_cells':cells,
            'upper_endpoint_words':['U1^z3 V','U1^4 V, all GERM-87-local'],
            'next_domain':'epsilon=omega10+d; 0<d<c11; 0<y<d',
            'next_tenth_word':NEXT,'next_guard':guard,'sampled_topology':False}


def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-87','standing':'UNRATIFIED',
         'entry_commit':'93b2023a0211ef6a946d563a6d379318580d6ef2',
         'new_exclusion_scope':'0<epsilon<=omega10, epsilon=e-e86; L86<L<=L86+omega10',
         'inherited_three_layer_formula_scope':'2h<e<=3h',
         'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
         'matrix_namespace':'P/Q/R/S are GERM86-local ninth maps; V/U0/U1 are GERM-87-local tenth maps',
         'tenth_word_dictionary':TENTH,
         'eleventh_word_dictionary':{f'{s}/{n}':w for (s,n),w in WORDS.items()},
         'arithmetic':arithmetic(),'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
         'full_lower_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
         'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
