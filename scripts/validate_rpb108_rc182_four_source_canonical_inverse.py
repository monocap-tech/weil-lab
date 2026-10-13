"""RC182: materialized infinite-psi carrier and correlated four-source inverse."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc129_four_vector_joint_moment import inv,mm,cong,add,transpose
from validate_rpb108_rc134_correlated_six_input_covariance import smul
from validate_rpb108_rc177_three_source_canonical_action_gram import scale,mat,width

def outer(x):return [[a*b for b in x] for a in x]
def total(xs):
    s=Z
    for x in xs:s=plus(s,x)
    return s

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];dats=list(map(json.loads,raw));hs=[hashlib.sha256(b).hexdigest() for b in raw]
    psiContract,prior,new,previous,three,fnew,p2,p0,joint,wold,old,metric,physical,endpoint,oldPsi,conditional,difference=dats
    assert [x['milestone'] for x in dats]==['RC181','RC180','RC179','RC178','RC177','RC176','RC172','RC171','RC129','RC128','RC127','RC121','RC175','RC154','RC130','RC151','RC153']
    assert prior['input_sha256']==hs[2:13] and endpoint['input_sha256']==[hs[8],hs[14],hs[15],hs[16]]
    assert psiContract['input_sha256'][0]==hs[1] and psiContract['input_sha256'][1]==hs[4] and psiContract['input_sha256'][4:6]==[hs[8],hs[13]]
    # Reproduce the historical complete Cpsi finite and analytic generator.
    path=Path(__file__).with_name('validate_rpb108_rc154_centered_analytic_tail_action.py');src=path.read_text().split("\nif __name__=='__main__':")[0]
    marker="    deltaError=F(difference['full_Cdelta_trial_D_norm_error_upper'])";assert src.count(marker)==1
    ns={'__file__':str(path)};exec(compile(src.replace(marker,'    return locals()',1),'RC154 materialization','exec'),ns)
    ep=ns['run']([paths[i] for i in [8,14,15,16]],replay)
    digest=hashlib.sha256(json.dumps(ep['payload'],sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert digest==endpoint['finite_action_trial_center_radius_sha256']
    assert ep['moments']==endpoint['analytic_output_moment_intervals'] and str(ep['error'])==endpoint['full_Cpsi_trial_D_norm_error_upper']
    cpsi={x['degree']:F(x['center']) for x in ep['payload']};nu=[F(x['center']) for x in ep['moments'][:25]];lamPsi=ep['lam']
    assert lamPsi==8190*8191 and len(nu)==25 and min(nu)>0
    print('RC182 historical Cpsi coefficient and moment hashes reproduced',flush=True)
    # Recover the four-direction carrier from RC180 without changing it.
    path=Path(__file__).with_name('validate_rpb108_rc180_residual_enriched_canonical_inverse.py');src=path.read_text().split("\nif __name__=='__main__':")[0]
    marker='    representedCross=[[sum(bounds(mixed[j][i]))/2 for j in range(3)] for i in range(4)]';assert src.count(marker)==1
    ns={'__file__':str(path)};exec(compile(src.replace(marker,'    return locals()',1),'RC180 carrier recovery','exec'),ns)
    base=ns['run'](paths[2:13],replay);oldCache=base['cache'];native=base['d'];mu=native['mu'];lam=native['lam'];r=F(789,125)
    O=16382;D=ep['dn'];s=ep['s'];sourcePsi={n:div(rat(F(2*n+1,n*(n+1))),D[n]) for n in range(990,O+1,2)}
    indices=[0,1,2,4];cache={};mixed=[[Z for _ in range(5)] for _ in range(5)];nominal=[[Z for _ in range(5)] for _ in range(5)]
    degrees=list(range(0,O+1,2));degrees=degrees[::-1] if replay else degrees
    for n in degrees:
        if n in oldCache:u4,v4,mass=oldCache[n]
        else:
            eta=div(rat(F(2*n+1,n*(n+1))),D[n]);z=n*(n+1)
            u4=[Z]*4;v4=[eta,smul(rat(1/(1-F(6,z))),eta),smul(rat(sum(mu[k]*(F(lam,z))**k for k in range(15))),eta),Z]
            mass=mul(rat(2*B/F(2*n+1)),D[n])
        psi=sourcePsi.get(n,Z);u=u4+[psi]
        vpsi=plus(rat(cpsi[n]),smul(minus(rat(F(3,2) if n>=8192 else F(1)),div(rat(r),D[n])),psi))
        v=v4+[vpsi];cache[n]=(u,v,mass)
        for i in range(5):
            for j in range(5):mixed[i][j]=plus(mixed[i][j],smul(mass,smul(u[i],v[j])))
            for j in range(i,5):nominal[i][j]=plus(nominal[i][j],smul(mass,smul(v[i],v[j])))
    Glo=mat(psiContract,'four_source_D_Gram_lower');Ghi=mat(psiContract,'four_source_D_Gram_upper')
    gl,gh=Glo[3][3],Ghi[3][3]
    GTlo=[row+[F(0)] for row in mat(prior,'enriched_trial_D_Gram_Loewner_lower')]+[[F(0)]*4+[gl]]
    GThi=[row+[F(0)] for row in mat(prior,'enriched_trial_D_Gram_Loewner_upper')]+[[F(0)]*4+[gh]]
    assert psd(GTlo)
    eps=list(map(F,three['individual_full_action_D_error_norm_upper']))+[F(new['complete_actual_canonical_q_action_D_error_norm_upper']),F(psiContract['canonical_psi_source_form_full_D_error_norm_upper'])]
    weights=[sqrtup(GThi[i][i]) for i in range(5)];sourceWeights=[sqrtup(Ghi[i][i]) for i in range(4)]
    first=O+2;z=first*(first+1);Dfirst=F(ep['dn'][O][0]);T=up(B/(Dfirst*(O-1)*O))
    amps=[F(1),1/(1-F(6,z)),sum(mu[k]*F(lam,z)**k for k in range(15)),F(0),F(3,2)+sum(nu[k]*F(lamPsi,z)**k for k in range(25))]
    qeLo=[[F(0)]*5 for _ in range(5)];qeHi=[[F(0)]*5 for _ in range(5)]
    meLo=[[F(0)]*5 for _ in range(5)];meHi=[[F(0)]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            lo,hi=bounds(mixed[i][j]);meLo[i][j]=lo;meHi[i][j]=up(hi+(amps[j]*T if i==4 else 0))
        for j in range(i,5):
            lo,hi=bounds(nominal[i][j]);qeLo[i][j]=qeLo[j][i]=lo;qeHi[i][j]=qeHi[j][i]=up(hi+amps[i]*amps[j]*T)
    Qlo,Qhi,_=loewner(qeLo,qeHi,weights);assert psd(Qlo)
    keLo=[[F(0)]*5 for _ in range(5)];keHi=[[F(0)]*5 for _ in range(5)]
    for i in range(5):
        for j in range(i,5):
            choices=[]
            for row,col in [(i,j),(j,i)]:
                err=up(weights[row]*eps[col]);choices.append((down(meLo[row][col]-err),up(meHi[row][col]+err)))
            if i<4 and j<4:choices.append((F(prior['enriched_trial_canonical_Gram_entry_lower'][i][j]),F(prior['enriched_trial_canonical_Gram_entry_upper'][i][j])))
            lo=max(x for x,y in choices);hi=min(y for x,y in choices);assert lo<=hi
            keLo[i][j]=keLo[j][i]=lo;keHi[i][j]=keHi[j][i]=hi
    KTlo,KThi,_=loewner(keLo,keHi,weights);a=F(metric['actual_canonical_diagonal_metric_lower'])
    assert psd(add(KTlo,scale(a,GThi),-1)) and psd(add(scale(2,GTlo),KThi,-1))
    C=sum(eps[i]/weights[i] for i in range(5));E0=[[up(eps[i]*weights[i]*C) if i==j else F(0) for j in range(5)] for i in range(5)]
    assert psd(add(E0,outer(eps),-1))
    GTmid=scale(F(1,2),add(GTlo,GThi));KTmid=scale(F(1,2),add(KTlo,KThi));Qmid=scale(F(1,2),add(qeLo,qeHi))
    YG=mm(inv(KTmid),[[row[j] for j in indices] for row in GTmid]);YR=mm(inv(Qmid),[[(meLo[j][i]+meHi[j][i])/2 for j in indices] for i in range(5)])
    trials={mode:[[down(x,10**30) for x in row] for row in Y] for mode,Y in [('Galerkin',YG),('least_residual',YR)]}
    delta2=F(6,z-6);deltaf=sum(mu[k]*F(lam,z)**k for k in range(1,15));deltaPsi=sum(nu[k]*F(lamPsi,z)**k for k in range(1,25))+r/(2*Dfirst)
    results=[];chosen=None
    for mode in sorted(trials,reverse=replay):
        Y=trials[mode];Jminus=[[F(i==indices[j])-Y[i][j] for j in range(4)] for i in range(5)]
        Clo=add(add(Glo,cong(Jminus,GThi),-1),cong(Y,add(GTlo,KThi,-1)))
        Chi=add(add(Ghi,cong(Jminus,GTlo),-1),cong(Y,add(GThi,KTlo,-1)));assert psd(Clo)
        fg=[[Z for _ in range(4)] for _ in range(4)]
        for n in degrees:
            u,v,mass=cache[n];res=[minus(u[indices[i]],total([smul(rat(Y[j][i]),v[j]) for j in range(5)])) for i in range(4)]
            for i in range(4):
                for j in range(i,4):fg[i][j]=plus(fg[i][j],smul(mass,smul(res[i],res[j])))
        fl=[[F(0)]*4 for _ in range(4)];fh=[[F(0)]*4 for _ in range(4)]
        for i in range(4):
            for j in range(i,4):
                lo,hi=bounds(fg[i][j]);fl[i][j]=fl[j][i]=lo;fh[i][j]=fh[j][i]=hi
        Nlo,prefixHi,_=loewner(fl,fh,sourceWeights);assert psd(Nlo)
        b=[F(i==3)-Y[0][i]-Y[1][i]-mu[0]*Y[2][i]-(F(3,2)+nu[0]-r/(2*Dfirst))*Y[4][i] for i in range(4)]
        rem=add(add(scale(delta2**2,outer(Y[1])),scale(deltaf**2,outer(Y[2]))),scale(deltaPsi**2,outer(Y[4])))
        tailTau=F(1,2);tailHi=add(scale((1+tailTau)*T,outer(b)),scale(3*(1+1/tailTau)*T,rem))
        Nhi=add(prefixHi,tailHi);E=cong(Y,E0);assert psd(add(Nhi,Nlo,-1))
        taus=[F(1,1000),F(1,300),F(1,100),F(1,30),F(1,10),F(1,3),F(1),F(3)]
        sigmas=[F(0),F(1,100),F(1,30),F(1,10),F(1,3),F(1,2)]
        if replay:taus.reverse();sigmas.reverse()
        best=None
        for tau in taus:
            Rhi=add(scale(1+tau,Nhi),scale(1+1/tau,E));upper=add(Chi,scale(1/a,Rhi))
            for sigma in sigmas:
                Rlo=[[F(0)]*4 for _ in range(4)] if sigma==0 else add(scale(1-sigma,Nlo),scale(-(1/sigma-1),E))
                if not psd(Rlo):continue
                lower=add(Clo,scale(F(1,2),Rlo));gap=add(upper,lower,-1);assert psd(lower) and psd(gap)
                beta=width(gap,Glo);key=(beta,tau,sigma)
                if best is None or key<best[0]:best=(key,lower,upper,Rlo,Rhi)
        (beta,tau,sigma),lower,upper,Rlo,Rhi=best
        assert psd(add(lower,scale(F(1,2),Glo),-1)) and psd(add(scale(1/a,Ghi),upper,-1))
        gate=add(scale(F(1,2),Glo),add(upper,lower,-1),-1);warm=width(scale(1/a,Rhi),lower)
        item=dict(trial=mode,trial_basis_coefficients=ser(Y),variational_response_lower=ser(Clo),variational_response_upper=ser(Chi),nominal_residual_Gram_lower=ser(Nlo),nominal_residual_Gram_upper=ser(Nhi),full_residual_tail_Gram_upper=ser(tailHi),transformed_action_error_Gram_upper=ser(E),
          selected_actual_residual_Gram_lower=ser(Rlo),selected_actual_residual_Gram_upper=ser(Rhi),selected_upper_tau=str(tau),selected_lower_tau=str(sigma),canonical_inverse_response_lower=ser(lower),canonical_inverse_response_upper=ser(upper),relative_inverse_width_upper=str(beta),half_Gram_gate_matrix=ser(gate),half_Gram_gate_passed=psd(gate),canonical_warmstart_relative_true_image_norm_upper=str(sqrtup(warm)))
        results.append(item)
        if chosen is None or (beta,mode)<chosen[0]:chosen=((beta,mode),item)
        print('RC182 four-source trial',mode,'width',float(beta),'half gate',psd(gate),flush=True)
    results.sort(key=lambda x:x['trial']);selected=chosen[1];beta=F(selected['relative_inverse_width_upper']);margin=F(1,2)-beta
    dashboard=dict(response_source_family=['P0','P2','f0','psi0'],inverse_trial_basis=['P0','P2','f0','q','psi0'],evaluated_parity='even',relative_inverse_width_upper=str(beta),local_inverse_width_threshold='1/2',certified_acceptance_ratio_upper=str(2*beta),certified_gate_margin_lower=str(margin),half_Gram_contract_closed=selected['half_Gram_gate_passed'],
      previous_three_source_width=prior['relative_inverse_width_upper'],previous_three_and_current_four_source_widths_directly_comparable=False,Stage_I_completion_ratio=None,Stage_I_closed=False)
    coefficients=dict(milestone='RC182-Cpsi-carrier',degrees='even 0..16382 in array order',finite_Cpsi_coefficient_centers=[str(cpsi[n]) for n in range(0,O+1,2)],historical_center_radius_sha256=digest,analytic_output_moments=endpoint['analytic_output_moment_intervals'],analytic_output_lambda=str(lamPsi),centered_input_tail_definition='(1/2)*psi on even n>=8192',whole_Cpsi_error_norm_upper=endpoint['full_Cpsi_trial_D_norm_error_upper'])
    result=dict(milestone='RC182',status='PASS: complete correlated actual four-source canonical inverse; gate result recorded explicitly',starting_commit='68d742a940ed624c7004dc7b39e99a5ed3e67e58',input_sha256=hs,response_source_order=['P0','P2','f0','psi0'],trial_basis_order=['P0','P2','f0','RC179 q','psi0'],
      Cpsi_coefficients_rematerialized=True,historical_Cpsi_center_radius_sha256=digest,finite_prefix_last_degree=O,first_omitted_even_degree=first,common_eta_tail_D_energy_upper=str(T),
      negative_r_psi_tail_midpoint_center=str(r/(2*Dfirst)),psi_tail_remainder_upper=str(deltaPsi),full_input_and_output_tails_and_mixed_errors_paid=True,
      source_D_Gram_lower=ser(Glo),source_D_Gram_upper=ser(Ghi),trial_D_Gram_lower=ser(GTlo),trial_D_Gram_upper=ser(GThi),trial_canonical_Gram_entry_lower=ser(keLo),trial_canonical_Gram_entry_upper=ser(keHi),trial_canonical_Gram_Loewner_lower=ser(KTlo),trial_canonical_Gram_Loewner_upper=ser(KThi),represented_action_Gram_entry_lower=ser(qeLo),represented_action_Gram_entry_upper=ser(qeHi),full_correlated_trial_action_error_Gram_upper=ser(E0),
      evaluated_inverse_trials=results,selected_trial=selected['trial'],selected_enclosure=selected,relative_inverse_width_upper=str(beta),canonical_half_Gram_inverse_width_gate_passed=selected['half_Gram_gate_passed'],completion_dashboard=dashboard,
      all_real_and_complex_four_source_inverse_mixtures_paid=True,actual_four_source_canonical_inverse_response_certified=True,native_seven_source_frame_changed=False,full_native_seven_source_inverse_certified=False,Stage_I_closed=False,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='continue actual canonical action and inverse coverage toward w14/v10/z_b6/t10, while recording acceptance and coverage separately')
    return result,coefficients

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--carrier-output',required=True);p.add_argument('--replay',action='store_true');p.add_argument('inputs',nargs=17)
    args=p.parse_args();result,carrier=run(args.inputs,args.replay)
    if args.replay:
        assert json.loads(Path(args.output).read_text())==result and json.loads(Path(args.carrier_output).read_text())==carrier
    else:
        Path(args.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n');Path(args.carrier_output).write_text(json.dumps(carrier,sort_keys=True,indent=2)+'\n')
    print('RC182 PASS: materialized infinite-psi carrier and four-source canonical inverse')
