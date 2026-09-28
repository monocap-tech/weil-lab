#!/usr/bin/env python3
"""GERM-74: internal-wrap closure by a typed sixth-return certificate.

Scope: 3h-alpha < e <= 3h-beta. Retains the GERM-73 source-word repair.
Uses fresh outward rational physical-map solves and exact affine domain
contracts. Each third map is lifted to the original source steps once;
fourth, fifth and sixth compositions check the already-proved input
contracts at EVERY intermediate point, without repeatedly flattening them.
Run without -O. No full parent symbolic or large-determinant suite is run.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of this verifier; do not use -O.'
ROOT = Path(__file__).resolve().parents[1]
PARENT_FILE = 'tools/sz_fourth_section_elliptic_visit_audit.py'
PARENT_SHA256 = '1b36e699415e0ebf2a93946161745e5f8297132e7ab1c6f2930a73a19bbb483f'
assert hashlib.sha256((ROOT/PARENT_FILE).read_bytes()).hexdigest() == PARENT_SHA256
import sz_fourth_section_elliptic_visit_audit as parent
old = parent.old
# Log series use 180 terms; atanh remainder is enclosed, never discarded.
# More grid precision controls cancellation in the long block determinants.
old.SCALE = 10**60
mat, mm, product = parent.mat, parent.mm, parent.product
inverse, det = parent.inverse, parent.det
af, add, sub, val, vertices = parent.af, parent.add, parent.sub, parent.val, parent.vertices

def scale(n, x): return tuple(n*t for t in x)

THIRD = {
    'Q': ['01-', '11+', '11+'],
    'P': ['11-', '11+', '11+', '10+'],
    'D': ['01-', '11+', '11+', '10+'],
    'I': ['11-', '11+', '11+', '11+'],
}
FOURTH = {'E': ['Q','P'], 'J0': ['Q','P','D'], 'J1': ['Q','I','P']}
FIFTH = {f'{i}/{n}': [f'J{i}']+['E']*(n-1) for i in (0,1) for n in (4,5)}
SIXTH = {}
for n in (19,20):
    SIXTH[f'out/{n}'] = ['0/4']+['0/5']*(n-1)
    for s in range(n):
        SIXTH[f'{s}/{n}'] = ['1/4']+['0/5']*(n-s-1)+['1/5']*s
assert len(SIXTH) == 41

def expand(word, dictionary): return [letter for k in word for letter in dictionary[k]]
def to_original(sixth_word):
    fourth = expand(sixth_word,FIFTH)
    third = expand(fourth,FOURTH)
    second = expand(third,THIRD)
    return parent.parent.expand_original(second)

def rational_audit():
    returns,pivots = parent.parent.parent.recalculate_returns()
    first = {k:product(w,returns) for k,w in parent.parent.FIRST.items()}
    second = {k:product(w,first) for k,w in parent.parent.SECOND.items()}
    fixture = json.loads((ROOT/'notes/_recurrence71_audit.json').read_text())
    fixture = fixture['audit']['rational_audit']['second_section_maps']
    for k,b in second.items():
        for i in range(2):
            for j in range(2):
                lo,hi=map(F,fixture[k][i][j])
                assert lo <= b[i][j].lo <= b[i][j].hi <= hi
    third={k:product(w,second) for k,w in THIRD.items()}
    fourth={k:product(w,third) for k,w in FOURTH.items()}
    fifth={k:product(w,fourth) for k,w in FIFTH.items()}
    for dictionary, library in ((THIRD,third),(FOURTH,fourth),(FIFTH,fifth)):
        for b in library.values(): assert det(b).lo>0
    for k,w in THIRD.items():
        ex=parent.parent.determinant_exponent(parent.parent.expand_original(w))
        assert ex=={'Q':-1,'P':1,'D':0,'I':0}[k]
    for k,w in FIFTH.items():
        w2=expand(expand(w,FOURTH),THIRD)
        assert parent.parent.determinant_exponent(parent.parent.expand_original(w2))==0
    # New nonwrap-in-the-fifth-section word really is elliptic.
    f=fifth['1/4']; trace=f[0][0]+f[1][1]; discr=trace*trace-4*det(f)
    assert discr.hi<0 and F(78,100)<trace.lo<trace.hi<F(79,100)
    chart=[[1,1],[0,3]]
    answer={}
    for key,w in SIXTH.items():
        left,nstr=key.split('/'); n=int(nstr)
        if left=='out': sign=(-1)**(n+1)
        else:
            s=int(left)
            sign=1 if s==n-1 else (-1)**(n+s)
        b=product(w,fifth)
        result=parent.cone_test(b,chart,sign,F(8000))
        original=to_original(w)
        assert len(original)==1654*n-297
        assert parent.parent.determinant_exponent(original)==0
        result.update({
            'fifth_word':w,
            'original_step_count':len(original),
            'original_word_sha256':hashlib.sha256(json.dumps(original,separators=(',',':')).encode()).hexdigest()})
        answer[key]=result
    return {
        'physical_source_maps':'FRESH OUTWARD RATIONAL PAIRED-SOURCE SOLVES',
        'rational_grid_denominator':'10^60',
        'second_map_regression':'CONTAINED IN PINNED GERM-71 BOXES',
        'layer_pivots':pivots,
        'fifth_maps':{k:old.display_matrix(b) for k,b in fifth.items()},
        'elliptic_fifth_map':'1/4',
        'elliptic_trace':old.display_matrix([[trace]]),
        'elliptic_discriminant':old.display_matrix([[discr]]),
        'chart':[['1','1'],['0','3']],
        'common_forward_backward_factor':'8000',
        'forty_one_sixth_words':answer,
        'determinants':'All complete fourth/fifth/sixth words are exactly one by expanded-word exponents; numerical inverse bounds use computed positive determinant enclosures.'}

# gamma=1; independent variables (r=beta/gamma, delta, seed).
# epsilon=beta+delta, so the newly active interval is 0<delta<=1.
zero,one=af(),af(1)
r,delta,seed=af(r=1),af(eta=1),af(z=1)
beta=r; alpha=add(r,one); theta=add(scale(2,r),one)
tau=add(scale(7,r),af(4)); epsilon=add(beta,delta)
zeta=add(sub(tau,theta),epsilon)
xi=sub(af(5),r)
omega=sub(one,scale(19,xi))
RANGE=(sub(r,af(F(94,19))),sub(af(F(99,20)),r))
GLOBAL=RANGE+(delta,sub(one,delta))

def audit_margins(margins, vv):
    assert vv, 'Empty domain cell.'
    weak=[]
    for name,a in margins:
        values=[val(a,v) for v in vv]
        assert min(values)>=0,(name,a,min(values))
        if max(values)==0:
            assert name.endswith('global_scope'),(name,a)
            weak.append(name)
    return {'vertices':len(vv),'checked_margins':len(margins),'weak_global':weak}

@lru_cache(None)
def second_template(key): return parent.second_template(key)

def second_lift(key,y):
    def subst(a):
        return add(add(scale(a[0],theta),scale(a[1],tau)),
                   add(scale(a[2],zeta),scale(a[3],y)))
    target,margins=second_template(key)
    return subst(target),[(name,subst(a)) for name,a in margins]

def third_requirements(key,v):
    wrapped=key!='Q'
    target=add(v,beta) if wrapped else sub(v,alpha)
    si=key in ('P','I'); ti=key in ('Q','I')
    return target,[
        ('third_v>0',v),('third_v<theta',sub(theta,v)),
        ('third_target>0',target),('third_target<theta',sub(theta,target)),
        ('third_source_overlap',sub(epsilon,v) if si else sub(v,epsilon)),
        ('third_target_overlap',sub(epsilon,target) if ti else sub(target,epsilon)),
        ('third_cut',sub(alpha,v) if wrapped else sub(v,alpha)),
        ('third_global_scope',sub(one,delta))]

def third_lift(key,v):
    target,margins=third_requirements(key,v)
    word=THIRD[key]; n=len(word)
    pp=[add(sub(tau,theta),v)]+[add(v,scale(j,theta)) for j in range(n)]
    assert pp[-1]==add(sub(tau,theta),target)
    si=key in ('P','I'); ti=key in ('Q','I')
    bits=[int(si)]+[1]*(n-1)+[int(ti)]
    assert word==[f'{bits[j]}{bits[j+1]}'+('-' if j==0 else '+') for j in range(n)]
    for j,k in enumerate(word):
        y,lower=second_lift(k,pp[j]); assert y==pp[j+1]
        margins += [(f'{j}:{name}',a) for name,a in lower]
        margins += [(f'no_earlier_third{j}',sub(sub(tau,theta),y) if j<n-1 else sub(y,sub(tau,theta)))]
    return target,margins

def fourth_requirements(key,w):
    target=sub(w,one) if key=='E' else add(w,sub(beta,one))
    m=[('fourth_w>0',w),('fourth_w<beta',sub(beta,w)),
       ('fourth_target>0',target),('fourth_target<beta',sub(beta,target)),
       ('fourth_cut',sub(w,one) if key=='E' else sub(one,w)),
       ('fourth_global_scope',sub(one,delta))]
    if key!='E': m += [('internal_wrap_bit',sub(delta,w) if key=='J1' else sub(w,delta))]
    return target,m

def fourth_lift(key,w):
    target,margins=fourth_requirements(key,w)
    pp=[add(alpha,w),w,add(w,beta)]
    if key!='E': pp.append(add(w,scale(2,beta)))
    assert pp[-1]==add(alpha,target)
    for j,k in enumerate(FOURTH[key]):
        v,lower=third_requirements(k,pp[j]); assert v==pp[j+1]
        margins += [(f'{j}:{name}',a) for name,a in lower]
        margins += [(f'no_earlier_fourth{j}',sub(alpha,v) if j<len(pp)-2 else sub(v,alpha))]
    return target,margins

def fifth_requirements(key,z):
    istr,nstr=key.split('/'); i,n=int(istr),int(nstr)
    target=add(z,sub(beta,af(n)))
    return target,[('fifth_z>0',z),('fifth_z<gamma',sub(one,z)),
        ('fifth_target>0',target),('fifth_target<gamma',sub(one,target)),
        ('fifth_cut',sub(xi,z) if n==4 else sub(z,xi)),
        ('fifth_source_bit',sub(delta,z) if i else sub(z,delta)),
        ('fifth_global_scope',sub(one,delta))]

def fifth_lift(key,z):
    n=int(key.split('/')[1]); target,margins=fifth_requirements(key,z)
    pp=[z]+[add(z,sub(beta,af(j))) for j in range(1,n+1)]
    assert pp[-1]==target
    for j,k in enumerate(FIFTH[key]):
        w,lower=fourth_requirements(k,pp[j]); assert w==pp[j+1]
        margins += [(f'{j}:{name}',a) for name,a in lower]
        margins += [(f'no_earlier_fifth{j}',sub(w,one) if j<n-1 else sub(one,w))]
    return target,margins

def sixth_lift(word,y):
    n=len(word)
    pp=[y]+[add(y,sub(one,scale(j,xi))) for j in range(1,n+1)]
    target=pp[-1]; margins=[('sixth_source>0',y),('sixth_source<xi',sub(xi,y)),
        ('sixth_target>0',target),('sixth_target<xi',sub(xi,target)),
        ('sixth_global_scope',sub(one,delta))]
    for j,k in enumerate(word):
        z,lower=fifth_requirements(k,pp[j]); assert z==pp[j+1]
        margins += [(f'{j}:{name}',a) for name,a in lower]
        margins += [(f'no_earlier_sixth{j}',sub(z,xi) if j<n-1 else sub(xi,z))]
    return target,margins

def geometry_audit():
    hv,kv=old.H,old.KAP
    tv=old.sub(hv,old.mul(5,kv)); thv=old.sub(kv,old.mul(8,tv))
    av=old.sub(tv,old.mul(3,thv)); bv=old.sub(thv,av); gv=old.sub(av,bv)
    xiv=old.sub(old.mul(5,gv),bv)
    fixed={'xi_positive':xiv,'gamma_gt_19xi':old.sub(gv,old.mul(19,xiv)),
           'gamma_lt_20xi':old.sub(old.mul(20,xiv),gv),'beta_gt_gamma':old.sub(bv,gv)}
    assert all(old.prime_sign(v[:3])>0 for v in fixed.values())
    lower={}
    for level,library,lift,req in ((3,THIRD,third_lift,third_requirements),
            (4,FOURTH,fourth_lift,fourth_requirements),
            (5,FIFTH,fifth_lift,fifth_requirements)):
        cells={}
        for key in library:
            _,rr=req(key,seed); _,margins=lift(key,seed)
            cond=GLOBAL+tuple(a for _,a in rr)
            cells[key]=audit_margins(margins,vertices(cond))
            # Domain faces are certified only for species present generically.
            present=(level==3 and key!='D') or (level==4 and key!='J0') or (level==5 and key.startswith('1/'))
            if present:
                cells[key]['delta_equals_gamma_face']=audit_margins(margins,vertices(cond+(sub(delta,one),)))
        lower[str(level)]=cells
    # Low source-bit case: 0<delta<=xi, all later sources are exterior.
    low={}
    for n in (19,20):
        q=add(seed,sub(one,scale(n,xi)))
        for i in (0,1):
            key=f'out/{n}' if i==0 else f'0/{n}'
            cond=GLOBAL+(sub(xi,delta),seed,sub(xi,seed),q,sub(xi,q),
                          sub(delta,seed) if i else sub(seed,delta))
            _,margins=sixth_lift(SIXTH[key],seed)
            low[f'{i}/{n}']=audit_margins(margins,vertices(cond))
            if i:
                low[f'{i}/{n}']['delta_equals_xi_face']=audit_margins(margins,vertices(cond+(sub(delta,xi),)))
    # High source-bit case: xi<=delta<=gamma. All smaller sources are inside.
    high={}
    for n in (19,20):
        q=add(seed,sub(one,scale(n,xi)))
        for s in range(n):
            cond=GLOBAL+(sub(delta,xi),seed,sub(xi,seed),q,sub(xi,q))
            if s==0: cond += (sub(add(q,xi),delta),)
            else: cond += (sub(delta,add(q,scale(s,xi))),sub(add(q,scale(s+1,xi)),delta))
            _,margins=sixth_lift(SIXTH[f'{s}/{n}'],seed)
            result=audit_margins(margins,vertices(cond))
            if s==n-1:
                result['delta_equals_gamma_face']=audit_margins(margins,vertices(cond+(sub(delta,one),)))
            high[f'{s}/{n}']=result
    # Return map y -> y+omega mod xi, with cut xi-omega.
    cut=sub(xi,omega)
    assert add(cut,omega)==xi
    assert sub(add(cut,omega),xi)==zero
    assert sub(one,scale(20,xi))==sub(omega,xi)
    # Above delta=gamma the H source may be inside on 0<w<delta-gamma.
    # Directly lift the new third nonwrap from the still-valid second system.
    small=sub(delta,one)
    cond=RANGE+(small,sub(xi,small),seed,sub(small,seed))
    v=add(alpha,seed)
    pp=[add(sub(tau,theta),v)]+[add(v,scale(j,theta)) for j in range(3)]
    guard_word=['11-','11+','11+']; margins=[]
    for j,key in enumerate(guard_word):
        yy,part=second_lift(key,pp[j]); assert yy==pp[j+1]
        margins += [(f'guard{j}:{name}',a) for name,a in part]
    assert pp[-1]==add(sub(tau,theta),seed)
    guard=audit_margins(margins,vertices(cond))
    return {'normalization':'gamma=1; 94/19<beta/gamma<99/20; variables (r,delta,seed)',
        'prime_power_checks':{k:'PASS' for k in fixed},
        'contract_policy':'Third cells lift to original steps; every higher composition checks the proven input contract at every intermediate point. No endpoint-only typing.',
        'level_3_4_5_domain_certificates':lower,
        'sixth_low_cells':low,'sixth_high_cells':high,
        'sixth_section':'0<y<xi, physically h-beta<t<h-beta+xi',
        'sixth_return_times':'19 if y<xi-omega; 20 if y>xi-omega; omega=gamma-19xi',
        'sixth_map':'y -> y+omega mod xi',
        'image_tiling':'(omega,xi) and (0,omega)',
        'above_scope_word':guard_word,
        'above_scope_domain':'delta=gamma+zeta; 0<w<zeta<xi; third source alpha+w',
        'above_scope_guard':guard,'sampled_topology':False}

def main():
    # beta=169k-878h, hence 3h-beta=881h-169k.
    final=F(16,3)*F(81,80)**3
    kap_arg=F(16,15)/F(81,80)**5
    tau_arg=F(81,80)/kap_arg**5
    theta_arg=kap_arg/tau_arg**8
    alpha_arg=tau_arg/theta_arg**3
    beta_arg=theta_arg/alpha_arg
    gamma_arg=alpha_arg/beta_arg
    previous=final/alpha_arg; endpoint=final/beta_arg
    assert endpoint==F(3**3692,2**4196*5**712)
    assert previous<endpoint<final and endpoint/previous==gamma_arg
    out={'pass':'SZ-KERNEL-EDGE-GERM-74','standing':'UNRATIFIED',
        'entry_commit':'5a3c0f58618e9ad5f24577f34e40d2fe43d87a7f',
        'inherited_formula_scope':'2h<e<=3h','new_exclusion_scope':'3h-alpha<e<=3h-beta',
        'experimental_endpoint':'log(3^3692/(2^4196*5^712))',
        'direct_dependency_sha256':{PARENT_FILE:PARENT_SHA256},
        'inherited_dependency_sha256':parent.PINS,
        'third_word_dictionary':THIRD,'fourth_word_dictionary':FOURTH,'fifth_word_dictionary':FIFTH,
        'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
        'full_parent_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
        'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
