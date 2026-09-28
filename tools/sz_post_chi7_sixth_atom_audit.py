#!/usr/bin/env python3
"""GERM-81: post-chi7 sixth-atom transfer, through t=sigma8.

The changed B15,19 atom is retained, not replaced by the old B14,19.
Fresh rational physical solves and full intermediate-domain contracts
certify the new downstream maps. One chart controls 23 distinct tenth
words on two parameter cells. All signs are exact/outward rational.
Run without -O. No full lower symbolic suite or large determinants run.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of the certificate; run without -O.'
ROOT=Path(__file__).resolve().parents[1]
PIN_PATH='tools/sz_ninth_return_double_internal_audit.py'
PIN_SHA='febb0139baf1962838a937d5034670dcf0a1719f363c60605a88c7dd49ae9f3c'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest()==PIN_SHA
import sz_ninth_return_double_internal_audit as parent
# Parent sets 10^120 rational grid and 400-term log bounds with tail bound.
g77,g75,old=parent.g77,parent.g75,parent.old
product,det=parent.product,parent.det
ATOMS={'A19':(14,19),'E19':(15,19),'E20':(15,20)}
SEVENTH={'U0':['E20','E20','A19'], 'U1':['E20','E20','E19'],
         'V0':['E20','E20','A19','E20','A19'],
         'V1':['E20','E20','E19','E20','A19']}
# Names are local to GERM-81: these are NOT unchanged GERM-80 matrices.
EIGHTH={f'{name}{i}':[f'V{i}']+['U0']*(n-1)
        for name,n in (('A',2),('B',3)) for i in (0,1)}
NINTH={'P':['A0','B0','B0'],'Q':['A1','B0','B0'],
       'R':['A0','B0','B0','B0'],'S':['A1','B0','B0','B0']}
LOW={(i,n):['Q' if i else 'P']+['R']*(n-1) for n in (10,11) for i in (0,1)}
HIGH={(s,n):['Q']+['R']*(n-s-1)+['S']*s for n in (10,11) for s in range(n)}
WORDS={f'out/{n}':LOW[0,n] for n in (10,11)}
WORDS.update({f'{s}/{n}':w for (s,n),w in HIGH.items()})
assert len(WORDS)==23
assert {tuple(w) for w in WORDS.values()}=={tuple(w) for w in list(LOW.values())+list(HIGH.values())}
CHART=[[1,1],[F(-8,5),8]]
GUARD=['A1','B0','B0','B1']

def expand(word,dictionary):return [x for key in word for x in dictionary[key]]

def arithmetic():
    sub,add,mul=old.sub,old.add,old.mul
    h,k=(-4,4,-1),(4,-1,-1)
    kap=sub(k,mul(5,h));tau=sub(h,mul(5,kap));th=sub(kap,mul(8,tau))
    a=sub(tau,mul(3,th));bb=sub(th,a);gg=sub(a,bb)
    xx=sub(mul(5,gg),bb);oo=sub(gg,mul(19,xx))
    ee=sub(xx,oo);cc=sub(mul(2,oo),xx);pp=sub(ee,cc)
    ss=sub(mul(3,pp),cc);rr=sub(pp,mul(3,ss));cut=sub(ss,rr)
    omt=sub(ss,mul(10,cut));top=add((4,-1,0),mul(3,h))
    L80=(193384,-169969,32737);L81=add(L80,ss)
    assert L81==(-8579064,7540488,-1452381)
    assert L81==add((4,-1,0),sub(mul(1798574,h),mul(346193,k)))
    checks={'sigma_positive':ss,'sigma_lt_psi':sub(pp,ss),
        'psi_lt_chi':sub(cc,pp),'chi_lt_eta':sub(ee,cc),
        'c10_positive':cut,'10c10_lt_sigma':omt,'sigma_lt_11c10':sub(cut,omt),
        'sixth_exterior_margin_at_t_eta':sub(sub(gg,xx),mul(15,xx)),
        'endpoint_below_three_layers':sub(top,L81),
        'beta_box_lower':sub(mul(157,bb),mul(777,gg)),
        'beta_box_upper':sub(mul(1069,gg),mul(216,bb))}
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(v):return sum((n*l for n,l in zip(v,logs)),old.box(0))
    boxes={key:enc(v) for key,v in checks.items()}
    assert all(b.lo>0 for b in boxes.values())
    assert add(mul(3,sub(cc,pp)),mul(5,pp))==xx
    assert add(mul(2,sub(mul(3,pp),cc)),mul(3,sub(cc,mul(2,pp))))==cc
    assert add(mul(3,sub(ss,rr)),mul(4,rr))==pp
    assert add(mul(10,sub(cut,omt)),mul(11,omt))==ss
    return {'rational_log_order_checks':{k:g77.show_box(v,34) for k,v in boxes.items()},
        'endpoint_prime_log_vector':L81,'endpoint_h_k_vector':[1798574,-346193],
        'increment_prime_log_vector':ss,'endpoint_decimal':g77.show_box(enc(L81),30),
        'increment_decimal':g77.show_box(enc(ss),34),
        'remaining_three_layer_width':g77.show_box(enc(sub(top,L81)),34),
        'tower_length_identities':'sixth->seventh->eighth->ninth->tenth all verified'}

def rational_audit():
    original,pivots=g75.parent.parent.parent.parent.recalculate_returns()
    legacy=g75.parent.parent.parent
    first={k:product(w,original) for k,w in legacy.FIRST.items()}
    second={k:product(w,first) for k,w in legacy.SECOND.items()}
    boxes=json.loads((ROOT/'notes/_recurrence71_audit.json').read_text())['audit']['rational_audit']['second_section_maps']
    for key,B in second.items():
        for i in range(2):
            for j in range(2):
                lo,hi=map(F,boxes[key][i][j]);assert lo<=B[i][j].lo<=B[i][j].hi<=hi
    third={k:product(w,second) for k,w in g75.THIRD.items()}
    fourth={k:product(w,third) for k,w in g75.FOURTH.items()}
    fifth={k:product(w,fourth) for k,w in g75.FIFTH.items()}
    atoms={k:product(g75.sixth_word(s,n),fifth) for k,(s,n) in ATOMS.items()}
    count6={}
    for key,(s,n) in ATOMS.items():
        ow=g75.to_original(g75.sixth_word(s,n))
        assert legacy.determinant_exponent(ow)==0
        assert len(ow)==1654*n-297;count6[key]=len(ow)
    seven={k:product(w,atoms) for k,w in SEVENTH.items()}
    eight={k:product(w,seven) for k,w in EIGHTH.items()}
    nine={k:product(w,eight) for k,w in NINTH.items()}
    c7={k:sum(count6[x] for x in w) for k,w in SEVENTH.items()}
    c8={k:sum(c7[x] for x in w) for k,w in EIGHTH.items()}
    c9={k:sum(c8[x] for x in w) for k,w in NINTH.items()}
    assert c9=={'P':965296,'Q':965296,'R':1319293,'S':1319293}
    for lib in (atoms,seven,eight,nine):
        for B in lib.values():
            dd=det(B);assert dd.lo>0 and dd.lo<=1<=dd.hi
    # Literal continuity of the old endpoint WORDS, not an endpoint theorem:
    # new U0/V0 coincide with the surviving GERM-80 U1/V1 at t=0.
    assert SEVENTH['U0']==g77.SEVENTH['U1']
    assert SEVENTH['V0']==g77.SEVENTH['V1']
    old8=parent.parent.EIGHTH
    old_nine_q=expand(expand(parent.NINTH['Q'],old8),g77.SEVENTH)
    old_nine_s=expand(expand(parent.NINTH['S'],old8),g77.SEVENTH)
    assert expand(expand(NINTH['P'],EIGHTH),SEVENTH)==old_nine_q
    assert expand(expand(NINTH['R'],EIGHTH),SEVENTH)==old_nine_s
    cert={}
    for key,w in WORDS.items():
        label,n=key.split('/');n=int(n)
        if label=='out':sign=-1
        else:
            s=int(label);sign=(-1)**s if s<n-2 else -(-1)**s
        B=product(w,nine)
        item=g77.cone_test(B,CHART,sign,F(75))
        assert sum(c9[x] for x in w)==965296+(n-1)*1319293
        w8=expand(w,NINTH);direct=product(w8,eight)
        for i in range(2):
            for j in range(2):
                # Regression only; equality follows from literal substitution.
                assert max(B[i][j].lo,direct[i][j].lo)<=min(B[i][j].hi,direct[i][j].hi)
        item.update({'ninth_word':w,'eighth_word':w8,'original_step_count':sum(c9[x] for x in w),
                     'determinant_rho_exponent':0})
        cert[key]=item
    changed=atoms['E19'];tr=changed[0][0]+changed[1][1]
    assert (tr*tr-4*det(changed)).hi<0
    B=product(GUARD,eight);trg=B[0][0]+B[1][1];disc=trg*trg-4*det(B)
    assert F(-119)<trg.lo<trg.hi<F(-118) and disc.lo>0
    inv=g75.inverse(g75.mat(CHART));conj=g75.mm(g75.mm(inv,B),g75.mat(CHART))
    assert all(x.lo>0 for x in conj[0]) and all(x.hi<0 for x in conj[1])
    return {'physical_recalculation':'FRESH PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
        'precision':{'grid':'10^120','log_series_terms':400},'layer_pivots':pivots,
        'GERM71_box_regression':'CONTAINED','changed_sixth_atom':'E19=B15,19 remains elliptic',
        'sixth_maps':{k:old.display_matrix(B) for k,B in atoms.items()},
        'seventh_maps':{k:old.display_matrix(B) for k,B in seven.items()},
        'ninth_maps':{k:old.display_matrix(B) for k,B in nine.items()},
        't0_word_regression':'new U0/V0=old U1/V1; new P/R=old Q/S, by literal substitution',
        'chart':[['1','1'],['-8/5','8']],'common_forward_backward_factor':'75',
        'distinct_word_count':23,'tenth_returns':cert,
        'next_ninth_eighth_word':GUARD,'next_trace':old.display_matrix([[trg]]),
        'next_determinant':old.display_matrix([[det(B)]]),'next_discriminant':old.display_matrix([[disc]]),
        'next_chart':old.display_matrix(conj),'next_status':'HYPERBOLIC; present chart has opposite row signs'}

# Exact affine coordinates from GERM-75: gamma=1, variables (beta/gamma,zeta,seed).
af,add,sub,val,vertices=parent.af,parent.add,parent.sub,parent.val,parent.vertices
scale=parent.scale;audit=g77.audit
zero=af();seed=g77.seed;xi=g77.xi;omega=g77.omega;eta=g77.eta
chi=g77.chi;psi=g77.psi;sigma=g77.sigma;nu=g77.nu
rho=sub(psi,scale(3,sigma));c=sub(sigma,rho);omt=sub(sigma,scale(10,c))
t=sub(g77.delta,chi);RANGE=parent.RANGE

def atom_req(key,y):
    wrap=key=='E20';target=sub(y,eta) if wrap else add(y,omega)
    m=[('y>0',y),('y<xi',sub(xi,y)),('target>0',target),('target<xi',sub(xi,target)),
       ('t>0',t),('sixth_global_scope',sub(eta,t)),
       ('sixth_cut',sub(y,eta) if wrap else sub(eta,y))]
    if not wrap:m.append(('new_sixth_bit',sub(t,y) if key=='E19' else sub(y,t)))
    return target,m

def atom_lift(key,y):
    target,m=atom_req(key,y);s,n=ATOMS[key]
    out,lower=g75.sixth_lift(s,n,y);assert out==target
    return out,m+[(f'fifth:{name}',a) for name,a in lower]

def seventh_req(key,z):
    wrap=key[0]=='V';bit=int(key[1]);target=add(z,sub(chi,psi)) if wrap else sub(z,psi)
    return target,[('z>0',z),('z<chi',sub(chi,z)),('target>0',target),('target<chi',sub(chi,target)),
        ('t>0',t),('seventh_global_scope',sub(chi,t)),
        ('seventh_cut',sub(psi,z) if wrap else sub(z,psi)),
        ('source_bit',sub(t,z) if bit else sub(z,t))]

def seventh_lift(key,z):
    target,m=seventh_req(key,z);word=SEVENTH[key]
    pp=g77.g76.seventh_positions(len(word),z)
    assert pp[-1]==add(scale(2,eta),target)
    for j,k in enumerate(word):
        q,lower=atom_req(k,pp[j]);assert q==pp[j+1]
        m += [(f'{j}:{name}',a) for name,a in lower]
        m.append((f'no_early_seventh_hit{j}',sub(scale(2,eta),q) if j<len(word)-1 else sub(q,scale(2,eta))))
    return target,m

def eighth_req(key,z):
    n=2 if key[0]=='A' else 3;bit=int(key[1]);target=add(z,sub(chi,scale(n,psi)))
    return target,[('z>0',z),('z<psi',sub(psi,z)),('target>0',target),('target<psi',sub(psi,target)),
        ('t>0',t),('eighth_global_scope',sub(psi,t)),
        ('eighth_cut',sub(sigma,z) if n==2 else sub(z,sigma)),
        ('source_bit',sub(t,z) if bit else sub(z,t))]

def eighth_lift(key,z):
    target,m=eighth_req(key,z);word=EIGHTH[key];n=len(word)
    pp=[z]+[add(z,sub(chi,scale(j,psi))) for j in range(1,n+1)]
    assert pp[-1]==target
    for j,k in enumerate(word):
        q,lower=seventh_req(k,pp[j]);assert q==pp[j+1]
        m += [(f'{j}:{name}',a) for name,a in lower]
        m.append((f'no_early_eighth_hit{j}',sub(q,psi) if j<n-1 else sub(psi,q)))
    return target,m

def ninth_req(key,y):
    n=3 if key in ('P','Q') else 4;bit=key in ('Q','S')
    target=add(y,sub(psi,scale(n,sigma)))
    return target,[('y>0',y),('y<sigma',sub(sigma,y)),('target>0',target),('target<sigma',sub(sigma,target)),
        ('t>0',t),('ninth_global_scope',sub(sigma,t)),
        ('ninth_cut',sub(c,y) if n==3 else sub(y,c)),
        ('source_bit',sub(t,y) if bit else sub(y,t))]

def ninth_lift(key,y):
    target,m=ninth_req(key,y);word=NINTH[key];n=len(word)
    pp=[y]+[add(y,sub(psi,scale(j,sigma))) for j in range(1,n+1)]
    assert pp[-1]==target
    for j,k in enumerate(word):
        q,lower=eighth_req(k,pp[j]);assert q==pp[j+1]
        m += [(f'{j}:{name}',a) for name,a in lower]
        m.append((f'no_early_ninth_hit{j}',sub(q,sigma) if j<n-1 else sub(sigma,q)))
    return target,m

def tenth_lift(word,y):
    n=len(word);pp=[y]+[add(y,sub(sigma,scale(j,c))) for j in range(1,n+1)]
    q=pp[-1];m=[('y>0',y),('y<c',sub(c,y)),('q>0',q),('q<c',sub(c,q))]
    for j,k in enumerate(word):
        out,lower=ninth_req(k,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',a) for name,a in lower]
        m.append((f'no_early_tenth_hit{j}',sub(out,c) if j<n-1 else sub(c,out)))
    return q,m

def geometry_audit():
    levels={}
    for label,lib,req,lift,upper,ends in (
        ('sixth',ATOMS,atom_req,atom_lift,eta,()),
        ('seventh',SEVENTH,seventh_req,seventh_lift,chi,()),
        ('eighth',EIGHTH,eighth_req,eighth_lift,psi,('A1','B1')),
        ('ninth',NINTH,ninth_req,ninth_lift,sigma,('Q','S'))):
        cells={}
        for key in lib:
            _,rr=req(key,seed);_,m=lift(key,seed)
            cond=RANGE+tuple(a for _,a in rr)
            item=audit(m,vertices(cond))
            if key in ends:item['upper_formula_endpoint']=audit(m,vertices(cond+(sub(t,upper),)))
            cells[key]=item
        levels[label]=cells
    low={};high={}
    for (i,n),w in LOW.items():
        q,m=tenth_lift(w,seed)
        cond=RANGE+(t,sub(c,t),seed,sub(c,seed),q,sub(c,q),sub(t,seed) if i else sub(seed,t))
        item=audit(m,vertices(cond))
        if i:item['t_equals_c_junction']=audit(m,vertices(cond+(sub(t,c),)))
        low[f'{i}/{n}']=item
    for (s,n),w in HIGH.items():
        q,m=tenth_lift(w,seed)
        cond=RANGE+(sub(t,c),sub(sigma,t),seed,sub(c,seed),q,sub(c,q))
        cond += (sub(add(q,c),t),) if s==0 else (sub(t,add(q,scale(s,c))),sub(add(q,scale(s+1,c)),t))
        item=audit(m,vertices(cond))
        if s==0:item['t_equals_c_junction']=audit(m,vertices(cond+(sub(c,t),)))
        if s==n-1:item['t_equals_sigma_endpoint']=audit(m,vertices(cond+(sub(t,sigma),)))
        high[f'{s}/{n}']=item
    # Exact image tiling and tower identity at the unchanged tenth section.
    assert add(sub(c,omt),omt)==c
    assert sub(sigma,scale(11,c))==sub(omt,c)
    assert add(scale(10,sub(c,omt)),scale(11,omt))==sigma
    # First change above t=sigma: four-step ninth return acquires B1 as
    # its last intermediate eighth map. Lower seventh/eighth scopes remain.
    eps=sub(t,sigma);pp=[seed]+[add(seed,sub(psi,scale(j,sigma))) for j in range(1,5)]
    m=[]
    for j,k in enumerate(GUARD):
        q,lower=eighth_req(k,pp[j]);assert q==pp[j+1]
        m += [(f'guard{j}:{name}',a) for name,a in lower]
        m.append((f'guard_no_early_hit{j}',sub(q,sigma) if j<3 else sub(sigma,q)))
    cond=RANGE+(eps,sub(rho,eps),sub(sigma,eps),sub(seed,c),sub(add(c,eps),seed))
    guard=audit(m,vertices(cond))
    return {'normalization':'gamma=1; inherited rational beta/gamma box and 10c10<sigma<11c10',
        'parameter':'t=delta-chi7=e-e80',
        'changed_sixth_partition':'E19 on (0,t); A19 on (t,eta7); E20 on (eta7,xi)',
        'formula_scopes':{'sixth':'0<t<eta7','seventh':'0<t<chi7','eighth':'0<t<=psi7','ninth':'0<t<=sigma8'},
        'rederived_level_contracts':levels,'physical_field':'W(t0+y); t0=h-beta+gamma-xi+2eta7',
        'tenth_section':'0<y<c10','tenth_map':'y -> y+omega10 mod c10',
        'tower_tiling':'(omega10,c10) and (0,omega10)',
        'low_cells':low,'high_cells':high,
        'new_exclusion_scope':'0<t<=sigma8','upper_endpoint_words':'S^9 Q and S^10 Q with the NEW ninth maps',
        'next_ninth_eighth_word':GUARD,'next_domain':'t=sigma8+eps; 0<eps<min(rho9,sigma8); c10<y<c10+eps',
        'next_guard':guard,'sampled_topology':False}

def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-81','standing':'UNRATIFIED',
        'entry_commit':'f20cf72ce881d68d9b343f911d6e7d5db08da968',
        'new_exclusion_scope':'0<t<=sigma8, t=e-e80; L80<L<=L80+sigma8',
        'experimental_endpoint':'log(3^7540488/(2^8579064*5^1452381))',
        'inherited_three_layer_formula_scope':'2h<e<=3h',
        'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
        'sixth_atom_dictionary':ATOMS,'seventh_word_dictionary':SEVENTH,
        'eighth_word_dictionary':EIGHTH,'ninth_word_dictionary':NINTH,
        'arithmetic':arithmetic(),'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
        'full_lower_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
        'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
