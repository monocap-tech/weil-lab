#!/usr/bin/env python3
"""MG07: exact SI29-feature-augmented Galerkin residual identity.

V=span(J,G14) where J contains original pole s and all 470
SM35 odd sources. For the genuine Astar-Galerkin response Z in V,
R=J-Astar Z satisfies J*R=G14*R=s*R=0. As B14-kappa I
is supported on the SI29 feature vectors and pole,
B14 R=kappa R, hence R*B14^-1 R=kappa^-1 R*R exactly.

Regression: independent rational 4D physical model with 2 source
columns, 1 SI29 feature, strict Astar>=B14>0, NONZERO strong
residual and feature correction in the unaugmented trial.
This is an algebraic theorem, not a computed original 470-source
physical residual nor a signed original odd positivity proof.
"""
from fractions import Fraction as F
from pathlib import Path
import json

def mat(x):return [[F(z) for z in row] for row in x]
def tr(a):return [list(x) for x in zip(*a)]
def mm(a,b):
    assert len(a[0])==len(b)
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0))
             for j in range(len(b[0]))] for i in range(len(a))]
def sub(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(x,a):return [[x*y for y in row] for row in a]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def inv(a):
    n=len(a);w=[list(a[i])+eye(n)[i] for i in range(n)]
    for k in range(n):
        if w[k][k]==0:
            q=next(i for i in range(k+1,n) if w[i][k]!=0)
            w[k],w[q]=w[q],w[k]
        u=w[k][k];w[k]=[z/u for z in w[k]]
        for i in range(n):
            if i!=k:
                z=w[i][k];w[i]=[v-z*q for v,q in zip(w[i],w[k])]
    return [row[n:] for row in w]
def gram(a,b):return mm(tr(a),b)

def exact_augmented_model():
    J=mat([[1,0],[0,1],[0,0],[0,0]])
    g=mat([[0],[0],[1],[0]])
    s=mat([[F(1,4)],[0],[0],[0]])
    U=mat([[1,0,0],[0,1,0],[0,0,1],[0,0,0]])
    A=mat([[2,0,F(1,3),F(1,4)],
           [0,2,F(1,4),F(1,5)],
           [F(1,3),F(1,4),3,F(1,6)],
           [F(1,4),F(1,5),F(1,6),2]])
    C=add(eye(4),mm(g,tr(g)))
    B=sub(C,scale(F(2),mm(s,tr(s))))
    assert B==mat([[F(7,8),0,0,0],[0,1,0,0],
                    [0,0,2,0],[0,0,0,1]])
    # A-B SPD by strict symmetric diagonal dominance.
    Delta=sub(A,B)
    assert all(Delta[i][i]>sum((abs(Delta[i][j])
               for j in range(4) if j!=i),F(0)) for i in range(4))
    assert gram(J,s)==mat([[F(1,4)],[0]])
    def response(V):
        AT=mm(gram(V,A),V)
        L=gram(V,J)
        Q=mm(inv(AT),L)
        Z=mm(V,Q)
        R=sub(J,mm(A,Z))
        assert gram(V,R)==mat([[0,0]]*len(V[0]))
        DB=mm(gram(R,inv(B)),R)
        D=gram(R,R)
        # Independent residual Gram via full original-style
        # source/trial stiffness and strong-action moments.
        ST=mm(gram(V,mm(A,A)),V)
        W=mm(gram(J,A),V)
        D2=add(sub(sub(gram(J,J),mm(W,Q)),
                   mm(tr(Q),tr(W))),mm(gram(Q,ST),Q))
        assert D==D2
        G0=mm(gram(Q,AT),Q)
        assert G0==gram(Z,mm(A,Z))
        return R,D,DB,Q,G0
    R0,D0,DB0,_,_=response(J)
    R,D,DB,Q,G0=response(U)
    # Pole-aligned added feature g_tilde=g-alpha*s, with s in J:
    # change of TRIAL coordinates only. The full original reference
    # g, not g_tilde, is still orthogonal to the augmented residual.
    alpha=F(3,5)
    Ualigned=sub(U,mm(s,mat([[0,0,alpha]])))
    assert Ualigned==mat([[1,0,-F(3,20)],[0,1,0],
                          [0,0,1],[0,0,0]])
    Raligned,Daligned,DBaligned,Qaligned,Galigned=response(Ualigned)
    assert Raligned==R and Daligned==D and DBaligned==DB
    assert Galigned==G0
    assert gram(g,Raligned)==mat([[0,0]])
    assert gram(s,Raligned)==mat([[0,0]])
    assert gram(g,R0)!=mat([[0,0]])
    assert gram(s,R0)==mat([[0,0]])
    assert DB0!=D0
    assert gram(g,R)==mat([[0,0]])
    assert gram(s,R)==mat([[0,0]])
    assert D[0][0]>0 and D[1][1]>0
    assert DB==D  # exact kappa=1 reference on augmented residual
    return dict(
      unaugmented_feature_overlap_nonzero=True,
      unaugmented_reference_response_differs_from_l2=True,
      augmented_source_count=2,augmented_trial_count=3,
      augmented_strong_residual_nonzero=True,
      augmented_Binv_residual_equals_kappa_inv_L2_exactly=True,
      pole_aligned_feature_basis_preserves_full_Galerkin_response_exactly=True,
      original_reference_g_still_orthogonal_after_pole_alignment=True,
      original_source_470_and_SI29_14_would_give_at_most_484_trial=True,
      tested_augmented_residual_gram=[[str(x) for x in row] for row in D],
      full_original_470_residual_computed=False,
      signed_odd_even_Weil_CC27_RH="OPEN")
if __name__=="__main__":
    r=exact_augmented_model()
    assert not r["full_original_470_residual_computed"]
    print(json.dumps(r,indent=2))
