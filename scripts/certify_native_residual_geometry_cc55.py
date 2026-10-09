#!/usr/bin/env python3
"""Original two-boundary residual norm and low-energy phase geometry.
Authenticated NF19 sources; exact interval transforms and paid determinant signs.
No full F112 residual or full critical frame is asserted.
"""
import argparse,json
from fractions import Fraction as F
from certify_native_collective_boundary_cc53 import OLD_SHA,NEW_SHA,read,bareiss_sign,ceil_fraction
SECOND_SHA='0a8f4ebd0778fa5c90209b3021d22791bdb0d9b73e0f19df608e04ed9ba2bcad'
GRID=10**100
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    p=[x*y for x in a for y in b];return min(p),max(p)
def div(a,b):
    assert b[0]>0
    return mul(a,(1/b[1],1/b[0]))
def I(p):return tuple(map(F,p['full']))
def round_interval(a):
    mid=(((a[0]+a[1])/2)*GRID).__floor__()
    return mid,max(abs(F(mid,GRID)-v) for v in a)

def certify(old_path,first_path,second_path):
    old=read(old_path,OLD_SHA);first=read(first_path,NEW_SHA);second=read(second_path,SECOND_SHA)
    assert old['aperture']==first['aperture']==second['aperture']=='53/50'
    assert second['parent_E112_SHA256']==OLD_SHA and second['parent_first_boundary_SHA256']==NEW_SHA
    assert second['new_columns']==[114,115] and len(second['original_full_source'])==116
    source={**old['complete_form'],**first['original_full_source'],**second['original_full_source']}
    assert len(source)==3422
    results=[]
    for parity,j,k,lo,hi,r1,r2,ker_lower in [
        ('even',112,114,F(136,1000),F(137,1000),(F(203,1000),F(204,1000)),(F(302,1000),F(303,1000)),F(53,1000)),
        ('odd',113,115,F(112,1000),F(113,1000),(F(205,1000),F(206,1000)),(F(275,1000),F(276,1000)),F(55,1000))]:
        ix=list(range(0 if parity=='even' else 1,112,2))
        d1=I(source[f'{j},{j}']);c=I(source[f'{j},{k}']);d2=I(source[f'{k},{k}'])
        alpha=div(c,d1)
        residual_d=sub(d2,div(mul(c,c),d1));assert residual_d[0]>3
        Ainterval=[[I(source[f'{min(i,l)},{max(i,l)}']) for l in ix] for i in ix]
        binterval=[sub(I(source[f'{i},{k}']),mul(alpha,I(source[f'{i},{j}']))) for i in ix]
        error=F(0);A=[];b=[]
        for row in Ainterval:
            ar=[]
            for v in row:
                mid,e=round_interval(v);ar.append(mid);error=max(error,e)
            A.append(ar)
        for v in binterval:
            mid,e=round_interval(v);b.append(mid);error=max(error,e)
        d,e=round_interval(residual_d);error=max(error,e)
        eps_units=ceil_fraction(57*error*GRID);eps=F(eps_units,GRID)
        assert eps<F(1,10**39)
        tests=[]
        for r,direction in [(lo,1),(hi,-1)]:
            den=r.denominator;num=r.numerator
            M=[[num*A[i][l] for l in range(56)]+[den*b[i]] for i in range(56)]
            M.append([den*v for v in b]+[den*d])
            for i in range(57):M[i][i]+=direction*den*eps_units
            signs=bareiss_sign(M)
            assert signs==((56,-1) if direction==1 else (57,1))
            tests.append(dict(r=str(r),envelope_direction=direction,positive_leading_minors=signs[0],final_sign=signs[1]))
        # Two positive rank-one operators in the exact A-energy metric:
        # largest eigenvalue R2, traces R1 and residual Rdelta.
        angle=div(mul(sub(r2,r1),sub(r2,(lo,hi))),mul(r1,(lo,hi)))
        assert 0<angle[0]<angle[1]<1
        kernel_response=mul((lo,hi),sub((F(1),F(1)),angle))
        assert kernel_response[0]>ker_lower and kernel_response[1]<F(59,1000)
        minor= sub(add(r1,(lo,hi)),r2)
        assert minor[0]>0 and minor[1]<r2[0]
        results.append(dict(parity=parity,high_degrees=[j,k],
            residual_high_diagonal_interval=[str(v) for v in residual_d],
            transformed_57_by_57_operator_error=str(eps),paid_residual_norm_tests=tests,
            residual_relative_norm_strict=[str(lo),str(hi)],
            squared_A_energy_source_angle_outward=[str(v) for v in angle],
            residual_norm_on_first_source_kernel_outward=[str(v) for v in kernel_response],
            residual_norm_on_first_source_kernel_simplified_strict=[str(ker_lower),'59/1000'],
            source_active_plane_lower_frame_eigenvalue_strict=[str(v) for v in minor],
            source_active_plane_dimension=2,full_retained_source_kernel_dimension=54,
            full_retained_lower_frame_bound=False))
    return dict(status='PASS',milestone='CC55',aperture='53/50',
        source_sha256={'E112':OLD_SHA,'first':NEW_SHA,'second':SECOND_SHA},
        upstream_R1_dependency='CC53 exact original collective certificate',
        upstream_R2_dependency='NF19 exact original collective certificate, replay required separately',
        parities=results,exact_paid_large_determinant_tests=4,
        actual_second_residual_relative_norm_certified=True,
        actual_source_active_plane_frame_certified=True,
        complete_F112_response=False,critical_subspace_in_active_plane_certified=False,
        CC52_carrier_transfer=False,whole_aperture_positive=False,RH=False,Lean=False)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('old');p.add_argument('first');p.add_argument('second');p.add_argument('--output');a=p.parse_args()
    result=certify(a.old,a.first,a.second);out=json.dumps(result,indent=2)+'\n'
    if a.output:open(a.output,'w').write(out)
    print(out)
