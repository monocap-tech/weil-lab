"""RC152: paid two-column action-error envelope for the uncovered sources."""
from pathlib import Path
from fractions import Fraction as F
import argparse
import hashlib
import json

from validate_rpb108_rc127_enriched_even_endpoint_action import psd, ser
from validate_rpb108_rc129_four_vector_joint_moment import add


def run(paths):
    raw = [Path(p).read_bytes() for p in paths]
    schur, remaining, correlated = map(json.loads, raw)
    assert [x['milestone'] for x in (schur, remaining, correlated)] == ['RC151', 'RC130', 'RC134']
    assert schur['complement_sources'] == ['psi0', 'z_b6-v10']
    assert remaining['remaining_action_columns'][0] == 'Cpsi_0'
    assert correlated['correlated_difference_controls_passed']
    G = [[F(x) for x in row] for row in schur['conditional_source_Gram_lower']]
    epsilon = F(remaining['full_action_D_norm_error_upper'][0])
    delta2 = F(correlated['z_minus_v_full_source_D_energy_upper'])
    assert epsilon > 0 and delta2 > 0 and psd(G)

    # RC130 supplies a finite polynomial qpsi with ||Cpsi-qpsi||_D <= epsilon.
    # The zero polynomial is a valid trial for Cdelta: 0 <= C <= I gives
    # ||Cdelta||_D^2 <= ||delta||_D^2 <= delta2. No mixed error sign is assumed.
    # Young's inequality pays the two errors together for every mixture.
    E = [[2*epsilon*epsilon, F(0)], [F(0), 2*delta2]]
    assert psd(E)

    def dominates(n):
        return psd(add([[F(n, 10**6)*x for x in row] for row in G], E, -1))

    hi = 1
    while not dominates(hi):
        hi *= 2
        assert hi < 10**12
    lo = 0
    while hi-lo > 1:
        mid = (hi+lo)//2
        if dominates(mid): hi = mid
        else: lo = mid
    beta = F(hi, 10**6)
    assert dominates(hi) and not dominates(lo)
    witness = [F(x) for x in schur['conditional_witness_mixture']]
    quad = lambda M: sum(witness[i]*M[i][j]*witness[j] for i in range(2) for j in range(2))
    qG, qE = quad(G), quad(E)
    assert qG > 0 and qE > qG/2
    assert E[1][1] > G[1][1]/2

    return dict(
        milestone='RC152',
        status='PASS: exact action-error envelope and conditional precision audit',
        starting_commit='d25f955bbb3b7730fb497ee07ee794d3819ec127',
        input_sha256=[hashlib.sha256(b).hexdigest() for b in raw],
        aperture='11/10',
        sources=['psi0', 'z_b6-v10'],
        psi_finite_action_trial_coefficient_sha256=remaining['finite_action_trial_coefficient_sha256'],
        psi_finite_action_trial_coefficient_count=remaining['finite_action_trial_coefficient_count_per_column'],
        psi_full_action_D_norm_error_upper=str(epsilon),
        delta_zero_trial_action_D_energy_error_upper=str(delta2),
        error_envelope_Loewner_upper=ser(E),
        conditional_source_Gram_lower=ser(G),
        envelope_relative_conditional_Gram_upper=str(beta),
        psi_error_envelope_diagonal_to_conditional_Gram=str(E[0][0]/G[0][0]),
        delta_error_envelope_diagonal_to_conditional_Gram=str(E[1][1]/G[1][1]),
        witness=list(map(str, witness)),
        witness_conditional_Gram_lower=str(qG),
        witness_action_error_envelope_upper=str(qE),
        witness_envelope_to_conditional_Gram=str(qE/qG),
        half_Gram_precision_not_established_by_these_action_trials=True,
        actual_error_lower_bound_inferred=False,
        mixed_action_error_sign_assumed=False,
        full_delta_action_trial_evaluated=False,
        seven_source_inverse_response_certified=False,
        original_Weil_or_augmented_actions_performed=False,
        whole_aperture_positivity_extended=False, RH=False, F4=False, Lean=False,
        next_cursor='construct a correlated nonzero Cdelta trial and evaluate mixed action pairings; the zero trial error envelope is too large against the conditioned difference source')


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--replay', action='store_true')
    p.add_argument('--output', required=True)
    p.add_argument('inputs', nargs=3)
    a = p.parse_args()
    result = run(a.inputs)
    if a.replay:
        assert json.loads(Path(a.output).read_text()) == result
    else:
        Path(a.output).write_text(json.dumps(result, sort_keys=True, indent=2)+'\n')
    print('RC152 PASS: complementary action-error budget')
