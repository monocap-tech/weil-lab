"""RC199: complete six-response inverse with seven paid raw trial actions."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,bounds,up,sqrtup,psd,ser,loewner,down
from validate_rpb108_rc129_four_vector_joint_moment import inv,mm,cong,add
from validate_rpb108_rc134_correlated_six_input_covariance import smul
from validate_rpb108_rc177_three_source_canonical_action_gram import mat,scale,width
from validate_rpb108_rc186_residual_enriched_five_source_inverse import outer,total
from validate_rpb108_rc198_v10_mixed_action_rows import inputs as mixed_inputs

def inputs():
    base=Path(__file__).resolve().parents[1]/'certificates'
    return [base/'rpb108_rc198_v10_mixed_action_rows.json']+mixed_inputs()

def run(paths,replay=False):
    raw=[p.read_bytes() for p in paths];data=list(map(json.loads,raw));hs=[hashlib.sha256(b).hexdigest() for b in raw];joint=data[0]
    assert joint['milestone']=='RC198' and joint['input_sha256']==hs[1:]
    path=Path(__file__).with_name('validate_rpb108_rc198_v10_mixed_action_rows.py');src=path.read_text().split("\nif __name__=='__main__':")[0]
    marker='    DG=[Z]*7;left=[Z]*7;right=[Z]*7;AQ=[Z]*7';assert src.count(marker)==1;src=src.replace(marker,'    expandedCache={}\n'+marker)
    marker='        uu=u+[vn];vv=v+[av]';assert src.count(marker)==1;src=src.replace(marker,marker+'\n        expandedCache[n]=(uu,vv,mass)')
    marker="    return dict(milestone='RC198'";assert src.count(marker)==1;src=src.replace(marker,"    return locals()\n"+marker)
    ns={'__file__':str(path)};exec(compile(src,'RC199 full expanded carrier replay','exec'),ns);d=ns['run'](paths[1:],replay)
    assert ser(d['Glo'])==joint['raw_trial_D_Gram_Loewner_lower'] and ser(d['actionLo'])==joint['nominal_raw_action_Gram_entry_lower']
    keep=[0,1,2,3,4,6];GSlo=mat(joint,'expanded_response_source_D_Gram_lower');GShi=mat(joint,'expanded_response_source_D_Gram_upper');GTlo=d['Glo'];GThi=d['Ghi'];Gi=inv(GSlo);sw=[sqrtup(GShi[i][i]) for i in range(6)]
    mid=lambda L,H:scale(F(1,2),add(L,H))
    KM=mid(d['kl'],d['kh']);QM=mid(d['actionLo'],d['actionHi']);GM=mid(d['gl'],d['gh'])
    pick=lambda A:[[A[i][j] for j in keep] for i in range(7)]
    trials={'Galerkin':mm(inv(KM),pick(GM)),'least_residual':mm(inv(QM),pick(KM))}
    trials={n:[[down(x,10**30) for x in row] for row in Y] for n,Y in trials.items()}
    eps=d['eps'];old=d['d'];T=d['T'];z=d['z'];dl=F(old['D'][old['O']][0]);r=old['r'];a=old['a'];mu=old['mu'];nu=old['nu'];omega=old['omega'];qmom=old['qmom']
    dv=sum(d['mu'][k]*F(d['lam'],z)**k for k in range(1,11));dc=sum(d['mom'][k]*F(d['epLam'],z)**k for k in range(1,25));vlead=(F(3,2)-r/dl)*d['mu'][0]+d['mom'][0];vm=F(3,2)*dv+r*d['mu'][0]/dl+dc
    df=old['df'];d2=old['d2'];dp=old['dp'];dw=old['dw'];dq=sum(abs(qmom[k])*F(old['qlam'],z)**k for k in range(1,25))
    results=[]
    for name in sorted(trials,reverse=replay):
        Y=trials[name];gg=[[Z]*6 for _ in range(6)];ur=[[Z]*6 for _ in range(6)]
        for n in old['degrees']:
            u,v,mass=d['expandedCache'][n];U=[total([smul(rat(Y[k][j]),u[k]) for k in range(7)]) for j in range(6)];V=[total([smul(rat(Y[k][j]),v[k]) for k in range(7)]) for j in range(6)];R=[minus(u[keep[j]],V[j]) for j in range(6)]
            if n%16384==0:print('RC199',name,'residual block',n,flush=True)
            for i in range(6):
                for j in range(6):ur[i][j]=plus(ur[i][j],smul(mass,smul(U[i],R[j])))
                for j in range(i,6):gg[i][j]=plus(gg[i][j],smul(mass,smul(R[i],R[j])))
        nl=[[F(0)]*6 for _ in range(6)];nh=[[F(0)]*6 for _ in range(6)];ul=[[F(0)]*6 for _ in range(6)];uh=[[F(0)]*6 for _ in range(6)]
        for i in range(6):
            for j in range(i,6):
                lo,hi=bounds(gg[i][j]);nl[i][j]=nl[j][i]=lo;nh[i][j]=nh[j][i]=hi
                lo,hi=bounds(smul(rat(F(1,2)),plus(ur[i][j],ur[j][i])));ul[i][j]=ul[j][i]=lo;uh[i][j]=uh[j][i]=hi
        Nlo,prefixHi,_=loewner(nl,nh,sw);assert psd(Nlo)
        lead=[F(j==3)+mu[0]*F(j==4)+d['mu'][0]*F(j==5)-Y[0][j]-Y[1][j]-mu[0]*Y[2][j]-(F(3,2)+nu[0]-r/(2*dl))*Y[3][j]-(old['cw0']*mu[0]+omega[0])*Y[4][j]-qmom[0]*Y[5][j]-vlead*Y[6][j] for j in range(6)]
        rem=scale(d2*d2,outer(Y[1]))
        for factor,vec in [(df,[F(j==4)-Y[2][j] for j in range(6)]),(dp,Y[3]),(dw,Y[4]),(dq,Y[5]),(dv,[F(j==5) for j in range(6)]),(vm,Y[6])]:rem=add(rem,scale(factor*factor,outer(vec)))
        Rtail=add(scale(F(3,2)*T,outer(lead)),scale(21*T,rem));Nhi=add(prefixHi,Rtail)
        leadU=[Y[3][j]+mu[0]*Y[4][j]+d['mu'][0]*Y[6][j] for j in range(6)]
        Utail=add(scale(2*T,outer(leadU)),scale(4*T,add(scale(df*df,outer(Y[4])),scale(dv*dv,outer(Y[6])))))
        UGlo=cong(Y,GTlo);UGhi=cong(Y,GThi);J=[[F(i==keep[j])-Y[i][j] for j in range(6)] for i in range(7)]
        SUlo=scale(F(1,2),add(add(GSlo,UGlo),cong(J,GThi),-1));SUhi=scale(F(1,2),add(add(GShi,UGhi),cong(J,GTlo),-1));crossLo,crossHi,_=loewner(ul,uh,sw)
        dual=[sum(Y[k][i]*Gi[i][j]*Y[k][j] for i in range(6) for j in range(6)) for k in range(7)];assert min(dual)>=0
        weights=[1/sqrtup(x) if x else F(1) for x in dual];factor=sum(eps[k]/weights[k] for k in range(7));E=[[sum(factor*eps[k]*weights[k]*Y[k][i]*Y[k][j] for k in range(7)) for j in range(6)] for i in range(6)]
        diagonal=[[factor*eps[i]*weights[i] if i==j else F(0) for j in range(7)] for i in range(7)];assert psd(add(diagonal,outer(eps),-1))
        cBest=None
        for theta in ([F(1,n) for n in [3000,1000,300,100,30,10,3,1]][::-1] if replay else [F(1,n) for n in [3000,1000,300,100,30,10,3,1]]):
            for tt in ([F(1,10),F(1,3),F(1)][::-1] if replay else [F(1,10),F(1,3),F(1)]):
                pay=add(add(scale(theta,UGhi),scale(1/(4*theta),E)),add(scale(tt,Utail),scale(1/(4*tt),Rtail)))
                Clo=add(add(SUlo,crossLo),pay,-1);Chi=add(add(SUhi,crossHi),pay);gap=add(Chi,Clo,-1)
                if cBest is not None and not psd(add(scale(cBest[0][0],GSlo),gap,-1)):continue
                cb=width(gap,GSlo);key=(cb,theta,tt)
                if cBest is None or key<cBest[0]:cBest=(key,Clo,Chi,pay)
        (cb,theta,tt),Clo,Chi,pay=cBest;best=None
        taus=[F(1,30),F(1,10),F(1,3),F(1),F(3)];sigmas=[F(0),F(1,10),F(1,3),F(1,2)]
        for tau in (taus[::-1] if replay else taus):
            Rhi=add(scale(1+tau,Nhi),scale(1+1/tau,E));upper=add(Chi,scale(1/a,Rhi))
            for sigma in (sigmas[::-1] if replay else sigmas):
                Rlo=[[F(0)]*6 for _ in range(6)] if sigma==0 else add(scale(1-sigma,Nlo),scale(-(1/sigma-1),E))
                if not psd(Rlo):continue
                lower=add(Clo,scale(F(1,2),Rlo))
                for ln,lc in [('refined',lower),('structural',scale(F(1,2),GSlo))]:
                    for hn,hc in [('refined',upper),('structural',scale(1/a,GShi))]:
                        if not psd(lc):continue
                        gap=add(hc,lc,-1)
                        if not psd(gap):continue
                        if best is not None and not psd(add(scale(best[0][0],GSlo),gap,-1)):continue
                        beta=width(gap,GSlo);key=(beta,tau,sigma,ln,hn)
                        if best is None or key<best[0]:best=(key,lc,hc,Rlo,Rhi)
        (beta,tau,sigma,ln,hn),lower,upper,Rlo,Rhi=best;gate=add(scale(F(1,2),GSlo),add(upper,lower,-1),-1)
        assert psd(add(scale(beta,GSlo),add(upper,lower,-1),-1))
        results.append(dict(trial=name,trial_basis_coefficients=ser(Y),nominal_residual_Gram_lower=ser(Nlo),nominal_residual_Gram_upper=ser(Nhi),nominal_residual_tail_Gram_upper=ser(Rtail),trial_source_tail_Gram_upper=ser(Utail),adaptive_action_error_Gram_upper=ser(E),adaptive_triangle_weights=list(map(str,weights)),variational_response_lower=ser(Clo),variational_response_upper=ser(Chi),variational_uncertainty_payment=ser(pay),relative_variational_width_upper=str(cb),selected_action_theta=str(theta),selected_tail_theta=str(tt),actual_residual_Gram_lower=ser(Rlo),actual_residual_Gram_upper=ser(Rhi),selected_upper_tau=str(tau),selected_lower_tau=str(sigma),selected_lower_type=ln,selected_upper_type=hn,canonical_inverse_response_lower=ser(lower),canonical_inverse_response_upper=ser(upper),relative_inverse_width_upper=str(beta),half_Gram_gate_matrix=ser(gate),half_Gram_gate_passed=psd(gate),nominal_residual_relative_Gram_upper=str(width(Nhi,GSlo)),adaptive_action_error_relative_Gram_upper=str(width(E,GSlo))))
        print('RC199',name,'inverse width',float(beta),'gate',psd(gate),flush=True)
    results.sort(key=lambda x:x['trial']);selected=min(results,key=lambda x:(F(x['relative_inverse_width_upper']),x['trial']));beta=F(selected['relative_inverse_width_upper'])
    witnesses=[]
    for denominator in [1,10,100,1000]:
        for j in range(6):
            probe=[F(i==j) for i in range(6)];value=sum(probe[i]*F(selected['half_Gram_gate_matrix'][i][k])*probe[k] for i in range(6) for k in range(6))
            if value<0:witnesses.append(dict(coefficients=list(map(str,probe)),gate_quadratic=str(value)));break
        if witnesses:break
    return dict(milestone='RC199',status='PASS: complete six-source canonical inverse; acceptance separately reported',starting_commit='af1ecbf6e1743eb378771c777857ae74c699c602',input_sha256=hs,response_source_order=joint['response_source_order'],raw_trial_basis_order=joint['raw_trial_basis_order'],source_D_Gram_lower=ser(GSlo),source_D_Gram_upper=ser(GShi),finite_prefix_last_degree=d['O'],evaluated_inverse_trials=results,selected_trial=selected['trial'],selected_enclosure=selected,relative_inverse_width_upper=str(beta),certified_acceptance_ratio_upper=str(2*beta),certified_gate_margin_lower=str(F(1,2)-beta),canonical_half_Gram_inverse_width_gate_passed=selected['half_Gram_gate_passed'],gate_failure_coordinate_witnesses=witnesses,actual_six_source_canonical_inverse_response_certified=True,all_finite_mixed_residuals_and_infinite_tails_paid=True,complex_response_mixtures_paid=True,accepted_five_source_inverse_unchanged=True,source_family_expanded_not_same_family_precision_comparison=True,Stage_I_closed=False,Stage_I_completion_ratio=None,RH=False,F4=False,Lean=False,next_cursor='refine v10 action or enrich expanded residual if gate fails; otherwise extend native z_b6/t10 coverage')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');a=p.parse_args();r=run(inputs(),a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC199 PASS')
