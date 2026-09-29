#!/usr/bin/env python3
"""GERM-97: post-d=omega sixth transfer through u=c11, u=e-e96.

Three sixth and five seventh formulas extend to u=eta7. Nested source-bit
formulas at levels 8--11 have decreasing parameter scopes. All 23 legal
twelfth words on 0<u<=c11 share the unchanged GERM-96 chart, factor 2000.
Exact source domains, endpoint faces, and outward rational coefficients.
Run with assertions enabled. No thirteenth induction or new coordinate.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of the certificate; run without -O.'
ROOT=Path(__file__).resolve().parents[1]
PIN_PATH='tools/sz_post_delta_4c11_eleventh_all_u1_audit.py'
PIN_SHA='a82ca16fe4668962d072ac52453ad5313a098d69a256d50c0f1da31cace3a51a'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest()==PIN_SHA
import sz_post_delta_4c11_eleventh_all_u1_audit as parent
g91,g75,g77,old=parent.g91,parent.g75,parent.g77,parent.old
product,det=parent.product,parent.det
ATOMS={'E19':(15,19),'F19':(16,19),'F20':(16,20)}
SEVENTH={'U0':['F20','F20','E19'],'U1':['F20','F20','F19'],
 'V0':['F20','F20','E19','F20','E19'],
 'V1':['F20','F20','F19','F20','E19'],
 'V2':['F20','F20','F19','F20','F19']}
TIMES={8:(2,3),9:(3,4),10:(10,11),11:(4,5)}
# A/B = short/long return, suffix = initial-source bit. Local to each level.
WORDS={j:{f'{letter}{i}':([f'V{i}']+['U0']*(n-1) if j==8 else
                         [f'A{i}']+['B0']*(n-1))
          for letter,n in zip(('A','B'),nn) for i in (0,1)} for j,nn in TIMES.items()}
TWELFTH={f'{s}/{n}':['A1']*s+['A0']*(n-s-1)+['B0']
         for n in (10,11) for s in range(n)}
TWELFTH.update({f'all/{n}':['A1']*(n-1)+['B1'] for n in (10,11)})
CHART=parent.CHART
FACTOR=F(2000)
NEXT=['A1','B0','B0','B0','B1'] # level-10 inputs

# Exact affine coordinates: (constant, beta/gamma, zeta/gamma, source/gamma).
af,add,sub,vertices=g91.af,g91.add,g91.sub,g91.vertices
scale,audit=g91.scale,g91.audit
seed,eta,chi,psi,xi,omega=g91.seed,g91.eta,g91.chi,g91.psi,g91.xi,g91.omega
zero=af();u=sub(g91.d,omega)
sigma=sub(scale(3,psi),chi);rho=sub(psi,scale(3,sigma));c=sub(sigma,rho)
om10=sub(sigma,scale(10,c));ell=sub(c,om10);w=sub(c,scale(4,ell))
r12=sub(ell,scale(10,w));om12=sub(w,r12)
RANGE=tuple(dict.fromkeys(parent.RANGE))
PERIOD={8:chi,9:psi,10:sigma,11:c}
SECTION={8:psi,9:sigma,10:c,11:ell}


def arithmetic():
    a,s,m=old.add,old.sub,old.mul
    h,k=(-4,4,-1),(4,-1,-1)
    kap=s(k,m(5,h));tau=s(h,m(5,kap));th=s(kap,m(8,tau))
    al=s(tau,m(3,th));be=s(th,al);ga=s(al,be)
    xx=s(m(5,ga),be);oo=s(ga,m(19,xx));ee=s(xx,oo)
    ch=s(m(2,oo),xx);ps=s(ee,ch);ss=s(m(3,ps),ch)
    rr=s(ps,m(3,ss));cc=s(ss,rr);o10=s(ss,m(10,cc));ll=s(cc,o10)
    ww=s(cc,m(4,ll));r=s(ll,m(10,ww));o12=s(ww,r)
    L96=(152396,-133943,25798);L97=a(L96,ll);top=a((4,-1,0),m(3,h))
    assert ll==(-350856932,308382254,-59397781)
    assert L97==(-350704536,308248311,-59371983)
    assert L97==a((4,-1,0),a(m(73524059,h),m(-14152076,k)))
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(v):return sum((b*l for b,l in zip(v,logs)),old.box(0))
    checks={'eta_gt_psi':s(ee,ps),'psi_gt_sigma':s(ps,ss),'sigma_gt_c':s(ss,cc),
      'c_gt_c11':s(cc,ll),'c11_positive':ll,'10w_lt_c11':r,'c11_lt_11w':o12,
      'sixth_exterior_gap_through_u_eta':s(ga,m(17,xx)),
      'new_formula_endpoint_below_three_layers':s(top,a(L96,ee)),
      'next_guard_inside_tenth_scope':s(s(cc,ll),ww)}
    # Certify every fixed shape constraint used by the affine polytope audit.
    for j,v in enumerate(RANGE):
        assert v[2]==v[3]==0
        checks[f'fixed_shape_{j}']=a(m(v[0],ga),m(v[1],be))
    boxes={key:enc(v) for key,v in checks.items()};assert all(b.lo>0 for b in boxes.values())
    return {'order_checks':{key:g77.show_box(b,38) for key,b in boxes.items()},
      'endpoint_prime_log_vector':L97,'endpoint_h_k_vector':[73524059,-14152076],
      'endpoint_decimal':g77.show_box(enc(L97),38),
      'increment':'c11','increment_prime_log_vector':ll,'increment_decimal':g77.show_box(enc(ll),38),
      'remaining_sixth_seventh_formula_width':g77.show_box(enc(s(ee,ll)),38),
      'remaining_tenth_formula_width':g77.show_box(enc(s(cc,ll)),38),
      'remaining_three_layer_width':g77.show_box(enc(s(top,L97)),38)}


def rational_audit():
    assert old.SCALE==10**120
    original,pivots=g75.parent.parent.parent.parent.recalculate_returns()
    legacy=g75.parent.parent.parent
    first={k:product(v,original) for k,v in legacy.FIRST.items()}
    second={k:product(v,first) for k,v in legacy.SECOND.items()}
    boxes=json.loads((ROOT/'notes/_recurrence71_audit.json').read_text())['audit']['rational_audit']['second_section_maps']
    for key,b in second.items():
        for i in range(2):
            for j in range(2):
                lo,hi=map(F,boxes[key][i][j]);assert lo<=b[i][j].lo<=b[i][j].hi<=hi
    third={k:product(v,second) for k,v in g75.THIRD.items()}
    fourth={k:product(v,third) for k,v in g75.FOURTH.items()}
    fifth={k:product(v,fourth) for k,v in g75.FIFTH.items()}
    atoms={k:product(g75.sixth_word(*pair),fifth) for k,pair in ATOMS.items()}
    counts={}
    for key,pair in ATOMS.items():
        ow=g75.to_original(g75.sixth_word(*pair))
        assert legacy.determinant_exponent(ow)==0 and len(ow)==1654*pair[1]-297
        counts[key]=len(ow)
    assert ATOMS['F19']==parent.NEXT_PAIR
    assert SEVENTH['U0']==g91.SEVENTH['U2'] and SEVENTH['V0']==g91.SEVENTH['V3']
    spectra={6:{}}
    for key,b in atoms.items():
        dd=det(b);tr=b[0][0]+b[1][1];disc=tr*tr-4*dd
        assert dd.lo>0 and dd.lo<=1<=dd.hi and disc.hi<0
        spectra[6][key]={'trace':old.display_matrix([[tr]]),
          'discriminant':old.display_matrix([[disc]]),'original_step_count':counts[key]}
    maps=atoms;level_matrices={}
    for j,dictionary in [(7,SEVENTH)]+list(WORDS.items()):
        maps={k:product(v,maps) for k,v in dictionary.items()}
        counts={k:sum(counts[x] for x in v) for k,v in dictionary.items()}
        spectra[j]={};level_matrices[j]=maps
        for key,b in maps.items():
            dd=det(b);tr=b[0][0]+b[1][1];disc=tr*tr-4*dd
            assert dd.lo>0 and dd.lo<=1<=dd.hi
            assert disc.hi<0 or disc.lo>0
            spectra[j][key]={'trace':old.display_matrix([[tr]]),
                 'discriminant':old.display_matrix([[disc]]),'original_step_count':counts[key]}
    assert CHART==[[1,1],[-1,3]] and det(g75.mat(CHART)).lo==4
    assert counts=={'A0':55313611,'A1':55313611,'B0':69471837,'B1':69471837}
    cert={}
    for key,word in TWELFTH.items():
        s,n=key.split('/');n=int(n)
        sign=-1 if s=='all' else (-1)**(n+int(s)+1)
        b=product(word,maps);item=g77.cone_test(b,CHART,sign,FACTOR)
        tr=b[0][0]+b[1][1];assert (tr*tr-4*det(b)).lo>0
        count=sum(counts[x] for x in word);assert count==55313611*(n-1)+69471837
        item.update({'word':word,'original_step_count':count});cert[key]=item
    b=product(NEXT,level_matrices[10]);tr=b[0][0]+b[1][1];disc=tr*tr-4*det(b)
    assert F(40,100)<tr.lo<tr.hi<F(41,100) and disc.hi<0
    return {'physical_recalculation':'FRESH PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
      'precision':{'grid':'10^120','log_series_terms':400},'layer_pivots':pivots,
      'GERM71_box_regression':'CONTAINED; not rounded proof inputs','level_spectra':spectra,
      'chart':CHART,'common_forward_backward_factor':'2000','twentythree_twelfth_certificates':cert,
      'next_level10_word':NEXT,'next_trace':old.display_matrix([[tr]]),
      'next_discriminant':old.display_matrix([[disc]]),'next_status':'ELLIPTIC NEW ELEVENTH SOURCE WORD'}


def atom_req(key,y):
    short=key!='F20';q=add(y,omega) if short else sub(y,eta)
    m=[('y>0',y),('y<xi',sub(xi,y)),('q>0',q),('q<xi',sub(xi,q)),
       ('sixth_lower_global_scope',u),('sixth_upper_global_scope',sub(eta,u)),
       ('sixth_cut',sub(eta,y) if short else sub(y,eta))]
    if short:m.append(('sixteenth_visit_bit',sub(u,y) if key=='F19' else sub(y,u)))
    return q,m


def atom_lift(key,y):
    q,m=atom_req(key,y);out,lower=g75.sixth_lift(*ATOMS[key],y);assert out==q
    return q,m+[(f'fifth:{name}',v) for name,v in lower]


def seventh_req(key,z):
    wrap=key.startswith('V');q=add(z,sub(chi,psi)) if wrap else sub(z,psi)
    m=[('z>0',z),('z<chi',sub(chi,z)),('q>0',q),('q<chi',sub(chi,q)),
       ('seventh_lower_global_scope',u),('seventh_upper_global_scope',sub(eta,u)),
       ('seventh_cut',sub(psi,z) if wrap else sub(z,psi))]
    if key in ('U0','V0'):m.append(('initial_low_exterior',sub(z,u)))
    else:m.append(('initial_low_interior',sub(u,z)))
    if key=='V1':m.append(('last_low_exterior',sub(add(chi,z),u)))
    if key=='V2':m.append(('last_low_interior',sub(u,add(chi,z))))
    return q,m


def seventh_lift(key,z):
    q,m=seventh_req(key,z);word=SEVENTH[key];pp=g77.g76.seventh_positions(len(word),z)
    assert pp[-1]==add(scale(2,eta),q)
    for j,k in enumerate(word):
        out,lo=atom_req(k,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lo]
        m.append((f'no_early_hit{j}',sub(scale(2,eta),out) if j<len(word)-1 else sub(out,scale(2,eta))))
    return q,m


def level_req(level,key,y):
    period,section=PERIOD[level],SECTION[level]
    short=key[0]=='A';n=TIMES[level][0 if short else 1]
    cut=sub(scale(n+1 if short else n,section),period)
    q=add(y,sub(period,scale(n,section)))
    return q,[('y>0',y),('y<section',sub(section,y)),('q>0',q),('q<section',sub(section,q)),
      ('lower_global_scope',u),('upper_global_scope',sub(section,u)),
      ('return_cut',sub(cut,y) if short else sub(y,cut)),
      ('initial_source_bit',sub(u,y) if key[1]=='1' else sub(y,u))]


def descending_lift(level,word,y):
    period,section=PERIOD[level],SECTION[level];n=len(word)
    pp=[y]+[add(y,sub(period,scale(j,section))) for j in range(1,n+1)]
    m=[('source>0',y),('source<section',sub(section,y)),('target>0',pp[-1]),('target<section',sub(section,pp[-1]))]
    for j,k in enumerate(word):
        out,lo=seventh_req(k,pp[j]) if level==8 else level_req(level-1,k,pp[j])
        assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lo]
        m.append((f'no_early_hit{j}',sub(out,section) if j<n-1 else sub(section,out)))
    return pp[-1],m


def level_lift(level,key,y):
    q,m=level_req(level,key,y);out,lo=descending_lift(level,WORDS[level][key],y);assert out==q
    return q,m+lo


def twelfth_lift(key,y):
    word=TWELFTH[key];n=len(word)
    pp=[add(y,scale(j,w)) for j in range(n)];q=sub(add(y,scale(n,w)),ell);pp.append(q)
    m=[('y>0',y),('y<w',sub(w,y)),('q>0',q),('q<w',sub(w,q)),
       ('twelfth_cut',sub(y,r12) if n==10 else sub(r12,y))]
    for j,k in enumerate(word):
        out,lo=level_req(11,k,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',v) for name,v in lo]
        m.append((f'no_early_hit{j}',sub(out,w) if j<n-1 else sub(w,out)))
    return q,m


def geometry_audit():
    # Recheck the existing third/fourth/fifth domain contracts; no old cone suite.
    lower={}
    for j,lib,req,lift,upper in ((3,g75.THIRD,g75.third_req,g75.third_lift,g75.beta),
       (4,g75.FOURTH,g75.fourth_req,g75.fourth_lift,g75.beta),
       (5,g75.FIFTH,g75.fifth_req,g75.fifth_lift,af(1))):
        cells={}
        for key in lib:
            _,rr=req(key,seed);_,m=lift(key,seed)
            cells[key]=audit(m,vertices(g75.RANGE+(g75.zeta,sub(upper,g75.zeta))+tuple(v for _,v in rr)))
        lower[j]=cells
    cells={}
    for j,lib,req,lift,upper,entry,end in (
      (6,ATOMS,atom_req,atom_lift,eta,('E19','F20'),('F19','F20')),
      (7,SEVENTH,seventh_req,seventh_lift,eta,('U0','V0'),('U1','V2'))):
        cells[j]={}
        for key in lib:
            _,rr=req(key,seed);_,m=lift(key,seed);cond=RANGE+tuple(v for _,v in rr)
            item=audit(m,vertices(cond))
            if key in entry:item['entry_u_zero']=audit(m,vertices(cond+(sub(zero,u),)))
            if key in end:item['formula_endpoint']=audit(m,vertices(cond+(sub(u,upper),)))
            cells[j][key]=item
    for j in TIMES:
        cells[j]={}
        for key in WORDS[j]:
            _,rr=level_req(j,key,seed);_,m=level_lift(j,key,seed);cond=RANGE+tuple(v for _,v in rr)
            item=audit(m,vertices(cond))
            face=sub(zero,u) if key[1]=='0' else sub(u,SECTION[j])
            item['entry' if key[1]=='0' else 'formula_endpoint']=audit(m,vertices(cond+(face,)))
            cells[j][key]=item
    tw={}
    for key,word in TWELFTH.items():
        q,m=twelfth_lift(key,seed);n=len(word);s=key.split('/')[0]
        if s=='all':lo=add(seed,scale(n-1,w));hi=ell
        else:
            s=int(s);lo=zero if s==0 else add(seed,scale(s-1,w));hi=add(seed,scale(s,w))
        cond=RANGE+(u,sub(ell,u),seed,sub(w,seed),q,sub(w,q),sub(u,lo),sub(hi,u))
        item=audit(m,vertices(cond))
        if s==0:item['entry_u_zero']=audit(m,vertices(cond+(sub(zero,u),)))
        if s=='all':item['endpoint_u_c11']=audit(m,vertices(cond+(sub(u,ell),)))
        for j in range(1,11):
            if (s=='all' and j>=n) or (s!='all' and s==j):
                face=scale(j,w)
                item[f'junction_u_{j}_omega11']=audit(m,vertices(cond+(sub(u,face),sub(face,u))))
        tw[key]=item
    assert add(eta,omega)==xi and add(chi,psi)==eta
    assert add(scale(3,sub(chi,psi)),scale(5,psi))==xi
    for j in TIMES:
        period,section=PERIOD[j],SECTION[j];n=TIMES[j][0]
        cut=sub(scale(n+1,section),period);res=sub(period,scale(n,section))
        assert add(cut,res)==section and add(scale(n,cut),scale(n+1,res))==period
    assert add(scale(10,om12),scale(11,r12))==ell
    assert g75.zeta==add(add(scale(15,xi),omega),u)
    # Next changed eleventh word for u=c11+v, cut11<y<cut11+v, 0<v<w.
    excess=sub(u,ell);cut11=sub(ell,w);q,m=descending_lift(11,NEXT,seed)
    cond=RANGE+(excess,sub(w,excess),sub(seed,cut11),sub(add(cut11,excess),seed))
    guard=audit(m,vertices(cond));assert q==sub(seed,cut11)
    return {'parameter':'u=e-e96=GERM91 d-omega','new_exclusion_scope':'0<u<=c11',
      'rechecked_lower_geometry':lower,'formula_cells':cells,'twelfth_cells':tw,
      'formula_scopes':{'sixth_seventh':'0<u<=eta7','eighth':'0<u<=psi7',
        'ninth':'0<u<=sigma8','tenth':'0<u<=c10','eleventh':'0<u<=c11'},
      'twelfth_map':'y -> y-rho12 mod omega11','endpoint_words':['B1 A1^9','B1 A1^10'],
      'physical_field':'W(t0+y); t0=h-beta+gamma-xi+2eta7',
      'next_domain':'u=c11+v; 0<v<omega11; c11-omega11<y<c11-omega11+v',
      'next_level10_word':NEXT,'next_guard':guard,'sampled_topology':False}


def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-97','standing':'UNRATIFIED',
      'entry_commit':'6c10a79b5b8b486acd5ed8836937fda3bb680dcf',
      'direct_dependency_sha256':{PIN_PATH:PIN_SHA},'sixth_atoms':ATOMS,
      'seventh_words':SEVENTH,'level_8_to_11_words':WORDS,'twelfth_words':TWELFTH,
      'matrix_namespace':'A0/A1/B0/B1 are distinct GERM-97-local names at each return level',
      'arithmetic':arithmetic(),'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
      'thirteenth_or_deeper_induction_used':False,'new_retained_coordinates':0,
      'full_lower_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
      'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
