#!/usr/bin/env python3
"""GERM-101: ten-initial visits via complete fourteenth returns.

Proves 0<b<=35delta13, b=e-e100. Three twelfth and four thirteenth
formulas extend through b=rho12. Seventy-two complete fourteenth words,
three rational charts in four parameter regimes, common factor 9/8.
Exact intermediate source contracts and outward rational coefficients.
Run with assertions enabled. Unratified research, not Lean certification.
"""
from fractions import Fraction as F
from functools import partial
from pathlib import Path
import hashlib
import json

assert __debug__, 'Run without -O; assertions are part of the certificate.'
ROOT=Path(__file__).resolve().parents[1]
PIN='tools/sz_post_v_omega11_eleventh_transfer_audit.py'
PIN_SHA='5051313d43e18a288bf35a866d27a7f55253ffb559c051d037640a105c251d2e'
assert hashlib.sha256((ROOT/PIN).read_bytes()).hexdigest()==PIN_SHA
import sz_post_v_omega11_eleventh_transfer_audit as p
old,g77=p.old,p.g77
# Recompute, do not artificially narrow old intervals. More series terms
# are required as well as a finer rounding grid for the long products.
assert isinstance(old.log_box,partial)
old.SCALE=10**240
old.log_box=partial(old.log_box.func,terms=800)
product,det=p.product,p.det
TW={'C':['A1']*9+['B0'],'D':['A1']*9+['A0','B0'],'E':['A1']*10+['B0']}
TH={'A0':['D','C'],'A1':['E','C'],'B0':['D','C','C'],'B1':['E','C','C']}
WORDS={f'{s}/{n}':['A1']*s+['A0']*(n-s-1)+['B0']
       for n in (35,36) for s in range(n)}
WORDS['all/35']=['A1']*34+['B1']
CHARTS={'I':[[-581,-58],[814,82]],'II':[[-80,-579],[60,815]],
        'III':[[-581,-58],[814,82]],'IV':[[-57,-30],[82,40]]}
INDICES={'I':[f'{s}/{n}' for n in (35,36) for s in range(24)],
         'II':[f'{s}/{n}' for n in (35,36) for s in range(23,26)],
         'III':[f'{s}/{n}' for n in (35,36) for s in range(25,35)],
         'IV':['34/35','34/36','35/36','all/35']}
BOUNDS={'I':(0,23),'II':(23,25),'III':(25,34),'IV':(34,35)}
FACTOR=F(9,8)
NEXT=['A1']*35+['B1']
af,add,sub,vertices=p.af,p.add,p.sub,p.vertices
scale,audit=p.scale,p.audit
seed,ell,w,r=p.seed,p.ell,p.w,p.r12
b=sub(p.a,scale(9,w));d=sub(w,scale(2,r));tau=sub(r,scale(35,d))
cut=sub(r,d);zero=af()
RANGE=p.RANGE+(tau,sub(d,tau))


def arithmetic():
    aa,ss,mm=old.add,old.sub,old.mul
    h,k=(-4,4,-1),(4,-1,-1)
    kap=ss(k,mm(5,h));tt=ss(h,mm(5,kap));theta=ss(kap,mm(8,tt))
    al=ss(tt,mm(3,theta));be=ss(theta,al);ga=ss(al,be)
    xi=ss(mm(5,ga),be);om=ss(ga,mm(19,xi));eta=ss(xi,om)
    chi=ss(mm(2,om),xi);psi=ss(eta,chi);sig=ss(mm(3,psi),chi)
    rho=ss(psi,mm(3,sig));cc=ss(sig,rho);o10=ss(sig,mm(10,cc))
    ll=ss(cc,o10);ww=ss(cc,mm(4,ll));rr=ss(ll,mm(10,ww))
    dd=ss(ww,mm(2,rr));tau14=ss(rr,mm(35,dd));inc=mm(35,dd)
    L100=(13356636944,-11739684839,2261191167)
    L101=aa(L100,inc);top=aa((4,-1,0),mm(3,h))
    assert dd==(29487130972,-25917424123,4991978177)
    assert aa(mm(2,rr),dd)==ww
    assert aa(mm(35,ss(dd,tau14)),mm(36,tau14))==rr
    checks={'tau14_positive':tau14,'tau14_below_delta13':ss(dd,tau14),
      'formula_inside_eleventh':ss(ll,aa(mm(9,ww),rr)),
      'formula_inside_tenth':ss(cc,aa(aa(ll,mm(10,ww)),rr)),
      'formula_below_three_layers':ss(top,aa(L100,rr))}
    for j,shape in enumerate(p.RANGE):
        assert shape[2]==shape[3]==0
        checks[f'parent_shape_{j}']=aa(mm(shape[0],ga),mm(shape[1],be))
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(vec):return sum((q*z for q,z in zip(vec,logs)),old.box(0))
    boxes={name:enc(vec) for name,vec in checks.items()}
    assert all(z.lo>0 for z in boxes.values())
    return {'order_checks':{k:g77.show_box(z,42) for k,z in boxes.items()},
      'endpoint_prime_log_vector':L101,'endpoint_decimal':g77.show_box(enc(L101),42),
      'increment':'35delta13','increment_prime_log_vector':inc,
      'increment_decimal':g77.show_box(enc(inc),42),
      'tau14_prime_log_vector':tau14,'tau14_decimal':g77.show_box(enc(tau14),42),
      'remaining_new_formula_width':g77.show_box(enc(tau14),42),
      'remaining_parent_eleventh_width':g77.show_box(enc(ss(ll,aa(mm(9,ww),inc))),42),
      'remaining_three_layer_width':g77.show_box(enc(ss(top,L101)),42)}


