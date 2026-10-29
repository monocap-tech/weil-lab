#!/usr/bin/env python3
"""NF389 exact source-pinned original two-witness sharpened upper.

Original n513 must be byte-identical to GH Actions run 40820718599
artifact 12882010193, ZIP SHA256 193483... and member SHA256 e0aaa...
This proves a METHOD-specific finite 2D stop, NOT infinite residual control.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)

N512_SHA='9d4b07fb2ca42c14ed995ddcd69811201eacb6f13f9f795a70c4b64889e9f83b'
N513_SHA='e0aaa0abb29c8ec75b3524ec6197c12235a7fc7fa66d76c77c4643c2ff27bffe'
SOURCE_SHA='abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770'
RANK_SHA='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
B=F(11,10)
D=F(2401,2*10**28)
R=F(1,75)
X=F(145134,10**6)
Y=F(7421,10**6)
UP=F(307,2000)
EXACT_COMPARISON=F(13809111,89984000)
REMAINING=F(1693,2000)

def load(p,sha,n):
    buf=Path(p).read_bytes()
    assert hashlib.sha256(buf).hexdigest()==sha,('native SHA mismatch',n)
    j=json.loads(buf)
    assert j['unfitted_n']==n and j['selected_rank']==242 and j['critical_count']==4
    assert j['original_source_sha256']==SOURCE_SHA
    assert j['original_rank_sha256']==RANK_SHA
    assert j['original_physical_16_Gram_overlaps'] is True
    assert j['original_signed_32_CE_BP_overlaps'] is True
    assert j['original_WJJ_WJF_archived_cells_reused']==30371
    assert j['original_lowband_integral_computed'] is False
    assert j['entire_exterior_inverse_computed'] is False
    assert F(j['original_direction_four_squared_residual_budget'])==D
    assert j['W_ODD_NEG']==j['RH']=='OPEN'
    g=tuple(F(t) for t in j['outside_E4_norm2_interval'])
    b=tuple(F(t) for t in j['complete_original_signed_u4_qperp_interval'])
    assert 0<g[0]<=g[1]<B and 0<b[0]<=b[1]
    return j,g,b

def evaluate(p512,p513,output=None):
    a,g1,b1=load(p512,N512_SHA,512)
    z,g2,b2=load(p513,N513_SHA,513)
    assert z['original_512_native_source_sha256']==N512_SHA
    for key in ('parent_original_archive_sha256','original_frame_sha256','archive_original_signed_matrix_sha256','archive_original_mixed_sha256'):
        assert a[key]==z[key],key
    x1=b1[1]*b1[1]/(g1[0]*D)
    y1=b2[1]*b2[1]/(g2[0]*D)
    assert x1<X and y1<Y
    # For original unprojected sine v_512 and v_513,
    # <v512,v513>=0, ||v_i||^2=B.
    # Projected q_i=(I-P_(J242+F4))v_i gives
    # |rho|^2 <=(B-g1)(B-g2)/(g1*g2).
    assert (B-g1[0])*(B-g2[0]) < R*R*g1[0]*g2[0]
    # Let a=b1/sqrt(g1), b=b2/sqrt(g2).
    # b^T G^-1 b=(a²+b²-2*rho*a*b)/(1-rho²)
    # <= [a²+b²+R*(a²/4+4*b²)]/(1-R²)
    # since 2|ab| <=a²/4+4*b² (exact Young inequality).
    exact_cap=((1+R/4)*X+(1+4*R)*Y)/(1-R*R)
    assert exact_cap==EXACT_COMPARISON and exact_cap<UP
    assert 1-UP==REMAINING
    out={
     'standing':'NF389 NATIVE ORIGINAL N513 ARCHIVAL AND SHARP TWO-RAY UPPER; METHOD STOP ONLY',
     'original_n512_sha256':N512_SHA,'original_n513_sha256':N513_SHA,
     'original_n513_artifact_run':40820718599,'original_n513_artifact_id':12882010193,
     'original_physical_and_signed_overlap_preflight_pass':True,
     'n512_squared_ray_share_D_actual_outward_upper':str(x1),
     'n513_squared_ray_share_D_actual_outward_upper':str(y1),
     'certified_normalized_physical_cross_upper':str(R),
     'coarse_n512_squared_dual_fraction_upper':str(X),
     'coarse_n513_squared_dual_fraction_upper':str(Y),
     'exact_young_inequality_two_ray_fraction_upper':str(EXACT_COMPARISON),
     'certified_whole_two_ray_fraction_strict_upper':str(UP),
     'if_full_original_strong_residual_squared_ge_D_then_unmeasured_L2_orthogonal_remainder_fraction_strictly_gt':str(REMAINING),
     'unmeasured_remainder_observed':False,
     'original_nf387_signed_fourier_mismatch_integrated':False,
     'original_lowband_upper_computed':False,
     'full_original_exterior_strong_residual_upper_computed':False,
     'entire_energy_inverse_computed':False,
     'original_operator_domain':'OPEN',
     'W_ODD_NEG':'OPEN','RH':'OPEN'}
    if output:
        p=Path(output);p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(json.dumps(out,indent=2)+'\n')
    print('NF389 SHA-pinned authentic native n512+n513 PASS')
    print('NF389 certified FULL 2D physical dual squared upper < 307/2000 D (15.35%)')
    print('NF389 if full squared residual >=D, unmeasured physical remainder > 1693/2000 D')
    print('NF389 no n513 new signed cells / no infinite residual upper / W-ODD-NEG, RH OPEN')
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--original-512',required=True)
    p.add_argument('--original-513',required=True)
    p.add_argument('--output')
    a=p.parse_args()
    evaluate(a.original_512,a.original_513,a.output)
