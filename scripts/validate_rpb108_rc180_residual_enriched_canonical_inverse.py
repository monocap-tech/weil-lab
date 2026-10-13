"""RC180: residual-enriched canonical inverse on original P0/P2/f0 sources."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc129_four_vector_joint_moment import inv,mm,cong,add,transpose
from validate_rpb108_rc134_correlated_six_input_covariance import smul
from validate_rpb108_rc177_three_source_canonical_action_gram import scale,mat,width

def outer(x):return [[a*b for b in x] for a in x]
def sum_interval(xs):
    total=Z
    for x in xs:total=plus(total,x)
    return total

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];new,previous,prior,*data=map(json.loads,raw);hs=[hashlib.sha256(b).hexdigest() for b in raw]
    assert [new['milestone'],previous['milestone'],prior['milestone']]==['RC179','RC178','RC177']
    assert new['input_sha256'][:10]==hs[1:] and previous['input_sha256'][0]==hs[2] and previous['input_sha256'][2:]==hs[3:]
    assert prior['input_sha256']==hs[3:]
    fnew,p2,p0,joint,wold,old,metric,physical=data
    src=Path(__file__).with_name('validate_rpb108_rc177_three_source_canonical_action_gram.py').read_text().split("\nif __name__=='__main__':")[0]
    marker='    nominal=[[Z for _ in range(3)] for _ in range(3)];mixed=[[Z for _ in range(3)] for _ in range(3)]'
    assert src.count(marker)==1
    ns={};exec(compile(src.replace(marker,'    return locals()',1),'RC177 immutable carrier reconstruction','exec'),ns)
    d=ns['run'](paths[3:],replay);assert d['digest']==prior['native_w14_finite_coefficient_sha256']
    dn,f,g,r0,r2,rf,neg=[d[k] for k in ['dn','f','g','r0','r2','rf','neg']]
    O=prior['finite_prefix_last_degree'];a=F(metric['actual_canonical_diagonal_metric_lower']);assert a==F(32125,230953)
    q={x['degree']:F(x['coefficient_center']) for x in new['finite_focus_direction']}
    eq={x['degree']:F(x['coefficient_center']) for x in new['endpoint_action_polynomial']}
    nq={x['degree']:F(x['coefficient_center']) for x in new['negative_r_D_inverse_direction_polynomial']}
    rq={x['degree']:F(x['coefficient_center']) for x in new['regular_action']['D_inverse_regular_polynomial']}
    vq={n:q.get(n,F(0))+eq.get(n,F(0))+nq.get(n,F(0))+rq.get(n,F(0)) for n in range(0,O+1,2)}
    eps=list(map(F,prior['individual_full_action_D_error_norm_upper']))+[F(new['complete_actual_canonical_q_action_D_error_norm_upper'])]
    cache={};mixed=[[Z for _ in range(4)] for _ in range(4)];gram=[[Z for _ in range(4)] for _ in range(4)];nominal=[[Z for _ in range(4)] for _ in range(4)]
    degrees=list(range(0,O+1,2));degrees=degrees[::-1] if replay else degrees
    for n in degrees:
        v=[rat(r0.get(n,F(0))),rat(r2.get(n,F(0))),plus(rat(g[n]+rf.get(n,F(0))+neg.get(n,F(0))),f.get(n,Z)),rat(vq[n])]
        if n==0:
            v[0]=plus(v[0],rat(1+F(p0['canonical_constant_action_P0_correction_center'])))
            v[1]=plus(v[1],rat(F(p2['endpoint_P0_coefficient_center'])))
        if n>=2:v[0]=plus(v[0],div(rat(F(2*n+1,n*(n+1))),dn[n]))
        if n==2:v[1]=plus(v[1],rat(1+F(p2['endpoint_P2_correction_center'])))
        if n>=4:v[1]=plus(v[1],div(rat(F(2*n+1,n*(n+1)-6)),dn[n]))
        u=[rat(F(n==0)),rat(F(n==2)),f.get(n,Z),rat(q.get(n,F(0)))]
        mass=mul(rat(2*B/F(2*n+1)),dn[n]);cache[n]=(u,v,mass)
        for i in range(4):
            for j in range(4):mixed[i][j]=plus(mixed[i][j],smul(mass,smul(u[i],v[j])))
            for j in range(i,4):
                gram[i][j]=plus(gram[i][j],smul(mass,smul(u[i],u[j])))
                nominal[i][j]=plus(nominal[i][j],smul(mass,smul(v[i],v[j])))
    def symmetric_entries(A):
        lo=[[F(0)]*4 for _ in range(4)];hi=[[F(0)]*4 for _ in range(4)]
        for i in range(4):
            for j in range(i,4):
                l,h=bounds(A[i][j]);lo[i][j]=lo[j][i]=l;hi[i][j]=hi[j][i]=h
        return lo,hi
    geLo,geHi=symmetric_entries(gram);qeLo,qeHi=symmetric_entries(nominal)
    Glo=mat(prior,'source_D_Gram_lower');Ghi=mat(prior,'source_D_Gram_upper')
    for i in range(3):
        for j in range(3):
            geLo[i][j]=Glo[i][j];geHi[i][j]=Ghi[i][j]
            qeLo[i][j]=F(prior['nominal_full_action_Gram_entry_lower'][i][j]);qeHi[i][j]=F(prior['nominal_full_action_Gram_entry_upper'][i][j])
    assert max(geLo[3][3],F(new['finite_focus_D_energy_lower']))<=min(geHi[3][3],F(new['finite_focus_D_energy_upper']))
    weights=[sqrtup(geHi[i][i]) for i in range(4)]
    GTlo,GThi,_=loewner(geLo,geHi,weights);assert psd(GTlo) and psd(add(GThi,GTlo,-1))
    QnomLo,QnomHi,_=loewner(qeLo,qeHi,weights);assert psd(QnomLo)
    keLo=[[F(0)]*4 for _ in range(4)];keHi=[[F(0)]*4 for _ in range(4)];controls=[]
    for i in range(4):
        for j in range(i,4):
            intervals=[]
            for row,col in [(i,j),(j,i)]:
                lo,hi=bounds(mixed[row][col]);err=up(weights[row]*eps[col]);intervals.append((down(lo-err),up(hi+err)))
            if i<3 and j<3:intervals.append((F(prior['actual_canonical_Gram_entry_lower'][i][j]),F(prior['actual_canonical_Gram_entry_upper'][i][j])))
            if i==j==3:intervals.append((F(new['actual_q_canonical_pairing_lower']),F(new['actual_q_canonical_pairing_upper'])))
            lo=max(x for x,y in intervals);hi=min(y for x,y in intervals);assert lo<=hi
            keLo[i][j]=keLo[j][i]=lo;keHi[i][j]=keHi[j][i]=hi
            controls.append(dict(row=i,column=j,lower=str(lo),upper=str(hi)))
    KTlo,KThi,_=loewner(keLo,keHi,weights)
    assert psd(add(KTlo,scale(a,GThi),-1)) and psd(add(scale(2,GTlo),KThi,-1))
    errorSum=sum(eps[i]/weights[i] for i in range(4));E0=[[up(eps[i]*weights[i]*errorSum) if i==j else F(0) for j in range(4)] for i in range(4)]
    assert psd(add(E0,outer(eps),-1))
    GTmid=scale(F(1,2),add(GTlo,GThi));KTmid=scale(F(1,2),add(KTlo,KThi));Qmid=scale(F(1,2),add(qeLo,qeHi))
    representedCross=[[sum(bounds(mixed[j][i]))/2 for j in range(3)] for i in range(4)]
    YG=mm(inv(KTmid),[row[:3] for row in GTmid]);YR=mm(inv(Qmid),representedCross)
    trials={mode:[[down(x,10**30) for x in row] for row in Y] for mode,Y in [('Galerkin',YG),('least_residual',YR)]}
    T=F(prior['common_eta_tail_D_energy_upper']);mu=d['mu'];lam=d['lam'];first=O+2;z=first*(first+1)
    delta2=F(6,z-6);deltaf=sum(mu[k]*(lam/z)**k for k in range(1,15));sourceWeights=[sqrtup(Ghi[i][i]) for i in range(3)]
    results=[];chosen=None
    for mode in (sorted(trials,reverse=replay)):
        Y=trials[mode];Jminus=[[F(i==j)-Y[i][j] for j in range(3)] for i in range(4)]
        Clo=add(add(Glo,cong(Jminus,GThi),-1),cong(Y,add(GTlo,KThi,-1)))
        Chi=add(add(Ghi,cong(Jminus,GTlo),-1),cong(Y,add(GThi,KTlo,-1)))
        assert psd(Clo) and psd(add(Chi,Clo,-1))
        residualGram=[[Z for _ in range(3)] for _ in range(3)]
        for n in degrees:
            u,v,mass=cache[n]
            residual=[minus(u[i],sum_interval([smul(rat(Y[j][i]),v[j]) for j in range(4)])) for i in range(3)]
            for i in range(3):
                for j in range(i,3):residualGram[i][j]=plus(residualGram[i][j],smul(mass,smul(residual[i],residual[j])))
        fl=[[F(0)]*3 for _ in range(3)];fh=[[F(0)]*3 for _ in range(3)]
        for i in range(3):
            for j in range(i,3):
                lo,hi=bounds(residualGram[i][j]);fl[i][j]=fl[j][i]=lo;fh[i][j]=fh[j][i]=hi
        Nlo,prefixHi,_=loewner(fl,fh,sourceWeights)
        b=[Y[0][i]+Y[1][i]+mu[0]*Y[2][i] for i in range(3)];tailTau=F(1,1000)
        rem=add(scale(delta2**2,outer(Y[1])),scale(deltaf**2,outer(Y[2])))
        tailHi=add(scale((1+tailTau)*T,outer(b)),scale(2*(1+1/tailTau)*T,rem))
        Nhi=add(prefixHi,tailHi);assert psd(Nlo) and psd(add(Nhi,Nlo,-1))
        E=cong(Y,E0);assert psd(E)
        taus=[F(1,1000),F(1,300),F(1,100),F(1,30),F(1,10),F(1,3),F(1)]
        sigmas=[F(0),F(1,100),F(1,30),F(1,10),F(1,3),F(1,2)]
        if replay:taus.reverse();sigmas.reverse()
        best=None;search=[]
        for tau in taus:
            Rhi=add(scale(1+tau,Nhi),scale(1+1/tau,E));upper=add(Chi,scale(1/a,Rhi))
            for sigma in sigmas:
                Rlo=[[F(0)]*3 for _ in range(3)] if sigma==0 else add(scale(1-sigma,Nlo),scale(-(1/sigma-1),E))
                if not psd(Rlo):continue
                lower=add(Clo,scale(F(1,2),Rlo));gap=add(upper,lower,-1);assert psd(lower) and psd(gap)
                beta=width(gap,Glo);key=(beta,tau,sigma);search.append(dict(upper_tau=str(tau),lower_tau=str(sigma),relative_width_upper=str(beta)))
                if best is None or key<best[0]:best=(key,lower,upper,Rlo,Rhi)
        (beta,tau,sigma),lower,upper,Rlo,Rhi=best
        assert psd(add(lower,scale(F(1,2),Glo),-1)) and psd(add(scale(1/a,Ghi),upper,-1))
        gate=add(scale(F(1,2),Glo),add(upper,lower,-1),-1);warmSquared=width(scale(1/a,Rhi),lower)
        item=dict(trial=mode,trial_basis_coefficients=ser(Y),variational_response_lower=ser(Clo),variational_response_upper=ser(Chi),
          nominal_residual_Gram_lower=ser(Nlo),nominal_residual_Gram_upper=ser(Nhi),full_nominal_residual_tail_Gram_upper=ser(tailHi),transformed_correlated_action_error_Gram_upper=ser(E),
          selected_actual_residual_Gram_lower=ser(Rlo),selected_actual_residual_Gram_upper=ser(Rhi),selected_upper_tau=str(tau),selected_lower_tau=str(sigma),
          canonical_inverse_response_lower=ser(lower),canonical_inverse_response_upper=ser(upper),relative_inverse_width_upper=str(beta),
          half_Gram_gate_matrix=ser(gate),half_Gram_gate_passed=psd(gate),canonical_warmstart_relative_true_image_norm_upper=str(sqrtup(warmSquared)),
          canonical_Riesz_trial_D_error_Gram_upper=ser(scale(1/(a*a),Rhi)),canonical_Riesz_trial_canonical_error_Gram_upper=ser(scale(1/a,Rhi)),
          relative_nominal_residual_Gram_upper=str(width(Nhi,Glo)),candidate_enclosures=sorted(search,key=lambda x:(F(x['upper_tau']),F(x['lower_tau']))))
        results.append(item)
        if chosen is None or (beta,mode)<chosen[0]:chosen=((beta,mode),item)
        print('RC180 enriched trial',mode,'relative width',float(beta),'half gate',psd(gate),flush=True)
    results.sort(key=lambda x:x['trial']);selected=chosen[1]
    oldWidth=F(previous['relative_inverse_width_upper']);newWidth=F(selected['relative_inverse_width_upper']);assert newWidth<oldWidth
    assert selected['half_Gram_gate_passed']
    return dict(milestone='RC180',status='PASS: residual-enriched actual three-source canonical inverse half-Gram gate',starting_commit='341d73b6367e52dadaa485fae68734be4b58c134',input_sha256=hs,aperture='11/10',
      response_source_order=['P0','P2','f0'],inverse_trial_basis_order=['P0','P2','f0','RC179 exact finite q'],native_seven_source_frame_changed=False,
      original_response_source_D_Gram_lower=ser(Glo),original_response_source_D_Gram_upper=ser(Ghi),
      enriched_trial_D_Gram_entry_lower=ser(geLo),enriched_trial_D_Gram_entry_upper=ser(geHi),enriched_trial_D_Gram_Loewner_lower=ser(GTlo),enriched_trial_D_Gram_Loewner_upper=ser(GThi),
      enriched_trial_canonical_Gram_entry_lower=ser(keLo),enriched_trial_canonical_Gram_entry_upper=ser(keHi),enriched_trial_canonical_Gram_Loewner_lower=ser(KTlo),enriched_trial_canonical_Gram_Loewner_upper=ser(KThi),
      enriched_represented_action_Gram_entry_lower=ser(qeLo),enriched_represented_action_Gram_entry_upper=ser(qeHi),enriched_full_correlated_action_error_Gram_upper=ser(E0),
      selfadjoint_mixed_action_controls=controls,enriched_trial_vectors_D_independent_certified=True,
      evaluated_inverse_trials=results,selected_trial=selected['trial'],selected_enclosure=selected,
      previous_three_source_relative_width_upper=str(oldWidth),relative_inverse_width_upper=str(newWidth),canonical_half_Gram_inverse_width_gate_passed=True,
      canonical_Riesz_warmstart_relative_true_image_norm_upper=selected['canonical_warmstart_relative_true_image_norm_upper'],
      original_three_source_actual_inverse_response_certified=True,all_real_and_complex_original_three_source_mixtures_paid=True,
      finite_q_input_approximation_error_not_charged_to_exact_q_action=True,full_infinite_residual_tails_and_mixed_errors_paid=True,
      new_operator_action_performed=False,canonical_Riesz_iteration_performed=False,original_augmentation_adjoint_range_identified=False,
      full_seven_source_canonical_inverse_certified=False,required_Stage_I_matrix_tolerance_specified=False,Stage_I_closed=False,
      original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='extend actual canonical action and inverse response coverage beyond P0/P2/f0 toward the native seven-source family, preserving Stage I original Weil target obligations')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');p.add_argument('inputs',nargs=11)
    args=p.parse_args();result=run(args.inputs,args.replay)
    if args.replay:assert json.loads(Path(args.output).read_text())==result
    else:Path(args.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC180 PASS: residual-enriched original three-source canonical inverse half-Gram gate')
