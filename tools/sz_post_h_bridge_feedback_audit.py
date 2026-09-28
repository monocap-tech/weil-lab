#!/usr/bin/env python3
"""GERM-66: exact two-layer feedback reduction and six-map cone certificate.

Scope: h < e <= 2h. No above-2h claim, canonical promotion, or Lean claim.
Run with assertions enabled. Dependency: sympy and the pinned GERM-65 helper
in this directory. The helper supplies rational interval primitives only;
its old large source-regression and determinant routines are not rerun.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sympy as sp
import sz_mixed_return_cone_audit as old

PARENT_SHA256 = 'f43eaf0e86e823a2f7ebeb6580b8ea12fcf4587ad405f708c3b66d6939b2a6c0'
assert __debug__, 'Run without -O: assertions are part of this audit.'
assert hashlib.sha256(Path(old.__file__).read_bytes()).hexdigest() == PARENT_SHA256

def zcheck(x):
    assert all(sp.factor(t) == 0 for t in x)

def symbolic_audit():
    a,d,c=sp.symbols('a d mu',nonzero=True)
    g=1-a; D=1-c*c; alpha=a/d; f=d/(g*D)
    nu=d+a*g/d; chi=2*a+d*d-1
    M=sp.Matrix([[(2*a-1)/(d*a),g/a],[-g/a,d/a]])
    N=sp.Matrix([[-g/(d*a),g*(1/d**2+1/a)],[-1/a,nu/a]])
    K=sp.Matrix([[-d/(g*c),1/c],[-1/c,g*D/(d*c)]])
    J=sp.Matrix([[0,1],[1,0]]); P=sp.diag(1,0); Q=sp.diag(0,1)
    row=sp.Matrix([[-d-a/d,1]])*K
    R=sp.Matrix([[0,a],[row[0],row[1]]])
    S=sp.Matrix([[1,-nu],[a*K[0,0],a*K[0,1]+alpha*row[1]]])
    assert sp.factor(R.det()+a*chi/(g*c))==0
    N0=(-R.inv()*S).applyfunc(sp.factor)
    K0=(K-alpha*P*K*(N0+alpha*Q)).applyfunc(sp.factor)
    v=sp.Matrix([a*g/d**3,a*g/d**2])
    F2=(N*N0+v*sp.Matrix([[0,1]])).applyfunc(sp.factor)
    N1=(F2*N0.inv()).applyfunc(sp.factor)
    K1=(K*(N0+alpha*Q)*N0.inv()).applyfunc(sp.factor)
    det0=sp.factor(N0.det())
    assert sp.factor(K0.det()-det0)==0
    assert sp.factor(F2.det()-2*g/d**2)==0
    zcheck(K1-J*K0.inv()*J)
    zcheck(N1*N0-F2)
    # Exact four-coordinate feedback bridge, before reducing its boundary data.
    B4=(K-alpha**2*P*K*Q).row_join(-alpha*P*K).col_join((alpha*K*Q).row_join(K))
    zcheck(B4-(sp.eye(2).row_join(-alpha*P).col_join(sp.zeros(2).row_join(sp.eye(2))))
           *sp.diag(K,K)*(sp.eye(2).row_join(sp.zeros(2)).col_join((alpha*Q).row_join(sp.eye(2)))))
    assert sp.factor(B4.det()-1)==0
    # Four physical seed coordinates, with parity in the reflected ones.
    x,y,z,w=sp.symbols('x y z w')
    for eps in (1,-1):
        B=eps*y; DD=eps*w
        W0=sp.Matrix([x,f*(x+c*B)])
        W1=sp.Matrix([z,f*(z+c*DD)-alpha*W0[1]])
        V1=sp.Matrix([f*(c*z+DD),DD])
        V0=sp.Matrix([f*(c*x+B)-alpha*V1[0],B])
        zcheck(B4*W0.col_join(W1)-V0.col_join(V1))
        # Original reduced first-cell row at t, not just a guessed transfer.
        raw=(D-a)*x+a*D*W1[1]-d*D*W0[1]-a*c*B
        zcheck(sp.Matrix([raw-D*(x+a*W1[1]-nu*W0[1])]))
    X,Y=sp.symbols('X Y'); W0=sp.Matrix([X,Y]); W1=N0*W0; W2=F2*W0
    V0=K0*W0; V1=K*(N0+alpha*Q)*W0
    # Row at t and reflected row at eta-t; these close the two-port solve.
    zcheck(sp.Matrix([X+a*W1[1]-nu*Y,a*V0[0]+V1[1]-nu*V1[0]]))
    # Source rows for the second bottom step, with the feedback retained.
    Z1=(W1[1]+alpha*Y-f*W1[0])/(f*c)
    zcheck(sp.Matrix([(D-a)*W1[0]+a*D*W2[1]-d*D*W1[1]-a*c*Z1,
                     g*W2[1]+a*(c*Z1+W1[0])/D-d*W2[0]]))
    # Reflection gives all three upper gates.
    for NN in (N0,N,N1): zcheck((J*NN.inv()*J)*J*NN-J)
    for NN,dd in ((M,1),(N,g/d**2),(K,1)): assert sp.factor(NN.det()-dd)==0
    zcheck(M*M-sp.trace(M)*M+sp.eye(2))
    # Return determinants follow from the audited factor determinants.
    dn=g/d**2; df=2*dn; dn1=sp.factor(N1.det())
    for got,want in ((dn/dn,1),(dn1*det0/dn,2),(dn1*det0/df,1),(dn/df,sp.Rational(1,2))):
        assert sp.factor(got-want)==0
    # At e>2h the once-unforced upper layer acquires another feedback bracket.
    x0,xr,xh,xhr,x2,x2r,top=sp.symbols('x0 xr xh xhr x2 x2r top')
    b=sp.symbols('b',nonzero=True)
    for eps in (1,-1):
        raw=top-b*(-b*(c*x2+eps*x2r)/D)-b*b*top-d*(c*xh+eps*xhr)/D
        guarded=(1-b*b)*top-d*(c*xh+eps*xhr)/D+b*b*(c*x2+eps*x2r)/D
        zcheck(sp.Matrix([raw-guarded]))
    return {'four_coordinate_bridge_det':1,'local_source_rows_both_parities':'PASS',
            'two_port_pivot':'-a*(2*a+d^2-1)/(g*mu)',
            'det_N0':str(det0),'det_K0_equals_det_N0':True,'det_F':'2*g/d^2',
            'gate_and_bridge_reflections':'PASS',
            'return_determinants':{'00+':1,'10+':2,'11+':1,'00-':1,'01-':'1/2','11-':1},
            'bulk_characteristic_identity':'PASS','above_2h_guard':'PASS'}

# Exact interval certificate. All inversions are either symbolically justified
# above, or use a direct interval determinant that excludes zero.
I=old.I; mat=old.mat; mm=old.mm; inv2=old.inv2; mpow=old.mpow

def msum(A,B):return [[x+y for x,y in zip(ar,br)] for ar,br in zip(A,B)]
def mscale(s,A):return [[s*x for x in row] for row in A]
def mdet(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def norm_inf(A):return max(sum(max(abs(x.lo),abs(x.hi)) for x in row) for row in A)

def interval_audit():
    l2,l3,l5=old.log_box(2),old.log_box(3),old.log_box(5)
    c=(l3/l2)/old.sqrt_box(3);beta=(l3/l2)*old.sqrt_box(F(2,3));d=(l5/l2)/old.sqrt_box(5)
    a=(beta*c)**2;g=1-a;D=1-c*c;alpha=a/d;nu=d+a*g/d;chi=2*a+d*d-1
    assert g.hi<0 and D.lo>0 and d.lo>0 and c.lo>0 and a.lo>0 and chi.lo>0
    M=mat([[(2*a-1)/(d*a),g/a],[-g/a,d/a]])
    N=mat([[-g/(d*a),g*(1/(d*d)+1/a)],[-1/a,nu/a]])
    K=mat([[-d/(g*c),1/c],[-1/c,g*D/(d*c)]])
    J=mat([[0,1],[1,0]]);P=mat([[1,0],[0,0]]);Q=mat([[0,0],[0,1]])
    row=mm(mat([[-d-a/d,1]]),K)[0]
    R=mat([[0,a],row]);S=mat([[1,-nu],[a*K[0][0],a*K[0][1]+alpha*row[1]]])
    pivot=-a*chi/(g*c); assert pivot.lo>10
    N0=mscale(-1,mm(inv2(R,pivot),S));det0=mdet(N0)
    assert F(-12,1000)<det0.lo and det0.hi<F(-11,1000)
    N0i=inv2(N0,det0)
    F2=msum(mm(N,N0),mat([[0,a*g/d**3],[0,a*g/d**2]]))
    detF=2*g/d**2; F2i=inv2(F2,detF)
    N1=mm(F2,N0i)
    K0=msum(K,mscale(-alpha,mm(mm(P,K),msum(N0,mscale(alpha,Q)))))
    K0i=inv2(K0,det0);K1=mm(mm(J,K0i),J)
    Mi=inv2(M,old.box(1));Ni=inv2(N,g/d**2)
    Hi=mm(mm(J,N),J);H1i=mm(mm(J,N1),J)
    T={
        '00+':mm(mm(mm(Ni,mpow(Mi,3)),Hi),K),
        '10+':mm(mm(mm(Ni,mpow(Mi,3)),H1i),K0),
        '11+':mm(mm(mm(F2i,mpow(Mi,2)),H1i),K0),
        '00-':mm(mm(mm(Ni,mpow(Mi,4)),Hi),K),
        '01-':mm(mm(mm(F2i,mpow(Mi,3)),Hi),K),
        '11-':mm(mm(mm(F2i,mpow(Mi,3)),H1i),K0)}
    determinants={'00+':F(1),'10+':F(2),'11+':F(1),'00-':F(1),'01-':F(1,2),'11-':F(1)}
    cert={}
    for key,B in T.items():
        assert all(t.lo>0 for row in B for t in row)
        forward=min(B[0][j].lo+B[1][j].lo for j in (0,1))
        backward=min(B[1][1].lo+B[1][0].lo,B[0][1].lo+B[0][0].lo)/determinants[key]
        assert forward>F(5,4) and backward>F(5,4), (key,forward,backward)
        cert[key]={'matrix':old.display_matrix(B),'determinant':str(determinants[key]),
                   'forward_l1_lower':old.outward_decimal(forward,8),
                   'backward_l1_lower':old.outward_decimal(backward,8)}
    locals_={'N0':N0,'N1':N1,'F':F2,'K0':K0,'K1':K1}
    # A deliberately coarse common norm bound for finite reconstruction.
    all_gates=dict(locals_,M=M,N=N,H=mm(mm(J,Ni),J),H0=mm(mm(J,N0i),J),H1=mm(mm(J,inv2(N1,detF/det0)),J))
    for name,B in all_gates.items():
        assert norm_inf(B)<300, (name,norm_inf(B))
        det=mdet(B);assert det.lo>0 or det.hi<0
        assert norm_inf(inv2(B,det))<300, name
    return {'coefficient_boxes':old.display_matrix([[c,d,a,g,D]]),
            'two_port_pivot':old.display_matrix([[pivot]]),
            'det_N0':old.display_matrix([[det0]]),
            'local_matrices':{k:old.display_matrix(v) for k,v in locals_.items()},
            'local_matrix_and_inverse_inf_bound':300,
            'returns':cert,'common_forward_backward_factor':'5/4','large_determinants_rerun':False}

# All return-word domain claims are linear inequalities after h-normalization.
# Verify them on exact rational polytope vertices, uniformly for
# 1/6 <= kappa/h <= 1/5, 0 <= eta/h <= 1, 0 <= t/h <= 1.
# An affine expression is [constant, coeff_r, coeff_eta, coeff_t].
def af(c=0,r=0,eta=0,t=0):return tuple(map(F,(c,r,eta,t)))
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def neg(x):return tuple(-a for a in x)
def sub(x,y):return add(x,neg(y))
def val(x,v):return x[0]+sum(a*b for a,b in zip(x[1:],v))
ZERO=af();ONE=af(1);RR=af(r=1);ETA=af(eta=1);TT=af(t=1)

@lru_cache(None)
def vertices(constraints):
    out=set()
    for selected in combinations(constraints,3):
        A=sp.Matrix([row[1:] for row in selected]);dd=A.det()
        if not dd:continue
        vv=tuple(F(t) for t in A.inv()*sp.Matrix([-row[0] for row in selected]))
        if all(val(row,vv)>=0 for row in constraints):out.add(vv)
    assert out
    return tuple(sorted(out))

WORDS={'00+':['N','M','M','M','H'],
       '10+':['N','M','M','M','H1'],
       '11+':['N0','N1','M','M','H1'],
       '00-':['N','M','M','M','M','H'],
       '01-':['N0','N1','M','M','M','H'],
       '11-':['N0','N1','M','M','M','H1']}
REGIONS={'N0':(ZERO,ETA),'N':(ETA,ONE),'N1':(ONE,add(ONE,ETA)),
         'M':(add(ONE,ETA),af(4,r=1)),
         'H1':(af(4,r=1),af(4,r=1,eta=1)),
         'H':(af(4,r=1,eta=1),af(5,r=1))}

def word_geometry():
    fixed={
        'kappa_positive':old.KAP[:3],
        'h_minus_5kappa':old.sub(old.H,old.mul(5,old.KAP))[:3],
        '6kappa_minus_h':old.sub(old.mul(6,old.KAP),old.H)[:3],
        'p_minus_k_minus_2h':old.sub(old.sub(old.P,old.K),old.mul(2,old.H))[:3],
        'j_minus_k_minus_2h':old.sub(old.sub(old.J,old.K),old.mul(2,old.H))[:3],
        'k_minus_3h':old.sub(old.K,old.mul(3,old.H))[:3]}
    assert all(old.prime_sign(v)>0 for v in fixed.values())
    common=(af(F(-1,6),r=1),af(F(1,5),r=-1),ETA,sub(ONE,ETA),TT,sub(ONE,TT))
    answer={}
    for key,word in WORDS.items():
        i,j=int(key[0]),int(key[1]);wrap=key[2]=='-'
        y=af(-int(wrap),r=1,t=1)
        side=af(-1 if wrap else 1,r=1 if wrap else -1,t=1 if wrap else -1)
        constraints=common+(side, sub(ETA,TT) if i else sub(TT,ETA),sub(ETA,y) if j else sub(y,ETA))
        vv=vertices(constraints)
        margins=[]
        for n,name in enumerate(word):
            point=add(y,af(n));lo,hi=REGIONS[name]
            for margin in (sub(point,lo),sub(hi,point)):
                signs=[val(margin,v) for v in vv]
                assert min(signs)>=0 and max(signs)>0,(key,n,name,margin,signs)
                margins.append(margin)
        assert add(y,af(len(word)))==af(5,r=1,t=1)
        answer[key]={'directed_word':word,'exact_polytope_vertices':len(vv),'all_gate_margins':'PASS'}
        if key in ('11+','11-'):
            # Explicitly audit the e=2h face, not just open parameter cells.
            endpoint=constraints+(sub(ETA,ONE),)
            ev=vertices(endpoint)
            for margin in margins:
                vals=[val(margin,v) for v in ev]
                assert min(vals)>=0 and max(vals)>0,(key,margin,vals)
            answer[key]['eta_equals_h_face']='PASS'
    return {'fixed_prime_power_inequalities':'PASS','six_return_words':answer,
            'endpoint_e_equals_2h':'PASS','topology_sampling_used':False}

def main():
    assert F(16,3)*F(81,80)**2 == F(2187,400)
    out={'pass':'SZ-KERNEL-EDGE-GERM-66','standing':'UNRATIFIED',
         'entry_commit':'23005f480cdff4eb04ee460f4cd6cf60d9ebcf0e',
         'scope':'h < e <= 2h','dependency_sha256':PARENT_SHA256,
         'symbolic_algebra':symbolic_audit(),'rational_cones':interval_audit(),
         'exact_domains':word_geometry()}
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
