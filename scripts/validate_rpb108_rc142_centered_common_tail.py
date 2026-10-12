"""RC142: orthogonal analytic tail and centered contraction energy upper."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import down,up,sqrtup
from validate_rpb108_rc141_positive_common_tail import run as rc141_run

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths]
    prior=json.loads(raw[0]);assert prior==rc141_run(paths[1:],replay)
    rc139=json.loads(raw[2]);response=json.loads(raw[3]);joint=json.loads(raw[5]);common=json.loads(raw[6])
    assert [x['milestone'] for x in (prior,rc139,response,joint,common)]==['RC141','RC139','RC138','RC136','RC135']
    assert common['source_finite_degree']==8190
    tail=F(common['common_input_analytic_tail_D_energy_upper'])
    guu=F(prior['common_source_D_energy_upper'])
    gut=F(prior['common_source_t_D_Gram_upper'])
    error=F(prior['paid_finite_action_common_pairing_error_upper'])
    assert tail>0 and guu>tail
    # u_f and u_tail have disjoint Legendre supports, so G(u,u_tail)=||u_tail||^2.
    # ||C-I/2||<=1/2 gives H(u,u_tail)<=tail/2+sqrt(Guu*tail)/2.
    interaction=up(tail/2+sqrtup(guu*tail)/2)
    centeredUpper=up(gut+error+interaction)
    oldUpper=F(response['trial_frame_endpoint_entry_upper'][3][3])
    newUpper=min(oldUpper,centeredUpper)
    newLower=F(prior['new_common_endpoint_energy_lower'])
    assert newLower<newUpper<oldUpper
    gain=oldUpper-newUpper
    G00upper=F(joint['actual_D_Gram_entry_upper'][0][0])
    trials=rc139['rational_trials'][:]
    if replay:trials.reverse()
    accepted=[]
    for trial in trials:
        cu=F(trial['coefficients'][3])
        L=F(trial['variational_functional_lower'])+cu*cu*gain
        lower=L+F(trial['true_residual_D_energy_lower'])/2
        accepted.append(dict(name=trial['name'],common_coefficient=str(cu),new_variational_functional_lower=str(L),new_absolute_response_lower=str(lower),new_normalized_response_lower=str(down(lower/G00upper,10**15))))
    accepted.sort(key=lambda x:x['name'])
    oldResponseLower=F(prior['normalized_P0_reference_response_lower'])
    responseLower=max([oldResponseLower]+[F(t['new_normalized_response_lower']) for t in accepted])
    responseUpper=F(prior['normalized_P0_reference_response_upper'])
    assert oldResponseLower<responseLower<responseUpper
    controls=[]
    for lam in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
        assert abs(lam-F(1,2))<=F(1,2)
        controls.append(dict(C_eigenvalue=str(lam),centered_operator_absolute_eigenvalue=str(abs(lam-F(1,2)))))
    return dict(milestone='RC142',status='PASS: centered common-tail contraction tightens endpoint upper and P0 inverse lower',starting_commit='cb519b03421a637b35f2191e98f85bcb58d73f70',input_sha256=[hashlib.sha256(b).hexdigest() for b in raw],aperture='11/10',carrier_family_dimension=7,new_family_vectors_added=0,finite_tail_D_orthogonality_exact=True,common_analytic_tail_D_energy_upper=str(tail),common_D_energy_upper=str(guu),centered_common_tail_endpoint_interaction_upper=str(interaction),common_endpoint_energy_lower_inherited=str(newLower),old_common_endpoint_energy_upper=str(oldUpper),new_common_endpoint_energy_upper=str(newUpper),common_endpoint_upper_improvement=str(gain),finite_common_action_pairing_error_paid=str(error),accepted_response_lower_trials=accepted,selected_lower_trial=[t['name'] for t in accepted if F(t['new_normalized_response_lower'])==responseLower],normalized_P0_reference_response_lower=str(responseLower),normalized_P0_reference_response_upper=str(responseUpper),normalized_P0_reference_response_interval_width=str(responseUpper-responseLower),RC141_response_lower=str(oldResponseLower),RC141_interval_width=str(responseUpper-oldResponseLower),previous_width_over_new_width_lower=str(down((responseUpper-oldResponseLower)/(responseUpper-responseLower),10**6)),centered_contraction_scalar_controls=controls,all_infinite_tail_interactions_paid=True,high_accuracy_reference_inverse_completed=False,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,next_cursor='refine t endpoint energies or full source response matrix; check explicit Stage I response budget before original-source transport')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=10)
    a=p.parse_args();result=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==result
    else:Path(a.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC142 PASS: centered common-tail energy bound')
