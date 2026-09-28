#!/usr/bin/env python3
"""GERM-71: second-section self-overlap, six retyped maps, seven exterior words.

New exclusion: 3h-tau < e <= 3h-theta. Retained formula scope: e<=3h.
Recalculates physical maps via the pinned paired-source rational solver.
All certificate signs, cone factors and source domains are exact/outward
rational checks. Floating exploratory chart selection is not a certificate.
Requires byte-pinned GERM-69/68/65 helpers and the GERM-67 regression fixture.
Run without -O. Does not rerun the parent symbolic or large determinant suites.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert __debug__, 'Assertions are part of the verifier; do not use -O.'
ROOT = Path(__file__).resolve().parents[1]
PINS = {
 'tools/sz_overlapping_section_audit.py':'0283a3412d0ef9d029e690693b472ad656602ca817e3d730d7c48234361602e4',
 'tools/sz_multivisit_section_audit.py':'16517b40a62f46ec32e439a42fe70e6a52cf5d665138f0c93be0ed25a6c31bb7',
 'tools/sz_mixed_return_cone_audit.py':'f43eaf0e86e823a2f7ebeb6580b8ea12fcf4587ad405f708c3b66d6939b2a6c0',
 'notes/_recurrence67_audit.json':'db2dcd27d30ca3199c444e449d7a2b93b674a7fe2b2d4cc764b38a9a863e0b09',
}
for path, expected in PINS.items():
    assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == expected, path
import sz_overlapping_section_audit as parent
old = parent.old
mat, mm, product = old.mat, old.mm, parent.product
inverse, det = parent.inverse, parent.mdet
af, add, sub, value, vertices = parent.af, parent.add, parent.sub, parent.val, parent.verts

def scale(c, a): return tuple(c*x for x in a)

# Words are chronological throughout; multiplication acts rightmost first.
FIRST = parent.first_words()
FIRST['J'] = ['11-']+['11+']*5  # GERM-70's missing inside-to-inside wrap.
SECOND = {
 '00+':['Q']+['E']*6+['P'],
 '10+':['E']*7+['P'],
 '11+':['E']*7+['J'],
 '00-':['Q']+['E']*7+['P'],
 '01-':['Q']+['E']*7+['J'],
 '11-':['E']*8+['J'],
}
PAIRS = [(s,n) for n in (3,4) for s in range(n)]

def third_word(s, n):
    if s == 0: return ['00-']+['00+']*(n-1)
    return ['01-']+['11+']*(s-1)+['10+']+['00+']*(n-s-1)

def expand_second(word):
    return [letter for key in word for letter in SECOND[key]]

def expand_original(word):
    return [letter for key in expand_second(word) for letter in FIRST[key]]

def determinant_exponent(original_word):
    # The inherited original six-map determinant library is rho^(i-j).
    return sum(int(key[0])-int(key[1]) for key in original_word)

def rational_audit():
    returns, pivots = parent.recalculate_returns()
    first = {key:product(word,returns) for key,word in FIRST.items()}
    second = {key:product(word,first) for key,word in SECOND.items()}
    for key, word in SECOND.items():
        n=8+int(key[-1]=='-')
        assert len(word)==n
        expanded=[z for x in word for z in FIRST[x]]
        assert len(expanded)==5*n+1
        assert determinant_exponent(expanded)==int(key[0])-int(key[1])
        assert det(second[key]).lo>0
    chart=mat([[1,1],[0,3]])
    ci=inverse(chart)
    answer={}
    for s,n in PAIRS:
        word=third_word(s,n)
        b=product(word,second)
        sign=(-1)**(n+1)
        positive=[[sign*x for x in row] for row in mm(mm(ci,b),chart)]
        assert all(x.lo>0 for row in positive for x in row),(s,n,old.display_matrix(positive))
        delta=det(positive)
        assert delta.lo>0 and delta.lo<=1<=delta.hi
        forward=min(positive[0][0].lo+positive[1][0].lo,
                    positive[0][1].lo+positive[1][1].lo)
        backward=min(positive[1][1].lo+positive[1][0].lo,
                     positive[0][1].lo+positive[0][0].lo)/delta.hi
        assert forward>F(5,2) and backward>F(5,2),(s,n,forward,backward)
        expanded=expand_original(word)
        assert len(expand_second(word))==8*n+1
        assert len(expanded)==41*n+5
        assert determinant_exponent(expanded)==0
        direct=product(expanded,returns)
        for i in range(2):
            for j in range(2):
                # Regression only. Equality is from literal word substitution.
                assert max(b[i][j].lo,direct[i][j].lo)<=min(b[i][j].hi,direct[i][j].hi)
        answer[f'{s}/{n}']={
          'second_section_word':word,'first_section_word':expand_second(word),
          'original_word':expanded,'original_step_count':len(expanded),
          'overall_sign':sign,'positive_conjugate':old.display_matrix(positive),
          'determinant_enclosure':old.display_matrix([[delta]]),
          'forward_lower':old.outward_decimal(forward,10),
          'backward_lower':old.outward_decimal(backward,10)}
    guard_word=['11-','11+','11+','10+']
    b=product(guard_word,second)
    cg=mm(mm(ci,b),chart);tr=b[0][0]+b[1][1];delta=det(b)
    disc=tr*tr-4*delta
    assert cg[0][0].hi<0<cg[0][1].lo and cg[1][0].hi<0 and cg[1][1].hi<0
    assert F(-22,10)<tr.lo and tr.hi<F(-21,10)
    assert disc.hi<0  # Nonunit determinant: trace alone does not classify it.
    return {
      'physical_source_maps':'FRESH OUTWARD RATIONAL PAIRED-SOURCE SOLVES',
      'parent_six_map_regression':'CONTAINED IN PINNED GERM-67 BOXES',
      'layer_pivots':pivots,'first_inside_wrap_word':FIRST['J'],
      'second_section_words':SECOND,
      'second_section_maps':{k:old.display_matrix(b) for k,b in second.items()},
      'chart':[['1','1'],['0','3']],'common_forward_backward_factor':'5/2',
      'seven_full_returns':answer,
      'above_scope_word':guard_word,'above_scope_conjugate':old.display_matrix(cg),
      'above_scope_trace':old.display_matrix([[tr]]),
      'above_scope_determinant':old.display_matrix([[delta]]),
      'above_scope_discriminant':old.display_matrix([[disc]]),
      'above_scope_determinant_rho_exponent':determinant_exponent(expand_original(guard_word)),
      'above_scope_same_chart':'FAILS; NEGATIVE PROJECTIVE DISCRIMINANT IS ALSO CERTIFIED',
    }

# Exact geometry: theta=1, variables (r=tau/theta, zeta, v).
# Physical r is strictly between 3 and 4; all inequalities hold on that box.
one=af(1);zero=af();tau=af(r=1);kap=af(1,r=8)
h=af(5,r=41);lam=af(4,r=33);zeta=af(eta=1);v=af(z=1)
nu=add(sub(kap,tau),zeta);eta=add(lam,nu)
alpha=sub(tau,af(3))

def audit_margins(margins, vv):
    weak=[]
    for name, margin in margins:
        values=[value(margin,w) for w in vv]
        assert min(values)>=0,(name,margin,min(values))
        if max(values)==0:
            assert name.endswith('section_separation'),(name,margin)
            weak.append(name)
    return {'checked_margins':len(margins),'vertices':len(vv),'weak_global_separation':weak}

def lift_second(key,y):
    """Every first-section position and every original R point of one S2 step."""
    si,tj=int(key[0]),int(key[1]);wrap=key[-1]=='-';n=8+int(wrap)
    target=sub(add(y,one),tau) if wrap else add(y,one)
    points=[add(sub(kap,scale(j+1,tau)),y) for j in range(n)]
    points.append(add(sub(kap,tau),target))
    bits=[si]+[1]*(n-1)+[tj]
    margins=[('y>0',y),('y<tau',sub(tau,y)),('target>0',target),('target<tau',sub(tau,target)),
       ('source_overlap',sub(zeta,y) if si else sub(y,zeta)),
       ('target_overlap',sub(zeta,target) if tj else sub(target,zeta)),
       ('second_rotation_cut',sub(y,sub(tau,one)) if wrap else sub(sub(tau,one),y))]
    expected=SECOND[key]
    for j,z in enumerate(points):
        margins += [(f'z{j}>0',z),(f'z{j}<kap',sub(kap,z)),
                    (f'z{j}overlap',sub(nu,z) if bits[j] else sub(z,nu)),
                    (f'z{j}F',sub(z,sub(kap,tau)) if j in(0,n) else sub(sub(kap,tau),z))]
    for j in range(n):
        z,next_z=points[j:j+2];fw=j==n-1;nn=6 if fw else 5
        assert next_z==(add(z,sub(kap,tau)) if fw else sub(z,tau))
        margins.append((f'Scut{j}',sub(tau,z) if fw else sub(z,tau)))
        pp=[add(lam,z)]+[add(z,scale(k,kap)) for k in range(nn)]
        assert pp[-1]==add(lam,next_z)
        bb=[bits[j]]+[1]*(nn-1)+[bits[j+1]]
        actual=[f'{bb[k]}{bb[k+1]}'+('-' if k==0 else '+') for k in range(nn)]
        assert actual==FIRST[expected[j]],(key,j,actual)
        for k,p in enumerate(pp):
            margins += [(f'R{j},{k}>0',p),(f'R{j},{k}<h',sub(h,p)),
                         (f'R{j},{k}I',sub(eta,p) if bb[k] else sub(p,eta)),
                         (f'R{j},{k}E',sub(p,lam) if k in(0,nn) else sub(lam,p))]
    return target,margins

def geometry_audit():
    hv,kv=old.H,old.KAP
    tv=old.sub(hv,old.mul(5,kv));thv=old.sub(kv,old.mul(8,tv))
    fixed={'theta_positive':thv,'tau_gt_3theta':old.sub(tv,old.mul(3,thv)),
           'tau_lt_4theta':old.sub(old.mul(4,thv),tv),
           'new_endpoint_gt_old':old.sub(tv,thv)}
    assert all(old.prime_sign(x[:3])>0 for x in fixed.values())
    base=(sub(tau,af(3)),sub(af(4),tau),zeta,sub(sub(tau,one),zeta),v,sub(one,v))
    # First validate the six S2 species over the full self-overlap formula
    # domain 0<zeta<tau, independently of the narrower exterior certificate.
    six={}
    sb=(sub(tau,af(3)),sub(af(4),tau),zeta,sub(tau,zeta),v,sub(tau,v))
    for key in SECOND:
        si,tj=int(key[0]),int(key[1]);wrapped=key[-1]=='-'
        target=sub(add(v,one),tau) if wrapped else add(v,one)
        conditions=sb+(sub(v,sub(tau,one)) if wrapped else sub(sub(tau,one),v),
                       sub(zeta,v) if si else sub(v,zeta),
                       sub(zeta,target) if tj else sub(target,zeta))
        yy,margins=lift_second(key,v)
        assert yy==target
        six[key]=audit_margins(margins,vertices(conditions))
    seven={}
    for s,n in PAIRS:
        word=third_word(s,n)
        pp=[add(sub(tau,one),v)]+[add(v,af(j)) for j in range(n)]
        cond=base+(sub(v,alpha) if n==3 else sub(alpha,v),)
        cond += (sub(v,zeta),) if s==0 else (sub(zeta,add(v,af(s-1))),sub(add(v,af(s)),zeta))
        margins=[('third_section_separation',sub(sub(tau,one),zeta))]
        for j,y in enumerate(pp):
            bit=1<=j<=s
            margins += [(f'third{j}>0',y),(f'third{j}<tau',sub(tau,y)),
                         (f'third{j}overlap',sub(zeta,y) if bit else sub(y,zeta)),
                         (f'third{j}section',sub(y,sub(tau,one)) if j in(0,n) else sub(sub(tau,one),y))]
        for j,key in enumerate(word):
            assert key==f'{int(1<=j<=s)}{int(1<=j+1<=s)}'+('-' if j==0 else '+')
            yy,lower=lift_second(key,pp[j]);assert yy==pp[j+1]
            margins += [(f'{j}:{name}',a) for name,a in lower]
        vv=vertices(cond);out=audit_margins(margins,vv)
        if s==n-1:
            face=cond+(sub(zeta,sub(tau,one)),)
            out['new_endpoint_face']=audit_margins(margins,vertices(face))
        seven[f'{s}/{n}']=out
    # Direct translation-image tiling of the new third section.
    assert sub(add(alpha,af(4)),tau)==one
    assert sub(add(alpha,af(3)),tau)==zero
    assert sub(af(4),tau)==sub(one,alpha)
    # Above the endpoint: zeta=tau-1+epsilon, 0<v<epsilon<min(alpha,1-alpha).
    eps=sub(zeta,sub(tau,one))
    guard=(sub(tau,af(3)),sub(af(4),tau),eps,sub(alpha,eps),sub(sub(one,alpha),eps),v,sub(eps,v))
    gg=['11-','11+','11+','10+']
    pp=[add(sub(tau,one),v)]+[add(v,af(j)) for j in range(4)]
    margins=[]
    for j,key in enumerate(gg):
        yy,lower=lift_second(key,pp[j]);assert yy==pp[j+1]
        margins += [(f'guard{j}:{name}',a) for name,a in lower]
        margins.append((f'guard_next{j}_section',sub(sub(tau,one),yy) if j<3 else sub(yy,sub(tau,one))))
    guard_result=audit_margins(margins,vertices(guard))
    return {'normalization':'theta=1; 3<tau/theta<4; variables (tau/theta,zeta,v)',
      'exact_prime_power_checks':{k:'PASS' for k in fixed},
      'second_section_formula_scope':'0<zeta<tau; six types retain endpoint bits',
      'six_second_map_cells':six,'third_section':'tau-theta<y<tau, physically h-theta<t<h',
      'third_return_times':'3 if v>alpha; 4 if v<alpha; alpha=tau-3theta',
      'third_induced_map':'v -> v-alpha mod theta',
      'third_image_tiling':'(0,theta-alpha) and (theta-alpha,theta)',
      'new_exclusion_scope':'0<zeta<=tau-theta','seven_cells':seven,
      'above_scope_guard':guard_result,
      'above_scope_domain':'zeta=tau-theta+epsilon; 0<v<epsilon<min(alpha,theta-alpha)',
      'above_scope_word':gg,'sampled_topology_used_in_certificate':False}

def main():
    # theta = kappa-8tau = 41kappa-8h = 41k-213h.
    endpoint=F(16,3)*F(81,80)**216/F(16,15)**41
    assert endpoint==F(3**904,2**1024*5**175)
    previous=F(2**116*5**18,3**98)
    final=F(16,3)*F(81,80)**3
    assert previous<endpoint<final
    kap_arg=F(16,15)/F(81,80)**5
    tau_arg=F(81,80)/kap_arg**5
    theta_arg=kap_arg/tau_arg**8
    assert endpoint==final/theta_arg
    out={'pass':'SZ-KERNEL-EDGE-GERM-71','standing':'UNRATIFIED',
         'entry_commit':'dd94ef57114d520169965fd4b4d558143fed90d4',
         'inherited_formula_scope':'2h<e<=3h',
         'new_exclusion_scope':'3h-tau<e<=3h-theta',
         'experimental_endpoint':'log(3^904/(2^1024*5^175))',
         'dependency_sha256':PINS,'rational_audit':rational_audit(),
         'exact_geometry':geometry_audit(),
         'full_parent_symbolic_suites_rerun':False,'old_large_determinants_rerun':False,
         'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'}
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
