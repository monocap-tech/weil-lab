#!/usr/bin/env python3
"""Exact full 118D physical Gram Riesz bound: 108 sine+pole backbone,
plus 10 true original x*cos(2*pi*c*x) degree-one SI10 generators.
All sine/pole/degree-one cross terms paid by elementary IBP bounds.
Neither original Astar action nor full 470D/484D Schur is claimed.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import json

from validate_rpb108_si10_complement_positivity import protected_inner_cover
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_si29_global_sine_pole_108_gram import verify as parent_verify

B=F(11,10)
DEN=10**12
INDICES=(96,98,99,100,101,102,103,104,105,106)
ROOT=Path(__file__).resolve().parents[1]

def upward(x):
    z=F(x)*DEN
    return F(-(-z.numerator//z.denominator),DEN)

def sine_first_bound(q):
    # |int[-B,B] x*sin(2*pi*q*x)dx|
    q=abs(F(q))
    return F(0) if not q else B/(3*q)+F(1,18*q*q)

def cosine_second_bound(q):
    # |int[-B,B] x²*cos(2*pi*q*x)dx|. Since 2*pi>6,
    # exact twofold IBP gives three nonnegative rational terms.
    q=abs(F(q))
    assert q>0
    return B*B/(3*q)+B/(9*q*q)+F(1,54*q**3)

def certify():
    parent=parent_verify()
    assert parent['status']=='EXACT_RATIONAL_GLOBAL_108_ORIGINAL_SINES_PLUS_POLE_PHYSICAL_GRAM'
    lam=F(parent['complete_global_108_physical_Gram_lower'])
    assert lam>F(1,200)
    clusters,*_=protected_inner_cover()
    assert len(clusters)==107
    centers=[(a+b)/2 for a,b,_ in clusters]
    orders=[taylor_order(b-a,9)[0] for a,b,_ in clusters]
    assert sum(orders)+1==470
    assert centers[96]==F(18235,32) and centers[106]==F(113013,128)
    assert all(orders[j]>=2 for j in INDICES)
    assert centers[0]==F(37,64)
    # Exact sinh(11/20)<3/5 via positive Taylor series.
    z=B/2
    k=24
    p=2*k+1
    sinh_hi=sum((z**(2*i+1)/factorial(2*i+1)
                 for i in range(k)),F(0))
    sinh_hi+=z**p/factorial(p)/(1-z*z/F((p+1)*(p+2)))
    assert sinh_hi<F(3,5)

    row_lowers=[]
    cross_sq=F(0)
    rows=[]
    for j in INDICES:
        c=centers[j]
        # v_j(x)=x*cos(2*pi*c*x) is an ODD original source.
        # ||v_j||²=B³/3+C_2(2c)/2.
        diag=B**3/3-upward(cosine_second_bound(2*c)/2)
        # sin(alpha)*x*cos(beta)=[x*sin(alpha+beta)+
        # x*sin(alpha-beta)]/2, with S_1(0)=0 exactly.
        qs=[upward((sine_first_bound(c+ci)+
                    sine_first_bound(c-ci))/2) for ci in centers]
        # g=x*sinh(x/2) is even and increasing for x>=0;
        # endpoint+variation IBP gives |<v_j,s>|
        # <=4B*sinh(B/2)/(2*pi*c) < 2B*(3/5)/(3c).
        qp=upward(2*B*F(3,5)/(3*c))
        col_sq=sum((q*q for q in qs),F(0))+qp*qp
        cross_sq+=col_sq
        # Off-diagonals: <v_i,v_j> =
        # (C_2(ci-cj)+C_2(ci+cj))/2.
        off=sum((upward((cosine_second_bound(c-centers[h])+
                         cosine_second_bound(c+centers[h]))/2)
                 for h in INDICES if h!=j),F(0))
        drow=diag-off
        row_lowers.append(drow)
        rows.append({'index':j,'center':str(c),'degree':1,
                     'diag_lower':str(diag),'off_row_abs_upper':str(off),
                     'cross_108_column_sq_upper':str(col_sq),
                     'Gershgorin_row_lower':str(drow)})
    d=min(row_lowers)
    schur=d-cross_sq/lam
    joint=(lam*d-cross_sq)/(lam+d)
    assert d>F(41,100) and cross_sq<F(2,1000)
    assert schur>F(4,100)
    assert joint>F(1,2000)
    result={
      'status':'EXACT_RATIONAL_GLOBAL_118_ORIGINAL_PHYSICAL_GRAM',
      'base_original_dimension':108,
      'new_original_degree_one_count':10,
      'joint_original_dimension':118,
      'original_cluster_indices':list(INDICES),
      'parent_108_physical_gram_lower':str(lam),
      'added_10D_physical_gram_lower':str(d),
      'complete_108_by_10_cross_Frobenius_sq_upper':str(cross_sq),
      'added_10D_schur_after_108_lower':str(schur),
      'joint_118_physical_gram_lower':str(joint),
      'origins':'SI10 true supported xcos degree-one; 107 degree-zero sines and true sinh pole',
      'methods':'Montgomery-Vaughan parent; exact rational IBP, outward ceiling, Gershgorin and 2x2 determinant/trace',
      'added_sources':rows,
      'complete_470_physical_gram':'OPEN',
      'SI29_full_14D_augmentation_schur':'OPEN',
      'Astar_signed_Wodd_even_CC27_RH':'OPEN'
    }
    out=ROOT/'artifacts/si29_global_118_degree1_physical_gram.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('Exact global 118 physical Gram PASS:',
          'new_10D_Schur>',float(schur),
          'whole_118_lambda_min>',float(joint),flush=True)
    return result

if __name__=='__main__':
    certify()
