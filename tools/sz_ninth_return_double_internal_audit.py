#!/usr/bin/env python3
"""GERM-80: double-internal ninth returns; close delta<=chi7.

New exclusion: delta79<delta<=chi7, including the previously open formula
endpoint. Recheck that endpoint from GERM-75 lower source contracts; do
not infer it by continuity. Four low-strip and 21 high-strip cone tests
cover 23 distinct tenth words (two shared). All signs and domain tests
are exact/outward rational. Run with assertions enabled, without -O.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import partial
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of this certificate; do not use -O.'
ROOT=Path(__file__).resolve().parents[1]
PIN_PATH='tools/sz_eighth_return_all_internal_audit.py'
PIN_SHA='f55b5e8db3837c59dce5d0f6c37f3624b8dccff49e9aa0615f86b3b31fa6dbba'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest()==PIN_SHA
import sz_eighth_return_all_internal_audit as parent
g77,g75,old=parent.g77,parent.g75,parent.old
# More digits AND more log-series terms: no narrowing of old intervals by fiat.
old.SCALE=10**120
_original_log_box=old.log_box
old.log_box=partial(_original_log_box,terms=400)
product,det=parent.product,parent.det

# Chronological eighth words. P/Q are the positive-rho ninth step; R/S
# are the negative-c ninth step. Q/S mean ninth source y<b.
NINTH={'P':['A','D','E'],'Q':['A','E','E'],
       'R':['A','D','E','E'],'S':['A','E','E','E']}
LOW={(i,n):[('Q' if i else 'P')]+['R']*(n-1)
     for n in (10,11) for i in (0,1)}
HIGH={(s,n):['Q']+['R']*(n-s-1)+['S']*s
      for n in (10,11) for s in range(n)}
assert len(LOW)==4 and len(HIGH)==21
assert len({tuple(w) for w in list(LOW.values())+list(HIGH.values())})==23
CLO=[[1,1],[F(-293,100),F(-14,5)]]
CHI=[[1,-1],[F(-113,40),F(277,100)]]
FACTOR=F(400)

def arithmetic():
    add,sub,mul=old.add,old.sub,old.mul
    h=(-4,4,-1);k=(4,-1,-1)
    kap=sub(k,mul(5,h));tau=sub(h,mul(5,kap));theta=sub(kap,mul(8,tau))
    alpha=sub(tau,mul(3,theta));beta=sub(theta,alpha);gamma=sub(alpha,beta)
    xi=sub(mul(5,gamma),beta);omega=sub(gamma,mul(19,xi))
    eta=sub(xi,omega);chi=sub(mul(2,omega),xi);psi=sub(eta,chi)
    sig=sub(mul(3,psi),chi);rho=sub(psi,mul(3,sig));c=sub(sig,rho)
    om=sub(sig,mul(10,c));cut=sub(c,om)
    L76=(-1390428,1222107,-235392);L79=(8965832,-7880426,1517855)
    L80=add(L76,chi);end3=add((4,-1,0),mul(3,h))
    assert L80==(193384,-169969,32737)
    assert sub(L80,L79)==sig
    assert L80==add((4,-1,0),add(mul(-40541,h),mul(7804,k)))
    assert add(mul(10,cut),mul(11,om))==sig
    checks={'c10_positive':c,'sigma8_gt_10c10':om,
            'sigma8_lt_11c10':cut,'endpoint_gt_L79':sig,
            'endpoint_below_3h':sub(end3,L80),
            'endpoint_below_sixth_exterior_limit':sub(sub(gamma,xi),add(mul(14,xi),omega)),
            'eta7_positive_for_next_guard':eta}
    # Certified logarithm series with rational remainder bounds avoid enormous
    # integer exponentiation at this residual scale. Every test remains an
    # exact rational inequality for an enclosure of the actual log expression.
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(v):return sum((n*l for n,l in zip(v,logs)),old.box(0))
    enclosed={name:enc(v) for name,v in checks.items()}
    assert all(v.lo>0 for v in enclosed.values())
    return {'outward_rational_log_order_checks':{name:g77.show_box(v,32) for name,v in enclosed.items()},
        'endpoint_prime_log_vector':L80,'endpoint_h_k_vector':[-40541,7804],
        'increment_prime_log_vector':sig,
        'endpoint_decimal':g77.show_box(enc(L80),28),
        'increment_decimal':g77.show_box(enc(sig),32),
        'c10_prime_log_vector':c,'omega10_prime_log_vector':om,
        'c10_decimal':g77.show_box(enc(c),32),
        'omega10_decimal':g77.show_box(enc(om),32),
        'remaining_three_layer_width':g77.show_box(enc(sub(end3,L80)),32),
        'seventh_formula_endpoint':'delta=chi7, included by new endpoint-domain checks'}

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
    atoms={k:product(g75.sixth_word(s,n),fifth) for k,(s,n) in g77.ATOMS.items()}
    counts={}
    for key,(s,n) in g77.ATOMS.items():
        ow=g75.to_original(g75.sixth_word(s,n))
        assert legacy.determinant_exponent(ow)==0
        assert len(ow)==1654*n-297;counts[key]=len(ow)
    seventh={k:product(w,atoms) for k,w in g77.SEVENTH.items()}
    c7={k:sum(counts[x] for x in w) for k,w in g77.SEVENTH.items()}
    eighth={k:product(w,seventh) for k,w in parent.EIGHTH.items()}
    c8={k:sum(c7[x] for x in w) for k,w in parent.EIGHTH.items()}
    ninth={k:product(w,eighth) for k,w in NINTH.items()}
    c9={k:sum(c8[x] for x in w) for k,w in NINTH.items()}
    assert c9=={'P':965296,'Q':965296,'R':1319293,'S':1319293}
    for B in list(eighth.values())+list(ninth.values()):
        dd=det(B);assert dd.lo>0 and dd.lo<=1<=dd.hi
    B=ninth['Q'];tr=B[0][0]+B[1][1];di=tr*tr-4*det(B)
    assert di.hi<0  # The entry obstruction remains elliptic.
    result={}
    for label,words,chart in (('low',LOW,CLO),('high',HIGH,CHI)):
        cert={}
        for (bit,n),w in words.items():
            B=product(w,ninth)
            sign=1 if label=='low' or bit==0 else -1
            item=g77.cone_test(B,chart,sign,FACTOR)
            count=sum(c9[k] for k in w)
            assert count==965296+(n-1)*1319293
            w8=[x for k in w for x in NINTH[k]]
            direct=product(w8,eighth)
            # Regression only: exact identity follows from literal substitution.
            for i in range(2):
                for j in range(2):
                    assert max(B[i][j].lo,direct[i][j].lo)<=min(B[i][j].hi,direct[i][j].hi)
            item.update({'ninth_word':w,'eighth_word':w8,
                         'original_step_count':count,'determinant_rho_exponent':0})
            cert[f'{bit}/{n}']=item
        result[label]=cert
    # Just outside the newly closed endpoint a SIXTH atom changes.
    next_word=g75.sixth_word(15,19);B=product(next_word,fifth)
    tr=B[0][0]+B[1][1];dd=det(B);disc=tr*tr-4*dd
    assert F(49,100)<tr.lo<tr.hi<F(50,100) and dd.lo>0 and disc.hi<0
    assert legacy.determinant_exponent(g75.to_original(next_word))==0
    return {'physical_recalculation':'FRESH OUTWARD RATIONAL PAIRED-SOURCE SOLVES',
        'grid':'10^120','log_series_terms':400,'layer_pivots':pivots,
        'GERM71_box_regression':'CONTAINED','ninth_maps':{k:old.display_matrix(v) for k,v in ninth.items()},
        'entry_elliptic_atom':'Q=E^2 A remains elliptic',
        'low_chart':[['1','1'],['-293/100','-14/5']],
        'high_chart':[['1','-1'],['-113/40','277/100']],
        'common_forward_backward_factor':'400','cone_tests':result,
        'distinct_temporal_words':23,'cone_chart_tests':25,
        'next_sixth_atom':'B15,19','next_fifth_word':next_word,
        'next_trace':old.display_matrix([[tr]]),'next_determinant':old.display_matrix([[dd]]),
        'next_discriminant':old.display_matrix([[disc]])}

# gamma=1; inherited affine variables (beta/gamma,zeta/gamma,seed/gamma).
af,add,sub,val,vertices=parent.af,parent.add,parent.sub,parent.val,parent.vertices
scale=parent.scale
zero=af();seed=parent.seed;psi=parent.psi;chi=parent.chi;delta=parent.delta
sigma=parent.sigma;rho=parent.rho9;c=sub(sigma,rho)
om=sub(sigma,scale(10,c));cut10=sub(c,om)
b=sub(parent.a,parent.amax)
RANGE=parent.RANGE+(om,sub(c,om))

def ninth_req(key,y):
    nonnegative_step=key in ('P','Q');interior=key in ('Q','S')
    target=add(y,rho) if nonnegative_step else sub(y,c)
    rr=[('y>0',y),('y<sigma',sub(sigma,y)),('target>0',target),('target<sigma',sub(sigma,target)),
        ('b>0',b),('ninth_global_scope',sub(sigma,b)),
        ('ninth_rotation_cut',sub(c,y) if nonnegative_step else sub(y,c)),
        ('ninth_source_bit',sub(b,y) if interior else sub(y,b))]
    return target,rr

def ninth_lift(key,y):
    target,m=ninth_req(key,y)
    s,n={'P':(1,3),'Q':(2,3),'R':(2,4),'S':(3,4)}[key]
    assert NINTH[key]==parent.ninth_word(s,n)
    q,lower=parent.ninth_lift(s,n,y);assert q==target
    return target,m+[(f'eighth:{name}',a) for name,a in lower]

def tenth_lift(word,y):
    n=len(word)
    pp=[y]+[add(y,sub(sigma,scale(j,c))) for j in range(1,n+1)]
    q=pp[-1]
    m=[('y>0',y),('y<c',sub(c,y)),('q>0',q),('q<c',sub(c,q))]
    for j,key in enumerate(word):
        target,lower=ninth_req(key,pp[j]);assert target==pp[j+1]
        m += [(f'{j}:{name}',a) for name,a in lower]
        m.append((f'no_earlier_tenth_hit{j}',sub(target,c) if j<n-1 else sub(c,target)))
    return q,m

def geometry_audit():
    audit=g77.audit
    levels={}
    # Endpoint extension is derived bottom-up from the still-valid GERM-75
    # source equations. Repeating a scope label is NOT an endpoint proof.
    six={}
    for key,(s,n) in g77.ATOMS.items():
        target,req=g77.atom_req(key,seed)
        q,m=g75.sixth_lift(s,n,seed);assert target==q
        cond=g77.RANGE+tuple(a for _,a in req)
        six[key]=audit(m,vertices(cond))
        if key in ('A19','E20'):
            six[key]['delta_equals_chi7_face']=audit(m,vertices(cond+(sub(delta,chi),)))
    levels['sixth']=six
    for label,lib,req,lift,endpoint_keys in (
            ('seventh',g77.SEVENTH,g77.seventh_req,g77.seventh_lift,('U1','V1')),
            ('eighth',parent.EIGHTH,parent.eighth_req,parent.eighth_lift,('A','E')),
            ('ninth',NINTH,ninth_req,ninth_lift,('Q','S'))):
        cells={}
        for key in lib:
            _,rr=req(key,seed);_,m=lift(key,seed)
            cond=RANGE+tuple(a for _,a in rr)
            cells[key]=audit(m,vertices(cond))
            if key in endpoint_keys:
                cells[key]['delta_equals_chi7_face']=audit(m,vertices(cond+(sub(delta,chi),)))
        levels[label]=cells
    low={};high={}
    for (i,n),word in LOW.items():
        q,m=tenth_lift(word,seed)
        cond=RANGE+(b,sub(c,b),seed,sub(c,seed),q,sub(c,q),
                    sub(b,seed) if i else sub(seed,b))
        m += [('low_upper_global_scope',sub(c,b))]
        item=audit(m,vertices(cond))
        if i==1:item['b_equals_c_junction']=audit(m,vertices(cond+(sub(b,c),)))
        low[f'{i}/{n}']=item
    for (s,n),word in HIGH.items():
        q,m=tenth_lift(word,seed)
        cond=RANGE+(sub(b,c),sub(sigma,b),seed,sub(c,seed),q,sub(c,q))
        cond += (sub(add(q,c),b),) if s==0 else (
            sub(b,add(q,scale(s,c))),sub(add(q,scale(s+1,c)),b))
        m += [('high_lower_global_scope',sub(b,c)),('high_upper_global_scope',sub(sigma,b))]
        item=audit(m,vertices(cond))
        if s==0:item['b_equals_c_junction']=audit(m,vertices(cond+(sub(c,b),)))
        if s==n-1:item['b_equals_sigma_endpoint']=audit(m,vertices(cond+(sub(b,sigma),)))
        high[f'{s}/{n}']=item
    # Exact first-return images and tower measure.
    assert add(cut10,om)==c
    assert sub(sigma,scale(10,c))==om
    assert sub(sigma,scale(11,c))==scale(-1,cut10)
    assert add(scale(10,cut10),scale(11,om))==sigma
    # Just above endpoint: d=omega+t, 0<y<t<eta7.
    t=sub(delta,chi);eta=g77.eta
    q,m=g75.sixth_lift(15,19,seed)
    assert q==add(seed,g77.omega)
    cond=RANGE+(t,sub(eta,t),seed,sub(t,seed))
    guard=audit(m,vertices(cond))
    return {'normalization':'gamma=1; inherited beta/gamma box refined by 10c10<sigma8<11c10',
        'endpoint_extension':'delta=chi7 derived from sixth-source contracts upward, not continuity',
        'rechecked_level_contracts_and_endpoint_faces':levels,
        'ninth_formula_scope':'0<b<=sigma8, including endpoint; b=delta-(chi7-sigma8)',
        'physical_field':'W(t0+y), t0=h-beta+gamma-xi+2eta7',
        'tenth_section':'0<y<c10; c10=sigma8-rho9',
        'tenth_times':'10 for y<c10-omega10; 11 for y>c10-omega10',
        'tenth_map':'y -> y+omega10 mod c10',
        'image_tiling':'(omega10,c10) and (0,omega10)',
        'tower_measure':'10(c10-omega10)+11omega10=sigma8',
        'low_cells':low,'high_cells':high,
        'completeness':'Initial P/Q and later R/S. For b<=c10 later bits are exterior. For b>=c10 the interior later bits form a final consecutive run.',
        'endpoint_survivors':'S^9 Q and S^10 Q; delta=chi7 is included',
        'next_domain':'delta=chi7+t; 0<y<t<eta7 on the sixth circle',
        'next_sixth_atom':'B15,19 replaces B14,19','next_guard':guard,'sampled_topology':False}

def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-80','standing':'UNRATIFIED',
        'entry_commit':'e7210aeb5441c9fe5b66eeac07877b4ee2980b72',
        'new_exclusion_scope':'chi7-sigma8<delta<=chi7; L79<L<=L76+chi7',
        'experimental_endpoint':'log(2^193384*5^32737/3^169969)',
        'inherited_three_layer_formula_scope':'2h<e<=3h',
        'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
        'ninth_word_dictionary':NINTH,
        'arithmetic':arithmetic(),'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
        'full_parent_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
        'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
