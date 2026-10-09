#!/usr/bin/env python3
"""RPB108 NF19 — exact collective first-TWO-exterior native Schur response.

Runs only exact Fraction/integer arithmetic on three authenticated
complete original signed Weil source interval archives. Certified response
is for span{e112,e114} or span{e113,e115}, not the full F112 inverse.
No mpmath eigenvalue enters the certificate.
"""
import argparse,gzip,hashlib,json
from math import lcm
from fractions import Fraction as F

OLD_SHA='f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81'
FIRST_SHA='da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee'
SECOND_SHA='0a8f4ebd0778fa5c90209b3021d22791bdb0d9b73e0f19df608e04ed9ba2bcad'
GRID=10**75

def read(path,sha):
    with gzip.open(path,'rb') as f:raw=f.read()
    assert hashlib.sha256(raw).hexdigest()==sha
    return json.loads(raw)

def bareiss_sign(m):
    """Exact integer fraction-free leading principal determinant sign."""
    m=[row[:] for row in m];previous=1;positive=0
    for k in range(len(m)):
        pivot=m[k][k]
        if pivot<=0:return positive,-1 if pivot<0 else 0
        positive+=1
        for i in range(k+1,len(m)):
            for j in range(i,len(m)):
                numerator=m[i][j]*pivot-m[i][k]*m[k][j]
                value,remainder=divmod(numerator,previous)
                assert remainder==0
                m[i][j]=m[j][i]=value
        previous=pivot
    return positive,1

def ceil_fraction(x):
    return -((-x.numerator)//x.denominator)

def certify(e112,first,second):
    old=read(e112,OLD_SHA);new1=read(first,FIRST_SHA);new2=read(second,SECOND_SHA)
    assert old['aperture']==new1['aperture']==new2['aperture']=='53/50'
    assert old['dim']==112 and new1['parent_sha256']==OLD_SHA
    assert new2['parent_E112_SHA256']==OLD_SHA
    assert new2['parent_first_boundary_SHA256']==FIRST_SHA
    assert new1['new_columns']==[112,113] and new2['new_columns']==[114,115]
    assert len(old['complete_form'])==3192
    assert len(new1['original_full_source'])==114
    assert len(new2['original_full_source'])==116
    source={**old['complete_form'],**new1['original_full_source'],**new2['original_full_source']}
    assert len(source)==3422
    center={};error=F(0);checks=0
    for key,record in source.items():
        pole='poles' if 'poles' in record else 'pole'
        assert set(record)=={'arch','prime',pole,'full'}
        for interval in record.values():
            lo,hi=map(F,interval);assert lo<=hi;checks+=1
        lo,hi=map(F,record['full'])
        assert lo<=sum(F(record[k][1]) for k in ('arch','prime',pole))
        assert hi>=sum(F(record[k][0]) for k in ('arch','prime',pole))
        mid=((lo+hi)/2*GRID).__floor__()
        center[key]=mid
        error=max(error,abs(F(mid,GRID)-lo),abs(F(mid,GRID)-hi))
    assert checks==13688
    eps_units=ceil_fraction(58*error*GRID)
    assert F(eps_units,GRID)<F(1,10**40)
    results=[]
    for parity,high,lower,upper,previous_upper in [
            ('even',[112,114],F(302,1000),F(303,1000),F(204,1000)),
            ('odd',[113,115],F(275,1000),F(276,1000),F(206,1000))]:
        ix=list(range(0 if parity=='even' else 1,112,2))
        A=[[center[f'{min(i,j)},{max(i,j)}'] for j in ix] for i in ix]
        B=[[center[f'{i},{j}'] for j in high] for i in ix]
        C=[[center[f'{min(i,j)},{max(i,j)}'] for j in high] for i in high]
        # Strictly positive original two-dimensional high Gram, with source error.
        c00=F(C[0][0],GRID)-error;c11=F(C[1][1],GRID)-error
        c01=max(abs(F(C[0][1],GRID)-error),abs(F(C[0][1],GRID)+error))
        assert c00>3 and c11>3 and c00*c11>c01*c01
        tests=[]
        for r,direction in ((lower,1),(upper,-1)):
            denominator=r.denominator;numerator=r.numerator
            M=[[numerator*A[i][j] for j in range(56)]+
               [denominator*B[i][0],denominator*B[i][1]] for i in range(56)]
            for k in range(2):
                M.append([denominator*B[i][k] for i in range(56)]+
                         [denominator*C[k][j] for j in range(2)])
            for i in range(58):
                M[i][i]+=direction*denominator*eps_units
            signature=bareiss_sign(M)
            assert signature==((57,-1) if direction==1 else (58,1))
            tests.append(dict(threshold=str(r),envelope_direction=direction,
                              certified_leading_positive_pivots=signature[0],
                              final_pivot_sign=signature[1]))
        assert lower>previous_upper
        results.append(dict(parity=parity,high_degrees=high,
          collective_two_mode_response_strict=[str(lower),str(upper)],
          first_mode_response_upper_from_CC53=str(previous_upper),
          second_mode_residual_operator_supremum_strict_lower=str(lower-previous_upper),
          all_direction_remaining_fraction_strict_lower=str(1-upper),
          verified_Bareiss_signs=tests))
    return dict(status='PASS',milestone='NF19',aperture='53/50',
       original_E112_sha256=OLD_SHA,first_boundary_sha256=FIRST_SHA,
       second_boundary_sha256=SECOND_SHA,complete_signed_native_entries=3422,
       interval_component_checks=checks,center_grid=str(GRID),
       maximum_source_entry_error=str(error),
       paid_58_by_58_operator_error=str(F(eps_units,GRID)),
       exact_large_integer_sign_tests=4,
       parity_collective_certificates=results,
       true_infinite_F112_inverse_evaluated=False,
       corrected_whole_domain_Schur=False,whole_original_aperture_positive=False,
       RH=False,Lean=False)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('e112');p.add_argument('first');p.add_argument('second')
    p.add_argument('--output')
    a=p.parse_args()
    out=json.dumps(certify(a.e112,a.first,a.second),indent=2)+'\n'
    if a.output:
        with open(a.output,'w') as f:f.write(out)
    print(out)
