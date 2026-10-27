#!/usr/bin/env python3
"""Exact replay of all retained coefficients, moments and joint kernel error."""
import json,sys
from fractions import Fraction as F
from math import factorial

def replay(z):
    assert z['status']=='CONDITIONAL_ORIGINAL_COMPLETE_ARCH_KERNEL_COMPRESSION_ERROR'
    assert z['frame_input_sha256']=='87d6f3ae24cde489adaf9ab3ac7efa612bc82bd78c6c9e94866802fdc550052f'
    assert z['accepted_source_transform_sha256']=='37c01971e3f63843cc15454172a46cad9079b6b64705e24cd9bb1bb4287c73e0'
    c=list(map(F,z['exact_regular_kernel_coefficients']));N=len(c)-1
    assert N==z['degree']==384
    # Replay using exponential identity, not the builder's sinh division.
    for n in range(N+1):
        assert sum((F(2**j,factorial(j+1))*c[n-j] for j in range(n+1)),F(0))==F(3,2)**n/factorial(n)
    check=z['Cauchy_bound_checks']
    slo=sum((F((-1)**j*3**(2*j+1),factorial(2*j+1)) for j in range(12)),F(0))
    eu=sum((F(3,2)**j/factorial(j) for j in range(25)),F(0))+F(3,2)**25/factorial(25)/(1-F(3,52))
    assert F(check['sin_3_lower'])==slo>F(7,50)
    assert F(check['exp_3_over_2_upper'])==eu<F(9,2)
    assert 3*eu/slo<128 and check['circle_radius']=='3' and check['circle_modulus_upper']=='128'
    L=F(11,5);q=L/3;d=[v*L**n for n,v in enumerate(c)]
    ms=list(map(F,z['scalar_moment_centers']));es=list(map(F,z['scalar_moment_error_uppers']))
    assert len(ms)==len(es)==128
    for j,(m,e) in enumerate(zip(ms,es),1):
        assert m==sum((v/F(j+n) for n,v in enumerate(d)),F(0))
        assert e==128*q**(N+1)/((1-q)*(N+j+1)) and m>e>0
    error=F(101,100)*128*q**(N+1)/((1-q)*(N+1))
    assert F(z['complete_normalized_mixed_kernel_replacement_error_upper'])==error<F(1,2**170)
    assert F(z['clean_complete_kernel_replacement_error_upper'])==F(1,2**170)
    for key in ('original_source_polynomial_approximation_certified','original_source_polynomial_degree_or_cost_certified','original_arch_mixed_matrix_computed','matched_forcing_computed','inverse_response_value_certified'):
        assert z[key] is False
    assert z['W_ODD_NEG']=='OPEN' and z['inherited_original_domain_review']=='OPEN'
    print('EXACT REPLAY PASS: 385 coefficients, 128 scalar moments, full JD/W kernel error <2^-170; original matrix OPEN')
if __name__=='__main__':replay(json.load(open(sys.argv[1])))
