"""RC197: complete native v10 canonical action with centered input tail."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup
from validate_rpb108_rc171_regular_legendre_projection import rat as hrat,divide,endpoints
from validate_rpb108_rc176_f0_regular_output_carrier import root,lower_root

def inputs():
    base=Path(__file__).resolve().parents[1]/'certificates'
    return [base/('rpb108_rc'+n+'.json') for n in ['196_adaptive_action_error_inverse','183_w14_canonical_action','183_materialized_w14_canonical_carrier','131_finite_part_response_capture','130_remaining_covariance','133_six_vector_joint_matrices','129_four_vector_joint_moment','121_diagonal_metric_equivalence','170_poisson_regular_action']]

def run(paths,replay=False):
    raw=[p.read_bytes() for p in paths];prior,attached,carrier,capture,history,joint6,joint,metric,regular=map(json.loads,raw);hs=[hashlib.sha256(b).hexdigest() for b in raw]
    assert [x['milestone'] for x in [prior,attached,carrier,capture,history,joint6,joint,metric,regular]]==['RC196','RC183','RC183-w14-carrier','RC131','RC130','RC133','RC129','RC121','RC170']
    assert attached['materialized_canonical_carrier_sha256']==hs[2] and attached['input_sha256'][1]==hs[4] and capture['input_sha256'][0]==hs[4]
    assert joint6['input_sha256'][1:4]==hs[3:5]+hs[6:7] and history['input_sha256'][0]==hs[6]
    assert carrier['historical_two_column_endpoint_sha256']==history['finite_action_trial_coefficient_sha256']
    assert metric['endpoint_form_bound']=='0 <= h <= J + 2 log(2) I <= D' and prior['canonical_half_Gram_inverse_width_gate_passed']
    native={2*i:F(c) for i,c in enumerate(carrier['Cg_finite_coefficient_centers'])};g={2*i:F(c) for i,c in enumerate(carrier['native_w14_finite_coefficient_centers'])}
    assert len(native)==4096 and max(native)==8190 and min(native.values())>0
    mu=list(map(F,capture['collective_capture_budgets'][1]['analytic_moment_center_coefficients']));lamNative=F(capture['tail_Lambda']);assert len(mu)==11 and lamNative==4094*4095
    M=512;O=1536;K=24;r=F(789,125)
    sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B)
    s=(rat(sl)[0],rat(sh)[1]);log=(rat(1-F(joint['actual_endpoint_pairing_entry_upper'][0][0])/(2*B))[0],rat(1-F(joint['actual_endpoint_pairing_entry_lower'][0][0])/(2*B))[1])
    H=[Z]
    for n in range(1,16383):H.append(plus(H[-1],rat(F(1,n))))
    D={n:plus(H[n],s) for n in range(0,8191,2)}
    diag=lambda n:minus(plus(minus(mul(rat(2),H[2*n]),mul(rat(2),H[n])),rat(F(1,2*n+1))),log)
    # RC130 and RC131 use identical Cg midpoint/floor formulas. Verify
    # direct controls against the custody-bound materialized native prefix.
    controls=[]
    for n in ([8190,512,2,0] if replay else [0,2,512,8190]):
        v=Z
        for m in sorted(g,reverse=replay):
            entry=diag(n) if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
            v=plus(v,mul(entry,rat(g[m])))
        lo,hi=bounds(div(v,D[n]));c=down((lo+hi)/2);assert c==native[n]
        controls.append(dict(degree=n,reconstructed_native_coefficient=str(c)))
    controls.sort(key=lambda x:x['degree'])
    # Reproduce every native finite center and radius, not only controls.
    nativePayload=[]
    for n in (range(8190,-1,-2) if replay else range(0,8191,2)):
        v=Z
        for m in sorted(g,reverse=replay):
            entry=diag(n) if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
            v=plus(v,mul(entry,rat(g[m])))
        lo,hi=bounds(div(v,D[n]));c=down((lo+hi)/2);rad=max(c-lo,hi-c)
        assert c==native[n]
        nativePayload.append(dict(degree=n,center=str(c),radius=str(rad)))
        if n%2048==0:print('RC197 complete native source block',n,flush=True)
    nativePayload.sort(key=lambda x:x['degree'])
    nativeDigest=hashlib.sha256(json.dumps(nativePayload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert nativeDigest==capture['finite_output_polynomial_center_radius_sha256']
    alpha={n:native[n] for n in range(0,M+1,2)}
    prefixLo=sum(down(2*B/F(2*n+1)*F(D[n][0])*c*c) for n,c in alpha.items())
    energyLo=F(joint6['actual_D_Gram_entry_lower'][4][4]);energyHi=F(joint6['actual_D_Gram_entry_upper'][4][4]);tailEnergy=up(energyHi-prefixLo);assert 0<tailEnergy<energyHi
    # Complete endpoint action on the exact finite prefix, plus half of
    # the actual omitted native source (0<=C<=I on the full D domain).
    endpoint=[];endpointEnergy=F(0);negative=[];negativeEnergy=F(0)
    for n in (range(O,-1,-2) if replay else range(0,O+1,2)):
        v=Z
        for m in sorted(alpha,reverse=replay):
            entry=diag(n) if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
            v=plus(v,mul(entry,rat(alpha[m])))
        lo,hi=bounds(div(v,D[n]));c=down((lo+hi)/2,10**40);rad=max(c-lo,hi-c)
        endpoint.append(dict(degree=n,coefficient_center=str(c),coefficient_radius=str(rad)))
        endpointEnergy+=2*B/F(2*n+1)*F(D[n][1])*rad*rad
        if n<=M:
            v=divide(hrat(-r*alpha[n]),D[n]);lo,hi=endpoints(v);c=(lo+hi)/2;rad=(hi-lo)/2
            negative.append(dict(degree=n,coefficient_center=str(c),coefficient_radius=str(rad)));negativeEnergy+=2*B/F(2*n+1)*F(D[n][1])*rad*rad
    endpoint.sort(key=lambda x:x['degree']);negative.sort(key=lambda x:x['degree'])
    lam=M*(M+1);rho=F(lam,(O+2)*(O+3));moments=[sum(alpha[m]*F(m*(m+1),lam)**k for m in sorted(alpha,reverse=replay)) for k in range(K+1)]
    A=sum(alpha.values());T=up(B/(F(D[O][0])*(O-1)*O));remainder=up(root(T)*A*rho**(K+1)/(1-rho),10**80)
    endpointError=up(root(endpointEnergy+remainder**2)+root(tailEnergy)/2)
    # Orthogonal high-input regular smoothing, with full native tail energy.
    e=F(regular['e_upper']);p=F(regular['pi_upper']);I2=up(e*p*p/3);band=F(M+1)/(6*p*B)
    phi2=up(min(r*r,4*B*I2*up(F(11,12)**(2*(M+1)),10**80)+e*e/(band*band)))
    inputError=up(root(phi2*tailEnergy/(sl*F(D[M+2][0]))))
    path=Path(__file__).with_name('validate_rpb108_rc179_focus_residual_canonical_action.py');src=path.read_text().split("\nif __name__=='__main__':")[0]
    assert src.count('K=192;N=768;J=')==1;src=src.replace('K=192;N=768;J=','K=192;N=1536;J=')
    ns={'__file__':str(path)};exec(compile(src,'RC197 finite regular action','exec'),ns)
    helper=Path(__file__).with_name('validate_rpb108_rc171_regular_legendre_projection.py');hsrc=helper.read_text().split("\nif __name__=='__main__':")[0]
    assert hsrc.count('prec=360')==2 and hsrc.count("TOL=D('1e-300')")==1
    hsrc=hsrc.replace('prec=360','prec=600').replace("TOL=D('1e-300')","TOL=D('1e-540')")
    private={};exec(compile(hsrc,'RC197 private directed interval helpers','exec'),private)
    for key in ['ZERO','rat','add','sub','mul','scale','divide','div_int','endpoints','log_point']:ns[key]=private[key]
    ns['root']=lambda x,grid=10**600:root(x,grid)
    reg=ns['regular_action'](alpha,regular,joint,replay)
    regularError=up(inputError+F(reg['complete_D_inverse_regular_action_error_norm_upper']))
    complete=up(endpointError+root(negativeEnergy)+regularError);relative=up(complete/lower_root(energyLo))
    print('RC197 v10 endpoint/regular/full/relative',float(endpointError),float(regularError),float(complete),float(relative),flush=True)
    return dict(milestone='RC197',status='PASS: complete native v10 canonical action with all input/output tails paid',starting_commit='a301c40dc56360621d20f044abbbd7e579639f23',input_sha256=hs,aperture='11/10',canonical_operator='M=D^-1 L',norm='D energy',native_source='unchanged v10, RC131 order10 finite/analytic source used by RC133',native_prefix_reference='RC183 Cg_finite_coefficient_centers, input_sha256[2], even0..8190',native_prefix_center_sha256=hashlib.sha256(json.dumps(list(map(str,native.values())),separators=(',',':')).encode()).hexdigest(),native_analytic_first_even_degree=8192,native_analytic_lambda=str(lamNative),native_analytic_moments=list(map(str,mu)),native_analytic_coefficient_formula='eta_n*sum_k=0..10 mu_k*(lambda/[n(n+1)])^k',native_prefix_generator_controls=controls,full_native_prefix_center_radius_sha256=nativeDigest,all_native_prefix_coefficients_and_radii_reproduced=True,native_D_energy_lower=str(energyLo),native_D_energy_upper=str(energyHi),finite_action_input_degree=M,endpoint_output_degree=O,input_prefix_coefficients=[dict(degree=n,coefficient_center=str(alpha[n])) for n in sorted(alpha)],omitted_native_input_D_energy_upper=str(tailEnergy),endpoint_action_polynomial=endpoint,endpoint_coefficient_error_D_energy_upper=str(up(endpointEnergy)),endpoint_analytic_first_even_degree=O+2,endpoint_analytic_lambda=str(lam),endpoint_analytic_signed_moments=list(map(str,moments)),endpoint_analytic_coefficient_formula='eta_n*sum_k=0..24 moment_k*(lambda/[n(n+1)])^k',endpoint_analytic_remainder_D_norm_upper=str(remainder),centered_endpoint_native_input_tail_first_even_degree=M+2,centered_endpoint_native_input_tail_coefficient='1/2 times actual native v10',complete_endpoint_action_D_error_norm_upper=str(endpointError),negative_r_finite_polynomial=negative,negative_r_coefficient_error_D_energy_upper=str(up(negativeEnergy)),exact_negative_r_native_tail='-r/D_n times actual native v10 coefficient, even n>=514; actual s retained',regular_action=reg,regular_input_smoothing_squared_upper=str(phi2),regular_input_tail_D_error_norm_upper=str(inputError),complete_D_inverse_Rv10_error_norm_upper=str(regularError),complete_canonical_v10_action_D_error_norm_upper=str(complete),complete_canonical_v10_relative_D_norm_error_upper=str(relative),represented_action='native v10 + finite endpoint action + retained analytic endpoint output + half omitted native input + negative-r finite polynomial + exact negative-r native tail + regular polynomial',all_native_input_and_infinite_output_tails_paid=True,native_source_definition_unchanged=True,endpoint_tail_commutation_assumed=False,interval_decimal_precision=600,square_root_bound_grid_digits=600,new_inverse_response_evaluated=False,accepted_five_source_inverse_width_retained=prior['relative_inverse_width_upper'],expanded_inverse_acceptance_open=True,Stage_I_closed=False,Stage_I_completion_ratio=None,RH=False,F4=False,Lean=False,next_cursor='attach native v10 action to full correlated mixed rows, extend inverse response family and test its acceptance separately')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');a=p.parse_args();r=run(inputs(),a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC197 PASS')
