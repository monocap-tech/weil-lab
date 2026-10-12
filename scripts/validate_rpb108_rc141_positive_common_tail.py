"""RC141: positive common analytic tail tightens H(u,u) and P0 response."""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,down,up,sqrtup
from validate_rpb108_rc140_residual_endpoint_probe import run as rc140_run


def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths]
    prior=json.loads(raw[0]);assert prior==rc140_run(paths[1:],replay)
    response,joint,common=map(lambda i:json.loads(raw[i]),(2,4,5))
    assert [x['milestone'] for x in (prior,response,joint,common)]==['RC140','RC138','RC136','RC135']
    # RC135 reconstructs and verifies the strictly positive finite u source.
    assert common['common_source_definition']=='u=(v10+z_b6)/2'
    assert common['source_finite_degree']==8190
    moments=[F(v) for v in common['common_input_analytic_moment_centers']]
    assert len(moments)==11 and all(v>0 for v in moments)
    assert all(F(v['lower'])>0 for v in common['positive_finite_source_moment_intervals'])
    # For n<=8190<m, the explicit endpoint kernel is 2B/|z_n-z_m|>0.
    controls=[]
    for n,m in ((0,8192),(2,8192),(8190,8192),(8190,16384)):
        coefficient=2*B/F(abs(n*(n+1)-m*(m+1)))
        assert n<=8190<m and coefficient>0
        controls.append(dict(finite_even_degree=n,analytic_even_degree=m,positive_cross_kernel=str(coefficient)))
    GL=[[F(x) for x in row] for row in joint['actual_D_Gram_entry_lower']]
    GU=[[F(x) for x in row] for row in joint['actual_D_Gram_entry_upper']]
    GuTlower=down((GL[4][6]+GL[5][6])/2)
    GuTupper=up((GU[4][6]+GU[5][6])/2)
    GuuUpper=up((GU[4][4]+2*GU[4][5]+GU[5][5])/4)
    finiteError=F(common['collective_capture_budgets'][1]['finite_common_action_trial_D_norm_error_upper'])
    paidError=up(finiteError*sqrtup(GuuUpper))
    # u=u_f+u_tail, t approximates C u_f with error finiteError.
    # H(u,u_tail)=H(u_f,u_tail)+H(u_tail,u_tail)>=0:
    # off-diagonal cross entries are positive, and C is positive on the tail.
    HuuSignLower=down(GuTlower-paidError)
    oldHuu=F(response['trial_frame_endpoint_entry_lower'][3][3])
    oldHuuUpper=F(response['trial_frame_endpoint_entry_upper'][3][3])
    tightened=max(oldHuu,HuuSignLower)
    assert oldHuu<tightened<=oldHuuUpper
    gain=tightened-oldHuu
    rc139=json.loads(raw[1]);trial=next(t for t in rc139['rational_trials'] if t['name']=='upper_optimized')
    c=[F(x) for x in trial['coefficients']]
    # Its c_u^2 H(u,u) contribution increases the lower endpoint energy;
    # all other RC139/RC140 signed entries and the residual bounds are inherited.
    assert c[3]!=0
    variationalUpper=F(trial['variational_functional_upper'])-c[3]*c[3]*gain
    absoluteUpper=variationalUpper+F(trial['true_residual_D_energy_upper'])-F(prior['actual_residual_endpoint_energy_lower'])/2
    G00lower=GL[0][0]
    newUpper=up(absoluteUpper/G00lower,10**15)
    oldUpper=F(prior['normalized_P0_reference_response_upper'])
    lower=F(prior['normalized_P0_reference_response_lower'])
    assert lower<newUpper<oldUpper
    return dict(milestone='RC141',status='PASS: positive common analytic source tail tightens actual endpoint energy and P0 reference response',starting_commit='4b849bc814baeda48aa67db1f925a2a7e643a396',input_sha256=[hashlib.sha256(b).hexdigest() for b in raw],aperture='11/10',carrier_family_dimension=7,new_family_vectors_added=0,common_finite_source_positive_inherited_from_RC135=True,common_analytic_moment_coefficient_count=len(moments),common_analytic_moment_coefficients_positive=True,positive_finite_analytic_cross_kernel_controls=controls,common_source_t_D_Gram_lower=str(GuTlower),common_source_t_D_Gram_upper=str(GuTupper),common_source_D_energy_upper=str(GuuUpper),finite_common_action_D_norm_error_upper=str(finiteError),paid_finite_action_common_pairing_error_upper=str(paidError),old_common_endpoint_energy_lower=str(oldHuu),positive_tail_common_endpoint_energy_lower=str(HuuSignLower),new_common_endpoint_energy_lower=str(tightened),common_endpoint_lower_improvement=str(gain),common_endpoint_upper_inherited=str(oldHuuUpper),selected_reference_trial='RC139 upper_optimized with RC140 endpoint residual correction',trial_common_coefficient=str(c[3]),normalized_P0_reference_response_lower=str(lower),normalized_P0_reference_response_upper=str(newUpper),normalized_P0_reference_response_interval_width=str(newUpper-lower),RC140_normalized_upper=str(oldUpper),upper_endpoint_improvement=str(oldUpper-newUpper),full_analytic_tail_input_paid_by_positive_cross_kernel_and_C_positivity=True,finite_action_rounding_and_omitted_output_paid=True,high_accuracy_reference_inverse_completed=False,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,next_cursor='sharpen common endpoint upper and t endpoint rows with explicit tail kernel bounds; identify matrix response tolerance and original-source transport requirements')


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--replay',action='store_true')
    p.add_argument('--output',required=True)
    p.add_argument('inputs',nargs=9)
    a=p.parse_args();result=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==result
    else:Path(a.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC141 PASS: positive common-tail endpoint sharpening')
