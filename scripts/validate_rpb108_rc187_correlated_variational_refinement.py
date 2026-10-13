"""RC187: matrix Young refinement of variational uncertainty on unchanged trials."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,bounds,down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc129_four_vector_joint_moment import add,cong
from validate_rpb108_rc134_correlated_six_input_covariance import smul
from validate_rpb108_rc177_three_source_canonical_action_gram import scale,mat,width
from validate_rpb108_rc185_five_source_focus_action import inputs as older_inputs
from validate_rpb108_rc186_residual_enriched_five_source_inverse import outer,total

def inputs():
    root=Path(__file__).resolve().parents[1]/'certificates'
    return [root/'rpb108_rc186_residual_enriched_five_source_inverse.json',root/'rpb108_rc185_five_source_focus_action.json']+older_inputs()
def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];data=list(map(json.loads,raw));hs=[hashlib.sha256(b).hexdigest() for b in raw];prior=data[0]
    assert prior['milestone']=='RC186' and prior['input_sha256']==hs[1:]
    src=Path(__file__).with_name('validate_rpb108_rc186_residual_enriched_five_source_inverse.py').read_text().split("\nif __name__=='__main__':")[0]
    marker='    for name in sorted(trials,reverse=replay):'
    assert src.count(marker)==1
    ns={'__file__':str(Path(__file__).with_name('validate_rpb108_rc186_residual_enriched_five_source_inverse.py'))};exec(compile(src.replace(marker,'    return locals()\n'+marker,1),'RC186 immutable carrier and mixed geometry reconstruction','exec'),ns)
    d=ns['run'](paths[1:],replay)
    cache=d['cache'];degrees=d['degrees'];T=d['T'];a=d['a'];df=d['df'];mu=d['mu'];Glo=d['Glo'];Ghi=d['Ghi'];GTlo=d['tgLo'];GThi=d['tgHi'];sw=d['sw']
    assert prior['source_D_Gram_lower']==ser(Glo) and prior['source_D_Gram_upper']==ser(Ghi)
    oldSelected=prior['selected_enclosure'];inheritedLo=mat(oldSelected,'canonical_inverse_response_lower');inheritedHi=mat(oldSelected,'canonical_inverse_response_upper');inheritedBeta=F(prior['relative_inverse_width_upper'])
    settings=[F(1,10000),F(1,3000),F(1,1000),F(1,300),F(1,100),F(1,30),F(1,10),F(1,3),F(1)]
    tailSettings=[F(1,100),F(1,10),F(1,3),F(1),F(3),F(10)]
    results=[]
    for old in sorted(prior['evaluated_inverse_trials'],key=lambda x:x['trial'],reverse=replay):
        name=old['trial'];Y=mat(old,'trial_basis_coefficients');J=[[F(i==j)-Y[i][j] for j in range(5)] for i in range(6)]
        UGlo=cong(Y,GTlo);UGhi=cong(Y,GThi);assert psd(UGhi)
        # Sym(S*D U) = (G_S + G_U - G_(S-U))/2.
        SUlo=scale(F(1,2),add(add(Glo,UGlo),cong(J,GThi),-1));SUhi=scale(F(1,2),add(add(Ghi,UGhi),cong(J,GTlo),-1))
        ur=[[Z for _ in range(5)] for _ in range(5)]
        for n in degrees:
            u,v,mass=cache[n];U=[total([smul(rat(Y[k][j]),u[k]) for k in range(6)]) for j in range(5)];V=[total([smul(rat(Y[k][j]),v[k]) for k in range(6)]) for j in range(5)];R=[minus(u[j],V[j]) for j in range(5)]
            for i in range(5):
                for j in range(5):ur[i][j]=plus(ur[i][j],smul(mass,smul(U[i],R[j])))
        ul=[[F(0)]*5 for _ in range(5)];uh=[[F(0)]*5 for _ in range(5)]
        for i in range(5):
            for j in range(i,5):
                lo,hi=bounds(smul(rat(F(1,2)),plus(ur[i][j],ur[j][i])));ul[i][j]=ul[j][i]=lo;uh[i][j]=uh[j][i]=hi
        prefixLo,prefixHi,_=loewner(ul,uh,sw)
        leadU=[Y[3][j]+mu[0]*Y[4][j] for j in range(5)]
        Utail=add(scale(2*T,outer(leadU)),scale(2*T*df*df,outer(Y[4])))
        Rtail=mat(old,'whole_residual_tail_Gram_upper');Nlo=mat(old,'nominal_residual_Gram_lower');Nhi=mat(old,'nominal_residual_Gram_upper')
        errors=[('inherited_selected',mat(old,'selected_response_action_error_Gram_upper')),('response_triangle',mat(old,'direct_response_action_error_Gram_upper'))]
        cBest=None
        for eName,E in (errors[::-1] if replay else errors):
            for theta in (settings[::-1] if replay else settings):
                actionPay=add(scale(theta,UGhi),scale(1/(4*theta),E))
                for tailTheta in (tailSettings[::-1] if replay else tailSettings):
                    tailPay=add(scale(tailTheta,Utail),scale(1/(4*tailTheta),Rtail));pay=add(actionPay,tailPay)
                    Clo=add(add(SUlo,prefixLo),pay,-1);Chi=add(add(SUhi,prefixHi),pay);gap=add(Chi,Clo,-1);assert psd(gap)
                    if cBest is not None and not psd(add(scale(cBest[0][0],Glo),gap,-1)):continue
                    if cBest is not None and not psd(add(scale(cBest[0][0]-F(1,10**6),Glo),gap,-1)):beta=cBest[0][0]
                    else:beta=width(gap,Glo)
                    key=(beta,theta,tailTheta,eName)
                    if cBest is None or key<cBest[0]:cBest=(key,Clo,Chi,actionPay,tailPay)
        (cBeta,theta,tailTheta,eName),Clo,Chi,actionPay,tailPay=cBest
        assert psd(add(scale(cBeta,Glo),add(Chi,Clo,-1),-1))
        best=None
        taus=[F(1,100),F(1,30),F(1,10),F(1,3),F(1),F(3)];sigmas=[F(0),F(1,30),F(1,10),F(1,3),F(1,2)]
        for errorName,E in (errors[::-1] if replay else errors):
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
                            if ln=='inherited' and hn=='inherited':beta=inheritedBeta
                            elif best is not None and not psd(add(scale(best[0][0]-F(1,10**6),Glo),gap,-1)):beta=best[0][0]
                            else:beta=width(gap,Glo)
                            key=(beta,tau,sigma,ln,hn,errorName)
                            if best is None or key<best[0]:best=(key,lc,hc,Rlo,Rhi)
        (beta,tau,sigma,ln,hn,errorName),lower,upper,Rlo,Rhi=best;gap=add(upper,lower,-1);assert psd(add(scale(beta,Glo),gap,-1))
        gate=add(scale(F(1,2),Glo),gap,-1)
        item=dict(trial=name,trial_basis_coefficients=ser(Y),full_trial_D_Gram_upper=ser(UGhi),full_source_trial_cross_Loewner_lower=ser(SUlo),full_source_trial_cross_Loewner_upper=ser(SUhi),finite_trial_nominal_residual_cross_entry_lower=ser(ul),finite_trial_nominal_residual_cross_entry_upper=ser(uh),trial_source_tail_D_Gram_upper=ser(Utail),nominal_residual_tail_D_Gram_upper=ser(Rtail),selected_variational_action_theta=str(theta),selected_variational_tail_theta=str(tailTheta),selected_variational_error_type=eName,variational_action_uncertainty_Loewner_upper=ser(actionPay),variational_tail_uncertainty_Loewner_upper=ser(tailPay),variational_response_lower=ser(Clo),variational_response_upper=ser(Chi),relative_variational_width_upper=str(cBeta),selected_residual_error_type=errorName,selected_upper_tau=str(tau),selected_lower_tau=str(sigma),actual_residual_Gram_lower=ser(Rlo),actual_residual_Gram_upper=ser(Rhi),selected_lower_type=ln,selected_upper_type=hn,canonical_inverse_response_lower=ser(lower),canonical_inverse_response_upper=ser(upper),relative_inverse_width_upper=str(beta),half_Gram_gate_matrix=ser(gate),half_Gram_gate_passed=psd(gate))
        results.append(item);print('RC187',name,'C width',float(cBeta),'inverse width',float(beta),'gate',psd(gate),flush=True)
    results.sort(key=lambda x:x['trial']);selected=min(results,key=lambda x:(F(x['relative_inverse_width_upper']),x['trial']));beta=F(selected['relative_inverse_width_upper'])
    return dict(milestone='RC187',status='PASS: correlated variational refinement; inverse gate separately reported',starting_commit='ce8ab73b05de739868149002541b449dd3e34505',input_sha256=hs,response_source_order=prior['response_source_order'],raw_trial_basis_order=prior['raw_trial_basis_order'],source_D_Gram_lower=ser(Glo),source_D_Gram_upper=ser(Ghi),evaluated_inverse_trials=results,selected_trial=selected['trial'],selected_enclosure=selected,relative_inverse_width_upper=str(beta),previous_same_family_width_upper=str(inheritedBeta),inverse_width_improved_over_RC186=beta<inheritedBeta,certified_acceptance_ratio_upper=str(2*beta),certified_gate_margin_lower=str(F(1,2)-beta),canonical_half_Gram_inverse_width_gate_passed=selected['half_Gram_gate_passed'],same_operator_norm_response_sources_and_trial_actions_as_RC186=True,new_action_carriers_constructed=False,correlated_variational_Young_bounds_certified=True,full_input_output_tails_and_complex_mixtures_paid=True,actual_five_source_canonical_inverse_response_certified=True,native_seven_source_frame_changed=False,Stage_I_closed=False,Stage_I_completion_ratio=None,original_Weil_or_augmented_actions_performed=False,RH=False,F4=False,Lean=False,next_cursor='tighten the retained psi0 and w14 endpoint action bounds if the five-source gate remains open; retain the refined correlated variational method')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');args=p.parse_args();result=run(inputs(),args.replay)
    if args.replay:assert json.loads(Path(args.output).read_text())==result
    else:Path(args.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC187 PASS: correlated variational enclosure refinement')
