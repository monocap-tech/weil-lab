#!/usr/bin/env python3
"""GERM-67: three-layer reduction and isolated-visit induced-cone certificate.

Three-layer formulas: 2h < e <= 3h. Kernel exclusion: 2h < e <= 2h+kappa.
No claim of exclusion above the latter endpoint. Run without -O. Requires
sympy and the pinned GERM-65/66 helpers in this directory. No numerical
orbit discovery, floating-point sign tests, or large determinants are used.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import hashlib
import json
import sympy as sp
import sz_mixed_return_cone_audit as old
import sz_post_h_bridge_feedback_audit as prev

assert __debug__, 'Run with assertions enabled.'
PINS = {'sz_mixed_return_cone_audit.py':
        'f43eaf0e86e823a2f7ebeb6580b8ea12fcf4587ad405f708c3b66d6939b2a6c0',
        'sz_post_h_bridge_feedback_audit.py':
        '511b6cf1b6bf59e6133e47b6103dd2ea9960cfa41abe4491d6b7d56c17b6cd97'}
for name, want in PINS.items():
    assert hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()==want
A,D,C = sp.symbols('a d mu', nonzero=True)
G=1-A; DELTA=1-C*C; ALPHA=A/D; FSEED=D/(G*DELTA)
J=sp.Matrix([[0,1],[1,0]])
M=sp.Matrix([[(2*A-1)/(D*A),G/A],[-G/A,D/A]])


def clean(x): return x.applyfunc(sp.factor)
def zero(x): assert all(sp.factor(t)==0 for t in x)

def layer(m):
    """Exact paired-source elimination; m=2 replays the previous local API."""
    aa=sp.symbols('A:'+str(m)); bb=sp.symbols('B:'+str(m))
    cs=[C*x+y for x,y in zip(aa,bb)]
    ds=[x+C*y for x,y in zip(aa,bb)]
    W=[sp.Matrix([aa[i],FSEED*(ds[i]-(ALPHA*ds[i-1] if i else 0))]) for i in range(m)]
    V=[sp.Matrix([FSEED*(cs[i]-(ALPHA*cs[i+1] if i+1<m else 0)),bb[i]]) for i in range(m)]
    rows=[]
    for i in range(m-1):
        # R_i and R_(e-t-(i+1)h), the latter written in reflected V ports.
        rows += [aa[i]+A*W[i+1][1]-D*W[i][1]-A*G/D*FSEED*ds[i],
                 A*V[i][0]+bb[i+1]-D*V[i+1][0]-A*G/D*FSEED*cs[i+1]]
    X,Y=sp.symbols('X Y'); xy=sp.Matrix([X,Y])
    substitute={aa[0]:X,bb[0]:(Y/FSEED-X)/C}
    unknown=[u for i in range(1,m) for u in (aa[i],bb[i])]
    cc, rhs=sp.linear_eq_to_matrix([r.subs(substitute) for r in rows],unknown)
    solved=clean(cc.inv()*rhs)
    substitute.update(dict(zip(unknown,solved)))
    ww=[clean(v.subs(substitute)) for v in W]
    vv=[clean(v.subs(substitute)) for v in V]
    qlast=(FSEED*ds[-1]).subs(substitute)
    ym=-ww[-1][0]/A+D/A*ww[-1][1]+G/D*qlast
    xm=G/D*ym+A*G/D**2*qlast
    ww.append(clean(sp.Matrix([xm,ym])))
    LL=[v.jacobian([X,Y]) for v in ww]
    PP=[v.jacobian([X,Y]) for v in vv]
    NN=[clean(LL[i+1]*LL[i].inv()) for i in range(m)]
    KK=[clean(PP[i]*LL[i].inv()) for i in range(m)]
    zero(LL[0]-sp.eye(2))
    zero(sp.Matrix(rows).subs(substitute))
    # The original low first-cell row, before eliminating reflected seeds.
    for i in range(m):
        raw=(DELTA-A)*aa[i]+A*DELTA*(W[i+1][1] if i+1<m else ww[-1][1])-D*DELTA*W[i][1]-A*C*bb[i]
        zero(sp.Matrix([raw]).subs(substitute))
    # The terminal upper first-cell companion used to reconstruct W_m.
    zero(sp.Matrix([G*ww[-1][1]+A/DELTA*ds[-1].subs(substitute)-D*ww[-1][0]]))
    for i in range(m):
        zero(KK[m-1-i]*J*KK[i]-J)
    # Six-coordinate (or four-coordinate) shear bridge, independent of the solve.
    ss=sp.Matrix([v for w in W for v in w]);tt=sp.Matrix([v for v0 in V for v in v0])
    seedvars=[u for i in range(m) for u in (aa[i],bb[i])]
    win=ss.jacobian(seedvars);vout=tt.jacobian(seedvars)
    Sin=sp.eye(2*m);Sout=sp.eye(2*m)
    for i in range(m):
        for j in range(i): Sin[2*i+1,2*j+1]=ALPHA**(i-j)
        if i+1<m: Sout[2*i,2*(i+1)]=-ALPHA
    K=sp.Matrix([[-D/(G*C),1/C],[-1/C,G*DELTA/(D*C)]])
    block=Sout*sp.diag(*([K]*m))*Sin
    zero(block*win-vout)
    assert sp.factor(Sin.det())==1 and sp.factor(Sout.det())==1 and sp.factor(K.det())==1
    # Both external parities are represented without extra assumptions.
    rawref=sp.symbols('ref:'+str(m))
    for eps in (1,-1):
        sigma={bb[i]:eps*rawref[i] for i in range(m)}
        zero((block*ss-tt).subs(sigma))
    return {'L':LL,'N':NN,'K':KK,'pivot':sp.factor(cc.det()),
            'prefix_dets':[sp.factor(v.det()) for v in LL],
            'paired_unknown_count':len(unknown)}


def symbolic_audit():
    layers={m:layer(m) for m in (2,3)}
    chi=2*A+D*D-1
    xi=chi**2+G**2*C**2-A**2*D**2
    psi=3*chi**2+G**2*C**2-2*A**2*D**2
    zero(sp.Matrix([layers[3]['pivot']-A**2*D**2*xi/(G**4*DELTA**2)]))
    zero(sp.Matrix([layers[3]['prefix_dets'][-1]-G*psi/(D**2*xi)]))
    zero(sp.Matrix([layers[2]['prefix_dets'][-1]-2*G/D**2]))
    # Match GERM-66's local two-layer reduction, not merely matrix dimension.
    K=layers[2]['K'][0];nu=D+A*G/D
    oldK=sp.Matrix([[-D/(G*C),1/C],[-1/C,G*DELTA/(D*C)]])
    row=sp.Matrix([[-D-A/D,1]])*oldK
    cc=sp.Matrix([[0,A],[row[0],row[1]]])
    dd=sp.Matrix([[1,-nu],[A*oldK[0,0],A*oldK[0,1]+ALPHA*row[1]]])
    N0=clean(-cc.inv()*dd)
    zero(N0-layers[2]['L'][1])
    NN=sp.Matrix([[-G/(D*A),G*(1/D**2+1/A)],[-1/A,nu/A]])
    FF=NN*N0+sp.Matrix([A*G/D**3,A*G/D**2])*sp.Matrix([[0,1]])
    zero(FF-layers[2]['L'][2])
    zero(oldK-ALPHA*sp.diag(1,0)*oldK*(N0+ALPHA*sp.diag(0,1))-K)
    # Return determinant cancellation follows from these exact identities.
    for m in (2,3):
        B=layers[m]
        zero(sp.Matrix([B['K'][0].det()-B['prefix_dets'][m-1]]))
        zero(sp.Matrix([B['N'][-1].det()*B['K'][0].det()-B['prefix_dets'][-1]]))
    zero(M*M-sp.trace(M)*M+sp.eye(2))
    assert sp.factor(M.det())==1
    return layers, {'three_layer_shear_bridge_determinant':1,
          'paired_rows_and_terminal_source_rows':'PASS',
          'external_parities':[1,-1], 'two_layer_local_regression':'EXACT MATCH',
          'three_layer_unknown_count':4,
          'three_layer_pivot':'a^2*d^2*Xi/(g^4*Delta^2)',
          'Xi':'(2a+d^2-1)^2+g^2*mu^2-a^2*d^2',
          'Psi':'3*(2a+d^2-1)^2+g^2*mu^2-2*a^2*d^2',
          'det_F3':'g*Psi/(d^2*Xi)',
          'bridge_reflection_and_prefix_identities':'PASS',
          'return_determinants':{'00+':'1','10+':'Psi/(2*Xi)','11+':'1',
                                 '00-':'1','01-':'2*Xi/Psi','11-':'1'},
          'bulk_characteristic_identity':'PASS'}


def interval_audit(layers):
    l2,l3,l5=old.log_box(2),old.log_box(3),old.log_box(5)
    c=(l3/l2)/old.sqrt_box(3); b=(l3/l2)*old.sqrt_box(F(2,3))
    d=(l5/l2)/old.sqrt_box(5); a=(b*c)**2
    coeff={A:a,D:d,C:c}
    @lru_cache(None)
    def evaluate(x):
        if x in coeff:return coeff[x]
        if x.is_Rational:return old.box(F(int(x.p),int(x.q)))
        if x.is_Add:return sum((evaluate(t) for t in x.args),old.box(0))
        if x.is_Mul:
            ans=old.box(1)
            for t in x.args:ans=ans*evaluate(t)
            return ans
        if x.is_Pow and x.exp.is_Integer:return evaluate(x.base)**int(x.exp)
        raise ValueError(('unsupported exact expression',x))
    def em(B):return [[evaluate(v) for v in row] for row in B.tolist()]
    inv=lambda B:old.inv2(B,prev.mdet(B))
    mats={m:{key:[em(v) for v in layer0[key]] for key in ('L','N','K')}
          for m,layer0 in layers.items()}
    audit={}
    for m,layer0 in layers.items():
        pivot=evaluate(layer0['pivot']);assert pivot.lo>0 if m==3 else pivot.hi<0
        if m==3:assert pivot.lo>19000 and pivot.hi<20000
        for key in ('L','N','K'):
            for B in mats[m][key]:
                determinant=prev.mdet(B)
                assert determinant.lo>0 or determinant.hi<0
                assert prev.norm_inf(B)<300 and prev.norm_inf(inv(B))<300
        audit[str(m)]={'paired_pivot':old.display_matrix([[pivot]]),
                       'prefix_determinants':old.display_matrix([[evaluate(v) for v in layer0['prefix_dets']]]),
                       'prefix_matrices':[old.display_matrix(v) for v in mats[m]['L']],
                       'first_bridge':old.display_matrix(mats[m]['K'][0])}
    g=1-a;chi=2*a+d*d-1;xi=chi**2+g*g*c*c-a*a*d*d
    psi=3*chi**2+g*g*c*c-2*a*a*d*d
    assert xi.lo>0 and psi.lo>0
    rho=psi/(2*xi)
    determinants={'00+':old.box(1),'10+':rho,'11+':old.box(1),'00-':old.box(1),
                  '01-':1/rho,'11-':old.box(1)}
    MI=old.inv2(em(M),old.box(1));JJ=old.mat([[0,1],[1,0]])
    assert prev.norm_inf(em(M))<300 and prev.norm_inf(MI)<300
    returns={}
    for key in determinants:
        i,j=int(key[0]),int(key[1]);wrap=int(key[2]=='-');mi=2+i;mj=2+j
        B=old.mm(old.mm(old.mm(old.mm(inv(mats[mj]['L'][-1]),old.mpow(MI,4+wrap-mj)),JJ),mats[mi]['N'][-1]),JJ)
        returns[key]=old.mm(B,mats[mi]['K'][0])
        got=prev.mdet(returns[key]);want=determinants[key]
        assert not (got.hi<want.lo or want.hi<got.lo)
    # The individual all-generator positive-quadrant method fails exactly.
    obstruction={}
    for key in ('11+','11-'):
        B=returns[key];tr=B[0][0]+B[1][1]
        assert 1<tr.lo and tr.hi<F(8,5) and B[0][1].hi<0
        disc=tr**2-4;assert disc.hi<0
        obstruction[key]={'trace':old.display_matrix([[tr]]),
                          'discriminant':old.display_matrix([[disc]]),
                          'negative_upper_right_entry':True,'determinant':'1'}
    # First-return induction removes the single isolated bad overlap visit.
    excursion=old.mm(returns['10+'],returns['01-'])
    blocks={'ordinary_nonwrap':returns['00+'],'ordinary_wrap':returns['00-'],
            'isolated_overlap_excursion':excursion}
    positive={}
    w=F(1,5)
    for key,B in blocks.items():
        assert all(v.lo>0 for row in B for v in row)
        forward=min(B[0][0].lo+w*B[1][0].lo,B[0][1].lo/w+B[1][1].lo)
        backward=min(B[1][1].lo+w*B[1][0].lo,B[0][1].lo/w+B[0][0].lo)
        assert forward>F(7,5) and backward>F(7,5),(key,forward,backward)
        positive[key]={'matrix':old.display_matrix(B),'determinant':'1',
                      'weighted_forward_lower':old.outward_decimal(forward,8),
                      'weighted_backward_lower':old.outward_decimal(backward,8)}
    # A second consecutive overlap visit is not silently covered by this test.
    two_visit=old.mm(old.mm(returns['10+'],returns['11+']),returns['01-'])
    tr=two_visit[0][0]+two_visit[1][1]
    assert F(18,10)<tr.lo and tr.hi<F(19,10) and two_visit[0][1].hi<0
    return {'coefficients':old.display_matrix([[c,d,a,g,1-c*c]]),
            'layers':audit,'all_local_maps_and_inverses_inf_bound':300,
            'three_layer_returns':{key:old.display_matrix(B) for key,B in returns.items()},
            'individual_generator_obstruction':obstruction,
            'induced_blocks':positive,'weighted_norm':'|X|+|Y|/5',
            'common_forward_backward_factor':'7/5',
            'two_visit_scope_guard':{'trace':old.display_matrix([[tr]]),'determinant':'1',
                                    'negative_upper_right_entry':True},
            'old_large_determinants_rerun':False}

# Exact, uniform h-normalized geometry. Affine variables are r=kappa/h,
# eta=(e-2h)/h, t=source/h; no representative orbit is sampled.
af=prev.af;add=prev.add;sub=prev.sub;val=prev.val;vertices=prev.vertices
ZERO=prev.ZERO;ONE=prev.ONE;RR=prev.RR;ETA=prev.ETA;TT=prev.TT
WORDS={'00+':['N20','N21','M','M','H21'],
       '10+':['N20','N21','M','M','H32'],
       '11+':['N30','N31','N32','M','H32'],
       '00-':['N20','N21','M','M','M','H21'],
       '01-':['N30','N31','N32','M','M','H21'],
       '11-':['N30','N31','N32','M','M','H32']}
REGIONS={'N30':(ZERO,ETA),'N20':(ETA,ONE),'N31':(ONE,add(ONE,ETA)),
         'N21':(add(ONE,ETA),af(2)),'N32':(af(2),af(2,eta=1)),
         'M':(af(2,eta=1),af(4,r=1)),
         'H32':(af(4,r=1),af(4,r=1,eta=1)),
         'H21':(af(4,r=1,eta=1),af(5,r=1))}

def geometry_audit():
    fixed={'kappa_positive':old.KAP[:3],
           'h_minus_5kappa':old.sub(old.H,old.mul(5,old.KAP))[:3],
           '6kappa_minus_h':old.sub(old.mul(6,old.KAP),old.H)[:3],
           'p_minus_k_minus_3h':old.sub(old.sub(old.P,old.K),old.mul(3,old.H))[:3],
           'j_minus_k_minus_3h':old.sub(old.sub(old.J,old.K),old.mul(3,old.H))[:3],
           'k_minus_4h':old.sub(old.K,old.mul(4,old.H))[:3]}
    assert all(old.prime_sign(v)>0 for v in fixed.values())
    common=(af(F(-1,6),r=1),af(F(1,5),r=-1),ETA,sub(ONE,ETA),TT,sub(ONE,TT))
    result={}
    for key,word in WORDS.items():
        i,j=int(key[0]),int(key[1]);wrap=int(key[2]=='-')
        y=af(-wrap,r=1,t=1)
        side=af(-1 if wrap else 1,r=1 if wrap else -1,t=1 if wrap else -1)
        constraints=common+(side,sub(ETA,TT) if i else sub(TT,ETA),sub(ETA,y) if j else sub(y,ETA))
        vv=vertices(constraints);margins=[]
        for n,name in enumerate(word):
            pt=add(y,af(n));lo,hi=REGIONS[name]
            for margin in (sub(pt,lo),sub(hi,pt)):
                vals=[val(margin,v) for v in vv]
                assert min(vals)>=0 and max(vals)>0,(key,n,name,vals)
                margins.append(margin)
        assert add(y,af(len(word)))==af(5,r=1,t=1)
        # Source bridge is B_(2+i),0 by the same domain split.
        result[key]={'directed_word':word,'exact_polytope_vertices':len(vv),'gate_margins':'PASS'}
        if key.startswith('11'):
            ev=vertices(constraints+(sub(ETA,ONE),))
            for margin in margins:
                vals=[val(margin,v) for v in ev]
                assert min(vals)>=0 and max(vals)>0
            result[key]['eta_equals_h_face']='PASS'
    # Isolated overlap: 0<eta<=r<h/5; first return to D=(eta,1).
    # Domains: (eta,1-r), (1-r,1-r+eta), (1-r+eta,1).
    # Translations: +r, +2r-1, +(r-1). Images tile D.
    isolated=(af(F(-1,6),r=1),af(F(1,5),r=-1),ETA,sub(RR,ETA))
    vv=vertices(isolated+(TT,sub(ONE,TT)))
    strict_gaps=[sub(af(1,r=-1),ETA),sub(RR,ETA),af(1,r=-2),RR]
    for margin in strict_gaps:
        values=[val(margin,v) for v in vv]
        assert min(values)>=0 and max(values)>0
    pieces=[(ETA,af(1,r=-1),RR),
            (af(1,r=-1),af(1,r=-1,eta=1),af(-1,r=2)),
            (af(1,r=-1,eta=1),ONE,af(-1,r=1))]
    images=[(add(lo,shift),add(hi,shift)) for lo,hi,shift in pieces]
    assert images==[(af(r=1,eta=1),ONE),(RR,af(r=1,eta=1)),(ETA,RR)]
    # e=2h+kappa: the last piece is empty, but the first two images still tile D.
    assert images[2][0]==ETA and images[2][1]==RR
    def eta_equals_r(expr):
        c,r,eta,t=expr
        return (c,r+eta,F(0),t)
    endpoint_images=[tuple(eta_equals_r(expr) for expr in pair) for pair in images]
    assert endpoint_images==[(af(r=2),ONE),(RR,af(r=2)),(RR,RR)]
    assert eta_equals_r(pieces[2][0])==eta_equals_r(pieces[2][1])==ONE
    return {'fixed_prime_power_inequalities':'PASS','six_return_words':result,
            'isolated_visit_range':'0 < eta <= kappa',
            'induced_domain_image_partition':'EXACT TRANSLATION TILING',
            'return_times':[1,2,1],'eta_equals_kappa_endpoint':'PASS',
            'three_layer_formula_endpoint_e_equals_3h':'PASS',
            'topology_sampling_used':False}


def main():
    layers, symbolic=symbolic_audit()
    # exp(2h+kappa)=exp(k-3h).
    endpoint=F(16,3)*F(16,15)*F(80,81)**3
    assert endpoint==F(26214400,4782969)
    output={'pass':'SZ-KERNEL-EDGE-GERM-67','standing':'UNRATIFIED',
            'entry_commit':'a5c44833c5555323ee5f383479181706affbeaf6',
            'formula_scope':'2h < e <= 3h',
            'proved_exclusion_scope':'2h < e <= 2h+kappa',
            'experimental_endpoint':'log(26214400/4782969)',
            'dependency_sha256':PINS,'symbolic_source_audit':symbolic,
            'rational_audit':interval_audit(layers),'exact_domains':geometry_audit()}
    print(json.dumps(output,indent=2))

if __name__=='__main__':main()
