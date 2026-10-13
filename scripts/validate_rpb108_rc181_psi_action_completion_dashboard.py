"""RC181: full psi regular-action bound, canonical source form, progress contracts."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,down,up,sqrtup,psd,ser
from validate_rpb108_rc129_four_vector_joint_moment import add
from validate_rpb108_rc177_three_source_canonical_action_gram import mat,scale,width

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];inverse,three,compression,regular,joint,endpoint,native=map(json.loads,raw)
    assert [x['milestone'] for x in (inverse,three,compression,regular,joint,endpoint,native)]==['RC180','RC177','RC174','RC170','RC129','RC154','RC169']
    hs=[hashlib.sha256(b).hexdigest() for b in raw]
    assert inverse['input_sha256'][2]==hs[1] and inverse['input_sha256'][6]==hs[4]
    assert compression['input_sha256'][1]==hs[6] and compression['input_sha256'][4]==hs[3] and compression['input_sha256'][-1]==hs[4]
    assert regular['input_sha256'][0]==hs[6] and endpoint['input_sha256'][0]==hs[4]
    assert inverse['original_response_source_D_Gram_lower']==three['source_D_Gram_lower']
    N=988;first=990;sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B)
    harmonics=list(range(1,first+1));harmonics=harmonics[::-1] if replay else harmonics
    Dfirst=sl+sum(F(1,n) for n in harmonics)
    gl=F(joint['actual_D_Gram_entry_lower'][1][1]);gh=F(joint['actual_D_Gram_entry_upper'][1][1]);assert 0<gl<=gh
    e=F(regular['e_upper']);p=F(regular['pi_upper']);r=F(789,125)
    I2=up(e*p*p/3);U=F(N+1)/(6*p*B)
    rem=up(F(11,12)**(2*(N+1)),10**80)
    phi2=up(min(r*r,4*B*I2*rem+e*e/(U*U)))
    physicalEnergy=up(gh/Dfirst);regularEnergy=up(phi2*physicalEnergy/sl)
    regularError=sqrtup(regularEnergy);regularRelativeEnergy=up(regularEnergy/gl)
    regularRelativeNorm=sqrtup(regularRelativeEnergy)
    componentBudget=F(1,100);componentRatio=up(regularRelativeNorm/componentBudget)
    assert regularEnergy<componentBudget*componentBudget*gl and componentRatio<1
    epsEndpoint=F(endpoint['full_Cpsi_trial_D_norm_error_upper'])
    canonicalError=up(epsEndpoint+regularError);canonicalRelativeNorm=up(canonicalError/(sqrtup(gl)-F(1,10**40)))
    # Exact source-form attachment keeps psi and -r D^-1 psi analytically;
    # only the actual bounded regular action is replaced by zero.
    assert endpoint['source_prefix_degree']==8190 and endpoint['output_prefix_degree']==16382
    assert endpoint['analytic_output_moment_count']==25 and not endpoint['analytic_input_tail_assigned_zero']
    assert len(endpoint['analytic_output_moment_intervals'])==26
    G3lo=mat(three,'source_D_Gram_lower');G3hi=mat(three,'source_D_Gram_upper')
    G4lo=[row+[F(0)] for row in G3lo]+[[F(0),F(0),F(0),gl]]
    G4hi=[row+[F(0)] for row in G3hi]+[[F(0),F(0),F(0),gh]]
    assert psd(G4lo)
    eps=list(map(F,three['individual_full_action_D_error_norm_upper']))+[canonicalError]
    weights=[sqrtup(G4hi[i][i]) for i in range(4)];S=sum(eps[i]/weights[i] for i in range(4))
    E=[[up(eps[i]*weights[i]*S) if i==j else F(0) for j in range(4)] for i in range(4)]
    assert psd(add(E,[[eps[i]*eps[j] for j in range(4)] for i in range(4)],-1))
    beta4=width(E,G4lo);norm4=sqrtup(beta4)
    assert beta4>F(three['action_error_relative_to_three_source_D_Gram_squared_upper'])
    selected=inverse['selected_enclosure'];upper=mat(selected,'canonical_inverse_response_upper');lower=mat(selected,'canonical_inverse_response_lower')
    beta=F(inverse['relative_inverse_width_upper']);budget=F(1,2);ratio=beta/budget;margin=budget-beta
    assert inverse['canonical_half_Gram_inverse_width_gate_passed'] and margin>0
    gap=add(upper,lower,-1);gate=add(scale(budget,G3lo),gap,-1)
    assert psd(add(scale(beta,G3lo),gap,-1)) and psd(add(gate,scale(margin,G3lo),-1))
    assert beta==F(300941,10**6) and ratio==F(300941,500000)
    nativeCoverage=[]
    for name in native['native_order']:
        if name=='P0':status='complete canonical carrier: RC171; inverse covered in RC180'
        elif name=='f0':status='complete canonical carrier: RC176; inverse covered in RC180'
        elif name=='psi0':status='RC154 endpoint generator plus exact analytic -r D^-1 term and RC181 paid regular zero carrier; coefficients not rematerialized here; inverse open'
        else:status='reference endpoint coverage inherited; explicit complete canonical carrier and inverse coverage open'
        nativeCoverage.append(dict(source=name,status=status))
    history=[dict(checkpoint='RC178',scope='same actual canonical inverse on P0/P2/f0',width=inverse['previous_three_source_relative_width_upper'],threshold='1/2',ratio=str(F(inverse['previous_three_source_relative_width_upper'])/budget),accepted=False),
      dict(checkpoint='RC180',scope='same actual canonical inverse on P0/P2/f0',width=str(beta),threshold='1/2',ratio=str(ratio),certified_margin_against_source_Gram=str(margin),accepted=True)]
    dashboard=dict(operator='actual supported canonical M=D^-1 L, B=11/10',response_source_family=['P0','P2','f0'],evaluated_inverse_parity_sectors=['even'],odd_sector_inverse_coverage_supplied_here=False,
      inverse_width_history=history,canonical_inverse_relative_width=str(beta),canonical_inverse_requested_width=str(budget),canonical_inverse_completion_ratio=str(ratio),canonical_inverse_certified_acceptance_margin=str(margin),
      canonical_inverse_half_Gram_contract_closed=True,canonical_warmstart_relative_true_image_norm_upper=inverse['canonical_Riesz_warmstart_relative_true_image_norm_upper'],
      three_source_first_moment_relative_width_upper=three['relative_first_moment_width_upper'],three_source_action_Gram_relative_width_upper=three['relative_action_Gram_width_upper'],
      three_source_first_moment_required_width=None,three_source_action_Gram_required_width=None,three_source_action_accuracy_required_norm=None,
      three_source_action_error_relative_squared_factor_upper=three['action_error_relative_to_three_source_D_Gram_squared_upper'],
      three_source_action_error_relative_norm_upper=str(sqrtup(F(three['action_error_relative_to_three_source_D_Gram_squared_upper']))),
      four_source_action_error_relative_squared_factor_upper=str(beta4),four_source_action_error_relative_norm_upper=str(norm4),
      four_source_action_error_family=['P0','P2','f0','psi0'],four_source_action_accuracy_acceptance_threshold=None,
      action_error_three_to_four_families_directly_comparable=False,coverage_grew_while_worst_error_bound_increased=True,
      psi_regular_component_local_relative_norm_budget=str(componentBudget),psi_regular_component_relative_norm_error_upper=str(regularRelativeNorm),psi_regular_component_completion_ratio=str(componentRatio),
      psi_regular_component_local_contract_closed=True,psi_complete_canonical_relative_norm_error_upper=str(canonicalRelativeNorm),psi_complete_canonical_required_accuracy=None,
      native_source_coverage=nativeCoverage,native_frame_dimension=7,auxiliary_polynomial_response_direction='P2',auxiliary_inverse_trial_direction='RC179 q',
      full_canonical_domain_structural_metric_theorem_covered=True,full_native_seven_source_canonical_inverse_closed=False,
      original_augmentation_adjoint_source_range_identified=False,original_augmented_Weil_floor_certified=False,original_auxiliary_response_below_one_certified=False,
      Stage_I_selected_numerical_matrix_tolerance=None,Stage_I_certified_acceptance_margin=None,Stage_I_completion_ratio=None,Stage_I_closed=False,
      aggregate_completion_percentage=None,same_operator_domain_norm_source_family_required_for_precision_comparison=True,
      finite_native_frame_is_not_original_full_source_coverage=True)
    return dict(milestone='RC181',status='PASS: actual infinite psi regular component and canonical source-form action error; explicit completion dashboard',starting_commit='078dd1eff1b1f94291264a60fed97f05ff018039',input_sha256=hs,
      actual_psi_definition='eta_n=(2n+1)/(n(n+1)(H_n+s)), even n>=990; all other coefficients zero',
      high_input_mode_cutoff=N,first_actual_psi_degree=first,diagonal_floor_on_psi_support_lower=str(Dfirst),low_frequency_half_bandwidth=str(U),regular_high_mode_operator_squared_bound=str(phi2),
      actual_psi_D_energy_lower=str(gl),actual_psi_D_energy_upper=str(gh),actual_psi_physical_L2_energy_upper=str(physicalEnergy),
      regular_psi_trial='zero on the entire output carrier; all actual omitted modes paid by the whole-function high-input-mode estimate',
      complete_actual_D_inverse_Rpsi_error_energy_upper=str(regularEnergy),complete_actual_D_inverse_Rpsi_error_norm_upper=str(regularError),regular_component_relative_D_norm_error_upper=str(regularRelativeNorm),
      regular_component_local_relative_norm_budget=str(componentBudget),regular_component_local_acceptance_ratio=str(componentRatio),regular_component_local_contract_closed=True,
      inherited_Cpsi_generator_definition=endpoint['trial_definition'],inherited_Cpsi_finite_center_radius_sha256=endpoint['finite_action_trial_center_radius_sha256'],
      inherited_Cpsi_analytic_moments=endpoint['analytic_output_moment_intervals'],inherited_Cpsi_full_action_error_norm_upper=str(epsEndpoint),
      canonical_psi_source_form='psi0 + RC154 Cpsi trial - r D^-1 psi0; exact analytic D^-1 psi retained, regular trial zero',
      exact_negative_r_D_inverse_psi_coefficient='-r*(2n+1)/(n(n+1)(H_n+s)^2), even n>=990',
      canonical_psi_source_form_full_D_error_norm_upper=str(canonicalError),canonical_psi_source_form_relative_D_norm_error_upper=str(canonicalRelativeNorm),
      canonical_psi_source_form_attached=True,canonical_psi_coefficients_rematerialized=False,regular_output_nonzero_coefficients_evaluated=False,
      four_source_D_Gram_lower=ser(G4lo),four_source_D_Gram_upper=ser(G4hi),four_source_full_correlated_action_error_Gram_upper=ser(E),
      four_source_action_error_relative_squared_factor_upper=str(beta4),four_source_action_error_relative_norm_upper=str(norm4),all_real_and_complex_four_source_action_error_mixtures_paid=True,
      completion_dashboard=dashboard,full_four_source_canonical_inverse_certified=False,full_seven_source_canonical_inverse_certified=False,native_seven_source_frame_changed=False,
      Stage_I_closed=False,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='rematerialize the inherited Cpsi finite/analytic carrier as needed for correlated four-source inverse trials, then certify the P0/P2/f0/psi0 inverse response; keep the dashboard scope and acceptance margins explicit')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');p.add_argument('inputs',nargs=7)
    args=p.parse_args();result=run(args.inputs,args.replay)
    if args.replay:assert json.loads(Path(args.output).read_text())==result
    else:Path(args.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC181 PASS: paid infinite psi action source form and completion dashboard')
