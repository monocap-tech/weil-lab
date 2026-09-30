#!/usr/bin/env python3
"""GERM-103: post-z=s15 double-internal transfer and full formula-window closure.

Proves 0<epsilon<=t15, epsilon=e-e102. Four sixteenth formulas hold on the
full remaining GERM-102 formula interval. Thirteen distinct complete
seventeenth returns have two parameter-fixed rational cone charts, factor 20.
Every intermediate source is checked. No eighteenth induction or new state.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
assert __debug__, 'Assertions are part of the certificate; run without -O.'
ROOT=Path(__file__).resolve().parents[1]
PIN='tools/sz_post_b_35delta13_fourteenth_all_internal_audit.py'
PIN_SHA='bc9f783b9c9c89072e5c6a468cf29d3dd98e85299bd9cf3cb274f078ea247a5e'
assert hashlib.sha256((ROOT/PIN).read_bytes()).hexdigest()==PIN_SHA
import sz_post_b_35delta13_fourteenth_all_internal_audit as p
old,g77,product,det=p.old,p.g77,p.product,p.det
g101,g100=p.p,p.p.p
SIXTEENTH={'A0':['J1']+['H1']*3,'A1':['J2']+['H1']*3,
           'B0':['J1']+['H1']*4,'B1':['J2']+['H1']*4}
LOW={(i,n):[f'A{i}']+['B0']*(n-1) for n in (5,6) for i in (0,1)}
HIGH={(s,n):['A1']+['B0']*(n-s-1)+['B1']*s for n in (5,6) for s in range(n)}
CHARTS={'low':[[1,1],[F(-2827,2000),F(-27,20)]],
        'high':[[1,1],[F(-279,200),F(-283,200)]]}
FACTOR=F(20)
af,add,sub,vertices=p.af,p.add,p.sub,p.vertices
scale,audit=p.scale,p.audit
seed,d,tau=p.seed,p.d,p.tau
z=p.z;s15=p.s15;t15=p.t15;rho16=p.rho16;cut16=p.cut16
epsilon=sub(z,s15);rho17=sub(t15,scale(5,cut16));cut17=sub(cut16,rho17);zero=af()
RANGE=p.RANGE+(rho17,cut17)

def arithmetic():
    a,s,m=old.add,old.sub,old.mul
    h,k=(-4,4,-1),(4,-1,-1)
    kap=s(k,m(5,h));tt=s(h,m(5,kap));theta=s(kap,m(8,tt));al=s(tt,m(3,theta));be=s(theta,al);ga=s(al,be)
    xi=s(m(5,ga),be);om=s(ga,m(19,xi));eta=s(xi,om);chi=s(m(2,om),xi);psi=s(eta,chi);sig=s(m(3,psi),chi)
    rho=s(psi,m(3,sig));cc=s(sig,rho);o10=s(sig,m(10,cc));ell=s(cc,o10);w=s(cc,m(4,ell));r12=s(ell,m(10,w));d13=s(w,m(2,r12));tau14=s(r12,m(35,d13));ss15=s(d13,tau14);tt15=s(m(2,tau14),d13)
    rr16=s(ss15,m(4,tt15));ct16=s(tt15,rr16);rr17=s(tt15,m(5,ct16));ct17=s(ct16,rr17)
    L102=(2121001134368,-1864233112976,359071602665);L103=a(L102,tt15);top=a((4,-1,0),m(3,h))
    assert L103==(-701561468,616630565,-118769764)
    assert L103==a((4,-1,0),a(m(147080066,h),m(-28310302,k)))
    assert a(scale(5,ct17),scale(6,rr17))==tt15
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(v):return sum((q*x for q,x in zip(v,logs)),old.box(0))
    checks={'t15_positive':tt15,'rho17_positive':rr17,'cut17_positive':ct17,
            'formula_endpoint_inside_GERM100':w,'endpoint_below_three_layers':s(top,L103)}
    boxes={k:enc(v) for k,v in checks.items()};assert all(v.lo>0 for v in boxes.values())
    return {'order_checks':{k:g77.show_box(v,48) for k,v in boxes.items()},
      'residual_vectors':{'t15':tt15,'rho17':rr17,'cut17':ct17},
      'endpoint_prime_log_vector':L103,'endpoint_h_k_vector':[147080066,-28310302],
      'endpoint_decimal':g77.show_box(enc(L103),48),'increment':'t15','increment_decimal':g77.show_box(enc(tt15),48),
      'remaining_GERM100_eleventh_width':g77.show_box(enc(w),48),
      'remaining_three_layer_width':g77.show_box(enc(s(top,L103)),48),
      'seventeenth_tower_identity':'5cut17+6rho17=t15'}

def build_matrices():
    m14,m15,piv=p.build_matrices()
    m16={k:product(word,m15) for k,word in SIXTEENTH.items()}
    return m16,piv

def rational_audit():
    m16,piv=build_matrices();spectra={}
    for k,M in m16.items():
        tr=M[0][0]+M[1][1];dd=det(M);disc=tr*tr-4*dd
        assert dd.lo>0 and dd.lo<=1<=dd.hi
        assert disc.lo>0
        spectra[k]={'trace':old.display_matrix([[tr]]),'discriminant':old.display_matrix([[disc]])}
    cert={};distinct=set();counts16={'A0':385874379584,'A1':385874379584,'B0':471492030349,'B1':471492030349}
    for reg,lib in (('low',LOW),('high',HIGH)):
        C=CHARTS[reg];cert[reg]={}
        for key,word in lib.items():
            M=product(word,m16);tr=M[0][0]+M[1][1];assert tr.lo>0 or tr.hi<0
            sg=1 if tr.lo>0 else -1;item=g77.cone_test(M,C,sg,FACTOR)
            assert (tr*tr-4*det(M)).lo>0
            item.update({'word':word,'original_step_count':sum(counts16[x] for x in word)})
            cert[reg][f'{key[0]}/{key[1]}']=item;distinct.add(tuple(word))
    assert len(distinct)==13
    l11,_=g100.build_matrices();next_word=['A1']*9+['B1'];M=product(next_word,l11);tr=M[0][0]+M[1][1];dd=det(M);disc=tr*tr-4*dd
    assert dd.lo>0 and dd.lo<=1<=dd.hi and disc.hi<0
    return {'physical_recalculation':'INHERITED PINNED 10^240 / 800-TERM STACK; GERM-102 REPLAYED',
      'layer_pivots':piv,'local_spectra':spectra,'charts':{k:[[str(x) for x in r] for r in C] for k,C in CHARTS.items()},
      'chart_determinants':['127/2000','-1/50'],'common_factor':'20','distinct_words':13,'chart_tests':15,'certificates':cert,
      'minimum_forward_lower':str(min(F(i['forward_lower']) for c in cert.values() for i in c.values())),
      'minimum_backward_lower':str(min(F(i['backward_lower']) for c in cert.values() for i in c.values())),
      'next_word':next_word,'next_trace':old.display_matrix([[tr]]),'next_discriminant':old.display_matrix([[disc]]),
      'next_status':'ELLIPTIC CHANGED TEN-STEP TWELFTH SOURCE WORD'}

def sixteenth_req(key,y):
    short=key.startswith('A');n=4 if short else 5;q=add(y,sub(s15,scale(n,t15)))
    return q,[('y>0',y),('y<t15',sub(t15,y)),('q>0',q),('q<t15',sub(t15,q)),
      ('lower_global_scope',epsilon),('upper_global_scope',sub(t15,epsilon)),
      ('return_cut',sub(cut16,y) if short else sub(y,cut16)),
      ('new_source_bit',sub(y,epsilon) if key.endswith('0') else sub(epsilon,y))]

def sixteenth_lift(key,y):
    q,m=sixteenth_req(key,y);word=SIXTEENTH[key];n=len(word)
    pp=[y]+[add(y,sub(s15,scale(j,t15))) for j in range(1,n+1)];assert pp[-1]==q
    for j,subkey in enumerate(word):
        out,lo=p.fifteenth_req(subkey,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lo]
        m.append((f'no_early16_{j}',sub(out,t15) if j<n-1 else sub(t15,out)))
    return q,m

def seventeenth_lift(word,y):
    n=len(word);q=add(y,sub(t15,scale(n,cut16)))
    pp=[y]+[add(y,sub(t15,scale(j,cut16))) for j in range(1,n+1)];assert pp[-1]==q
    m=[('y>0',y),('y<cut16',sub(cut16,y)),('q>0',q),('q<cut16',sub(cut16,q)),
       ('return_cut',sub(cut17,y) if n==5 else sub(y,cut17))]
    for j,key in enumerate(word):
        out,lo=sixteenth_req(key,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lo]
        m.append((f'no_early17_{j}',sub(out,cut16) if j<n-1 else sub(cut16,out)))
    return q,m

def geometry_audit():
    pg=p.geometry_audit();parent_hash=hashlib.sha256(json.dumps(pg,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    formulas={}
    for key in SIXTEENTH:
        _,rr=sixteenth_req(key,seed);_,m=sixteenth_lift(key,seed);cond=RANGE+tuple(v for _,v in rr)
        item=audit(m,vertices(cond))
        if key.endswith('0'):item['entry_epsilon_zero']=audit(m,vertices(cond+(sub(zero,epsilon),)))
        if key.endswith('1'):item['formula_endpoint_epsilon_t15']=audit(m,vertices(cond+(sub(epsilon,t15),sub(t15,epsilon))))
        formulas[key]=item
    low={}
    for (i,n),word in LOW.items():
        q,m=seventeenth_lift(word,seed);bit=sub(seed,epsilon) if i==0 else sub(epsilon,seed)
        cond=RANGE+(epsilon,sub(cut16,epsilon),seed,sub(cut16,seed),q,sub(cut16,q),bit)
        item=audit(m,vertices(cond))
        if i==0:item['entry']=audit(m,vertices(cond+(sub(zero,epsilon),)))
        if i==1:item['chart_junction']=audit(m,vertices(cond+(sub(epsilon,cut16),sub(cut16,epsilon))))
        low[f'{i}/{n}']=item
    high={}
    for (s,n),word in HIGH.items():
        q,m=seventeenth_lift(word,seed);cond=RANGE+(sub(epsilon,cut16),sub(t15,epsilon),seed,sub(cut16,seed),q,sub(cut16,q))
        if s==0:cond+=(sub(add(q,cut16),epsilon),)
        else:cond+=(sub(epsilon,add(q,scale(s,cut16))),sub(add(q,scale(s+1,cut16)),epsilon))
        item=audit(m,vertices(cond))
        if s==0:item['chart_junction']=audit(m,vertices(cond+(sub(epsilon,cut16),sub(cut16,epsilon))))
        if s==n-1:item['formula_endpoint']=audit(m,vertices(cond+(sub(epsilon,t15),sub(t15,epsilon))))
        high[f'{s}/{n}']=item
    assert add(scale(5,cut17),scale(6,rho17))==t15
    excess=sub(z,tau);y=seed;word=['A1']*9+['B1'];n=10;q=sub(add(y,scale(n,g100.w)),g100.ell)
    pp=[add(y,scale(j,g100.w)) for j in range(n)]+[q];gm=[]
    for j,key in enumerate(word):
        out,lo=g100.eleventh_req(key,pp[j]);assert out==pp[j+1]
        gm += [(f'{j}:{name}',v) for name,v in lo]
        gm.append((f'no_early_twelfth_{j}',sub(out,g100.w) if j<n-1 else sub(g100.w,out)))
    guard_cond=g100.RANGE+(excess,sub(sub(g100.w,g100.r12),excess),sub(y,g100.r12),sub(add(g100.r12,excess),y),sub(g100.w,y))
    guard=audit(gm,vertices(guard_cond))
    return {'parameter':'epsilon=z-s15=e-e102','new_exclusion_scope':'0<epsilon<=t15','parent_geometry_rechecked':True,
      'parent_geometry_compact_sha256':parent_hash,'sixteenth_formula_cells':formulas,
      'seventeenth_section':'(0,cut16)','seventeenth_map':'y -> y+rho17 mod cut16',
      'seventeenth_cells':{'low':low,'high':high},'entry_words':['A0/B0^4','A0/B0^5'],
      'endpoint_words':['A1/B1^4','A1/B1^5'],'next_domain':'z=tau14+excess; rho12<y<rho12+excess',
      'next_guard':guard,'sampled_topology':False}

def main():
    print(json.dumps({'pass':'SZ-KERNEL-EDGE-GERM-103','standing':'UNRATIFIED','entry_commit':'26cc010882c02069da2d7298f530e710f116db58',
      'dependency_sha256':{PIN:PIN_SHA},'scope':'0<epsilon<=t15, epsilon=e-e102','sixteenth_words':SIXTEENTH,
      'seventeenth_low_words':{f'{k[0]}/{k[1]}':v for k,v in LOW.items()},'seventeenth_high_words':{f'{k[0]}/{k[1]}':v for k,v in HIGH.items()},
      'arithmetic':arithmetic(),'rational_audit':rational_audit(),'geometry':geometry_audit(),
      'eighteenth_or_deeper_induction_used':False,'new_retained_coordinates':0,'full_lower_symbolic_suites_rerun':False,
      'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'},indent=2))
if __name__=='__main__':main()
