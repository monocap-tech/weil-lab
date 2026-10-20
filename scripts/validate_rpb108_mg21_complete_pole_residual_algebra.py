#!/usr/bin/env python3
"""MG21 exact-rational pole-corrected source / strong residual identities.

This is a NON-TRIVIAL FINITE-DIMENSIONAL ALGEBRAIC REGRESSION ONLY.
It does not mechanize the mathematical lemma that finitely many
independent compactly supported functions have strictly positive
positive-frequency Fourier moments on any nonempty open interval.
That lemma is proved separately in MG21's note by holomorphic identity
and Fourier uniqueness.

Nor does this small regression certify the true original A_o Fourier
operator, its closure/domain, 470D inverse, signed odd/even or RH.
"""
import argparse
import json
from fractions import Fraction as F
from pathlib import Path

def mat(a):
    return [[F(x) for x in row] for row in a]
def trans(a):
    return [list(row) for row in zip(*a)]
def mm(a,b):
    assert a and b and len(a[0])==len(b)
    t=trans(b)
    return [[sum((x*y for x,y in zip(row,col)),F(0))
             for col in t] for row in a]
def plus(a,b):
    return [[x+y for x,y in zip(ra,rb)] for ra,rb in zip(a,b)]
def times(q,a):
    return [[F(q)*v for v in row] for row in a]
def diff(a,b):
    return plus(a,times(-1,b))
def vec(a):
    assert all(len(row)==1 for row in a)
    return [row[0] for row in a]
def outer(x,y):
    return [[a*b for b in y] for a in x]
def col(a,k):
    return [[row[k]] for row in a]
def diag(a):
    return [a[i][i] for i in range(len(a))]
def eq(a,b):
    assert a==b
    return True

def verify():
    # Physical full-Hilbert finite-dimensional surrogate, 6 rows.
    # The first four columns are independent physical source pilots.
    W=mat([[1,0,2,0],
           [0,1,1,0],
           [1,1,0,1],
           [2,0,1,1],
           [0,1,2,1],
           [1,-1,1,2]])
    n=len(W[0]); m=len(W)
    assert n==4 and m==6
    s=col(W,n-1)
    Ao=mat([[6,1,0,0,0,0],
            [1,7,1,0,0,0],
            [0,1,8,1,0,0],
            [0,0,1,9,1,0],
            [0,0,0,1,10,1],
            [0,0,0,0,1,11]])
    assert Ao==trans(Ao)
    S=mm(s,trans(s))
    Astar=plus(Ao,times(-2,S))
    H=mm(trans(W),W)
    Go=mm(mm(trans(W),Ao),W)
    So=mm(mm(trans(W),Ao),mm(Ao,W))
    b=mm(trans(W),s)
    c=mm(mm(trans(W),Ao),s)
    assert b==col(H,n-1)
    assert c==col(Go,n-1)
    sigma=mm(trans(s),s)[0][0]
    assert sigma>0
    bb=mm(b,trans(b))
    pole_cross=plus(mm(c,trans(b)),mm(b,trans(c)))
    analytic_G=plus(Go,times(-2,bb))
    analytic_S=plus(plus(So,times(-2,pole_cross)),times(4*sigma,bb))
    direct_G=mm(mm(trans(W),Astar),W)
    direct_S=mm(mm(trans(W),Astar),mm(Astar,W))
    eq(analytic_G,direct_G)
    eq(analytic_S,direct_S)
    assert analytic_S==trans(analytic_S)
    assert analytic_G==trans(analytic_G)

    # Actual R=J-Astar Y, with a nontrivial physical source response Y.
    C=mat([[1,2],
           [3,-1],
           [2,1],
           [1,-2]])
    Y=mm(W,C)
    J=mat([[1,0],
           [-1,3],
           [2,2],
           [0,-2],
           [3,1],
           [1,4]])
    AY=mm(Astar,Y)
    R=diff(J,AY)
    direct_R2=mm(trans(R),R)
    identity_R2=plus(
        diff(mm(trans(J),J),
             plus(mm(trans(J),AY),mm(trans(AY),J))),
        mm(trans(AY),AY))
    eq(direct_R2,identity_R2)
    assert all(x>0 for x in diag(direct_R2))
    # Explicitly show the proper pole response matters; dropping
    # the mixed cross terms changes the true strong source matrix.
    wrong_S=plus(So,times(4*sigma,bb))
    assert wrong_S!=analytic_S
    return {
        "status":"EXACT_RATIONAL_POLE_SOURCE_AND_RESIDUAL_IDENTITY_REGRESSION",
        "canonical_W_ODD_NEG":"OPEN",
        "finite_surrogate_ambient_dimension":m,
        "finite_surrogate_source_dimension":n,
        "genuine_sinh_pole_analog_is_explicit_source_channel":True,
        "original_pole_gram_column_identity_passed":True,
        "original_pole_Ao_response_column_identity_passed":True,
        "complete_Gstar_Go_minus_2bbstar_identity_passed":True,
        "complete_Sstar_Aostar_squared_mixed_pole_identity_passed":True,
        "complete_strong_residual_RstarR_identity_passed":True,
        "dropping_mixed_pole_cross_terms_detected_as_wrong":True,
        "analytic_original_compact_support_Fourier_uniqueness_proved_by_script":False,
        "original_physical_24channel_quantitative_gamma_computed":False,
        "complete_original_low_frequency_band_and_tail_integrated":False,
        "original_full470_source_Galerkin_strong_residual_certified":False,
        "signed_complete_odd_even_Weil_CC27_RH":"OPEN",
        "independent_original_Fourier_form_and_domain_audit":"OPEN",
        "interpretation":"Algebraic regression of necessary complete-operator pole and residual identities only; analytic compact-support Fourier positivity is a written mathematical lemma, not computer-certified by this test."
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/mg21_exact_pole_and_residual_identities.json")
    args=p.parse_args()
    result=verify()
    out=Path(__file__).resolve().parent.parent/args.output
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+"\n")
    print("MG21 exact rational complete pole/residual algebra PASS",flush=True)
if __name__=="__main__":
    main()
