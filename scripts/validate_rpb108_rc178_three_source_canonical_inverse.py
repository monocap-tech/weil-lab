"""RC178: actual three-source canonical inverse with full correlated residuals."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc129_four_vector_joint_moment import inv,mm,cong,add,transpose
from validate_rpb108_rc134_correlated_six_input_covariance import smul
from validate_rpb108_rc177_three_source_canonical_action_gram import scale,mat,width

def outer(x):return [[a*b for b in x] for a in x]
def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];prior,two,*data=map(json.loads,raw);hs=[hashlib.sha256(x).hexdigest() for x in raw]
    assert prior['milestone']=='RC177' and two['milestone']=='RC173'
    assert prior['input_sha256']==hs[2:] and two['input_sha256']==[hs[3],hs[4],hs[8],hs[5]]
    fnew,p2,p0,joint,wold,old,metric,physical=data
    # Recover the immutable carrier generator, stopping before its Gram loop.
    src=Path(__file__).with_name('validate_rpb108_rc177_three_source_canonical_action_gram.py').read_text().split("\nif __name__=='__main__':")[0]
    marker='    nominal=[[Z for _ in range(3)] for _ in range(3)];mixed=[[Z for _ in range(3)] for _ in range(3)]'
    assert src.count(marker)==1
    ns={};exec(compile(src.replace(marker,'    return locals()',1),'RC177 carrier reconstruction','exec'),ns)
    d=ns['run'](paths[2:],replay)
    dn,f,g,r0,r2,rf,neg=[d[k] for k in ['dn','f','g','r0','r2','rf','neg']]
    assert d['digest']==prior['native_w14_finite_coefficient_sha256']
    Glo=mat(prior,'source_D_Gram_lower');Ghi=mat(prior,'source_D_Gram_upper')
    Klo=mat(prior,'actual_canonical_Gram_Loewner_lower');Khi=mat(prior,'actual_canonical_Gram_Loewner_upper')
    Gmid=scale(F(1,2),add(Glo,Ghi));Kmid=scale(F(1,2),add(Klo,Khi))
    Qnom=scale(F(1,2),add(mat(prior,'nominal_full_action_Gram_entry_lower'),mat(prior,'nominal_full_action_Gram_entry_upper')))
    assert psd(Qnom)
    candidatesY={'Galerkin':mm(inv(Kmid),Gmid),'least_residual':mm(inv(Qnom),Kmid)}
    candidatesY={name:[[down(x,10**30) for x in row] for row in Y] for name,Y in candidatesY.items()}
    O=prior['finite_prefix_last_degree'];T=F(prior['common_eta_tail_D_energy_upper']);first=O+2;z=first*(first+1)
    mu=d['mu'];lam=d['lam'];delta2=F(6,z-6);deltaf=sum(mu[k]*(lam/z)**k for k in range(1,15))
    a=F(metric['actual_canonical_diagonal_metric_lower']);assert a==F(32125,230953)
    weights=[sqrtup(Ghi[i][i]) for i in range(3)];E0=mat(prior,'full_correlated_action_error_Gram_upper')
    results=[];selection=None
    modes=list(candidatesY);modes=modes[::-1] if replay else modes
    for mode in modes:
        Y=candidatesY[mode];Iminus=[[F(i==j)-Y[i][j] for j in range(3)] for i in range(3)]
        Clo=add(add(Glo,cong(Iminus,Ghi),-1),cong(Y,add(Glo,Khi,-1)))
        Chi=add(add(Ghi,cong(Iminus,Glo),-1),cong(Y,add(Ghi,Klo,-1)))
        assert psd(Clo) and psd(add(Chi,Clo,-1))
        finite=[[Z for _ in range(3)] for _ in range(3)]
        degrees=list(range(0,O+1,2));degrees=degrees[::-1] if replay else degrees
        for n in degrees:
            v=[rat(r0.get(n,F(0))),rat(r2.get(n,F(0))),plus(rat(g[n]+rf.get(n,F(0))+neg.get(n,F(0))),f.get(n,Z))]
            if n==0:
                v[0]=plus(v[0],rat(1+F(p0['canonical_constant_action_P0_correction_center'])))
                v[1]=plus(v[1],rat(F(p2['endpoint_P0_coefficient_center'])))
            if n>=2:v[0]=plus(v[0],div(rat(F(2*n+1,n*(n+1))),dn[n]))
            if n==2:v[1]=plus(v[1],rat(1+F(p2['endpoint_P2_correction_center'])))
            if n>=4:v[1]=plus(v[1],div(rat(F(2*n+1,n*(n+1)-6)),dn[n]))
            u=[rat(F(n==0)),rat(F(n==2)),f.get(n,Z)]
            residual=[minus(u[i],sum_interval([smul(rat(Y[j][i]),v[j]) for j in range(3)])) for i in range(3)]
            mass=mul(rat(2*B/F(2*n+1)),dn[n])
            for i in range(3):
                for j in range(i,3):finite[i][j]=plus(finite[i][j],smul(mass,smul(residual[i],residual[j])))
        flo=[[F(0)]*3 for _ in range(3)];fhi=[[F(0)]*3 for _ in range(3)]
        for i in range(3):
            for j in range(i,3):
                lo,hi=bounds(finite[i][j]);flo[i][j]=flo[j][i]=lo;fhi[i][j]=fhi[j][i]=hi
        Nlo,prefixHi,_=loewner(flo,fhi,weights);assert psd(Nlo)
        tailTau=F(1,1000);b=[Y[0][i]+Y[1][i]+mu[0]*Y[2][i] for i in range(3)]
        remainder=add(scale(delta2**2,outer(Y[1])),scale(deltaf**2,outer(Y[2])))
        tailHi=add(scale((1+tailTau)*T,outer(b)),scale(2*(1+1/tailTau)*T,remainder))
        Nhi=add(prefixHi,tailHi);assert psd(tailHi) and psd(add(Nhi,Nlo,-1))
        E=cong(Y,E0);assert psd(E)
        upperTau=[F(1,1000),F(1,300),F(1,100),F(1,30),F(1,10),F(1,3),F(1)]
        lowerTau=[F(0),F(1,100),F(1,30),F(1,10),F(1,3),F(1,2)]
        if replay:upperTau.reverse();lowerTau.reverse()
        best=None;rows=[]
        for tau in upperTau:
            Rhi=add(scale(1+tau,Nhi),scale(1+1/tau,E));upper=add(Chi,scale(1/a,Rhi))
            for sigma in lowerTau:
                Rlo=[[F(0)]*3 for _ in range(3)] if sigma==0 else add(scale(1-sigma,Nlo),scale(-(1/sigma-1),E))
                if not psd(Rlo):continue
                lower=add(Clo,scale(F(1,2),Rlo));gap=add(upper,lower,-1)
                assert psd(lower) and psd(gap)
                beta=width(gap,Glo);key=(beta,tau,sigma)
                rows.append(dict(upper_tau=str(tau),lower_tau=str(sigma),relative_inverse_width_upper=str(beta)))
                if best is None or key<best[0]:best=(key,lower,upper,Rlo,Rhi)
        (beta,tau,sigma),lower,upper,Rlo,Rhi=best
        assert psd(add(lower,scale(F(1,2),Glo),-1)) and psd(add(scale(1/a,Ghi),upper,-1))
        gate=add(scale(F(1,2),Glo),add(upper,lower,-1),-1)
        warmSquared=width(scale(1/a,Rhi),lower)
        item=dict(trial=mode,trial_source_coefficients=ser(Y),variational_response_lower=ser(Clo),variational_response_upper=ser(Chi),
          nominal_residual_finite_entry_lower=ser(flo),nominal_residual_finite_entry_upper=ser(fhi),
          nominal_residual_Gram_lower=ser(Nlo),nominal_residual_Gram_upper=ser(Nhi),full_inverse_trial_tail_Gram_upper=ser(tailHi),
          transformed_action_error_Gram_upper=ser(E),selected_actual_residual_Gram_lower=ser(Rlo),selected_actual_residual_Gram_upper=ser(Rhi),
          selected_upper_tau=str(tau),selected_lower_tau=str(sigma),canonical_inverse_response_lower=ser(lower),canonical_inverse_response_upper=ser(upper),
          relative_inverse_width_upper=str(beta),canonical_half_Gram_gate_matrix=ser(gate),canonical_half_Gram_gate_passed=psd(gate),
          canonical_Riesz_trial_D_error_Gram_upper=ser(scale(1/(a*a),Rhi)),canonical_Riesz_trial_canonical_error_Gram_upper=ser(scale(1/a,Rhi)),
          canonical_warmstart_relative_true_image_norm_upper=str(sqrtup(warmSquared)),canonical_warmstart_relative_true_image_squared_upper=str(warmSquared),
          relative_nominal_residual_Gram_upper=str(width(Nhi,Glo)),candidate_enclosures=sorted(rows,key=lambda x:(F(x['upper_tau']),F(x['lower_tau']))))
        results.append(item)
        key=(beta,mode)
        if selection is None or key<selection[0]:selection=(key,item)
        print('RC178 full inverse trial',mode,'relative width',float(beta),flush=True)
    results.sort(key=lambda x:x['trial']);selected=selection[1]
    assert F(selected['relative_inverse_width_upper'])<1
    probe=[F(-1,1200),F(-1,6),F(1)]
    quadratic=lambda A:sum(probe[i]*A[i][j]*probe[j] for i in range(3) for j in range(3))
    gateWitness=quadratic(mat(selected,'canonical_half_Gram_gate_matrix'));assert gateWitness<0
    nominalSquared=quadratic(mat(selected,'nominal_residual_Gram_lower'));errorSquared=quadratic(mat(selected,'transformed_action_error_Gram_upper'))
    rootLower=sqrtup(nominalSquared)-F(1,10**40)
    assert rootLower>0 and rootLower*rootLower<=nominalSquared
    residualLower=rootLower-sqrtup(errorSquared);assert residualLower>0
    relativeResidualLower=down(residualLower*residualLower/quadratic(Ghi),10**12)
    assert relativeResidualLower>F(1,10)
    return dict(milestone='RC178',status='PASS: actual three-source canonical inverse; selected half-Gram gate recorded separately',starting_commit='bef9b6cb547a05c5d260a67e5474e6ad3371fefa',input_sha256=hs,
      source_order=['P0','P2','f0'],inverse_response_definition='Sigma=(D S)^* L^-1(D S)=S^*D M^-1 S; M=D^-1 L',
      source_D_Gram_lower=ser(Glo),source_D_Gram_upper=ser(Ghi),native_w14_coefficient_sha256=d['digest'],
      trial_construction_definitions={'Galerkin':'Y=K_mid^-1 G_mid','least_residual':'Y=Qhat_mid^-1 K_mid; a trial only, actual residual evaluated independently'},
      finite_prefix_last_degree=O,first_omitted_even_degree=first,common_eta_tail_D_energy_upper=str(T),native_tail_lambda=str(lam),
      tail_P2_relative_remainder_upper=str(delta2),tail_w14_relative_remainder_upper=str(deltaf),full_tail_mixed_remainders_paid=True,
      evaluated_inverse_trials=results,selected_trial=selected['trial'],selected_enclosure=selected,
      actual_three_source_canonical_inverse_response_certified=True,all_real_and_complex_three_source_mixtures_paid=True,
      relative_inverse_width_upper=selected['relative_inverse_width_upper'],canonical_half_Gram_inverse_width_gate_passed=selected['canonical_half_Gram_gate_passed'],
      canonical_Riesz_warmstart_relative_true_image_norm_upper=selected['canonical_warmstart_relative_true_image_norm_upper'],
      half_Gram_gate_failure_witness_source_coefficients=list(map(str,probe)),half_Gram_gate_failure_witness_quadratic=str(gateWitness),
      residual_focus_source='f0-P2/6-P0/1200',residual_focus_nominal_vector='(S-VY)*probe; V is the full RC177 action carrier and Y is the selected trial',
      residual_focus_actual_D_norm_lower=str(down(residualLower)),residual_focus_actual_relative_D_norm_squared_lower=str(relativeResidualLower),
      residual_focus_nominal_to_actual_D_error_norm_upper=str(sqrtup(errorSquared)),
      prior_two_source_inverse_certificate_preserved=True,three_source_gate_failure_is_not_true_inverse_uncertainty_lower_bound=True,
      new_operator_action_performed=False,finite_compression_invariance_assumed=False,canonical_Riesz_iteration_performed=False,native_seven_source_frame_changed=False,
      full_seven_source_canonical_inverse_certified=False,original_augmentation_adjoint_range_identified=False,required_Stage_I_matrix_tolerance_specified=False,
      Stage_I_closed=False,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='pay the actual canonical action on a finite approximation of the selected residual for f0-P2/6-P0/1200, retaining its input and output tails, then enrich the inverse trial space; the three-source half-Gram gate remains open')

def sum_interval(xs):
    total=Z
    for x in xs:total=plus(total,x)
    return total

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');p.add_argument('inputs',nargs=10)
    args=p.parse_args();r=run(args.inputs,args.replay)
    if args.replay:assert json.loads(Path(args.output).read_text())==r
    else:Path(args.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC178 PASS: actual three-source canonical inverse response with full residuals')
