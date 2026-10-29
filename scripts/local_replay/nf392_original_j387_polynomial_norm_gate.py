#!/usr/bin/env python3
"""NF392: tighter EXACT original j387 physical L2 norm using polynomial integration.

This is an original source-only necessary candidate-moment stop sensitivity,
NOT an actual selected signed moment, NOT a spectral lowband upper and NOT RH.
Optionally consume authentic NF390 native selected moment using parent's exact
two-shadow gate, with actual result never silently invented.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
import nf391_original_orthogonal_lowband_moment_gate as parent
sys.set_int_max_str_digits(0)

B=F(11,10)
ALPHA=F(-88873,2**48)
SQRT_POLY_BOUND=F(1311,10)
THRESHOLD=F(131,10**22) # 1.31e-20
PREVIOUS_CEILING=F(181,10**22) # 1.81e-20, NF391
R0=F(2673,10**16)

def evaluate(native512,nf375,j387,native390=None,output=None):
    earlier=parent.run(native512,nf375,j387,native390=native390)
    frozen=parent.read(j387,git_sha=parent.GIT_J387)
    gate=parent.read(nf375,git_sha=parent.GIT_NF375)
    assert frozen['scalar_alpha']==str(ALPHA)
    assert frozen['candidate_formula'].startswith('alpha*(121-100*x^2)')
    assert frozen['nonzero_raw_source_indices']==[0,2]
    assert frozen['endpoint_value_exact']=='0'
    # h=alpha(121-100 x^2)sin(2*pi*(37/64)x), physical support [-B,B].
    # |sin|<=1, hence norm^2<=alpha^2 integral (121-100x²)^2 dx.
    poly_integral=2*(F(121**2)*B
       -F(2*121*100)*B**3/3+F(10000)*B**5/5)
    assert poly_integral==F(1288408,75)
    assert (100*B*B)==121
    assert SQRT_POLY_BOUND**2>poly_integral
    norm_upper=abs(ALPHA)*SQRT_POLY_BOUND
    old_norm_upper=abs(ALPHA)*F(363,2)
    assert norm_upper<old_norm_upper
    cutoff=gate['directions'][3]['dyadic_cutoff_options']
    x=[v for v in cutoff if v['log2_cutoff']==24]
    assert len(x)==1 and x[0]['cutoff']==2**24
    assert x[0]['exact_squared_original_individual_gate'] is True
    H=F(x[0]['highband_upper'])
    tau=F(x[0]['chosen_future_lowband_target'])
    assert tau==F(7,25*10**12)
    assert F(earlier['remaining_selected_shadow_norm_upper_sufficient_for_stop'])==R0
    assert F(earlier['certified_n512_orthogonal_lowband_norm_strictly_greater_than'])==F(834,10**16)
    assert F(834,10**16)**2+R0**2>tau**2
    threshold=(H+R0)*norm_upper
    assert threshold<THRESHOLD<PREVIOUS_CEILING
    out={
       'standing':'NF392 ORIGINAL J387 POLYNOMIAL-INTEGRAL L2 NORM CERTIFICATE AND IMPROVED CONDITIONAL SELECTED MOMENT STOP; NATIVE STATUS SEPARATE',
       'original_j387_git_blob_sha1':parent.GIT_J387,
       'original_nf375_git_blob_sha1':parent.GIT_NF375,
       'original_n512_sha256':parent.SHA512,
       'fixed_physical_halfwidth':str(B),
       'actual_j387_dyadic_alpha':str(ALPHA),
       'original_polynomial_squared_integral_exact':str(poly_integral),
       'polynomial_squared_integral_sqrt_strict_upper':str(SQRT_POLY_BOUND),
       'actual_original_j387_L2_norm_strict_upper':str(norm_upper),
       'previous_NF391_j387_L2_norm_strict_upper':str(old_norm_upper),
       'actual_original_fourth_NF375_highband_upper':str(H),
       'original_nf375_lowband_future_target':str(tau),
       'original_n512_orthogonal_lowband_norm_strict_lower':'834/10000000000000000',
       'remaining_selected_moment_norm_required_for_joint_stop':str(R0),
       'new_original_j387_absolute_moment_discrepancy_stop_strict_ceiling':str(threshold),
       'new_original_j387_absolute_moment_discrepancy_safe_rational_ceiling':str(THRESHOLD),
       'previous_NF391_coarse_discrepancy_sufficient_ceiling':str(PREVIOUS_CEILING),
       'if_original_pole_corrected_selected_moment_abs_discrepancy_gt_1_31e_20_then_fixed_j387_fails':True,
       'original_nf390_native_selected_moment_result_supplied':native390 is not None,
       'original_nf390_native_selected_moment_outcome':earlier['nf390_native_selected_moment_result'],
       'fixed_j387_specific_candidate_stop':earlier['nf387_specific_candidate_joint_method_stopped'],
       'fixed_j387_candidate_verdict': ('PENDING' if native390 is None else
             'STOP' if earlier['nf387_specific_candidate_joint_method_stopped'] else 'INCONCLUSIVE'),
       'actual_original_lowband_signed_integral_computed':False,
       'actual_original_full_lowband_upper_computed':False,
       'full_original_exterior_inverse_computed':False,
       'original_operator_domain_review':'OPEN',
       'W_ODD_NEG':'OPEN','RH':'OPEN'}
    if native390:
        n=parent.read(native390)
        assert n['pole_restored_for_selected_test'] is True
        assert n['fresh_original_signed_kernel_cells']==0
        out['native_pole_corrected_selected_discrepancy_interval']=n['actual_selected_moment_discrepancy_interval']
        out['native_physical_j387_norm_squared_interval']=n['original_j387_physical_norm_squared_interval']
    if output:
        p=Path(output);p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(json.dumps(out,indent=2)+'\n')
    print('NF392 exact original polynomial² norm integral:',poly_integral)
    print('NF392 source-only candidate strict moment ceiling <',THRESHOLD)
    print('NF392 native original selected moment:',earlier['nf390_native_selected_moment_result'])
    print('NF392 full lowband upper and W-ODD-NEG/RH OPEN')
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--original-512',required=True)
    p.add_argument('--nf375',required=True)
    p.add_argument('--j387',required=True)
    p.add_argument('--native390')
    p.add_argument('--output')
    a=p.parse_args()
    evaluate(a.original_512,a.nf375,a.j387,a.native390,a.output)
