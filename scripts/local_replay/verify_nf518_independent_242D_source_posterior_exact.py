#!/usr/bin/env python3
"""NF518 independent exact 242D source fit posterior, different precision.

Independent complete 242x242 source integer inverse verification with
1e68 Gram and 1e38 inverse scales; independently checks original source
242-vector normal residual at 1e125, no reliance on prior trial residual.
All ACCEPTANCE arithmetic exact, candidate NumPy inverse untrusted.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
SHA='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
S=10**125;U=10**68;V=10**38;N=242
def floor(x):return x.numerator//x.denominator
def ceil(x):return -floor(-x)
def dyad(v):
    a,e=map(int,v)
    return Q(a<<e) if e>=0 else Q(a,1<<(-e))
def quant(v,s):
    a,e=map(int,v)
    return (a*s)<<e if e>=0 else (a*s)//(1<<(-e))
def f(v):
    a,e=map(int,v)
    if not a:return 0.
    sign=1 if a>0 else -1;a=abs(a)
    sh=max(0,a.bit_length()-51)
    return sign*np.ldexp(float(a>>sh),e+sh)
def read(p):
    raw=Path(p).read_bytes();return json.loads(raw),hashlib.sha256(raw).hexdigest()
def main():
    p=argparse.ArgumentParser()
    for field in ('native','primary','output'):p.add_argument('--'+field,required=True)
    a=p.parse_args()
    native,nsha=read(a.native);result,rsha=read(a.primary)
    assert nsha==SHA
    assert result['pass'] in (
       'NF518-source-certified-242D-historical-D-exterior-coefficient-vector',
       'NF518-exact-original-242D-source-posterior-fit')
    assert result['original_nf505_native_SHA256']==nsha
    assert native['pass']=='NF504-native'
    assert native['original_selected_J_dimension']==N
    assert native['original_original_D_frame_SHA256']==result.get(
       'original_historical_D_frame_SHA256',result.get('original_exact_historical_D_frame_SHA256'))
    assert native['source_original_NF407_sha256']==result.get(
       'original_nf407_source_SHA256',result.get('original_source_nf407_SHA256'))
    assert native['source_original_NF406_sha256']==result.get(
       'original_nf406_seams_SHA256',result.get('original_source_nf406_SHA256'))
    g=native['original_actual_exterior_J242_D_Gram_rows_outward']
    b=native['original_actual_exterior_W_moments_D_outward']
    denominator=int(result.get('original_exact_trial_D_coordinates_denominator',
                               result.get('original_selected_D_frame_coefficients_exact_rational_denominator')))
    x=list(map(int,result.get('original_exact_trial_D_coordinates_integer_numerators',
                              result.get('original_selected_D_frame_coefficients_exact_rational_candidates_numerators'))))
    assert len(x)==N and denominator==10**105
    matrix=[];small=np.empty((N,N),dtype=object);floating=np.empty((N,N))
    for i,row in enumerate(g):
        assert len(row)==N;vals=[]
        for j,box in enumerate(row):
            assert 0<=dyad(box[1])<Q(1,S)
            vals.append(quant(box[0],S))
            small[i,j]=quant(box[0],U)
            floating[i,j]=f(box[0])
        matrix.append(vals)
    qb=[];bfee=0
    for low,high in b:
        low,high=Q(low),Q(high)
        assert low<=high
        k=floor((low+high)*S/2)
        qb.append(k)
        bfee=max(bfee,ceil(k-low*S),ceil(high*S-k))
    rmax=max(abs(sum(matrix[i][j]*x[j] for j in range(N))-qb[i]*denominator)
             for i in range(N))
    residual=Q(rmax,S*denominator)+Q(2*sum(map(abs,x)),S*denominator)+Q(bfee,S)
    invf=np.linalg.inv(floating)
    inv=np.empty((N,N),dtype=object)
    for i in range(N):
        for j in range(N):
            inv[i,j]=floor(Q.from_float(float(invf[i,j]))*V+Q(1,2))
    product=small@inv
    matrix_fee=max(sum(abs((U*V if i==j else 0)-product[i,j])
                       for j in range(N)) for i in range(N))
    rowbound=max(sum(abs(v) for v in inv[i,:]) for i in range(N))
    epsnum=matrix_fee+2*N*rowbound;epsden=U*V
    assert epsnum<epsden
    inverse=Q(rowbound*U,epsden-epsnum)
    assert inverse<Q(9*10**9)
    coefferr=inverse*residual
    assert coefferr<Q(2,10**84)
    assert Q(result.get('original_source_coefficient_error_exact_upper',
                        result.get('original_each_selected_D_frame_coefficient_error_strict_upper')))<Q(2,10**84)
    Gram_abs=Q(sum(abs(t) for row in matrix for t in row)+2*N*N,S)
    assert Gram_abs<Q(443)
    assert Gram_abs*coefferr**2<Q(5,10**83)**2
    rhi=Q(native['original_original_saturated_exterior_residual_outward'][1])
    assert 0<rhi<Q(13,10**12)**2
    assert 2*Q(13,10**12)*Q(5,10**83)+Q(5,10**83)**2<Q(2,10**93)
    out={
       'pass':'NF518-independent-original-242D-alternate-source-inverse-posterior',
       'original_NF505_source_SHA256':nsha,'original_primary_certificate_SHA256':rsha,
       'independent_original_source_G_d_quantization_scale':str(S),
       'independent_inverse_source_G_scale':str(U),
       'independent_inverse_trial_scale':str(V),
       'independent_source_exact_inverse_Neumann_upper':str(Q(epsnum,epsden)),
       'independent_source_exact_inverse_infinity_norm_upper':str(inverse),
       'independent_original_Galerkin_normal_residual_upper':str(residual),
       'independent_every_original_D_coordinate_error_upper':str(coefferr),
       'independent_every_original_D_coefficient_error_lt_2e_minus_84':True,
       'independent_selected_physical_exterior_L2_fit_error_lt_5e_minus_83':True,
       'independent_any_original_physical_D_residual_squared_coeff_error_lt_2e_minus_93':True,
       'original_historical_D_raw_frame_matrix_recomputed':False,
       'original_complete_J242_named_cell_e_D':'OPEN',
       'original_Fredholm_kernel_gap':'OPEN',
       'original_NF404_named_support_gate':'OPEN',
       'original_Weil_image_graph_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN'}
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
    print('NF518 INDEPENDENT exact original source 242D a posteriori PASS')
    print('Every historical D coordinate error <2e-84; any cell squared e uncertainty from fit coefficients <2e-93')
    print('Source local e_D / spectral gap / NF404 / Weil source domain / RH OPEN')
if __name__=='__main__':main()
