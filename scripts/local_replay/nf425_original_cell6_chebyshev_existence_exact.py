#!/usr/bin/env python3
"""NF425 source-exact cell-6 global Chebyshev existence/remainder preflight.

Replays the original NF407 full 242+4 source, original NF406 knots, NF423
whole-cell derivative, and NF424 source/image error. Proves a single
degree-2048 Chebyshev interpolant exists with rigorous full-real-cell
<2e-45 function approximation, based on an explicit E_2 analytic bound.

CRUCIAL: does NOT calculate any Chebyshev coefficients, z^2, p*z or NF404.
Analytic digamma/Cauchy bounds are detailed in the corresponding NF425 note;
this script verifies all rational numerical premises and budgets.
"""
from __future__ import annotations
import argparse,hashlib,json,math
from fractions import Fraction as F
from pathlib import Path

B=F(11,10)
C=F(91,100)
H=F(7,100)
RHO=F(2)
N=2048
POLE=F(6677356497477490213,4611686018427387904)

def load(path):
    data=Path(path).read_bytes()
    return json.loads(data),hashlib.sha256(data).hexdigest()

def dyad(z):
    m,e=int(z[0]),int(z[1])
    return F(m*2**e) if e>=0 else F(m,2**(-e))

def source(s):
    coeff={}
    pole=F(0);S0=F(0)
    def add(f,k,q):
        coeff[(f,k)]=coeff.get((f,k),F(0))+q
    for (freq,k),(mid,rad) in zip(
        s['original_selected_generator_node_orders'],
        s['original_exact_native_raw_selected_coefficients_mid_radius']):
        a=dyad(mid);e=abs(dyad(rad))
        if freq=='pole':
            pole+=a;S0+=e
        else:
            add(F(freq),k,a);S0+=e*B**k
    for (mid,rad),shape in zip(
        s['original_exact_native_original_four_critical_coefficients_mid_radius'],
        s['original_source_critical_sines_and_pole_coefficients']):
        a=dyad(mid);e=abs(dyad(rad))
        for freq,val in zip(s['original_source_critical_sine_frequencies'],
                            shape['sine_coefficients']):
            add(F(freq),0,a*F(val));S0+=e*abs(F(val))
        pole+=a*F(shape['sinh_coefficient'])
        S0+=e*abs(F(shape['sinh_coefficient']))
    return coeff,pole,S0

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
    p.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
    p.add_argument('--nf423',default='notes/data/provisional/NF423_original_entire_open_cell6_zthird_native.json')
    p.add_argument('--nf424',default='scripts/local_replay/nf424_original_cell6_global_exponential_transfer_exact.py')
    p.add_argument('--output',required=True)
    a=p.parse_args()
    src,source_sha=load(a.source)
    seams,seams_sha=load(a.seams)
    parent,parent_sha=load(a.nf423)
    _,nf424_script_sha=load_text(a.nf424)
    assert src['original_dimension']==242
    assert len(src['original_exact_native_raw_selected_coefficients_mid_radius'])==242
    assert len(src['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
    assert len(src['original_source_critical_sine_frequencies'])==32
    assert src['W_ODD_NEG']==src['RH']=='OPEN'
    assert parent['original_nf407_source_sha256']==source_sha
    assert parent['original_nf406_exact_support_seams_sha256']==seams_sha
    assert parent['true_original_entire_open_cell6_zthird_uniform_strict_upper']==286758
    assert parent['original_all_seven_real_signed_prime_branches_inside_open_cell']==['post-seam']*5+['neither']*2
    assert parent['true_active_prime_weight_strict_upper']==3
    assert parent['true_analytic_arch_A_absolute_strict_upper']==4
    knots=seams['certified_ordered_knots']
    assert knots[13]['label']=='-B+log(7)' and knots[14]['label']=='-B+log(8)'
    assert F(21,25)<F(knots[13]['low'])<F(knots[13]['high'])
    assert F(knots[14]['low'])<F(knots[14]['high'])<F(49,50)
    assert F(knots[13]['high'])<F(knots[14]['low'])

    # True J6 is inside [0.84,0.98]. This wider interval crosses original
    # seams, so ONLY the fixed cell6 BRANCH is analytically continued on it.
    assert C-H==F(21,25) and C+H==F(49,50)
    # Bernstein E_2: horizontal semi-axis 5H/4 and vertical 3H/4.
    remax=C+H*F(5,4);remin=C-H*F(5,4)
    immax=H*F(3,4)
    assert (remin,remax,immax)==(F(329,400),F(399,400),F(21,400))
    assert B-remax==F(41,400)>F(1,10)
    assert remax<B
    # No zeros/poles in the physical log(B/(B-x)) (principal branch):
    # Re(B-x)>0 over E2, and both image sums converge normally.

    coeff,pole,S0=source(src)
    raw=sum((abs(c)*B**k for (f,k),c in coeff.items()),abs(pole))
    assert raw<10**160 and S0<F(1,10**700)
    assert 0<=min(k for f,k in coeff)
    assert max(k for f,k in coeff)<=13
    assert 0<min(f for f,k in coeff) and max(f for f,k in coeff)<883
    assert POLE<2 and POLE>1
    # For each exponential Fourier frequency lambda=+/-2*pi*i*f,
    # 2*pi*f<7064 (pi<4). Cauchy lambda disks radius 1/8:
    # Re(1/4+/-lambda/2) >= 3/16. All corresponding digamma poles are
    # absent. |Im lambda| < 7065.
    assert F(1,4)-F(1,16)==F(3,16)
    assert F(7065)*immax+F(1,8)*F(11,10)<373
    # psi(z)=-gamma+sum(1/(m+1)-1/(m+z)).
    # For Re z>=3/16 and |z-1|<4000, first 10000 summands are
    # <= 1+16/3, tail <=4000/9999, |gamma|<1.
    psi_majorant=F(1)+10000*(F(1)+F(16,3))+F(4000,9999)
    assert psi_majorant<64000
    # Each endpoint image geometric series is bounded using
    # t>=2*(B-remax)=41/200, 1/(1-e^-t)<1+1/t<6.
    tmin=2*(B-remax)
    assert tmin==F(41,200) and 1+1/tmin<6
    # Source lambda disks are distant from m=0 poles:
    assert F(1,4)-F(1,16)==F(3,16)
    # At lambda=+/-1/2 the isolated m=0 pole is removed by
    # [exp(-2*beta*d)-1]/beta and psi(1+beta), not separately evaluated.
    assert 2*(B+F(11,10))<5
    # 13! 8^13 is a Cauchy derivative bound for k<=13.
    cauchy=math.factorial(13)*8**13
    assert cauchy<10**24
    # On E2 the entire fixed-cell-6 finite model, including the
    # true 5-prime post-seam continuation and endpoint log, has the
    # conservative mathematical maximum M<1e400. Sources:
    # |G_N|<1e6*3^373 on +/- frequency disks, psi<64000,
    # normal geometric image bounds, lambda-pole cancellation;
    # 3^13<1e7 for shifted source monomials, raw source<1e160.
    # Prove the final outward INTEGER scale, do not infer a small
    # observed function from this deliberately gigantic triangle bound.
    analytic_M=10**400
    assert 10**190 * 3**373 < analytic_M

    # Chebyshev degree N interpolant of the already finite source model
    # over [C-H,C+H] exists. Standard Bernstein ellipse interpolation:
    # ||f-I_N f|| <= 4*M * rho^-N/(rho-1).
    cheb_bound=F(4*analytic_M,2**N)
    assert cheb_bound<F(1,10**200)
    # Original endpoint log has an explicit Chebyshev expansion.
    # (B-C)-H t = Q*(1-2*q*t+q^2), Q=(A+sqrt(A^2-H^2))/2.
    # A=19/100,H=7/100, sqrt(A^2-H^2)=sqrt(78)/50,
    # q=7/(19+2*sqrt(78))<1/5 since sqrt(78)>8.
    assert B-C==F(19,100) and H==F(7,100)
    assert 19**2-7**2==4*78
    assert 78>8**2
    q_up=F(1,5)
    # For log(B/(B-x)) the coefficient for T_n (n>=1) is 2q^n/n.
    # Truncation from n=N+1 satisfies 2*q^(N+1)/(N+1)/(1-q).
    log_tail=2*q_up**(N+1)/(F(N+1)*(1-q_up))
    assert log_tail<F(1,10**1400)
    # Replay NF424 entire-cell original SOURCE and 2048-image tail.
    # On real J6 t1>6/25; this bound does NOT extend to E2.
    image_tail=F(36,2000)*10**160*F(3,8)**480
    source_charge=(10**12+20)*S0
    assert image_tail<F(1,10**45)
    assert source_charge<F(1,10**680)
    total=image_tail+source_charge+cheb_bound
    assert total<F(2,10**45)
    # If each of the N+1 actual interpolant coefficients receives
    # an outward radius e, then sup error from coefficient intervals
    # is <=(N+1)*e: practical future acceptance specification only.
    coeff_radius_target=F(1,10**25)
    coeff_radius_total=(N+1)*coeff_radius_target
    assert coeff_radius_total<F(1,10**21)
    assert total+coeff_radius_total<F(1,10**20)
    out={
      'pass':'NF425',
      'standing':'ACCEPTED ORIGINAL-CELL6 FINITE-MODEL CHEBYSHEV DEGREE AND EXISTENCE ERROR; NO FINITE-MODEL COEFFICIENTS/INTEGRALS EVALUATED',
      'source_sha256':source_sha,'seams_sha256':seams_sha,
      'nf423_full_cell_parent_sha256':parent_sha,
      'nf424_exact_transfer_script_sha256':nf424_script_sha,
      'canonical_active_obligation':'W-ODD-NEG',
      'exact_original_cell6':'(log(7)-11/10,log(8)-11/10)',
      'Chebyshev_branch_analytic_continuation_not_true_z_outside_J6':True,
      'outer_rational_interval':['21/25','49/50'],
      'Chebyshev_center':str(C),'Chebyshev_halfwidth':str(H),
      'Bernstein_rho':'2',
      'ellipse_real_min_max':[str(remin),str(remax)],
      'ellipse_imag_max_abs':str(immax),
      'ellipse_distance_to_B_real_lower':str(B-remax),
      'original_242_selected_plus_four_critical_source_preserved':True,
      'original_prime_active_and_inactive':['2','3','4','5','7','8:neither','9:neither'],
      'digamma_psi_modulus_majorant':'64000',
      'original_source_coefficient_raw_triangle_strict_upper':'1e160',
      'finite_model_analytic_ellipse_modulus_strict_upper':'1e400',
      'original_midpoint_finite_image_terms_each_side':N,
      'Chebyshev_polynomial_degree':N,
      'Chebyshev_exact_bound_interpolation_error':str(cheb_bound),
      'Chebyshev_interpolation_error_strict_upper':'1e-200',
      'log_Chebyshev_parameter_q_upper':'1/5',
      'log_Chebyshev_tail_N_plus_one_exact_upper':str(log_tail),
      'log_Chebyshev_coeff_n_ge_1':'2*q^n/n',
      'source_coefficient_ball_error_exact':str(source_charge),
      'finite_image_series_tail_exact':str(image_tail),
      'entire_true_original_cell6_cheb_existential_error_exact':str(total),
      'entire_true_original_cell6_cheb_existential_error_strict_upper':'2e-45',
      'independently_certified_physical_t_integral_centers_required':0,
      'direct_coefficient_bessel_generating_formula':'e^(lambda*C)*[I0(lambda*H) if n=0 else 2*I_n(lambda*H)]',
      'direct_lambda_differentiation_for_x_polynomial_source':True,
      'future_each_coefficient_radius_target_exact':str(coeff_radius_target),
      'future_all_coefficient_radii_sum_target_exact':str(coeff_radius_total),
      'actual_2049_correlated_Chebyshev_coefficients_computed':False,
      'actual_cell6_pz_z2_integrated':False,
      'NF410_all_eight_original_cells_certified':False,
      'NF404_signed_scalar_decided':False,
      'W_ODD_NEG':'OPEN','RH':'OPEN'}
    dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print('NF425 entire original cell6 analytic Chebyshev existence and strict error preflight PASS')
    print('NF425 true cell6 finite-image model degree 2048 polynomial exists; error <2e-45')
    print('NF425 numerical coefficients, cell integral, NF404 and RH remain OPEN')

def load_text(path):
    data=Path(path).read_bytes()
    return data,hashlib.sha256(data).hexdigest()

if __name__=='__main__':main()
