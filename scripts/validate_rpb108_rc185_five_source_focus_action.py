"""RC185: paid five-source residual polynomial and complete canonical action."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,up,down,ser
from validate_rpb108_rc171_regular_legendre_projection import ZERO,add,sub,mul,scale,divide,endpoints,log_point
from validate_rpb108_rc176_f0_regular_output_carrier import root,lower_root
from validate_rpb108_rc179_focus_residual_canonical_action import regular_action

NAMES=['184_five_source_canonical_inverse','183_w14_canonical_action','183_materialized_w14_canonical_carrier','182_four_source_canonical_inverse','182_materialized_Cpsi_carrier','181_psi_action_completion_dashboard','180_residual_enriched_canonical_inverse','179_focus_residual_canonical_action','178_three_source_canonical_inverse','177_three_source_canonical_action_gram','176_f0_regular_output_carrier','172_quadratic_regular_action','171_regular_legendre_projection','129_four_vector_joint_moment','128_collective_second_response','127_enriched_even_endpoint_action','121_diagonal_metric_equivalence','175_f0_regular_physical_source','154_centered_analytic_tail_action','170_poisson_regular_action']
def inputs():return [Path(__file__).resolve().parents[1]/'certificates'/('rpb108_rc'+n+'.json') for n in NAMES]
def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];data=list(map(json.loads,raw));hs=[hashlib.sha256(b).hexdigest() for b in raw]
    focus=data[0];regular=data[-1];joint=data[13];metric=data[16]
    assert focus['milestone']=='RC184' and focus['input_sha256']==hs[1:19] and regular['milestone']=='RC170'
    # Reconstruct only the immutable coefficient carriers, skipping the old
    # Gram and optimization work. This uses the exact RC184 source formulas.
    src=Path(__file__).with_name('validate_rpb108_rc184_five_source_canonical_inverse.py').read_text().split("\nif __name__=='__main__':")[0]
    start=src.index('        for i in range(6):\n            for j in range(6):mixed')
    stop=src.index('    first=O+2;',start)
    src=src[:start]+"    return locals()\n"+src[stop:]
    ns={};exec(compile(src,'RC184 immutable coefficient carriers','exec'),ns)
    d=ns['run'](paths[1:19],replay)
    dn=d['D'];sl=d['sl'];sh=d['sh'];prefixO=d['O'];M=256;O=4094
    selected=focus['selected_enclosure'];Y=[[F(x) for x in row] for row in selected['trial_basis_coefficients']]
    probe=list(map(F,focus['half_Gram_gate_failure_witness_coefficients']))
    y=[sum(Y[i][j]*probe[j] for j in range(5)) for i in range(5)]
    quadratic=lambda A:sum(probe[i]*F(A[i][j])*probe[j] for i in range(5) for j in range(5))
    q={};qrows=[];roundEnergy=F(0);finiteTail=F(0)
    order=list(range(0,prefixO+1,2));order=order[::-1] if replay else order
    for n in order:
        u,v,mass=d['cache'][n];u=[u[i] for i in [0,1,2,4,5]];v=[v[i] for i in [0,1,2,4,5]]
        value=ZERO
        for i in range(5):value=add(value,sub(scale(probe[i],u[i]),scale(y[i],v[i])))
        lo,hi=endpoints(value);masshi=2*B/F(2*n+1)*F(dn[n][1])
        if n<=M:
            c=down((lo+hi)/2,10**40);rad=max(c-lo,hi-c);q[n]=c;roundEnergy+=up(masshi*rad*rad)
            qrows.append(dict(degree=n,coefficient_center=str(c),coefficient_radius=str(rad)))
        else:finiteTail+=up(masshi*max(abs(lo),abs(hi))**2)
    qrows.sort(key=lambda x:x['degree'])
    analyticTail=quadratic(selected['whole_residual_tail_Gram_upper'])
    nominalError=root(roundEnergy+finiteTail+analyticTail)
    inheritedResidualError=F(focus['residual_focus_nominal_to_actual_D_error_norm_upper'])
    eps=list(map(F,data[9]['individual_full_action_D_error_norm_upper']))+[F(data[5]['canonical_psi_source_form_full_D_error_norm_upper']),F(data[1]['complete_canonical_w14_action_D_error_norm_upper'])]
    directResidualError=up(sum(abs(y[i])*eps[i] for i in range(5)))
    actualResidualError=min(inheritedResidualError,directResidualError)
    assert directResidualError<inheritedResidualError
    nominalFocusLower=lower_root(quadratic(selected['nominal_residual_Gram_lower']))
    actualFocusLower=down(nominalFocusLower-actualResidualError)
    assert actualFocusLower>=F(focus['residual_focus_actual_D_norm_lower'])
    inputError=up(nominalError+actualResidualError)
    relativeInput=up(inputError/actualFocusLower)
    qEnergyLo=qEnergyHi=F(0)
    for n,c in q.items():
        qEnergyLo+=down(2*B/F(2*n+1)*F(dn[n][0])*c*c)
        qEnergyHi+=up(2*B/F(2*n+1)*F(dn[n][1])*c*c)
    assert qEnergyLo>0
    print('RC185 focus input error',float(inputError),'relative',float(relativeInput),flush=True)
    reg=regular_action(q,regular,joint,replay)
    sl,sh=d['sl'],d['sh'];A=sum(abs(c) for c in q.values());log2=log_point(F(2));r=F(789,125)
    H=[F(0)]
    for n in range(1,2*O+1):H.append(H[-1]+F(1,n))
    endpoint=[];endpointEnergy=F(0);negative=[];negativeEnergy=F(0)
    jobs=sorted(q,reverse=replay)
    for n in range(0,O+1,2):
        value=ZERO
        for m in jobs:
            if n==m:entry=sub(rat(2*H[2*n]-2*H[n]+F(1,2*n+1)),log2)
            else:entry=rat(F(2*n+1,abs(n-m)*(n+m+1)))
            value=add(value,scale(q[m],entry))
        value=divide(value,dn[n]);lo,hi=endpoints(value);c=(lo+hi)/2;rad=(hi-lo)/2
        endpointEnergy+=up(2*B/F(2*n+1)*(sh+H[n])*rad*rad)
        endpoint.append(dict(degree=n,coefficient_center=str(c),coefficient_radius=str(rad)))
        if n<=M:
            value=divide(rat(-r*q[n]),dn[n]);lo,hi=endpoints(value);c=(lo+hi)/2;rad=(hi-lo)/2
            negativeEnergy+=up(2*B/F(2*n+1)*(sh+H[n])*rad*rad)
            negative.append(dict(degree=n,coefficient_center=str(c),coefficient_radius=str(rad)))
        if n%1024==0:print('RC185 signed endpoint block',n,flush=True)
    first=O+2;rho=F(M*(M+1),first*(first+1));T=up(B/(F(dn[O][0])*(O-1)*O))
    endpointTail=up(root(T)*A/(1-rho));endpointError=up(root(endpointEnergy+endpointTail**2))
    actionError=up(endpointError+root(negativeEnergy)+F(reg['complete_D_inverse_regular_action_error_norm_upper']))
    focusActionError=up(actionError+2*inputError)
    # Exact rational finite source and its represented complete action.
    cq={x['degree']:F(x['coefficient_center']) for x in endpoint};nq={x['degree']:F(x['coefficient_center']) for x in negative};rq={x['degree']:F(x['coefficient_center']) for x in reg['D_inverse_regular_polynomial']}
    trial={n:q.get(n,F(0))+cq.get(n,F(0))+nq.get(n,F(0))+rq.get(n,F(0)) for n in range(0,O+1,2)}
    pair=ZERO
    for n in jobs:pair=add(pair,mul(rat(2*B/F(2*n+1)*q[n]*trial[n]),dn[n]))
    lo,hi=endpoints(pair);pairError=up(root(qEnergyHi)*actionError)
    actualPairLo=down(lo-pairError);actualPairHi=up(hi+pairError)
    assert actualPairLo>F(metric['actual_canonical_diagonal_metric_lower'])*qEnergyHi and actualPairHi<2*qEnergyLo
    return dict(milestone='RC185',status='PASS: paid five-source residual approximation and complete canonical action',starting_commit='2d768e05d14b04040ba2195a6050c2d770b53840',input_sha256=hs,aperture='11/10',response_source_order=focus['response_source_order'],residual_source_probe=list(map(str,probe)),selected_inverse_trial=focus['selected_trial'],inverse_trial_focus_coefficients=list(map(str,y)),
      finite_focus_direction_definition='q185=rounded degree-256 prefix of RC184 (S-VY)*probe; exact rational polynomial, distinct from RC179 q',finite_focus_direction=qrows,
      finite_input_degree=M,nominal_focus_input_rounding_D_energy_upper=str(up(roundEnergy)),omitted_finite_focus_D_energy_upper=str(up(finiteTail)),omitted_analytic_focus_D_energy_upper=str(up(analyticTail)),inherited_nominal_to_actual_focus_D_error_norm_upper=str(inheritedResidualError),direct_nominal_to_actual_focus_D_error_norm_upper=str(directResidualError),actual_focus_D_norm_lower=str(actualFocusLower),single_focus_error_uses_columnwise_triangle_inequality=True,nominal_focus_to_q_D_error_norm_upper=str(up(nominalError)),actual_focus_to_q_D_error_norm_upper=str(inputError),actual_focus_to_q_relative_D_norm_error_upper=str(relativeInput),finite_focus_D_energy_lower=str(qEnergyLo),finite_focus_D_energy_upper=str(qEnergyHi),regular_action=reg,
      endpoint_action_polynomial=endpoint,endpoint_output_degree=O,endpoint_action_full_output_tail_D_norm_upper=str(endpointTail),endpoint_action_full_D_error_norm_upper=str(endpointError),negative_r_D_inverse_direction_polynomial=negative,
      complete_canonical_q_action_definition='q185 + endpoint polynomial + negative-r D inverse polynomial + regular D inverse polynomial',complete_actual_canonical_q_action_D_error_norm_upper=str(actionError),complete_actual_focus_residual_action_D_error_norm_upper=str(focusActionError),actual_q_canonical_pairing_lower=str(actualPairLo),actual_q_canonical_pairing_upper=str(actualPairHi),canonical_q_pairing_structural_a_D_to_2_D_verified=True,
      canonical_action_on_new_finite_direction_evaluated=True,full_input_and_output_tails_paid=True,actual_focus_action_transfer_uses_M_norm_at_most_two=True,enriched_inverse_response_evaluated=False,canonical_half_Gram_gate_closed=False,native_seven_source_frame_changed=False,original_Weil_or_augmented_actions_performed=False,Stage_I_closed=False,RH=False,F4=False,Lean=False,
      next_cursor='orthogonalize q185 against the existing five-source trial family, certify correlated mixed Gram and action rows, and re-evaluate the same five-source inverse gate')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');args=p.parse_args()
    result=run(inputs(),args.replay)
    if args.replay:assert json.loads(Path(args.output).read_text())==result
    else:Path(args.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC185 PASS: five-source focus polynomial and complete canonical action')
