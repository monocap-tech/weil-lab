#!/usr/bin/env python3
"""NF518: independently certified original 242D selected Galerkin coefficients.

SHA-pinned original NF505 4096-bit source N_O,d_O in historical D frame.
All ACCEPTANCE inequalities are exact BIG INTEGER / Fraction. NumPy's
binary64 inverse/solve is *only* the trial/preconditioner; exact residuals
and a Neumann posterior certify the true source vector. No original raw
D 242x242 columns, cell residual e_H or kernel gap claimed.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
N=242;S=10**120;T=10**105;U=10**70;V=10**35
SHA='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAM='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
FRAME='18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e'
def down(z):return z.numerator//z.denominator
def up(z):return -down(-z)
def dyad(z):
    a,e=map(int,z)
    return Q(a<<e) if e>=0 else Q(a,1<<(-e))
def fdyad(z,scale):
    a,e=map(int,z)
    return (a*scale)<<e if e>=0 else (a*scale)//(1<<(-e))
def approx(z):
    a,e=map(int,z)
    if not a:return 0.
    sign=1 if a>0 else -1;a=abs(a)
    sh=max(0,a.bit_length()-50)
    return sign*np.ldexp(float(a>>sh),e+sh)
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--native',required=True)
    p.add_argument('--output',required=True)
    z=p.parse_args()
    raw=Path(z.native).read_bytes();sha=hashlib.sha256(raw).hexdigest()
    assert sha==SHA
    native=json.loads(raw)
    assert native['pass']=='NF504-native'
    assert native['original_selected_J_dimension']==N
    assert native['source_original_NF407_sha256']==SRC
    assert native['source_original_NF406_sha256']==SEAM
    assert native['original_original_D_frame_SHA256']==FRAME
    assert native['original_support_saturated_physical_Hilbert_gate']=='CERTIFIED_PHYSICAL_SUPPORT_NO_GO'
    entries=native['original_actual_exterior_J242_D_Gram_rows_outward']
    moments=native['original_actual_exterior_W_moments_D_outward']
    assert len(entries)==len(moments)==N
    M=[];Msmall=np.empty((N,N),dtype=object);Mf=np.empty((N,N))
    for i,row in enumerate(entries):
        assert len(row)==N
        arr=[]
        for j,(mid,rad) in enumerate(row):
            assert 0<=dyad(rad)<Q(1,S)
            arr.append(fdyad(mid,S))
            Msmall[i,j]=fdyad(mid,U)
            Mf[i,j]=approx(mid)
        M.append(arr)
    b=[];bfee=0
    for lo,hi in moments:
        lo,hi=Q(lo),Q(hi)
        assert lo<=hi
        k=down((lo+hi)*S/2)
        b.append(k)
        bfee=max(bfee,up(k-lo*S),up(hi*S-k))
    # Independently certify inverse of the ORIGINAL source Gram:
    # B is a binary64 candidate with 1e35 integer quantization. The
    # acceptance uses exact integer 242x242 Msmall@B and all source
    # interval fees, not a floating condition estimate.
    BinvF=np.linalg.inv(Mf)
    Binv=np.empty((N,N),dtype=object)
    for i in range(N):
        for j in range(N):
            Binv[i,j]=down(Q.from_float(float(BinvF[i,j]))*V+Q(1,2))
    product=Msmall@Binv
    matrix_fee=max(sum(abs((U*V if i==j else 0)-product[i,j])
                       for j in range(N)) for i in range(N))
    rowB=max(sum(abs(v) for v in Binv[i,:]) for i in range(N))
    epsnum=matrix_fee+2*N*rowB;epsden=U*V
    assert epsnum<epsden
    inverse=Q(rowB*U,epsden-epsnum)
    assert inverse<Q(9*10**9)
    # Fixed-point exact iterative refinement of an arbitrary binary64
    # candidate. The correction vector is computed with BIG INTEGER
    # matrix-vector multiplications, and only the final exact source
    # normal-equation residual is accepted.
    x0=np.linalg.solve(Mf,np.array([float(v)/S for v in b]))
    x=[down(Q.from_float(float(t))*T+Q(1,2)) for t in x0]
    iterations=0
    for k in range(30):
        residual=[b[i]*T-sum(M[i][j]*x[j] for j in range(N))
                  for i in range(N)]
        dx=[down(Q(sum(Binv[i,j]*residual[j] for j in range(N)),S*V)
                 +Q(1,2)) for i in range(N)]
        x=[u+v for u,v in zip(x,dx)]
        iterations+=1
        if not any(dx):break
    resmax=max(abs(sum(M[i][j]*x[j] for j in range(N))-b[i]*T)
               for i in range(N))
    # |G-M/S|<2/S per entry, source b uncertainty <=bfee/S.
    source_residual=Q(resmax,S*T)+Q(2*sum(map(abs,x)),S*T)+Q(bfee,S)
    coeff_error=inverse*source_residual
    assert coeff_error<Q(2,10**84)
    # Physical L2(O) source fit error WITHOUT realizing huge raw D:
    # ||J_D delta a||²_O = delta a^T N_O delta a
    #                       <= ||delta a||_inf² sum_ij |N_Oij|.
    absolute_Gram=Q(sum(abs(t) for row in M for t in row)+2*N*N,S)
    assert absolute_Gram<Q(443)
    fitted_error=Q(5,10**83)
    assert absolute_Gram*coeff_error**2<fitted_error**2
    old_Rhi=Q(native['original_original_saturated_exterior_residual_outward'][1])
    assert 0<old_Rhi<Q(13,10**12)**2
    # Any D subset O: ||rtrial||²_D−||rtrue||²_D bounded by
    # 2||rtrue||_O||p-ptrial||_O + ||p-ptrial||²_O.
    any_cell_sq_error=2*Q(13,10**12)*fitted_error+fitted_error**2
    assert any_cell_sq_error<Q(2,10**93)
    out={
      'pass':'NF518-exact-original-242D-source-posterior-fit',
      'standing':'SOURCE-CERTIFIED all 242 historical D Galerkin coordinates; ANY physical D squared residual coefficient-error <2e-93; true local e_D and kernel gap OPEN',
      'original_nf505_native_SHA256':sha,
      'original_nf407_source_SHA256':SRC,'original_nf406_seams_SHA256':SEAM,
      'original_historical_D_frame_SHA256':FRAME,
      'original_selected_dimension':N,
      'source_input_fixed_scale':str(S),'trial_vector_integer_denominator':str(T),
      'source_independent_inverse_input_scale':str(U),
      'source_inverse_trial_integer_denominator':str(V),
      'inverse_Neumann_eps_exact_upper':str(Q(epsnum,epsden)),
      'inverse_infinity_norm_exact_upper':str(inverse),
      'original_source_normal_equation_residual_exact_upper':str(source_residual),
      'original_source_coefficient_error_exact_upper':str(coeff_error),
      'source_coefficient_error_strict_lt_2e_minus_84':True,
      'source_original_selected_Gram_sum_abs_entries_lt_443':True,
      'source_selected_fitted_physical_L2_O_error_strict_lt_5e_minus_83':True,
      'any_original_physical_D_subset_O_squared_residual_coeff_uncertainty_lt_2e_minus_93':True,
      'original_exact_trial_D_coordinates_integer_numerators':[str(t) for t in x],
      'original_exact_trial_D_coordinates_denominator':str(T),
      'exact_fixed_point_refinement_iterations':iterations,
      'original_D_raw_coefficient_matrix_reconstructed':False,
      'source_original_complete_J242_locally_fitted_eD':'OPEN',
      'source_original_local_kernel_gap':'OPEN',
      'original_NF404_named_patch':'OPEN',
      'original_Weil_multiplier_image_graph_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    Path(z.output).write_text(json.dumps(out,indent=2)+'\n')
    print('NF518 SOURCE CERTIFIED 242D original fit a_O: error <2e-84, L2(O) fit error <5e-83')
    print('NF518 ANY physical subset D squared residual coefficient-only uncertainty <2e-93')
    print('Original local e_D, kernel gap, NF404 patch, source image and RH OPEN')
if __name__=='__main__':main()
