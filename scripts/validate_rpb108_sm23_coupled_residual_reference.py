#!/usr/bin/env python3
"""SM23: exact rational coupled odd residual Woodbury matrix and null floor.

Original objects: B14 = kappa I + G Gamma G* - 2|s><s| <= A_*,
K=Gamma^-1+kappa^-1 G*G, theta=1-2<s,C14^-1 s>.
For a REAL N-column residual E:
E*B14^-1 E = kappa^-1 D-kappa^-2 V*K^-1 V +2/theta p*p
p=kappa^-1 h-kappa^-2 c*K^-1 V.
An exact rational witness Z provides a Loewner upper without evaluating
K^-1; the null-feature floor applies to B14^-1, NOT A_*^-1.
The true original 890-column data are NOT computed here.
W-ODD-NEG, full even Weil, native CC27 D-Riesz and RH remain OPEN.
"""
from fractions import Fraction as F
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
def tr(a):
    return [list(x) for x in zip(*a)]
def mat(a,b):
    assert len(a[0])==len(b)
    return [[sum((x*y for x,y in zip(row,col)),F(0))
             for col in tr(b)] for row in a]
def add(a,b):
    return [[x+y for x,y in zip(rowa,rowb)] for rowa,rowb in zip(a,b)]
def neg(a):
    return [[-x for x in row] for row in a]
def sub(a,b):
    return add(a,neg(b))
def scale(a,x):
    return [[x*v for v in row] for row in a]
def diag(vals):
    return [[v if i==j else F(0) for j in range(len(vals))]
            for i,v in enumerate(vals)]
def scalar(a):
    assert len(a)==len(a[0])==1
    return a[0][0]
def inv(a):
    n=len(a)
    assert n>0 and all(len(row)==n for row in a)
    aug=[list(row)+list(unit) for row,unit in zip(a,diag([F(1)]*n))]
    for k in range(n):
        piv=next((r for r in range(k,n) if aug[r][k]),None)
        assert piv is not None,"singular exact rational matrix"
        aug[k],aug[piv]=aug[piv],aug[k]
        divisor=aug[k][k]
        aug[k]=[v/divisor for v in aug[k]]
        for i in range(n):
            if i==k: continue
            t=aug[i][k]
            aug[i]=[v-t*w for v,w in zip(aug[i],aug[k])]
    return [row[n:] for row in aug]
def psd2(m):
    assert len(m)==len(m[0])==2 and m[0][1]==m[1][0]
    return m[0][0]>=0 and m[1][1]>=0 and (
        m[0][0]*m[1][1]>=m[0][1]**2)

def run():
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert "SM23" in gov["evidence"]
    assert gov["evidence"]["SM23"]["kind"].startswith("original odd")

    # Exact 4D odd physical-style matrix test only; NOT a Galerkin
    # evaluation of 890 true original negative Taylor packets.
    kappa=F(1)
    G=[[F(1),F(0)],[F(0),F(1)],[F(1),F(1)],[F(0),F(1)]]
    gamma=diag([F(2),F(3)])
    gamma_inv=diag([F(1,2),F(1,3)])
    s=[[F(1,5)],[F(0)],[F(1,10)],[F(1,10)]]
    E=[[F(1),F(0)],[F(1),F(1)],[F(-1),F(0)],[F(0),F(1)]]
    C=add(scale(diag([F(1)]*4),kappa),mat(mat(G,gamma),tr(G)))
    B=sub(C,scale(mat(s,tr(s)),F(2)))
    K=add(gamma_inv,scale(mat(tr(G),G),1/kappa))
    K_inv=inv(K)
    D=mat(tr(E),E)
    V=mat(tr(G),E)
    h=mat(tr(s),E)
    c=mat(tr(G),s)
    true_t=scalar(mat(mat(tr(s),inv(C)),s))
    theta=1-2*true_t
    assert F(0)<theta<F(1)
    # Certified upper on 2t, intentionally looser than true value.
    L=F(1,5)
    assert F(0)<2*true_t<=L<F(1)

    exact=mat(mat(tr(E),inv(B)),E)
    qcorr=mat(mat(tr(V),K_inv),V)
    p=sub(scale(h,1/kappa),scale(mat(mat(tr(c),K_inv),V),1/kappa**2))
    wood=add(sub(scale(D,1/kappa),scale(qcorr,1/kappa**2)),
             scale(mat(tr(p),p),2/theta))
    assert exact==wood,"negative-pole exact Woodbury sign wrong"

    # Source-coupled rational trial Z, no evaluated inverse used in
    # the upper-bound formula. Here the 2x2 inverse is computed
    # solely to verify the algebra and explicit residual margins.
    Z_exact=mat(K_inv,V)
    Z=add(Z_exact,[[F(1,10),F(0)],[F(0),F(1,7)]])
    residual=sub(V,mat(K,Z))
    M=sub(add(mat(tr(Z),V),mat(tr(V),Z)),mat(mat(tr(Z),K),Z))
    rquad=mat(mat(tr(residual),K_inv),residual)
    assert qcorr==add(M,rquad)
    pz=sub(scale(h,1/kappa),scale(mat(tr(c),Z),1/kappa**2))
    delta=F(1)
    # K^-1<=Gamma: sign-protected positive-rank-one residual upper.
    c_gamma_c=scalar(mat(mat(tr(c),gamma),c))
    bound=add(sub(scale(D,1/kappa),scale(M,1/kappa**2)),
              scale(add(scale(mat(tr(pz),pz),1+delta),
                        scale(mat(mat(tr(residual),gamma),residual),
                              (1+1/delta)*c_gamma_c/kappa**4)),
                    F(2)/(1-L)))
    diff=sub(bound,exact)
    assert psd2(diff),"source-conditioned Loewner upper invalid"

    # True source correction need not be discarded. At Z_exact the
    # correction M=V*K^-1 V exactly; comparison with coarse drop.
    M_exact=sub(add(mat(tr(Z_exact),V),mat(tr(V),Z_exact)),
                mat(mat(tr(Z_exact),K),Z_exact))
    assert M_exact==qcorr
    assert psd2(qcorr)
    # The 14+1 reference is just kappa I on the orthogonal complement
    # of feature span. The test adds a fifth, null-feature coordinate.
    G5=G+[[F(0),F(0)]]
    s5=s+[[F(0)]]
    C5=add(diag([kappa]*5),mat(mat(G5,gamma),tr(G5)))
    B5=sub(C5,scale(mat(s5,tr(s5)),F(2)))
    n=[[F(0)],[F(0)],[F(0)],[F(0)],[F(1)]]
    assert mat(B5,n)==scale(n,kappa)
    assert scalar(mat(mat(tr(n),inv(B5)),n))==1/kappa

    print("SM23 exact rational demo theta",theta,flush=True)
    print("SM23 exact signed 2-column residual inverse:",exact,flush=True)
    print("SM23 rational trial upper minus exact:",diff,flush=True)
    print("SM23 rational residual Schur correction Gram:",rquad,flush=True)
    print("SM23 PASS SCOPED: signed coupled N-column Woodbury "
          "identity, rational trial Loewner upper, and finite "
          "feature-null preconditioner floor. No actual original "
          "SM10 890-column E/V/h/D computed; no W-ODD-NEG, "
          "W-EVEN-FORM, whole Weil, CC27 D-Riesz, or RH closure.",
          flush=True)

if __name__=="__main__":
    run()
