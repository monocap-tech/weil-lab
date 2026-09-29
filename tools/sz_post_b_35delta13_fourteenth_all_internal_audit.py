#!/usr/bin/env python3
"""GERM-102: fourteenth all-internal control via sixteenth returns.

Proves 0<z<=s15, z=e-e101, s15=delta13-tau14. Three fourteenth and five
fifteenth formulas hold through z=tau14. Eleven distinct complete sixteenth
words have thirteen tests in two fixed-parameter integer charts, factor 7.
All intermediate sources are checked. Run without -O. Unratified research.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of the certificate; run without -O.'
ROOT=Path(__file__).resolve().parents[1]
PIN='tools/sz_post_a_9omega11_twelfth_ten_visit_audit.py'
PIN_SHA='fc0d153bccf205823ef35b4cc4bfde85aeb4b261fcd0a88c4722b0a9f0f76a00'
assert hashlib.sha256((ROOT/PIN).read_bytes()).hexdigest()==PIN_SHA
import sz_post_a_9omega11_twelfth_ten_visit_audit as p
old,g77,product,det=p.old,p.g77,p.product,p.det
# Inputs A1/B0/B1 mean GERM-101-local thirteenth H1/J0/J1.
FOURTEENTH={'A':['A1']*34+['B1'], 'D':['A1']*35+['B0'], 'E':['A1']*35+['B1']}
FIFTEENTH={'H0':['D','A'],'H1':['E','A'],
           'J0':['D','D','A'],'J1':['E','D','A'],'J2':['E','E','A']}
LOW={(i,n):[f'J{i}']+['H0']*(n-1) for n in (4,5) for i in (0,1)}
HIGH={(s,n):['J1']+['H0']*(n-s-1)+['H1']*s for n in (4,5) for s in range(n)}
CHARTS={'low':[[50,50],[-72,-71]],'high':[[500,-1000],[-708,1413]]}
FACTOR=F(7)
NEXT=['J2','H1','H1','H1']
af,add,sub,vertices=p.af,p.add,p.sub,p.vertices
scale,audit=p.scale,p.audit
seed,d,tau=p.seed,p.d,p.tau
z=sub(p.b,scale(35,d));s15=sub(d,tau);t15=sub(scale(2,tau),d)
rho16=sub(s15,scale(4,t15));cut16=sub(t15,rho16);zero=af()
RANGE=p.RANGE+(t15,rho16,cut16)


def arithmetic():
    aa,ss,mm=old.add,old.sub,old.mul
    h,k=(-4,4,-1),(4,-1,-1)
    kap=ss(k,mm(5,h));tt=ss(h,mm(5,kap));theta=ss(kap,mm(8,tt))
    al=ss(tt,mm(3,theta));be=ss(theta,al);ga=ss(al,be)
    xi=ss(mm(5,ga),be);om=ss(ga,mm(19,xi));eta=ss(xi,om)
    chi=ss(mm(2,om),xi);psi=ss(eta,chi);sig=ss(mm(3,psi),chi)
    rho=ss(psi,mm(3,sig));cc=ss(sig,rho);o10=ss(sig,mm(10,cc))
    ll=ss(cc,o10);ww=ss(cc,mm(4,ll));rr=ss(ll,mm(10,ww))
    dd=ss(ww,mm(2,rr));tt14=ss(rr,mm(35,dd))
    ss15=ss(dd,tt14);tt15=ss(mm(2,tt14),dd)
    rr16=ss(ss15,mm(4,tt15));kk16=ss(tt15,rr16)
    L101=(1045406220964,-918849529144,176980427362)
    L102=aa(L101,ss15);top=aa((4,-1,0),mm(3,h))
    assert L102==(2121001134368,-1864233112976,359071602665)
    assert L102==aa((4,-1,0),aa(mm(-444660943128,h),mm(85589340463,k)))
    assert aa(ss15,tt15)==tt14 and aa(mm(2,ss15),tt15)==dd
    assert aa(mm(4,kk16),mm(5,rr16))==ss15
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(vec):return sum((q*v for q,v in zip(vec,logs)),old.box(0))
    checks={'s15_positive':ss15,'t15_positive':tt15,'rho16_positive':rr16,
      'rho16_below_t15':kk16,'s15_below_tau14':ss(tt14,ss15),
      'formula_inside_GERM100_eleventh':ss(ll,aa(mm(9,ww),rr)),
      'formula_below_three_layers':ss(top,aa(L101,tt14))}
    for j,shape in enumerate(p.RANGE):
        assert shape[2]==shape[3]==0
        checks[f'parent_shape_{j}']=aa(mm(shape[0],ga),mm(shape[1],be))
    boxes={name:enc(vec) for name,vec in checks.items()}
    assert all(v.lo>0 for v in boxes.values())
    residuals={'delta13':dd,'tau14':tt14,'s15':ss15,'t15':tt15,'rho16':rr16,'cut16':kk16}
    return {'order_checks':{k:g77.show_box(v,45) for k,v in boxes.items()},
      'residual_vectors':residuals,'residual_decimals':{k:g77.show_box(enc(v),45) for k,v in residuals.items()},
      'endpoint_prime_log_vector':L102,'endpoint_decimal':g77.show_box(enc(L102),45),
      'increment':'s15=delta13-tau14','increment_decimal':g77.show_box(enc(ss15),45),
      'remaining_new_formula_width':g77.show_box(enc(tt15),45),
      'remaining_GERM100_eleventh_width':g77.show_box(enc(aa(ww,tt15)),45),
      'remaining_three_layer_width':g77.show_box(enc(ss(top,L102)),45)}


def build_matrices():
    _,m13,pivots=p.build_matrices()
    m14={k:product(word,m13) for k,word in FOURTEENTH.items()}
    m15={k:product(word,m14) for k,word in FIFTEENTH.items()}
    return m14,m15,pivots


def rational_audit():
    m14,m15,pivots=build_matrices();spectra={}
    for level,lib in ((14,m14),(15,m15)):
        spectra[level]={}
        for key,M in lib.items():
            tr=M[0][0]+M[1][1];dd=det(M);disc=tr*tr-4*dd
            assert dd.lo>0 and dd.lo<=1<=dd.hi
            assert disc.hi<0 if (level,key) in ((14,'E'),(15,'H1')) else disc.lo>0
            spectra[level][key]={'trace':old.display_matrix([[tr]]),'discriminant':old.display_matrix([[disc]])}
    assert FOURTEENTH['A']==p.WORDS['all/35']
    assert FOURTEENTH['D']==p.WORDS['35/36'] and FOURTEENTH['E']==p.NEXT
    counts14={'A':42213874241,'D':43403776524,'E':43403776524}
    counts15={k:sum(counts14[v] for v in word) for k,word in FIFTEENTH.items()}
    certificates={}
    for regime,words in (('low',LOW),('high',HIGH)):
        C=CHARTS[regime]
        assert C[0][0]*C[1][1]-C[0][1]*C[1][0]=={'low':50,'high':-1500}[regime]
        certificates[regime]={}
        for key,word in words.items():
            M=product(word,m15);tr=M[0][0]+M[1][1]
            assert tr.lo>0 or tr.hi<0
            sign=1 if tr.lo>0 else -1
            item=g77.cone_test(M,C,sign,FACTOR)
            assert (tr*tr-4*det(M)).lo>0
            item['word']=word;item['original_step_count']=sum(counts15[k] for k in word)
            certificates[regime][f'{key[0]}/{key[1]}']=item
    distinct={tuple(word) for words in (LOW,HIGH) for word in words.values()}
    assert len(distinct)==11
    M=product(NEXT,m15);tr=M[0][0]+M[1][1];dd=det(M);disc=tr*tr-4*dd
    assert dd.lo>0 and dd.lo<=1<=dd.hi and disc.lo>0
    assert F(244,100)<tr.lo<tr.hi<F(245,100)
    C=CHARTS['high'];qm=g77.mm(g77.mm(g77.inverse(g77.mat(C)),M),g77.mat(C))
    assert any(v.hi<0 for row in qm for v in row) and any(v.lo>0 for row in qm for v in row)
    return {'physical_recalculation':'FRESH PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
      'precision':{'grid':'10^240','log_series_terms':800},'layer_pivots':pivots,
      'local_spectra':spectra,'charts':CHARTS,'distinct_words':11,'chart_tests':13,
      'common_factor':'7','certificates':certificates,'original_step_counts_15':counts15,
      'minimum_forward_lower':str(min(F(i['forward_lower']) for c in certificates.values() for i in c.values())),
      'minimum_backward_lower':str(min(F(i['backward_lower']) for c in certificates.values() for i in c.values())),
      'next_word':NEXT,'next_trace':old.display_matrix([[tr]]),
      'next_discriminant':old.display_matrix([[disc]]),'next_high_chart':old.display_matrix(qm),
      'next_status':'HYPERBOLIC; MIXED SIGNS IN CURRENT HIGH CHART'}


def fourteenth_req(key,y):
    short=key=='A';q=sub(y,tau) if short else add(y,s15)
    m=[('y>0',y),('y<d',sub(d,y)),('q>0',q),('q<d',sub(d,q)),
       ('lower_global_scope',z),('upper_global_scope',sub(tau,z)),
       ('return_cut',sub(y,tau) if short else sub(tau,y))]
    if key=='D':m.append(('source_exterior',sub(y,z)))
    if key=='E':m.append(('source_interior',sub(z,y)))
    return q,m


def fourteenth_lift(key,y):
    q,m=fourteenth_req(key,y);out,lo=p.fourteenth_lift(FOURTEENTH[key],y)
    assert out==q
    return q,m+[(f'parent13:{name}',v) for name,v in lo]


def fifteenth_req(key,y):
    short=key.startswith('H');q=sub(y,t15) if short else add(y,sub(s15,t15))
    m=[('y>0',y),('y<s15',sub(s15,y)),('q>0',q),('q<s15',sub(s15,q)),
       ('lower_global_scope',z),('upper_global_scope',sub(tau,z)),
       ('return_cut',sub(y,t15) if short else sub(t15,y))]
    if key.endswith('0'):m.append(('initial_exterior',sub(y,z)))
    else:m.append(('initial_interior',sub(z,y)))
    if key=='J1':m.append(('middle_exterior',sub(add(y,s15),z)))
    if key=='J2':m.append(('middle_interior',sub(z,add(y,s15))))
    return q,m


def fifteenth_lift(key,y):
    q,m=fifteenth_req(key,y);word=FIFTEENTH[key];n=len(word)
    pp=[add(y,scale(j,s15)) for j in range(n)]+[q]
    for j,subkey in enumerate(word):
        out,lo=fourteenth_req(subkey,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lo]
        m.append((f'no_early15_{j}',sub(out,s15) if j<n-1 else sub(s15,out)))
    return q,m


def sixteenth_lift(word,y):
    n=len(word);q=add(y,sub(s15,scale(n,t15)))
    pp=[y]+[add(y,sub(s15,scale(j,t15))) for j in range(1,n+1)]
    m=[('y>0',y),('y<t15',sub(t15,y)),('q>0',q),('q<t15',sub(t15,q)),
       ('return_cut',sub(cut16,y) if n==4 else sub(y,cut16))]
    for j,key in enumerate(word):
        out,lo=fifteenth_req(key,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lo]
        m.append((f'no_early16_{j}',sub(out,t15) if j<n-1 else sub(t15,out)))
    return q,m


def geometry_audit():
    # The parent geometry proves the contracts used below, including its
    # larger formula endpoint; its stopped cone inventory is not rerun here.
    pg=p.geometry_audit()
    parent_hash=hashlib.sha256(json.dumps(pg,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    formula={}
    for level,lib,req,lift in ((14,FOURTEENTH,fourteenth_req,fourteenth_lift),
                              (15,FIFTEENTH,fifteenth_req,fifteenth_lift)):
        formula[level]={}
        for key in lib:
            _,rr=req(key,seed);_,m=lift(key,seed);cond=RANGE+tuple(v for _,v in rr)
            item=audit(m,vertices(cond))
            entry=key in (('A','D') if level==14 else ('H0','J0'))
            endpoint=key in (('A','E') if level==14 else ('H1','J2'))
            if entry:item['entry_z_zero']=audit(m,vertices(cond+(sub(zero,z),)))
            if endpoint:item['formula_endpoint_z_tau']=audit(m,vertices(cond+(sub(z,tau),)))
            formula[level][key]=item
    low={}
    for (i,n),word in LOW.items():
        q,m=sixteenth_lift(word,seed)
        bit=sub(z,seed) if i else sub(seed,z)
        cond=RANGE+(z,sub(t15,z),seed,sub(t15,seed),q,sub(t15,q),bit)
        item=audit(m,vertices(cond))
        if i==0:item['entry']=audit(m,vertices(cond+(sub(zero,z),)))
        if i==1:item['chart_junction']=audit(m,vertices(cond+(sub(z,t15),)))
        low[f'{i}/{n}']=item
    high={}
    for (s,n),word in HIGH.items():
        q,m=sixteenth_lift(word,seed)
        cond=RANGE+(sub(z,t15),sub(s15,z),seed,sub(t15,seed),q,sub(t15,q))
        if s==0:cond+=(sub(add(q,t15),z),)
        else:cond+=(sub(z,add(q,scale(s,t15))),sub(add(q,scale(s+1,t15)),z))
        item=audit(m,vertices(cond))
        if s==0:item['chart_junction']=audit(m,vertices(cond+(sub(t15,z),)))
        if s==n-1:item['exclusion_endpoint_z_s15']=audit(m,vertices(cond+(sub(z,s15),)))
        for j in (2,3,4):
            if s==j-1:item[f'junction_{j}t15']=audit(m,vertices(cond+(sub(z,scale(j,t15)),sub(scale(j,t15),z))))
        high[f'{s}/{n}']=item
    assert add(s15,t15)==tau and add(scale(2,s15),t15)==d
    assert add(scale(4,cut16),scale(5,rho16))==s15
    # Above the new exclusion boundary, the middle fourteenth source of a
    # three-step fifteenth return is internal too: J1 -> J2.
    excess=sub(z,s15);q,m=sixteenth_lift(NEXT,seed)
    cond=RANGE+(excess,sub(cut16,excess),seed,sub(excess,seed))
    guard=audit(m,vertices(cond));assert q==add(seed,rho16)
    return {'parameter':'z=e-e101=b-35delta13','new_exclusion_scope':'0<z<=s15',
      'new_formula_scope':'0<z<=tau14, three fourteenth and five fifteenth maps',
      'parent_geometry_rechecked':True,'parent_geometry_compact_sha256':parent_hash,
      'formula_cells':formula,'sixteenth_cells':{'low':low,'high':high},
      'fifteenth_section':'(0,s15)','fifteenth_map':'y -> y-t15 mod s15',
      'sixteenth_section':'(0,t15)','sixteenth_map':'y -> y+rho16 mod t15',
      'endpoint_words':['H1^3 J1','H1^4 J1'],'formula_endpoint_maps':['H1','J2'],
      'next_domain':'z=s15+excess; 0<y<excess<cut16','next_guard':guard,
      'sampled_topology':False}


def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-102','standing':'UNRATIFIED',
      'entry_commit':'c5237bc961b4db5330df7beda7dca82323584b0c',
      'dependency_sha256':{PIN:PIN_SHA},'scope':'0<z<=s15, z=e-e101',
      'fourteenth_words':FOURTEENTH,'fifteenth_words':FIFTEENTH,
      'arithmetic':arithmetic(),'rational_audit':rational_audit(),'geometry':geometry_audit(),
      'seventeenth_or_deeper_induction_used':False,'new_retained_coordinates':0,
      'full_lower_symbolic_suites_rerun':False,'complete_GERM60_reduction_rerun':False,
      'old_large_determinants_rerun':False,'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
