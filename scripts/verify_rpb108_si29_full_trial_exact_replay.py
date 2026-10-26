"""Exact Fraction composition replay; native Gram enclosure is a separate step."""
import argparse,json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

def main():
    p=argparse.ArgumentParser();p.add_argument('certificate');args=p.parse_args()
    z=json.loads(Path(args.certificate).read_bytes())
    assert z['status']=='CONDITIONAL_ORIGINAL_FULL_484_TRIAL_PHYSICAL_PRECONDITIONER'
    assert z['native_input_sha256']=='c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60'
    assert z['working_precision_bits']==4096
    assert (z['original_source_count'],z['actual_continuous_feature_count'],z['full_trial_dimension'])==(470,14,484)
    rows=list(map(F,z['full_physical_Gram_row_error_uppers']))
    assert len(rows)==484 and min(rows)>=0 and max(rows)<F(1,100)
    assert z['physical_Gram_lower']=='99/100' and z['physical_Gram_upper']=='101/100'
    trace=F(z['full_trial_derivative_Gram_trace_upper']);endpoint=F(z['full_trial_endpoint_vector_squared_upper'])
    V=8*endpoint+F(44,10)*trace
    assert trace>0 and endpoint>0 and V==F(z['full_trial_variation_squared_upper'])
    x=F(7,10);assert sum((x**j/factorial(j) for j in range(5)),F(0))>2
    choices=[(F(101,100)*max(F(36),17+x*k)+V*(18+x*k)/(18*2**k),k) for k in range(100)]
    bound,k=min(choices);clean=(bound.numerator+bound.denominator-1)//bound.denominator
    assert k==z['chosen_log_split_dyadic_exponent'] and bound==F(z['exact_energy_upper'])
    assert clean==z['rational_Astar_trial_energy_upper'] and clean<=128
    lower=F(33621,10**9)*F(99,100)
    assert lower==F(z['conditional_Astar_trial_energy_lower'])
    assert F(clean)/lower==F(z['conditional_full_trial_energy_condition_upper'])
    for key in ['actual_Astar_matrix_entries_computed','actual_Astar_projection_computed','matched_forcing_computed','inverse_response_value_certified','energy_projected_negative_action_computed','negative_action_transfer_claimed']:
        assert z[key] is False
    assert z['W_ODD_NEG']=='OPEN' and z['inherited_original_domain_review']=='OPEN'
    print('EXACT 484D PHYSICAL/ENERGY COMPOSITION PASS',clean, str(F(clean)/lower))
if __name__=='__main__':main()
