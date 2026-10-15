"""RC278: a rank-371 positive reference and paid rescaled source responses."""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json
import validate_rpb108_rc277_weighted_prime_schur as parent
import validate_rpb108_rc230_augmentation_range_bridge as bridge
ROOT=parent.ROOT; up=parent.up; down=parent.down; root=parent.parent.root
orig=parent.parent.orig; p=bridge.p; B=F(11,10); SHIFT=F(789,125)
PINS=dict(parent.PINS); HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc277_weighted_prime_schur.json':'7363b4667ebc9272e8c5b929fab8a0400495b6c4','notes/RPB108_RC277_WEIGHTED_PRIME_SCHUR_20261014.md':'5442828a46217fc4998da318f865e6dfce5610ec'})
HELPER_PINS['scripts/validate_rpb108_rc277_weighted_prime_schur.py']='7addcb150f4341f703762fa324a2e8011a3f6b86'

def controls():
    # A full diagonal lower form gives inverse order even when G mixes P,Q.
    W=[[F(4),F(0)],[F(0),F(1,5)]]
    G=p.add(W,[[F(1),F(1,2)],[F(1,2),F(1,4)]])
    assert p.psd(p.add(G,W,-1)) and p.psd(p.add(p.inv(W),p.inv(G),-1))
    for t in [F(1,2),F(2),F(7,3)]:
        u=[[F(1)],[F(0)]]; z=[[F(1,7)],[F(-1,9)]]; tz=p.scale(t,z)
        e=p.add(u,p.mm(G,tz),-1)
        center=2*p.mm(p.trans(u),tz)[0][0]-p.mm(p.trans(tz),p.mm(G,tz))[0][0]
        correction=p.mm(p.trans(e),p.mm(p.inv(G),e))[0][0]
        assert center+correction==p.mm(p.trans(u),p.mm(p.inv(G),u))[0][0]
        paid=p.mm(p.trans(e),p.mm(p.inv(W),e))[0][0]
        assert correction<=paid
    # Rescaling for a changed augmentation does not preserve old residuals.
    old=F(5); new=F(3); d=F(7); t=F(2); z=F(1,9); source=F(1)
    action=F(4,11); olde=(source-old*z)/d-action
    actual=(source-t*new*z)/d-t*action
    assert actual==t*olde+((1-t)*source+t*(old-new)*z)/d
    assert actual!=t*olde
    return dict(noncommuting_full_diagonal_inverse_order_checked=True,rescaled_variational_center_plus_added_covariance_checked=True,changed_reference_residual_update_checked=True)

