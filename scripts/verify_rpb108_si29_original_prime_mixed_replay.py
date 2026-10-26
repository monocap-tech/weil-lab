"""Exact composition check of native full-prime mixed-block ball radii."""
import argparse,json
from fractions import Fraction as F
from pathlib import Path
from validate_rpb108_si06_negative_band import ACTIVE,SHIFTS,WEIGHTS

def dy(x):
    n,e=int(x[0]),int(x[1]);return F(n*2**max(e,0),2**max(-e,0))
def interval(v):
    mid,rad=map(dy,v);assert rad>=0
    return mid-rad,mid+rad
def main():
    p=argparse.ArgumentParser();p.add_argument('certificate');args=p.parse_args()
    z=json.loads(Path(args.certificate).read_bytes())
    assert z['status']=='COMPLETE_ORIGINAL_SEVEN_PRIME_J470_W14_MIXED_BLOCK'
    assert z['native_input_sha256']=='c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60'
    assert z['working_precision_bits']==4096
    assert (z['original_J_count'],z['actual_feature_count'],z['prime_count'])==(470,14,7)
    witnesses=z['prime_witnesses']
    assert [(v['n'],v['prime_base']) for v in witnesses]==list(ACTIVE.items())
    for v in witnesses:
        n=v['n'];lo,hi=interval(v['shift_ball'])
        assert SHIFTS[n][0]<=lo<=hi<=SHIFTS[n][1]
        lo,hi=interval(v['coefficient_ball'])
        assert WEIGHTS[n][0]<=lo<=hi<=WEIGHTS[n][1]
        assert interval(v['maximum_entry_radius'])[1]<F(1,10**100)
    A=z['mixed_block_balls'];assert len(A)==470 and all(len(row)==14 for row in A)
    radius2=F(0)
    for row in A:
        for entry in row:
            interval(entry);radius2+=dy(entry[1])**2
    assert radius2==F(z['exact_Frobenius_entry_radius_squared'])>0
    eps=F(z['coupled_mixed_midpoint_operator_error_upper'])
    assert 0<eps<F(1,10**90) and eps**2>=radius2>eps**2/4
    assert eps.numerator==1 and eps.denominator&(eps.denominator-1)==0
    assert z['independent_all_continuous_feature_clipped_Taylor_degree']==255
    assert z['independent_entire_primitive_series_degree']==255
    for name in ['archimedean_mixed_computed','negative_multiplier_mixed_computed','complete_Astar_mixed_computed','energy_projection_computed','matched_forcing_computed','inverse_response_value_certified']:
        assert z[name] is False
    assert z['W_ODD_NEG']=='OPEN' and z['inherited_original_domain_review']=='OPEN'
    print('EXACT COMPLETE 470x14 PRIME BLOCK/RADIUS COMPOSITION PASS; coupled operator error <= 2^-'+str(eps.denominator.bit_length()-1))
if __name__=='__main__':main()
