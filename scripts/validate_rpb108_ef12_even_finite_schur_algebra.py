#!/usr/bin/env python3
"""EF12: exact *abstract* finite-dimensional residual Schur identity.

This is a guarded algebraic regression for the next ORIGINAL even-form
obligation after EF10's conservative cap no-go. The model is deliberately
small and rational. It establishes NO quantitative original Weil matrix
certificate, and imports no false cofinite coercivity or hidden inverse.
"""
from fractions import Fraction as F

def transpose(A):
    return [list(row) for row in zip(*A)]

def mult(A,B):
    assert len(A[0])==len(B)
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
             for j in range(len(B[0]))] for i in range(len(A))]

def add(A,B,sign=1):
    assert len(A)==len(B) and len(A[0])==len(B[0])
    return [[A[i][j]+sign*B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]

def inv(A):
    n=len(A)
    assert all(len(row)==n for row in A)
    work=[list(A[i])+[F(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        p=next((i for i in range(j,n) if work[i][j]),None)
        assert p is not None
        work[j],work[p]=work[p],work[j]
        piv=work[j][j]
        work[j]=[v/piv for v in work[j]]
        for i in range(n):
            if i==j:continue
            s=work[i][j]
            work[i]=[work[i][k]-s*work[j][k] for k in range(2*n)]
    return [row[n:] for row in work]

def identity(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]

def subtract_scalar(A,t):
    return [[a-(t if i==j else 0) for j,a in enumerate(row)]
            for i,row in enumerate(A)]

def psd2(A):
    assert len(A)==len(A[0])==2 and A[0][1]==A[1][0]
    return A[0][0]>=0 and A[1][1]>=0 and A[0][0]*A[1][1]-A[0][1]**2>=0

def certificate(A,B,C,T):
    """A: 2x2 original signed exceptional block, B: 2x3 cross,
    C: 3x3 positive complement, T: 3x2 approximate Riesz lifts.

    If C >= gamma I is separately established and ||r_i||_C*
    <= rho_i, then S >= M - (sum rho_i²) I.

    In this finite *illustration*, exact C^-1 computes all quantities
    to verify equality. In a genuine even infinite-dimensional
    application computing C^-1 is NOT allowed as an assumption.
    """
    invC=inv(C)
    H=mult(invC,transpose(B))
    BT=mult(B,T)
    TTBT=transpose(BT)
    CTT=mult(C,T)
    M=add(add(add(A,BT,-1),TTBT,-1),mult(transpose(T),CTT))
    S=add(A,mult(B,H),-1)
    resid=add(transpose(B),CTT,-1)
    E=mult(transpose(resid),mult(invC,resid))
    diff=add(M,S,-1)
    assert diff==E, "Exact residual energy identity failed"
    # Exact nonnegative Gram validation for two columns.
    assert psd2(E)
    delta=add(H,T,-1)
    assert E==mult(transpose(delta),mult(C,delta))
    rho2=E[0][0]+E[1][1] # ONLY model: exactly computed dual norms
    assert rho2>=0
    bound=add([[rho2,F(0)],[F(0),rho2]],E,-1)
    assert psd2(bound)
    assert S==add(subtract_scalar(M,rho2),bound)
    return dict(A=A,B=B,C=C,M=M,S=S,E=E,rho2=rho2,
                sufficient=psd2(subtract_scalar(M,rho2)),
                direct_schur_psd=psd2(S))

def validate():
    C=[[F(4),F(1),F(0)],
       [F(1),F(3),F(0)],
       [F(0),F(0),F(2)]]
    # Positive definite: leading minors 4, 11, 22.
    assert 4>0 and 4*3-1==11 and 22>0
    B=[[F(1),F(0),F(1)],
       [F(0),F(1),F(1)]]
    T=[[F(1,4),F(0)],
       [F(0),F(1,3)],
       [F(1,2),F(1,2)]]
    positive=certificate([[F(3),F(0)],[F(0),F(4)]],B,C,T)
    assert positive["sufficient"] and positive["direct_schur_psd"]
    # The NEGATIVE example rejects the mistaken inference that
    # cofinite positivity alone establishes full positivity.
    negative=certificate([[F(0),F(0)],[F(0),F(0)]],B,C,T)
    assert not negative["sufficient"] and not negative["direct_schur_psd"]
    print("EF12 exact original-form STRUCTURAL Schur algebra: PASS",flush=True)
    print("EF12 identity: S = M - E; E=R^T C^-1 R >= 0.",flush=True)
    print("EF12 sufficient: M - (sum_i rho_i^2)I >= 0.",
          flush=True)
    print("EF12 positive toy direct and sufficient:",positive["direct_schur_psd"],
          positive["sufficient"],flush=True)
    print("EF12 negative toy direct and sufficient:",negative["direct_schur_psd"],
          negative["sufficient"],flush=True)
    print("EF12 actual original even finite V, complement coercivity,",
          "Riesz lifts, residual dual bounds, full Q_e PSD,",
          "whole Weil, global bridge and RH: ALL OPEN.",flush=True)

if __name__=="__main__":
    validate()
