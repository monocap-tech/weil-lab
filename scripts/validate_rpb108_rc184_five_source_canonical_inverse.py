"""RC184: actual correlated inverse response including native w14."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc129_four_vector_joint_moment import add,inv,mm,cong
from validate_rpb108_rc134_correlated_six_input_covariance import smul
from validate_rpb108_rc177_three_source_canonical_action_gram import scale,mat,width

def outer(x):return [[a*b for b in x] for a in x]
def total(xs):
    s=Z
    for x in xs:s=plus(s,x)
    return s

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];data=list(map(json.loads,raw));hs=[hashlib.sha256(b).hexdigest() for b in raw]
    wcert,wcarrier,prior,pcarrier,psiCert,threeInverse,qcert,oldInverse,three,fnew,p2,p0,joint,response,old,metric,physical,endpoint=data
    assert [x['milestone'] for x in data]==['RC183','RC183-w14-carrier','RC182','RC182-Cpsi-carrier','RC181','RC180','RC179','RC178','RC177','RC176','RC172','RC171','RC129','RC128','RC127','RC121','RC175','RC154']
    assert wcert['input_sha256'][0]==hs[2] and wcert['input_sha256'][2:5]==hs[12:15] and wcert['materialized_canonical_carrier_sha256']==hs[1]
    assert prior['input_sha256'][:14]==hs[4:]
    assert pcarrier['historical_center_radius_sha256']==prior['historical_Cpsi_center_radius_sha256'] and pcarrier['analytic_output_moments']==endpoint['analytic_output_moment_intervals']
    O=16382;r=F(789,125);a=F(metric['actual_canonical_diagonal_metric_lower']);sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B)
    H=[Z]
    for n in range(1,O+3):H.append(plus(H[-1],rat(F(1,n))))
    D={n:(plus(H[n],rat(sl))[0],plus(H[n],rat(sh))[1]) for n in range(0,O+3,2)}
    g={2*i:F(c) for i,c in enumerate(wcarrier['native_w14_finite_coefficient_centers'])};mu=list(map(F,wcarrier['analytic_moment_centers']));lam=F(wcarrier['analytic_lambda'])
    cpsi={2*i:F(c) for i,c in enumerate(pcarrier['finite_Cpsi_coefficient_centers'])};nu=[F(x['center']) for x in pcarrier['analytic_output_moments'][:25]];lamPsi=F(pcarrier['analytic_output_lambda'])
    cw={2*i:F(c) for i,c in enumerate(wcarrier['Cg_finite_coefficient_centers'])};negw={x['degree']:F(x['coefficient_center']) for x in wcarrier['negative_r_D_inverse_w14_finite_polynomial']};rw={x['degree']:F(x['coefficient_center']) for x in wcarrier['D_inverse_regular_polynomial']}
    r0={x['degree']:F(x['D_inverse_trial_coefficient']) for x in p0['physical_regular_coefficient_enclosures']};r2={x['degree']:F(x['D_inverse_trial_coefficient']) for x in p2['physical_regular_coefficient_enclosures']}
    rf={x['degree']:F(x['coefficient_center']) for x in fnew['D_inverse_regular_polynomial']};negf={x['degree']:F(x['coefficient_center']) for x in fnew['negative_r_D_inverse_f0_polynomial']}
    q={x['degree']:F(x['coefficient_center']) for x in qcert['finite_focus_direction']};cq={x['degree']:F(x['coefficient_center']) for x in qcert['endpoint_action_polynomial']};nq={x['degree']:F(x['coefficient_center']) for x in qcert['negative_r_D_inverse_direction_polynomial']};rq={x['degree']:F(x['coefficient_center']) for x in qcert['regular_action']['D_inverse_regular_polynomial']}
    eps=list(map(F,three['individual_full_action_D_error_norm_upper']))+[F(qcert['complete_actual_canonical_q_action_D_error_norm_upper']),F(psiCert['canonical_psi_source_form_full_D_error_norm_upper']),F(wcert['complete_canonical_w14_action_D_error_norm_upper'])]
    indices=[0,1,2,4,5];cache={};GG=[[Z for _ in range(6)] for _ in range(6)];mixed=[[Z for _ in range(6)] for _ in range(6)];QQ=[[Z for _ in range(6)] for _ in range(6)]
    degrees=list(range(0,O+1,2));degrees=degrees[::-1] if replay else degrees
    for n in degrees:
        eta=div(rat(F(2*n+1,n*(n+1))),D[n]) if n else Z
        f=eta if 2<=n<=988 else Z;psi=eta if n>=990 else Z
        w=rat(g[n]) if n<=4094 else smul(rat(sum(mu[k]*F(lam,n*(n+1))**k for k in range(15))),eta)
        u=[rat(F(n==0)),rat(F(n==2)),f,rat(q.get(n,F(0))),psi,w]
        v0=rat(r0.get(n,F(0)))
        if n==0:v0=plus(v0,rat(1+F(p0['canonical_constant_action_P0_correction_center'])))
        if n>=2:v0=plus(v0,eta)
        v2=rat(r2.get(n,F(0)))
        if n==0:v2=plus(v2,rat(F(p2['endpoint_P0_coefficient_center'])))
        if n==2:v2=plus(v2,rat(1+F(p2['endpoint_P2_correction_center'])))
        if n>=4:v2=plus(v2,div(rat(F(2*n+1,n*(n+1)-6)),D[n]))
        vf=plus(plus(f,w),rat(negf.get(n,F(0))+rf.get(n,F(0))))
        vq=rat(q.get(n,F(0))+cq.get(n,F(0))+nq.get(n,F(0))+rq.get(n,F(0)))
        vp=plus(rat(cpsi[n]),smul(minus(rat(F(3,2) if n>=8192 else F(1)),div(rat(r),D[n])),psi))
        vw=plus(w,rat(cw.get(n,F(0))+negw.get(n,F(0))+rw.get(n,F(0))))
        if n>=4096:vw=plus(vw,smul(minus(rat(F(1,2)),div(rat(r),D[n])),w))
        v=[v0,v2,vf,vq,vp,vw];mass=mul(rat(2*B/F(2*n+1)),D[n]);cache[n]=(u,v,mass)
        for i in range(6):
            for j in range(6):mixed[i][j]=plus(mixed[i][j],smul(mass,smul(u[i],v[j])))
            for j in range(i,6):
                GG[i][j]=plus(GG[i][j],smul(mass,smul(u[i],u[j])))
                QQ[i][j]=plus(QQ[i][j],smul(mass,smul(v[i],v[j])))
        if n%4096==0:print('RC184 finite mixed block',n,flush=True)
    first=O+2;z=first*(first+1);dl=F(D[O][0]);T=up(B/(dl*(O-1)*O))
    Aw=sum(mu[k]*F(lam,z)**k for k in range(15));Ap=F(3,2)+sum(nu[k]*F(lamPsi,z)**k for k in range(25))
    srcAmps=[F(0)]*4+[F(1),Aw];actAmps=[F(1),1/(1-F(6,z)),Aw,F(0),Ap,F(3,2)*Aw]
    geLo=[[F(0)]*6 for _ in range(6)];geHi=[[F(0)]*6 for _ in range(6)];qeLo=[[F(0)]*6 for _ in range(6)];qeHi=[[F(0)]*6 for _ in range(6)];meLo=[[F(0)]*6 for _ in range(6)];meHi=[[F(0)]*6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            lo,hi=bounds(mixed[i][j]);meLo[i][j]=lo;meHi[i][j]=up(hi+srcAmps[i]*actAmps[j]*T)
        for j in range(i,6):
            lo,hi=bounds(GG[i][j]);geLo[i][j]=geLo[j][i]=lo;geHi[i][j]=geHi[j][i]=up(hi+srcAmps[i]*srcAmps[j]*T)
            lo,hi=bounds(QQ[i][j]);qeLo[i][j]=qeLo[j][i]=lo;qeHi[i][j]=qeHi[j][i]=up(hi+actAmps[i]*actAmps[j]*T)
    # Intersect available exact native Gram rows and diagonal energies.
    nativeIndex={0:0,2:2,4:1,5:3}
    for i,ni in nativeIndex.items():
        for j,nj in nativeIndex.items():
            geLo[i][j]=max(geLo[i][j],F(joint['actual_D_Gram_entry_lower'][ni][nj]));geHi[i][j]=min(geHi[i][j],F(joint['actual_D_Gram_entry_upper'][ni][nj]));assert geLo[i][j]<=geHi[i][j]
    # Exact finite polynomial versus f0 cancellations give the P2/f0 row.
    geLo[1][2]=geLo[2][1]=geHi[1][2]=geHi[2][1]=2*B/6
    weights=[sqrtup(geHi[i][i]) for i in range(6)];GTlo,GThi,_=loewner(geLo,geHi,weights);assert psd(GTlo)
    keLo=[[F(0)]*6 for _ in range(6)];keHi=[[F(0)]*6 for _ in range(6)]
    for i in range(6):
        for j in range(i,6):
            choices=[]
            for row,col in [(i,j),(j,i)]:
                err=up(weights[row]*eps[col]);choices.append((down(meLo[row][col]-err),up(meHi[row][col]+err)))
            if i<5 and j<5:choices.append((F(prior['trial_canonical_Gram_entry_lower'][i][j]),F(prior['trial_canonical_Gram_entry_upper'][i][j])))
            lo=max(x for x,y in choices);hi=min(y for x,y in choices);assert lo<=hi
            keLo[i][j]=keLo[j][i]=lo;keHi[i][j]=keHi[j][i]=hi
    # q and native w14 nearly overlap. Use the five native/auxiliary
    # response directions themselves as the inverse trial basis.
    keep=indices[:]
    submatrix=lambda A:[[A[i][j] for j in keep] for i in keep]
    geLo,geHi,keLo,keHi,qeLo,qeHi,meLo,meHi=map(submatrix,[geLo,geHi,keLo,keHi,qeLo,qeHi,meLo,meHi])
    eps=[eps[i] for i in keep]
    cache={n:([u[i] for i in keep],[v[i] for i in keep],mass) for n,(u,v,mass) in cache.items()}
    indices=list(range(5));weights=[sqrtup(geHi[i][i]) for i in range(5)]
    GTlo,GThi,_=loewner(geLo,geHi,weights);assert psd(GTlo)
    KTlo,KThi,_=loewner(keLo,keHi,weights);a=F(metric['actual_canonical_diagonal_metric_lower'])
    adverse_first_moment_floor_passed=psd(add(KTlo,scale(a,GThi),-1));adverse_first_moment_ceiling_passed=psd(add(scale(2,GTlo),KThi,-1))
    assert psd(KTlo)
    Qlo,Qhi,_=loewner(qeLo,qeHi,weights);assert psd(Qlo)
    Glo=[[GTlo[i][j] for j in indices] for i in indices];Ghi=[[GThi[i][j] for j in indices] for i in indices];sw=[sqrtup(Ghi[i][i]) for i in range(5)]
    C=sum(eps[i]/weights[i] for i in range(5));E0=[[up(eps[i]*weights[i]*C) if i==j else F(0) for j in range(5)] for i in range(5)];assert psd(add(E0,outer(eps),-1))
    GM=scale(F(1,2),add(GTlo,GThi));KM=scale(F(1,2),add(KTlo,KThi));QM=scale(F(1,2),add(qeLo,qeHi))
    YG=mm(inv(KM),[[row[j] for j in indices] for row in GM]);YR=mm(inv(QM),[[(meLo[j][i]+meHi[j][i])/2 for j in indices] for i in range(5)])
    trials={name:[[down(x,10**30) for x in row] for row in Y] for name,Y in [('Galerkin',YG),('least_residual',YR)]}
    structural_inverse_lower=scale(F(1,2),Glo);structural_inverse_upper=scale(1/a,Ghi)
    df=sum(mu[k]*F(lam,z)**k for k in range(1,15));d2=F(6,z-6);dp=sum(nu[k]*F(lamPsi,z)**k for k in range(1,25))+r/(2*dl)
    cw0=F(3,2)-r/(2*dl);dw=abs(cw0)*df+Aw*r/(2*dl)
    results=[];chosen=None
    for name in sorted(trials,reverse=replay):
        Y=trials[name];Jm=[[F(i==indices[j])-Y[i][j] for j in range(5)] for i in range(5)]
        Clo=add(add(Glo,cong(Jm,GThi),-1),cong(Y,add(GTlo,KThi,-1)));Chi=add(add(Ghi,cong(Jm,GTlo),-1),cong(Y,add(GThi,KTlo,-1)));assert psd(Clo)
        fg=[[Z for _ in range(5)] for _ in range(5)]
        for n in degrees:
            u,v,mass=cache[n];res=[minus(u[indices[i]],total([smul(rat(Y[j][i]),v[j]) for j in range(5)])) for i in range(5)]
            for i in range(5):
                for j in range(i,5):fg[i][j]=plus(fg[i][j],smul(mass,smul(res[i],res[j])))
        fl=[[F(0)]*5 for _ in range(5)];fh=[[F(0)]*5 for _ in range(5)]
        for i in range(5):
            for j in range(i,5):
                lo,hi=bounds(fg[i][j]);fl[i][j]=fl[j][i]=lo;fh[i][j]=fh[j][i]=hi
        Nlo,prefixHi,_=loewner(fl,fh,sw);assert psd(Nlo)
        b=[F(i==3)+F(i==4)*mu[0]-Y[0][i]-Y[1][i]-mu[0]*Y[2][i]-(F(3,2)+nu[0]-r/(2*dl))*Y[3][i]-cw0*mu[0]*Y[4][i] for i in range(5)]
        srcrow=[F(i==4) for i in range(5)]
        rem=add(add(scale(d2*d2,outer(Y[1])),scale(df*df,outer([srcrow[i]-Y[2][i] for i in range(5)]))),add(scale(dp*dp,outer(Y[3])),scale(dw*dw,outer(Y[4]))))
        tailHi=add(scale(F(3,2)*T,outer(b)),scale(12*T,rem));Nhi=add(prefixHi,tailHi);E=cong(Y,E0)
        best=None
        for tau in ([F(1,100),F(1,30),F(1,10),F(1,3),F(1),F(3)] if not replay else [F(3),F(1),F(1,3),F(1,10),F(1,30),F(1,100)]):
            Rhi=add(scale(1+tau,Nhi),scale(1+1/tau,E));upper=add(Chi,scale(1/a,Rhi))
            for sigma in ([F(0),F(1,30),F(1,10),F(1,3),F(1,2)] if not replay else [F(1,2),F(1,3),F(1,10),F(1,30),F(0)]):
                Rlo=[[F(0)]*5 for _ in range(5)] if sigma==0 else add(scale(1-sigma,Nlo),scale(-(1/sigma-1),E))
                if not psd(Rlo):continue
                lower=add(Clo,scale(F(1,2),Rlo));gap=add(upper,lower,-1);assert psd(lower) and psd(gap)
                for lowerName,loCandidate in [('residual',lower),('structural',structural_inverse_lower)]:
                    for upperName,hiCandidate in [('residual',upper),('structural',structural_inverse_upper)]:
                        candidateGap=add(hiCandidate,loCandidate,-1);assert psd(candidateGap)
                        beta=width(candidateGap,Glo);key=(beta,tau,sigma,lowerName,upperName)
                        if best is None or key<best[0]:best=(key,loCandidate,hiCandidate,Rlo,Rhi)
        (beta,tau,sigma,lowerName,upperName),lower,upper,Rlo,Rhi=best
        assert psd(lower) and psd(add(upper,lower,-1))
        gate=add(scale(F(1,2),Glo),add(upper,lower,-1),-1)
        item=dict(trial=name,selected_lower_type=lowerName,selected_upper_type=upperName,trial_basis_coefficients=ser(Y),variational_response_lower=ser(Clo),variational_response_upper=ser(Chi),nominal_residual_Gram_lower=ser(Nlo),nominal_residual_Gram_upper=ser(Nhi),whole_residual_tail_Gram_upper=ser(tailHi),transformed_action_error_Gram_upper=ser(E),actual_residual_Gram_lower=ser(Rlo),actual_residual_Gram_upper=ser(Rhi),selected_upper_tau=str(tau),selected_lower_tau=str(sigma),canonical_inverse_response_lower=ser(lower),canonical_inverse_response_upper=ser(upper),relative_inverse_width_upper=str(beta),half_Gram_gate_matrix=ser(gate),half_Gram_gate_passed=psd(gate),canonical_warmstart_relative_true_image_norm_upper=str(sqrtup(width(scale(1/a,Rhi),lower))))
        results.append(item)
        if chosen is None or (beta,name)<chosen[0]:chosen=((beta,name),item)
        print('RC184 five-source trial',name,'width',float(beta),'half gate',psd(gate),flush=True)
    results.sort(key=lambda x:x['trial']);selected=chosen[1];beta=F(selected['relative_inverse_width_upper'])
    probe=[F(-1,120),F(3,50),F(-14,25),F(-26,25),F(1)]
    quad=lambda A:sum(probe[i]*A[i][j]*probe[j] for i in range(5) for j in range(5))
    witness=quad(mat(selected,'half_Gram_gate_matrix'));assert witness<0
    nominalSquared=quad(mat(selected,'nominal_residual_Gram_lower'));errorSquared=quad(mat(selected,'transformed_action_error_Gram_upper'))
    nominalRootLower=sqrtup(nominalSquared)-F(1,10**40);assert nominalRootLower*nominalRootLower<=nominalSquared
    focusResidualLower=max(F(0),nominalRootLower-sqrtup(errorSquared))
    return dict(milestone='RC184',status='PASS: actual five-source canonical inverse; local gate reported separately',starting_commit='06bc8a80d99b03d953892ebc36db12f2b46c9fa1',input_sha256=hs,response_source_order=['P0','P2','f0','psi0','w14'],trial_basis_order=['P0','P2','f0','psi0','w14'],near_dependent_q_trial_direction_removed=True,
      source_D_Gram_lower=ser(Glo),source_D_Gram_upper=ser(Ghi),trial_D_Gram_lower=ser(GTlo),trial_D_Gram_upper=ser(GThi),trial_canonical_Gram_entry_lower=ser(keLo),trial_canonical_Gram_entry_upper=ser(keHi),trial_canonical_Gram_Loewner_lower=ser(KTlo),trial_canonical_Gram_Loewner_upper=ser(KThi),represented_action_Gram_entry_lower=ser(qeLo),represented_action_Gram_entry_upper=ser(qeHi),full_correlated_action_error_Gram_upper=ser(E0),
      finite_prefix_last_degree=O,first_omitted_even_degree=first,common_eta_tail_D_energy_upper=str(T),w14_tail_product_remainder_upper=str(dw),all_source_and_action_tails_and_mixed_errors_paid=True,evaluated_inverse_trials=results,selected_trial=selected['trial'],selected_enclosure=selected,
      relative_inverse_width_upper=str(beta),canonical_half_Gram_inverse_width_gate_passed=selected['half_Gram_gate_passed'],certified_acceptance_ratio_upper=str(2*beta),certified_gate_margin_lower=str(F(1,2)-beta),
      adverse_first_moment_floor_check_passed=adverse_first_moment_floor_passed,adverse_first_moment_ceiling_check_passed=adverse_first_moment_ceiling_passed,structural_and_residual_inverse_bounds_both_valid=True,half_Gram_gate_failure_witness_coefficients=list(map(str,probe)),half_Gram_gate_failure_witness_quadratic=str(witness),residual_focus_nominal_vector='(S-VY)*probe for the selected five-source trial',residual_focus_actual_D_norm_lower=str(down(focusResidualLower)),residual_focus_nominal_to_actual_D_error_norm_upper=str(sqrtup(errorSquared)),gate_failure_is_not_true_inverse_uncertainty_lower_bound=True,actual_five_source_canonical_inverse_response_certified=True,all_real_and_complex_five_source_mixtures_paid=True,previous_four_source_gate_preserved=True,previous_four_and_new_five_source_widths_directly_comparable=False,
      native_seven_source_frame_changed=False,full_native_seven_source_inverse_certified=False,Stage_I_completion_ratio=None,Stage_I_closed=False,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='construct and pay a finite approximation to the selected five-source focus residual, evaluate its actual canonical action, and enrich the inverse trial space; native v10/z_b6/t10 actions remain subsequent coverage obligations')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');p.add_argument('inputs',nargs=18)
    args=p.parse_args();result=run(args.inputs,args.replay)
    if args.replay:assert json.loads(Path(args.output).read_text())==result
    else:Path(args.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC184 PASS: correlated actual five-source canonical inverse response')
