"""RC147: exact attribution and necessary endpoint precision for narrow t10 witness."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import down,up
from validate_rpb108_rc129_four_vector_joint_moment import mm
from validate_rpb108_rc146_narrow_coordinate import run as rc146_run

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths]
    prior=json.loads(raw[0]);assert prior==rc146_run(paths[1:],replay)
    old=json.loads(raw[1]);frame=json.loads(raw[8]);joint=json.loads(raw[10])
    sign=json.loads(raw[5]);tail=json.loads(raw[4])
    assert [x['milestone'] for x in (prior,old,frame,joint,sign,tail)]==['RC146','RC145','RC138','RC136','RC141','RC142']
    def mat(d,k):return [[F(x) for x in row] for row in d[k]]
    S=mat(frame,'trial_source_matrix');D=mat(old,'trial_source_frame_coefficients')
    Y=mm(S,D);w=[F(x) for x in old['witness_mixture']]
    s=[sum(S[i][k]*w[k] for k in range(5)) for i in range(7)]
    y=[sum(Y[i][k]*w[k] for k in range(5)) for i in range(7)]
    h=[sum(D[i][k]*w[k] for k in range(5)) for i in range(5)]
    GL,GU=mat(joint,'actual_D_Gram_entry_lower'),mat(joint,'actual_D_Gram_entry_upper')
    HL,HU=mat(frame,'trial_frame_endpoint_entry_lower'),mat(frame,'trial_frame_endpoint_entry_upper')
    HL[3][3]=F(sign['new_common_endpoint_energy_lower']);HU[3][3]=F(tail['new_common_endpoint_energy_upper'])
    gpairs=[(i,j) for i in range(7) for j in range(7)]
    hpairs=[(i,j) for i in range(5) for j in range(i,5)]
    if replay:gpairs.reverse();hpairs.reverse()
    gramWidth=sum(abs(s[i]*y[j]+y[i]*s[j]-y[i]*y[j])*(GU[i][j]-GL[i][j]) for i,j in gpairs)
    charges={f'{i},{j}':(1 if i==j else 2)*abs(h[i]*h[j])*(HU[i][j]-HL[i][j]) for i,j in hpairs}
    endpointWidth=sum(charges.values());rawWidth=gramWidth+endpointWidth
    oldEntryWidth=F(prior['transformed_variational_entry_upper'][4][4])-F(prior['transformed_variational_entry_lower'][4][4])
    assert rawWidth<=oldEntryWidth<rawWidth+F(2,10**40)
    loewnerWidth=F(prior['transformed_variational_Loewner_upper'][4][4])-F(prior['transformed_variational_Loewner_lower'][4][4])
    residual=F(prior['transformed_full_residual_Gram_upper'][4][4])
    sourceHi=F(prior['transformed_source_Gram_upper'][4][4])
    inflation=loewnerWidth-oldEntryWidth
    assert inflation>=0 and loewnerWidth+residual>sourceHi/2
    tt=charges['4,4'];ut=charges['3,4'];uu=charges['3,3']
    # Even abolishing this one endpoint interval leaves the direct signed-entry
    # width plus paid residual above the half-source-energy threshold.
    afterTT=rawWidth-tt+residual
    excess=afterTT-sourceHi/2
    assert excess>0 and excess<ut
    # If all other charges stay fixed and the t10 diagonal is made exact,
    # at least this fraction of the common/t10 mixed charge must also go.
    requiredMixedFraction=excess/ut
    q=10**24
    def floor(x):return str(down(x,q))
    def ceil(x):return str(up(x,q))
    return dict(milestone='RC147',status='PASS: exact narrow-direction endpoint budget locates coupled precision obligation',
        starting_commit='e4dc634151d140ffae58e510f1cb3903f3e915d9',
        input_sha256=[hashlib.sha256(b).hexdigest() for b in raw],aperture='11/10',
        response_source_count=5,carrier_family_dimension=7,witness_mixture=list(map(str,w)),
        witness_frame_coefficients=list(map(str,h)),
        signed_D_Gram_interval_width_upper=ceil(gramWidth),
        signed_endpoint_interval_width_upper=ceil(endpointWidth),
        endpoint_pair_interval_charges_upper={k:ceil(v) for k,v in sorted(charges.items())},
        direct_signed_entry_width_lower=floor(rawWidth),
        actual_entry_rounding_inflation_upper=ceil(oldEntryWidth-rawWidth),
        entry_to_Loewner_width_inflation_upper=ceil(inflation),
        paid_residual_narrow_upper=ceil(residual),
        t10_diagonal_charge_lower=floor(tt),common_t10_mixed_charge_lower=floor(ut),
        common_diagonal_charge_lower=floor(uu),
        source_energy_upper=ceil(sourceHi),half_source_energy_upper=ceil(sourceHi/2),
        direct_plus_residual_after_exact_t10_diagonal_lower=floor(afterTT),
        remaining_excess_after_exact_t10_diagonal_lower=floor(excess),
        necessary_common_t10_charge_reduction_fraction_lower=floor(requiredMixedFraction),
        conditional_precision_statement='With all other direct signed-entry and residual charges fixed, zero t10 diagonal interval still fails half-Gram; the common/t10 mixed charge must shrink by more than the stated fraction.',
        no_intrinsic_operator_obstruction_claimed=True,required_Stage_I_matrix_tolerance_specified=False,
        original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,
        RH=False,F4=False,Lean=False,
        next_cursor='derive correlated common/t10 endpoint interval or exact combined endpoint energy for the narrow frame vector')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=15)
    a=p.parse_args();result=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==result
    else:Path(a.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC147 PASS: narrow endpoint precision budget')
