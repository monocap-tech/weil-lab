#!/usr/bin/env python3
"""GERM-82: post-sigma8 ninth maps through t=psi7, without tenth induction.

Seven complete ninth words are derived from the GERM-81 eighth contracts.
One signed rational chart certifies factor 7/2 directly on the ninth circle.
All source inequalities are exact affine tests; all coefficient signs use
fresh outward rational solves. Run with assertions enabled, without -O.
The GERM-72 correction and all inherited scope limits remain in force.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of this certificate; run without -O.'
ROOT=Path(__file__).resolve().parents[1]
PIN_PATH='tools/sz_post_chi7_sixth_atom_audit.py'
PIN_SHA='f68e1f1bb2924462740bf54d992f50e76126a1de5d27717f5c2b5e504d979f17'
assert hashlib.sha256((ROOT/PIN_PATH).read_bytes()).hexdigest()==PIN_SHA
import sz_post_chi7_sixth_atom_audit as parent
g77,g75,old=parent.g77,parent.g75,parent.old
product,det=parent.product,parent.det
# The inherited arithmetic stack recomputes at grid 10^120 with 400 log terms.
NINTH={f'{s}/{n}':['A1']+['B0']*(n-s-1)+['B1']*s
       for n in (3,4) for s in range(n)}
CHART=[[1,-1],[F(-12,5),F(21,10)]]
FACTOR=F(7,2)
GUARD=['V1','U0','U1']  # GERM-81-local seventh maps, NOT earlier namesakes.
assert len(NINTH)==7
assert NINTH['0/3']==parent.NINTH['Q']
assert NINTH['0/4']==parent.NINTH['S']
assert NINTH['1/4']==parent.GUARD

def arithmetic():
    add,sub,mul=old.add,old.sub,old.mul
    h=(-4,4,-1);k=(4,-1,-1)
    kap=sub(k,mul(5,h));tau=sub(h,mul(5,kap));theta=sub(kap,mul(8,tau))
    alpha=sub(tau,mul(3,theta));beta=sub(theta,alpha);gamma=sub(alpha,beta)
    xi=sub(mul(5,gamma),beta);omega=sub(gamma,mul(19,xi))
    eta=sub(xi,omega);chi=sub(mul(2,omega),xi);psi=sub(eta,chi)
    sigma=sub(mul(3,psi),chi);rho=sub(psi,mul(3,sigma));c=sub(sigma,rho)
    nu=sub(psi,sigma)
    assert nu==sub(chi,mul(2,psi))
    L80=(193384,-169969,32737);L81=add(L80,sigma);L82=add(L80,psi)
    assert L81==(-8579064,7540488,-1452381)
    assert L82==(-2202828,1936158,-372926)
    assert L82==add((4,-1,0),sub(mul(461817,h),mul(88891,k)))
    assert sub(L82,L81)==nu
    top=add((4,-1,0),mul(3,h))
    checks={'sigma_positive':sigma,'3sigma_lt_psi':rho,
            'psi_lt_4sigma':c,'psi_lt_chi':sub(chi,psi),
            'chi_lt_eta':sub(eta,chi),'increment_nu8_positive':nu,
            'endpoint_below_three_layers':sub(top,L82)}
    logs=[old.log_box(n) for n in (2,3,5)]
    def enc(v):return sum((n*l for n,l in zip(v,logs)),old.box(0))
    enclosed={key:enc(v) for key,v in checks.items()}
    assert all(v.lo>0 for v in enclosed.values())
    assert add(mul(3,c),mul(4,rho))==psi
    assert add(mul(2,sigma),mul(3,sub(psi,sigma)))==chi
    return {'rational_log_order_checks':{k:g77.show_box(v,34) for k,v in enclosed.items()},
        'endpoint_prime_log_vector':L82,'endpoint_h_k_vector':[461817,-88891],
        'increment_prime_log_vector':nu,'increment_name':'nu8=psi7-sigma8',
        'endpoint_decimal':g77.show_box(enc(L82),30),
        'increment_decimal':g77.show_box(enc(nu),34),
        'remaining_three_layer_width':g77.show_box(enc(sub(top,L82)),34),
        'ninth_tower_identity':'3c10+4rho9=psi7'}

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
    atoms={k:product(g75.sixth_word(s,n),fifth) for k,(s,n) in parent.ATOMS.items()}
    c6={}
    for k,(s,n) in parent.ATOMS.items():
        ow=g75.to_original(g75.sixth_word(s,n))
        assert legacy.determinant_exponent(ow)==0
        assert len(ow)==1654*n-297;c6[k]=len(ow)
    seven={k:product(w,atoms) for k,w in parent.SEVENTH.items()}
    eight={k:product(w,seven) for k,w in parent.EIGHTH.items()}
    c7={k:sum(c6[x] for x in w) for k,w in parent.SEVENTH.items()}
    c8={k:sum(c7[x] for x in w) for k,w in parent.EIGHTH.items()}
    for lib in (atoms,seven,eight):
        for B in lib.values():
            dd=det(B);assert dd.lo>0 and dd.lo<=1<=dd.hi
    cert={}
    for key,w in NINTH.items():
        s,n=map(int,key.split('/'));B=product(w,eight)
        sign=1 if s==n-1 else -1
        item=g77.cone_test(B,CHART,sign,FACTOR)
        count=sum(c8[x] for x in w);assert count==257302+(n-1)*353997
        w7=parent.expand(w,parent.EIGHTH);direct=product(w7,seven)
        for i in range(2):
            for j in range(2):
                # Regression only. Exact identity is literal substitution.
                assert max(B[i][j].lo,direct[i][j].lo)<=min(B[i][j].hi,direct[i][j].hi)
        tr=B[0][0]+B[1][1];disc=tr*tr-4*det(B)
        assert disc.lo>0  # All seven actual ninth matrices are hyperbolic.
        item.update({'eighth_word':w,'seventh_word':w7,'original_step_count':count,
                     'determinant_rho_exponent':0,'trace':old.display_matrix([[tr]])})
        cert[key]=item
    B=product(GUARD,seven);tr=B[0][0]+B[1][1];disc=tr*tr-4*det(B)
    assert det(B).lo>0 and det(B).lo<=1<=det(B).hi
    assert F(-246,100)<tr.lo<tr.hi<F(-245,100) and disc.lo>0
    return {'physical_recalculation':'FRESH PAIRED-SOURCE OUTWARD RATIONAL SOLVES',
        'precision':{'grid':'10^120','log_series_terms':400},'layer_pivots':pivots,
        'GERM71_box_regression':'CONTAINED; not a rounded numerical input',
        'chart':[['1','-1'],['-12/5','21/10']],
        'common_forward_backward_factor':'7/2','seven_ninth_returns':cert,
        'tenth_induction_used':False,'all_seven_ninth_discriminants':'POSITIVE',
        'next_eighth_seventh_word':GUARD,'next_trace':old.display_matrix([[tr]]),
        'next_determinant':old.display_matrix([[det(B)]]),
        'next_discriminant':old.display_matrix([[disc]]),
        'next_status':'NEW EIGHTH SOURCE WORD; HYPERBOLIC; NO EXCLUSION CLAIM ABOVE t=psi7'}

# Exact affine coordinates remain those of GERM-75, gamma=1.
af,add,sub,val,vertices=parent.af,parent.add,parent.sub,parent.val,parent.vertices
scale,audit=parent.scale,parent.audit
seed,t,psi,sigma,chi=parent.seed,parent.t,parent.psi,parent.sigma,parent.chi
rho,c,RANGE=parent.rho,parent.c,parent.RANGE

def ninth_req(key,y):
    s,n=map(int,key.split('/'));q=add(y,sub(psi,scale(n,sigma)))
    m=[('y>0',y),('y<sigma',sub(sigma,y)),('q>0',q),('q<sigma',sub(sigma,q)),
       ('lower_global_scope',sub(t,sigma)),('upper_global_scope',sub(psi,t)),
       ('ninth_cut',sub(c,y) if n==3 else sub(y,c))]
    if s==0:m.append(('no_internal_target',sub(add(q,sigma),t)))
    else:m += [('last_internal_source',sub(t,add(q,scale(s,sigma)))),
               ('first_exterior_source',sub(add(q,scale(s+1,sigma)),t))]
    return q,m

def ninth_lift(key,y):
    q,m=ninth_req(key,y);w=NINTH[key];n=len(w)
    pp=[y]+[add(y,sub(psi,scale(j,sigma))) for j in range(1,n+1)]
    assert pp[-1]==q
    for j,k in enumerate(w):
        out,lower=parent.eighth_req(k,pp[j]);assert out==pp[j+1]
        m += [(f'{j}:{name}',a) for name,a in lower]
        m.append((f'no_early_ninth_hit{j}',sub(out,sigma) if j<n-1 else sub(sigma,out)))
    return q,m

def geometry_audit():
    lower_levels={}
    for label,lib,req,lift,ends in (
        ('sixth',parent.ATOMS,parent.atom_req,parent.atom_lift,()),
        ('seventh',parent.SEVENTH,parent.seventh_req,parent.seventh_lift,()),
        ('eighth',parent.EIGHTH,parent.eighth_req,parent.eighth_lift,('A1','B1'))):
        cells={}
        for key in lib:
            _,rr=req(key,seed);_,m=lift(key,seed)
            cond=RANGE+tuple(a for _,a in rr);item=audit(m,vertices(cond))
            if key in ends:item['t_equals_psi_endpoint']=audit(m,vertices(cond+(sub(t,psi),)))
            cells[key]=item
        lower_levels[label]=cells
    cells={}
    for key,w in NINTH.items():
        s,n=map(int,key.split('/'));_,rr=ninth_req(key,seed);_,m=ninth_lift(key,seed)
        cond=RANGE+tuple(a for _,a in rr);item=audit(m,vertices(cond))
        if s==0:item['t_equals_sigma_entry_face']=audit(m,vertices(cond+(sub(sigma,t),)))
        if s in (1,2):
            face=scale(s+1,sigma)
            item[f't_equals_{s+1}sigma_face']=audit(m,vertices(cond+(sub(t,face),sub(face,t))))
        if s==n-1:item['t_equals_psi_endpoint']=audit(m,vertices(cond+(sub(t,psi),)))
        cells[key]=item
    # Direct image tiling of the complete ninth first-return map.
    assert add(c,rho)==sigma
    assert add(scale(3,c),scale(4,rho))==psi
    # Next eighth branch: t=psi+eps, sigma<z<sigma+eps, eps<nu8.
    eps=sub(t,psi);nu=sub(psi,sigma)
    pp=[seed]+[add(seed,sub(chi,scale(j,psi))) for j in range(1,4)]
    m=[('guard_z>sigma',sub(seed,sigma)),('guard_z<psi',sub(psi,seed))]
    for j,k in enumerate(GUARD):
        q,lower=parent.seventh_req(k,pp[j]);assert q==pp[j+1]
        m += [(f'guard{j}:{name}',a) for name,a in lower]
        m.append((f'guard_no_early_hit{j}',sub(q,psi) if j<2 else sub(psi,q)))
    cond=RANGE+(eps,sub(nu,eps),sub(seed,sigma),sub(add(sigma,eps),seed))
    guard=audit(m,vertices(cond))
    return {'normalization':'GERM-75 affine coordinates; exact rational beta/gamma box',
        'parameter':'t=e-e80; new exclusion sigma8<t<=psi7',
        'rechecked_lower_contracts':lower_levels,'seven_ninth_cells':cells,
        'ninth_map':'y -> y+rho9 mod sigma8',
        'ninth_images':'(rho9,sigma8) and (0,rho9)',
        'ninth_tower_identity':'3c10+4rho9=psi7',
        'physical_field':'W(t0+y), t0=h-beta+gamma-xi+2eta7; 0<y<sigma8',
        'upper_endpoint_words':['A1,B1,B1','A1,B1,B1,B1'],
        'next_eighth_seventh_word':GUARD,
        'next_domain':'t=psi7+eps; 0<eps<nu8; sigma8<z<sigma8+eps',
        'next_guard':guard,'sampled_topology':False}

def main():
    out={'pass':'SZ-KERNEL-EDGE-GERM-82','standing':'UNRATIFIED',
        'entry_commit':'d7da5057bc1f8d998037d51005fb67f6c6df6719',
        'new_exclusion_scope':'sigma8<t<=psi7, t=e-e80; L81<L<=L80+psi7',
        'experimental_endpoint':'log(3^1936158/(2^2202828*5^372926))',
        'increment':'nu8=psi7-sigma8','inherited_three_layer_formula_scope':'2h<e<=3h',
        'direct_dependency_sha256':{PIN_PATH:PIN_SHA},
        'matrix_namespace':'A_i,B_i,U_i,V_i are GERM-81-local; N_(s,n) is GERM-82-local',
        'ninth_word_dictionary':NINTH,'arithmetic':arithmetic(),
        'rational_audit':rational_audit(),'exact_geometry':geometry_audit(),
        'full_lower_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
        'tenth_return_induction_used':False,
        'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