def build_matrices():
    level11,pivots=p.build_matrices()
    level12={k:product(word,level11) for k,word in TW.items()}
    level13={k:product(word,level12) for k,word in TH.items()}
    return level12,level13,pivots


def rational_audit():
    m12,m13,pivots=build_matrices();spectra={}
    for level,lib in ((12,m12),(13,m13)):
        spectra[level]={}
        for key,M in lib.items():
            tr=M[0][0]+M[1][1];dd=det(M);disc=tr*tr-4*dd
            assert dd.lo>0 and dd.lo<=1<=dd.hi
            assert disc.hi<0 if (level,key) in ((12,'E'),(13,'A1')) else disc.lo>0
            spectra[level][key]={'trace':old.display_matrix([[tr]]),
                                'discriminant':old.display_matrix([[disc]])}
    matrices={k:product(word,m13) for k,word in WORDS.items()}
    assert len(matrices)==72
    cert={}
    for regime,indices in INDICES.items():
        C=CHARTS[regime]
        assert C[0][0]*C[1][1]-C[0][1]*C[1][0] =={'I':-430,'II':-30460,'III':-430,'IV':180}[regime]
        cert[regime]={}
        for key in indices:
            M=matrices[key];tr=M[0][0]+M[1][1]
            assert tr.lo>0 or tr.hi<0
            sign=1 if tr.lo>0 else -1
            item=g77.cone_test(M,C,sign,FACTOR)
            assert (tr*tr-4*det(M)).lo>0
            n=int(key.split('/')[1])
            item['original_step_count']=(n-1)*1189902283+1757196619
            cert[regime][key]=item
    M=product(NEXT,m13);tr=M[0][0]+M[1][1];dd=det(M);disc=tr*tr-4*dd
    assert dd.lo>0 and dd.lo<=1<=dd.hi and disc.hi<0
    assert F(-195,1000)<tr.lo<tr.hi<F(-194,1000)
    minima={reg:{name:str(min(F(z[name]) for z in items.values()))
                    for name in ('forward_lower','backward_lower')}
            for reg,items in cert.items()}
    return {'physical_recalculation':'FRESH PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
      'precision':{'grid':'10^240','log_series_terms':800},'layer_pivots':pivots,
      'local_spectra':spectra,'charts':CHARTS,'distinct_charts':3,
      'distinct_words':72,'chart_tests':sum(map(len,INDICES.values())),
      'common_factor':'9/8','certificates':cert,'minima':minima,
      'next_word':NEXT,'next_trace':old.display_matrix([[tr]]),
      'next_discriminant':old.display_matrix([[disc]])}


def twelfth_req(key,y):
    n=10 if key=='C' else 11;q=sub(add(y,scale(n,w)),ell)
    m=[('y>0',y),('y<w',sub(w,y)),('q>0',q),('q<w',sub(w,q)),
       ('lower_global_scope',b),('upper_global_scope',sub(r,b)),
       ('cut',sub(y,r) if n==10 else sub(r,y))]
    if key=='D':m.append(('source_exterior',sub(y,b)))
    if key=='E':m.append(('source_interior',sub(b,y)))
    return q,m


def twelfth_lift(key,y):
    q,m=twelfth_req(key,y)
    out,lo=p.twelfth_lift(TW[key],y);assert out==q
    return q,m+[(f'eleventh:{name}',z) for name,z in lo]


def thirteenth_req(key,y):
    short=key[0]=='A';q=add(y,d) if short else sub(y,cut)
    return q,[('y>0',y),('y<r',sub(r,y)),('q>0',q),('q<r',sub(r,q)),
      ('lower_global_scope',b),('upper_global_scope',sub(r,b)),
      ('cut',sub(cut,y) if short else sub(y,cut)),
      ('source_bit',sub(y,b) if key.endswith('0') else sub(b,y))]


