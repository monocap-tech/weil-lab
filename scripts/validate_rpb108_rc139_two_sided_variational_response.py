"""RC139: paid lower residual correction and rational trial optimization."""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json
from validate_rpb108_rc127_enriched_even_endpoint_action import down, up, sqrtup, ser
from validate_rpb108_rc129_four_vector_joint_moment import cong, mm
from validate_rpb108_rc138_reference_variational_response import run as rc138_run


def run(paths, replay=False):
    raw = [Path(p).read_bytes() for p in paths]
    previous = json.loads(raw[0])
    assert previous == rc138_run(paths[1:], replay)
    assert previous['milestone'] == 'RC138' and previous['reference_P0_inverse_interval_improved']
    joint = json.loads(raw[2])
    assert joint['milestone'] == 'RC136'
    def mat(key):
        return [[F(x) for x in row] for row in joint[key]]
    GL, GU = mat('actual_D_Gram_entry_lower'), mat('actual_D_Gram_entry_upper')
    GLo, GHi = mat('actual_D_Gram_Loewner_lower'), mat('actual_D_Gram_Loewner_upper')
    S = [[F(x) for x in row] for row in previous['trial_source_matrix']]
    T = [[F(x) for x in row] for row in previous['trial_action_approximation_matrix']]
    HL = [[F(x) for x in row] for row in previous['trial_frame_endpoint_entry_lower']]
    HU = [[F(x) for x in row] for row in previous['trial_frame_endpoint_entry_upper']]
    eps = [F(x) for x in previous['trial_action_D_norm_error_upper']]
    # Float optimization is only a proposal; each listed rational is rechecked below.
    choices = [
        ('RC138_four_reaudit', previous['candidate_reference_trials'][1]['trial_frame_coefficients']),
        ('lower_optimized', ['0.925434036459561', '-0.922015173075978', '0.829208807428684', '-0.436397951990341']),
        ('upper_optimized', ['0.925492928248732', '-0.917716767437642', '0.801150850566005', '-0.397946627540913']),
        ('balanced_optimized', ['0.925446845389304', '-0.921674493293984', '0.826527549539202', '-0.432759778567057']),
    ]
    pairs = [(i, j) for i in range(7) for j in range(7)]
    if replay:
        pairs.reverse()
        choices.reverse()
    def signed(x, y, lo, hi):
        lower = upper = F(0)
        for i, j in pairs:
            c = x[i] * y[j]
            lower += c * (lo[i][j] if c >= 0 else hi[i][j])
            upper += c * (hi[i][j] if c >= 0 else lo[i][j])
        return lower, upper
    trials = []
    for name, values in choices:
        c = [F(x) for x in values]
        assert len(c) == 4
        y = [sum(S[i][j] * c[j] for j in range(4)) for i in range(7)]
        r = [sum((S[i][j] + T[i][j]) * c[j] for j in range(4)) - F(i == 0) for i in range(7)]
        rlo = cong([[x] for x in r], GLo)[0][0]
        rhi = cong([[x] for x in r], GHi)[0][0]
        assert 0 < rlo <= rhi
        action_error = sum(abs(c[j]) * eps[j] for j in range(4))
        # The directed rational sqrt bounds are independent of the optimizer.
        nominal_lower = max(F(0), sqrtup(rlo) - F(1, 10**40))
        nominal_upper = sqrtup(rhi)
        residual_lower = max(F(0), nominal_lower - action_error)
        residual_upper = up(nominal_upper + action_error)
        residual_energy_lower = down(residual_lower**2, 10**100)
        residual_energy_upper = up(residual_upper**2, 10**100)
        assert residual_energy_lower > 0
        pL, pU = signed([F(i == 0) for i in range(7)], y, GL, GU)
        gramL = cong([[x] for x in y], GLo)[0][0]
        gramU = cong([[x] for x in y], GHi)[0][0]
        hpairs = [(i, j) for i in range(4) for j in range(4)]
        if replay: hpairs.reverse()
        hL = hU = F(0)
        for i, j in hpairs:
            v = c[i] * c[j]
            hL += v * (HL[i][j] if v >= 0 else HU[i][j])
            hU += v * (HU[i][j] if v >= 0 else HL[i][j])
        variational_lower = 2*pL - gramU - hU
        variational_upper = 2*pU - gramL - hL
        response_lower = variational_lower + residual_energy_lower/2
        response_upper = variational_upper + residual_energy_upper
        assert 0 < response_lower < response_upper
        trials.append(dict(name=name, coefficients=list(map(str, c)), nominal_residual_D_energy_lower=str(rlo), nominal_residual_D_energy_upper=str(rhi), full_action_error_D_norm_upper=str(action_error), true_residual_D_norm_lower=str(residual_lower), true_residual_D_norm_upper=str(residual_upper), true_residual_D_energy_lower=str(residual_energy_lower), true_residual_D_energy_upper=str(residual_energy_upper), variational_functional_lower=str(variational_lower), variational_functional_upper=str(variational_upper), response_lower=str(response_lower), response_upper=str(response_upper), normalized_response_lower=str(down(response_lower/GU[0][0], 10**12)), normalized_response_upper=str(up(response_upper/GL[0][0], 10**12))))
    trials.sort(key=lambda x:x['name'])
    old_lower = F(previous['normalized_P0_reference_response_lower'])
    old_upper = F(previous['normalized_P0_reference_response_upper'])
    lower = max([old_lower]+[F(t['normalized_response_lower']) for t in trials])
    upper = min([old_upper]+[F(t['normalized_response_upper']) for t in trials])
    assert old_lower < lower < upper < old_upper
    best_lower = [t['name'] for t in trials if F(t['normalized_response_lower']) == lower]
    best_upper = [t['name'] for t in trials if F(t['normalized_response_upper']) == upper]
    # For any spectral A eigenvalue in [1,2], A^-1 >= 1/2 and <= 1.
    controls = []
    for lam in (F(0), F(1,4), F(1,2), F(1)):
        for z in (F(0), F(1,3), F(-2,5)):
            exact = 1/(1+lam)
            L = 2*z - (1+lam)*z*z
            rr = ((1+lam)*z-1)**2
            assert L+rr/2 <= exact <= L+rr
            controls.append(dict(C_eigenvalue=str(lam), signed_trial=str(z), two_sided_identity_verified=True))
    return dict(milestone='RC139', status='PASS: paid two-sided residual variational correction narrows direct P0 inverse interval', starting_commit='5c368d73a5e640092db7ef6285b126abd58fc826', input_sha256=[hashlib.sha256(b).hexdigest() for b in raw], carrier_family_dimension=7, new_family_vectors_added=0, rational_trials=trials, normalized_P0_reference_response_lower=str(lower), normalized_P0_reference_response_upper=str(upper), normalized_P0_reference_response_interval_width=str(upper-lower), RC138_interval_width=str(old_upper-old_lower), previous_width_over_new_width_lower=str(down((old_upper-old_lower)/(upper-lower), 10**6)), selected_lower_trial=best_lower, selected_upper_trial=best_upper, lower_residual_correction_certified=True, all_accepted_residual_energies_lower_positive=True, full_action_error_paid_before_both_residual_norm_bounds=True, actual_Gram_and_endpoint_enclosures_used=True, scalar_controls=controls, high_accuracy_reference_inverse_completed=False, original_Weil_or_augmented_actions_performed=False, whole_aperture_positivity_extended=False, RH=False, F4=False, Lean=False, next_cursor='tighten t and common-source endpoint energies, or derive sharper global residual spectral bounds; test required reference tolerance before original source transport')


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--replay', action='store_true')
    p.add_argument('--output', required=True)
    p.add_argument('inputs', nargs=7)
    a = p.parse_args()
    result = run(a.inputs, a.replay)
    if a.replay: assert json.loads(Path(a.output).read_text()) == result
    else: Path(a.output).write_text(json.dumps(result, sort_keys=True, indent=2)+'\n')
    print('RC139 PASS: two-sided direct P0 variational response')
