"""RC192: analytic regular carriers for the unchanged P0 and P2 sources."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import up
from validate_rpb108_rc179_focus_residual_canonical_action import regular_action

def inputs():
    root=Path(__file__).resolve().parents[1]/'certificates'
    return [root/('rpb108_rc'+x+'.json') for x in ['191_two_refined_actions_five_source_inverse','171_regular_legendre_projection','172_quadratic_regular_action','170_poisson_regular_action','129_four_vector_joint_moment','121_diagonal_metric_equivalence']]

def run(paths,replay=False):
    raw=[p.read_bytes() for p in paths];prior,p0,p2,regular,joint,metric=map(json.loads,raw)
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert [x['milestone'] for x in [prior,p0,p2,regular,joint,metric]]==['RC191','RC171','RC172','RC170','RC129','RC121']
    assert p2['input_sha256'][0]==hashes[1]
    assert p0['input_sha256'][0]==hashes[3] and p0['input_sha256'][2:]==[hashes[5],hashes[4]]
    assert metric['endpoint_form_bound']=='0 <= h <= J + 2 log(2) I <= D'
    rows=[]
    for degree in ([2,0] if replay else [0,2]):
        old=p0 if degree==0 else p2
        reg=regular_action({degree:F(1)},regular,joint,replay)
        correction=old['canonical_constant_action_P0_correction_error_norm_upper'] if degree==0 else old['endpoint_finite_coefficient_error_norm_upper']
        old_reg=old['full_D_inverse_regular_constant_source_error_norm_upper'] if degree==0 else old['full_D_inverse_regular_P2_error_norm_upper']
        old_full=old['canonical_constant_action_D_error_norm_upper'] if degree==0 else old['canonical_P2_action_D_error_norm_upper']
        complete=up(F(correction)+F(reg['complete_D_inverse_regular_action_error_norm_upper']))
        assert complete<F(old_full) and F(reg['complete_D_inverse_regular_action_error_norm_upper'])<F(old_reg)
        rows.append(dict(source='P'+str(degree),regular_action=reg,retained_endpoint_and_negative_r_coefficient_error_norm_upper=correction,previous_regular_action_error_norm_upper=old_reg,previous_complete_canonical_action_D_error_norm_upper=old_full,complete_canonical_action_D_error_norm_upper=str(complete)))
        print('RC192 source',degree,'old',float(F(old_full)),'new',float(complete),flush=True)
    rows.sort(key=lambda x:x['source'])
    return dict(milestone='RC192',status='PASS: complete unchanged P0 and P2 actions with analytic regular carriers',starting_commit='d7f1e98dd02901d3cc50d0df5cec886bb4655b9f',input_sha256=hashes,aperture='11/10',canonical_operator='M=D^-1 L',norm='D energy',actions=rows,regular_kernel_degree=192,regular_output_degree=768,finite_inputs_exact=True,analytic_output_log_tails_paid=True,source_coverage_unchanged=True,native_seven_source_frame_changed=False,new_inverse_response_evaluated=False,inherited_RC191_inverse_width_upper=prior['relative_inverse_width_upper'],canonical_half_Gram_inverse_width_gate_closed=False,Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='refine f0 regular action and q185 endpoint output tail; reconstruct mixed action rows before evaluating a new inverse width')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');a=p.parse_args();result=run(inputs(),a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==result
    else:Path(a.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC192 PASS: exact low-polynomial regular carriers')
