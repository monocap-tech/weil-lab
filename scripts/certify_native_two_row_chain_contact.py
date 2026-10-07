#!/usr/bin/env python3
"""Exact finite projection controls, not an analytic/actual-null certificate."""
from fractions import Fraction as F
import json

def transpose(a):
    return [list(row) for row in zip(*a)]

def multiply(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0))
             for j in range(len(b[0]))] for i in range(len(a))]

def subtract(a,b):
    return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]

def energy(a,v):
    return sum((v[i]*a[i][j]*v[j] for i in range(len(v))
                for j in range(len(v))),F(0))

def positive_pivots(a):
    a=[row[:] for row in a]
    values=[]
    for k in range(len(a)):
        p=a[k][k]
        assert p>0
        values.append(p)
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                a[i][j]-=a[i][k]*a[k][j]/p
    return values

entry_checks=energy_checks=pivot_checks=negative_controls=0
for q in range(1,13):
    L=[[F(1),F(q,2),F(1,3),F(0)],
       [F(0),F(1),F(q,3),F(1,5)],
       [F(0),F(0),F(1),F(q,7)],
       [F(0),F(0),F(0),F(1)]]
    W=[[F(q+i+1) if i==j else F(0) for j in range(4)] for i in range(4)]
    A=multiply(multiply(transpose(L),W),L)
    pivot_checks+=len(positive_pivots(A))
    H=[r[:2] for r in A[:2]]
    det=H[0][0]*H[1][1]-H[0][1]*H[1][0]
    assert det>0 and H[0][1]!=0
    Hi=[[H[1][1]/det,-H[0][1]/det],[-H[1][0]/det,H[0][0]/det]]
    AX=[r[:2] for r in A]
    correction=multiply(multiply(AX,Hi),transpose(AX))
    B=subtract(A,correction)
    # Independently form the lower Schur block; all other entries must be zero.
    C=[r[2:] for r in A[:2]]
    S=subtract([r[2:] for r in A[2:]],multiply(multiply(transpose(C),Hi),C))
    pivot_checks+=len(positive_pivots(S))
    for i in range(4):
        for j in range(4):
            expected=S[i-2][j-2] if i>=2 and j>=2 else F(0)
            assert B[i][j]==expected
            entry_checks+=1
    # Full mixed annihilation: both columns, not merely two diagonal zeros.
    assert all(B[i][j]==0 for i in range(4) for j in range(2))
    assert S[0][0]*S[1][1]-S[0][1]*S[1][0]>0
    for i in range(-2,3):
        for j in range(-2,3):
            v=[F(1),F(i),F(j),F(i-j)]
            av=multiply(transpose(AX),[[x] for x in v])
            coeff=multiply(Hi,av)
            residual=[v[0]-coeff[0][0],v[1]-coeff[1][0],v[2],v[3]]
            assert energy(B,v)==energy(A,residual)>=0
            energy_checks+=1
    # Normalizing each nonorthogonal row separately does NOT give projection.
    wrong_inverse=[[1/H[0][0],F(0)],[F(0),1/H[1][1]]]
    wrong=subtract(A,multiply(multiply(AX,wrong_inverse),transpose(AX)))
    assert wrong[0][0]==-H[0][1]**2/H[1][1]<0
    negative_controls+=1

print(json.dumps({
    "status":"PASS",
    "scope":"rational finite projection and kernel controls; analytic contact proved separately",
    "nonorthogonal_backgrounds":12,
    "independent_schur_entry_agreements":entry_checks,
    "residual_energy_agreements":energy_checks,
    "positive_background_and_schur_pivots":pivot_checks,
    "diagonal_only_negative_controls":negative_controls,
    "actual_divisor_row_realization":False,
    "actual_null_or_lean_certificate":False,
},indent=2,sort_keys=True))
