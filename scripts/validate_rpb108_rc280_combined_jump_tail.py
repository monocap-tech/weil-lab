"""RC280: combine endpoint jumps before bounding infinite prime-output tails."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc279_six_mode_gate as parent
import validate_rpb108_rc262_prime_tail_source_1024 as leg
import validate_rpb108_rc277_weighted_prime_schur as schur
ROOT=parent.ROOT;up=parent.up;down=parent.down;root=parent.root
orig=parent.orig;p=parent.p;B=parent.B;m=leg.m
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc279_six_mode_gate.json':'bd729c0f5a41debac61a0f3c37276bb94e7834e5','notes/RPB108_RC279_SIX_MODE_GATE_20261014.md':'4efd5fd45ce04df9967914a376242c7da00eb343'})
HELPER_PINS['scripts/validate_rpb108_rc279_six_mode_gate.py']='02ff6e1b70e79ede5691aa55bc98c877939cce23'

def step_tails(parameters,reverse):
    rows=[];step_coefficients=[]
    for row in parameters:
        b=abs(1-F(row['chosen_translation'])/B);assert 0<b<1
        values=leg.legendre_intervals(b,reverse);tails=[];by_parity=[]
        for base in range(2):
            norm=2*B*(b if base==0 else 1-b)
            captured=[2*B*b*b] if base==0 else [];coef=[m.ip(F(0)) for n in range(2049)];coef[0]=m.ip(-b if base==0 else F(0))
            for n in range(1,2049):
                if n%2!=base:continue
                v=m.isc(m.ia(values[n-1],m.neg(m.isc(values[n],b))),F(2*n+1,n+1))
                coef[n]=v
                minimum=F(0) if v[0]<=0<=v[1] else min(abs(v[0]),abs(v[1]))
                captured.append(down(orig.mass(n)*minimum*minimum))
            if reverse:captured.reverse()
            capture=sum(captured,F(0));tail=up(norm-capture);assert 0<tail<norm
            tails.append(dict(parity=['even','odd'][base],full_step_pair_physical_norm_squared=str(norm),captured_through_2048_lower=str(capture),step_pair_physical_tail_upper=str(tail)))
            by_parity.append(coef)
        rows.append(dict(prime_power=row['n'],positive_boundary=str(b),chosen_coefficient=row['chosen_coefficient'],parity_step_pair_tails=tails))
        step_coefficients.append(by_parity)
    assert len(rows)==7 and len({v['positive_boundary'] for v in rows})==7
    universal=[];knots=sorted({F(0),F(1)}|{F(v['positive_boundary']) for v in rows})
    for base in range(2):
        signed=[F(v['chosen_coefficient'])*(1 if F(parameters[k]['chosen_translation'])<B else (-1)**(base+1)) for k,v in enumerate(rows)]
        cells=[]
        for l,r in zip(knots,knots[1:]):
            mid=(l+r)/2;value=F(0)
            for k,v in enumerate(rows):
                b=F(v['positive_boundary'])
                shape=(-F(mid<b)) if base==0 else F(mid>b)
                value+=signed[k]*shape
            cells.append((r-l)*value*value)
        norm=2*B*sum(cells,F(0))
        captured=[]
        for n in range(base,2049,2):
            value=m.ip(F(0))
            for k in range(7):value=m.ia(value,m.isc(step_coefficients[k][base][n],signed[k]))
            minimum=F(0) if value[0]<=0<=value[1] else min(abs(value[0]),abs(value[1]))
            captured.append(down(orig.mass(n)*minimum*minimum))
        if reverse:captured.reverse()
        capture=sum(captured,F(0));tail=up(norm-capture);assert 0<tail<norm
        universal.append(dict(parity=['even','odd'][base],signed_jump_coefficients=list(map(str,signed)),piecewise_constant_physical_energy=str(norm),captured_through_2048_lower=str(capture),complete_universal_jump_physical_tail_upper=str(tail),all_cross_prime_jump_terms_retained=True))
    return rows,universal

def endpoint_tail(a,first,sl,H):
    x=F(first*(first+1));ts=[F(n*(n+1)) for n in range(len(a))];tmax=max(ts);assert x>tmax
    moments=[sum((c*t**k for c,t in zip(a,ts)),F(0)) for k in range(4)]
    absolute=sum((abs(c)*t**4 for c,t in zip(a,ts)),F(0));rem=absolute/(x**4*(1-tmax/x))
    lo=moments[0]+sum((min(F(0),moments[k])/x**k for k in range(1,4)),F(0))-rem
    hi=moments[0]+sum((max(F(0),moments[k])/x**k for k in range(1,4)),F(0))+rem
    upper=max(abs(lo),abs(hi));parity_sum=(F(1,first*first)+F(1,first*first)-F(1,(first+1)**2))/2
    bound=up(2*B*upper*upper*parity_sum/(H[first]+sl))
    return bound,dict(signed_endpoint_moments=list(map(str,moments)),geometric_remainder_upper=str(up(rem)),uniform_endpoint_bracket_absolute_upper=str(up(upper)),endpoint_D_tail_upper=str(bound),arbitrary_endpoint_sum_sign_supported=True)

def controls():
    # Paired step projections include their constant term and parity exactly.
    b=F(2,5)
    for base in [0,1]:
        for n in range(9):
            poly=orig.legendre(n)
            integral=-orig.integral(poly,-b,b) if base==0 else orig.integral(poly,b,F(1))-orig.integral(poly,F(-1),-b)
            actual=F(2*n+1,2)*integral
            if n==0:formula=-b if base==0 else F(0)
            elif n%2!=base:formula=F(0)
            else:formula=F(2*n+1,n+1)*(parent.high.prime.evaluate(orig.legendre(n-1),b)-b*parent.high.prime.evaluate(poly,b))
            assert actual==formula
    # Exact derivative Gram needed for the continuous remainder's energy.
    for n in range(1,9):
        for j in range(1,n+1):
            deriv=lambda q:[(k+1)*v for k,v in enumerate(q[1:])]
            value=orig.integral(orig.product(deriv(orig.legendre(n)),deriv(orig.legendre(j))))
            assert value==(F(j*(j+1)) if (n-j)%2==0 else F(0))
    # Correlated jump cancellation must precede absolute values.
    a=[F(1),F(-1)];assert abs(sum(a))==0<sum(map(abs,a))
    return dict(exact_paired_step_projection_and_parity_checked=True,exact_Legendre_derivative_Gram_checked=True,endpoint_jump_cancellation_before_norm_checked=True,inherited_joint_covariance_controls=parent.controls())

def run(reverse=False):
    data={}
    for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
        raw=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==sha,(path,'pin')
        if path.endswith('.json'):data[path]=json.loads(raw)
    get=lambda s:data['certificates/rpb108_rc'+s+'.json']
    prior=get('279_six_mode_gate');refs=get('278_smaller_positive_reference')['smaller_reference_certificates']
    metric=get('129_four_vector_joint_moment');sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B)
    H=[F(0)]
    for n in range(1,2051):H.append(H[-1]+F(1,n))
    parameters=prior['coupled_six_mode_gate_certificates'][0]['actual_polynomial_action_certificates'][0]['prime_projection_certificate']['prime_controls']['chosen_prime_model_parameters']
    for r in prior['coupled_six_mode_gate_certificates']:
        for act in r['actual_polynomial_action_certificates']:
            assert act['prime_projection_certificate']['prime_controls']['chosen_prime_model_parameters']==parameters
    for r in get('274_mixed_diagonal_inverse')['projection_mixed_inverse_response_certificates']:
        assert r['secondary_prime_projection_certificate']['prime_controls']['chosen_prime_model_parameters']==parameters
    modelrows=[dict(n=v['n'],translation_lower=v['chosen_translation'],translation_upper=v['chosen_translation'],coefficient_lower=v['chosen_coefficient'],coefficient_upper=v['chosen_coefficient']) for v in parameters]
    modelnorm=F(3013,1000);modelproof=schur.prime_bound(modelrows,F(3,10),modelnorm,reverse);assert modelproof is not None
    steps,universal=step_tails(parameters,reverse);rows=[]
    for base,old in enumerate(prior['coupled_six_mode_gate_certificates']):
        ref=refs[base];lam=F(ref['augmentation_coefficient']);mu=F(ref['full_D_reference_floor_lower']);first=ref['first_omitted_degree'];tailfirst=2049 if base else 2050
        tailweight=down(1-lam/down(H[tailfirst]+sl));Y=[[F(r['exact_basis_coefficients'][k]) for r in old['response_trials']] for k in range(4)]
        Z0=list(map(F,ref['exact_trial_Legendre_coefficients']));trialproof=[];tails=[];trialvectors=[];endpointtails=[]
        for j in range(3):
            a=[Y[0][j]*v for v in Z0]
            for k in range(3):a[base+2*k]+=Y[k+1][j]
            S=sum(a,F(0));derivative_energy=B*sum((u*v*min(n,d)*(min(n,d)+1) for n,u in enumerate(a) for d,v in enumerate(a) if (n-d)%2==0),F(0));assert derivative_energy>=0
            trialvectors.append(a)
            jumpnorm=up(abs(S)*root(F(universal[base]['complete_universal_jump_physical_tail_upper'])))
            continuous=up(modelnorm*root(up(derivative_energy/F(tailfirst*(tailfirst+1)))))
            physical=up((jumpnorm+continuous)**2);primeD=up(physical/(H[tailfirst]+sl))
            endpoint,ep=endpoint_tail(a,tailfirst,sl,H)
            endpointtails.append(up(endpoint/tailweight))
            tail=up((root(primeD)+root(endpoint))**2/tailweight);tails.append(tail)
            trialproof.append(dict(source='P'+str(base+2*j),exact_trial_Legendre_coefficients=list(map(str,a)),signed_endpoint_value=str(S),input_derivative_physical_energy=str(derivative_energy),combined_prime_jump_tail_norm_upper=str(jumpnorm),continuous_prime_remainder_tail_norm_upper=str(continuous),combined_prime_physical_tail_upper=str(physical),combined_prime_D_tail_upper=str(primeD),endpoint_tail_certificate=ep,complete_original_model_inverse_weighted_tail_upper=str(tail)))
        # Remove only supported model tails from the old noise construction;
        # retain all global action faults and all finite interval uncertainty.
        oldhigh=get('274_mixed_diagonal_inverse')['projection_mixed_inverse_response_certificates'][base];scale=F(ref['exact_trial_scale']);e0round=[]
        for v in ref['retained_low_residual_certificate']:
            n=v['degree'];e0round.append(up(orig.mass(n)*(H[n]+sh)*F(v['source_and_center_rounding_radius'])**2))
        for v in oldhigh['residual_physical_numerator_intervals_65_through_2048']:
            n=v['degree'];values=[scale*F(v[k])/(H[n]+s) for k in ['lower','upper'] for s in [sl,sh]];l,r=min(values),max(values);c=down((l+r)/2);rad=up(max(c-l,r-c));w=F(1) if n<first else down(1-lam/down(H[n]+sl));e0round.append(up(orig.mass(n)*(H[n]+sh)*rad*rad/w))
        if reverse:e0round.reverse()
        eps0=up(root(up(sum(e0round,F(0))))+root(up(F(ref['remaining_global_D_fault_norm_upper'])**2/mu)))
        eps=[eps0]+[root(up(F(a['global_D_fault_norm_upper'])**2/mu)) for a in old['actual_polynomial_action_certificates']]
        rounding=[F(r['source_rounding_weighted_inverse_energy_upper']) for r in old['response_trials']]
        fine=[[5*sum((eps[k]**2*Y[k][i]*Y[k][j] for k in range(4)),F(0))+(15*rounding[i] if i==j else F(0)) for j in range(3)] for i in range(3)]
        endpoints=[sum(a,F(0)) for a in trialvectors]
        jumpfactor=up(F(universal[base]['complete_universal_jump_physical_tail_upper'])/(H[tailfirst]+sl)/tailweight)
        jumpcov=[[jumpfactor*endpoints[i]*endpoints[j] for j in range(3)] for i in range(3)]
        derivativegram=[[B*sum((u*v*min(n,d)*(min(n,d)+1) for n,u in enumerate(trialvectors[i]) for d,v in enumerate(trialvectors[j]) if (n-d)%2==0),F(0)) for j in range(3)] for i in range(3)]
        assert p.psd(derivativegram)
        derivativefactor=up(modelnorm**2/F(tailfirst*(tailfirst+1))/(H[tailfirst]+sl)/tailweight)
        continuouscov=p.scale(derivativefactor,derivativegram)
        endpointcov=[[3*endpointtails[i] if i==j else F(0) for j in range(3)] for i in range(3)]
        Sgram=[[F(v) for v in row] for row in old['finite_residual_Gram_Loewner_upper']];centers=[[(F(l),F(r)) for l,r in row] for row in old['variational_response_center_intervals']];mid=[[(l+r)/2 for l,r in row] for row in centers];radius=F(old['center_interval_Loewner_radius'])
        choices=[]
        for eta in [F(1,10),F(1,3),F(1),F(3),F(10)]:
          remainder=p.add(p.scale(F(11,10),continuouscov),p.scale(F(11),endpointcov))
          tailcov=p.add(p.scale(1+eta,jumpcov),p.scale(1+1/eta,remainder))
          for zeta in [F(1,100),F(1,10),F(1)]:
            noise=p.add(p.scale(1+zeta,tailcov),p.scale(1+1/zeta,fine))
            for k in range(1,101):
                theta=F(k,100);paid=p.add(p.scale(1+theta,Sgram),p.scale(1+1/theta,noise));gate=[[F(i==j)*orig.mass(base+2*i)-lam*(mid[i][j]+paid[i][j]+(radius if i==j else F(0))) for j in range(3)] for i in range(3)]
                for subset in [[0],[0,1],[0,2],[0,1,2]]:
                    small=[[gate[i][j] for j in subset] for i in subset]
                    if p.psd(small) and p.inv(small):
                        inverse=p.inv(small);floor=down(1/sum((inverse[i][i] for i in range(len(subset))),F(0)))
                        assert floor>0 and p.psd(p.add(small,p.scale(floor,[[F(i==j) for j in subset] for i in subset]),-1))
                        choices.append((len(subset),floor,zeta,theta,eta,subset,noise,paid,gate,tailcov))
        assert choices
        count,floor,zeta,theta,eta,subset,noise,paid,gate,tailcov=max(choices,key=lambda v:(v[0],v[1],-v[2],-v[3],-v[4]))
        rows.append(dict(parity=old['parity'],combined_trial_tail_certificates=trialproof,rank_one_universal_jump_covariance=p.ser(jumpcov),exact_input_derivative_Gram=p.ser(derivativegram),continuous_prime_remainder_covariance=p.ser(continuouscov),endpoint_tail_covariance=p.ser(endpointcov),global_and_finite_fault_covariance=p.ser(fine),supported_combined_tail_covariance=p.ser(tailcov),selected_jump_continuous_Young_parameter=str(eta),fixed_continuous_endpoint_Young_parameter='1/10',selected_tail_fault_Young_parameter=str(zeta),selected_finite_noise_Young_parameter=str(theta),new_complete_noise_covariance=p.ser(noise),old_complete_noise_covariance=old['complete_noise_Gram_Loewner_upper'],complete_inverse_residual_covariance_upper=p.ser(paid),actual_native_gate_Loewner_lower=p.ser(gate),positive_block_degrees=[base+2*i for i in subset],positive_block_dimension=count,positive_block_native_floor_lower=str(floor),full_three_mode_positive_certified=count==3,remaining_auxiliary_dimension=ref['reference_rank']-count,old_positive_block_degrees=old['positive_block_degrees']))
        print('RC280 '+old['parity']+': positive block '+str([base+2*i for i in subset])+'; floor '+str(float(floor)),flush=True)
    count=sum(r['positive_block_dimension'] for r in rows);assert count>=prior['positive_auxiliary_block_dimension']
    return dict(milestone='RC280',starting_commit='c895261129ffbaae169508c06f8b243421340906',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,rational_prime_model_weighted_Schur_certificate=modelproof,paired_step_tail_certificates=steps,universal_prime_jump_tail_certificates=universal,combined_jump_tail_gate_certificates=rows,exact_controls=controls(),reference_rank_unchanged=371,positive_auxiliary_block_dimension=count,remaining_exact_Schur_dimension=371-count,full_six_mode_positive_certified=count==6,all_actual_prime_model_faults_preserved=True,all_infinite_output_tails_paid=True,new_finite_original_actions_performed=False,finite_trial_response_centers_and_residual_Gram_unchanged=True,new_block_to_remaining_cross_columns_paid=False,original_nonpositive_count_upper_preserved=301,original_at_or_below_one_hundredth_count_upper_preserved=371,original_below_one_hundredth_count_lower_preserved=10,positive_block_not_subtracted_from_independent_index_bounds=True,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC281: pay the enlarged positive block cross columns and certify its remaining principal Schur response; retain the combined prime-jump tail covariance')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
    if args.replay:assert result==json.loads(args.output.read_text())
    else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC280 VALIDATED: combined infinite jump tails and paid joint response gates; full Schur gate open',flush=True)
