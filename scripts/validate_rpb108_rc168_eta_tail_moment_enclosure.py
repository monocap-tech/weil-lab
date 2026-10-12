"""RC168: paid positive common-eta moments and reference inverse re-audit."""
from pathlib import Path
from fractions import Fraction as F
from math import sqrt,ceil
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,mul,div,bounds,up,down,sqrtup,psd,ser,loewner
from validate_rpb108_rc129_four_vector_joint_moment import add,mm,inv,cong,transpose

def run(paths,reverse=False):
    raw=[Path(p).read_bytes() for p in paths]
    prior,gram,assembly,transport,action,interface,joint,parameters=map(json.loads,raw)
    assert [d['milestone'] for d in (prior,gram,assembly,transport,action,interface,joint,parameters)]==['RC167','RC159','RC158','RC160','RC165','RC155','RC136','RC129']
    hs=[hashlib.sha256(b).hexdigest() for b in raw]
    assert prior['input_sha256'][1:]==[hs[2],hs[1]]
    assert gram['input_sha256'][:3]==[hs[2],hs[5],hs[6]]
    assert assembly['input_sha256'][2]==hs[5] and assembly['input_sha256'][5]==hs[6]
    assert transport['input_sha256']==[hs[2],hs[1]]
    assert action['input_sha256'][1]==hs[6] and action['input_sha256'][3:6]==[hs[5],hs[2],hs[1]]
    assert joint['input_sha256'][6]==hs[7]
    mat=lambda d,k:[[F(x) for x in row] for row in d[k]]
    oldGLo,oldGHi=mat(gram,'conditioned_source_Gram_lower'),mat(gram,'conditioned_source_Gram_upper')
    weights=[sqrtup(oldGHi[i][i]) for i in range(7)]
    yp=mat(prior,'combined_inverse_source_tail_polynomials');ap=mat(prior,'combined_action_tail_polynomials');rp=mat(prior,'combined_nominal_residual_tail_polynomials')
    sp=transpose(mat(gram,'conditioned_scaled_tail_polynomial_coefficients'))
    degree=2*(max(map(len,yp+ap+rp+sp))-1)
    first=16384;last=65534;lam=first*(first+1)
    s=(rat(F(parameters['actual_D_Gram_entry_lower'][0][0])/(2*B))[0],rat(F(parameters['actual_D_Gram_entry_upper'][0][0])/(2*B))[1])
    harmonic=[Z]
    for n in range(1,last+1):harmonic.append(plus(harmonic[-1],rat(F(1,n))))
    sums=[Z for _ in range(degree+1)]
    degrees=list(range(first,last+1,2));degrees=degrees[::-1] if reverse else degrees
    for n in degrees:
        z=n*(n+1);dn=plus(harmonic[n],s)
        term=div(rat(2*B*F(2*n+1,z*z)),dn);ratio=rat(F(lam,z))
        for k in range(degree+1):
            sums[k]=plus(sums[k],term);term=mul(term,ratio)
    # Monotone preceding width-two cells pay the complete remaining eta
    # energy. Every higher moment is bounded by its maximal omitted ratio.
    remaining=up(B/(F(plus(harmonic[last],s)[0])*(last-1)*last))
    rho=F(lam,(last+2)*(last+3));moments=[];ml=[];mu=[]
    for k,total in enumerate(sums):
        lo,hi=bounds(total);tail=up(remaining*rho**k)
        lower=lo;upper=up(hi+tail)
        assert 0<lower<=upper
        ml.append(lower);mu.append(upper)
        moments.append(dict(order=k,finite_block_lower=str(lo),finite_block_upper=str(hi),remaining_upper=str(tail),full_lower=str(lower),full_upper=str(upper)))
    assert all(mu[k]<=mu[0] for k in range(len(mu)))
    oldT=F(gram['common_eta_tail_D_energy_upper']);assert mu[0]<oldT
    assert oldT==up(B/(F(plus(harmonic[first-2],s)[0])*(first-3)*(first-2)))
    print('RC168 positive eta moments and all infinite remainders paid',flush=True)
    def oldpair(a,b):
        terms=[x*y for x in a for y in b]
        return oldT*sum(min(F(0),x) for x in terms),oldT*sum(max(F(0),x) for x in terms)
    def product(a,b):
        coeff=[F(0)]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):coeff[i+j]+=x*y
        return coeff
    def newpair(a,b):
        coeff=product(a,b);lo=hi=F(0)
        orders=list(range(len(coeff)));orders=orders[::-1] if reverse else orders
        for k in orders:
            c=coeff[k];lo+=c*(ml[k] if c>=0 else mu[k]);hi+=c*(mu[k] if c>=0 else ml[k])
        return down(lo),up(hi)
    def entries(polys,other=None,old=False):
        L=[[F(0)]*7 for _ in range(7)];U=[[F(0)]*7 for _ in range(7)]
        pair=oldpair if old else newpair
        for i in range(7):
            for j in range(i,7):
                if other is None:lo,hi=pair(polys[i],polys[j])
                else:
                    l1,h1=pair(polys[i],other[j]);l2,h2=pair(polys[j],other[i]);lo=(l1+l2)/2;hi=(h1+h2)/2
                L[i][j]=L[j][i]=lo;U[i][j]=U[j][i]=hi
        return L,U
    oldHL,oldHU=entries(ap,yp,True);newHL,newHU=entries(ap,yp)
    oldRL,oldRU=entries(rp,old=True);newRL,newRU=entries(rp)
    oldhLo,oldhHi,_=loewner(oldHL,oldHU,weights);newhLo,newhHi,_=loewner(newHL,newHU,weights)
    _,oldnHi,_=loewner(oldRL,oldRU,weights);_,newnHi,_=loewner(newRL,newRU,weights)
    # The interval-to-Loewner construction is linear at fixed weights.
    # Subtracting the old exact tail interval leaves a valid finite-prefix
    # enclosure, including every inherited outward-rounding margin.
    prefixHLo=add(mat(prior,'direct_approximate_endpoint_Loewner_lower'),oldhLo,-1)
    prefixHHi=add(mat(prior,'direct_approximate_endpoint_Loewner_upper'),oldhHi,-1)
    prefixNHi=add(mat(prior,'direct_nominal_residual_Gram_upper'),oldnHi,-1)
    assert psd(prefixNHi) and psd(add(prefixHHi,prefixHLo,-1))
    approxLo,approxHi=add(prefixHLo,newhLo),add(prefixHHi,newhHi)
    NHi=add(prefixNHi,newnHi);assert psd(NHi)
    sourceTL,sourceTU=entries(sp);sourceTailLo,sourceTailHi,_=loewner(sourceTL,sourceTU,weights)
    prefixGHi=add(oldGHi,mat(gram,'conditioned_correlated_tail_Gram_upper'),-1)
    GLo,GHi=add(oldGLo,sourceTailLo),add(prefixGHi,sourceTailHi)
    assert psd(GLo) and psd(add(GHi,GLo,-1))
    V=mat(transport,'trial_conditioned_source_matrix');I=[[F(i==j) for j in range(7)] for i in range(7)];ZV=add(I,V,-1)
    GL,GU=add(GLo,cong(ZV,GHi),-1),add(GHi,cong(ZV,GLo),-1)
    GY=cong(V,GHi)
    # Actual action-error matrices remain valid as fixed quadratic uppers;
    # a better source Gram does not assert a better measured action norm.
    Y=mat(assembly,'trial_source_frame_coefficients');eps=list(map(F,action['updated_action_column_D_norm_error_upper']))
    K=inv(cong(mat(interface,'source_frame_matrix'),mat(joint,'actual_D_Gram_Loewner_lower')))
    w=[sqrtup(K[i][i]) for i in range(7)];total=sum(eps[i]*w[i] for i in range(7))
    weighted=cong(Y,[[total*eps[i]/w[i] if i==j else F(0) for j in range(7)] for i in range(7)])
    uniform=mat(action,'new_inverse_trial_error_Gram_upper')
    try:
        import numpy as np
        scale=[sqrt(float(GLo[i][i])) for i in range(7)]
        chol=np.linalg.cholesky([[float(GLo[i][j])/scale[i]/scale[j] for j in range(7)] for i in range(7)])
    except (ImportError,ValueError,ArithmeticError):chol=None
    def width(gap):
        yes=lambda k:psd(add([[F(k,10**6)*x for x in row] for row in GLo],gap,-1))
        if chol is not None:
            try:
                A=np.array([[float(gap[i][j])/scale[i]/scale[j] for j in range(7)] for i in range(7)])
                left=np.linalg.solve(chol,A);H=np.linalg.solve(chol,left.T).T
                n=max(1,ceil(float(np.linalg.eigvalsh((H+H.T)/2)[-1])*10**6))
                for _ in range(8):
                    if yes(n):
                        if not yes(n-1):return F(n,10**6)
                        n-=1
                    else:n+=1
            except (ValueError,ArithmeticError):pass
        hi=1
        while not yes(hi):hi*=2
        lo=0
        while hi-lo>1:
            mid=(lo+hi)//2
            if yes(mid):hi=mid
            else:lo=mid
        assert yes(hi) and not yes(lo);return F(hi,10**6)
    candidates=[];best=None;endpointBest=None
    alphas=[F(0),F(1,2),F(1)];gammas=[F(1),F(2),F(3),F(4)];taus=[F(1,4),F(1,2),F(1),F(2),F(4)]
    if reverse:alphas.reverse();gammas.reverse();taus.reverse()
    structuralLo=[[x/2 for x in row] for row in GLo]
    for alpha in alphas:
        E=add([[alpha*x for x in row] for row in weighted],[[(1-alpha)*x for x in row] for row in uniform]);assert psd(E)
        for gamma in gammas:
            deviation=add([[gamma*x/2 for x in row] for row in E],[[x/(2*gamma) for x in row] for row in GY])
            hlo,hhi=add(approxLo,deviation,-1),add(approxHi,deviation)
            endpointWidth=width(add(hhi,hlo,-1));LLo,LHi=add(GL,hhi,-1),add(GU,hlo,-1)
            if endpointBest is None or (endpointWidth,alpha,gamma)<endpointBest[0]:endpointBest=((endpointWidth,alpha,gamma),LLo)
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
                    candidates.append(dict(weighted_fraction=str(alpha),gamma=str(gamma),tau=str(tau),lower=lowerName,upper=upperName,relative_inverse_width_upper=str(beta)))
                    if best is None or key<best[0]:best=(key,lower,upper,E)
    (newWidth,alpha,gamma,tau,lowerName,upperName),lower,upper,E=best
    oldLower,oldUpper=mat(prior,'conditioned_reference_inverse_lower'),mat(prior,'conditioned_reference_inverse_upper')
    oldWidthInNewGram=width(add(oldUpper,oldLower,-1));selected='RC168 paid eta moments';beta=newWidth
    if oldWidthInNewGram<beta:beta=oldWidthInNewGram;lower,upper=oldLower,oldUpper;selected='retained RC167 enclosure measured against new Gram lower'
    assert psd(lower) and psd(add(upper,lower,-1))
    assert psd(add([[beta*x for x in row] for row in GLo],add(upper,lower,-1),-1))
    gateMatrix=add([[F(1,2)*x for x in row] for row in GLo],add(upper,lower,-1),-1);gate=psd(gateMatrix)
    candidates.sort(key=lambda c:(F(c['weighted_fraction']),F(c['gamma']),F(c['tau']),c['lower'],c['upper']))
    assert width(add(GHi,GLo,-1))<F(gram['relative_source_Gram_width_upper'])
    return dict(milestone='RC168',status='PASS: positive eta tail moment enclosures and full reference inverse audit',
      starting_commit='515236e9c87245d5252c30791c0177886bf72def',input_sha256=hs,aperture='11/10',
      eta_definition='eta_n=(2*n+1)/(n*(n+1)*D_n), D_n=s+H_n; even n>=16384',
      moment_definition='M_k=sum_even_n>=16384 2*a*(2*n+1)/(n^2*(n+1)^2*D_n)*(16384*16385/[n*(n+1)])^k',
      finite_tail_first_degree=first,finite_tail_last_degree=last,moment_count=len(moments),tail_moment_intervals=moments,
      remaining_eta_D_energy_upper=str(remaining),remaining_monomial_ratio_upper=str(rho),
      products_combined_by_degree_before_sign_bounds=True,finite_prefix_enclosures_recovered_by_exact_linearity=True,
      original_outward_rounding_margins_retained=True,no_new_endpoint_actions_performed=True,
      conditioned_source_Gram_lower=ser(GLo),conditioned_source_Gram_upper=ser(GHi),relative_source_Gram_width_upper=str(width(add(GHi,GLo,-1))),
      approximate_endpoint_Loewner_lower=ser(approxLo),approximate_endpoint_Loewner_upper=ser(approxHi),approximate_endpoint_relative_width_upper=str(width(add(approxHi,approxLo,-1))),
      nominal_residual_Gram_upper=ser(NHi),nominal_residual_relative_upper=str(width(NHi)),best_endpoint_relative_width_upper=str(endpointBest[0][0]),
      inverse_candidates=candidates,inverse_candidate_count=len(candidates),best_new_relative_inverse_width_upper=str(newWidth),
      selected_inverse_enclosure=selected,relative_inverse_width_upper=str(beta),previous_relative_inverse_width_upper=prior['relative_inverse_width_upper'],
      previous_enclosure_width_against_new_source_lower=str(oldWidthInNewGram),
      selected_weighted_fraction=str(alpha),selected_endpoint_gamma=str(gamma),selected_residual_tau=str(tau),selected_lower=lowerName,selected_upper=upperName,
      conditioned_reference_inverse_lower=ser(lower),conditioned_reference_inverse_upper=ser(upper),half_Gram_gate_matrix=ser(gateMatrix),half_Gram_inverse_width_gate_passed=gate,
      source_and_action_trials_unchanged=True,action_error_norms_unchanged=True,source_conditioning_and_inverse_coefficients_unchanged=True,
      true_inverse_uncertainty_lower_bound_inferred=False,Stage_I_closed=False,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor=('audit and discharge the actual Stage I required tolerance and transport obligations; the reference half-Gram width gate is now paid' if gate else 'refine remaining tail moments or q_psi action and retain the paid complete three-action interface'))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=8)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC168 PASS: positive eta moments and inverse enclosure',flush=True)
