"""RC160: transport correlated Gram bounds into the seven-source functional."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import psd,ser,loewner,sqrtup
from validate_rpb108_rc129_four_vector_joint_moment import add,mm,transpose,cong,inv

def run(paths,reverse=False):
    raw=[Path(p).read_bytes() for p in paths];prior,gram=map(json.loads,raw)
    assert [d['milestone'] for d in (prior,gram)]==['RC158','RC159']
    assert gram['input_sha256'][0]==hashlib.sha256(raw[0]).hexdigest()
    directory=Path(paths[0]).parent
    names=['rpb108_rc157_five_by_two_cross_pairings.json','rpb108_rc156_complement_direct_pairings.json',
      'rpb108_rc155_seven_source_action_interface.json','rpb108_rc149_combined_five_matrix.json',
      'rpb108_rc138_reference_variational_response.json','rpb108_rc136_seven_vector_joint_matrices.json',
      'rpb108_rc145_fifth_source_conditioning.json','rpb108_rc146_narrow_coordinate.json']
    earlier=[str(directory/n) for n in names]
    assert [hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in earlier]==prior['input_sha256']
    path=Path(__file__).with_name('validate_rpb108_rc158_seven_inverse_assembly.py');src=path.read_text()
    ns={'__file__':str(path)}
    exec(compile(src[:src.index('    LL=')]+'\n    return locals()\n','RC160-reconstruction','exec'),ns)
    d=ns['run'](earlier,reverse)
    mat=lambda doc,key:[[F(x) for x in row] for row in doc[key]]
    X,Y,U=d['X'],d['Y'],d['U'];V=mm(inv(X),Y)
    GLo,GHi=mat(gram,'conditioned_source_Gram_lower'),mat(gram,'conditioned_source_Gram_upper')
    assert GLo==mat(prior,'conditioned_source_Gram_lower')
    I=[[F(i==j) for j in range(7)] for i in range(7)];Z=add(I,V,-1)
    # Exact correlated identity: S^*Y+Y^*S-Y^*Y = G-(S-Y)^*(S-Y).
    # This keeps the entire Gram Loewner uncertainty correlated, rather
    # than extracting independently uncertain entries before cancellation.
    GL=add(GLo,cong(Z,GHi),-1);GU=add(GHi,cong(Z,GLo),-1)
    assert psd(add(GU,GL,-1))
    HL=[[F(0)]*7 for _ in range(7)];HU=[[F(0)]*7 for _ in range(7)]
    for i in range(7):
        for j in range(i,7):
            coeff=[[U[a][i]*U[b][j] for b in range(7)] for a in range(7)]
            lo,hi=d['interval'](coeff,d['HBL'],d['HBU'])
            HL[i][j]=HL[j][i]=lo;HU[i][j]=HU[j][i]=hi
    weights=[sqrtup(GHi[i][i]) for i in range(7)]
    HLo,HHi,Herr=loewner(HL,HU,weights)
    LLo,LHi=add(GL,HHi,-1),add(GU,HLo,-1)
    oldNHi=mat(prior,'nominal_residual_Gram_Loewner_upper')
    EHi=mat(prior,'joint_action_error_Gram_Loewner_upper')
    structuralLo=[[x/2 for x in row] for row in GLo]
    lower=LLo if psd(LLo) else structuralLo
    def width(gap):
        def yes(n):return psd(add([[F(n,10**6)*x for x in row] for row in GLo],gap,-1))
        hi=1
        while not yes(hi):hi*=2
        lo=0
        while hi-lo>1:
            mid=(lo+hi)//2
            if yes(mid):hi=mid
            else:lo=mid
        assert yes(hi) and not yes(lo)
        return F(hi,10**6)
    # Transport the carrier part of the nominal residual as a complete
    # correlated Gram quadratic; keep directly paid q_new cross terms.
    Znative=add(mm(d['W'],add(Y,X,-1)),mm(d['T'],Y[:5]))
    Zframe=mm(d['Wi'],Znative);Zconditioned=mm(inv(X),Zframe)
    ql=mat(d['cross'],'new_trial_old_source_pairing_lower');qu=mat(d['cross'],'new_trial_old_source_pairing_upper')
    qnl=mat(d['new'],'trial_source_pairing_entry_lower');qnu=mat(d['new'],'trial_source_pairing_entry_upper')
    ql=[ql[i]+qnl[i] for i in range(2)];qu=[qu[i]+qnu[i] for i in range(2)]
    rl,ru=mat(d['new'],'trial_Gram_entry_lower'),mat(d['new'],'trial_Gram_entry_upper')
    CL=[[F(0)]*7 for _ in range(7)];CU=[[F(0)]*7 for _ in range(7)]
    for i in range(7):
        for j in range(i,7):
            a,b=d['interval']([[Y[k+5][i]*Zframe[l][j]+Y[k+5][j]*Zframe[l][i] for l in range(7)] for k in range(2)],ql,qu)
            c,e=d['interval']([[Y[k+5][i]*Y[l+5][j] for l in range(2)] for k in range(2)],rl,ru)
            CL[i][j]=CL[j][i]=a+c;CU[i][j]=CU[j][i]=b+e
    _,CHi,_=loewner(CL,CU,weights)
    newNHi=add(cong(Zconditioned,GHi),CHi);assert psd(newNHi)
    oldNorm,newNorm=width(oldNHi),width(newNHi)
    residualRefined=newNorm<oldNorm
    NHi=newNHi if residualRefined else oldNHi
    candidates=[];best=None
    options=[F(1,4),F(1,2),F(1),F(2),F(4)]
    if reverse:options.reverse()
    for tau in options:
        residual=add([[(1+tau)*x for x in row] for row in NHi],[[(1+1/tau)*x for x in row] for row in EHi])
        upper=add(LHi,residual);gap=add(upper,lower,-1)
        assert psd(gap)
        beta=width(gap);candidates.append(dict(tau=str(tau),relative_inverse_width_upper=str(beta)))
        if best is None or (beta,tau)<best[0]:best=((beta,tau),upper)
    baseline=width(add(GHi,lower,-1))
    if baseline<best[0][0]:beta=baseline;upper=GHi;selection='correlated structural upper'
    else:beta=best[0][0];upper=best[1];selection='correlated variational upper'
    assert psd(lower) and psd(add(upper,lower,-1))
    assert psd(add([[beta*x for x in row] for row in GLo],add(upper,lower,-1),-1))
    assert beta<F(prior['relative_source_Gram_inverse_matrix_width_upper'])
    witness=list(map(F,prior['enclosure_width_failure_witness']))
    quad=lambda A:sum(witness[i]*A[i][j]*witness[j] for i in range(7) for j in range(7))
    # Separate budgets on the limiting conditioned direction identify the
    # next estimate to sharpen without treating a failed enclosure as a
    # mathematical obstruction or a true inverse uncertainty lower bound.
    qg=quad(GLo)
    budgets=dict(Gram_functional_interval_width_over_source_lower=str(quad(add(GU,GL,-1))/qg),
      endpoint_functional_interval_width_over_source_lower=str(quad(add(HHi,HLo,-1))/qg),
      variational_lower_over_source_lower=str(quad(LLo)/qg),
      selected_nominal_residual_upper_over_source_lower=str(quad(NHi)/qg),
      inherited_action_error_upper_over_source_lower=str(quad(EHi)/qg),
      selected_inverse_width_over_source_lower=str(quad(add(upper,lower,-1))/qg))
    candidates.sort(key=lambda v:F(v['tau']))
    return dict(milestone='RC160',status='PASS: correlated Gram transport and seven-source inverse-width re-audit',
      starting_commit='7564929eb405a7f9a0874f60d1ec8ff48f082001',input_sha256=[hashlib.sha256(b).hexdigest() for b in raw],
      RC158_dependency_sha256=prior['input_sha256'],aperture='11/10',
      trial_conditioned_source_matrix=ser(V),
      correlated_Gram_functional_Loewner_lower=ser(GL),correlated_Gram_functional_Loewner_upper=ser(GU),
      endpoint_functional_Loewner_lower=ser(HLo),endpoint_functional_Loewner_upper=ser(HHi),
      endpoint_interval_error_diagonal=list(map(str,Herr)),
      correlated_variational_Loewner_lower=ser(LLo),correlated_variational_Loewner_upper=ser(LHi),
      variational_lower_psd_verified=psd(LLo),selected_lower_uses_structural_half_Gram=not psd(LLo),
      conditioned_reference_inverse_lower=ser(lower),conditioned_reference_inverse_upper=ser(upper),
      selected_upper=selection,relative_inverse_width_upper=str(beta),candidate_widths=candidates,
      previous_relative_inverse_width_upper=prior['relative_source_Gram_inverse_matrix_width_upper'],
      old_nominal_residual_relative_upper=str(oldNorm),transported_nominal_residual_relative_upper=str(newNorm),
      selected_nominal_residual_Gram_upper=ser(NHi),
      limiting_direction_separate_budgets=budgets,
      half_Gram_inverse_width_gate_passed=psd(add([[F(1,2)*x for x in row] for row in GLo],add(upper,lower,-1),-1)),
      correlated_Gram_functional_transport_performed=True,
      nominal_residual_correlated_transport_performed=True,
      nominal_residual_bound_inherited_unchanged=not residualRefined,endpoint_joint_error_correlation_refined=False,
      true_inverse_uncertainty_lower_bound_inferred=False,
      original_Weil_or_augmented_actions_performed=False,
      whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='refine the conditioned endpoint functional using the combined action identity and joint error map; retain the improved correlated nominal residual and rerun the full inverse-width gate')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=2)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC160 PASS: correlated variational Gram transport')
