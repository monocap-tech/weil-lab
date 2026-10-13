"""RC190: exact fixed-point materialization of a larger centered native Cw14 carrier."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import numpy as np
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup
from validate_rpb108_rc176_f0_regular_output_carrier import root,lower_root

def inputs():
    root=Path(__file__).resolve().parents[1]/'certificates'
    return [root/('rpb108_rc'+n+'.json') for n in ['189_refined_psi_five_source_inverse','183_w14_canonical_action','183_materialized_w14_canonical_carrier','129_four_vector_joint_moment','121_diagonal_metric_equivalence','170_poisson_regular_action','174_regular_source_tail_compression']]
def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];prior,old,source,joint,metric,regular,compression=map(json.loads,raw);hs=[hashlib.sha256(b).hexdigest() for b in raw]
    assert [x['milestone'] for x in [prior,old,source,joint,metric,regular,compression]]==['RC189','RC183','RC183-w14-carrier','RC129','RC121','RC170','RC174']
    assert all(h in prior['input_sha256'] for h in hs[1:5])
    assert old['input_sha256'][5:7]==hs[5:] and compression['input_sha256'][4]==hs[5] and compression['input_sha256'][-1]==hs[3]
    assert old['materialized_canonical_carrier_sha256']==hs[2]
    assert metric['endpoint_form_bound']=='0 <= h <= J + 2 log(2) I <= D'
    assert metric['whole_supported_canonical_form_domain_covered'] and joint['joint_Gram_positive_and_endpoint_contraction_verified']
    g={2*i:F(c) for i,c in enumerate(source['native_w14_finite_coefficient_centers'])}
    nativeMu=list(map(F,source['analytic_moment_centers']));nativeLambda=F(source['analytic_lambda'])
    assert len(g)==2048 and min(g.values())>0 and len(nativeMu)==15 and min(nativeMu)>=0 and nativeLambda==977132
    L=32766;O=65534;K=24;S=2**32;Q=2**28;CENTER=10**30
    sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B)
    loglo=1-F(joint['actual_endpoint_pairing_entry_upper'][0][0])/(2*B);loghi=1-F(joint['actual_endpoint_pairing_entry_lower'][0][0])/(2*B)
    H=[Z]
    for n in range(1,2*O+1):H.append(plus(H[-1],rat(F(1,n))))
    D={n:(plus(H[n],rat(sl))[0],plus(H[n],rat(sh))[1]) for n in range(0,O+1,2)}
    diag={n:minus(plus(minus(mul(rat(2),H[2*n]),mul(rat(2),H[n])),rat(F(1,2*n+1))),(rat(loglo)[0],rat(loghi)[1])) for n in D}
    alpha={};inputEnergy=F(0)
    jobs=list(range(0,L+1,2));jobs=jobs[::-1] if replay else jobs
    for m in jobs:
        if m<=4094:coefficient=rat(g[m])
        else:
            eta=div(rat(F(2*m+1,m*(m+1))),D[m]);Aw=sum(nativeMu[k]*F(nativeLambda,m*(m+1))**k for k in range(15));coefficient=mul(eta,rat(Aw))
        lo,hi=bounds(coefficient)
        integer=int(down((lo+hi)/2, S)*S);assert integer>0;alpha[m]=integer
        radius=max(abs(F(integer,S)-lo),abs(hi-F(integer,S)))
        inputEnergy+=up(2*B/F(2*m+1)*F(D[m][1])*radius*radius,10**80)
    # Every entry is nonnegative; prove the entire dot sum fits int64.
    # Off-diagonal entries <=2/|n-m|=1/|n/2-m/2|, so their row
    # sum is <=2 H_N. Kernel floors can only decrease these entries.
    count=len(jobs);hn=sum(F(1,k) for k in range(1,count+1));maxDiag=max(bounds(v)[1] for v in diag.values())
    assert min(bounds(v)[0] for v in diag.values())>0
    intSumUpper=up(max(alpha.values())*Q*(maxDiag+2*hn))
    assert intSumUpper<2**63
    assert (2*O+1)*Q<2**63 and O*(O+L+1)<2**63
    ms=np.array(jobs,dtype=np.int64);av=np.array([alpha[m] for m in jobs],dtype=np.int64)
    inputSum=F(sum(alpha.values()),S);sumInt=sum(alpha.values())
    centers=[None]*(O//2+1);rounding=F(0);dotHashes=[None]*len(centers)
    degrees=list(range(0,O+1,2));degrees=degrees[::-1] if replay else degrees
    for n in degrees:
        den=np.abs(n-ms)*(n+ms+1);den[ms==n]=1
        kernels=((2*n+1)*Q)//den
        dlo,dhi=bounds(diag[n]);diagInteger=int(down(dlo,Q)*Q)
        kernels[ms==n]=diagInteger
        # Integer arithmetic only; positivity and the global sum guard
        # rule out overflow in every product and partial reduction.
        assert kernels.min()>=0
        dot=int(np.sum(kernels*av,dtype=np.int64));assert 0<=dot<=intSumUpper
        lo=F(dot,S*Q);hi=lo+inputSum/Q+F(alpha.get(n,0),S)*(dhi-dlo)
        coefficient=div((rat(lo)[0],rat(hi)[1]),D[n]);cl,ch=bounds(coefficient)
        center=down((cl+ch)/2,CENTER);radius=max(center-cl,ch-center)
        assert radius>=0
        centers[n//2]=str(int(center*CENTER));dotHashes[n//2]=str(dot)
        rounding+=up(2*B/F(2*n+1)*F(D[n][1])*radius*radius,10**80)
        if n%8192==0:print('RC190 exact fixed-point output',n,flush=True)
    lam=L*(L+1);rho=F(lam,(O+2)*(O+3));moments=[]
    for k in range(K+2):
        exact=F(sum(alpha[m]*(m*(m+1))**k for m in jobs),S*lam**k)
        center=down(exact,10**40);radius=exact-center
        moments.append(dict(order=k,lower=str(exact),upper=str(exact),center=str(center),radius=str(radius)))
    T=up(B/(F(D[O][0])*(O-1)*O));inputEtaTail=up(B/(F(D[L][0])*(L-1)*L))
    first=L+2;inputAw=sum(nativeMu[k]*F(nativeLambda,first*(first+1))**k for k in range(15));inputTail=up(inputEtaTail*inputAw*inputAw)
    remainder=up(T*(F(moments[K+1]['upper'])*rho**(K+1)/(1-rho))**2,10**80)
    momentRound=up(T*sum(F(moments[k]['radius'])*rho**k for k in range(K+1))**2,10**80)
    endpointError=up(sqrtup(inputEnergy)+sqrtup(rounding)+sqrtup(momentRound)+sqrtup(remainder)+sqrtup(inputTail)/2)
    oldError=F(old['new_centered_Cw14_error_norm_upper']);assert endpointError<oldError
    # Extend the exact finite regular input and pay the entire omitted native
    # source by RC174's high-mode smoothing estimate, as in RC183.
    M=512;alphaRegular={n:g[n] for n in range(0,M+1,2)}
    prefixEnergy=sum(down(2*B/F(2*n+1)*F(D[n][0])*c*c) for n,c in alphaRegular.items())
    tailEnergy=up(F(old['native_D_energy_upper'])-prefixEnergy);assert tailEnergy>0
    firstRegular=M+2;Dfirst=sl+sum(F(1,n) for n in range(1,firstRegular+1))
    e=F(regular['e_upper']);p=F(regular['pi_upper']);r=F(789,125);I2=up(e*p*p/3);band=F(M+1)/(6*p*B)
    phi2=up(min(r*r,4*B*I2*up(F(11,12)**(2*(M+1)),10**80)+e*e/(band*band)))
    regularInputError=up(root(phi2*tailEnergy/(sl*Dfirst)))
    path=Path(__file__).with_name('validate_rpb108_rc179_focus_residual_canonical_action.py')
    src=path.read_text().split('\nif __name__==\'__main__\':')[0]
    assert src.count('K=192;N=768;J=')==1
    src=src.replace('K=192;N=768;J=','K=192;N=1536;J=')
    ns={'__file__':str(path)};exec(compile(src,'RC190 extended finite regular projection','exec'),ns)
    # Degree 512 has larger monomial coefficients. Use private directed
    # Decimal contexts, without changing any historical helper module.
    helper=Path(__file__).with_name('validate_rpb108_rc171_regular_legendre_projection.py')
    hsrc=helper.read_text().split('\nif __name__==\'__main__\':')[0]
    assert hsrc.count('prec=360')==2 and hsrc.count("TOL=D('1e-300')")==1
    hsrc=hsrc.replace('prec=360','prec=600').replace("TOL=D('1e-300')","TOL=D('1e-540')")
    private={};exec(compile(hsrc,'RC190 private higher-precision interval helpers','exec'),private)
    for key in ['ZERO','rat','add','sub','mul','scale','divide','div_int','endpoints','log_point']:ns[key]=private[key]
    ns['root']=lambda x,grid=10**600:root(x,grid)
    reg=ns['regular_action'](alphaRegular,regular,joint,replay)
    reg['interval_decimal_precision']=600
    reg['square_root_bound_grid_digits']=600
    regularError=up(regularInputError+F(reg['complete_D_inverse_regular_action_error_norm_upper']))
    assert regularError<F(old['complete_D_inverse_Rw14_error_norm_upper'])
    negativeEnergy=F(old['negative_r_finite_coefficient_error_D_energy_upper'])
    complete=up(endpointError+regularError+sqrtup(negativeEnergy));oldComplete=F(old['complete_canonical_w14_action_D_error_norm_upper']);assert complete<oldComplete
    energyLo=F(old['native_D_energy_lower']);relative=up(complete/(sqrtup(energyLo)-F(1,10**40)))
    carrier=dict(milestone='RC190-Cw14-carrier',source_prefix_degree=L,output_prefix_degree=O,finite_center_scale=str(CENTER),finite_Cw14_coefficient_center_numerators=centers,analytic_output_moments=moments,analytic_output_lambda=str(lam),centered_input_tail_first_even_degree=L+2,centered_input_tail_coefficient='1/2 times native w14',finite_polynomial_input_scale=str(S),finite_polynomial_input_coefficient_sha256=hashlib.sha256(json.dumps([str(alpha[m]) for m in sorted(alpha)],separators=(',',':')).encode()).hexdigest(),finite_kernel_dot_product_sha256=hashlib.sha256(json.dumps(dotHashes,separators=(',',':')).encode()).hexdigest(),whole_Cw14_error_norm_upper=str(endpointError),native_source_and_retained_canonical_carrier_sha256=hs[2])
    carrier['D_inverse_regular_polynomial']=reg['D_inverse_regular_polynomial']
    carrier['regular_input_degree']=M
    carrier['regular_output_degree']=1536
    carrier['complete_D_inverse_Rw14_error_norm_upper']=str(regularError)
    carrierBytes=(json.dumps(carrier,sort_keys=True,indent=2)+'\n').encode()
    result=dict(milestone='RC190',status='PASS: extended centered w14 endpoint carrier and improved complete canonical w14 action',starting_commit='88de98936b811f072ed76f7f9dae54948b0b8f4c',input_sha256=hs,aperture='11/10',actual_source_definition='unchanged native w14: stored g on even 0..4094, eta_n times 15 native moments on even n>=4096',native_source_carrier_sha256=hs[2],source_prefix_degree=L,output_prefix_degree=O,analytic_output_moment_count=K+1,finite_polynomial_input_scale=str(S),fixed_kernel_scale=str(Q),finite_output_center_scale=str(CENTER),input_coefficient_count=count,finite_output_coefficient_count=len(centers),integer_dot_product_upper=str(intSumUpper),integer_arithmetic_overflow_ruled_out=True,no_floating_point_arithmetic_used=True,finite_input_quantization_D_energy_upper=str(inputEnergy),finite_action_interval_and_center_rounding_D_energy_upper=str(rounding),input_eta_tail_D_energy_upper=str(inputEtaTail),native_input_tail_moment_amplitude_upper=str(inputAw),input_w14_tail_D_energy_upper=str(inputTail),centered_input_tail_squared_error_upper=str(inputTail/4),output_moment_rounding_D_energy_upper=str(momentRound),output_geometric_remainder_D_energy_upper=str(remainder),common_eta_output_tail_D_energy_upper=str(T),output_geometric_ratio_upper=str(rho),new_centered_Cw14_error_norm_upper=str(endpointError),previous_same_source_centered_Cw14_error_norm_upper=str(oldError),same_source_endpoint_error_improvement_factor_lower=str(down(oldError/endpointError)),canonical_w14_source_form='native w14 + RC190 Cw14 trial + retained RC183 negative-r finite correction and exact negative-r native tail + retained RC183 regular polynomial',complete_canonical_w14_action_D_error_norm_upper=str(complete),previous_same_source_canonical_w14_error_norm_upper=str(oldComplete),complete_canonical_w14_relative_D_norm_error_upper=str(relative),inherited_regular_w14_error_norm_upper=str(regularError),inherited_negative_r_finite_coefficient_error_D_energy_upper=str(negativeEnergy),materialized_endpoint_carrier_sha256=hashlib.sha256(carrierBytes).hexdigest(),full_input_output_tails_paid=True,endpoint_cutoff_commutation_assumed=False,canonical_operator_and_native_w14_source_unchanged=True,new_inverse_response_evaluated=False,previous_RC189_inverse_width_upper=prior['relative_inverse_width_upper'],canonical_half_Gram_inverse_width_gate_closed=False,native_seven_source_frame_changed=False,Stage_I_closed=False,original_Weil_or_augmented_actions_performed=False,RH=False,F4=False,Lean=False,next_cursor='tighten the retained regular w14 action error if needed, then recompute mixed rows and the same five-source inverse with the refined psi and w14 carriers')
    result.update(canonical_w14_source_form='native w14 + RC190 Cw14 trial + retained RC183 negative-r finite correction and exact negative-r native tail + RC190 degree-1536 regular polynomial',inherited_regular_w14_error_norm_upper=old['complete_D_inverse_Rw14_error_norm_upper'],complete_D_inverse_Rw14_error_norm_upper=str(regularError),regular_action=reg,retained_regular_input_degree=M,omitted_regular_input_D_energy_upper=str(tailEnergy),regular_input_tail_action_D_error_norm_upper=str(regularInputError),regular_input_tail_smoothing_squared_factor_upper=str(phi2),native_D_energy_lower=old['native_D_energy_lower'],native_D_energy_upper=old['native_D_energy_upper'])
    result.pop('no_floating_point_arithmetic_used')
    result['endpoint_no_floating_point_arithmetic_used']=True
    result['regular_uses_directed_decimal_intervals']=True
    print('RC190 endpoint error',float(endpointError),'regular error',float(regularError),'full canonical error',float(complete),'relative',float(relative),flush=True)
    return result,carrier
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--carrier-output',required=True);p.add_argument('--replay',action='store_true');args=p.parse_args();result,carrier=run(inputs(),args.replay)
    if args.replay:assert json.loads(Path(args.output).read_text())==result and json.loads(Path(args.carrier_output).read_text())==carrier
    else:Path(args.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n');Path(args.carrier_output).write_text(json.dumps(carrier,sort_keys=True,indent=2)+'\n')
    print('RC190 PASS: larger paid centered native w14 action carrier')
