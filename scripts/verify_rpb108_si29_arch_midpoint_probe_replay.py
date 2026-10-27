"""Exact all-entry uncertainty replay for a shift NODE, never an integral."""
import argparse,json
from fractions import Fraction as F
from pathlib import Path
def dy(x):
    n,e=int(x[0]),int(x[1]);return F(n*2**max(e,0),2**max(-e,0))
def main():
    p=argparse.ArgumentParser();p.add_argument('certificate');a=p.parse_args()
    z=json.loads(Path(a.certificate).read_bytes())
    assert z['status']=='DIAGNOSTIC_COMPLETE_ARCH_SHIFT_NODE_NOT_INTEGRAL'
    assert z['native_input_sha256']=='c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60'
    assert z['working_precision_bits']==4096 and F(z['physical_shift'])==F(11,10)
    assert z['exact_right_endpoint']=='0' and z['exact_zero_endpoint_regularized_limit_checked'] is True
    assert (z['raw_original_source_count'],z['actual_feature_count'])==(470,14)
    A=z['raw_arch_integrand_node_balls'];assert len(A)==470 and all(len(r)==14 for r in A)
    radius2=F(0)
    for row in A:
        for mid_rad in row:
            mid,rad=map(dy,mid_rad);assert rad>=0;radius2+=rad*rad
    assert radius2==F(z['exact_raw_entry_radius_squared'])>0
    eps=F(z['coupled_raw_node_midpoint_operator_error_upper'])
    assert eps**2>=radius2>eps**2/4 and eps<F(1,10**90)
    assert z['independent_all_feature_Taylor_degree']==255
    for name in ['source_frame_D_applied','arch_integral_computed','quadrature_error_certified','matched_forcing_computed','inverse_response_value_certified']:
        assert z[name] is False
    assert z['W_ODD_NEG']=='OPEN' and z['inherited_original_domain_review']=='OPEN'
    print('EXACT COMPLETE SHIFT NODE/RADIUS REPLAY PASS; NOT AN ARCH INTEGRAL CERTIFICATE')
if __name__=='__main__':main()
