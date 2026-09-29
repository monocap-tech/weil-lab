#!/usr/bin/env python3
"""GERM-98: post-u=c11 last-visit transfer via a thirteenth section.

New exclusion: 0<v<=delta13, v=e-e97, delta13=omega12-rho12.
GERM-98-local eleventh A/D/E maps are propagated to the twelfth circle.
Three complete thirteenth returns share one signed rational cone with common
factor 10^6. Every intermediate source is checked down to GERM-97 level 10.
No fourteenth induction or extra retained coordinate is used.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib, json

assert __debug__, 'Assertions are part of the certificate; run without -O.'
ROOT=Path(__file__).resolve().parents[1]
PIN_PATH='tools/sz_post_d_omega_sixth_19_step_audit.py'
PIN_SHA='a550c7ac2c8b4baaa69ea8823fcaa6f2da313b4370f7126cd8fe362a2d48a196'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest()==PIN_SHA
import sz_post_d_omega_sixth_19_step_audit as parent
g75,g77,old=parent.g75,parent.g77,parent.old
product,det=parent.product,parent.det

ELEVENTH={
  'A':['A1','B0','B0','B0'],
  'D':['A1','B0','B0','B0','B0'],
  'E':['A1','B0','B0','B0','B1'],
}
TWELFTH={
  'D10':['A']*9+['D'],
  'E10':['A']*9+['E'],
  'D11':['A']*10+['D'],
}
THIRTEENTH={
  'A':['D11','D10'],
  'D':['D11','D10','D10'],
  'E':['D11','D10','E10'],
}
CHART=[[-27,-145],[40,-488]]
SIGNS={'A':1,'D':-1,'E':1}
FACTOR=F(10**6)
NEXT=['D11','E10']

af,add,sub,vertices=parent.af,parent.add,parent.sub,parent.vertices
scale,audit=parent.scale,parent.audit
seed=parent.seed
ell,w,r12,om12=parent.ell,parent.w,parent.r12,parent.om12
c,u=parent.c,parent.u
v=sub(u,ell)
delta13=sub(om12,r12)
cut13=sub(r12,delta13)
k=sub(ell,w)
zero=af();RANGE=parent.RANGE

def arithmetic():
    a,s,m=old.add,old.sub,old.mul
    h,kb=(-4,4,-1),(4,-1,-1)
    kap=s(kb,m(5,h));tau=s(h,m(5,kap));th=s(kap,m(8,tau))
    al=s(tau,m(3,th));be=s(th,al);ga=s(al,be)
    xx=s(m(5,ga),be);oo=s(ga,m(19,xx));ee=s(xx,oo)
    ch=s(m(2,oo),xx);ps=s(ee,ch);ss=s(m(3,ps),ch)
    rr=s(ps,m(3,ss));cc=s(ss,rr);o10=s(ss,m(10,cc));ll=s(cc,o10)
    ww=s(cc,m(4,ll));rr12=s(ll,m(10,ww));oo12=s(ww,rr12);d13=s(oo12,rr12)
    L97=(-350704536,308248311,-59371983);L98=a(L97,d13);top=a((4,-1,0),m(3,h))
    assert d13==(29487130972,-25917424123,4991978177)
    assert L98==(29136426436,-25609175812,4932606194)
    assert L98==a((4,-1,0),a(m(-6108356401,h),m(1175750207,kb)))
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(vec):return sum((q*z for q,z in zip(vec,logs)),old.box(0))
    checks={
      'delta13_positive':d13,
      'rho12_minus_delta13_positive':s(rr12,d13),
      'delta13_below_omega11':s(ww,d13),
      'new_endpoint_inside_level10_formula':s(cc,a(ll,d13)),
      'new_endpoint_inside_sixth_seventh_formula':s(ee,a(ll,d13)),
      'endpoint_below_three_layers':s(top,L98),
    }
    for j,shape in enumerate(RANGE):
        assert shape[2]==shape[3]==0
        checks[f'fixed_shape_{j}']=a(m(shape[0],ga),m(shape[1],be))
    boxes={name:enc(vec) for name,vec in checks.items()};assert all(z.lo>0 for z in boxes.values())
    return {
      'order_checks':{name:g77.show_box(z,40) for name,z in boxes.items()},
      'endpoint_prime_log_vector':L98,'endpoint_h_k_vector':[-6108356401,1175750207],
      'endpoint_decimal':g77.show_box(enc(L98),40),
      'increment':'delta13=omega12-rho12','increment_prime_log_vector':d13,
      'increment_decimal':g77.show_box(enc(d13),40),
      'remaining_eleventh_formula_width':g77.show_box(enc(s(ww,d13)),40),
      'remaining_sixth_seventh_formula_width':g77.show_box(enc(s(ee,a(ll,d13))),40),
      'remaining_three_layer_width':g77.show_box(enc(s(top,L98)),40),
      'thirteenth_tower_identity':'2*(rho12-delta13)+3*delta13=omega11',
    }

def build_matrices():
    original,pivots=g75.parent.parent.parent.parent.recalculate_returns()
    legacy=g75.parent.parent.parent
    first={key:product(word,original) for key,word in legacy.FIRST.items()}
    second={key:product(word,first) for key,word in legacy.SECOND.items()}
    boxes=json.loads((ROOT/'notes/_recurrence71_audit.json').read_text())['audit']['rational_audit']['second_section_maps']
    for key,B in second.items():
        for i in range(2):
            for j in range(2):
                lo,hi=map(F,boxes[key][i][j]);assert lo<=B[i][j].lo<=B[i][j].hi<=hi
    third={key:product(word,second) for key,word in g75.THIRD.items()}
    fourth={key:product(word,third) for key,word in g75.FOURTH.items()}
    fifth={key:product(word,fourth) for key,word in g75.FIFTH.items()}
    atoms={key:product(g75.sixth_word(*pair),fifth) for key,pair in parent.ATOMS.items()}
    maps={key:product(word,atoms) for key,word in parent.SEVENTH.items()}
    for level in parent.TIMES:
        maps={key:product(word,maps) for key,word in parent.WORDS[level].items()}
        if level==10: level10=maps
    level11={key:product(word,level10) for key,word in ELEVENTH.items()}
    level12={key:product(word,level11) for key,word in TWELFTH.items()}
    return level10,level11,level12,pivots

def rational_audit():
    level10,level11,level12,pivots=build_matrices()
    spectra={11:{},12:{}}
    for level,lib in ((11,level11),(12,level12)):
        for key,B in lib.items():
            dd=det(B);tr=B[0][0]+B[1][1];disc=tr*tr-4*dd
            assert dd.lo>0 and dd.lo<=1<=dd.hi
            spectra[level][key]={'trace':old.display_matrix([[tr]]),'discriminant':old.display_matrix([[disc]])}
    assert spectra[11]['E']['discriminant'][0][0][1].startswith('-')
    cert={}
    for key,word in THIRTEENTH.items():
        B=product(word,level12);item=g77.cone_test(B,CHART,SIGNS[key],FACTOR)
        tr=B[0][0]+B[1][1];disc=tr*tr-4*det(B);assert disc.lo>0
        item.update({'word':word,'overall_sign':SIGNS[key]});cert[key]=item
    B=product(NEXT,level12);tr=B[0][0]+B[1][1];dd=det(B);disc=tr*tr-4*dd
    assert dd.lo>0 and dd.lo<=1<=dd.hi and disc.lo>0
    assert F(-726000000)<tr.lo<tr.hi<F(-725000000)
    return {
      'physical_recalculation':'FRESH PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
      'precision':{'grid':'10^120','log_series_terms':400},'layer_pivots':pivots,
      'GERM71_box_regression':'CONTAINED; not rounded proof inputs',
      'eleventh_word_dictionary':ELEVENTH,'twelfth_word_dictionary':TWELFTH,
      'level_spectra':spectra,'thirteenth_word_dictionary':THIRTEENTH,
      'chart':[[str(x) for x in row] for row in CHART],'chart_determinant':'18976',
      'common_forward_backward_factor':'1000000','three_complete_returns':cert,
      'minimum_forward_lower':min(x['forward_lower'] for x in cert.values()),
      'minimum_backward_lower':min(x['backward_lower'] for x in cert.values()),
      'next_thirteenth_word':NEXT,'next_trace':old.display_matrix([[tr]]),
      'next_determinant':old.display_matrix([[dd]]),'next_discriminant':old.display_matrix([[disc]]),
      'next_status':'HYPERBOLIC NEW TWO-STEP THIRTEENTH RETURN',
    }

def level11_req(key,y):
    short=key=='A';n=4 if short else 5;q=add(y,sub(c,scale(n,ell)))
    m=[('y>0',y),('y<c11',sub(ell,y)),('q>0',q),('q<c11',sub(ell,q)),
       ('lower_global_scope',v),('upper_global_scope',sub(w,v)),
       ('eleventh_cut',sub(k,y) if short else sub(y,k))]
    if key=='D':m.append(('last_source_exterior',sub(y,add(k,v))))
    if key=='E':m.append(('last_source_interior',sub(add(k,v),y)))
    return q,m

def level11_lift(key,y):
    word=ELEVENTH[key];n=len(word)
    pp=[y]+[add(y,sub(c,scale(j,ell))) for j in range(1,n+1)]
    q=pp[-1];_,m=level11_req(key,y)
    for j,subkey in enumerate(word):
        out,lower=parent.level_lift(10,subkey,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',z) for name,z in lower]
        m.append((f'no_early_level11_hit{j}',sub(out,ell) if j<n-1 else sub(ell,out)))
    return q,m

def twelfth_req(key,y):
    n=10 if key.endswith('10') else 11;q=sub(add(y,scale(n,w)),ell)
    m=[('y>0',y),('y<omega11',sub(w,y)),('q>0',q),('q<omega11',sub(w,q)),
       ('lower_global_scope',v),('upper_global_scope',sub(om12,v)),
       ('twelfth_cut',sub(y,r12) if n==10 else sub(r12,y))]
    if key=='D10':m.append(('last_long_exterior',sub(y,add(r12,v))))
    if key=='E10':m.append(('last_long_interior',sub(add(r12,v),y)))
    if key=='D11':m.append(('eleven_step_exterior',sub(add(y,om12),v)))
    return q,m

def twelfth_lift(key,y):
    word=TWELFTH[key];n=len(word)
    pp=[add(y,scale(j,w)) for j in range(n)];q=sub(add(y,scale(n,w)),ell);pp.append(q)
    _,m=twelfth_req(key,y)
    for j,subkey in enumerate(word):
        out,lower=level11_lift(subkey,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',z) for name,z in lower]
        m.append((f'no_early_twelfth_hit{j}',sub(out,w) if j<n-1 else sub(w,out)))
    return q,m

def thirteenth_req(key,y):
    short=key=='A'
    q=add(y,delta13) if short else sub(y,cut13)
    m=[('y>0',y),('y<rho12',sub(r12,y)),('q>0',q),('q<rho12',sub(r12,q)),
       ('lower_global_scope',v),('upper_global_scope',sub(delta13,v)),
       ('thirteenth_cut',sub(cut13,y) if short else sub(y,cut13))]
    if key=='D':m.append(('third_source_exterior',sub(y,add(cut13,v))))
    if key=='E':m.append(('third_source_interior',sub(add(cut13,v),y)))
    return q,m

def thirteenth_lift(key,y):
    word=THIRTEENTH[key]
    if key=='A': pp=[y,add(y,om12),add(y,delta13)]
    else: pp=[y,add(y,om12),add(y,delta13),sub(y,cut13)]
    q=pp[-1];_,m=thirteenth_req(key,y)
    for j,subkey in enumerate(word):
        out,lower=twelfth_lift(subkey,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',z) for name,z in lower]
        m.append((f'no_early_thirteenth_hit{j}',sub(out,r12) if j<len(word)-1 else sub(r12,out)))
    return q,m

def geometry_audit():
    lower='CHECKED COMPOSITIONALLY IN ELEVENTH/TWELFTH/THIRTEENTH CELLS'
    e11={}
    for key in ELEVENTH:
        _,rr=level11_req(key,seed);_,m=level11_lift(key,seed);cond=RANGE+tuple(z for _,z in rr)
        item=audit(m,vertices(cond))
        if key in ('A','D'):item['entry_v_zero']=audit(m,vertices(cond+(sub(zero,v),)))
        if key in ('A','E'):item['endpoint_v_delta13']=audit(m,vertices(cond+(sub(v,delta13),sub(delta13,v))))
        e11[key]=item
    e12={}
    for key in TWELFTH:
        _,rr=twelfth_req(key,seed);_,m=twelfth_lift(key,seed);cond=RANGE+tuple(z for _,z in rr)
        item=audit(m,vertices(cond))
        if key in ('D10','D11'):item['entry_v_zero']=audit(m,vertices(cond+(sub(zero,v),)))
        if key in ('E10','D11'):item['endpoint_v_delta13']=audit(m,vertices(cond+(sub(v,delta13),sub(delta13,v))))
        e12[key]=item
    e13={}
    for key in THIRTEENTH:
        _,rr=thirteenth_req(key,seed);_,m=thirteenth_lift(key,seed);cond=RANGE+tuple(z for _,z in rr)
        item=audit(m,vertices(cond))
        if key in ('A','D'):item['entry_v_zero']=audit(m,vertices(cond+(sub(zero,v),)))
        if key in ('A','E'):item['endpoint_v_delta13']=audit(m,vertices(cond+(sub(v,delta13),sub(delta13,v))))
        e13[key]=item
    assert add(r12,om12)==w and sub(om12,r12)==delta13
    assert add(scale(2,cut13),scale(3,delta13))==w
    excess=sub(v,delta13)
    pp=[seed,add(seed,om12),add(seed,delta13)]
    gm=[]
    for j,subkey in enumerate(NEXT):
        out,lo=twelfth_lift(subkey,pp[j]);assert out==pp[j+1]
        gm += [(f'{j}:{name}',z) for name,z in lo]
        gm.append((f'no_early_hit{j}',sub(out,r12) if j<len(NEXT)-1 else sub(r12,out)))
    guard_cond=RANGE+(delta13,v,sub(om12,v),excess,sub(cut13,excess),seed,sub(excess,seed),sub(w,seed),sub(r12,seed))
    guard=audit(gm,vertices(guard_cond))
    return {
      'parameter':'v=u-c11=e-e97','new_exclusion_scope':'0<v<=delta13',
      'delta13_definition':'omega12-rho12','rechecked_GERM97_level10_contracts':lower,
      'eleventh_cells':e11,'twelfth_cells':e12,'thirteenth_cells':e13,
      'thirteenth_section':'0<y<rho12','thirteenth_map':'y -> y+delta13 mod rho12',
      'entry_words':['A','D'],'endpoint_words':['A','E'],
      'next_domain':'v=delta13+x; 0<x<rho12-delta13; 0<y<x',
      'next_thirteenth_word':NEXT,'next_guard':guard,'sampled_topology':False,
    }

def main():
    out={
      'pass':'SZ-KERNEL-EDGE-GERM-98','standing':'UNRATIFIED',
      'entry_commit':'4b1c24633f9e06b523857529c868ae36714e70a0',
      'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
      'new_exclusion_scope':'0<v<=delta13, v=e-e97; delta13=omega12-rho12',
      'matrix_namespace':'GERM-97 level-10 inputs; GERM-98-local eleventh/twelfth/thirteenth maps',
      'arithmetic':arithmetic(),'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
      'fourteenth_or_deeper_induction_used':False,'new_retained_coordinates':0,
      'full_lower_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
      'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE',
    }
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
