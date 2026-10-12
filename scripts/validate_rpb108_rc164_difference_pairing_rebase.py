"""RC164: direct RC163 delta pairings and coherent inverse reassembly."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from math import ceil,sqrt
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,div,bounds,up,down,sqrtup,psd,ser,loewner
from validate_rpb108_rc134_correlated_six_input_covariance import smul
from validate_rpb108_rc129_four_vector_joint_moment import add,mm,inv,cong

def reconstruct(name,cut,paths,reverse):
    path=Path(__file__).with_name(name);src=path.read_text();ns={'__file__':str(path)}
    exec(compile(src[:src.index(cut)]+'\n    return locals()\n','RC164-'+name,'exec'),ns)
    return ns['run'](paths,reverse)

def run(paths,reverse=False):
    raw=[Path(p).read_bytes() for p in paths]
    action,prior,endpoint,transport,assembly,gram,cross=map(json.loads,raw)
    assert [x['milestone'] for x in (action,prior,endpoint,transport,assembly,gram,cross)]==['RC163','RC162','RC161','RC160','RC158','RC159','RC157']
    hs=[hashlib.sha256(b).hexdigest() for b in raw];directory=Path(paths[0]).parent
    assert action['input_sha256'][2:]==[hs[i] for i in (4,5,1)]
    assert action['input_sha256'][1]==assembly['input_sha256'][2]
    assert prior['input_sha256']==[hs[i] for i in (2,3,4,5)]
    assert transport['input_sha256']==[hs[i] for i in (4,5)]
    # Exact predecessor filenames are located by milestone and hash, never
    # accepted merely because the filename resembles the expected record.
    candidates=list(directory.glob('*.json'));earlier=[]
    for digest in cross['input_sha256']:
        matches=[p for p in candidates if hashlib.sha256(p.read_bytes()).hexdigest()==digest]
        assert len(matches)==1;earlier.append(str(matches[0]))
    print('RC164 reconstructing paid finite carrier and trials',flush=True)
    r=reconstruct('validate_rpb108_rc157_five_by_two_cross_pairings.py','\n    newQlo=',earlier,reverse)
    p,d=r['p'],r['d'];O=r['O'];lam=d['L']*(d['L']+1);first=(O+2)*(O+3)
    assert action['input_sha256'][0]==hashlib.sha256(Path(r['r']['delta_paths'][-1]).with_name('rpb108_rc153_correlated_difference_action.json').read_bytes()).hexdigest()
    # RC163 trial: exact old finite centers, centered omitted source, and
    # the stored analytic polynomial. Recheck its finite hash and moments.
    digest=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    finite=[dict(degree=v['degree'],center=str(F(v['center'])+(d['delta'][v['degree']]/2 if v['degree']>d['L'] else 0))) for v in d['output']]
    assert digest(finite)==action['finite_trial_center_sha256']
    jobs=sorted((n for n in d['delta'] if n<=d['L']),reverse=reverse)
    for k,moment in enumerate(action['analytic_output_moments']):
        exact=sum(-d['delta'][n]*F(n*(n+1),lam)**k for n in jobs)
        assert down(exact)==F(moment['center']) and up(exact-down(exact))==F(moment['radius'])
    tail=list(map(F,action['analytic_trial_tail_polynomial']))
    sourceTail=list(map(F,d['cov']['z_minus_v_combined_tail_polynomial']))
    retainedMoments=action['analytic_output_moments'][:25]
    assert tail==[(sourceTail[k]/2 if k<len(sourceTail) else F(0))-(F(retainedMoments[k]['center']) if k<len(retainedMoments) else F(0)) for k in range(max(len(sourceTail),len(retainedMoments)))]
    qd={v['degree']:rat(F(v['center'])) for v in finite}
    for n in range(d['O']+2,O+1,2):
        eta=div(rat(F(2*n+1,n*(n+1))),r['dn'][n])
        qd[n]=smul(eta,rat(sum(v*F(lam,n*(n+1))**k for k,v in enumerate(tail))))
    qpoly=[v*F(lam,first)**k for k,v in enumerate(tail)]
    sources=r['sources']+r['r']['sources'];sourcepolys=r['sp']+r['r']['ss']
    trials=r['oldtrials']+r['r']['trials'];trialpolys=r['tq']+r['r']['tp']
    trials[-1]=qd;trialpolys[-1]=qpoly
    Qrow=[r['pair'](qd,s,qpoly,poly) for s,poly in zip(sources,sourcepolys)]
    Rrow=[r['pair'](qd,q,qpoly,poly) for q,poly in zip(trials,trialpolys)]
    assert 0<Rrow[-1][0]<=Rrow[-1][1]
    QL=[list(row) for row in r['r']['QL']];QU=[list(row) for row in r['r']['QU']]
    # r['r'].QL is just the complementary block; combine the unchanged
    # psi row with the already certified old-source cross entries.
    mat=lambda doc,key:[[F(x) for x in row] for row in doc[key]]
    ql=mat(cross,'new_trial_old_source_pairing_lower');qu=mat(cross,'new_trial_old_source_pairing_upper')
    ql=[ql[i]+QL[i] for i in range(2)];qu=[qu[i]+QU[i] for i in range(2)]
    ql[1]=[v[0] for v in Qrow];qu[1]=[v[1] for v in Qrow]
    rl=[list(row) for row in r['r']['RL']];ru=[list(row) for row in r['r']['RU']]
    for j in range(2):rl[1][j]=rl[j][1]=Rrow[j+5][0];ru[1][j]=ru[j][1]=Rrow[j+5][1]
    print('RC164 all seven changed trial-source and trial Gram entries paid',flush=True)
    t=reconstruct('validate_rpb108_rc160_correlated_variational_transport.py','\n    candidates=',paths[4:6],reverse)
    a=t['d'];GLo,GHi=t['GLo'],t['GHi'];X,Y,V=t['X'],t['Y'],t['V'];weights=t['weights'];width=t['width']
    # Floating point selects a grid candidate only. Acceptance and its
    # immediate predecessor are tested by the original exact PSD routine.
    # If the numerical hint is unavailable or unstable, use exact bisection.
    try:
        import numpy as np
        scale=[sqrt(float(GLo[i][i])) for i in range(7)]
        normalized=np.array([[float(GLo[i][j])/scale[i]/scale[j] for j in range(7)] for i in range(7)])
        chol=np.linalg.cholesky(normalized)
    except (ImportError,ValueError,ArithmeticError):
        chol=None
    def width(gap):
        if chol is not None:
            try:
                A=np.array([[float(gap[i][j])/scale[i]/scale[j] for j in range(7)] for i in range(7)])
                left=np.linalg.solve(chol,A)
                normalizedGap=np.linalg.solve(chol,left.T).T
                hint=float(np.linalg.eigvalsh((normalizedGap+normalizedGap.T)/2)[-1])
                n=max(1,ceil(hint*10**6))
                yes=lambda k:psd(add([[F(k,10**6)*x for x in row] for row in GLo],gap,-1))
                for _ in range(8):
                    if yes(n):
                        if not yes(n-1):return F(n,10**6)
                        n-=1
                    else:n+=1
            except (ValueError,ArithmeticError):pass
        return t['width'](gap)
    assert ser(Y)==assembly['trial_source_frame_coefficients']
    # Same source/resolvent y=WY, new q(Y): only the approximation changes.
    nativeAction=mm(a['T'],Y[:5]);actionFrame=mm(a['Wi'],nativeAction);conditionedAction=mm(inv(X),actionFrame)
    Aplus,Aminus=add(conditionedAction,V),add(conditionedAction,V,-1)
    oldLo=[[x/4 for x in row] for row in add(cong(Aplus,GLo),cong(Aminus,GHi),-1)]
    oldHi=[[x/4 for x in row] for row in add(cong(Aplus,GHi),cong(Aminus,GLo),-1)]
    NL=[[F(0)]*7 for _ in range(7)];NU=[[F(0)]*7 for _ in range(7)]
    CL=[[F(0)]*7 for _ in range(7)];CU=[[F(0)]*7 for _ in range(7)]
    for i in range(7):
        for j in range(i,7):
            coeff=[[(Y[k+5][i]*Y[b][j]+Y[k+5][j]*Y[b][i])/2 for b in range(7)] for k in range(2)]
            low,high=a['interval'](coeff,ql,qu);NL[i][j]=NL[j][i]=low;NU[i][j]=NU[j][i]=high
            low,high=a['interval']([[Y[k+5][i]*t['Zframe'][b][j]+Y[k+5][j]*t['Zframe'][b][i] for b in range(7)] for k in range(2)],ql,qu)
            l2,h2=a['interval']([[Y[k+5][i]*Y[b+5][j] for b in range(2)] for k in range(2)],rl,ru)
            CL[i][j]=CL[j][i]=low+l2;CU[i][j]=CU[j][i]=high+h2
    nlo,nhi,_=loewner(NL,NU,weights);approxLo,approxHi=add(oldLo,nlo),add(oldHi,nhi)
    _,chi,_=loewner(CL,CU,weights);NHi=add(cong(t['Zconditioned'],GHi),chi);assert psd(NHi)
    # Build fresh error uppers for the changed physical q_delta column.
    eps=list(map(F,a['actions']['action_column_D_norm_error_upper']));eps[-1]=F(action['full_Cdelta_trial_D_norm_error_upper'])
    K=inv(cong(a['W'],a['GLo']));w=[sqrtup(K[i][i]) for i in range(7)];total=sum(eps[i]*w[i] for i in range(7))
    weighted=cong(Y,[[total*eps[i]/w[i] if i==j else F(0) for j in range(7)] for i in range(7)])
    uniform=mat(action,'new_inverse_trial_error_Gram_upper');GY=cong(V,GHi)
    candidates=[];best=None;endpointBest=None
    alphas=[F(0),F(1,2),F(1)];gammas=[F(1),F(2),F(3),F(4)];taus=[F(1,4),F(1,2),F(1),F(2),F(4)]
    if reverse:alphas.reverse();gammas.reverse();taus.reverse()
    for alpha in alphas:
        E=add([[alpha*x for x in row] for row in weighted],[[(1-alpha)*x for x in row] for row in uniform]);assert psd(E)
        for gamma in gammas:
            deviation=add([[gamma*x/2 for x in row] for row in E],[[x/(2*gamma) for x in row] for row in GY])
            HL,HU=add(approxLo,deviation,-1),add(approxHi,deviation)
            endpointWidth=width(add(HU,HL,-1));LLo,LHi=add(t['GL'],HU,-1),add(t['GU'],HL,-1)
            key=(endpointWidth,alpha,gamma)
            if endpointBest is None or key<endpointBest[0]:endpointBest=(key,LLo,LHi)
            lower=LLo if psd(LLo) else [[x/2 for x in row] for row in GLo]
            options=[('structural upper',F(0),GHi)]
            for tau in taus:
                residual=add([[(1+tau)*x for x in row] for row in NHi],[[(1+1/tau)*x for x in row] for row in E])
                options.append(('paid variational upper',tau,add(LHi,residual)))
            for name,tau,upper in options:
                gap=add(upper,lower,-1)
                assert psd(gap)
                beta=width(gap);key=(beta,alpha,gamma,tau,name)
                candidates.append(dict(weighted_fraction=str(alpha),gamma=str(gamma),tau=str(tau),upper=name,relative_inverse_width_upper=str(beta),relative_endpoint_width_upper=str(endpointWidth),variational_lower_psd=psd(LLo)))
                if best is None or key<best[0]:best=(key,lower,upper,E)
    (newWidth,alpha,gamma,tau,name),lower,upper,error=best
    selected='new RC163 trial enclosure: '+name;beta=newWidth
    if F(prior['relative_inverse_width_upper'])<beta:
        beta=F(prior['relative_inverse_width_upper']);lower=mat(prior,'conditioned_reference_inverse_lower');upper=mat(prior,'conditioned_reference_inverse_upper');selected='retained RC162 enclosure'
    assert psd(lower) and psd(add(upper,lower,-1))
    assert psd(add([[beta*x for x in row] for row in GLo],add(upper,lower,-1),-1))
    gate=psd(add([[F(1,2)*x for x in row] for row in GLo],add(upper,lower,-1),-1))
    candidates.sort(key=lambda c:(F(c['weighted_fraction']),F(c['gamma']),F(c['tau']),c['upper']))
    return dict(milestone='RC164',status='PASS: direct changed delta pairings and coherent reference inverse reassembly',
      starting_commit='36123323ace400c74bfb856ce69c876c28a738b4',aperture='11/10',input_sha256=hs,
      RC157_dependency_sha256=cross['input_sha256'],new_delta_finite_trial_hash_verified=True,new_delta_output_moments_verified=True,
      finite_pairing_prefix_degree=O,signed_analytic_pairing_tails_paid=True,
      new_delta_trial_source_pairing_lower=list(map(str,ql[1])),new_delta_trial_source_pairing_upper=list(map(str,qu[1])),
      new_delta_trial_Gram_row_lower=[str(v[0]) for v in Rrow],new_delta_trial_Gram_row_upper=[str(v[1]) for v in Rrow],
      new_two_trial_source_pairing_lower=ser(ql),new_two_trial_source_pairing_upper=ser(qu),
      new_two_trial_Gram_lower=ser(rl),new_two_trial_Gram_upper=ser(ru),
      new_approximate_endpoint_Loewner_lower=ser(approxLo),new_approximate_endpoint_Loewner_upper=ser(approxHi),
      new_nominal_residual_Gram_upper=ser(NHi),new_nominal_residual_relative_upper=str(width(NHi)),
      previous_nominal_residual_relative_upper=str(width(t['NHi'])),
      best_new_relative_endpoint_width_upper=str(endpointBest[0][0]),
      best_new_endpoint_variational_lower_psd=psd(endpointBest[1]),
      new_inverse_candidates=candidates,best_new_relative_inverse_width_upper=str(newWidth),
      selected_inverse_enclosure=selected,relative_inverse_width_upper=str(beta),
      conditioned_reference_inverse_lower=ser(lower),conditioned_reference_inverse_upper=ser(upper),
      half_Gram_inverse_width_gate_passed=gate,changed_trial_pairing_and_residual_rebase_completed=True,
      old_delta_trial_pairings_reused_for_new_delta_trial=False,
      Stage_I_closed=False,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='inspect the updated endpoint, nominal residual, and action-error budgets on the conditioned limiting direction before selecting the next physical trial refinement')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=7)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC164 PASS: changed delta pairing and inverse rebase',flush=True)
