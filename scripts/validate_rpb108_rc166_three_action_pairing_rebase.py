"""RC166: direct q_t mixed pairings and three-action reference reassembly."""
from pathlib import Path
from fractions import Fraction as F
from math import sqrt,ceil
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,mul,div,bounds,up,down,sqrtup,psd,ser,loewner
from validate_rpb108_rc134_correlated_six_input_covariance import smul
from validate_rpb108_rc129_four_vector_joint_moment import add,mm,inv,cong

def reconstruct(name,cut,paths,reverse):
    path=Path(__file__).with_name(name);src=path.read_text();ns={'__file__':str(path)}
    exec(compile(src[:src.index(cut)]+'\n    return locals()\n','RC166-'+name,'exec'),ns)
    return ns['run'](paths,reverse)

def run(paths,reverse=False):
    raw=[Path(p).read_bytes() for p in paths]
    action,prior,assembly,gram,transport=map(json.loads,raw)
    assert [d['milestone'] for d in (action,prior,assembly,gram,transport)]==['RC165','RC164','RC158','RC159','RC160']
    hs=[hashlib.sha256(b).hexdigest() for b in raw]
    assert action['input_sha256'][4:]==hs[2:4]+[hs[1]]
    assert action['input_sha256'][3]==assembly['input_sha256'][2]
    assert prior['input_sha256'][4:6]==hs[2:4] and prior['input_sha256'][3]==hs[4]
    assert transport['input_sha256']==hs[2:4]
    directory=Path(paths[0]).parent;index={}
    for path in directory.glob('*.json'):
        key=hashlib.sha256(path.read_bytes()).hexdigest();assert key not in index;index[key]=str(path)
    earlier=[index[h] for h in prior['input_sha256']]
    print('RC166 reconstructing paid RC164 source and action interface',flush=True)
    b=reconstruct('validate_rpb108_rc164_difference_pairing_rebase.py','\n    t=reconstruct(',earlier,reverse)
    mat=lambda d,k:[[F(x) for x in row] for row in d[k]]
    assert ser(b['ql'])==prior['new_two_trial_source_pairing_lower']
    assert ser(b['ru'])==prior['new_two_trial_Gram_upper']
    r=b['r'];O=r['O'];L=4094;out=8190;lam=L*(L+1);first=(O+2)*(O+3)
    nativeT=r['native'][6]
    assert nativeT==b['sources'][4]
    source={n:F(v[0]) for n,v in nativeT.items() if n<=L}
    assert all(v[0]==v[1] for v in nativeT.values()) and min(source.values())>0
    jobs=sorted(source,reverse=reverse);payload=[];rounding=F(0)
    for n in range(0,out+1,2):
        value=Z
        for m in jobs:
            entry=r['diag'][n] if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
            value=plus(value,mul(entry,rat(source[m])))
        lo,hi=bounds(div(value,r['dn'][n]));center=down((lo+hi)/2);radius=max(center-lo,hi-center)
        payload.append(dict(degree=n,center=str(center),radius=str(radius)))
        rounding+=up(2*B/F(2*n+1)*F(r['dn'][n][1])*radius*radius,10**100)
    digest=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert digest(payload)==action['finite_Ct_action_center_radius_sha256']
    finite=[dict(degree=v['degree'],center=str(F(v['center'])+(F(nativeT[v['degree']][0])/2 if v['degree']>L else 0))) for v in payload]
    assert digest(finite)==action['finite_corrected_trial_center_sha256']
    moments=action['analytic_output_moments']
    for k,moment in enumerate(moments):
        exact=sum(source[m]*F(m*(m+1),lam)**k for m in jobs)
        assert down(exact)==F(moment['center']) and up(exact-down(exact))==F(moment['radius'])
    assert rounding==F(action['finite_action_rounding_D_energy_upper'])
    rho=F(lam,8192*8193);T=F(action['leading_output_eta_tail_D_energy_upper'])
    momentRounding=up(T*sum(F(moments[k]['radius'])*rho**k for k in range(25))**2,10**100)
    remainderAmplitude=up((F(moments[25]['center'])+F(moments[25]['radius']))*rho**25/(1-rho))
    remainder=up(T*remainderAmplitude**2,10**100)
    error=up(sqrtup(rounding)+sqrtup(momentRounding)+sqrtup(remainder)+sqrtup(F(action['omitted_full_t_source_D_energy_upper']))/2)
    assert error==F(action['full_Ct_trial_D_norm_error_upper'])
    mu=list(map(lambda v:F(v['center']),moments[:25]))
    qt={v['degree']:rat(F(v['center'])) for v in finite}
    for n in range(out+2,O+1,2):
        eta=div(rat(F(2*n+1,n*(n+1))),r['dn'][n])
        qt[n]=plus(smul(eta,rat(sum(v*F(lam,n*(n+1))**k for k,v in enumerate(mu)))),smul(rat(F(1,2)),nativeT[n]))
    assert list(map(F,action['canonical_t_analytic_moment_centers']))==r['nut']
    assert F(action['canonical_t_tail_Lambda'])==8190*8191
    actionpoly=[v*F(lam,first)**k for k,v in enumerate(mu)]
    nativepoly=r['polys'][6]
    qtpoly=[(actionpoly[k] if k<len(actionpoly) else F(0))+(nativepoly[k]/2 if k<len(nativepoly) else F(0)) for k in range(max(len(actionpoly),len(nativepoly)))]
    # Pay the source row and all old/new Gram crosses, including the new
    # diagonal. The old fitted Ct is recorded for audit, never substituted.
    Qrow=[r['pair'](qt,s,qtpoly,poly) for s,poly in zip(b['sources'],b['sourcepolys'])]
    Rrow=[r['pair'](qt,q,qtpoly,poly) for q,poly in zip(b['trials']+[qt],b['trialpolys']+[qtpoly])]
    assert 0<Rrow[-1][0]<=Rrow[-1][1]
    ql=[[v[0] for v in Qrow]]+b['ql'];qu=[[v[1] for v in Qrow]]+b['qu']
    rl=[[F(0)]*3 for _ in range(3)];ru=[[F(0)]*3 for _ in range(3)]
    rl[0][0],ru[0][0]=Rrow[-1]
    for j in range(2):
        rl[0][j+1]=rl[j+1][0]=Rrow[j+5][0];ru[0][j+1]=ru[j+1][0]=Rrow[j+5][1]
        for k in range(2):rl[j+1][k+1]=b['rl'][j][k];ru[j+1][k+1]=b['ru'][j][k]
    print('RC166 all seven source and eight old/new trial pairings paid',flush=True)
    t=reconstruct('validate_rpb108_rc160_correlated_variational_transport.py','\n    candidates=',paths[2:4],reverse)
    a=t['d'];GLo,GHi=t['GLo'],t['GHi'];X,Y,V=t['X'],t['Y'],t['V'];weights=t['weights']
    assert ser(Y)==assembly['trial_source_frame_coefficients']
    # Remove the old fitted Ct native column completely. Its replacement
    # is the first of the three non-native actions, with coefficients Y4.
    nativeAction=mm([row[:4] for row in a['T']],Y[:4])
    actionFrame=mm(a['Wi'],nativeAction);actionConditioned=mm(inv(X),actionFrame)
    Znative=add(mm(a['W'],add(Y,X,-1)),nativeAction)
    Zframe=mm(a['Wi'],Znative);Zconditioned=mm(inv(X),Zframe)
    plusA,minusA=add(actionConditioned,V),add(actionConditioned,V,-1)
    oldLo=[[x/4 for x in row] for row in add(cong(plusA,GLo),cong(minusA,GHi),-1)]
    oldHi=[[x/4 for x in row] for row in add(cong(plusA,GHi),cong(minusA,GLo),-1)]
    NL=[[F(0)]*7 for _ in range(7)];NU=[[F(0)]*7 for _ in range(7)]
    CL=[[F(0)]*7 for _ in range(7)];CU=[[F(0)]*7 for _ in range(7)]
    for i in range(7):
        for j in range(i,7):
            coeff=[[(Y[k+4][i]*Y[v][j]+Y[k+4][j]*Y[v][i])/2 for v in range(7)] for k in range(3)]
            low,high=a['interval'](coeff,ql,qu);NL[i][j]=NL[j][i]=low;NU[i][j]=NU[j][i]=high
            low,high=a['interval']([[Y[k+4][i]*Zframe[v][j]+Y[k+4][j]*Zframe[v][i] for v in range(7)] for k in range(3)],ql,qu)
            l2,h2=a['interval']([[Y[k+4][i]*Y[v+4][j] for v in range(3)] for k in range(3)],rl,ru)
            CL[i][j]=CL[j][i]=low+l2;CU[i][j]=CU[j][i]=high+h2
    nlo,nhi,_=loewner(NL,NU,weights);approxLo,approxHi=add(oldLo,nlo),add(oldHi,nhi)
    _,chi,_=loewner(CL,CU,weights);NHi=add(cong(Zconditioned,GHi),chi);assert psd(NHi)
    eps=list(map(F,action['updated_action_column_D_norm_error_upper']))
    K=inv(cong(a['W'],a['GLo']));w=[sqrtup(K[i][i]) for i in range(7)];total=sum(eps[i]*w[i] for i in range(7))
    weighted=cong(Y,[[total*eps[i]/w[i] if i==j else F(0) for j in range(7)] for i in range(7)])
    uniform=mat(action,'new_inverse_trial_error_Gram_upper');GY=cong(V,GHi)
    # Numerical hints do not certify anything: exact PSD acceptance and
    # rejection at adjacent grid points prove every reported width.
    try:
        import numpy as np
        scale=[sqrt(float(GLo[i][i])) for i in range(7)]
        chol=np.linalg.cholesky([[float(GLo[i][j])/scale[i]/scale[j] for j in range(7)] for i in range(7)])
    except (ImportError,ValueError,ArithmeticError):chol=None
    def width(gap):
        if chol is not None:
            try:
                A=np.array([[float(gap[i][j])/scale[i]/scale[j] for j in range(7)] for i in range(7)])
                left=np.linalg.solve(chol,A);H=np.linalg.solve(chol,left.T).T
                n=max(1,ceil(float(np.linalg.eigvalsh((H+H.T)/2)[-1])*10**6))
                yes=lambda k:psd(add([[F(k,10**6)*x for x in row] for row in GLo],gap,-1))
                for _ in range(8):
                    if yes(n):
                        if not yes(n-1):return F(n,10**6)
                        n-=1
                    else:n+=1
            except (ValueError,ArithmeticError):pass
        return t['width'](gap)
    candidates=[];best=None;endpointBest=None
    alphas=[F(0),F(1,2),F(1)];gammas=[F(1),F(2),F(3),F(4)];taus=[F(1,4),F(1,2),F(1),F(2),F(4)]
    if reverse:alphas.reverse();gammas.reverse();taus.reverse()
    structuralLo=[[x/2 for x in row] for row in GLo]
    for alpha in alphas:
        E=add([[alpha*x for x in row] for row in weighted],[[(1-alpha)*x for x in row] for row in uniform]);assert psd(E)
        for gamma in gammas:
            deviation=add([[gamma*x/2 for x in row] for row in E],[[x/(2*gamma) for x in row] for row in GY])
            HL,HU=add(approxLo,deviation,-1),add(approxHi,deviation)
            endpointWidth=width(add(HU,HL,-1));LLo,LHi=add(t['GL'],HU,-1),add(t['GU'],HL,-1)
            if endpointBest is None or (endpointWidth,alpha,gamma)<endpointBest[0]:endpointBest=((endpointWidth,alpha,gamma),LLo,LHi)
            lowers=[('structural half Gram',structuralLo)]
            if psd(LLo):lowers.append(('positive variational lower',LLo))
            uppers=[('structural upper',F(0),GHi)]
            for tau in taus:
                residual=add([[(1+tau)*x for x in row] for row in NHi],[[(1+1/tau)*x for x in row] for row in E])
                uppers.append(('paid variational upper',tau,add(LHi,residual)))
            for lowerName,lower in lowers:
                for upperName,tau,upper in uppers:
                    gap=add(upper,lower,-1);assert psd(gap)
                    beta=width(gap);key=(beta,alpha,gamma,tau,lowerName,upperName)
                    candidates.append(dict(weighted_fraction=str(alpha),gamma=str(gamma),tau=str(tau),lower=lowerName,upper=upperName,relative_inverse_width_upper=str(beta),relative_endpoint_width_upper=str(endpointWidth)))
                    if best is None or key<best[0]:best=(key,lower,upper,E)
    (newWidth,alpha,gamma,tau,lowerName,upperName),lower,upper,error=best
    selected='RC166 three-action enclosure';beta=newWidth
    if F(prior['relative_inverse_width_upper'])<beta:
        beta=F(prior['relative_inverse_width_upper']);lower=mat(prior,'conditioned_reference_inverse_lower');upper=mat(prior,'conditioned_reference_inverse_upper');selected='retained RC164 enclosure'
    assert psd(lower) and psd(add(upper,lower,-1))
    assert psd(add([[beta*x for x in row] for row in GLo],add(upper,lower,-1),-1))
    gate=psd(add([[F(1,2)*x for x in row] for row in GLo],add(upper,lower,-1),-1))
    witness=list(map(F,assembly['enclosure_width_failure_witness']))
    quad=lambda M:sum(witness[i]*M[i][j]*witness[j] for i in range(7) for j in range(7))
    qg=quad(GLo)
    budgets=dict(approximate_endpoint_interval_width_over_source_lower=str(quad(add(approxHi,approxLo,-1))/qg),
      nominal_residual_upper_over_source_lower=str(quad(NHi)/qg),
      selected_action_error_upper_over_source_lower=str(quad(error)/qg),
      selected_inverse_width_over_source_lower=str(quad(add(upper,lower,-1))/qg))
    candidates.sort(key=lambda c:(F(c['weighted_fraction']),F(c['gamma']),F(c['tau']),c['lower'],c['upper']))
    return dict(milestone='RC166',status='PASS: paid new t mixed pairings and coherent three-action inverse reassembly',
      starting_commit='22d8ab30361a167cbb586712c35bb045bcae3935',input_sha256=hs,RC164_dependency_sha256=prior['input_sha256'],aperture='11/10',
      source_frame_dimension=7,non_native_action_order=['RC165 q_t','RC154 q_psi','RC163 q_delta'],
      finite_pairing_prefix_degree=O,new_t_finite_action_and_trial_hashes_verified=True,new_t_moment_and_norm_certificate_replayed=True,
      new_t_source_pairing_lower=[str(v[0]) for v in Qrow],new_t_source_pairing_upper=[str(v[1]) for v in Qrow],
      new_t_trial_Gram_row_order=['old qP0','old qf','old qB','old qu','old fitted qt','q_psi','q_delta_new','q_t_new'],
      new_t_trial_Gram_row_lower=[str(v[0]) for v in Rrow],new_t_trial_Gram_row_upper=[str(v[1]) for v in Rrow],
      three_trial_source_pairing_lower=ser(ql),three_trial_source_pairing_upper=ser(qu),
      three_trial_Gram_lower=ser(rl),three_trial_Gram_upper=ser(ru),signed_analytic_pairing_tails_paid=True,
      old_fitted_Ct_native_action_column_removed=True,new_t_trial_pairings_rebased=True,
      new_approximate_endpoint_Loewner_lower=ser(approxLo),new_approximate_endpoint_Loewner_upper=ser(approxHi),
      new_nominal_residual_Gram_upper=ser(NHi),new_nominal_residual_relative_upper=str(width(NHi)),
      previous_nominal_residual_relative_upper=prior['new_nominal_residual_relative_upper'],
      best_new_relative_endpoint_width_upper=str(endpointBest[0][0]),
      best_new_endpoint_variational_lower_psd=psd(endpointBest[1]),
      inverse_candidates=candidates,inverse_candidate_count=len(candidates),best_new_relative_inverse_width_upper=str(newWidth),
      selected_inverse_enclosure=selected,relative_inverse_width_upper=str(beta),previous_relative_inverse_width_upper=prior['relative_inverse_width_upper'],
      selected_weighted_fraction=str(alpha),selected_endpoint_gamma=str(gamma),selected_residual_tau=str(tau),
      selected_new_lower=lowerName,selected_new_upper=upperName,selected_new_action_error_Gram_upper=ser(error),
      conditioned_reference_inverse_lower=ser(lower),conditioned_reference_inverse_upper=ser(upper),
      half_Gram_inverse_width_gate_passed=gate,limiting_direction_budgets=budgets,
      source_and_inverse_source_coefficients_unchanged=True,true_inverse_uncertainty_lower_bound_inferred=False,
      Stage_I_closed=False,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor=('audit the required Stage I tolerance and original source transport separately from the paid half-Gram reference inverse gate' if gate else 'refine q_psi actual action or pay conditioned analytic-tail cancellations before the next reference inverse-width audit'))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=5)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC166 PASS: three-action pairing and inverse rebase',flush=True)
