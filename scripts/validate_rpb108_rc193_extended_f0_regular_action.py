"""RC193: larger paid regular input/output carrier for unchanged native f0."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,up,down
from validate_rpb108_rc176_f0_regular_output_carrier import root,lower_root

def inputs():
    base=Path(__file__).resolve().parents[1]/'certificates'
    return [base/('rpb108_rc'+x+'.json') for x in ['192_low_polynomial_regular_actions','176_f0_regular_output_carrier','174_regular_source_tail_compression','170_poisson_regular_action','129_four_vector_joint_moment','121_diagonal_metric_equivalence']]

def run(paths,replay=False):
    raw=[p.read_bytes() for p in paths];prior,old,tail,regular,joint,metric=map(json.loads,raw);hs=[hashlib.sha256(x).hexdigest() for x in raw]
    assert [x['milestone'] for x in [prior,old,tail,regular,joint,metric]]==['RC192','RC176','RC174','RC170','RC129','RC121']
    assert old['input_sha256'][1:]==hs[2:5]
    assert metric['endpoint_form_bound']=='0 <= h <= J + 2 log(2) I <= D'
    M=512;N=1536;r=F(789,125);sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B)
    harmonic=[F(0)]
    for n in range(1,989):harmonic.append(harmonic[-1]+F(1,n))
    alpha={};rows=[];centerEnergy=F(0);tailEnergy=F(0)
    for n in (range(988,1,-2) if replay else range(2,989,2)):
        mass=2*B/F(2*n+1);base=F(2*n+1,n*(n+1));lo=base/(sh+harmonic[n]);hi=base/(sl+harmonic[n])
        if n<=M:
            lo,hi=down(lo,10**80),up(hi,10**80);cc=(lo+hi)/2;rad=(hi-lo)/2;alpha[n]=cc
            centerEnergy+=mass*rad*rad;rows.append(dict(degree=n,coefficient_center=str(cc),coefficient_radius=str(rad)))
        else:tailEnergy+=mass*hi*hi
    rows.sort(key=lambda x:x['degree']);centerEnergy=up(centerEnergy);tailEnergy=up(tailEnergy)
    # R has physical L2 norm <=r. RC174's orthogonal high-mode smoothing
    # pays the actual f0 tail (degrees 514..988), independently of centres.
    e=F(regular['e_upper']);p=F(regular['pi_upper']);I2=up(e*p*p/3);band=F(M+1)/(6*p*B)
    phi2=up(min(r*r,4*B*I2*up(F(11,12)**(2*(M+1)),10**80)+e*e/(band*band)))
    tailError=up(root(phi2*tailEnergy)/lower_root(sl));centerError=up(r*root(centerEnergy)/lower_root(sl))
    path=Path(__file__).with_name('validate_rpb108_rc179_focus_residual_canonical_action.py');src=path.read_text().split("\nif __name__=='__main__':")[0]
    assert src.count('K=192;N=768;J=')==1;src=src.replace('K=192;N=768;J=','K=192;N=1536;J=')
    ns={'__file__':str(path)};exec(compile(src,'RC193 extended analytic regular projection','exec'),ns)
    helper=Path(__file__).with_name('validate_rpb108_rc171_regular_legendre_projection.py');hsrc=helper.read_text().split("\nif __name__=='__main__':")[0]
    assert hsrc.count('prec=360')==2 and hsrc.count("TOL=D('1e-300')")==1
    hsrc=hsrc.replace('prec=360','prec=600').replace("TOL=D('1e-300')","TOL=D('1e-540')")
    private={};exec(compile(hsrc,'RC193 private directed interval helpers','exec'),private)
    for key in ['ZERO','rat','add','sub','mul','scale','divide','div_int','endpoints','log_point']:ns[key]=private[key]
    ns['root']=lambda x,grid=10**600:root(x,grid)
    reg=ns['regular_action'](alpha,regular,joint,replay)
    regularError=up(tailError+centerError+F(reg['complete_D_inverse_regular_action_error_norm_upper']))
    # RC176's complete bound is its regular error plus endpoint/correction
    # payments, rounded upwards. Their difference is therefore a safe
    # upper bound for the retained nonregular payments.
    retained=F(old['canonical_f0_trial_D_error_norm_upper'])-F(old['complete_actual_D_inverse_Rf0_carrier_error_norm_upper']);assert retained>=0
    complete=up(regularError+retained);assert regularError<F(old['complete_actual_D_inverse_Rf0_carrier_error_norm_upper']) and complete<F(old['canonical_f0_trial_D_error_norm_upper'])
    result=dict(milestone='RC193',status='PASS: extended regular carrier for unchanged native f0',starting_commit='0318b854a18957aea75b5443b407e1aab9416b22',input_sha256=hs,aperture='11/10',canonical_operator='M=D^-1 L',norm='D energy',native_source='f0=sum eta_n Pn over even n=2..988',regular_input_degree=M,regular_output_degree=N,input_coefficient_intervals=rows,physical_input_center_error_energy_upper=str(centerEnergy),physical_input_tail_energy_upper=str(tailEnergy),regular_input_tail_smoothing_squared_factor_upper=str(phi2),regular_input_tail_D_action_error_norm_upper=str(tailError),regular_input_center_D_action_error_norm_upper=str(centerError),regular_action=reg,interval_decimal_precision=600,square_root_bound_grid_digits=600,complete_actual_D_inverse_Rf0_carrier_error_norm_upper=str(regularError),retained_endpoint_and_negative_r_error_norm_upper=str(retained),canonical_f0_trial_D_error_norm_upper=str(complete),previous_same_source_regular_error_norm_upper=old['complete_actual_D_inverse_Rf0_carrier_error_norm_upper'],previous_same_source_complete_action_error_norm_upper=old['canonical_f0_trial_D_error_norm_upper'],negative_r_D_inverse_f0_polynomial=old['negative_r_D_inverse_f0_polynomial'],canonical_f0_trial='native f0 + native w14 + retained RC176 negative-r correction + RC193 regular polynomial',full_input_and_output_tails_paid=True,native_seven_source_frame_changed=False,new_inverse_response_evaluated=False,inherited_inverse_width_upper=prior['inherited_RC191_inverse_width_upper'],canonical_half_Gram_inverse_width_gate_closed=False,Stage_I_closed=False,original_Weil_or_augmented_actions_performed=False,RH=False,F4=False,Lean=False,next_cursor='refine q185 endpoint output tail, then rebuild complete mixed rows and unchanged five-source inverse with RC192 and RC193 regular carriers')
    print('RC193 regular',float(regularError),'full',float(complete),'old full',float(F(old['canonical_f0_trial_D_error_norm_upper'])),flush=True)
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');a=p.parse_args();result=run(inputs(),a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==result
    else:Path(a.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC193 PASS: extended native f0 regular action')
