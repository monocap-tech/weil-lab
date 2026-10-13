"""RC207: exact method barrier for fixed-trial scalar Young payment tuning.
This is not an obstruction to actual inverse positivity or to other enclosures.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,json
import validate_rpb108_rc206_directional_error_inverse as prev
from validate_rpb108_rc177_three_source_canonical_action_gram import mat,scale
ROOT=Path(__file__).resolve().parents[1]
PINS=dict(prev.PINS)
PINS['certificates/rpb108_rc206_directional_error_inverse.json']='2107f2138b113b4a3093b98429c9d55024ea54d4'
PINS['certificates/rpb108_rc201_refined_v10_six_source_inverse.json']='cf224ee3495e23376bff696ee0bac9c81ff9cca7'
HELPER_PINS=dict(prev.HELPER_PINS)
HELPER_PINS['scripts/validate_rpb108_rc206_directional_error_inverse.py']='7ada815599b8d2b607aed030e38b8daa01801496'
PROBE=['1619/500000','-14633/1000000','160653/1000000','-1','-569149/1000000','596627/1000000']
GRID=10**30

def sqrt_lower(x):
    assert x>=0
    r=F(isqrt(x.numerator*GRID*GRID//x.denominator),GRID)
    assert r*r<=x<(r+F(1,GRID))**2
    return r

def run(reverse=False,probe=None):
    for path,sha in HELPER_PINS.items():assert prev.prev.blob((ROOT/path).read_bytes())==sha,(path,'helper Git blob mismatch')
    data={}
    for path,sha in PINS.items():
        raw=(ROOT/path).read_bytes();assert prev.prev.blob(raw)==sha,(path,'input Git blob mismatch');data[path]=json.loads(raw)
    base=data['certificates/rpb108_rc203_residual_enriched_six_source_inverse.json'];prior=data['certificates/rpb108_rc206_directional_error_inverse.json'];metric=data['certificates/rpb108_rc121_diagonal_metric_equivalence.json']
    assert base['selected_trial']=='least_residual' and prior['relative_inverse_width_upper']=='21003/31250'
    x=list(map(F,PROBE if probe is None else probe));assert len(x)==6
    order=list(range(6));raw_order=list(range(8))
    if reverse:order.reverse();raw_order.reverse()
    q=lambda A:sum(x[i]*A[i][j]*x[j] for i in order for j in order)
    G=mat(base,'source_D_Gram_lower');g=q(G);assert g>0,'probe must have positive source Gram energy'
    c=prev.prev.context(base,base['selected_enclosure']);a=F(metric['actual_canonical_diagonal_metric_lower']);assert a>0
    Y=mat(base['selected_enclosure'],'trial_basis_coefficients');eps=list(map(F,base['individual_raw_trial_action_error_norm_upper']));assert min(eps)>=0
    absolute_error=sum(eps[k]*abs(sum(Y[k][j]*x[j] for j in order)) for k in raw_order)
    e_triangle=absolute_error**2;e_signed=prev.BETA*g;e=min(e_triangle,e_signed)
    u,n,ut,rt,nlo=[q(c[k]) for k in ['UG','Nhi','Utail','Rtail','Nlo']];assert min(u,n,ut,rt,nlo,e)>=0
    roots=dict(action=sqrt_lower(u*e),tail=sqrt_lower(ut*rt),residual=sqrt_lower(n*e))
    payment_lower=roots['action']+roots['tail']
    residual_upper_payment_lower=(n+e+2*roots['residual'])/a
    refined_lower_ceiling=q(c['baseLo'])-payment_lower+nlo/2
    refined_upper_floor=q(c['baseHi'])+payment_lower+residual_upper_payment_lower
    lowers=[dict(label='all_refined_lower_parameters',value=refined_lower_ceiling)]
    uppers=[dict(label='all_refined_upper_parameters',value=refined_upper_floor)]
    filenames={201:'refined_v10_six_source_inverse',203:'residual_enriched_six_source_inverse',205:'signed_error_inverse',206:'directional_error_inverse'}
    nums=list(filenames)
    if reverse:nums.reverse()
    for number in nums:
        d=data[f'certificates/rpb108_rc{number}_{filenames[number]}.json']
        trials=d.get('evaluated_inverse_trials',[d['selected_enclosure']])
        for k,s in enumerate(trials):
            label=f'RC{number}_'+s.get('trial',d.get('selected_trial','selected'))
            lowers.append(dict(label=label,value=q(mat(s,'canonical_inverse_response_lower'))))
            uppers.append(dict(label=label,value=q(mat(s,'canonical_inverse_response_upper'))))
    lowers.append(dict(label='structural',value=g/2));uppers.append(dict(label='structural',value=q(mat(base,'source_D_Gram_upper'))/a))
    best_lower=max(lowers,key=lambda z:(z['value'],z['label']));best_upper=min(uppers,key=lambda z:(z['value'],z['label']))
    gap_lower=best_upper['value']-best_lower['value'];ratio=gap_lower/g
    certified=F(ratio.numerator*10**6//ratio.denominator,10**6)
    assert certified<=ratio and certified>F(1,2)
    controls=[]
    for lo in sorted(lowers,key=lambda z:z['label']):
        for hi in sorted(uppers,key=lambda z:z['label']):
            diff=hi['value']-lo['value'];assert diff>g/2
            controls.append(dict(lower=lo['label'],upper=hi['label'],gate_probe_strictly_negative=True))
    return dict(milestone='RC207',starting_commit='a23209ae4334772f81c35ad1838103749aa27d8e',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,probe_coefficients=list(map(str,x)),probe_source_D_energy=str(g),minimum_allowed_error_envelope_probe_energy=str(e),triangle_error_envelope_probe_floor=str(e_triangle),signed_error_envelope_probe_energy=str(e_signed),trial_source_probe_energy_upper=str(u),nominal_residual_probe_energy_upper=str(n),nominal_residual_probe_energy_lower=str(nlo),source_tail_probe_energy_upper=str(ut),residual_tail_probe_energy_upper=str(rt),exact_square_root_lowers={k:str(v) for k,v in roots.items()},square_root_grid=GRID,all_positive_scalar_Young_parameters_covered=True,all_positive_triangle_weights_covered=True,all_convex_triangle_signed_mixes_covered=True,all_residual_lower_sigma_in_zero_to_one_covered=True,selected_lower_probe_ceiling=str(best_lower['value']),selected_lower_probe_ceiling_label=best_lower['label'],selected_upper_probe_floor=str(best_upper['value']),selected_upper_probe_floor_label=best_upper['label'],fixed_scheme_inverse_width_lower=str(certified),gate_rejection_margin_lower=str(certified-F(1,2)),checked_endpoint_pair_families=controls,latest_certified_inverse_width_upper_unchanged=prior['relative_inverse_width_upper'],canonical_half_Gram_inverse_width_gate_passed=False,method_scope='RC203 fixed Y and carriers; RC205/206 scalar Young variational/residual formulas; positive weighted triangle and convex signed error majorants; listed inherited/structural endpoints',actual_operator_obstruction_claimed=False,all_possible_error_majorants_or_enclosures_ruled_out=False,Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC208: improve physical action/nominal residual or direct cross-tail data, or enrich Y with a newly certified complete action; stop parameter-only passes in this fixed payment scheme')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--replay',action='store_true');args=p.parse_args()
    result=run(args.replay)
    if args.replay:assert json.loads(args.output.read_text())==result
    else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC207 PASS: method-specific inverse-width lower',result['fixed_scheme_inverse_width_lower'],'half-Gram gate impossible within stated scope')
