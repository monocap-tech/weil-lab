"""RC140: certified endpoint probe tightens the upper inverse residual."""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json
from validate_rpb108_rc127_enriched_even_endpoint_action import down, up, sqrtup
from validate_rpb108_rc139_two_sided_variational_response import run as rc139_run


def run(paths, replay=False):
    raw = [Path(p).read_bytes() for p in paths]
    prior = json.loads(raw[0])
    assert prior == rc139_run(paths[1:], replay)
    previous = json.loads(raw[1]); joint = json.loads(raw[3])
    assert (prior['milestone'], previous['milestone'], joint['milestone']) == ('RC139', 'RC138', 'RC136')
    trial = next(t for t in prior['rational_trials'] if t['name'] == 'upper_optimized')
    c = [F(x) for x in trial['coefficients']]
    S = [[F(x) for x in row] for row in previous['trial_source_matrix']]
    T = [[F(x) for x in row] for row in previous['trial_action_approximation_matrix']]
    r = [sum((S[i][j] + T[i][j])*c[j] for j in range(4)) - F(i == 0) for i in range(7)]
    # The candidate direction is fixed rational, chosen outside the acceptance calculation.
    k = F('5.711278414')
    s = [F(0)]*7
    s[0] = 1
    s[2] = -k
    HL = [[F(x) for x in row] for row in joint['actual_endpoint_pairing_entry_lower']]
    HU = [[F(x) for x in row] for row in joint['actual_endpoint_pairing_entry_upper']]
    order = [(i,j) for i in range(7) for j in range(7)]
    if replay: order.reverse()
    def bil(x,y):
        lo = hi = F(0)
        for i,j in order:
            v=x[i]*y[j]
            lo+=v*(HL[i][j] if v>=0 else HU[i][j])
            hi+=v*(HU[i][j] if v>=0 else HL[i][j])
        return lo,hi
    nominal_lo,nominal_hi=bil(r,s)
    source_lo,source_hi=bil(s,s)
    assert 0<source_lo<=source_hi and 0<nominal_lo<=nominal_hi
    action_error=F(trial['full_action_error_D_norm_upper'])
    # C^2 <= C bounds ||Cs|| by sqrt(H(s,s)); pay action error in C pairing.
    pairing_error=up(action_error*sqrtup(source_hi))
    true_pairing_lower=down(nominal_lo-pairing_error)
    assert true_pairing_lower>0
    # Cauchy in the positive C form gives H(r,r) >= H(r,s)^2/H(s,s).
    residual_endpoint_lower=down(true_pairing_lower**2/source_hi,10**100)
    assert residual_endpoint_lower>0
    # Scalar 1/(1+lambda) <= 1-lambda/2, for 0<=lambda<=1.
    absolute_upper=F(trial['variational_functional_upper'])+F(trial['true_residual_D_energy_upper'])-residual_endpoint_lower/2
    G00lo=F(joint['actual_D_Gram_entry_lower'][0][0])
    normalized_upper=up(absolute_upper/G00lo,10**15)
    old_upper=F(prior['normalized_P0_reference_response_upper'])
    old_lower=F(prior['normalized_P0_reference_response_lower'])
    assert old_lower<normalized_upper<old_upper
    controls=[]
    for lam in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
        gap=1-lam/2-1/(1+lam)
        assert gap==lam*(1-lam)/(2*(1+lam))>=0
        controls.append(dict(C_eigenvalue=str(lam),upper_inverse_polynomial_gap=str(gap)))
    return dict(milestone='RC140',status='PASS: positive residual endpoint probe improves the direct P0 upper response',starting_commit='53906860e45d605a7d17710b602c3e63831e2cf3',input_sha256=[hashlib.sha256(b).hexdigest() for b in raw],aperture='11/10',carrier_family_dimension=7,new_family_vectors_added=0,reference_trial='RC139 upper_optimized',endpoint_probe='P0-k*f0',probe_coefficient_k=str(k),nominal_residual_probe_endpoint_lower=str(nominal_lo),nominal_residual_probe_endpoint_upper=str(nominal_hi),probe_endpoint_energy_lower=str(source_lo),probe_endpoint_energy_upper=str(source_hi),full_action_error_D_norm_upper=str(action_error),probe_pairing_error_upper=str(pairing_error),actual_residual_probe_endpoint_pairing_lower=str(true_pairing_lower),actual_residual_endpoint_energy_lower=str(residual_endpoint_lower),residual_inverse_upper_spectral_inequality='(I+C)^-1 <= I-C/2 for 0<=C<=I',normalized_P0_reference_response_lower=str(old_lower),normalized_P0_reference_response_upper=str(normalized_upper),normalized_P0_reference_response_interval_width=str(normalized_upper-old_lower),RC139_normalized_upper=str(old_upper),RC139_width=str(old_upper-old_lower),upper_endpoint_improvement=str(old_upper-normalized_upper),scalar_spectral_controls=controls,full_action_error_paid_before_endpoint_projection=True,positive_C_form_Cauchy_used=True,high_accuracy_reference_inverse_completed=False,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,next_cursor='directly refine common-source and t endpoint energies; identify explicit Stage I matrix response tolerance and original-source transport requirements')


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--replay',action='store_true')
    p.add_argument('--output',required=True)
    p.add_argument('inputs',nargs=8)
    a=p.parse_args()
    result=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==result
    else:Path(a.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC140 PASS: paid residual endpoint probe')
