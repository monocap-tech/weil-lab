#!/usr/bin/env python3
"""GERM-100: post-omega11 transfer, with direct twelfth exclusion.

Proves 0<a<=9w, a=e-e99 and w=omega11. Four eleventh formulas hold on
0<a<=c11. Twenty complete twelfth words have two parameter-fixed integer
charts and common factor 6/5. Every intermediate source is checked.
No thirteenth induction or new retained coordinate is used. Run without -O.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of the certificate; run without -O.'
ROOT=Path(__file__).resolve().parents[1]
PIN='tools/sz_post_v_delta13_thirteenth_transfer_audit.py'
PIN_SHA='0fe14d514e97559904d267eefdc6e6a3cded44a187235d62b6687f0fab93f9e6'
assert hashlib.sha256((ROOT/PIN).read_bytes()).hexdigest()==PIN_SHA
import sz_post_v_delta13_thirteenth_transfer_audit as parent
g98,g97,old=parent.p,parent.g97,parent.old
g75,g77=g97.g75,g97.g77
product,det=parent.product,parent.det
# Inputs are GERM-97 level-10 maps. New A/B are GERM-100 level-11 maps.
ELEVENTH={'A0':['A1','B0','B0','B0'], 'A1':['A1','B0','B0','B1'],
          'B0':['A1','B0','B0','B0','B1'], 'B1':['A1','B0','B0','B1','B1']}
WORDS={(s,n):['A1']*s+['A0']*(n-s-1)+['B0'] for n in (10,11) for s in range(10)}
CHARTS={'low':[[31,38],[-46,-56]], 'high':[[1,46],[-3,-62]]}
INDICES={'low':[(s,n) for n in (10,11) for s in range(9)],
         'high':[(s,n) for n in (10,11) for s in (8,9)]}
FACTOR=F(6,5)
NEXT=['A1']*10+['B0']
af,add,sub,vertices=g97.af,g97.add,g97.sub,g97.vertices
scale,audit=g97.scale,g97.audit
seed,u,ell,w,r12,c=g97.seed,g97.u,g97.ell,g97.w,g97.r12,g97.c
k=sub(ell,w);a=sub(u,add(ell,w));zero=af();RANGE=g97.RANGE


def arithmetic():
    aa,ss,mm=old.add,old.sub,old.mul
    h,kb=(-4,4,-1),(4,-1,-1)
    kap=ss(kb,mm(5,h));tau=ss(h,mm(5,kap));theta=ss(kap,mm(8,tau))
    alpha=ss(tau,mm(3,theta));beta=ss(theta,alpha);gamma=ss(alpha,beta)
    xi=ss(mm(5,gamma),beta);om=ss(gamma,mm(19,xi));eta=ss(xi,om)
    chi=ss(mm(2,om),xi);psi=ss(eta,chi);sigma=ss(mm(3,psi),chi)
    rho=ss(psi,mm(3,sigma));cc=ss(sigma,rho);o10=ss(sigma,mm(10,cc))
    ll=ss(cc,o10);ww=ss(cc,mm(4,ll));rr=ss(ll,mm(10,ww))
    L99=(1020029612,-896545004,172684332);inc=mm(9,ww);L100=aa(L99,inc)
    assert ww==(1370734148,-1204793315,232056315)
    assert L100==(13356636944,-11739684839,2261191167)
    assert L100==aa((4,-1,0),aa(mm(-2800175201,h),mm(538984034,kb)))
    assert cc==aa(mm(4,ll),ww)
    top=aa((4,-1,0),mm(3,h))
    checks={'r12_positive':rr,'r12_below_w':ss(ww,rr),
      'proof_endpoint_before_long_bit_change':ss(ss(ll,ww),mm(9,ww)),
      'new_formula_inside_tenth':ss(cc,aa(mm(2,ll),ww)),
      'new_formula_inside_sixth':ss(eta,aa(mm(2,ll),ww)),
      'new_formula_below_three_layers':ss(top,aa(L99,ll))}
    for j,shape in enumerate(RANGE):
        assert shape[2]==shape[3]==0
        checks[f'fixed_shape_{j}']=aa(mm(shape[0],gamma),mm(shape[1],beta))
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(vec):return sum((q*z for q,z in zip(vec,logs)),old.box(0))
    boxes={name:enc(vec) for name,vec in checks.items()}
    assert all(b.lo>0 for b in boxes.values())
    return {'order_checks':{name:g77.show_box(b,40) for name,b in boxes.items()},
      'endpoint_prime_log_vector':L100,'endpoint_h_k_vector':[-2800175201,538984034],
      'endpoint_decimal':g77.show_box(enc(L100),40),'increment':'9omega11',
      'increment_prime_log_vector':inc,'increment_decimal':g77.show_box(enc(inc),40),
      'remaining_new_eleventh_formula_width':g77.show_box(enc(ss(ll,inc)),40),
      'remaining_tenth_formula_width':g77.show_box(enc(ss(cc,aa(ll,mm(10,ww)))),40),
      'remaining_three_layer_width':g77.show_box(enc(ss(top,L100)),40)}


def build_matrices():
    # Fresh physical solves and the GERM-71 enclosure regression, via pinned code.
    level10,_,_,pivots=g98.build_matrices()
    level11={key:product(word,level10) for key,word in ELEVENTH.items()}
    return level11,pivots


def rational_audit():
    assert old.SCALE==10**120
    maps,pivots=build_matrices();spectra={}
    # Literal source-word identities, not just numerical equality.
    assert ELEVENTH['A1']==['A1','B0','B0','B1']
    assert ELEVENTH['A0']==g98.ELEVENTH['A']
    assert ELEVENTH['B0']==g98.ELEVENTH['E']
    for key,B in maps.items():
        tr=B[0][0]+B[1][1];dd=det(B);disc=tr*tr-4*dd
        assert dd.lo>0 and dd.lo<=1<=dd.hi
        assert disc.lo>0 if key=='A0' else disc.hi<0
        spectra[key]={'trace':old.display_matrix([[tr]]),'discriminant':old.display_matrix([[disc]])}
    cert={}
    for regime,indices in INDICES.items():
        C=CHARTS[regime]
        assert C[0][0]*C[1][1]-C[0][1]*C[1][0]==(12 if regime=='low' else 76)
        cert[regime]={}
        for s,n in indices:
            B=product(WORDS[s,n],maps);tr=B[0][0]+B[1][1]
            assert tr.lo>0 or tr.hi<0
            sign=1 if tr.lo>0 else -1
            item=g77.cone_test(B,C,sign,FACTOR)
            assert (tr*tr-4*det(B)).lo>0
            item.update({'word':WORDS[s,n],'original_step_count':55313611*(n-1)+69471837})
            cert[regime][f'{s}/{n}']=item
    B=product(NEXT,maps);tr=B[0][0]+B[1][1];dd=det(B);disc=tr*tr-4*dd
    assert dd.lo>0 and dd.lo<=1<=dd.hi and disc.hi<0
    assert F(-93,1000)<tr.lo<tr.hi<F(-92,1000)
    minima={regime:{name:min((F(z[name]) for z in items.values())) for name in ('forward_lower','backward_lower')}
            for regime,items in cert.items()}
    return {'physical_recalculation':'FRESH PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
      'precision':{'grid':'10^120','log_series_terms':400},'layer_pivots':pivots,
      'eleventh_spectra':spectra,'charts':CHARTS,'common_factor':'6/5',
      'distinct_words':len(WORDS),'chart_tests':sum(map(len,INDICES.values())),
      'certificates':cert,'minima':{r:{k:str(v) for k,v in d.items()} for r,d in minima.items()},
      'next_word':NEXT,'next_trace':old.display_matrix([[tr]]),
      'next_discriminant':old.display_matrix([[disc]]),'next_status':'ELLIPTIC TEN-INITIAL-A1 ELEVEN-STEP TWELFTH RETURN'}


def eleventh_req(key,y):
    short=key.startswith('A');n=4 if short else 5
    q=add(y,sub(c,scale(n,ell)))
    return q,[('y>0',y),('y<ell',sub(ell,y)),('q>0',q),('q<ell',sub(ell,q)),
      ('lower_global_scope',a),('upper_global_scope',sub(ell,a)),
      ('return_cut',sub(k,y) if short else sub(y,k)),
      ('new_visit_bit',sub(a,y) if key.endswith('1') else sub(y,a))]


def eleventh_lift(key,y):
    q,m=eleventh_req(key,y);word=ELEVENTH[key];n=len(word)
    pp=[y]+[add(y,sub(c,scale(j,ell))) for j in range(1,n+1)]
    assert pp[-1]==q
    for j,subkey in enumerate(word):
        out,lo=g97.level_lift(10,subkey,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',z) for name,z in lo]
        m.append((f'no_early_eleventh_hit{j}',sub(out,ell) if j<n-1 else sub(ell,out)))
    return q,m


def twelfth_lift(word,y):
    n=len(word);q=sub(add(y,scale(n,w)),ell)
    pp=[add(y,scale(j,w)) for j in range(n)]+[q]
    m=[('y>0',y),('y<w',sub(w,y)),('q>0',q),('q<w',sub(w,q)),
       ('twelfth_cut',sub(y,r12) if n==10 else sub(r12,y))]
    for j,key in enumerate(word):
        out,lo=eleventh_req(key,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',z) for name,z in lo]
        m.append((f'no_early_twelfth_hit{j}',sub(out,w) if j<n-1 else sub(w,out)))
    return q,m


def source_condition(s,n,y,q):
    lo=zero if s==0 else add(y,scale(s-1,w));hi=add(y,scale(s,w))
    return (y,sub(w,y),q,sub(w,q),sub(a,lo),sub(hi,a))


def geometry_audit():
    # Recheck source identities below the new level, not old cone inventories.
    lower={}
    for j,lib,req,lift,upper in ((3,g75.THIRD,g75.third_req,g75.third_lift,g75.beta),
      (4,g75.FOURTH,g75.fourth_req,g75.fourth_lift,g75.beta),
      (5,g75.FIFTH,g75.fifth_req,g75.fifth_lift,af(1))):
        lower[j]={}
        for key in lib:
            _,rr=req(key,seed);_,m=lift(key,seed)
            lower[j][key]=audit(m,vertices(g75.RANGE+(g75.zeta,sub(upper,g75.zeta))+tuple(z for _,z in rr)))
    for j,lib,req,lift in ((6,g97.ATOMS,g97.atom_req,g97.atom_lift),
                         (7,g97.SEVENTH,g97.seventh_req,g97.seventh_lift)):
        lower[j]={}
        for key in lib:
            _,rr=req(key,seed);_,m=lift(key,seed)
            lower[j][key]=audit(m,vertices(RANGE+tuple(z for _,z in rr)))
    for j in (8,9,10):
        lower[j]={}
        for key in g97.WORDS[j]:
            _,rr=g97.level_req(j,key,seed);_,m=g97.level_lift(j,key,seed)
            lower[j][key]=audit(m,vertices(RANGE+tuple(z for _,z in rr)))
    e11={}
    for key in ELEVENTH:
        _,rr=eleventh_req(key,seed);_,m=eleventh_lift(key,seed);cond=RANGE+tuple(z for _,z in rr)
        item=audit(m,vertices(cond))
        face=sub(zero,a) if key.endswith('0') else sub(a,ell)
        item['entry' if key.endswith('0') else 'formula_endpoint']=audit(m,vertices(cond+(face,)))
        e11[key]=item
    tw={}
    for regime,indices in INDICES.items():
        bounds=(a,sub(scale(8,w),a)) if regime=='low' else (sub(a,scale(8,w)),sub(scale(9,w),a))
        tw[regime]={}
        for s,n in indices:
            q,m=twelfth_lift(WORDS[s,n],seed)
            cond=RANGE+bounds+source_condition(s,n,seed,q)
            item=audit(m,vertices(cond))
            if s==0:item['entry']=audit(m,vertices(cond+(sub(zero,a),)))
            if s==8:item['chart_junction_8w']=audit(m,vertices(cond+(sub(a,scale(8,w)),sub(scale(8,w),a))))
            if s==9:item['endpoint_9w']=audit(m,vertices(cond+(sub(a,scale(9,w)),)))
            if regime=='low' and 1<=s<=7:
                item[f'visit_junction_{s}w']=audit(m,vertices(cond+(sub(a,scale(s,w)),sub(scale(s,w),a))))
            tw[regime][f'{s}/{n}']=item
    assert add(scale(10,sub(w,r12)),scale(11,r12))==ell
    # First new word after 9w: 10 interior short steps, then exterior B0.
    excess=sub(a,scale(9,w));q,m=twelfth_lift(NEXT,seed)
    cond=RANGE+(excess,sub(r12,excess),seed,sub(excess,seed))
    assert q==add(seed,sub(w,r12))
    guard=audit(m,vertices(cond))
    return {'parameter':'a=e-e99=u-c11-omega11','eleventh_formula_scope':'0<a<=c11',
      'new_exclusion_scope':'0<a<=9omega11','rechecked_lower_geometry':lower,
      'eleventh_cells':e11,'twelfth_cells':tw,
      'twelfth_map':'y -> y-rho12 mod omega11','physical_field':'W(t0+y); t0=h-beta+gamma-xi+2eta7',
      'endpoint_words':['B0 A1^9','B0 A0 A1^9'],
      'next_domain':'a=9omega11+b; 0<y<b<rho12','next_word':NEXT,'next_guard':guard,
      'sampled_topology':False}


def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-100','standing':'UNRATIFIED',
      'entry_commit':'2c28b18ea653fea5f8501f869a6ede18996bc3c2',
      'dependency_sha256':{PIN:PIN_SHA},'new_exclusion_scope':'0<a<=9omega11, a=e-e99',
      'matrix_namespace':'GERM-97 level-10 inputs; GERM-100-local eleventh A0/A1/B0/B1',
      'eleventh_word_dictionary':ELEVENTH,'arithmetic':arithmetic(),
      'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
      'thirteenth_or_deeper_induction_used':False,'new_retained_coordinates':0,
      'full_lower_symbolic_suites_rerun':False,'complete_GERM60_reduction_rerun':False,
      'old_large_determinants_rerun':False,'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
