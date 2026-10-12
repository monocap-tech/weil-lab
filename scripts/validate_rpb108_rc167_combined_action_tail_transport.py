"""RC167: aggregate signed action/source tails before endpoint/residual bounds."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import Z,rat,plus,down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc134_correlated_six_input_covariance import smul
from validate_rpb108_rc129_four_vector_joint_moment import add,mm

def run(paths,reverse=False):
    raw=[Path(p).read_bytes() for p in paths];prior,assembly,gram=map(json.loads,raw)
    hs=[hashlib.sha256(b).hexdigest() for b in raw]
    assert [d['milestone'] for d in (prior,assembly,gram)]==['RC166','RC158','RC159']
    assert prior['input_sha256'][2:4]==hs[1:]
    index={hashlib.sha256(p.read_bytes()).hexdigest():str(p) for p in Path(paths[0]).parent.glob('*.json')}
    earlier=[index[h] for h in prior['input_sha256']]
    path=Path(__file__).with_name('validate_rpb108_rc166_three_action_pairing_rebase.py');src=path.read_text();ns={'__file__':str(path)}
    exec(compile(src[:src.index('\n    candidates=[]')]+'\n    return locals()\n','RC167-reconstruction','exec'),ns)
    d=ns['run'](earlier,reverse)
    assert ser(d['ql'])==prior['three_trial_source_pairing_lower'] and ser(d['ru'])==prior['three_trial_Gram_upper']
    r,b=d['r'],d['b'];X,Y=d['X'],d['Y'];W=d['a']['W'];GLo,GHi=d['GLo'],d['GHi'];width=d['width']
    O=r['O'];degrees=list(range(0,O+1,2));degrees=degrees[::-1] if reverse else degrees
    newtrials=[d['qt'],b['trials'][5],b['trials'][6]]
    newpolys=[d['qtpoly'],b['trialpolys'][5],b['trialpolys'][6]]
    sourceNative=mm(W,X);yNative=mm(W,Y)
    # The aggregate native coefficients are exact rationals. All signed
    # tail coefficients are combined before products and absolute bounds.
    def aggregate(nativeCoefficients,trialCoefficients=None):
        vectors=[];polys=[]
        count=max([len(p) for p in r['polys']+newpolys])
        for j in range(7):
            coeff=[nativeCoefficients[i][j] for i in range(7)]
            vector=r['vector'](coeff)
            if trialCoefficients is not None:
                for n in degrees:
                    for k in range(3):vector[n]=plus(vector[n],smul(rat(trialCoefficients[k][j]),newtrials[k][n]))
            poly=[sum(coeff[i]*(r['polys'][i][k] if k<len(r['polys'][i]) else F(0)) for i in range(7)) for k in range(count)]
            if trialCoefficients is not None:
                poly=[poly[k]+sum(trialCoefficients[i][j]*(newpolys[i][k] if k<len(newpolys[i]) else F(0)) for i in range(3)) for k in range(count)]
            vectors.append(vector);polys.append(poly)
        return vectors,polys
    y,yp=aggregate(yNative)
    action,ap=aggregate(d['nativeAction'],Y[4:])
    residual,rp=aggregate(d['Znative'],Y[4:])
    assert all(rp[j][k]==ap[j][k]+yp[j][k]-sum(sourceNative[i][j]*(r['polys'][i][k] if k<len(r['polys'][i]) else F(0)) for i in range(7)) for j in range(7) for k in range(len(rp[j])))
    HL=[[F(0)]*7 for _ in range(7)];HU=[[F(0)]*7 for _ in range(7)]
    RL=[[F(0)]*7 for _ in range(7)];RU=[[F(0)]*7 for _ in range(7)]
    for i in range(7):
        for j in range(i,7):
            l1,h1=r['pair'](action[i],y[j],ap[i],yp[j])
            l2,h2=r['pair'](action[j],y[i],ap[j],yp[i])
            HL[i][j]=HL[j][i]=down((l1+l2)/2);HU[i][j]=HU[j][i]=up((h1+h2)/2)
            low,high=r['pair'](residual[i],residual[j],rp[i],rp[j])
            RL[i][j]=RL[j][i]=low;RU[i][j]=RU[j][i]=high
    hLo,hHi,_=loewner(HL,HU,d['weights']);_,nHi,_=loewner(RL,RU,d['weights'])
    assert psd(nHi) and psd(add(hHi,hLo,-1))
    oldHLo,oldHHi=d['approxLo'],d['approxHi'];oldN=d['NHi']
    oldEndpoint=width(add(oldHHi,oldHLo,-1));newEndpoint=width(add(hHi,hLo,-1))
    oldResidual,newResidual=width(oldN),width(nHi)
    # Choose whole valid enclosures, not entrywise or matrix minima.
    if newEndpoint<oldEndpoint:approxLo,approxHi=hLo,hHi;endpointSelection='combined signed tails'
    else:approxLo,approxHi=oldHLo,oldHHi;endpointSelection='retained RC166 block transport'
    if newResidual<oldResidual:NHi=nHi;residualSelection='combined signed tails'
    else:NHi=oldN;residualSelection='retained RC166 residual'
    print('RC167 signed endpoint and nominal residual combinations paid',flush=True)
    candidates=[];best=None;endpointBest=None
    alphas=[F(0),F(1,2),F(1)];gammas=[F(1),F(2),F(3),F(4)];taus=[F(1,4),F(1,2),F(1),F(2),F(4)]
    if reverse:alphas.reverse();gammas.reverse();taus.reverse()
    structuralLo=[[x/2 for x in row] for row in GLo]
    for alpha in alphas:
        E=add([[alpha*x for x in row] for row in d['weighted']],[[(1-alpha)*x for x in row] for row in d['uniform']]);assert psd(E)
        for gamma in gammas:
            deviation=add([[gamma*x/2 for x in row] for row in E],[[x/(2*gamma) for x in row] for row in d['GY']])
            lo,hi=add(approxLo,deviation,-1),add(approxHi,deviation)
            endpointWidth=width(add(hi,lo,-1));LLo,LHi=add(d['t']['GL'],hi,-1),add(d['t']['GU'],lo,-1)
            if endpointBest is None or (endpointWidth,alpha,gamma)<endpointBest[0]:endpointBest=((endpointWidth,alpha,gamma),LLo,LHi)
            lowers=[('structural half Gram',structuralLo)]
            if psd(LLo):lowers.append(('positive variational lower',LLo))
            uppers=[('structural upper',F(0),GHi)]
            for tau in taus:
                error=add([[(1+tau)*x for x in row] for row in NHi],[[(1+1/tau)*x for x in row] for row in E])
                uppers.append(('paid variational upper',tau,add(LHi,error)))
            for lowerName,lower in lowers:
                for upperName,tau,upper in uppers:
                    gap=add(upper,lower,-1);assert psd(gap)
                    beta=width(gap);key=(beta,alpha,gamma,tau,lowerName,upperName)
                    candidates.append(dict(weighted_fraction=str(alpha),gamma=str(gamma),tau=str(tau),lower=lowerName,upper=upperName,relative_inverse_width_upper=str(beta),relative_endpoint_width_upper=str(endpointWidth)))
                    if best is None or key<best[0]:best=(key,lower,upper,E)
    (newWidth,alpha,gamma,tau,lowerName,upperName),lower,upper,E=best
    mat=lambda d,k:[[F(x) for x in row] for row in d[k]]
    beta=newWidth;selected='RC167 combined-tail enclosure'
    if F(prior['relative_inverse_width_upper'])<beta:
        beta=F(prior['relative_inverse_width_upper']);lower=mat(prior,'conditioned_reference_inverse_lower');upper=mat(prior,'conditioned_reference_inverse_upper');selected='retained RC166 inverse enclosure'
    assert psd(lower) and psd(add(upper,lower,-1))
    assert psd(add([[beta*x for x in row] for row in GLo],add(upper,lower,-1),-1))
    gate=psd(add([[F(1,2)*x for x in row] for row in GLo],add(upper,lower,-1),-1))
    witness=list(map(F,assembly['enclosure_width_failure_witness']))
    quad=lambda M:sum(witness[i]*M[i][j]*witness[j] for i in range(7) for j in range(7))
    qg=quad(GLo)
    candidates.sort(key=lambda c:(F(c['weighted_fraction']),F(c['gamma']),F(c['tau']),c['lower'],c['upper']))
    assert newEndpoint<oldEndpoint or newResidual<oldResidual
    return dict(milestone='RC167',status='PASS: combined signed action tails and full inverse re-audit',
      starting_commit='a29a689a4ca2ced03e136b444886dc69ef9256e6',input_sha256=hs,RC166_dependency_sha256=prior['input_sha256'],aperture='11/10',
      finite_pairing_prefix_degree=O,combined_inverse_source_tail_polynomials=ser(yp),combined_action_tail_polynomials=ser(ap),combined_nominal_residual_tail_polynomials=ser(rp),
      direct_approximate_endpoint_entry_lower=ser(HL),direct_approximate_endpoint_entry_upper=ser(HU),
      direct_approximate_endpoint_Loewner_lower=ser(hLo),direct_approximate_endpoint_Loewner_upper=ser(hHi),
      direct_nominal_residual_Gram_upper=ser(nHi),old_approximate_endpoint_relative_width_upper=str(oldEndpoint),
      direct_approximate_endpoint_relative_width_upper=str(newEndpoint),old_nominal_residual_relative_upper=str(oldResidual),direct_nominal_residual_relative_upper=str(newResidual),
      selected_endpoint_interval=endpointSelection,selected_nominal_residual_interval=residualSelection,
      selected_approximate_endpoint_Loewner_lower=ser(approxLo),selected_approximate_endpoint_Loewner_upper=ser(approxHi),selected_nominal_residual_Gram_upper=ser(NHi),
      best_new_relative_endpoint_width_upper=str(endpointBest[0][0]),best_endpoint_variational_lower_psd=psd(endpointBest[1]),
      inverse_candidates=candidates,inverse_candidate_count=len(candidates),best_new_relative_inverse_width_upper=str(newWidth),
      selected_inverse_enclosure=selected,relative_inverse_width_upper=str(beta),previous_relative_inverse_width_upper=prior['relative_inverse_width_upper'],
      conditioned_reference_inverse_lower=ser(lower),conditioned_reference_inverse_upper=ser(upper),half_Gram_inverse_width_gate_passed=gate,
      limiting_direction_old_approximate_endpoint_width=str(quad(add(oldHHi,oldHLo,-1))/qg),limiting_direction_direct_approximate_endpoint_width=str(quad(add(hHi,hLo,-1))/qg),
      limiting_direction_old_nominal_residual_upper=str(quad(oldN)/qg),limiting_direction_direct_nominal_residual_upper=str(quad(nHi)/qg),
      source_and_action_trial_vectors_unchanged=True,action_column_error_norms_unchanged=True,inverse_source_coefficients_unchanged=True,
      signed_coefficients_combined_before_tail_products=True,no_mixed_error_sign_or_tail_orthogonality_assumed=True,
      true_inverse_uncertainty_lower_bound_inferred=False,Stage_I_closed=False,
      original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor=('audit Stage I tolerance and original source transport separately from the reference half-Gram width gate' if gate else 'sharpen the actual q_psi action or test additional positive-contraction inverse bounds using the paid three-action moment interface'))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=3)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC167 PASS: signed aggregate action-tail transport',flush=True)
