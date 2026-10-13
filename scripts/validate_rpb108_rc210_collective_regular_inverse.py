"""RC210: transport the collective regular-tail bound through coupled inverse."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json
import validate_rpb108_rc206_directional_error_inverse as prev
import validate_rpb108_rc210_collective_regular_input_tail as tail210
from validate_rpb108_rc127_enriched_even_endpoint_action import psd,ser
from validate_rpb108_rc129_four_vector_joint_moment import cong,add
from validate_rpb108_rc177_three_source_canonical_action_gram import mat,scale,width
ROOT=Path(__file__).resolve().parents[1]
PINS=dict(prev.PINS)
PINS['certificates/rpb108_rc206_directional_error_inverse.json']='2107f2138b113b4a3093b98429c9d55024ea54d4'
PINS['certificates/rpb108_rc208_coupled_action_error_inverse.json']='223949fb0bda706ea6a70c001a8a7a3072518cdb'
PINS['certificates/rpb108_rc210_collective_regular_input_tail.json']='7079034c7c8f130868dfb8e32bcf7b4d9524ef2a'
HELPER_PINS=dict(prev.HELPER_PINS)
HELPER_PINS['scripts/validate_rpb108_rc206_directional_error_inverse.py']='7ada815599b8d2b607aed030e38b8daa01801496'
HELPER_PINS['scripts/validate_rpb108_rc210_collective_regular_input_tail.py']='03dae85f568ea15d8a0a64482eda41bf0b42bccc'

DEFAULT_PROPOSAL={'action_lower_theta': '1980731251/500000000000', 'action_upper_theta': '2785371823/1000000000000', 'tail_variational_theta': '15151655169/15625000000', 'tail_cross_theta': '19394146537/20000000000'}

def run(proposal,reverse=False):
    for path,sha in HELPER_PINS.items():assert prev.prev.blob((ROOT/path).read_bytes())==sha,(path,'helper Git blob mismatch')
    data={}
    for path,sha in PINS.items():
        raw=(ROOT/path).read_bytes();assert prev.prev.blob(raw)==sha,(path,'input Git blob mismatch');data[path]=json.loads(raw)
    base=data['certificates/rpb108_rc203_residual_enriched_six_source_inverse.json'];prior=data['certificates/rpb108_rc206_directional_error_inverse.json'];metric=data['certificates/rpb108_rc121_diagonal_metric_equivalence.json'];trial=base['selected_enclosure']
    assert base['selected_trial']=='least_residual' and prior['relative_inverse_width_upper']=='21003/31250'
    G=mat(base,'source_D_Gram_lower');GH=mat(base,'source_D_Gram_upper');Y=mat(trial,'trial_basis_coefficients');ctx=prev.prev.context(base,trial);keep=[0,1,2,3,4,6]
    J=[[F(i==keep[j])-Y[i][j] for j in range(6)] for i in range(8)]
    SUlo=scale(F(1,2),add(add(G,cong(Y,mat(base,'raw_trial_D_Gram_Loewner_lower'))),cong(J,mat(base,'raw_trial_D_Gram_Loewner_upper')),-1))
    SUhi=scale(F(1,2),add(add(GH,ctx['UG']),cong(J,mat(base,'raw_trial_D_Gram_Loewner_lower')),-1))
    Xlo=add(ctx['baseLo'],SUlo,-1);Xhi=add(ctx['baseHi'],SUhi,-1);assert psd(add(Xhi,Xlo,-1))
    a=F(metric['actual_canonical_diagonal_metric_lower']);assert 0<a<=2
    s=prior['selected_enclosure'];eps=list(map(F,base['individual_raw_trial_action_error_norm_upper']));w=list(map(F,s['triangle_weights']));assert F(s['triangle_mix'])==1
    E=prev.error_gram(Y,eps,w);assert ser(E)==s['action_error_Gram_upper'] and psd(E)
    tail=data['certificates/rpb108_rc210_collective_regular_input_tail.json']
    assert tail210.run(reverse)==tail,'collective tail certificate replay mismatch'
    E=mat(tail,'complete_fixed_trial_action_error_Gram_upper');assert psd(E)
    latest=data['certificates/rpb108_rc208_coupled_action_error_inverse.json']
    l,u,tC,tW=[F(proposal[k]) for k in ['action_lower_theta','action_upper_theta','tail_variational_theta','tail_cross_theta']]
    assert 0<l<=F(1,2) and min(u,tC,tW)>0
    tailC=add(scale(tC,ctx['Utail']),scale(1/(4*tC),ctx['Rtail']))
    tailW=add(scale(tW,ctx['Utail']),scale(1/(4*tW),ctx['Rtail']))
    def Wupper(c):
        terms=[ctx['UG'],scale(c*c,ctx['Nhi']),scale(2*c,Xhi),scale(2*c,tailW)]
        if reverse:terms.reverse()
        out=scale(F(0),G)
        for term in terms:out=add(out,term)
        assert psd(out)
        return out
    WL=Wupper(F(1));WU=Wupper(2/a)
    lower=add(add(add(ctx['baseLo'],scale(F(1,2),ctx['Nlo'])),tailC,-1),add(scale(l,WL),scale(1/(4*l)-F(1,2),E)),-1)
    upper=add(add(add(ctx['baseHi'],scale(1/a,ctx['Nhi'])),tailC),add(scale(u,WU),scale(1/a+1/(4*u),E)))
    inheritedL=mat(latest['selected_enclosure'],'canonical_inverse_response_lower');inheritedH=mat(latest['selected_enclosure'],'canonical_inverse_response_upper');candidates=[]
    optsL=[('coupled',lower),('inherited_RC208',inheritedL)];optsH=[('coupled',upper),('inherited_RC208',inheritedH)]
    if reverse:optsL.reverse();optsH.reverse()
    for ln,lo in optsL:
        for hn,hi in optsH:
            gap=add(hi,lo,-1)
            if not psd(lo) or not psd(gap):continue
            beta=width(gap,G);gate=add(scale(F(1,2),G),gap,-1);assert psd(add(scale(beta,G),gap,-1))
            candidates.append(dict(lower_type=ln,upper_type=hn,relative_inverse_width_upper=str(beta),half_Gram_gate_passed=psd(gate),canonical_inverse_response_lower=ser(lo),canonical_inverse_response_upper=ser(hi),half_Gram_gate_matrix=ser(gate)))
    chosen=min(candidates,key=lambda x:(F(x['relative_inverse_width_upper']),x['lower_type'],x['upper_type']));beta=F(chosen['relative_inverse_width_upper']);old=F(latest['relative_inverse_width_upper']);assert beta<=old
    return dict(milestone='RC210-inverse',starting_commit='2733eb54d1a7858f3d1d1c59be33df19e7207adf',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,rational_parameter_proposal=proposal,source_family=base['response_source_order'],trial_family=base['raw_trial_basis_order'],fixed_trial_map_and_all_physical_carriers_unchanged=True,RC206_error_rebuilt_as_control=True,RC210_collective_regular_tail_error_replayed_exactly=True,full_source_and_residual_tails_retained=True,finite_source_residual_cross_lower=ser(Xlo),finite_source_residual_cross_upper=ser(Xhi),coupled_lower_error_vector_Gram_upper=ser(WL),coupled_upper_error_vector_Gram_upper=ser(WU),selected_enclosure=chosen,relative_inverse_width_upper=str(beta),previous_same_family_width_upper=str(old),certified_acceptance_ratio_upper=str(2*beta),certified_gate_margin_lower=str(F(1,2)-beta),canonical_half_Gram_inverse_width_gate_passed=chosen['half_Gram_gate_passed'],same_error_combined_before_Young=True,method_outside_RC207_separate_payment_barrier=True,complex_response_mixtures_paid=True,acceptance_verified_by_exact_rational_PSD=True,numerical_optimization_used_only_for_parameter_proposal=True,Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC211: if six-source gate is accepted, extend native z_b6/t10 and odd/source-range coverage; original augmentation and Stage I remain open')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--proposal',type=Path);p.add_argument('--output',type=Path,required=True);p.add_argument('--replay',action='store_true');args=p.parse_args()
    expected=json.loads(args.output.read_text()) if args.replay else None
    proposal=expected['rational_parameter_proposal'] if expected is not None else (json.loads(args.proposal.read_text()) if args.proposal else DEFAULT_PROPOSAL)
    result=run(proposal,args.replay)
    if args.replay:assert result==expected,'reversed-order replay differs'
    else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC210 inverse PASS: inverse width',result['relative_inverse_width_upper'],'half-Gram gate',result['canonical_half_Gram_inverse_width_gate_passed'])
