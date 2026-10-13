"""RC216: complete native t10 canonical action with all omitted inputs paid."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,div,bounds,up,down,sqrtup
from validate_rpb108_rc176_f0_regular_output_carrier import root,lower_root
from validate_rpb108_rc179_focus_residual_canonical_action import regular_action
import validate_rpb108_rc210_collective_regular_input_tail as prev
ROOT=Path(__file__).resolve().parents[1]
PINS={k:v for k,v in prev.PINS.items() if any(n in k for n in ['129_four','170_poisson','183_materialized','174_regular','121_diagonal'])}
PINS.update({'certificates/rpb108_rc132_balanced_action_shared_covariance.json': '035eac34848eb3f8f0a2d65424340050936e980c', 'certificates/rpb108_rc136_seven_vector_joint_matrices.json': '84ed91819c32053ae78caf340758e7d0c07a9568'})
HELPER_PINS=dict(prev.HELPER_PINS)
HELPER_PINS.update({'scripts/validate_rpb108_rc127_enriched_even_endpoint_action.py': 'd5d82bf70c1a178f0fe1da61f27b8623e42ed361', 'scripts/validate_rpb108_rc171_regular_legendre_projection.py': '29a8ab157b16d262a78abe9bf9348a271a34fff5', 'scripts/validate_rpb108_rc176_f0_regular_output_carrier.py': '38fa42607e423de666ffbb4ebc0f703c7c0fe1d7', 'scripts/validate_rpb108_rc179_focus_residual_canonical_action.py': '012cc045537e82d78a51299ffb9c5356a488ac6a', 'scripts/validate_rpb108_rc210_collective_regular_input_tail.py': '03dae85f568ea15d8a0a64482eda41bf0b42bccc'})
PINS['certificates/rpb108_rc135_common_response_capture.json']='2de31504cf1bc7645d3dc850f147ad6bb0582cfb'
PINS['certificates/rpb108_rc212_native_t10_canonical_action.json']='442f9963189a32fa8185daf5558e0673753ed0f1'
PINS['certificates/rpb108_rc215_correlated_common_error_preflight.json']='31338be9ef05d8677f2325a6f2fbb708f94fb812'
M=4094;RINPUT=512;O=8190

def run(reverse=False):
    for path,sha in HELPER_PINS.items():assert prev.prev.prev.blob((ROOT/path).read_bytes())==sha,(path,'helper Git blob mismatch')
    data={}
    for path,sha in PINS.items():
        b=(ROOT/path).read_bytes();assert prev.prev.prev.blob(b)==sha,(path,'input Git blob mismatch');data[path]=json.loads(b)
    get=lambda n:data['certificates/rpb108_rc'+n+'.json']
    balanced=get('132_balanced_action_shared_covariance');joint=get('129_four_vector_joint_moment');full=get('136_seven_vector_joint_matrices');source=get('183_materialized_w14_canonical_carrier');regular=get('170_poisson_regular_action');metric=get('121_diagonal_metric_equivalence')
    assert full['joint_family'][6]=='t10_common_response' and full['seven_vector_independence_certified']
    assert metric['endpoint_form_bound']=='0 <= h <= J + 2 log(2) I <= D'
    sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B)
    s=(rat(sl)[0],rat(sh)[1]);log=(rat(1-F(joint['actual_endpoint_pairing_entry_upper'][0][0])/(2*B))[0],rat(1-F(joint['actual_endpoint_pairing_entry_lower'][0][0])/(2*B))[1])
    H=[Z]
    for n in range(1,2*8190+3):H.append(plus(H[-1],rat(F(1,n))))
    D={n:plus(H[n],s) for n in range(0,8193,2)}
    diag=lambda n:minus(plus(minus(mul(rat(2),H[2*n]),mul(rat(2),H[n])),rat(F(1,2*n+1))),log)
    g={2*i:F(c) for i,c in enumerate(source['native_w14_finite_coefficient_centers'])};alpha=F(balanced['alpha']);b={};rows=[]
    for n in range(0,4095,2):
        value=rat(g[n])
        if n>=990:value=minus(value,mul(rat(alpha),div(rat(F(2*n+1,n*(n+1))),D[n])))
        lo,hi=bounds(value);assert lo>0;b[n]=value;rows.append(dict(degree=n,lower=str(lo),upper=str(hi)))
    digest=hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest();assert digest==balanced['balanced_source_interval_sha256']
    z={};zPayload=[];jobs=sorted(b,reverse=reverse)
    for n in range(0,8191,2):
        value=Z
        for m in jobs:
            entry=diag(n) if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
            value=plus(value,mul(entry,b[m]))
        lo,hi=bounds(div(value,D[n]));cc=down((lo+hi)/2);rad=max(cc-lo,hi-cc);assert cc>0
        z[n]=cc;zPayload.append(dict(degree=n,center=str(cc),radius=str(rad)))
        if n%1024==0:print('RC216 full z_b6 input reconstruction',n,flush=True)
    zhash=hashlib.sha256(json.dumps(zPayload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert zhash==balanced['finite_output_polynomial_center_radius_sha256']
    v={2*i:F(c) for i,c in enumerate(source['Cg_finite_coefficient_centers'])};assert len(v)==len(z)==4096
    common={n:(v[n]+z[n])/2 for n in z};capture=get('135_common_response_capture')
    commonRows=[dict(degree=n,center=str(common[n])) for n in sorted(common)]
    commonHash=hashlib.sha256(json.dumps(commonRows,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert commonHash==capture['common_finite_source_coefficient_sha256']
    native={};prefixRows=[]
    for n in range(0,M+1,2):
        value=Z
        for m in sorted(common,reverse=reverse):
            entry=diag(n) if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
            value=plus(value,mul(entry,rat(common[m])))
        lo,hi=bounds(div(value,D[n]));cc=down((lo+hi)/2);rad=max(cc-lo,hi-cc);assert cc>0
        native[n]=cc;prefixRows.append(dict(degree=n,center=str(cc),generator_radius=str(rad)))
        if n%128==0:print('RC216 native t10 prefix',n,flush=True)
    # These are exactly the pinned RC135 midpoint/floor source coefficients,
    # not a new approximation to the native t10 source.
    inherited=get('212_native_t10_canonical_action');assert prefixRows[:len(inherited['native_source_low_prefix'])]==inherited['native_source_low_prefix']
    energyLo=F(full['actual_D_Gram_entry_lower'][6][6]);energyHi=F(full['actual_D_Gram_entry_upper'][6][6]);assert 0<energyLo<=energyHi
    prefixLo=sum(down(2*B/F(2*n+1)*F(D[n][0])*cc*cc) for n,cc in native.items());omitted=up(energyHi-prefixLo);assert 0<omitted<energyHi
    endpoint=[];roundEnergy=F(0)
    for n in (range(O,-1,-2) if reverse else range(0,O+1,2)):
        value=Z
        for m in sorted(native,reverse=reverse):
            entry=diag(n) if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
            value=plus(value,mul(entry,rat(native[m])))
        lo,hi=bounds(div(value,D[n]));cc=down((lo+hi)/2);rad=max(cc-lo,hi-cc)
        endpoint.append(dict(degree=n,coefficient_center=str(cc),coefficient_radius=str(rad)));roundEnergy+=up(2*B/F(2*n+1)*F(D[n][1])*rad*rad)
        if n%1024==0:print('RC216 t10 endpoint action',n,flush=True)
    endpoint.sort(key=lambda r:r['degree']);lam=M*(M+1);rho=F(lam,(O+2)*(O+3));K=24
    moments=[sum(native[m]*F(m*(m+1),lam)**k for m in sorted(native,reverse=reverse)) for k in range(K+2)]
    T=up(B/(F(D[O][0])*(O-1)*O));remainder=up(root(T)*moments[K+1]*rho**(K+1)/(1-rho))
    endpointError=up(root(roundEnergy)+remainder+root(omitted)/2)
    # The complete negative-r multiplier is exact on the actual native source.
    # Regular projection is explicit; the entire omitted input remains paid.
    r=F(789,125);low={n:cc for n,cc in native.items() if n<=RINPUT}
    # Reuse the pinned RC179 analytic projection at the precision/output
    # cutoffs already used for degree-512 input in RC197.
    path=ROOT/'scripts/validate_rpb108_rc179_focus_residual_canonical_action.py'
    src=path.read_text().split("\nif __name__=='__main__':")[0]
    assert src.count('K=192;N=768;J=')==1
    src=src.replace('K=192;N=768;J=','K=192;N=1536;J=')
    ns={'__file__':str(path)};exec(compile(src,'RC216 finite regular action','exec'),ns)
    hsrc=(ROOT/'scripts/validate_rpb108_rc171_regular_legendre_projection.py').read_text().split("\nif __name__=='__main__':")[0]
    assert hsrc.count('prec=360')==2 and hsrc.count("TOL=D('1e-300')")==1
    hsrc=hsrc.replace('prec=360','prec=600').replace("TOL=D('1e-300')","TOL=D('1e-540')")
    private={};exec(compile(hsrc,'RC216 private directed interval helpers','exec'),private)
    for key in ['ZERO','rat','add','sub','mul','scale','divide','div_int','endpoints','log_point']:ns[key]=private[key]
    ns['root']=lambda x,grid=10**600:root(x,grid)
    reg=ns['regular_action'](low,regular,joint,reverse)
    regPrefix=sum(down(2*B/F(2*n+1)*F(D[n][0])*cc*cc) for n,cc in low.items());regTail=up(energyHi-regPrefix);assert regTail>0
    e=F(regular['e_upper']);p=F(regular['pi_upper']);I2=up(e*p*p/3);band=F(RINPUT+1)/(6*p*B)
    phi=up(min(r*r,4*B*I2*up(F(11,12)**(2*(RINPUT+1)),10**80)+e*e/(band*band)))
    inputError=up(root(phi*regTail/(sl*F(D[RINPUT+2][0]))));regularError=up(inputError+F(reg['complete_D_inverse_regular_action_error_norm_upper']))
    complete=up(endpointError+regularError);relative=up(complete/lower_root(energyLo))
    preflight=get('215_correlated_common_error_preflight');target=F(preflight['concrete_future_t10_error_target'])
    factors=[(F(c['quadratic'])*complete*complete+F(c['linear'])*complete+F(c['constant']),c['mask']) for c in preflight['signed_t_error_budget_quadratics']]
    worst,mask=max(factors,key=lambda c:(c[0],-c[1]));factorUpper=up(worst,10**6)
    assert complete<=target and factorUpper<F(1,2)
    print('RC216 full error / target / correlated factor',float(complete),float(target),float(factorUpper),flush=True)
    return dict(milestone='RC216',starting_commit='88867e956e449cc805f2bf4f8497cbe7398d83a4',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,native_source='unchanged t10: RC135 finite center polynomial through 16382 and its selected order-10 analytic carrier',full_z_finite_source_generator_sha256=zhash,full_z_finite_source_generator_hash_verified=True,full_common_input_source_sha256=commonHash,full_common_input_source_hash_verified=True,native_source_low_prefix_degree=M,native_source_low_prefix=prefixRows,balanced_input_interval_sha256=digest,balanced_input_intervals_reproduced=True,native_low_prefix_follows_exact_historical_midpoint_floor_generator=True,native_D_energy_lower=str(energyLo),native_D_energy_upper=str(energyHi),endpoint_input_prefix_degree=M,endpoint_output_prefix_degree=O,endpoint_action_polynomial=endpoint,endpoint_analytic_first_even_degree=O+2,endpoint_analytic_lambda=str(lam),endpoint_signed_moment_coefficients=list(map(str,moments[:K+1])),endpoint_geometric_ratio_upper=str(rho),endpoint_output_tail_remainder_D_norm_upper=str(remainder),endpoint_output_rounding_D_energy_upper=str(up(roundEnergy)),omitted_native_endpoint_input_D_energy_upper=str(omitted),centered_omitted_endpoint_input_coefficient='1/2 times actual native t10 coefficients for even degree >=4096',complete_endpoint_t10_D_error_norm_upper=str(endpointError),negative_r_multiplier='exact -r/D_n times the actual native t10 coefficient on every even degree; r=789/125',regular_input_prefix_degree=RINPUT,regular_action=reg,regular_omitted_input_D_energy_upper=str(regTail),regular_high_input_smoothing_squared_factor_upper=str(phi),regular_omitted_input_D_action_error_norm_upper=str(inputError),complete_D_inverse_Rt10_error_norm_upper=str(regularError),complete_canonical_t10_action_D_error_norm_upper=str(complete),complete_canonical_t10_relative_D_norm_error_upper=str(relative),represented_canonical_action='native t10 + finite/analytic endpoint prefix action + 1/2 omitted native endpoint input - r D^-1 native t10 + regular projection polynomial',complete_native_t10_canonical_action_certified=True,inherited_RC212_low_prefix_reproduced=True,regular_decimal_precision=600,regular_output_prefix_degree=1536,RC215_t10_error_target=str(target),RC215_t10_error_target_met=True,correlated_eight_source_action_error_factor_exact=str(worst),correlated_eight_source_action_error_factor_upper=str(factorUpper),correlated_eight_source_half_Gram_action_error_margin_lower=str(F(1,2)-factorUpper),correlated_eight_source_half_Gram_action_error_gate_passed=True,correlated_worst_signed_mask=mask,nominal_mixed_or_action_Gram_centers_assembled=False,whole_native_input_and_infinite_output_tails_paid=True,source_and_domain_definitions_unchanged=True,endpoint_cutoff_commutation_assumed=False,expanded_inverse_response_evaluated=False,accepted_RC210_six_source_inverse_width_unchanged='4361/10000',remaining_native_t10_canonical_action_open=False,Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC217: assemble compatible expanded nominal mixed/action/residual centers and certify the eight-source inverse gate; preserve accepted six-source result')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--replay',action='store_true');a=p.parse_args();result=run(a.replay)
    if a.replay:assert json.loads(a.output.read_text())==result
    else:a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC216 PASS: complete native t10 action, D-error',result['complete_canonical_t10_action_D_error_norm_upper'])
