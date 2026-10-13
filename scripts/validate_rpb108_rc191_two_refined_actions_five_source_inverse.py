"""RC191: five-source inverse with both refined complete action carriers."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,bounds,down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc129_four_vector_joint_moment import add,cong
from validate_rpb108_rc134_correlated_six_input_covariance import smul
from validate_rpb108_rc177_three_source_canonical_action_gram import scale,mat,width
from validate_rpb108_rc185_five_source_focus_action import inputs as older_inputs
from validate_rpb108_rc186_residual_enriched_five_source_inverse import outer,total

from validate_rpb108_rc189_refined_psi_five_source_inverse import inputs as previous_inputs, refine184 as refine_psi184

def refine184(src):
    src=refine_psi184(src)
    marker="    cw={2*i:F(c) for i,c in enumerate(wcarrier['Cg_finite_coefficient_centers'])};negw={x['degree']:F(x['coefficient_center']) for x in wcarrier['negative_r_D_inverse_w14_finite_polynomial']};rw={x['degree']:F(x['coefficient_center']) for x in wcarrier['D_inverse_regular_polynomial']}"
    assert src.count(marker)==1
    src=src.replace(marker,marker+"\n    cw={2*i:F(int(c),int(REFINED_W_CARRIER['finite_center_scale'])) for i,c in enumerate(REFINED_W_CARRIER['finite_Cw14_coefficient_center_numerators'])};rw={x['degree']:F(x['coefficient_center']) for x in REFINED_W_CARRIER['D_inverse_regular_polynomial']}")
    marker="        if n>=4096:vw=plus(vw,smul(minus(rat(F(1,2)),div(rat(r),D[n])),w))"
    assert src.count(marker)==1
    src=src.replace(marker,"        if n>=4096:vw=minus(vw,smul(div(rat(r),D[n]),w))\n        if n>=32768:vw=plus(vw,smul(rat(F(1,2)),w))")
    return src

def inputs():
    root=Path(__file__).resolve().parents[1]/'certificates'
    return [root/('rpb108_rc'+n+'.json') for n in ['190_extended_w14_endpoint_action','190_materialized_Cw14_carrier','189_refined_psi_five_source_inverse']]+previous_inputs()
def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];data=list(map(json.loads,raw));hs=[hashlib.sha256(b).hexdigest() for b in raw]
    newW,wcarrier,prior,new,carrier=data[:5]
    assert [x['milestone'] for x in data[:5]]==['RC190','RC190-Cw14-carrier','RC189','RC188','RC188-Cpsi-carrier']
    assert prior['input_sha256']==hs[3:] and newW['input_sha256'][0]==hs[2]
    assert newW['materialized_endpoint_carrier_sha256']==hs[1] and newW['native_source_carrier_sha256']==hs[10]
    assert new['materialized_carrier_sha256']==hs[4] and carrier['whole_Cpsi_error_norm_upper']==new['full_Cpsi_trial_D_norm_error_upper']
    assert wcarrier['whole_Cw14_error_norm_upper']==newW['new_centered_Cw14_error_norm_upper']
    assert wcarrier['complete_D_inverse_Rw14_error_norm_upper']==newW['complete_D_inverse_Rw14_error_norm_upper']
    assert wcarrier['output_prefix_degree']==carrier['output_prefix_degree']==65534
    assert wcarrier['centered_input_tail_first_even_degree']==carrier['centered_input_tail_first_even_degree']==32768
    src=Path(__file__).with_name('validate_rpb108_rc186_residual_enriched_five_source_inverse.py').read_text().split("\nif __name__=='__main__':")[0]
    hook="    start=src.index('        for i in range(6):\\n            for j in range(6):mixed')"
    assert src.count(hook)==1
    src=src.replace(hook,'    src=REFINE184(src)\n'+hook)
    src=src.replace('ns={};exec(compile(src,',"ns={'REFINED_PSI_CARRIER':REFINED_PSI_CARRIER,'REFINED_W_CARRIER':REFINED_W_CARRIER};exec(compile(src,")
    src=src.replace("F(data[6]['canonical_psi_source_form_full_D_error_norm_upper'])","F(REFINED_PSI_CERT['canonical_psi_source_form_full_D_error_norm_upper'])")
    src=src.replace("F(data[2]['complete_canonical_w14_action_D_error_norm_upper'])","F(REFINED_W_CERT['complete_canonical_w14_action_D_error_norm_upper'])")
    src=src.replace("T=F(prior['common_eta_tail_D_energy_upper'])","T=up(B/(dl*(O-1)*O))")
    marker="    Aw=sum(mu[k]*F(lam,z)**k for k in range(15));Ap="
    assert src.count(marker)==1
    src=src.replace(marker,"    omega=[F(x['center']) for x in REFINED_W_CARRIER['analytic_output_moments'][:25]];lamW=F(REFINED_W_CARRIER['analytic_output_lambda']);Bw=sum(omega[k]*F(lamW,z)**k for k in range(25))\n"+marker)
    assert src.count('Aw,Ap,F(3,2)*Aw,F(0)')==1
    src=src.replace('Aw,Ap,F(3,2)*Aw,F(0)','Aw,Ap,F(3,2)*Aw+Bw,F(0)')
    marker='dw=abs(cw0)*df+Aw*r/(2*dl)'
    assert src.count(marker)==1
    src=src.replace(marker,marker+'+sum(omega[k]*F(lamW,z)**k for k in range(1,25))')
    marker='    for name in sorted(trials,reverse=replay):';assert src.count(marker)==1
    ns={'__file__':str(Path(__file__).with_name('validate_rpb108_rc186_residual_enriched_five_source_inverse.py')),'REFINE184':refine184,'REFINED_PSI_CARRIER':carrier,'REFINED_PSI_CERT':new,'REFINED_W_CARRIER':wcarrier,'REFINED_W_CERT':newW}
    exec(compile(src.replace(marker,'    return locals()\n'+marker,1),'RC191 complete two-refined-action mixed reconstruction','exec'),ns)
    d=ns['run'](paths[7:],replay)
    cache=d['cache'];degrees=d['degrees'];T=d['T'];a=d['a'];df=d['df'];mu=d['mu'];Glo=d['Glo'];Ghi=d['Ghi'];GTlo=d['tgLo'];GThi=d['tgHi'];sw=d['sw']
    # Every nominal residual, represented mixed row and error transformation
    # is reconstructed for the new carrier, rather than reusing RC186 values.
    fresh=[]
    for name in sorted(d['trials'],reverse=replay):
        Y=d['trials'][name];fg=[[Z for _ in range(5)] for _ in range(5)];ur=[[Z for _ in range(5)] for _ in range(5)]
        for n in degrees:
            u,v,mass=cache[n];U=[total([smul(rat(Y[k][j]),u[k]) for k in range(6)]) for j in range(5)];V=[total([smul(rat(Y[k][j]),v[k]) for k in range(6)]) for j in range(5)];R=[minus(u[j],V[j]) for j in range(5)]
            for i in range(5):
                for j in range(5):ur[i][j]=plus(ur[i][j],smul(mass,smul(U[i],R[j])))
                for j in range(i,5):fg[i][j]=plus(fg[i][j],smul(mass,smul(R[i],R[j])))
        fl=[[F(0)]*5 for _ in range(5)];fh=[[F(0)]*5 for _ in range(5)]
        for i in range(5):
            for j in range(i,5):lo,hi=bounds(fg[i][j]);fl[i][j]=fl[j][i]=lo;fh[i][j]=fh[j][i]=hi
        Nlo,prefixHi,_=loewner(fl,fh,sw);assert psd(Nlo)
        nu=d['nu'];r=d['r'];dl=d['dl'];cw0=d['cw0'];dp=d['dp'];dw=d['dw'];d2=d['d2']
        lead=[F(j==3)+F(j==4)*mu[0]-Y[0][j]-Y[1][j]-mu[0]*Y[2][j]-(F(3,2)+nu[0]-r/(2*dl))*Y[3][j]-(cw0*mu[0]+d['omega'][0])*Y[4][j] for j in range(5)]
        rem=add(add(scale(d2*d2,outer(Y[1])),scale(df*df,outer([F(j==4)-Y[2][j] for j in range(5)]))),add(scale(dp*dp,outer(Y[3])),scale(dw*dw,outer(Y[4]))))
        tailHi=add(scale(F(3,2)*T,outer(lead)),scale(12*T,rem));Nhi=add(prefixHi,tailHi)
        ce=[up(sum(abs(Y[k][j])*d['eps'][k] for k in range(6))) for j in range(5)];ec=sum(ce[j]/sw[j] for j in range(5));directE=[[up(ce[j]*sw[j]*ec) if i==j else F(0) for j in range(5)] for i in range(5)];assert psd(add(directE,outer(ce),-1))
        fresh.append(dict(trial=name,trial_basis_coefficients=ser(Y),finite_cross_intervals=ur,whole_residual_tail_Gram_upper=ser(tailHi),nominal_residual_Gram_lower=ser(Nlo),nominal_residual_Gram_upper=ser(Nhi),selected_response_action_error_Gram_upper=ser(cong(Y,d['rawE'])),direct_response_action_error_Gram_upper=ser(directE)))
    assert prior['source_D_Gram_lower']==ser(Glo) and prior['source_D_Gram_upper']==ser(Ghi)
    oldSelected=prior['selected_enclosure'];inheritedLo=mat(oldSelected,'canonical_inverse_response_lower');inheritedHi=mat(oldSelected,'canonical_inverse_response_upper');inheritedBeta=F(prior['relative_inverse_width_upper'])
    settings=[F(1,10000),F(1,3000),F(1,1000),F(1,300),F(1,100),F(1,30),F(1,10),F(1,3),F(1)]
    tailSettings=[F(1,100),F(1,10),F(1,3),F(1),F(3),F(10)]
    results=[]
    for old in sorted(fresh,key=lambda x:x['trial'],reverse=replay):
        name=old['trial'];Y=mat(old,'trial_basis_coefficients');J=[[F(i==j)-Y[i][j] for j in range(5)] for i in range(6)]
        UGlo=cong(Y,GTlo);UGhi=cong(Y,GThi);assert psd(UGhi)
        # Sym(S*D U) = (G_S + G_U - G_(S-U))/2.
        SUlo=scale(F(1,2),add(add(Glo,UGlo),cong(J,GThi),-1));SUhi=scale(F(1,2),add(add(Ghi,UGhi),cong(J,GTlo),-1))
        ur=old['finite_cross_intervals']
        ul=[[F(0)]*5 for _ in range(5)];uh=[[F(0)]*5 for _ in range(5)]
        for i in range(5):
            for j in range(i,5):
                lo,hi=bounds(smul(rat(F(1,2)),plus(ur[i][j],ur[j][i])));ul[i][j]=ul[j][i]=lo;uh[i][j]=uh[j][i]=hi
        prefixLo,prefixHi,_=loewner(ul,uh,sw)
        leadU=[Y[3][j]+mu[0]*Y[4][j] for j in range(5)]
        Utail=add(scale(2*T,outer(leadU)),scale(2*T*df*df,outer(Y[4])))
        Rtail=mat(old,'whole_residual_tail_Gram_upper');Nlo=mat(old,'nominal_residual_Gram_lower');Nhi=mat(old,'nominal_residual_Gram_upper')
        errors=[('raw_trial_triangle',mat(old,'selected_response_action_error_Gram_upper')),('response_triangle',mat(old,'direct_response_action_error_Gram_upper'))]
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
        item=dict(trial=name,trial_basis_coefficients=ser(Y),full_trial_D_Gram_upper=ser(UGhi),full_source_trial_cross_Loewner_lower=ser(SUlo),full_source_trial_cross_Loewner_upper=ser(SUhi),finite_trial_nominal_residual_cross_entry_lower=ser(ul),finite_trial_nominal_residual_cross_entry_upper=ser(uh),trial_source_tail_D_Gram_upper=ser(Utail),nominal_residual_tail_D_Gram_upper=ser(Rtail),nominal_residual_Gram_lower=ser(Nlo),nominal_residual_Gram_upper=ser(Nhi),nominal_residual_relative_Gram_upper=str(width(Nhi,Glo)),selected_variational_action_theta=str(theta),selected_variational_tail_theta=str(tailTheta),selected_variational_error_type=eName,variational_action_uncertainty_Loewner_upper=ser(actionPay),variational_tail_uncertainty_Loewner_upper=ser(tailPay),variational_response_lower=ser(Clo),variational_response_upper=ser(Chi),relative_variational_width_upper=str(cBeta),selected_residual_error_type=errorName,selected_upper_tau=str(tau),selected_lower_tau=str(sigma),actual_residual_Gram_lower=ser(Rlo),actual_residual_Gram_upper=ser(Rhi),selected_lower_type=ln,selected_upper_type=hn,canonical_inverse_response_lower=ser(lower),canonical_inverse_response_upper=ser(upper),relative_inverse_width_upper=str(beta),half_Gram_gate_matrix=ser(gate),half_Gram_gate_passed=psd(gate))
        results.append(item);print('RC191',name,'C width',float(cBeta),'inverse width',float(beta),'gate',psd(gate),flush=True)
    results.sort(key=lambda x:x['trial']);selected=min(results,key=lambda x:(F(x['relative_inverse_width_upper']),x['trial']));beta=F(selected['relative_inverse_width_upper'])
    return dict(milestone='RC191',status='PASS: same-family inverse with refined psi and w14 actions; gate separately reported',starting_commit='060f4476d36f50f4aee22cd651d08ae145a79ece',input_sha256=hs,response_source_order=prior['response_source_order'],raw_trial_basis_order=prior['raw_trial_basis_order'],source_D_Gram_lower=ser(Glo),source_D_Gram_upper=ser(Ghi),finite_prefix_last_degree=d['O'],common_eta_tail_D_energy_upper=str(T),new_psi_carrier_sha256=hs[4],new_w14_carrier_sha256=hs[1],canonical_w14_action_error_norm_upper=newW['complete_canonical_w14_action_D_error_norm_upper'],canonical_psi_action_error_norm_upper=new['canonical_psi_source_form_full_D_error_norm_upper'],individual_raw_trial_action_error_norm_upper=list(map(str,d['eps'])),raw_trial_D_Gram_Loewner_lower=ser(GTlo),raw_trial_D_Gram_Loewner_upper=ser(GThi),raw_trial_canonical_Gram_entry_lower=ser(d['kl']),raw_trial_canonical_Gram_entry_upper=ser(d['kh']),evaluated_inverse_trials=results,selected_trial=selected['trial'],selected_enclosure=selected,relative_inverse_width_upper=str(beta),previous_same_family_width_upper=str(inheritedBeta),inverse_width_improved_over_RC189=beta<inheritedBeta,certified_acceptance_ratio_upper=str(2*beta),certified_gate_margin_lower=str(F(1,2)-beta),canonical_half_Gram_inverse_width_gate_passed=selected['half_Gram_gate_passed'],same_operator_norm_and_five_response_sources_as_RC189=True,RC188_psi_carrier_attached=True,RC190_w14_endpoint_and_regular_carrier_attached=True,all_mixed_rows_and_residuals_recomputed=True,full_input_output_tails_and_complex_mixtures_paid=True,actual_five_source_canonical_inverse_response_certified=True,native_seven_source_frame_changed=False,Stage_I_closed=False,Stage_I_completion_ratio=None,original_Weil_or_augmented_actions_performed=False,RH=False,F4=False,Lean=False,next_cursor='use remaining same-family residual and uncertainty budgets to select the next precision pass if the gate is open; native v10/z_b6/t10 remain subsequent coverage obligations')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');args=p.parse_args();result=run(inputs(),args.replay)
    if args.replay:assert json.loads(Path(args.output).read_text())==result
    else:Path(args.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC191 PASS: two-refined-action same-family canonical inverse')
