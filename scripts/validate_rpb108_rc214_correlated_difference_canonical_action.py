"""RC214: complete correlated difference canonical action with all omitted inputs paid."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,div,bounds,up,down
from validate_rpb108_rc176_f0_regular_output_carrier import root,lower_root
from validate_rpb108_rc179_focus_residual_canonical_action import regular_action
import validate_rpb108_rc210_collective_regular_input_tail as prev
ROOT=Path(__file__).resolve().parents[1]
PINS={k:v for k,v in prev.PINS.items() if any(n in k for n in ['129_four','170_poisson','183_materialized','174_regular','121_diagonal'])}
PINS.update({'certificates/rpb108_rc132_balanced_action_shared_covariance.json': '035eac34848eb3f8f0a2d65424340050936e980c', 'certificates/rpb108_rc136_seven_vector_joint_matrices.json': '84ed91819c32053ae78caf340758e7d0c07a9568'})
HELPER_PINS=dict(prev.HELPER_PINS)
HELPER_PINS.update({'scripts/validate_rpb108_rc127_enriched_even_endpoint_action.py': 'd5d82bf70c1a178f0fe1da61f27b8623e42ed361', 'scripts/validate_rpb108_rc171_regular_legendre_projection.py': '29a8ab157b16d262a78abe9bf9348a271a34fff5', 'scripts/validate_rpb108_rc176_f0_regular_output_carrier.py': '38fa42607e423de666ffbb4ebc0f703c7c0fe1d7', 'scripts/validate_rpb108_rc179_focus_residual_canonical_action.py': '012cc045537e82d78a51299ffb9c5356a488ac6a', 'scripts/validate_rpb108_rc210_collective_regular_input_tail.py': '03dae85f568ea15d8a0a64482eda41bf0b42bccc'})
PINS['certificates/rpb108_rc134_correlated_six_input_covariance.json']='451dd35ea6af09b6d307b39f6cd7156ce92307c3'
PINS['certificates/rpb108_rc153_correlated_difference_action.json']='d4481915a84ec33f349d6f95e4da8f0b7efdc232'
PINS['certificates/rpb108_rc213_eight_source_error_interface.json']='23aaa6e712fca038e87603471f59c08066d6a0a9'
PINS['certificates/rpb108_rc203_residual_enriched_six_source_inverse.json']='5d321b659367ba459682b557b12ef63451f63e49'
M=4094;RINPUT=128;O=8190

def run(reverse=False):
    for path,sha in HELPER_PINS.items():assert prev.prev.prev.blob((ROOT/path).read_bytes())==sha,(path,'helper Git blob mismatch')
    data={}
    for path,sha in PINS.items():
        b=(ROOT/path).read_bytes();assert prev.prev.prev.blob(b)==sha,(path,'input Git blob mismatch');data[path]=json.loads(b)
    get=lambda n:data['certificates/rpb108_rc'+n+'.json']
    balanced=get('132_balanced_action_shared_covariance');joint=get('129_four_vector_joint_moment');full=get('136_seven_vector_joint_matrices');source=get('183_materialized_w14_canonical_carrier');regular=get('170_poisson_regular_action');metric=get('121_diagonal_metric_equivalence')
    assert full['joint_family'][4:6]==['v10','z_b6'] and full['seven_vector_independence_certified']
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
        if n%1024==0:print('RC214 full z_b6 input reconstruction',n,flush=True)
    zhash=hashlib.sha256(json.dumps(zPayload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert zhash==balanced['finite_output_polynomial_center_radius_sha256']
    v={2*i:F(c) for i,c in enumerate(source['Cg_finite_coefficient_centers'])};assert len(v)==len(z)==4096
    native={n:z[n]-v[n] for n in z};assert all(c<0 for c in native.values())
    rows=[dict(degree=n,center=str(native[n])) for n in sorted(native)]
    nativeHash=hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    old=get('153_correlated_difference_action');cov=get('134_correlated_six_input_covariance')
    assert nativeHash==old['reconstructed_finite_delta_center_sha256']
    energyLo=sum(down(2*B/F(2*n+1)*F(D[n][0])*cc*cc) for n,cc in native.items())
    finiteHi=sum(up(2*B/F(2*n+1)*F(D[n][1])*cc*cc,10**100) for n,cc in native.items())
    assert finiteHi==F(cov['z_minus_v_finite_source_D_energy_upper'])
    energyHi=F(cov['z_minus_v_full_source_D_energy_upper']);assert 0<energyLo<=energyHi
    prefixRows=[dict(degree=n,center=str(native[n])) for n in sorted(native) if n<=M]
    prefixLo=sum(down(2*B/F(2*n+1)*F(D[n][0])*cc*cc) for n,cc in native.items() if n<=M)
    omitted=up(energyHi-prefixLo);assert 0<omitted<energyHi
    native={n:c for n,c in native.items() if n<=M}
    endpoint=[];roundEnergy=F(0)
    for n in (range(O,-1,-2) if reverse else range(0,O+1,2)):
        value=Z
        for m in sorted(native,reverse=reverse):
            entry=diag(n) if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
            value=plus(value,mul(entry,rat(-native[m])))
        lo,hi=bounds(div(value,D[n]));positive=down((lo+hi)/2);rad=max(positive-lo,hi-positive);cc=-positive
        endpoint.append(dict(degree=n,coefficient_center=str(cc),coefficient_radius=str(rad)));roundEnergy+=up(2*B/F(2*n+1)*F(D[n][1])*rad*rad)
        if n%1024==0:print('RC214 delta endpoint action',n,flush=True)
    endpoint.sort(key=lambda r:r['degree']);lam=M*(M+1);rho=F(lam,(O+2)*(O+3));K=24
    moments=[sum(native[m]*F(m*(m+1),lam)**k for m in sorted(native,reverse=reverse)) for k in range(K+2)]
    T=up(B/(F(D[O][0])*(O-1)*O));remainder=up(root(T)*abs(moments[K+1])*rho**(K+1)/(1-rho))
    endpointError=up(root(roundEnergy)+remainder+root(omitted)/2)
    # The complete negative-r multiplier is exact on the actual native source.
    # Regular projection is explicit; the entire omitted input remains paid.
    r=F(789,125);low={n:cc for n,cc in native.items() if n<=RINPUT}
    reg=regular_action(low,regular,joint,reverse)
    regPrefix=sum(down(2*B/F(2*n+1)*F(D[n][0])*cc*cc) for n,cc in low.items());regTail=up(energyHi-regPrefix);assert regTail>0
    e=F(regular['e_upper']);p=F(regular['pi_upper']);I2=up(e*p*p/3);band=F(RINPUT+1)/(6*p*B)
    phi=up(min(r*r,4*B*I2*up(F(11,12)**(2*(RINPUT+1)),10**80)+e*e/(band*band)))
    inputError=up(root(phi*regTail/(sl*F(D[RINPUT+2][0]))));regularError=up(inputError+F(reg['complete_D_inverse_regular_action_error_norm_upper']))
    complete=up(endpointError+regularError);relative=up(complete/lower_root(energyLo))
    interface=get('213_eight_source_error_interface')
    assert interface['response_source_order'][4:6]==['v10','z_b6']
    vError=F(interface['complete_canonical_column_error_norm_upper'][4])
    assert vError==F(get('203_residual_enriched_six_source_inverse')['individual_raw_trial_action_error_norm_upper'][6])
    oldZError=F(interface['complete_canonical_column_error_norm_upper'][5])
    newZError=up(vError+complete)
    assert newZError<oldZError and complete*complete<energyLo/2
    newZRelative=up(newZError/lower_root(F(full['actual_D_Gram_entry_lower'][5][5])))
    return dict(milestone='RC214',starting_commit='4424d4573be099cc364d99bfa60f022fbedd112d',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,
        native_source='delta=z_b6-v10, unchanged native finite coefficients and combined selected analytic carriers',
        full_z_finite_source_generator_sha256=zhash,full_z_finite_source_generator_hash_verified=True,
        full_difference_source_sha256=nativeHash,full_difference_source_hash_verified=True,
        balanced_input_interval_sha256=digest,balanced_input_intervals_reproduced=True,
        native_source_low_prefix_degree=M,native_source_low_prefix=prefixRows,
        native_D_energy_lower=str(energyLo),native_D_energy_upper=str(energyHi),
        endpoint_input_prefix_degree=M,endpoint_output_prefix_degree=O,endpoint_action_polynomial=endpoint,
        endpoint_analytic_first_even_degree=O+2,endpoint_analytic_lambda=str(lam),endpoint_signed_moment_coefficients=list(map(str,moments[:K+1])),endpoint_geometric_ratio_upper=str(rho),
        endpoint_output_tail_remainder_D_norm_upper=str(remainder),endpoint_output_rounding_D_energy_upper=str(up(roundEnergy)),
        omitted_native_endpoint_input_D_energy_upper=str(omitted),centered_omitted_endpoint_input_coefficient='1/2 times actual native delta coefficients for even degree >=4096',
        complete_endpoint_delta_D_error_norm_upper=str(endpointError),negative_r_multiplier='exact -r/D_n times actual native delta on every even degree; r=789/125',
        regular_input_prefix_degree=RINPUT,regular_action=reg,regular_omitted_input_D_energy_upper=str(regTail),regular_high_input_smoothing_squared_factor_upper=str(phi),
        regular_omitted_input_D_action_error_norm_upper=str(inputError),complete_D_inverse_Rdelta_error_norm_upper=str(regularError),
        complete_canonical_delta_action_D_error_norm_upper=str(complete),complete_canonical_delta_relative_D_norm_error_upper=str(relative),
        represented_canonical_action='native delta + finite/analytic endpoint prefix action + 1/2 omitted native endpoint input - r D^-1 native delta + regular projection polynomial',
        inherited_v10_complete_canonical_action_error_norm_upper=str(vError),
        prior_independently_constructed_z_action_error_norm_upper=str(oldZError),
        rebuilt_correlated_z_action='pinned RC203 v10 canonical carrier plus RC214 delta canonical carrier',
        rebuilt_correlated_z_action_D_error_norm_upper=str(newZError),rebuilt_correlated_z_relative_D_norm_error_upper=str(newZRelative),
        correlated_error_identity='e_z=e_v+e_delta for the rebuilt z carrier; the old RC211 z carrier is not used in this identity',
        error_generator_order=['e_v','e_delta'],error_generator_to_v_z_matrix=[['1','0'],['1','1']],
        difference_direction_half_Gram_error_test_passed=True,
        complete_native_difference_canonical_action_certified=True,coefficients_combined_before_action_and_tail_payment=True,
        whole_native_input_and_infinite_output_tails_paid=True,source_and_domain_definitions_unchanged=True,endpoint_cutoff_commutation_assumed=False,
        expanded_inverse_response_evaluated=False,accepted_RC210_six_source_inverse_width_unchanged='4361/10000',Stage_I_closed=False,RH=False,F4=False,Lean=False,
        next_cursor='RC215: correlated common carrier and conditioned expanded action/residual assembly; preserve accepted six-source result')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--replay',action='store_true');a=p.parse_args();result=run(a.replay)
    if a.replay:assert json.loads(a.output.read_text())==result
    else:a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC214 PASS: complete correlated delta action, D-error',result['complete_canonical_delta_action_D_error_norm_upper'])
