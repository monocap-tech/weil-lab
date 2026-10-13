"""RC209: exact parameter-family barrier for RC208's coupled payments.
This bounds method-generated enclosure widths, not actual inverse uncertainty.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,json
import validate_rpb108_rc208_coupled_action_error_inverse as prev
from validate_rpb108_rc177_three_source_canonical_action_gram import mat,scale
from validate_rpb108_rc129_four_vector_joint_moment import cong,add
ROOT=Path(__file__).resolve().parents[1]
PINS=dict(prev.PINS)
PINS['certificates/rpb108_rc208_coupled_action_error_inverse.json']='223949fb0bda706ea6a70c001a8a7a3072518cdb'
PINS['certificates/rpb108_rc201_refined_v10_six_source_inverse.json']='cf224ee3495e23376bff696ee0bac9c81ff9cca7'
HELPER_PINS=dict(prev.HELPER_PINS)
HELPER_PINS['scripts/validate_rpb108_rc208_coupled_action_error_inverse.py']='c48293c69950c40bd1b66d0cb7572bce2c5bf967'
PROBE=['427/125000','-15419/1000000','84697/500000','-1','-600677/1000000','315051/500000']
GRID=10**30

def sqrt_lower(x):
    assert x>=0
    r=F(isqrt(x.numerator*GRID*GRID//x.denominator),GRID)
    assert r*r<=x<(r+F(1,GRID))**2
    return r

def run(reverse=False,probe=None):
    for path,sha in HELPER_PINS.items():assert prev.prev.prev.blob((ROOT/path).read_bytes())==sha,(path,'helper Git blob mismatch')
    data={}
    for path,sha in PINS.items():
        raw=(ROOT/path).read_bytes();assert prev.prev.prev.blob(raw)==sha,(path,'input Git blob mismatch');data[path]=json.loads(raw)
    base=data['certificates/rpb108_rc203_residual_enriched_six_source_inverse.json'];latest=data['certificates/rpb108_rc208_coupled_action_error_inverse.json'];metric=data['certificates/rpb108_rc121_diagonal_metric_equivalence.json'];trial=base['selected_enclosure']
    assert base['selected_trial']=='least_residual' and latest['relative_inverse_width_upper']=='74677/125000'
    x=list(map(F,PROBE if probe is None else probe));assert len(x)==6
    order=list(range(6));raw_order=list(range(8))
    if reverse:order.reverse();raw_order.reverse()
    q=lambda A:sum(x[i]*A[i][j]*x[j] for i in order for j in order)
    G=mat(base,'source_D_Gram_lower');GH=mat(base,'source_D_Gram_upper');g=q(G);assert g>0,'positive source energy required'
    ctx=prev.prev.prev.context(base,trial);Y=mat(trial,'trial_basis_coefficients');keep=[0,1,2,3,4,6];J=[[F(i==keep[j])-Y[i][j] for j in range(6)] for i in range(8)]
    SUhi=scale(F(1,2),add(add(GH,ctx['UG']),cong(J,mat(base,'raw_trial_D_Gram_Loewner_lower')),-1));Xhi=add(ctx['baseHi'],SUhi,-1)
    assert ser_matrix(Xhi)==latest['finite_source_residual_cross_upper']
    a=F(metric['actual_canonical_diagonal_metric_lower']);assert 0<a<=2
    eps=list(map(F,base['individual_raw_trial_action_error_norm_upper']));assert min(eps)>=0
    e_tri=sum(eps[k]*abs(sum(Y[k][j]*x[j] for j in order)) for k in raw_order)**2;e_signed=prev.prev.BETA*g;e=min(e_tri,e_signed)
    u,n,nlo,ut,rt,xc=[q(A) for A in [ctx['UG'],ctx['Nhi'],ctx['Nlo'],ctx['Utail'],ctx['Rtail'],Xhi]];assert min(u,n,nlo,ut,rt,e)>=0
    tail=sqrt_lower(ut*rt);c=2/a
    wL=u+n+2*xc+2*tail;wU=u+c*c*n+2*c*xc+2*c*tail;assert min(wL,wU)>=0
    lower_cross=sqrt_lower(wL*e);upper_cross=sqrt_lower(wU*e)
    refined_lower_ceiling=q(ctx['baseLo'])+nlo/2-tail-lower_cross+e/2
    refined_upper_floor=q(ctx['baseHi'])+n/a+tail+upper_cross+e/a
    lowers=[dict(label='all_coupled_lower_parameters',value=refined_lower_ceiling)];uppers=[dict(label='all_coupled_upper_parameters',value=refined_upper_floor)]
    filenames={201:'refined_v10_six_source_inverse',203:'residual_enriched_six_source_inverse',205:'signed_error_inverse',206:'directional_error_inverse',208:'coupled_action_error_inverse'}
    nums=list(filenames)
    if reverse:nums.reverse()
    for number in nums:
        d=data[f'certificates/rpb108_rc{number}_{filenames[number]}.json']
        for s in d.get('evaluated_inverse_trials',[d['selected_enclosure']]):
            label=f'RC{number}_'+s.get('trial',d.get('selected_trial','selected'))
            lowers.append(dict(label=label,value=q(mat(s,'canonical_inverse_response_lower'))));uppers.append(dict(label=label,value=q(mat(s,'canonical_inverse_response_upper'))))
    lowers.append(dict(label='structural',value=g/2));uppers.append(dict(label='structural',value=q(GH)/a))
    bestL=max(lowers,key=lambda z:(z['value'],z['label']));bestH=min(uppers,key=lambda z:(z['value'],z['label']));gap=bestH['value']-bestL['value'];ratio=gap/g
    certified=F(ratio.numerator*10**6//ratio.denominator,10**6);assert certified<=ratio and certified>F(1,2)
    controls=[]
    for lo in sorted(lowers,key=lambda z:z['label']):
        for hi in sorted(uppers,key=lambda z:z['label']):
            assert hi['value']-lo['value']>g/2
            controls.append(dict(lower=lo['label'],upper=hi['label'],gate_probe_strictly_negative=True))
    return dict(milestone='RC209',starting_commit='b748b2dba7e69bd1f8906d4984139b43cd8deaac',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,probe_coefficients=list(map(str,x)),probe_source_D_energy=str(g),minimum_error_majorant_probe_energy=str(e),triangle_error_majorant_probe_floor=str(e_tri),signed_error_majorant_probe_energy=str(e_signed),source_trial_probe_energy_upper=str(u),nominal_residual_probe_energy_upper=str(n),nominal_residual_probe_energy_lower=str(nlo),source_tail_probe_energy_upper=str(ut),residual_tail_probe_energy_upper=str(rt),finite_source_residual_cross_probe_upper=str(xc),tail_pairing_payment_lower=str(tail),coupled_lower_vector_Gram_probe_floor=str(wL),coupled_upper_vector_Gram_probe_floor=str(wU),lower_cross_payment_sqrt_lower=str(lower_cross),upper_cross_payment_sqrt_lower=str(upper_cross),square_root_grid=GRID,all_positive_triangle_weights_covered=True,all_convex_triangle_signed_mixes_covered=True,all_coupled_parameters_in_stated_range_covered=True,lower_theta_range='0 < theta_lower <= 1/2',selected_lower_probe_ceiling=str(bestL['value']),selected_lower_probe_ceiling_label=bestL['label'],selected_upper_probe_floor=str(bestH['value']),selected_upper_probe_floor_label=bestH['label'],coupled_scheme_inverse_width_lower=str(certified),gate_rejection_margin_lower=str(certified-F(1,2)),checked_endpoint_pair_families=controls,latest_certified_inverse_width_upper_unchanged=latest['relative_inverse_width_upper'],canonical_half_Gram_inverse_width_gate_passed=False,scope='fixed RC203 Y and full carrier/nominal/cross/tail bounds; RC208 coupled formula with diagonal weighted triangle/convex signed error majorants and listed inherited/structural endpoints',actual_operator_obstruction_claimed=False,other_error_correlations_or_new_carriers_ruled_out=False,Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC210: change complete nominal residual/cross-tail or action-error data, or certify a changed trial; stop parameter-only passes in the fixed coupled family')

def ser_matrix(A):return [[str(x) for x in row] for row in A]

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--replay',action='store_true');args=p.parse_args();result=run(args.replay)
    if args.replay:assert json.loads(args.output.read_text())==result
    else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC209 PASS: coupled-method width lower',result['coupled_scheme_inverse_width_lower'],'half-Gram gate impossible within stated scope')
