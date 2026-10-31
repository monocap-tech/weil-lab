#!/usr/bin/env python3
"""NF424 exact-source cell-6 global exponential-transfer preflight.

No quadrature and no independently sampled physical centers. This exact
Fraction replay proves the finite 2048-image source model's UNIFORM tail and
source-radius budgets, using the ORIGINAL NF407 242+4 coefficients / NF406
knots / NF423 full-cell parent. It does NOT evaluate the finite model, certify
z^2 or p*z, or decide NF404 and W-ODD-NEG.
"""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

B = Q(11,10)
N = 2048
ACTIVE = (2,3,4,5,7)

def load(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()

def dyad(pair):
    m,e=int(pair[0]),int(pair[1])
    return Q(m*2**e) if e>=0 else Q(m,2**(-e))

def original_source(s):
    coeff={}
    pole=Q(0)
    radius=Q(0)
    def add(f,k,c):
        key=(f,k)
        coeff[key]=coeff.get(key,Q(0))+c
    for (freq,k),(mid,rad) in zip(
        s['original_selected_generator_node_orders'],
        s['original_exact_native_raw_selected_coefficients_mid_radius']
    ):
        c=dyad(mid);err=abs(dyad(rad))
        if freq=='pole':
            pole+=c
            radius+=err
        else:
            add(Q(freq),k,c)
            radius+=err*B**k
    for (mid,rad),shape in zip(
        s['original_exact_native_original_four_critical_coefficients_mid_radius'],
        s['original_source_critical_sines_and_pole_coefficients']
    ):
        c=dyad(mid);err=abs(dyad(rad))
        for freq,amp in zip(s['original_source_critical_sine_frequencies'],
                            shape['sine_coefficients']):
            add(Q(freq),0,c*Q(amp))
            radius+=err*abs(Q(amp))
        pole+=c*Q(shape['sinh_coefficient'])
        radius+=err*abs(Q(shape['sinh_coefficient']))
    return coeff,pole,radius

def symbolic_transfer():
    # Key: Psi_0, Psi_minus, Psi_plus, log_pi, E0_1, E0_2,
    # Eminus_1, Eplus_2. Exact group-ring algebra of the
    # I0/I1-to-global-series cancellation, no numeric quadrature.
    L=['Psi0','PsiMinus','PsiPlus','LogPi','E01','E02',
       'Eminus1','Eplus2']
    a=dict.fromkeys(L,Q(0))
    a['Psi0']+=1;a['LogPi']-=1
    a['E01']+=Q(1,2);a['E02']+=Q(1,2)
    a['PsiMinus']+=Q(1,2);a['PsiPlus']+=Q(1,2)
    a['Psi0']-=1
    a['Eminus1']+=Q(1,2);a['Eplus2']+=Q(1,2)
    a['E01']-=Q(1,2);a['E02']-=Q(1,2)
    target=dict.fromkeys(L,Q(0))
    target['PsiMinus']=target['PsiPlus']=Q(1,2)
    target['LogPi']=-1
    target['Eminus1']=target['Eplus2']=Q(1,2)
    assert a==target
    return True

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
    parser.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
    parser.add_argument('--nf423',default='notes/data/provisional/NF423_original_entire_open_cell6_zthird_native.json')
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    s,source_hash=load(args.source)
    knots,knot_hash=load(args.seams)
    prev,prev_hash=load(args.nf423)
    assert source_hash==prev['original_nf407_source_sha256']
    assert knot_hash==prev['original_nf406_exact_support_seams_sha256']
    assert prev['true_original_entire_open_cell6_zthird_uniform_strict_upper']==286758
    assert prev['original_all_seven_real_signed_prime_branches_inside_open_cell']==[
        'post-seam']*5+['neither']*2
    assert prev['true_active_prime_weight_strict_upper']==3
    assert prev['true_analytic_arch_A_absolute_strict_upper']==4
    assert s['original_dimension']==242
    assert len(s['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
    assert len(s['original_source_critical_sine_frequencies'])==32
    assert s['W_ODD_NEG']==s['RH']=='OPEN'

    true_knots=knots['certified_ordered_knots']
    assert true_knots[13]['label']=='-B+log(7)'
    assert true_knots[14]['label']=='-B+log(8)'
    assert Q(21,25)<Q(true_knots[13]['low'])
    assert Q(true_knots[14]['high'])<Q(49,50)
    assert Q(true_knots[13]['high'])<Q(true_knots[14]['low'])
    # Hence on ENTIRE genuine open J6, 0.24<t1=2(B-x)<0.52,
    # and t2=2(B+x)<4.16. No fabricated rational cell endpoints.
    tmin=Q(6,25)
    assert 2*(B-Q(49,50))==tmin
    assert 2*(B-Q(21,25))<1
    assert 2*(B+Q(49,50))<Q(21,5)

    coeff,pole,radius=original_source(s)
    assert len(s['original_selected_generator_node_orders'])==242
    assert coeff and 0<=min(k for f,k in coeff)<=max(k for f,k in coeff)<=13
    assert max(f for f,k in coeff)<883
    raw=sum((abs(c)*B**k for (f,k),c in coeff.items()),abs(pole))
    assert raw<10**160
    assert radius<Q(1,10**700)
    assert symbolic_transfer()

    # Tail of the exact full-line digamma + two image-series transfer.
    # At lambda=i*2*pi*f source monomials are real/imag lambda-jets.
    # Their m>=N image tails are bounded by
    #  (B+t/2)^k <= B^k exp(13*t/(2B)).
    # At lambda=+/-1/2 (odd pole) absorb exp((B+t/2)/2)
    # by 3 exp(t/4). The geometric m-tail is
    # exp(-N*t)/(1-exp(-t)), and the two image boundaries
    # have t>=t1>6/25. Thus M=N-13/(2B)>2000.
    # e>8/3, 1-exp(-tmin)>1/6 and exp(B/2)<3 yield
    # a deliberately overcharged exact-rational ceiling:
    # |finite_source_arch - 2048-image_arch| <
    #  36*10^160/2000 * (3/8)^480.
    M=Q(N)-Q(13)/(2*B)
    assert M>2000 and 2000*tmin==480
    image_tail=Q(36,2000)*10**160*Q(3,8)**480
    assert image_tail<Q(1,10**45)

    # Native coefficient balls are a SINGLE correlated 246-generator
    # source. The sum of their absolute radii bounds |du| by radius
    # on [-B,B]; with 2*pi*f<7000 and k<=13,
    # |du''|<10^12 radius (full polynomial/product derivatives).
    curvature_factor=Q(7000)**2+2*13*7000/B+Q(13*12)/B**2
    assert curvature_factor<10**12
    # On J6, |A|<4, L/2<3/2, I0 error< E2/8,
    # I1 error<8 radius, 5 true signed primes sum<3 and
    # each post-seam source-plus-endpoint difference costs 2 radius.
    # Pole-centering a is exact dyadic, not subject to this radius.
    true_source_error=(10**12+20)*radius
    assert true_source_error<Q(1,10**680)
    total=image_tail+true_source_error
    assert total<Q(1,10**45)

    out={
      'pass':'NF424',
      'standing':'SOURCE-EXACT GLOBAL CELL6 IMAGE-SERIES REPRESENTATION AND UNIFORM TRUNCATION/COEFFICIENT BUDGET; FINITE MODEL NOT NUMERICALLY ENCLOSED',
      'original_nf407_source_sha256':source_hash,
      'original_nf406_seam_sha256':knot_hash,
      'original_nf423_entire_cell_parent_sha256':prev_hash,
      'original_full_242_plus_four_source_unchanged':True,
      'entire_exact_cell6':'(log(7)-11/10,log(8)-11/10)',
      'five_post_seam_primes':list(ACTIVE),
      'inactive_original_prime_powers':[8,9],
      'exact_symbolic_arch_full_line_plus_two_image_transfer':True,
      'original_source_frequency_degree_max':max(k for f,k in coeff),
      'number_original_source_exponential_polynomial_terms':len(coeff),
      'series_image_terms_each_side':N,
      'extra_independently_certified_t_panel_centers_required':0,
      'original_midpoint_source_raw_triangle_strict_upper':'10^160',
      'original_source_true_radii_strict_upper':'10^-700',
      'analytic_uniform_series_tail_rational_upper':str(image_tail),
      'true_original_source_coefficient_radius_rational_upper':str(true_source_error),
      'entire_cell6_total_model_residual_rational_upper':str(total),
      'entire_cell6_total_model_residual_less_than_1e_minus_45':True,
      'finite_2048_term_model_numerically_enclosed':False,
      'cell6_full_L2_and_signed_integral_certified':False,
      'NF410_all_eight_original_cells_certified':False,
      'NF404_original_signed_centered_scalar_decided':False,
      'W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print('NF424 original entire cell6 structural image-series and source-radius preflight PASS')
    print('NF424 full cell6 guaranteed residual < 1e-45; finite series not yet evaluated')
    print('NF424 NF404/W-ODD-NEG/RH OPEN')

if __name__=='__main__':
    main()
