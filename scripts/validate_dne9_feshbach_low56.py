#!/usr/bin/env python3
"""DNE9 exact rational Feshbach, residual and finite-null control tests.

This tests only the finite-dimensional algebra/quantifiers in the DNE9
report. The actual high-mode native F112 inverse/residual is NOT evaluated.
"""
from fractions import Fraction as F
from itertools import product
import json

def dot(x,y):
    return sum((a*b for a,b in zip(x,y)),F(0))

def determinant(A):
    # Exact Leibniz 2x2 and 3x3 are sufficient for these controls.
    if len(A)==2:
        return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    assert len(A)==3
    return sum(((-1)**j)*A[0][j]*determinant(
        [[A[i][k] for k in range(3) if k!=j] for i in range(1,3)])
        for j in range(3)),F(0))

def run():
    count=0
    def check(v):
        nonlocal count
        assert v
        count+=1

    K=[F(1,4),F(1,2)]
    for s in [F(-1,32),F(0),F(1,16)]:
        A=[[K[i]*K[j]+(s if i==j==0 else F(1) if i==j==1 else F(0))
            for j in range(2)] for i in range(2)]
        C=F(1)
        full=[[A[0][0],A[0][1],K[0]],
              [A[1][0],A[1][1],K[1]],
              [K[0],K[1],C]]
        check(A[0][0]>0 and determinant(A)>0)
        check(C>0)
        check(determinant(full)==s)
        for lam in [F(-1),F(-1,2),F(0),F(1,4),F(1,2),F(3,4)]:
            d=C-lam
            Schur=[[A[i][j]-(lam if i==j else 0)-K[i]*K[j]/d
                    for j in range(2)] for i in range(2)]
            shifted=[[full[i][j]-(lam if i==j else 0)
                      for j in range(3)] for i in range(3)]
            check(d>0)
            check(determinant(shifted)==d*determinant(Schur))
            for x,y in product((-2,-1,0,1,2),repeat=2):
                v=[F(x),F(y)]
                z=-dot(K,v)/d
                q=dot(v,[dot(A[i],v) for i in range(2)])+2*dot(K,v)*z+z*z
                mass=dot(v,v)+z*z
                qshift=q-lam*mass
                sc=dot(v,[dot(Schur[i],v) for i in range(2)])
                check(qshift==sc)
                # Strict decrease of the pencil, including full response.
                deriv=-dot(v,v)-(dot(K,v)/d)**2
                check(deriv==-dot(v,v)-z*z)
                # Approximate response at half the true high solution.
                zhat=z/F(2)
                cross=dot(K,v)
                qhat=dot(v,[dot(A[i],v) for i in range(2)])+2*cross*zhat+zhat*zhat
                qhatshift=qhat-lam*(dot(v,v)+zhat*zhat)
                r=cross+d*zhat
                check(qhatshift-sc==r*r/d)
                check(sc<=qhatshift)
                # DNE9's 101 is conservative at lambda zero only.
                if lam==0:
                    check(sc>=qhatshift-F(101)*r*r)

    # The s=0 contact has actual high component: both blocks positive.
    v=[F(1),F(0)]
    high=-dot(K,v)
    check(high==-F(1,4))
    check(dot(v,v)+high*high==F(17,16))

    # Finite penalty certificate on the joint kernel of S=diag(0,1)
    # and moment ell(v)=v_2. Two reflected forms have opposite decisions.
    S2=[[F(0),F(0)],[F(0),F(1)]]
    ell=[F(0),F(1)]
    P=[[sum((S2[i][k]*S2[k][j] for k in range(2)),F(0))
        +ell[i]*ell[j] for j in range(2)] for i in range(2)]
    check(P==[[F(0),F(0)],[F(0),F(2)]])
    M_good=[[F(1),F(3)],[F(3),F(-1)]]
    M_bad=[[F(-1),F(0)],[F(0),F(1)]]
    t=F(16)
    Lgood=[[M_good[i][j]+t*P[i][j] for j in range(2)] for i in range(2)]
    Lbad=[[M_bad[i][j]+t*P[i][j] for j in range(2)] for i in range(2)]
    check(Lgood[0][0]>0 and determinant(Lgood)>0)
    check(Lbad[0][0]<0)
    check(dot(v,[dot(M_good[i],v) for i in range(2)])>0)
    check(dot(v,[dot(M_bad[i],v) for i in range(2)])<0)

    # Unmeasured high source directions can hide all finite tested rows.
    # E=R, F=R²; high block I; cross K=(0,1/4).
    Alow=F(1,16)
    highK=(F(0),F(1,4))
    schur=Alow-sum((q*q for q in highK),F(0))
    check(schur==0)
    check(Alow-highK[0]**2>0) # first measured high mode passes
    check(highK[1]!=0) # genuine missing high response
    assert count==1930, count
    return dict(stage="DNE9 native pole-free Feshbach controls",
                all_passed=True,exact_fraction_checks=count,
                native_high_form_floor="1/101 (analytic inherited NF10/CC40)",
                eigenmode_count_per_parity=56,
                first_two_high_columns_close_full_inverse=False,
                actual_full_high_dual_residual_evaluated=False,
                reflected_finite_gate_certified=False,
                RH_proved=False,lean_certified=False)

if __name__=="__main__":
    print(json.dumps(run(),indent=2))
