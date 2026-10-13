"""RC196: certified response-adapted triangle weights on unchanged RC195 data."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import up,psd,ser,loewner,sqrtup
from validate_rpb108_rc129_four_vector_joint_moment import inv,cong,add
from validate_rpb108_rc177_three_source_canonical_action_gram import mat,scale,width
from validate_rpb108_rc186_residual_enriched_five_source_inverse import outer

def inputs():
    base=Path(__file__).resolve().parents[1]/'certificates'
    return [base/('rpb108_rc'+n+'.json') for n in ['195_refined_five_source_inverse','121_diagonal_metric_equivalence','184_five_source_canonical_inverse']]

def run(paths,replay=False):
    raw=[p.read_bytes() for p in paths];prior,metric,historical=map(json.loads,raw);hs=[hashlib.sha256(b).hexdigest() for b in raw]
    assert [d['milestone'] for d in [prior,metric,historical]]==['RC195','RC121','RC184']
    assert hs[1] in prior['input_sha256'] and hs[2] in prior['input_sha256']
    assert metric['endpoint_form_bound']=='0 <= h <= J + 2 log(2) I <= D'
    Glo=mat(prior,'source_D_Gram_lower');Ghi=mat(prior,'source_D_Gram_upper');Gi=inv(Glo);eps=list(map(F,prior['individual_raw_trial_action_error_norm_upper']))
    assert len(eps)==6 and psd(Glo)
    a=F(metric['actual_canonical_diagonal_metric_lower']);sw=[sqrtup(Ghi[i][i]) for i in range(5)]
    inheritedLo=mat(prior['selected_enclosure'],'canonical_inverse_response_lower');inheritedHi=mat(prior['selected_enclosure'],'canonical_inverse_response_upper');inheritedBeta=F(prior['relative_inverse_width_upper'])
    results=[]
    for trial in sorted(prior['evaluated_inverse_trials'],key=lambda x:x['trial'],reverse=replay):
        Y=mat(trial,'trial_basis_coefficients');UGhi=mat(trial,'full_trial_D_Gram_upper');SUlo=mat(trial,'full_source_trial_cross_Loewner_lower');SUhi=mat(trial,'full_source_trial_cross_Loewner_upper')
        ul=mat(trial,'finite_trial_nominal_residual_cross_entry_lower');uh=mat(trial,'finite_trial_nominal_residual_cross_entry_upper');prefixLo,prefixHi,_=loewner(ul,uh,sw)
        Utail=mat(trial,'trial_source_tail_D_Gram_upper');Rtail=mat(trial,'nominal_residual_tail_D_Gram_upper');Nlo=mat(trial,'nominal_residual_Gram_lower');Nhi=mat(trial,'nominal_residual_Gram_upper')
        # For every complex response x, ||sum e_k Y_k x|| <= sum eps_k |Y_k x|.
        # Any positive weights t give squared norm <= (sum eps_k/t_k)
        # sum eps_k t_k |Y_k x|^2. Choose t_k near 1/||Y_k||_(Glo^-1).
        dual=[sum(Y[k][i]*Gi[i][j]*Y[k][j] for i in range(5) for j in range(5)) for k in range(6)]
        assert min(dual)>=0
        weights=[1/sqrtup(d) if d else F(1) for d in dual];factor=sum(eps[k]/weights[k] for k in range(6))
        adaptive=[[sum(factor*eps[k]*weights[k]*Y[k][i]*Y[k][j] for k in range(6)) for j in range(5)] for i in range(5)]
        rawWeights=[sqrtup(F(prior['raw_trial_D_Gram_Loewner_upper'][k][k])) for k in range(6)]
        rawFactor=sum(eps[k]/rawWeights[k] for k in range(6));oldRaw=[[up(eps[i]*rawWeights[i]*rawFactor) if i==j else F(0) for j in range(6)] for i in range(6)]
        raw=cong(Y,oldRaw)
        ce=[sum(abs(Y[k][j])*eps[k] for k in range(6)) for j in range(5)];c=sum(ce[j]/sw[j] for j in range(5));direct=[[up(ce[j]*sw[j]*c) if i==j else F(0) for j in range(5)] for i in range(5)]
        assert psd(adaptive)
        # Independent exact Cauchy Gram check before congruence.
        diagonal=[[factor*eps[i]*weights[i] if i==j else F(0) for j in range(6)] for i in range(6)]
        assert psd(add(diagonal,outer(eps),-1))
        errors=[('response_adapted_triangle',adaptive),('raw_trial_triangle',raw),('response_triangle',direct)]
        settings=[F(1,n) for n in [10000,3000,1500,1000,750,600,500,400,350,300,250,200,150,100,75,50,30,10,3,1]]
        tailSettings=[F(1,10),F(1,3),F(1)]
        cBest=None
        for eName,E in (errors[::-1] if replay else errors):
            for theta in (settings[::-1] if replay else settings):
                actionPay=add(scale(theta,UGhi),scale(1/(4*theta),E))
                for tt in (tailSettings[::-1] if replay else tailSettings):
                    tailPay=add(scale(tt,Utail),scale(1/(4*tt),Rtail));pay=add(actionPay,tailPay)
                    Clo=add(add(SUlo,prefixLo),pay,-1);Chi=add(add(SUhi,prefixHi),pay);gap=add(Chi,Clo,-1)
                    if cBest is not None and not psd(add(scale(cBest[0][0],Glo),gap,-1)):continue
                    cb=width(gap,Glo);key=(cb,theta,tt,eName)
                    if cBest is None or key<cBest[0]:cBest=(key,Clo,Chi,actionPay,tailPay)
        (cb,theta,tt,eName),Clo,Chi,actionPay,tailPay=cBest
        best=None
        taus=[F(1,n) for n in [100,30,10,5,4,3,2,1]]+[F(3)];sigmas=[F(0),F(1,30),F(1,10),F(1,3),F(1,2)]
        for rn,E in (errors[::-1] if replay else errors):
            for tau in (taus[::-1] if replay else taus):
                Rhi=add(scale(1+tau,Nhi),scale(1+1/tau,E));upper=add(Chi,scale(1/a,Rhi))
                for sigma in (sigmas[::-1] if replay else sigmas):
                    Rlo=[[F(0)]*5 for _ in range(5)] if sigma==0 else add(scale(1-sigma,Nlo),scale(-(1/sigma-1),E))
                    if not psd(Rlo):continue
                    lower=add(Clo,scale(F(1,2),Rlo))
                    for ln,lc in [('refined',lower),('inherited',inheritedLo),('structural',scale(F(1,2),Glo))]:
                        for hn,hc in [('refined',upper),('inherited',inheritedHi),('structural',scale(1/a,Ghi))]:
                            if not psd(lc):continue
                            gap=add(hc,lc,-1)
                            if not psd(gap):continue
                            if best is not None and not psd(add(scale(best[0][0],Glo),gap,-1)):continue
                            beta=inheritedBeta if ln==hn=='inherited' else width(gap,Glo)
                            key=(beta,tau,sigma,ln,hn,rn)
                            if best is None or key<best[0]:best=(key,lc,hc,Rlo,Rhi)
        (beta,tau,sigma,ln,hn,rn),lower,upper,Rlo,Rhi=best
        gap=add(upper,lower,-1);assert psd(add(scale(beta,Glo),gap,-1));gate=add(scale(F(1,2),Glo),gap,-1)
        results.append(dict(trial=trial['trial'],trial_basis_coefficients=ser(Y),row_dual_D_energy_squared=list(map(str,dual)),adaptive_triangle_weights=list(map(str,weights)),adaptive_triangle_factor=str(factor),adaptive_response_action_error_Gram_upper=ser(adaptive),raw_trial_response_action_error_Gram_upper=ser(raw),direct_response_action_error_Gram_upper=ser(direct),selected_variational_action_theta=str(theta),selected_variational_tail_theta=str(tt),selected_variational_error_type=eName,variational_action_uncertainty_Loewner_upper=ser(actionPay),variational_tail_uncertainty_Loewner_upper=ser(tailPay),variational_response_lower=ser(Clo),variational_response_upper=ser(Chi),relative_variational_width_upper=str(cb),selected_residual_error_type=rn,selected_upper_tau=str(tau),selected_lower_tau=str(sigma),actual_residual_Gram_lower=ser(Rlo),actual_residual_Gram_upper=ser(Rhi),selected_lower_type=ln,selected_upper_type=hn,canonical_inverse_response_lower=ser(lower),canonical_inverse_response_upper=ser(upper),relative_inverse_width_upper=str(beta),half_Gram_gate_matrix=ser(gate),half_Gram_gate_passed=psd(gate),nominal_residual_Gram_unchanged=True,adaptive_error_relative_Gram_upper=str(width(adaptive,Glo))))
        print('RC196',trial['trial'],'inverse width',float(beta),'gate',psd(gate),'adaptiveE',float(width(adaptive,Glo)),flush=True)
    results.sort(key=lambda x:x['trial']);selected=min(results,key=lambda x:(F(x['relative_inverse_width_upper']),x['trial']));beta=F(selected['relative_inverse_width_upper'])
    probe=list(map(F,historical['half_Gram_gate_failure_witness_coefficients']));value=sum(probe[i]*F(selected['half_Gram_gate_matrix'][i][j])*probe[j] for i in range(5) for j in range(5))
    return dict(milestone='RC196',status='PASS: response-adapted certified action-error bound and same-family inverse; gate separately reported',starting_commit='6d435ace9ae49dec6acd6b6c963f567ac4c6fd92',input_sha256=hs,response_source_order=prior['response_source_order'],raw_trial_basis_order=prior['raw_trial_basis_order'],source_D_Gram_lower=ser(Glo),source_D_Gram_upper=ser(Ghi),individual_raw_trial_action_error_norm_upper=prior['individual_raw_trial_action_error_norm_upper'],evaluated_inverse_trials=results,selected_trial=selected['trial'],selected_enclosure=selected,relative_inverse_width_upper=str(beta),previous_same_family_width_upper=str(inheritedBeta),certified_acceptance_ratio_upper=str(2*beta),certified_gate_margin_lower=str(F(1,2)-beta),canonical_half_Gram_inverse_width_gate_passed=selected['half_Gram_gate_passed'],historical_gate_probe_coefficients=list(map(str,probe)),historical_gate_probe_quadratic=str(value),all_RC195_complete_carriers_and_mixed_matrices_retained=True,source_trial_and_action_carriers_unchanged=True,nominal_residual_matrices_unchanged=True,full_complex_mixtures_and_infinite_tails_paid=True,actual_five_source_canonical_inverse_response_certified=True,native_seven_source_frame_changed=False,Stage_I_closed=False,Stage_I_completion_ratio=None,RH=False,F4=False,Lean=False,next_cursor='extend native source coverage if the same-family gate passes; otherwise refine remaining actual action and residual bounds')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');a=p.parse_args();r=run(inputs(),a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC196 PASS')
