#!/usr/bin/env python3
"""GERM-75: fourth-section self-overlap and thirty exterior sixth returns.

New exclusion: 3h-beta < e <= 3h-beta+14xi, xi=5gamma-beta.
Fresh outward rational source solves; typed affine-domain contracts at every
intermediate source. Parent full suites and large determinants are not run.
Run with assertions enabled, without -O. Dependency hashes are checked.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of this certificate; do not use -O.'
ROOT=Path(__file__).resolve().parents[1]
PIN_PATH='tools/sz_fourth_section_internal_wrap_audit.py'
PIN_SHA='455da5af8ed16e6c3de3a03004e7232df3c73f24b62e27686ae449bd041ca5b1'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest()==PIN_SHA
import sz_fourth_section_internal_wrap_audit as parent
old=parent.old
old.SCALE=10**60
mat,mm,product=parent.mat,parent.mm,parent.product
inverse,det=parent.inverse,parent.det
af,add,sub,val,vertices=parent.af,parent.add,parent.sub,parent.val,parent.vertices

def scale(n,x): return tuple(n*t for t in x)
def expand(word,dictionary): return [a for k in word for a in dictionary[k]]

# Chronological words. N is the NEW inside-to-inside nonwrap (3 letters),
# distinct from the internal wrap I (4 letters).
THIRD={'Q':['01-','11+','11+'], 'N':['11-','11+','11+'],
       'P':['11-','11+','11+','10+'], 'I':['11-','11+','11+','11+']}
FOURTH={'00+':['Q','P'], '01+':['Q','I'], '11+':['N','I'],
        '00-':['Q','I','P'], '10-':['N','I','P'], '11-':['N','I','I']}
FIFTH={}
for k in FOURTH:
    i,j=int(k[0]),int(k[1]); n=5 if k[-1]=='+' else 4
    FIFTH[k]=['10-' if i else '00-']+['00+']*(n-2)+['01+' if j else '00+']

def sixth_word(s,n):
    if s==0: return ['00+']*(n-1)+['00-']
    return ['00+']*(n-s-1)+['01+']+['11+']*(s-1)+['10-']
SIXTH={f'{s}/{n}':sixth_word(s,n) for n in (19,20) for s in range(15)}
assert len(SIXTH)==30

def to_original(word):
    second=expand(expand(expand(word,FIFTH),FOURTH),THIRD)
    return parent.parent.parent.expand_original(second)

def rational_audit():
    original,pivots=parent.parent.parent.parent.recalculate_returns()
    legacy=parent.parent.parent
    first={k:product(w,original) for k,w in legacy.FIRST.items()}
    second={k:product(w,first) for k,w in legacy.SECOND.items()}
    fixture=json.loads((ROOT/'notes/_recurrence71_audit.json').read_text())
    boxes=fixture['audit']['rational_audit']['second_section_maps']
    for k,b in second.items():
        for i in range(2):
            for j in range(2):
                lo,hi=map(F,boxes[k][i][j]); assert lo<=b[i][j].lo<=b[i][j].hi<=hi
    third={k:product(w,second) for k,w in THIRD.items()}
    fourth={k:product(w,third) for k,w in FOURTH.items()}
    fifth={k:product(w,fourth) for k,w in FIFTH.items()}
    ex=legacy.determinant_exponent
    for k,w in THIRD.items():
        assert ex(legacy.expand_original(w))=={'Q':-1,'N':0,'P':1,'I':0}[k]
        assert det(third[k]).lo>0
    for level,lib,dictionary in ((4,fourth,FOURTH),(5,fifth,FIFTH)):
        for k,w in dictionary.items():
            w3=w if level==4 else expand(w,FOURTH)
            ow=legacy.expand_original(expand(w3,THIRD))
            assert ex(ow)==int(k[0])-int(k[1]); assert det(lib[k]).lo>0
    chart=[[-1,4],[1,F(-48,5)]]
    answer={}
    for k,w in SIXTH.items():
        s,n=map(int,k.split('/')); b=product(w,fifth)
        # No overall sign changes are needed for this entire library.
        item=parent.parent.cone_test(b,chart,1,F(3))
        ow=to_original(w)
        assert len(ow)==1654*n-297 and ex(ow)==0
        item.update({'fifth_word':w,'original_step_count':len(ow),
            'original_word_sha256':hashlib.sha256(json.dumps(ow,separators=(',',':')).encode()).hexdigest()})
        answer[k]=item
    # Immediate above-scope N=20, s=15 word is genuinely elliptic.
    guard=sixth_word(15,20); b=product(guard,fifth)
    tr=b[0][0]+b[1][1]; d=det(b); disc=tr*tr-4*d
    assert F(132,100)<tr.lo<tr.hi<F(133,100) and d.lo>0 and disc.hi<0
    assert ex(to_original(guard))==0
    return {'physical_maps':'FRESH OUTWARD RATIONAL PAIRED-SOURCE SOLVES',
        'grid':'10^60','layer_pivots':pivots,
        'second_map_regression':'CONTAINED IN PINNED GERM-71 BOXES',
        'fourth_maps':{k:old.display_matrix(b) for k,b in fourth.items()},
        'fifth_maps':{k:old.display_matrix(b) for k,b in fifth.items()},
        'chart':[['-1','4'],['1','-48/5']], 'common_forward_backward_factor':'3',
        'thirty_sixth_returns':answer,
        'above_scope_word':guard,'above_scope_trace':old.display_matrix([[tr]]),
        'above_scope_determinant':old.display_matrix([[d]]),
        'above_scope_discriminant':old.display_matrix([[disc]])}

# gamma=1, coordinates (r=beta/gamma, zeta/gamma, source/gamma).
zero,one=af(),af(1)
beta,zeta,seed=af(r=1),af(eta=1),af(z=1)
alpha=add(beta,one); theta=add(scale(2,beta),one)
tau=add(scale(7,beta),af(4)); epsilon=add(alpha,zeta)
zeta2=add(sub(tau,theta),epsilon)
xi=sub(af(5),beta); omega=sub(one,scale(19,xi))
RANGE=(sub(beta,af(F(94,19))),sub(af(F(99,20)),beta))

@lru_cache(None)
def second_template(k): return parent.parent.second_template(k)

def second_lift(k,y):
    def subst(a):
        return add(add(scale(a[0],theta),scale(a[1],tau)),
                   add(scale(a[2],zeta2),scale(a[3],y)))
    target,margins=second_template(k)
    return subst(target),[(name,subst(a)) for name,a in margins]

def audit(margins,vv):
    assert vv, 'Empty certificate cell.'
    weak=[]
    for name,a in margins:
        vals=[val(a,v) for v in vv]
        assert min(vals)>=0,(name,a,min(vals))
        if max(vals)==0:
            assert name.endswith('global_scope'),(name,a)
            weak.append(name)
    return {'vertices':len(vv),'checked_margins':len(margins),'weak_global':weak}

def third_req(k,v):
    wrap=k in ('P','I'); si=k!='Q'; tj=k!='P'
    target=add(v,beta) if wrap else sub(v,alpha)
    return target,[('v>0',v),('v<theta',sub(theta,v)),('target>0',target),
        ('target<theta',sub(theta,target)),
        ('source_bit',sub(epsilon,v) if si else sub(v,epsilon)),
        ('target_bit',sub(epsilon,target) if tj else sub(target,epsilon)),
        ('third_cut',sub(alpha,v) if wrap else sub(v,alpha)),
        ('third_global_scope',sub(beta,zeta))]

def third_lift(k,v):
    target,m=third_req(k,v); word=THIRD[k]; n=len(word)
    pp=[add(sub(tau,theta),v)]+[add(v,scale(j,theta)) for j in range(n)]
    assert pp[-1]==add(sub(tau,theta),target)
    bits=[int(k!='Q')]+[1]*(n-1)+[int(k!='P')]
    assert word==[f'{bits[j]}{bits[j+1]}'+('-' if j==0 else '+') for j in range(n)]
    for j,key in enumerate(word):
        y,lower=second_lift(key,pp[j]); assert y==pp[j+1]
        m += [(f'{j}:{name}',a) for name,a in lower]
        m += [(f'earlier_hit{j}',sub(sub(tau,theta),y) if j<n-1 else sub(y,sub(tau,theta)))]
    return target,m

def fourth_req(k,w):
    i,j=int(k[0]),int(k[1]); wrap=k[-1]=='-'
    target=add(w,sub(beta,one)) if wrap else sub(w,one)
    return target,[('w>0',w),('w<beta',sub(beta,w)),('target>0',target),
        ('target<beta',sub(beta,target)),('fourth_cut',sub(one,w) if wrap else sub(w,one)),
        ('source_bit',sub(zeta,w) if i else sub(w,zeta)),
        ('target_bit',sub(zeta,target) if j else sub(target,zeta)),
        ('fourth_global_scope',sub(beta,zeta))]

def fourth_lift(k,w):
    target,m=fourth_req(k,w); word=FOURTH[k]
    pp=[add(alpha,w),w,add(w,beta)]
    if k[-1]=='-': pp.append(add(w,scale(2,beta)))
    assert pp[-1]==add(alpha,target)
    for j,key in enumerate(word):
        v,lower=third_req(key,pp[j]); assert v==pp[j+1]
        m += [(f'{j}:{name}',a) for name,a in lower]
        m += [(f'earlier_hit{j}',sub(alpha,v) if j<len(word)-1 else sub(v,alpha))]
    return target,m

def fifth_req(k,z):
    i,j=int(k[0]),int(k[1]); n=4 if k[-1]=='-' else 5
    target=add(z,sub(beta,af(n)))
    return target,[('z>0',z),('z<gamma',sub(one,z)),('target>0',target),
        ('target<gamma',sub(one,target)),('fifth_cut',sub(xi,z) if n==4 else sub(z,xi)),
        ('source_bit',sub(zeta,z) if i else sub(z,zeta)),
        ('target_bit',sub(zeta,target) if j else sub(target,zeta)),
        ('fifth_global_scope',sub(one,zeta))]

def fifth_lift(k,z):
    target,m=fifth_req(k,z); n=4 if k[-1]=='-' else 5
    pp=[z]+[add(z,sub(beta,af(j))) for j in range(1,n+1)]
    assert pp[-1]==target
    for j,key in enumerate(FIFTH[k]):
        w,lower=fourth_req(key,pp[j]); assert w==pp[j+1]
        m += [(f'{j}:{name}',a) for name,a in lower]
        m += [(f'earlier_hit{j}',sub(w,one) if j<n-1 else sub(one,w))]
    return target,m

def sixth_lift(s,n,y):
    pp=[add(sub(one,scale(j+1,xi)),y) for j in range(n)]
    q=pp[-1]; pp.append(add(sub(one,xi),q))
    m=[('y>0',y),('y<xi',sub(xi,y)),('q>0',q),('q<xi',sub(xi,q)),
       ('sixth_global_scope',sub(sub(one,xi),zeta))]
    word=sixth_word(s,n)
    for j,key in enumerate(word):
        bit=lambda index: int(n-s<=index<n) if s else 0
        assert key==f'{bit(j)}{bit(j+1)}'+('-' if j==n-1 else '+')
        z,lower=fifth_req(key,pp[j]); assert z==pp[j+1]
        m += [(f'{j}:{name}',a) for name,a in lower]
        m += [(f'earlier_hit{j}',sub(sub(one,xi),z) if j<n-1 else sub(z,sub(one,xi)))]
    return q,m

def geometry_audit():
    h,k=old.H,old.KAP
    t=old.sub(h,old.mul(5,k)); th=old.sub(k,old.mul(8,t))
    a=old.sub(t,old.mul(3,th)); b=old.sub(th,a); g=old.sub(a,b)
    x=old.sub(old.mul(5,g),b)
    checks={'xi>0':x,'gamma>19xi':old.sub(g,old.mul(19,x)),
        'gamma<20xi':old.sub(old.mul(20,x),g),
        'beta>gamma':old.sub(b,g),'gamma>15xi':old.sub(g,old.mul(15,x))}
    assert all(old.prime_sign(v[:3])>0 for v in checks.values())
    levels={}
    for level,lib,req,lift,upper in ((3,THIRD,third_req,third_lift,beta),
            (4,FOURTH,fourth_req,fourth_lift,beta),(5,FIFTH,fifth_req,fifth_lift,one)):
        base=RANGE+(zeta,sub(upper,zeta)); cells={}
        for key in lib:
            _,rr=req(key,seed); _,m=lift(key,seed)
            cells[key]=audit(m,vertices(base+tuple(a for _,a in rr)))
        levels[str(level)]=cells
    cells={}
    for n in (19,20):
        for s in range(15):
            q,m=sixth_lift(s,n,seed)
            cond=RANGE+(zeta,sub(scale(14,xi),zeta),seed,sub(xi,seed),q,sub(xi,q))
            cond += (sub(q,zeta),) if s==0 else (
                sub(zeta,add(q,scale(s-1,xi))),sub(add(q,scale(s,xi)),zeta))
            item=audit(m,vertices(cond))
            if s==14:
                item['zeta_equals_14xi_face']=audit(m,vertices(cond+(sub(zeta,scale(14,xi)),)))
            cells[f'{s}/{n}']=item
    # Piecewise translations tile the sixth section, in y coordinates.
    cut=sub(xi,omega)
    assert add(cut,omega)==xi and sub(add(cut,omega),xi)==zero
    assert sub(one,scale(20,xi))==sub(omega,xi)
    # Immediate new word: 0<d=zeta-14xi<omega and cut<y<cut+d.
    d=sub(zeta,scale(14,xi)); q,m=sixth_lift(15,20,seed)
    cond=RANGE+(d,sub(omega,d),sub(seed,cut),sub(add(cut,d),seed))
    assert q==sub(seed,cut)
    guard=audit(m,vertices(cond))
    return {'normalization':'gamma=1; 94/19<beta/gamma<99/20; coordinates (r,zeta,seed)',
        'prime_power_checks':{k:'PASS' for k in checks},
        'contract_policy':'Third maps lift to original steps once. Every higher composition checks each established lower source contract and the exact affine target identity.',
        'third_formula_scope':'0<zeta<beta', 'fourth_formula_scope':'0<zeta<beta',
        'fifth_formula_scope':'0<zeta<gamma', 'level_3_4_5_cells':levels,
        'sixth_section':'gamma-xi<z<gamma; physical h-beta+gamma-xi<t<h-beta+gamma',
        'sixth_times':'19 for y<xi-omega; 20 for y>xi-omega',
        'sixth_map':'y -> y+omega mod xi', 'sixth_tiling':'(omega,xi) and (0,omega)',
        'new_exclusion_scope':'0<zeta<=14xi', 'thirty_sixth_cells':cells,
        'above_scope_domain':'zeta=14xi+d; 0<d<omega; xi-omega<y<xi-omega+d',
        'above_scope_guard':guard,'sampled_topology':False}

def main():
    H=F(81,80); K=F(16,15); kap=K/H**5; tau_arg=H/kap**5
    theta_arg=kap/tau_arg**8; alpha_arg=tau_arg/theta_arg**3
    beta_arg=theta_arg/alpha_arg; gamma_arg=alpha_arg/beta_arg
    xi_arg=gamma_arg**5/beta_arg
    end3=F(16,3)*H**3; previous=end3/beta_arg; endpoint=previous*xi_arg**14
    assert previous<endpoint<end3
    # beta=169k-878h, gamma=1543h-297k, xi=8593h-1654k.
    assert endpoint==F(3**508056,2**578028*5**97858)
    out={'pass':'SZ-KERNEL-EDGE-GERM-75','standing':'UNRATIFIED',
        'entry_commit':'20d06346bf81479c97c4e06aa24bab0238fae4c2',
        'inherited_formula_scope':'2h<e<=3h','new_exclusion_scope':'3h-beta<e<=3h-beta+14xi',
        'experimental_endpoint':'log(3^508056/(2^578028*5^97858))',
        'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
        'third_word_dictionary':THIRD,'fourth_word_dictionary':FOURTH,'fifth_word_dictionary':FIFTH,
        'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
        'full_parent_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
        'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