def run(reverse=False):
    data={}
    for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
        raw=(ROOT/path).read_bytes()
        assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==sha,(path,'pin')
        if path.endswith('.json'):data[path]=json.loads(raw)
    get=lambda s:data['certificates/rpb108_rc'+s+'.json']
    previous=get('277_weighted_prime_schur');metric=get('129_four_vector_joint_moment')
    sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);sm=(sl+sh)/2
    harmonics=[F(0)]
    for n in range(1,2051):harmonics.append(harmonics[-1]+F(1,n))
    dlo=[down(h+sl) for h in harmonics];dhi=[up(h+sh) for h in harmonics]
    prime=F(previous['actual_prime_weighted_Schur_certificate']['operator_norm_upper']);regular=F(previous['regular_operator_norm_upper'])
    oldrefs=get('271_diagonal_projection_reference')['projection_reference_models'][0]
    rows=[]
    for base,r in enumerate(previous['original_diagonal_index_certificates'][1]['parity_certificates']):
        C=F(r['physical_negative_allowance_C']);lam=C;first=r['first_omitted_Legendre_degree'];degrees=r['retained_Legendre_degrees']
        assert degrees==list(range(base,first,2)) and len(degrees)==[142,229][base]
        mu=down(1-C/dlo[first]);eta=down(mu/2);assert mu>F(1,50) and eta>F(1,100)
        positivepole=2*F(get('42_native_signed_pole_head')['cosh_physical_norm_squared_upper']) if base==0 else F(0)
        upperconstant=regular+prime+positivepole+lam-SHIFT
        nu=up(2+max(F(0),upperconstant)/sl);assert 0<mu<nu
        budgets=bridge.polynomial_budgets(mu,nu,up(1/sl),lam)
        s=get('272_projection_source_responses')['projection_source_response_certificates'][base]
        high=get('274_mixed_diagonal_inverse')['projection_mixed_inverse_response_certificates'][base]
        old=get('275_canonical_shift_inverse')['canonical_shift_response_certificates'][base]
        oldcross=get('276_projection_cross_columns')['projection_cross_column_certificates'][base]
        oldlam=F(oldrefs['parity_projection_reference_certificates'][base]['new_exact_projection_augmentation_coefficient'])
        z=list(map(F,s['exact_trial_Legendre_coefficients']));assert len(z)==65 and all(not zn or n in degrees for n,zn in enumerate(z))
        linear=orig.mass(base)*z[base]
        change=(oldlam-lam)*sum((orig.mass(n)*zn*zn for n,zn in enumerate(z)),F(0))
        qlo=down(2*linear-F(s['variational_inverse_center_upper'])-change)
        qhi=up(2*linear-F(s['variational_inverse_center_lower'])-change)
        assert 0<qlo<=qhi
        t=down(linear/((qlo+qhi)/2));assert t>0
        centerlo=down(2*t*linear-t*t*qhi);centerhi=up(2*t*linear-t*t*qlo)
        # e_new=t e_old+D^-1[(1-t)u+t(lambda_old-lambda_new)Z].
        # The D-inverse source radius is recomputed for u-t lambda_new Z.
        low=[];energy=[];rounding=[]
        for n,a in enumerate(s['retained_actual_residual_center'][:65]):
            dm=harmonics[n]+sm
            c=down(t*F(a['coefficient'])+((1-t)*F(n==base)+t*(oldlam-lam)*z[n])/dm)
            # Center rounding is also paid as a D-energy fault.
            exact=t*F(a['coefficient'])+((1-t)*F(n==base)+t*(oldlam-lam)*z[n])/dm
            numerator=F(n==base)-t*lam*z[n]
            rad=up(max(abs(numerator/(harmonics[n]+sl)-numerator/dm),abs(numerator/(harmonics[n]+sh)-numerator/dm))+abs(exact-c))
            assert n<first
            energy.append(up(orig.mass(n)*dhi[n]*c*c))
            rounding.append(up(orig.mass(n)*dhi[n]*rad*rad))
            low.append(dict(degree=n,residual_center=str(c),source_and_center_rounding_radius=str(rad)))
        for a in high['residual_physical_numerator_intervals_65_through_2048']:
            n=a['degree'];v=max(abs(F(a['lower'])),abs(F(a['upper'])))
            weight=F(1) if n<first else down(1-C/dlo[n]);assert weight>=mu
            energy.append(up(t*t*orig.mass(n)*v*v/dlo[n]/weight))
        firsttail=2050 if base==0 else 2049
        tailweight=down(1-C/dlo[firsttail]);assert tailweight>mu
        tail=up(t*t*F(high['complete_full_trial_model_tail_D_energy_upper'])/tailweight)
        if reverse:energy.reverse();rounding.reverse()
        model=up(sum(energy,F(0))+tail);roundcost=up(sum(rounding,F(0)))
        faultnorm=up(t*F(high['new_complete_global_D_fault_norm_upper']));fault=up(faultnorm*faultnorm/mu)
        correction=up((root(model)+root(roundcost)+root(fault))**2)
        lower=centerlo;upper=up(centerhi+correction);assert 0<lower<=upper
        mass=orig.mass(base);pivot=down(mass-lam*upper);pivothi=up(mass-lam*lower);assert 0<pivot<=pivothi
        remaining=degrees[1:];Z=[t*zn for zn in z]
        # G_new>=D_P+(D-C)_Q>=d_base P. Full cross covariance
        # follows from this projection coercivity and the complete residual.
        kappa=dlo[base];radius2=up(lam*lam*correction/kappa)
        dual=up(sum((lam*lam*orig.mass(n)*Z[n]*Z[n] for n in remaining if n<65),F(0)))
        weighted=up(radius2/pivot);payment=up((root(dual)+root(radius2))**2/pivot)
        assert mu>F(old['fresh_all_source_N_D_floor_lower']) and nu<F(old['unchanged_all_source_N_D_upper'])
        assert payment<F(oldcross['complete_actual_cross_payment_native_mass_operator_norm_upper'])
        rows.append(dict(parity=r['parity'],reference_rank=len(degrees),retained_Legendre_degrees=degrees,first_omitted_degree=first,augmentation_coefficient=str(lam),physical_negative_allowance_C=str(C),full_D_reference_floor_lower=str(mu),full_canonical_reference_floor_lower=str(eta),full_D_reference_upper=str(nu),upper_physical_remainder_allowance=str(upperconstant),D_condition_number_upper=str(up(nu/mu)),conditional_exact_action_inverse_budgets=budgets,old_all_source_D_floor=old['fresh_all_source_N_D_floor_lower'],old_all_source_D_upper=old['unchanged_all_source_N_D_upper'],old_conditional_exact_action_inverse_budgets=old['conditional_exact_action_inverse_budgets'],source='P'+str(base),trial_is_rational_rescaling_of_RC272=True,exact_trial_scale=str(t),exact_trial_Legendre_coefficients=list(map(str,Z)),changed_augmentation_trial_form_lower=str(qlo),changed_augmentation_trial_form_upper=str(qhi),variational_inverse_center_lower=str(centerlo),variational_inverse_center_upper=str(centerhi),retained_low_residual_certificate=low,complete_model_weighted_inverse_energy_upper=str(model),weighted_source_and_center_rounding_energy_upper=str(roundcost),remaining_global_D_fault_norm_upper=str(faultnorm),remaining_global_fault_weighted_inverse_energy_upper=str(fault),complete_added_inverse_residual_correction_upper=str(correction),actual_source_inverse_response_lower=str(lower),actual_source_inverse_response_upper=str(upper),native_auxiliary_source_mass=str(mass),native_auxiliary_pivot_lower=str(pivot),native_auxiliary_pivot_upper=str(pivothi),normalized_auxiliary_pivot_lower=str(down(pivot/mass)),native_projection_coercivity_lower=str(kappa),remaining_auxiliary_degrees=remaining,remaining_auxiliary_dimension=len(remaining),cross_center_formula='-lambda mass_j Z_j on same parity; zero on opposite parity',cross_center_dual_mass_squared_upper=str(dual),complete_cross_error_dual_mass_squared_upper=str(radius2),weighted_cross_error_covariance_mass_coefficient_upper=str(weighted),complete_cross_payment_mass_norm_upper=str(payment),old_complete_cross_payment_mass_norm_upper=oldcross['complete_actual_cross_payment_native_mass_operator_norm_upper'],old_positive_pivot_not_transferred=True,new_positive_pivot_certified=True))
        print('RC278 '+r['parity']+': rank '+str(len(degrees))+'; D floor '+str(float(mu))+'; new pivot '+str(float(pivot))+'; inverse degrees '+str([v['residual_polynomial_degree'] for v in budgets]),flush=True)
    assert sum(r['reference_rank'] for r in rows)==371
    assert sum(r['remaining_auxiliary_dimension'] for r in rows)==369
    return dict(milestone='RC278',starting_commit='bf38411bc8696b55901ea6ddab301e1009760c05',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,smaller_reference_certificates=rows,exact_controls=controls(),new_reference_rank=371,new_reference_formula='G_new=G0+C_b P_b; P_b physical Legendre projection of rank 142 even or 229 odd',global_lower_form='G_new>=D_P+(D-C_b)_Q',global_upper_form='G_new<=2D+(regular+prime+positive_pole+C_b-789/125) I_physical',canonical_metric_bounds_used='L<=2D; h<=D; I_physical<=D/s_lower',response_gate_formula='Mass-C_b T; T_ij=<P_i,N_new^-1 D^-1 P_j>_physical',complete_residual_identity='e_new=t e_old+D^-1[(1-t)u+t(lambda_old-C_b)Z_old]',remaining_exact_Schur_dimension=369,new_positive_auxiliary_source_count=2,full_remaining_principal_response_evaluated=False,cross_covariance_contract='C* Gamma^-1 C <= (1+theta) Chat* Gamma_lo^-1 Chat +(1+1/theta) direct_sum[(radius_squared/Gamma_lo) Mass]',inverse_correction_sign='added',new_global_original_Weil_actions_performed=False,old_actual_2048_output_and_infinite_tail_reused_with_exact_rescaling=True,conditional_polynomial_inverse_actions_performed=False,original_nonpositive_count_upper_preserved=301,original_at_or_below_one_hundredth_count_upper_preserved=371,original_below_one_hundredth_count_lower_preserved=10,positive_pivots_not_subtracted_from_independent_index_bounds=True,legacy_rank_639_and_rank_608_references_preserved=True,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC279: bound the remaining rank-371 reference principal response, or execute paid polynomial inverse actions using the improved full-source spectral interval; retain joint cross covariance in the 369-dimensional Schur gate')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
    if args.replay:assert result==json.loads(args.output.read_text())
    else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC278 VALIDATED: smaller positive reference and two paid new pivots; full Schur gate open',flush=True)
