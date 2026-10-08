"""Exact complete-source shell, defect-resolvent and shifted-level controls.

Finite matrices audit the algebra; they are not a zeta source-gain certificate.
"""
from fractions import Fraction as F
import json


def transpose(A): return [list(c) for c in zip(*A)]
def mm(A,B):
    return [[sum((a*b for a,b in zip(row,col)),F(0))
             for col in zip(*B)] for row in A]
def add(A,B,sign=1):
    return [[a+sign*b for a,b in zip(ar,br)] for ar,br in zip(A,B)]
def ident(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def inverse2(A):
    det=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    assert det
    return [[A[1][1]/det,-A[0][1]/det],[-A[1][0]/det,A[0][0]/det]]
def det2(A): return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def quadratic(A,x): return mm(transpose(x),mm(A,x))[0][0]


def run():
    checks=0; cases=0; positive=0; negative=0
    def check(v):
        nonlocal checks
        assert v
        checks+=1
    for p in [F(0),F(1,4),F(1,2),F(3,4)]:
      for q in [F(0),F(1,3),F(2,3)]:
       for r in [F(0),F(1,8)]:
        T=[[p,r],[F(0),q]]
        Dt=add(ident(2),mm(transpose(T),T),-1)
        Dn=add(ident(2),mm(T,transpose(T)),-1)
        check(Dt[0][0]>0 and det2(Dt)>0)
        check(Dn[0][0]>0 and det2(Dn)>0)
        check(inverse2(Dn)==add(ident(2),mm(mm(T,inverse2(Dt)),transpose(T))))
        for u in [F(0),F(1,8),F(1,2),F(1)]:
         for v in [F(0),F(1,5),F(2,3)]:
            K=[[u],[v]]
            Aold=mm(T,transpose(T))
            Tall=[row+[K[i][0]] for i,row in enumerate(T)]
            Anew=mm(Tall,transpose(Tall))
            check(Anew==add(Aold,mm(K,transpose(K))))
            cost=mm(mm(transpose(K),inverse2(Dn)),K)[0][0]
            schur=1-mm(transpose(K),K)[0][0]-mm(mm(mm(mm(transpose(K),T),inverse2(Dt)),transpose(T)),K)[0][0]
            check(schur==1-cost)
            check(cost>=0)
            x=mm(mm(inverse2(Dt),transpose(T)),K)+[[F(1)]]
            full=add(ident(3),mm(transpose(Tall),Tall),-1)
            check(quadratic(full,x)==schur)
            if schur>0:
                positive+=1
                # Entire negative-source resolvent update, including all slots.
                inv_old=inverse2(Dn)
                update=mm(mm(inv_old,K),mm(transpose(K),inv_old))
                update=[[a/schur for a in row] for row in update]
                check(inverse2(add(ident(2),Anew,-1))==add(inv_old,update))
            elif schur<0:
                negative+=1
                check(quadratic(full,x)<0)
            cases+=1
    # Directional incoming-source suppression: equal raw norm, different cost.
    for d in [F(1,4),F(1,16),F(1,256),F(1,65536)]:
        A=[[1-d,F(0)],[F(0),F(0)]]
        for k in [F(1,8),F(1,4),F(1,2)]:
            parallel=[[k],[F(0)]];orthogonal=[[F(0)],[k]]
            inv=inverse2(add(ident(2),A,-1))
            check(quadratic(inv,parallel)==k*k/d)
            check(quadratic(inv,orthogonal)==k*k)
            check(quadratic(ident(2),parallel)==quadratic(ident(2),orthogonal))
    # Exact unit contact with nonzero complete source energies.
    N=[[F(4,5),F(3,5)]]
    Q=add(ident(2),mm(transpose(N),N),-1)
    h=[[F(4,3)],[F(1)]]
    check(quadratic(Q,h)==0)
    check(quadratic(ident(2),h)==F(25,9))
    check(quadratic(mm(transpose(N),N),h)==F(25,9))
    # Original positive eigenlevel: shift creates unit gain; original gap stays.
    N=[[F(4,5),F(1,2)]]
    gram=mm(transpose(N),N)
    h=transpose(N); mu=F(11,100)
    Q=add(ident(2),gram,-1)
    check(mm(Q,h)==[[mu*a[0]] for a in h])
    shifted=add(Q,[[mu*a for a in row] for row in ident(2)],-1)
    check(quadratic(shifted,h)==0)
    check(quadratic(Q,h)>0)
    # Spectral leakage integral identity evaluated exactly on diagonal spectra.
    for lam in [F(0),F(1,4),F(3,4),F(15,16),F(255,256)]:
        # Integral_0^lam du/(1-u)^2=1/(1-lam)-1.
        integral=1/(1-lam)-1
        check(1+integral==1/(1-lam))
        check(integral>=0)
    # A fixed ORIGINAL nested sequence: old columns never change, all retained.
    cols=[F(1,2),F(1,3),F(1,4),F(1,5),F(1,6)]
    old=F(0)
    for col in cols:
        new=old+col*col
        check(new>=old)
        check(1-new==(1-old)*(1-col*col/(1-old)))
        old=new
    check(positive>0 and negative>0)
    return {'passed':True,'exact_checks':checks,'coupled_source_cases':cases,
            'positive_cases':positive,'negative_cases':negative,
            'complete_negative_source_gram_update':'A_t=A_s+K K*',
            'exact_continuation_cost':'K* (I-A_s)^(-1) K',
            'directional_leakage_requirement':'incoming near-unit output weight must vanish relative to old defect',
            'new_zeta_source_gain_bound':False,
            'arithmetic_relative_loss_nondivergence_proved':False,
            'new_aperture_certificate':False,'lean_certified':False}


if __name__=='__main__': print(json.dumps(run(),indent=2))
