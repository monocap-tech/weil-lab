"""RC198: complete native v10 mixed rows on the expanded canonical family."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,div,bounds,down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc134_correlated_six_input_covariance import smul
from validate_rpb108_rc129_four_vector_joint_moment import inv
from validate_rpb108_rc177_three_source_canonical_action_gram import mat
from validate_rpb108_rc195_refined_five_source_inverse import inputs as prior_inputs

def inputs():
    base=Path(__file__).resolve().parents[1]/'certificates'
    return [base/('rpb108_rc'+n+'.json') for n in ['197_native_v10_canonical_action','196_adaptive_action_error_inverse','195_refined_five_source_inverse','133_six_vector_joint_matrices']]+prior_inputs()

def reconstruct(paths,replay):
    path=Path(__file__).with_name('validate_rpb108_rc195_refined_five_source_inverse.py');src=path.read_text().split("\nif __name__=='__main__':")[0]
    hook='    src=change(src,"    assert prior[\'source_D_Gram_lower\']==ser(Glo)","    prior=PREVIOUS\\n    assert prior[\'source_D_Gram_lower\']==ser(Glo)")'
    assert src.count(hook)==1
    marker="    cache=d['cache'];degrees=d['degrees'];T=d['T'];a=d['a'];df=d['df'];mu=d['mu'];Glo=d['Glo'];Ghi=d['Ghi'];GTlo=d['tgLo'];GThi=d['tgHi'];sw=d['sw']"
    src=src.replace(hook,hook+'\n    src=change(src,'+repr(marker)+','+repr('    return d\n'+marker)+')')
    target="    result=ns['run'](paths[4:],replay)";assert src.count(target)==1
    src=src.replace(target,"    return ns['run'](paths[4:],replay)")
    ns={'__file__':str(path)};exec(compile(src,'RC198 complete inherited carrier reconstruction','exec'),ns)
    return ns['run'](paths,replay)

def run(paths,replay=False):
    raw=[p.read_bytes() for p in paths];data=list(map(json.loads,raw));hs=[hashlib.sha256(b).hexdigest() for b in raw]
    new,accepted,old,joint6=data[:4]
    assert [x['milestone'] for x in data[:4]]==['RC197','RC196','RC195','RC133']
    assert old['input_sha256']==hs[4:] and accepted['input_sha256'][0]==hs[2] and new['input_sha256'][0]==hs[1] and new['input_sha256'][5]==hs[3]
    sourceIndex=[x['milestone'] for x in data].index('RC183-w14-carrier');source=data[sourceIndex]
    assert new['input_sha256'][2]==hs[sourceIndex] and new['all_native_prefix_coefficients_and_radii_reproduced']
    assert accepted['canonical_half_Gram_inverse_width_gate_passed']
    d=reconstruct(paths[4:],replay);assert list(map(str,d['eps']))==old['individual_raw_trial_action_error_norm_upper']
    native={2*i:F(c) for i,c in enumerate(source['Cg_finite_coefficient_centers'])}
    mu=list(map(F,new['native_analytic_moments']));lam=F(new['native_analytic_lambda']);mom=list(map(F,new['endpoint_analytic_signed_moments']));epLam=F(new['endpoint_analytic_lambda'])
    cp={x['degree']:F(x['coefficient_center']) for x in new['endpoint_action_polynomial']};neg={x['degree']:F(x['coefficient_center']) for x in new['negative_r_finite_polynomial']};reg={x['degree']:F(x['coefficient_center']) for x in new['regular_action']['D_inverse_regular_polynomial']}
    assert len(mu)==11 and len(mom)==25 and new['finite_action_input_degree']==512 and new['endpoint_output_degree']==1536
    DG=[Z]*7;left=[Z]*7;right=[Z]*7;AQ=[Z]*7
    for n in d['degrees']:
        u,v,mass=d['cache'][n];dn=d['D'][n]
        eta=div(rat(F(2*n+1,n*(n+1))),dn) if n else Z
        vn=rat(native[n]) if n<=8190 else smul(eta,rat(sum(mu[k]*F(lam,n*(n+1))**k for k in range(11))))
        av=plus(vn,rat(cp.get(n,F(0))+neg.get(n,F(0))+reg.get(n,F(0))))
        if n>=514:av=plus(av,minus(smul(rat(F(1,2)),vn),smul(div(rat(d['r']),dn),vn)))
        if n>=1538:av=plus(av,smul(eta,rat(sum(mom[k]*F(epLam,n*(n+1))**k for k in range(25)))))
        uu=u+[vn];vv=v+[av]
        for i in range(7):
            DG[i]=plus(DG[i],smul(mass,smul(uu[i],vn)))
            left[i]=plus(left[i],smul(mass,smul(uu[i],av)))
            right[i]=plus(right[i],smul(mass,smul(vn,vv[i])))
            AQ[i]=plus(AQ[i],smul(mass,smul(vv[i],av)))
        if n%8192==0:print('RC198 native mixed rows through',n,flush=True)
    O=d['O'];z=(O+2)*(O+3);T=d['T'];Av=sum(mu[k]*F(lam,z)**k for k in range(11));Cp=sum(mom[k]*F(epLam,z)**k for k in range(25));Mv=F(3,2)*Av+Cp
    assert min(mu)>0 and min(mom)>0 and F(d['D'][O][0])>d['r']
    sa=d['sa']+[Av];va=d['va']+[Mv];assert len(sa)==len(va)==7
    gl=[[F(0)]*7 for _ in range(7)];gh=[[F(0)]*7 for _ in range(7)];prefixL=[[F(0)]*7 for _ in range(7)];prefixH=[[F(0)]*7 for _ in range(7)]
    for i in range(6):
        for j in range(6):
            gl[i][j]=d['gl'][i][j];gh[i][j]=d['gh'][i][j]
            lo,hi=bounds(d['gg'][min(i,j)][max(i,j)]);prefixL[i][j]=lo;prefixH[i][j]=hi
    for i in range(7):
        lo,hi=bounds(DG[i]);prefixL[i][6]=prefixL[6][i]=lo;prefixH[i][6]=prefixH[6][i]=hi
        gl[i][6]=gl[6][i]=lo;gh[i][6]=gh[6][i]=up(hi+sa[i]*Av*T)
    # Native Gram ancestry sharpens exact source rows; these are ENTRY
    # intersections only, not substitutions for a Loewner endpoint.
    index={0:0,2:2,3:1,4:3,6:4}
    for i,ni in index.items():
        for j,nj in index.items():
            gl[i][j]=max(gl[i][j],F(joint6['actual_D_Gram_entry_lower'][ni][nj]));gh[i][j]=min(gh[i][j],F(joint6['actual_D_Gram_entry_upper'][ni][nj]));assert gl[i][j]<=gh[i][j]
    weights=[sqrtup(gh[i][i]) for i in range(7)]
    Glo,_,_=loewner(prefixL,prefixH,weights);_,Ghi,_=loewner(gl,gh,weights)
    assert psd(Glo);inv(Glo)
    eps=list(d['eps'])+[F(new['complete_canonical_v10_action_D_error_norm_upper'])]
    kl=[[F(0)]*7 for _ in range(7)];kh=[[F(0)]*7 for _ in range(7)]
    for i in range(6):
        for j in range(6):kl[i][j]=F(old['raw_trial_canonical_Gram_entry_lower'][i][j]);kh[i][j]=F(old['raw_trial_canonical_Gram_entry_upper'][i][j])
    actionLo=[[F(0)]*7 for _ in range(7)];actionHi=[[F(0)]*7 for _ in range(7)]
    for i in range(6):
        for j in range(6):actionLo[i][j]=d['ql'][i][j];actionHi[i][j]=d['qh'][i][j]
    rows=[]
    for i in range(7):
        ll,lh=bounds(left[i]);rl,rh=bounds(right[i]);ql,qh=bounds(AQ[i])
        le=up(sa[i]*Mv*T+weights[i]*eps[6]);re=up(Av*va[i]*T+weights[6]*eps[i])
        kLo=max(down(ll-le),down(rl-re));kHi=min(up(lh+le),up(rh+re));assert kLo<=kHi
        if i==6:
            kLo=max(kLo,d['a']*gl[6][6]);kHi=min(kHi,2*gh[6][6]);assert kLo<=kHi
        kl[i][6]=kl[6][i]=kLo;kh[i][6]=kh[6][i]=kHi
        # Nominal represented action tail pairings have either sign; diagonal
        # tail energy is nonnegative. Actual action-Gram errors are separate.
        qLo=ql if i==6 else down(ql-va[i]*Mv*T);qHi=up(qh+va[i]*Mv*T)
        actionLo[i][6]=actionLo[6][i]=qLo;actionHi[i][6]=actionHi[6][i]=qHi
        error=up(2*weights[i]*eps[6]+2*weights[6]*eps[i]+eps[i]*eps[6])
        rows.append(dict(other_raw_trial_index=i,source_D_pairing_lower=str(gl[i][6]),source_D_pairing_upper=str(gh[i][6]),canonical_mixed_pairing_lower=str(kLo),canonical_mixed_pairing_upper=str(kHi),nominal_action_pairing_lower=str(qLo),nominal_action_pairing_upper=str(qHi),actual_action_pairing_lower=str(down(qLo-error)),actual_action_pairing_upper=str(up(qHi+error)),action_Gram_error_payment_upper=str(error)))
    order=['P0','P2','f0','psi0','w14','q185','v10'];keep=[0,1,2,3,4,6]
    responseLo=[[Glo[i][j] for j in keep] for i in keep];responseHi=[[Ghi[i][j] for j in keep] for i in keep]
    assert psd(responseLo);inv(responseLo)
    print('RC198 full seven-trial source Gram positive; v10 canonical diagonal',float(kl[6][6]),float(kh[6][6]),flush=True)
    return dict(milestone='RC198',status='PASS: complete v10 mixed canonical and action rows; expanded source Gram certified',starting_commit='fdc2fce47a8d5278fcce0bb4e100efa7a12d9049',input_sha256=hs,aperture='11/10',canonical_operator='M=D^-1 L',norm='D energy',raw_trial_basis_order=order,response_source_order=[order[i] for i in keep],finite_prefix_last_degree=O,common_eta_tail_D_energy_upper=str(T),source_tail_amplitude_upper=list(map(str,sa)),nominal_action_tail_absolute_amplitude_upper=list(map(str,va)),raw_trial_D_Gram_entry_lower=ser(gl),raw_trial_D_Gram_entry_upper=ser(gh),raw_trial_D_Gram_Loewner_lower=ser(Glo),raw_trial_D_Gram_Loewner_upper=ser(Ghi),raw_trial_canonical_Gram_entry_lower=ser(kl),raw_trial_canonical_Gram_entry_upper=ser(kh),expanded_response_source_D_Gram_lower=ser(responseLo),expanded_response_source_D_Gram_upper=ser(responseHi),nominal_raw_action_Gram_entry_lower=ser(actionLo),nominal_raw_action_Gram_entry_upper=ser(actionHi),v10_complete_mixed_rows=rows,individual_raw_trial_action_error_norm_upper=list(map(str,eps)),seven_raw_trial_independence_verified=True,six_response_source_independence_verified=True,all_finite_mixed_rows_and_infinite_tails_paid=True,signed_tail_pairings_paid_on_both_sides=True,self_adjoint_mixed_intersections_verified=True,source_action_definitions_unchanged=True,accepted_five_source_inverse_width_retained=accepted['relative_inverse_width_upper'],expanded_inverse_response_evaluated=False,expanded_inverse_acceptance_open=True,native_z_b6_t10_action_coverage_open=True,Stage_I_closed=False,Stage_I_completion_ratio=None,RH=False,F4=False,Lean=False,next_cursor='use full paid seven-trial mixed data to select and certify the six-source canonical inverse; its acceptance is separate from RC196')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');a=p.parse_args();r=run(inputs(),a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC198 PASS')
