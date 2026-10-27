#!/usr/bin/env python3
"""Replay exact degree/cost facts and the retained interval-box obstruction."""
import json,sys
from fractions import Fraction as F
from math import factorial

def dy(v):
 n,e=int(v[0]),int(v[1]);return F(n*2**max(e,0),2**max(-e,0))
def main(z):
 assert z['status']=='SCOPED_FIXED_4096_GLOBAL_MONOMIAL_IMPLEMENTATION_STOP'
 assert z['native_input_sha256']=='c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60'
 assert z['frame_input_sha256']=='87d6f3ae24cde489adaf9ab3ac7efa612bc82bd78c6c9e94866802fdc550052f'
 c=F(z['actual_source_frequency']);B=F(z['physical_half_width']);assert c==F(113013,128) and B==F(11,10)
 v2=2*B/F(99,100);assert F(z['raw_source_coefficient_norm_squared_upper'])==v2<F(9,4)
 assert z['normalized_frame_uniform_error_target']=='1/3'
 count=int((4*B*c+1)/2);assert count==z['positive_extremum_count']==1942
 assert z['total_alternating_extrema']==2*count and z['necessary_uniform_polynomial_degree']==2*count-1==3883
 assert F(2*count-1,4)/c<=B<F(2*count+1,4)/c
 t=F(z['angular_argument_rational_upper']);assert t==F(44,7)*B*c
 K=z['first_odd_degree_passing_raw_Lagrange_bound'];assert K==16643
 for degree,passes in [(K,True),(K-2,False)]:
  n=degree+1;assert (t.numerator**n*2**80 < factorial(n)*t.denominator**n)==passes
 n=(K+1)//2;assert n==z['odd_polynomial_dimension']==8322
 assert z['dense_universal_odd_Gram_entries']==n*n and z['independent_symmetric_odd_Gram_entries']==n*(n+1)//2
 assert z['tested_Taylor_coefficient_degree']==2*(int(t)//2)+1<=K
 assert z['working_precision_bits']==4096 and z['flint_version']=='0.8.0'
 assert dy(z['coefficient_radius_dyadic'])>2**4700 and z['coefficient_radius_strict_lower_power_of_two']==4700
 for key in ('normalized_trial_Taylor_remainder_certified','alternative_polynomial_representations_ruled_out','actual_arch_mixed_matrix_computed','full_coupling_route_proved_impossible','higher_precision_campaign_launched'):
  assert z[key] is False
 assert z['W_ODD_NEG']=='OPEN' and z['inherited_original_domain_review']=='OPEN'
 # Low-frequency regression for the extrema count, including endpoint peaks.
 assert int((4*F(1)*F(1)+1)/2)==2 and int((4*F(1,4)*F(1)+1)/2)==1
 print('EXACT SCOPED STOP REPLAY PASS: degree/cost/radius facts; no method-class impossibility or positivity promotion')
if __name__=='__main__':main(json.load(open(sys.argv[1])))
