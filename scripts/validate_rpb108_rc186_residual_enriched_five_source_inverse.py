"""RC186: paid q185 enrichment of the unchanged five-source inverse target."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc129_four_vector_joint_moment import inv,mm,cong,add,transpose
from validate_rpb108_rc134_correlated_six_input_covariance import smul
from validate_rpb108_rc177_three_source_canonical_action_gram import scale,mat,width
from validate_rpb108_rc185_five_source_focus_action import inputs as prior_inputs

def outer(x):return [[a*b for b in x] for a in x]
def total(xs):
    out=Z
    for x in xs:out=plus(out,x)
    return out

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];data=list(map(json.loads,raw));hs=[hashlib.sha256(b).hexdigest() for b in raw]
    new,prior=data[:2];assert new['milestone']=='RC185' and prior['milestone']=='RC184' and new['input_sha256']==hs[1:]
    src=Path(__file__).with_name('validate_rpb108_rc184_five_source_canonical_inverse.py').read_text().split("\nif __name__=='__main__':")[0]
    start=src.index('        for i in range(6):\n            for j in range(6):mixed');stop=src.index('    first=O+2;',start)
    src=src[:start]+"    return locals()\n"+src[stop:];ns={};exec(compile(src,'RC184 immutable coefficient carriers','exec'),ns)
    d=ns['run'](paths[2:20],replay)
    O=d['O'];mu=d['mu'];nu=d['nu'];lam=d['lam'];lamPsi=d['lamPsi'];D=d['D'];r=d['r'];a=d['a']
    q={x['degree']:F(x['coefficient_center']) for x in new['finite_focus_direction']}
    vq=q.copy()
    for rows in [new['endpoint_action_polynomial'],new['negative_r_D_inverse_direction_polynomial'],new['regular_action']['D_inverse_regular_polynomial']]:
        for row in rows:vq[row['degree']]=vq.get(row['degree'],F(0))+F(row['coefficient_center'])
    eps=list(map(F,data[10]['individual_full_action_D_error_norm_upper']))+[F(data[6]['canonical_psi_source_form_full_D_error_norm_upper']),F(data[2]['complete_canonical_w14_action_D_error_norm_upper']),F(new['complete_actual_canonical_q_action_D_error_norm_upper'])]
    cache={};gg=[[Z for _ in range(6)] for _ in range(6)];qq=[[Z for _ in range(6)] for _ in range(6)];mixed=[[Z for _ in range(6)] for _ in range(6)]
    degrees=list(range(0,O+1,2));degrees=degrees[::-1] if replay else degrees
    for n in degrees:
        u,v,mass=d['cache'][n];u=[u[i] for i in [0,1,2,4,5]]+[rat(q.get(n,F(0)))];v=[v[i] for i in [0,1,2,4,5]]+[rat(vq.get(n,F(0)))];cache[n]=(u,v,mass)
        for i in range(6):
            for j in range(6):mixed[i][j]=plus(mixed[i][j],smul(mass,smul(u[i],v[j])))
            for j in range(i,6):
                gg[i][j]=plus(gg[i][j],smul(mass,smul(u[i],u[j])));qq[i][j]=plus(qq[i][j],smul(mass,smul(v[i],v[j])))
        if n%4096==0:print('RC186 mixed block',n,flush=True)
    z=(O+2)*(O+3);dl=F(D[O][0]);T=F(prior['common_eta_tail_D_energy_upper'])
    Aw=sum(mu[k]*F(lam,z)**k for k in range(15));Ap=F(3,2)+sum(nu[k]*F(lamPsi,z)**k for k in range(25))
    sa=[F(0),F(0),F(0),F(1),Aw,F(0)];va=[F(1),1/(1-F(6,z)),Aw,Ap,F(3,2)*Aw,F(0)]
    gl=[[F(0)]*6 for _ in range(6)];gh=[[F(0)]*6 for _ in range(6)];ql=[[F(0)]*6 for _ in range(6)];qh=[[F(0)]*6 for _ in range(6)];ml=[[F(0)]*6 for _ in range(6)];mh=[[F(0)]*6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            lo,hi=bounds(mixed[i][j]);ml[i][j]=lo;mh[i][j]=up(hi+sa[i]*va[j]*T)
        for j in range(i,6):
            lo,hi=bounds(gg[i][j]);gl[i][j]=gl[j][i]=lo;gh[i][j]=gh[j][i]=up(hi+sa[i]*sa[j]*T)
            lo,hi=bounds(qq[i][j]);ql[i][j]=ql[j][i]=lo;qh[i][j]=qh[j][i]=up(hi+va[i]*va[j]*T)
    # Intersections are ENTRY enclosures, never substituted Loewner endpoints.
    for i in range(5):
        for j in range(5):
            ni={0:0,2:2,3:1,4:3}.get(i);nj={0:0,2:2,3:1,4:3}.get(j)
            if ni is not None and nj is not None:
                gl[i][j]=max(gl[i][j],F(data[14]['actual_D_Gram_entry_lower'][ni][nj]));gh[i][j]=min(gh[i][j],F(data[14]['actual_D_Gram_entry_upper'][ni][nj]))
            assert gl[i][j]<=gh[i][j]
    gl[1][2]=gl[2][1]=gh[1][2]=gh[2][1]=2*B/6
    gl[5][5]=max(gl[5][5],F(new['finite_focus_D_energy_lower']));gh[5][5]=min(gh[5][5],F(new['finite_focus_D_energy_upper']));assert gl[5][5]<=gh[5][5]
    Glo=mat(prior,'source_D_Gram_lower');Ghi=mat(prior,'source_D_Gram_upper');sw=[sqrtup(Ghi[i][i]) for i in range(5)]
    GM=scale(F(1,2),add(gl,gh));QM=scale(F(1,2),add(ql,qh))
    # Rational D-projection selects an invertible change of TRIAL coordinates.
    # Its actual overlaps and action errors are always paid after selection.
    projection=mm(inv([row[:5] for row in GM[:5]]),[[GM[i][5]] for i in range(5)])
    b=[down(row[0],10**30) for row in projection]
    residualEnergy=GM[5][5]-2*sum(b[i]*GM[i][5] for i in range(5))+sum(b[i]*GM[i][j]*b[j] for i in range(5) for j in range(5))
    assert residualEnergy>0
    normalization=sqrtup(residualEnergy)
    A=[[F(i==j) for j in range(6)] for i in range(6)]
    for i in range(5):A[i][5]=-b[i]/normalization
    A[5][5]=1/normalization
    transformedGM=cong(A,GM);transformedQM=cong(A,QM)
    tgLo,tgHi,_=loewner(gl,gh,[sqrtup(gh[i][i]) for i in range(6)])
    # This check controls actual independence even when selected coordinates
    # have only approximately orthogonal centers.
    transformedGramLo=cong(A,tgLo);assert psd(transformedGramLo)
    inv(transformedGramLo)  # PSD and nonsingular certify strict positivity.
    cross=[[(ml[j][i]+mh[j][i])/2 for j in range(5)] for i in range(6)]
    transformedCross=mm(transpose(A),cross)
    enriched=mm(A,mm(inv(transformedQM),transformedCross))
    trials={'enriched_least_residual':[[down(x,10**30) for x in row] for row in enriched],
            'baseline_least_residual':mat(prior['selected_enclosure'],'trial_basis_coefficients')+[[F(0)]*5]}
    # Actual symmetric first-moment rows, including the new direction, remain
    # independently reviewable; no strong adverse floor is required to select Y.
    kl=[[F(0)]*6 for _ in range(6)];kh=[[F(0)]*6 for _ in range(6)];tw=[sqrtup(gh[i][i]) for i in range(6)]
    for i in range(6):
        for j in range(i,6):
            intervals=[(down(ml[i][j]-tw[i]*eps[j]),up(mh[i][j]+tw[i]*eps[j])),(down(ml[j][i]-tw[j]*eps[i]),up(mh[j][i]+tw[j]*eps[i]))]
            if i<5 and j<5:intervals.append((F(prior['trial_canonical_Gram_entry_lower'][i][j]),F(prior['trial_canonical_Gram_entry_upper'][i][j])))
            if i==j==5:intervals.append((F(new['actual_q_canonical_pairing_lower']),F(new['actual_q_canonical_pairing_upper'])))
            lo=max(x for x,y in intervals);hi=min(y for x,y in intervals);assert lo<=hi;kl[i][j]=kl[j][i]=lo;kh[i][j]=kh[j][i]=hi
    KTlo,KThi,_=loewner(kl,kh,tw)
    rawErrorSum=sum(eps[i]/tw[i] for i in range(6))
    rawE=[[up(eps[i]*tw[i]*rawErrorSum) if i==j else F(0) for j in range(6)] for i in range(6)]
    assert psd(add(rawE,outer(eps),-1))
    df=sum(mu[k]*F(lam,z)**k for k in range(1,15));d2=F(6,z-6);dp=sum(nu[k]*F(lamPsi,z)**k for k in range(1,25))+r/(2*dl);cw0=F(3,2)-r/(2*dl);dw=abs(cw0)*df+Aw*r/(2*dl)
    responseGramInverse=inv(Glo)
    results=[]
    for name in sorted(trials,reverse=replay):
        Y=trials[name];colError=[up(sum(abs(Y[i][j])*eps[i] for i in range(6))) for j in range(5)]
        # Universal absolute-coefficient triangle bound, valid for complex mixtures.
        ec=sum(colError[i]/sw[i] for i in range(5));E=[[up(colError[i]*sw[i]*ec) if i==j else F(0) for j in range(5)] for i in range(5)];assert psd(add(E,outer(colError),-1))
        fg=[[Z for _ in range(5)] for _ in range(5)];ur=[[Z for _ in range(5)] for _ in range(5)];ug=[[Z for _ in range(5)] for _ in range(5)]
        for n in degrees:
            u,v,mass=cache[n];U=[total([smul(rat(Y[k][j]),u[k]) for k in range(6)]) for j in range(5)];V=[total([smul(rat(Y[k][j]),v[k]) for k in range(6)]) for j in range(5)];R=[minus(u[j],V[j]) for j in range(5)]
            for i in range(5):
                for j in range(5):ur[i][j]=plus(ur[i][j],smul(mass,smul(U[i],R[j])))
                for j in range(i,5):
                    fg[i][j]=plus(fg[i][j],smul(mass,smul(R[i],R[j])));ug[i][j]=plus(ug[i][j],smul(mass,smul(U[i],U[j])))
        fl=[[F(0)]*5 for _ in range(5)];fh=[[F(0)]*5 for _ in range(5)]
        for i in range(5):
            for j in range(i,5):lo,hi=bounds(fg[i][j]);fl[i][j]=fl[j][i]=lo;fh[i][j]=fh[j][i]=hi
        Nlo,prefixHi,_=loewner(fl,fh,sw);assert psd(Nlo)
        lead=[F(j==3)+F(j==4)*mu[0]-Y[0][j]-Y[1][j]-mu[0]*Y[2][j]-(F(3,2)+nu[0]-r/(2*dl))*Y[3][j]-cw0*mu[0]*Y[4][j] for j in range(5)]
        rem=add(add(scale(d2*d2,outer(Y[1])),scale(df*df,outer([F(j==4)-Y[2][j] for j in range(5)]))),add(scale(dp*dp,outer(Y[3])),scale(dw*dw,outer(Y[4]))))
        tailHi=add(scale(F(3,2)*T,outer(lead)),scale(12*T,rem));Nhi=add(prefixHi,tailHi)
        ua=[abs(Y[3][j])+Aw*abs(Y[4][j]) for j in range(5)]
        ra=[abs(lead[j])+d2*abs(Y[1][j])+df*abs(F(j==4)-Y[2][j])+dp*abs(Y[3][j])+dw*abs(Y[4][j]) for j in range(5)]
        un=[]
        for i in range(5):un.append(sqrtup(up(bounds(ug[i][i])[1]+T*ua[i]*ua[i])))
        # C=Sym(S*D U)+Sym(U*D R_actual), exact variational response.
        # Source/U tails use full source Gram entry intervals. U/residual tails
        # retain their shared leading cancellation before taking absolute values.
        cl=[[F(0)]*5 for _ in range(5)];ch=[[F(0)]*5 for _ in range(5)]
        for i in range(5):
            for j in range(i,5):
                value=Z
                for k in range(6):
                    value=plus(value,smul(rat(Y[k][j]/2),(rat(gl[i][k])[0],rat(gh[i][k])[1])))
                    value=plus(value,smul(rat(Y[k][i]/2),(rat(gl[j][k])[0],rat(gh[j][k])[1])))
                value=plus(value,smul(rat(F(1,2)),plus(ur[i][j],ur[j][i])))
                radius=up(T*(ua[i]*ra[j]+ua[j]*ra[i])/2+(un[i]*colError[j]+un[j]*colError[i])/2)
                lo,hi=bounds(value);cl[i][j]=cl[j][i]=down(lo-radius);ch[i][j]=ch[j][i]=up(hi+radius)
        directClo,directChi,_=loewner(cl,ch,sw)
        J=[[F(i==j)-Y[i][j] for j in range(5)] for i in range(6)]
        algebraicClo=add(add(Glo,cong(J,tgHi),-1),cong(Y,add(tgLo,KThi,-1)))
        algebraicChi=add(add(Ghi,cong(J,tgLo),-1),cong(Y,add(tgHi,KTlo,-1)))
        cOptions=[('direct',directClo,directChi),('algebraic',algebraicClo,algebraicChi)]
        if name=='baseline_least_residual':cOptions.append(('inherited',mat(prior['selected_enclosure'],'variational_response_lower'),mat(prior['selected_enclosure'],'variational_response_upper')))
        directE=E
        errorOptions=[('response_triangle',E),('raw_trial_triangle',cong(Y,rawE))]
        best=None
        taus=[F(1,100),F(1,30),F(1,10),F(1,3),F(1),F(3)];sigmas=[F(0),F(1,30),F(1,10),F(1,3),F(1,2)]
        for cName,Clo,Chi in (cOptions[::-1] if replay else cOptions):
            for eName,E in (errorOptions[::-1] if replay else errorOptions):
                for tau in (taus[::-1] if replay else taus):
                    Rhi=add(scale(1+tau,Nhi),scale(1+1/tau,E));upper=add(Chi,scale(1/a,Rhi))
                    residualScore=sum(responseGramInverse[i][j]*Rhi[j][i] for i in range(5) for j in range(5))
                    for sigma in (sigmas[::-1] if replay else sigmas):
                        Rlo=[[F(0)]*5 for _ in range(5)] if sigma==0 else add(scale(1-sigma,Nlo),scale(-(1/sigma-1),E))
                        if not psd(Rlo):continue
                        lower=add(Clo,scale(F(1,2),Rlo))
                        for ln,lc in [('residual',lower),('structural',scale(F(1,2),Glo)),('inherited',mat(prior['selected_enclosure'],'canonical_inverse_response_lower'))]:
                            for hn,hc in [('residual',upper),('structural',scale(1/a,Ghi)),('inherited',mat(prior['selected_enclosure'],'canonical_inverse_response_upper'))]:
                                if not psd(lc):continue
                                gap=add(hc,lc,-1)
                                if not psd(gap):continue
                                if best is not None and not psd(add(scale(best[0][0],Glo),gap,-1)):continue
                                if ln=='inherited' and hn=='inherited':beta=F(prior['relative_inverse_width_upper'])
                                elif best is not None and not psd(add(scale(best[0][0]-F(1,10**6),Glo),gap,-1)):beta=best[0][0]
                                else:beta=width(gap,Glo)
                                key=(beta,residualScore,tau,sigma,ln,hn,cName,eName)
                                if best is None or key<best[0]:best=(key,lc,hc,Rlo,Rhi,Clo,Chi,E)
        assert best is not None
        (beta,residualScore,tau,sigma,ln,hn,cName,eName),lower,upper,Rlo,Rhi,Clo,Chi,E=best;gate=add(scale(F(1,2),Glo),add(upper,lower,-1),-1)
        assert psd(add(scale(beta,Glo),add(upper,lower,-1),-1))
        item=dict(trial=name,trial_basis_coefficients=ser(Y),direct_response_column_action_errors=list(map(str,colError)),direct_response_action_error_Gram_upper=ser(directE),selected_response_action_error_Gram_upper=ser(E),direct_variational_response_entry_lower=ser(cl),direct_variational_response_entry_upper=ser(ch),variational_response_lower=ser(Clo),variational_response_upper=ser(Chi),nominal_residual_Gram_lower=ser(Nlo),nominal_residual_Gram_upper=ser(Nhi),whole_residual_tail_Gram_upper=ser(tailHi),actual_residual_Gram_lower=ser(Rlo),actual_residual_Gram_upper=ser(Rhi),selected_upper_tau=str(tau),selected_lower_tau=str(sigma),selected_lower_type=ln,selected_upper_type=hn,selected_variational_bound_type=cName,selected_action_error_bound_type=eName,canonical_inverse_response_lower=ser(lower),canonical_inverse_response_upper=ser(upper),relative_inverse_width_upper=str(beta),half_Gram_gate_matrix=ser(gate),half_Gram_gate_passed=psd(gate),nominal_residual_relative_Gram_upper=str(width(Nhi,Glo)),actual_residual_relative_Gram_upper=str(width(Rhi,Glo)),selected_residual_normalized_trace_score=str(residualScore))
        results.append(item);print('RC186 trial',name,'width',float(beta),'gate',psd(gate),flush=True)
    results.sort(key=lambda x:x['trial']);selected=min(results,key=lambda x:(F(x['relative_inverse_width_upper']),F(x['nominal_residual_relative_Gram_upper']),x['trial']));beta=F(selected['relative_inverse_width_upper'])
    return dict(milestone='RC186',status='PASS: certified same-family enriched canonical inverse; gate separately reported',starting_commit='a7abe9482eaa49e5d901facd6f1811387bda9d3e',input_sha256=hs,response_source_order=prior['response_source_order'],raw_trial_basis_order=prior['trial_basis_order']+['q185'],source_D_Gram_lower=ser(Glo),source_D_Gram_upper=ser(Ghi),raw_trial_D_Gram_entry_lower=ser(gl),raw_trial_D_Gram_entry_upper=ser(gh),raw_trial_canonical_Gram_entry_lower=ser(kl),raw_trial_canonical_Gram_entry_upper=ser(kh),trial_coordinate_transformation=ser(A),q185_midpoint_D_projection_coefficients=list(map(str,b)),q185_projection_residual_midpoint_D_energy=str(residualEnergy),transformed_trial_D_Gram_lower=ser(transformedGramLo),trial_independence_verified=True,trial_coordinate_change_is_not_exact_source_orthogonality=True,finite_prefix_last_degree=O,all_input_output_tails_and_mixed_errors_paid=True,evaluated_inverse_trials=results,selected_trial=selected['trial'],selected_enclosure=selected,relative_inverse_width_upper=str(beta),certified_acceptance_ratio_upper=str(2*beta),certified_gate_margin_lower=str(F(1,2)-beta),canonical_half_Gram_inverse_width_gate_passed=selected['half_Gram_gate_passed'],same_five_response_sources_as_RC184=True,previous_same_family_width_upper=prior['relative_inverse_width_upper'],full_complex_five_source_mixtures_paid=True,actual_five_source_canonical_inverse_response_certified=True,native_seven_source_frame_changed=False,full_native_seven_source_inverse_certified=False,Stage_I_completion_ratio=None,Stage_I_closed=False,original_Weil_or_augmented_actions_performed=False,RH=False,F4=False,Lean=False,inverse_width_improved_over_RC184=beta<F(prior['relative_inverse_width_upper']),next_cursor='tighten the inherited actual canonical endpoint-action and variational enclosures on the same five-source family; the paid q185 enrichment has reduced its nominal residual but the inverse gate remains open')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');args=p.parse_args();paths=[Path(__file__).resolve().parents[1]/'certificates/rpb108_rc185_five_source_focus_action.json']+prior_inputs();result=run(paths,args.replay)
    if args.replay:assert json.loads(Path(args.output).read_text())==result
    else:Path(args.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC186 PASS: same-family five-source inverse with paid residual enrichment')