def thirteenth_lift(key,y):
    q,m=thirteenth_req(key,y);word=TH[key]
    pp=[y,add(y,sub(w,r)),add(y,d)]
    if len(word)==3:pp.append(sub(y,cut))
    for j,subkey in enumerate(word):
        out,lo=twelfth_req(subkey,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',z) for name,z in lo]
        m.append((f'no_early13_{j}',sub(out,r) if j<len(word)-1 else sub(r,out)))
    assert pp[-1]==q
    return q,m


def fourteenth_lift(word,y):
    n=len(word);q=sub(add(y,scale(n,d)),r)
    pp=[add(y,scale(j,d)) for j in range(n)]+[q]
    m=[('y>0',y),('y<d',sub(d,y)),('q>0',q),('q<d',sub(d,q)),
       ('return_cut',sub(y,tau) if n==35 else sub(tau,y))]
    for j,key in enumerate(word):
        out,lo=thirteenth_req(key,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',z) for name,z in lo]
        m.append((f'no_early14_{j}',sub(out,d) if j<n-1 else sub(d,out)))
    return q,m


def cell_condition(key,y,q):
    prefix,n=key.split('/');n=int(n)
    common=(y,sub(d,y),q,sub(d,q))
    if prefix=='all':return common+(sub(b,add(y,scale(n-1,d))),)
    s=int(prefix)
    if s==0:return common+(sub(y,b),)
    return common+(sub(b,add(y,scale(s-1,d))),sub(add(y,scale(s,d)),b))


def geometry_audit():
    # Recheck the parent eleventh derivation at every tenth source;
    # earlier licensed identities are inherited through the pinned chain.
    lower={}
    for key in p.ELEVENTH:
        _,rr=p.eleventh_req(key,seed);_,m=p.eleventh_lift(key,seed)
        lower[key]=audit(m,vertices(p.RANGE+tuple(z for _,z in rr)))
    cells={}
    for level,lib,req,lift in ((12,TW,twelfth_req,twelfth_lift),
                              (13,TH,thirteenth_req,thirteenth_lift)):
        cells[level]={}
        for key in lib:
            _,rr=req(key,seed);_,m=lift(key,seed);cond=RANGE+tuple(z for _,z in rr)
            item=audit(m,vertices(cond))
            entry=key in (('C','D') if level==12 else ('A0','B0'))
            endpoint=key in (('C','E') if level==12 else ('A1','B1'))
            if entry:item['entry_b_zero']=audit(m,vertices(cond+(sub(zero,b),)))
            if endpoint:item['formula_endpoint_b_r']=audit(m,vertices(cond+(sub(b,r),)))
            cells[level][key]=item
    complete={}
    for regime,indices in INDICES.items():
        left,right=BOUNDS[regime];bounds=(sub(b,scale(left,d)),sub(scale(right,d),b))
        complete[regime]={}
        for key in indices:
            q,m=fourteenth_lift(WORDS[key],seed)
            cond=RANGE+bounds+cell_condition(key,seed,q)
            item=audit(m,vertices(cond))
            s,n=key.split('/');n=int(n)
            for j in range(left,right+1):
                if s==str(j) or (s=='all' and j>=n):
                    item[f'junction_{j}d']=audit(m,vertices(cond+(sub(b,scale(j,d)),sub(scale(j,d),b))))
            if regime=='IV' and key in ('34/35','35/36'):
                item['long_source_junction']=audit(m,vertices(cond+(sub(b,cut),sub(cut,b))))
            complete[regime][key]=item
    assert add(scale(2,sub(r,d)),scale(3,d))==w
    assert add(scale(35,sub(d,tau)),scale(36,tau))==r
    # First beyond-scope word: all 36 sources are interior.
    excess=sub(b,scale(35,d));q,m=fourteenth_lift(NEXT,seed)
    cond=RANGE+(excess,sub(tau,excess),seed,sub(excess,seed))
    guard=audit(m,vertices(cond))
    assert q==add(seed,sub(d,tau))
    return {'parameter':'b=e-e100=a-9omega11','formula_scope':'0<b<=rho12',
      'new_exclusion_scope':'0<b<=35delta13','rechecked_parent_eleventh':lower,
      'local_formula_cells':cells,'fourteenth_cells':complete,
      'fourteenth_section':'(0,delta13)','fourteenth_map':'y -> y-tau14 mod delta13',
      'tau14':'rho12-35delta13','entry_words':['0/35','0/36'],
      'endpoint_words':['all/35','35/36'],
      'next_domain':'b=35delta13+z; 0<y<z<tau14','next_guard':guard,
      'sampled_topology':False}


def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-101','standing':'UNRATIFIED',
      'entry_commit':'e80d69344ab2f3e191b4d96fd4363007df965707',
      'dependency_sha256':{PIN:PIN_SHA},'scope':'0<b<=35delta13, b=e-e100',
      'twelfth_words':TW,'thirteenth_words':TH,'fourteenth_words':WORDS,
      'arithmetic':arithmetic(),'rational_audit':rational_audit(),'geometry':geometry_audit(),
      'fifteenth_or_deeper_induction_used':False,'new_retained_coordinates':0,
      'full_lower_symbolic_suites_rerun':False,'complete_GERM60_reduction_rerun':False,
      'old_large_determinants_rerun':False,'canonical_cursor':'SZ-CROSS-COLLAR-3',
      'canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
