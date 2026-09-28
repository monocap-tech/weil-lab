#!/usr/bin/env python3
"""GERM-65: exact local algebra, rational cone bounds, source-row regressions.

Scope: lambda_ret < e <= h. No above-h closure, Lean certification, or
canonical promotion. This is a new verifier; it does NOT rerun the earlier
large determinant programs. Requires sympy for the local algebra checks.
All printed decimal intervals are rounded OUTWARD; no float sign is used.
"""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from math import isqrt, lcm
import json
import sympy as sp

SCALE = 10**30

def down(x):
    x=F(x); return F(x.numerator*SCALE//x.denominator,SCALE)
def up(x): return -down(-F(x))

@dataclass(frozen=True)
class I:
    lo: F
    hi: F
    def __post_init__(self):
        assert self.lo <= self.hi
    @staticmethod
    def make(lo,hi=None):
        return I(down(lo),up(lo if hi is None else hi))
    def __add__(self,o):
        o=box(o); return I.make(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+-box(o)
    def __rsub__(self,o): return box(o)+-self
    def __mul__(self,o):
        o=box(o); v=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
        return I.make(min(v),max(v))
    __rmul__=__mul__
    def inv(self):
        assert self.lo>0 or self.hi<0, ('zero denominator',self)
        return I.make(1/self.hi,1/self.lo)
    def __truediv__(self,o): return self*box(o).inv()
    def __rtruediv__(self,o): return box(o)*self.inv()
    def __pow__(self,n):
        assert isinstance(n,int)
        if n<0:return self.inv()**(-n)
        v=I.make(1)
        for _ in range(n):v=v*self
        return v

def box(x):return x if isinstance(x,I) else I.make(x)

def log_box(n,terms=180):
    y=F(n-1,n+1)
    s=2*sum((y**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
    rem=2*y**(2*terms+1)/(F(2*terms+1)*(1-y*y))
    return I.make(s,s+rem)

def sqrt_box(x):
    x=box(x);assert x.lo>=0
    def lower(q):return F(isqrt(q.numerator*SCALE*SCALE//q.denominator),SCALE)
    l=lower(x.lo);r=lower(x.hi)
    return I(l,r if r*r==x.hi else r+F(1,SCALE))

def mat(x):return [[box(t) for t in r] for r in x]
def mm(x,y):
    assert len(x[0])==len(y)
    return [[sum((x[i][k]*y[k][j] for k in range(len(y))),box(0))
             for j in range(len(y[0]))] for i in range(len(x))]
def mpow(x,n):
    assert n>=0
    v=mat([[1,0],[0,1]])
    for _ in range(n):v=mm(v,x)
    return v

def inv2(x,det):
    # det is supplied only after an exact symbolic identity establishes it.
    a,b=x[0];c,d=x[1]
    return [[d/det,-b/det],[-c/det,a/det]]

def outward_decimal(q,places,upper=False):
    scale=10**places
    n=-((-q.numerator*scale)//q.denominator) if upper else q.numerator*scale//q.denominator
    sign='-' if n<0 else '';n=abs(n)
    return f'{sign}{n//scale}.{n%scale:0{places}d}'

def display_matrix(x):
    return [[[outward_decimal(t.lo,10),outward_decimal(t.hi,10,True)] for t in row] for row in x]

def zero_matrix(m):assert all(sp.factor(t)==0 for t in m)

def local_algebra():
    a,d,c=sp.symbols('a d c',nonzero=True);g=1-a;D=1-c*c
    M=sp.Matrix([[(2*a-1)/(d*a),g/a],[-g/a,d/a]])
    N=sp.Matrix([[-g/(d*a),g*(1/d**2+1/a)],[-1/a,g/d+d/a]])
    J=sp.Matrix([[0,1],[1,0]])
    K=sp.Matrix([[-d/(g*c),1/c],[-1/c,g*D/(d*c)]])
    H=sp.simplify(J*N.inv()*J)
    assert sp.factor(M.det()-1)==0
    assert sp.factor(K.det()-1)==0
    assert sp.factor(N.det()-g/d**2)==0
    assert sp.factor(H.det()-d**2/g)==0
    f=d/(g*D)
    zero_matrix(K*sp.Matrix([[1,0],[f,f*c]])-sp.Matrix([[f*c,f],[0,1]]))
    for X,Y in ((1,0),(0,1)):
        X1,Y1=M*sp.Matrix([X,Y])
        assert sp.factor(g*X+a*Y1-d*Y)==0
        assert sp.factor(g*Y1+a*X-d*X1)==0
        X1,Y1=N*sp.Matrix([X,Y])
        assert sp.factor(a*Y1+X-(d+a*g/d)*Y)==0
        assert sp.factor(d*X1-g*Y1-a*g/d*Y)==0
    # Reflection of the lower gate gives the upper gate, not another SL2 atom.
    zero_matrix(H*J*N-J)
    # Imported double-tail Schur block, checked for BOTH parity signs.
    x,y=sp.symbols('x y')
    for eps in (1,-1):
        tail=sp.Matrix([[-c*(x+eps*c*y)/D],[-c*(y+eps*c*x)/D]])
        block=sp.Matrix([[1,-eps*c],[-eps*c,1]])
        zero_matrix(block*tail+c*sp.Matrix([x,y]))
        # RC3's K2 row after the high-band reflection substitution.
        b=sp.symbols('b',nonzero=True);gg=1-b*b;ff=d/(gg*D)
        top=ff*(c*x+eps*y);high=-b*(c*x+eps*y)/D
        assert sp.factor(top+eps*b*(-eps*b*top)+(d/b)*high)==0
    # Above-h scope guard: the top row acquires a second low-seed pair.
    b,Z0,Zr,Zh,Zhr,Top=sp.symbols('b Z0 Zr Zh Zhr Top')
    gg=1-b*b
    for eps in (1,-1):
        high=-b*(c*Zh+eps*Zhr)/D
        source=Top-b*high+b*eps*(-b*eps*Top)-d*(c*Z0+eps*Zr)/D
        guarded=gg*Top-d*(c*Z0+eps*Zr)/D+b*b*(c*Zh+eps*Zhr)/D
        assert sp.factor(source-guarded)==0
    # The characteristic-polynomial compression is valid in this derived state.
    zero_matrix(M*M-sp.trace(M)*M+sp.eye(2))
    return {'bulk_det':1,'bridge_det':1,'lower_gate_det':'g/d^2',
            'upper_gate_det':'d^2/g','return_dets':[1,1],
            'local_source_identities':'PASS','parities':[1,-1]}

def cone_certificate():
    l2,l3,l5=log_box(2),log_box(3),log_box(5)
    beta=(l3/l2)*sqrt_box(F(2,3));c=(l3/l2)/sqrt_box(3);d=(l5/l2)/sqrt_box(5)
    a=(beta*c)**2;g=1-a;D=1-c*c
    assert c.lo>0 and c.hi<1 and g.hi<0 and D.lo>0
    M=mat([[(2*a-1)/(d*a),g/a],[-g/a,d/a]])
    N=mat([[-g/(d*a),g*(1/(d*d)+1/a)],[-1/a,g/d+d/a]])
    J=mat([[0,1],[1,0]])
    K=mat([[-d/(g*c),1/c],[-1/c,g*D/(d*c)]])
    Mi=inv2(M,box(1));Ni=inv2(N,g/(d*d));Ki=inv2(K,box(1))
    H=mm(mm(J,Ni),J);Hi=mm(mm(J,N),J)
    # Positive directed maps: +kappa and -lambda_ret.
    Tk=mm(mm(mm(Ni,mpow(Mi,3)),Hi),K)
    Tw=mm(mm(mm(Ni,mpow(Mi,4)),Hi),K)
    ell_in=mm(mm(mat([[g,-d]]),mpow(M,4)),N)
    ell_out=mm(mm(mm(mat([[-d,g]]),mpow(Mi,4)),Hi),K)
    bounds_k=[[(10,11),(3,4)],[(6,7),(2,3)]]
    bounds_w=[[(12,13),(3,5)],[(9,10),(2,4)]]
    for T,bds in ((Tk,bounds_k),(Tw,bounds_w)):
        for i in range(2):
            for j in range(2):
                lo,hi=bds[i][j];assert T[i][j].lo>lo and T[i][j].hi<hi
        # l1 growth on same-sign quadrant forward, opposite-sign backward.
        forward=[T[0][j].lo+T[1][j].lo for j in range(2)]
        backward=[T[1][1].lo+T[1][0].lo,T[0][1].lo+T[0][0].lo]
        assert min(forward)>5 and min(backward)>5
    assert -1<ell_in[0][0].lo<=ell_in[0][0].hi<F(-4,5)
    assert F(13,10)<ell_in[0][1].lo<=ell_in[0][1].hi<F(3,2)
    assert 4<ell_out[0][0].lo<=ell_out[0][0].hi<6
    assert 1<ell_out[0][1].lo<=ell_out[0][1].hi<2
    return {'T_kappa':display_matrix(Tk),'T_minus_lambda':display_matrix(Tw),
            'entry_covector':display_matrix(ell_in),'exit_covector':display_matrix(ell_out),
            'uniform_l1_factor':5,'quadrant_certificate':'PASS',
            'coefficient_box':display_matrix([[beta,c,d,a,g,D]])}

# Affine source points: coefficients of (q,j,k,e,z), exactly as RC5.
Q=(1,0,0,0,0);J=(0,1,0,0,0);K=(0,0,1,0,0);E=(0,0,0,1,0);Z=(0,0,0,0,1)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(n,a):return tuple(n*x for x in a)
def sub(a,b):return add(a,mul(-1,b))
ZERO=mul(0,Q);R=add(Q,J);S=sub(Q,K);U=add(K,E);V=add(sub(Q,J),E);W=add(mul(2,Q),E)
H=sub(add(mul(2,J),K),Q);P=sub(sub(Q,J),K);KAP=sub(K,mul(5,H));LAM=sub(H,KAP)

@lru_cache(None)
def prime_sign(v):
    aq,aj,ak=map(F,v);exps=(2*aq-3*aj+4*ak,-aq+2*aj-ak,-ak)
    scale=lcm(*(x.denominator for x in exps));num=den=1
    for prime,expo in zip((2,3,5),exps):
        n=int(expo*scale)
        if n>=0:num*=prime**n
        else:den*=prime**(-n)
    return (num>den)-(num<den)

def at(t,ef,zf):
    return tuple(F(t[i])+(t[3]*ef+t[4]*zf)*KAP[i] for i in range(3))

def region(t,ef,zf):
    for name,lo,hi in (('A',ZERO,U),('B',U,V),('D',V,Q),('T',Q,W)):
        if prime_sign(at(sub(t,lo),ef,zf))>0 and prime_sign(at(sub(hi,t),ef,zf))>0:return name
    raise AssertionError(('threshold point',t,ef,zf))

def source_row(t,rg,eps):
    row=[(t,'1',1)]
    if rg=='A':row += [(add(t,R),'beta',1),(add(t,S),'d',1),(sub(U,t),'d',-eps)]
    elif rg=='B':row += [(add(t,R),'beta',1)]
    elif rg=='T':row += [(sub(t,Q),'mu',1),(sub(W,t),'mu',-eps)]
    return tuple(sorted(row))

def orbit(ef,zf):
    seen={Z};todo=deque([Z]);rgs={}
    while todo:
        t=todo.popleft();rg=region(t,ef,zf);rgs[t]=rg
        for s,_,_ in source_row(t,rg,1):
            if s not in seen:seen.add(s);todo.append(s)
        assert len(seen)<500,'regression orbit unexpectedly exceeds finite scope'
    return seen,rgs

def reflect(t):return (*t[:3],t[3]+t[4],-t[4])
def orient(t):
    assert t[3:]==(0,1) or t[3:]==(1,-1)
    return t[4]

def check_regions(rgs,verts):
    for t,rg in rgs.items():
        lo,hi={'A':(ZERO,U),'B':(U,V),'D':(V,Q),'T':(Q,W)}[rg]
        for margin in (sub(t,lo),sub(hi,t)):
            signs=[prime_sign(at(margin,ef,zf)) for ef,zf in verts]
            assert min(signs)>=0 and max(signs)>0

def check_gauge(rgs):
    for t,rg in rgs.items():
        plus=source_row(t,rg,1)
        gauged=tuple(sorted((s,c,sg*orient(t)*orient(s)) for s,c,sg in plus))
        assert gauged==source_row(t,rg,-1)

def regressions():
    sk=[]
    for base in (ZERO,P,S,R,add(Q,S)):
        sk.extend(add(base,mul(n,H)) for n in range(6))
    sk.append(add(P,mul(6,H)));assert len(set(sk))==31
    base,bregs=orbit(F(1,2),F(137,1000))
    constants={add(t,mul(n,KAP)) for t in sk for n in (0,1)}
    expected={add(C,Z) for C in constants}|{add(C,sub(E,Z)) for C in constants}
    assert base==expected and len(base)==124
    check_regions(bregs,((0,0),(1,0),(1,1)))
    # Literal RC4 block-row rules reproduce the source rows, not just dimensions.
    for C in constants:
        for reflected in (False,True):
            off=sub(E,Z) if reflected else Z;opp=Z if reflected else sub(E,Z)
            t=add(C,off);rg=bregs[t];assert rg==bregs[add(C,opp)]
            row=[(t,'1',1)]
            if rg=='A':row += [(add(add(C,R),off),'beta',1),(add(add(C,S),off),'d',1),(add(sub(K,C),opp),'d',-1)]
            elif rg=='B':row += [(add(add(C,R),off),'beta',1)]
            elif rg=='T':row += [(add(sub(C,Q),off),'mu',1),(add(sub(mul(2,Q),C),opp),'mu',-1)]
            assert tuple(sorted(row))==source_row(t,rg,1)
    low,lr=orbit(F(6,5),F(7,100));mid,mr=orbit(F(6,5),F(3,5));high,hr=orbit(F(6,5),F(113,100))
    assert (len(low),len(mid),len(high))==(186,124,186)
    assert mid==base and mr==bregs
    assert {reflect(t) for t in low}==high
    for t in low:
        assert tuple(sorted((reflect(s),c,sg) for s,c,sg in source_row(t,lr[t],1)))==source_row(reflect(t),hr[reflect(t)],1)
    check_regions(lr,((1,0),(2,0),(2,1)))
    check_regions(mr,((1,0),(1,1),(2,1)))
    assert sum(orient(t)==1 for t in low)==93
    for rgs in (bregs,lr,mr,hr):check_gauge(rgs)
    expected_plus={add(s,mul(n,KAP))[:3] for s in sk for n in (0,1,2)}
    expected_minus={add(s,mul(n,KAP))[:3] for s in sk for n in (-1,0,1)}
    assert {t[:3] for t in low if orient(t)==1}==expected_plus
    assert {t[:3] for t in low if orient(t)==-1}==expected_minus
    # Exact fixed logarithmic inequalities used in the e<=h source partition.
    for v in (H,KAP,sub(H,mul(5,KAP)),sub(mul(6,KAP),H),sub(P,add(K,H))):
        assert prime_sign(v[:3])>0
    return {'base_variables':124,'base_block_rows':'EXACT MATCH',
            'extra_layer_variables':[186,124,186],'middle_rows':'EXACT MATCH',
            'reflection_gauge':'PASS','affine_polygon_typing':'PASS',
            'large_determinants_rerun':False}

def main():
    result={'pass':'SZ-KERNEL-EDGE-GERM-65','standing':'UNRATIFIED',
            'scope':'lambda_ret < e <= h',
            'local_algebra':local_algebra(),'cone':cone_certificate(),
            'source_regressions':regressions()}
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
