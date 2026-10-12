"""RC161: full combined endpoint action with paid joint error correlations."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import psd,ser,loewner,sqrtup
from validate_rpb108_rc129_four_vector_joint_moment import add,mm,transpose,cong,inv

def run(paths,reverse=False):
    raw=[Path(p).read_bytes() for p in paths];prior,assembly,gram=map(json.loads,raw)
    assert [x['milestone'] for x in (prior,assembly,gram)]==['RC160','RC158','RC159']
    assert prior['input_sha256']==[hashlib.sha256(x).hexdigest() for x in raw[1:]]
    path=Path(__file__).with_name('validate_rpb108_rc160_correlated_variational_transport.py');src=path.read_text()
    ns={'__file__':str(path)}
    exec(compile(src[:src.index('    candidates=[]')]+'\n    return locals()\n','RC161-reconstruction','exec'),ns)
    r=ns['run'](paths[1:],reverse);d=r['d'];GLo,GHi=r['GLo'],r['GHi'];V,Y,X=r['V'],r['Y'],r['X']
    mat=lambda doc,key:[[F(x) for x in row] for row in doc[key]]
    assert ser(r['NHi'])==prior['selected_nominal_residual_Gram_upper']
    nativeAction=mm(d['T'],Y[:5]);actionFrame=mm(d['Wi'],nativeAction);actionConditioned=mm(inv(X),actionFrame)
    # H_approx = Sym <q(Y), y(Y)>. Its old part is a correlated Gram
    # polarization, and its new part retains the two direct Q blocks.
    plus=add(actionConditioned,V);minus=add(actionConditioned,V,-1)
    oldLo=add(cong(plus,GLo),cong(minus,GHi),-1)
    oldHi=add(cong(plus,GHi),cong(minus,GLo),-1)
    oldLo=[[x/4 for x in row] for row in oldLo];oldHi=[[x/4 for x in row] for row in oldHi]
    QL,QU=r['ql'],r['qu'];NL=[[F(0)]*7 for _ in range(7)];NU=[[F(0)]*7 for _ in range(7)]
    for i in range(7):
        for j in range(i,7):
            coeff=[[(Y[a+5][i]*Y[b][j]+Y[a+5][j]*Y[b][i])/2 for b in range(7)] for a in range(2)]
            lo,hi=d['interval'](coeff,QL,QU)
            NL[i][j]=NL[j][i]=lo;NU[i][j]=NU[j][i]=hi
    weights=r['weights'];nlo,nhi,_=loewner(NL,NU,weights)
    approximateLo,approximateHi=add(oldLo,nlo),add(oldHi,nhi)
    assert psd(add(approximateHi,approximateLo,-1))
    # e=Cy-q(Y), so the symmetric endpoint deviation is Sym <e,y>.
    # For every mixture c, absolute deviation is <=||e(c)|| ||y(c)||.
    # Young gives a single matrix +/- (gamma E + G_y/gamma)/2.
    GY=cong(V,GHi);assert psd(GY)
    eps=list(map(F,d['actions']['action_column_D_norm_error_upper']))
    frameLo=cong(d['W'],d['GLo']);K=inv(frameLo)
    w=[sqrtup(K[i][i]) for i in range(7)]
    total=sum(eps[i]*w[i] for i in range(7))
    weighted=cong(Y,[[total*eps[i]/w[i] if i==j else F(0) for j in range(7)] for i in range(7)])
    # Weighted Cauchy bounds (sum eps_i |c_i|)^2 by this diagonal
    # source-coordinate form. It preserves tiny old action columns.
    errors=[('RC155 global Gram bound',r['EHi']),('weighted seven-column Cauchy',weighted)]
    gammas=[F(1,4),F(1,2),F(1),F(2),F(4)]
    if reverse:errors.reverse();gammas.reverse()
    candidates=[];best=None
    for name,E in errors:
        assert psd(E)
        for gamma in gammas:
            deviation=add([[gamma*x/2 for x in row] for row in E],[[x/(2*gamma) for x in row] for row in GY])
            HL=add(approximateLo,deviation,-1);HU=add(approximateHi,deviation)
            assert psd(HU) and psd(add(HU,HL,-1))
            beta=r['width'](add(HU,HL,-1))
            candidates.append(dict(error_bound=name,gamma=str(gamma),relative_endpoint_width_upper=str(beta)))
            if best is None or (beta,name,gamma)<best[0]:best=((beta,name,gamma),HL,HU,E)
    (endpointWidth,name,gamma),HL,HU,E=best
    oldWidth=r['width'](add(r['HHi'],r['HLo'],-1))
    assert endpointWidth<oldWidth
    LLo,LHi=add(r['GL'],HU,-1),add(r['GU'],HL,-1)
    # Endpoint and residual use the same selected paid error upper.
    lower=LLo if psd(LLo) else [[x/2 for x in row] for row in GLo]
    inverseCandidates=[];inverseBest=None
    taus=[F(1,4),F(1,2),F(1),F(2),F(4)]
    if reverse:taus.reverse()
    for tau in taus:
        residual=add([[(1+tau)*x for x in row] for row in r['NHi']],[[(1+1/tau)*x for x in row] for row in E])
        upper=add(LHi,residual);gap=add(upper,lower,-1);assert psd(gap)
        beta=r['width'](gap);inverseCandidates.append(dict(tau=str(tau),relative_inverse_width_upper=str(beta)))
        if inverseBest is None or (beta,tau)<inverseBest[0]:inverseBest=((beta,tau),upper)
    baseline=r['width'](add(GHi,lower,-1))
    if baseline<inverseBest[0][0]:beta=baseline;upper=GHi;selected='correlated structural upper'
    else:beta=inverseBest[0][0];upper=inverseBest[1];selected='combined endpoint variational upper'
    bestNewWidth=beta
    if F(prior['relative_inverse_width_upper'])<beta:
        beta=F(prior['relative_inverse_width_upper'])
        lower=mat(prior,'conditioned_reference_inverse_lower');upper=mat(prior,'conditioned_reference_inverse_upper')
        selected='retained sharper RC160 enclosure'
    assert psd(lower) and psd(add(upper,lower,-1))
    assert psd(add([[beta*x for x in row] for row in GLo],add(upper,lower,-1),-1))
    witness=list(map(F,assembly['enclosure_width_failure_witness']))
    quad=lambda A:sum(witness[i]*A[i][j]*witness[j] for i in range(7) for j in range(7))
    qg=quad(GLo);oldWitness=quad(add(r['HHi'],r['HLo'],-1));newWitness=quad(add(HU,HL,-1))
    assert 0<newWitness<oldWitness
    candidates.sort(key=lambda v:(v['error_bound'],F(v['gamma'])));inverseCandidates.sort(key=lambda v:F(v['tau']))
    return dict(milestone='RC161',status='PASS: combined seven-source endpoint-functional error enclosure',
      starting_commit='35dd036a8badd49571194fb4ccd5be662ef56587',input_sha256=[hashlib.sha256(b).hexdigest() for b in raw],
      RC158_dependency_sha256=assembly['input_sha256'],aperture='11/10',
      approximate_endpoint_Loewner_lower=ser(approximateLo),approximate_endpoint_Loewner_upper=ser(approximateHi),
      selected_error_bound=name,selected_endpoint_Young_gamma=str(gamma),selected_joint_error_Gram_upper=ser(E),
      combined_endpoint_functional_Loewner_lower=ser(HL),combined_endpoint_functional_Loewner_upper=ser(HU),
      endpoint_candidates=candidates,relative_endpoint_width_upper=str(endpointWidth),previous_relative_endpoint_width_upper=str(oldWidth),
      limiting_direction_endpoint_width_over_source_lower=str(newWitness/qg),
      limiting_direction_endpoint_width_improvement_factor=str(oldWitness/newWitness),
      combined_variational_Loewner_lower=ser(LLo),combined_variational_Loewner_upper=ser(LHi),
      variational_lower_psd_verified=psd(LLo),
      selected_lower_uses_structural_half_Gram=lower==[[x/2 for x in row] for row in GLo],
      conditioned_reference_inverse_lower=ser(lower),conditioned_reference_inverse_upper=ser(upper),
      selected_inverse_upper=selected,relative_inverse_width_upper=str(beta),inverse_candidates=inverseCandidates,
      best_new_inverse_width_upper=str(bestNewWidth),
      half_Gram_inverse_width_gate_passed=psd(add([[F(1,2)*x for x in row] for row in GLo],add(upper,lower,-1),-1)),
      limiting_direction_variational_lower_over_source_lower=str(quad(LLo)/qg),
      combined_action_identity_and_mixed_error_paid=True,mixed_error_sign_or_orthogonality_assumed=False,
      true_inverse_uncertainty_lower_bound_inferred=False,
      original_Weil_or_augmented_actions_performed=False,
      whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='refine the joint action-error bound on the conditioned inverse trials, preserving accurate old columns; recheck combined endpoint positivity and full inverse precision')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=3)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC161 PASS: combined endpoint functional')
