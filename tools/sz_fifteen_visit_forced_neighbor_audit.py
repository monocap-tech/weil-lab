#!/usr/bin/env python3
"""GERM-76: fifteen-visit control by a seventh exterior return section.

Scope: 3h-beta+14xi < e <= 3h-beta+14xi+eta7,
eta7=xi-omega. Retains all GERM-75 typed source domains. The first newly
legal B15,20 elliptic return is grouped with its forced neighbors. Exact
source-domain contracts and outward rational cone bounds are checked.
Run with assertions enabled. No parent full symbolic suite or large
Determinant inventory is rerun.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib, json

assert __debug__
ROOT=Path(__file__).resolve().parents[1]
PIN_PATH='tools/sz_fourth_section_self_overlap_audit.py'
PIN_SHA='805831ec2a937babcd3bb37a4528af22fc17cdade5dcee032befb592a79149fd'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest()==PIN_SHA
import sz_fourth_section_self_overlap_audit as parent
old=parent.old
old.SCALE=10**60
product=parent.product

def scale(n,x): return tuple(n*t for t in x)

ATOMS={'A19':(14,19),'A20':(14,20),'E20':(15,20)}
SEVENTH={
 '3out':['A20','A20','A19'],
 '3in':['A20','E20','A19'],
 '5out':['A20','A20','A19','A20','A19'],
 '5one':['A20','E20','A19','A20','A19'],
 '5two':['A20','E20','A19','E20','A19'],
}

def rational_audit():
    original,pivots=parent.parent.parent.parent.parent.recalculate_returns()
    legacy=parent.parent.parent.parent
    first={k:product(w,original) for k,w in legacy.FIRST.items()}
    second={k:product(w,first) for k,w in legacy.SECOND.items()}
    third={k:product(w,second) for k,w in parent.THIRD.items()}
    fourth={k:product(w,third) for k,w in parent.FOURTH.items()}
    fifth={k:product(w,fourth) for k,w in parent.FIFTH.items()}
    atoms={name:product(parent.sixth_word(s,n),fifth) for name,(s,n) in ATOMS.items()}
    chart=[[1,1],[F(-5,2),-3]]
    cert={}
    for name,w in SEVENTH.items():
        b=product(w,atoms)
        item=parent.parent.parent.cone_test(b,chart,1,F(12))
        item['sixth_return_word']=w
        cert[name]=item
    guard=['E20','E20','A19','E20','A19']
    b=product(guard,atoms)
    tr=b[0][0]+b[1][1]; d=parent.det(b); disc=tr*tr-4*d
    assert F(-13,10)<tr.lo<tr.hi<F(-12,10) and d.lo>0 and disc.hi<0
    return {
      'physical_maps':'FRESH OUTWARD RATIONAL PAIRED-SOURCE SOLVES VIA PINNED GERM-75 STACK',
      'grid':'10^60','layer_pivots':pivots,
      'atom_dictionary':ATOMS,'seventh_word_dictionary':SEVENTH,
      'chart':[['1','1'],['-5/2','-3']],
      'common_forward_backward_factor':'12','five_complete_returns':cert,
      'above_scope_word':guard,'above_scope_trace':old.display_matrix([[tr]]),
      'above_scope_determinant':old.display_matrix([[d]]),
      'above_scope_discriminant':old.display_matrix([[disc]]),
      'above_scope_status':'PROJECTIVELY ELLIPTIC'}

af,add,sub,val,vertices=parent.af,parent.add,parent.sub,parent.val,parent.vertices
zero,one=af(),af(1)
beta,zeta,seed=parent.beta,parent.zeta,parent.seed
xi,omega=parent.xi,parent.omega
eta7=sub(xi,omega)                  # xi-omega
chi7=sub(scale(2,omega),xi)         # 2omega-xi
psi7=sub(eta7,chi7)                 # 2xi-3omega
base75=scale(14,xi)
d=sub(zeta,base75)
RANGE=(sub(beta,af(F(777,157))),sub(af(F(292,59)),beta))

def audit(margins,vv):
    assert vv
    weak=[]
    for name,a in margins:
        vals=[val(a,v) for v in vv]
        assert min(vals)>=0,(name,a,min(vals))
        if max(vals)==0:
            assert name.endswith('global_scope'),(name,a)
            weak.append(name)
    return {'vertices':len(vv),'checked_margins':len(margins),'weak_global':weak}

def atom_lift(name,y):
    s,n=ATOMS[name]
    return parent.sixth_lift(s,n,y)

def seventh_positions(n,z):
    y0=add(scale(2,eta7),z)
    if n==3:
        return [y0,add(eta7,z),z,add(omega,z)]
    assert n==5
    return [y0,add(eta7,z),z,add(omega,z),add(chi7,z),
            add(add(eta7,scale(2,chi7)),z)]

def geometry_audit():
    H,K=old.H,old.KAP
    TAU=old.sub(H,old.mul(5,K)); TH=old.sub(K,old.mul(8,TAU))
    A=old.sub(TAU,old.mul(3,TH)); B=old.sub(TH,A); G=old.sub(A,B)
    X=old.sub(old.mul(5,G),B); O=old.sub(G,old.mul(19,X))
    E7=old.sub(X,O); C7=old.sub(old.mul(2,O),X); P7=old.sub(E7,C7)
    checks={
      'eta7_positive':E7,'chi7_positive':C7,'psi7_positive':P7,
      'chi7_minus_psi7_positive':old.sub(C7,P7),
      'eta7_minus_chi7_equals_psi7':P7,
      'omega_minus_eta7_equals_chi7':C7,
      'section_scope_below_parent':old.sub(old.sub(G,X),add(scale(14,X),E7)),
      'beta_over_gamma_gt_777_157':old.sub(B,old.mul(F(777,157),G)),
      'beta_over_gamma_lt_292_59':old.sub(old.mul(F(292,59),G),B),
    }
    assert all(old.prime_sign(v[:3])>0 for k,v in checks.items()
               if 'equals' not in k)
    assert old.sub(E7,C7)==P7 and old.sub(O,E7)==C7

    common=RANGE+(d,sub(eta7,d),seed,sub(chi7,seed))
    cells={}
    specs={
      '3out':(3,SEVENTH['3out'],(sub(seed,psi7),sub(seed,d))),
      '3in': (3,SEVENTH['3in'], (sub(seed,psi7),sub(d,seed))),
      '5out':(5,SEVENTH['5out'],(sub(psi7,seed),sub(seed,d))),
      '5one':(5,SEVENTH['5one'],(sub(psi7,seed),sub(d,seed),sub(add(seed,chi7),d))),
      '5two':(5,SEVENTH['5two'],(sub(psi7,seed),sub(d,add(seed,chi7)))),
    }
    for name,(n,word,extra) in specs.items():
        pp=seventh_positions(n,seed)
        assert len(word)==n
        margins=[('section_source_low',sub(pp[0],scale(2,eta7))),
                 ('section_source_high',sub(xi,pp[0]))]
        for j,key in enumerate(word):
            target,lower=atom_lift(key,pp[j]); assert target==pp[j+1],(name,j,target,pp[j+1])
            margins += [(f'{j}:{nm}',a) for nm,a in lower]
            if j<n-1:
                margins.append((f'section_no_early_{j}',sub(scale(2,eta7),target)))
            else:
                margins += [('section_return_low',sub(target,scale(2,eta7))),
                            ('section_return_high',sub(xi,target))]
        vv=vertices(common+extra)
        item=audit(margins,vv)
        if name in ('3in','5two'):
            face=common+extra+(sub(d,eta7),)
            item['d_equals_eta7_face']=audit(margins,vertices(face))
        cells[name]=item

    assert sub(add(psi7,chi7),eta7)==zero
    assert sub(add(psi7,eta7),xi) == sub(psi7,add(eta7,chi7))  # affine sanity
    eps=sub(d,eta7)
    pp=seventh_positions(5,seed)
    guard_word=['E20','E20','A19','E20','A19']
    margins=[]
    for j,key in enumerate(guard_word):
        target,lower=atom_lift(key,pp[j]); assert target==pp[j+1]
        margins += [(f'guard{j}:{nm}',a) for nm,a in lower]
    guard_cond=RANGE+(eps,sub(psi7,eps),sub(sub(chi7,psi7),eps),seed,sub(eps,seed))
    guard=audit(margins,vertices(guard_cond))
    return {
      'normalization':'gamma=1 inherited; d=zeta-14xi',
      'fixed_checks':{k:'PASS' for k in checks},
      'residual_relations':'eta7=xi-omega=chi7+psi7; omega=eta7+chi7; xi=2eta7+chi7',
      'seventh_section':'2eta7<y<xi; coordinate 0<z<chi7',
      'seventh_return_times':'3 for z>psi7; 5 for z<psi7',
      'seventh_map':'z -> z-psi7 mod chi7',
      'new_exclusion_scope':'0<d<=eta7','five_cells':cells,
      'above_scope_domain':'d=eta7+eps; 0<z<eps<min(psi7,chi7-psi7)',
      'above_scope_word':guard_word,'above_scope_guard':guard,
      'sampled_topology':False}

def main():
    H=F(81,80); K=F(16,15)
    kap=K/H**5; tau=H/kap**5; theta=kap/tau**8
    alpha=tau/theta**3; beta_r=theta/alpha; gamma=alpha/beta_r
    xi_r=gamma**5/beta_r; omega_r=gamma/xi_r**19; eta_r=xi_r/omega_r
    end75=F(16,3)*H**3/beta_r*xi_r**14
    endpoint=end75*eta_r
    assert endpoint==F(3**1222107,2**1390428*5**235392)
    end3=F(16,3)*H**3
    assert end75<endpoint<end3
    out={'pass':'SZ-KERNEL-EDGE-GERM-76','standing':'UNRATIFIED',
      'entry_commit':'39da808600e0b7edee589317bf0baf396c103bba',
      'inherited_formula_scope':'2h<e<=3h',
      'new_exclusion_scope':'3h-beta+14xi<e<=3h-beta+14xi+eta7',
      'experimental_endpoint':'log(3^1222107/(2^1390428*5^235392))',
      'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
      'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
      'full_parent_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
      'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
