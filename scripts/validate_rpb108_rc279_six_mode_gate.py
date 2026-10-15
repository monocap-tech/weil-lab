"""RC279: resolve secondary prime output and certify a coupled six-mode gate."""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json
import validate_rpb108_rc278_smaller_positive_reference as parent
import validate_rpb108_rc273_projection_original_tail as high
import validate_rpb108_rc268_two_pivot_schur_reduction as signed
ROOT=parent.ROOT; up=parent.up; down=parent.down; root=parent.root
orig=parent.orig; p=parent.p; B=parent.B
PINS=dict(parent.PINS); HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc278_smaller_positive_reference.json':'edc59d6cec516d597c2c7816bec2a38a2677e18d','notes/RPB108_RC278_SMALLER_POSITIVE_REFERENCE_20261014.md':'e3f6084063628aa843f89cd2d838d2d1ed7aedcd'})
HELPER_PINS['scripts/validate_rpb108_rc278_smaller_positive_reference.py']='00c2f7e305e5908f2a0c7aac931c814c59184f58'

def bilinear(A,u,v):
    lo=hi=F(0)
    for i in range(len(u)):
        for j in range(len(v)):
            a,b=A[i][j];w=u[i]*v[j];lo+=min(w*a,w*b);hi+=max(w*a,w*b)
    return down(lo),up(hi)

def secondary_action(degree,old,arithmetic,sl,sh,H,reverse):
    base=degree%2;a=[F(n==degree) for n in range(degree+1)]
    coeff,ptail,pfault,proof=high.prime_output(a,base,arithmetic,reverse)
    lookup={v['degree']:v for v in coeff}
    low=old.get('finite_original_D_action',old.get('finite_complete_original_D_action'))
    out=[dict(degree=v['degree'],coefficient=v['coefficient']) for v in low]
    rounding=[]
    for n in range(len(low),2049):
        if n%2!=base:
            out.append(dict(degree=n,coefficient='0'));continue
        h,hr=high.native.endpoint(a,n,F(0),F(0));assert hr==0
        lo=h+F(lookup[n]['lower']);hi=h+F(lookup[n]['upper'])
        values=[q/(H[n]+s) for q in [lo,hi] for s in [sl,sh]]
        l,r=min(values),max(values);c=down((l+r)/2);rad=up(max(c-l,r-c))
        out.append(dict(degree=n,coefficient=str(c)))
        rounding.append(up(orig.mass(n)*(H[n]+sh)*rad*rad))
    firsttail=2049 if base else 2050
    endpoint,endpointproof=high.endpoint.tail_bound(a,firsttail,sl,H)
    tail=up((root(endpoint)+root(up(ptail/(H[firsttail]+sl))))**2)
    components=old['D_energy_component_squared_errors']
    # The old center is retained in full. Its old omitted endpoint and prime
    # errors are replaced by explicit high output plus a new supported tail.
    nuisance=sum((root(F(components[k])) for k in ['finite_rounding','regular_kernel','prime_arithmetic','pole_Taylor','regular_omitted_output']),F(0))
    nuisance=up(nuisance+root(up(pfault*pfault/sl))+root(up(sum(rounding,F(0)))))
    print('RC279 P'+str(degree)+': actual original output through 2048 resolved',flush=True)
    return dict(source='P'+str(degree),input_degree=degree,retained_old_center_length=len(low),finite_original_D_action=out,global_D_fault_norm_upper=str(nuisance),model_D_energy_beyond_2048_upper=str(tail),prime_projection_certificate=proof,endpoint_tail_certificate=endpointproof,regular_omitted_output_paid_globally=True)

def controls():
    # Correlated residuals permit diagonal payment only with weights summing 1.
    E=[[F(1),F(2),F(-1)],[F(3),F(-1),F(2)]];gram=p.mm(p.trans(E),E)
    tau=[F(1,2),F(1,3),F(1,6)]
    bound=[[gram[i][i]/tau[i] if i==j else F(0) for j in range(3)] for i in range(3)]
    assert p.psd(p.add(bound,gram,-1))
    assert not p.psd(p.add([[gram[i][i] if i==j else F(0) for j in range(3)] for i in range(3)],gram,-1))
    V=[[F(1,3),F(-2),F(1)],[F(2),F(1,7),F(3)]]
    actual=p.mm(p.trans(p.add(E,V)),p.add(E,V))
    for theta in [F(1,10),F(1),F(2)]:
        paid=p.add(p.scale(1+theta,gram),p.scale(1+1/theta,p.mm(p.trans(V),V)))
        assert p.psd(p.add(paid,actual,-1))
    return dict(correlated_residual_covariance_diagonal_payment_checked=True,unweighted_diagonal_covariance_rejected=True,full_matrix_Young_covariance_payment_checked=True)

def run(reverse=False):
    data={}
    for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
        raw=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==sha,(path,'pin')
        if path.endswith('.json'):data[path]=json.loads(raw)
    get=lambda s:data['certificates/rpb108_rc'+s+'.json']
    metric=get('129_four_vector_joint_moment');sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);sm=(sl+sh)/2
    H=[F(0)]
    for n in range(1,2051):H.append(H[-1]+F(1,n))
    rows=[]
    for base,ref in enumerate(get('278_smaller_positive_reference')['smaller_reference_certificates']):
        lam=F(ref['augmentation_coefficient']);mu=F(ref['full_D_reference_floor_lower']);first=ref['first_omitted_degree']
        second=get('237_two_trial_signed_response')['parity_two_trial_signed_response_certificates'][base]['new_complete_original_action']
        third=get('240_three_trial_signed_response')['parity_three_trial_signed_response_certificates'][base]['new_complete_original_action']
        oldsource=get('272_projection_source_responses')['projection_source_response_certificates'][base]
        firstaction=get('245_source_refined_response')['parity_source_refined_response_certificates'][base]['refined_complete_original_source_action']
        actions=[secondary_action(base,firstaction,get('43_native_prime_head'),sl,sh,H,reverse),secondary_action(base+2,second,get('43_native_prime_head'),sl,sh,H,reverse),secondary_action(base+4,third,get('43_native_prime_head'),sl,sh,H,reverse)]
        oldR=list(map(F,get('242_residual_original_actions')['parity_residual_original_action_certificates'][base]['exact_input_Legendre_coefficients']))
        V=[[F(n==base+2*j) for n in range(65)] for j in range(3)]+[oldR]
        oldforms=get('247_materialized_four_trial_response')['parity_materialized_four_trial_response_certificates'][base]['original_trial_form_intervals']
        G4=[]
        for i,row in enumerate(oldforms):
            G4.append([])
            for j,(l,r) in enumerate(row):
                mass=sum((orig.mass(n)*V[i][n]*V[j][n] for n in range(65)),F(0))
                G4[-1].append((F(l)+lam*mass,F(r)+lam*mass))
        firstcoeff=[F(ref['exact_trial_scale'])*F(v) for v in oldsource['exact_trial_coefficients']]
        basis=[firstcoeff,[F(1),F(0),F(0),F(0)],[F(0),F(1),F(0),F(0)],[F(0),F(0),F(1),F(0)]]
        G=[[bilinear(G4,u,v) for v in basis] for u in basis]
        mid=[[(l+r)/2 for l,r in row] for row in G]
        Z0=list(map(F,ref['exact_trial_Legendre_coefficients']))
        sourcepair=[[orig.mass(base+2*j)*(Z0[base+2*j] if k==0 else F(k-1==j)) for j in range(3)] for k in range(4)]
        Y=[[down(v) for v in row] for row in p.mm(p.inv(mid),sourcepair)]
        corrections=[];response_trials=[]
        O=[[F(v['coefficient']) for v in a['finite_original_D_action']] for a in actions]
        e0=[F(0)]*2049;e0rad=[F(0)]*2049
        for v in ref['retained_low_residual_certificate']:
            e0[v['degree']]=F(v['residual_center']);e0rad[v['degree']]=F(v['source_and_center_rounding_radius'])
        oldhigh=get('274_mixed_diagonal_inverse')['projection_mixed_inverse_response_certificates'][base]
        scale=F(ref['exact_trial_scale'])
        for v in oldhigh['residual_physical_numerator_intervals_65_through_2048']:
            n=v['degree'];values=[scale*F(v[k])/(H[n]+s) for k in ['lower','upper'] for s in [sl,sh]]
            l,r=min(values),max(values);e0[n]=down((l+r)/2);e0rad[n]=up(max(e0[n]-l,r-e0[n]))
        weights=[F(1) if n<first else down(1-lam/down(H[n]+sl)) for n in range(2049)]
        e0round=up(sum((up(orig.mass(n)*(H[n]+sh)*e0rad[n]**2/weights[n]) for n in range(2049)),F(0)))
        tailweight=down(1-lam/down(H[2049 if base else 2050]+sl))
        eps0=up(root(up(scale*scale*F(oldhigh['complete_full_trial_model_tail_D_energy_upper'])/tailweight))+root(up(F(ref['remaining_global_D_fault_norm_upper'])**2/mu))+root(e0round))
        eps=[eps0]+[up(root(up(F(act['model_D_energy_beyond_2048_upper'])/tailweight))+root(up(F(act['global_D_fault_norm_upper'])**2/mu))) for act in actions]
        model_columns=[];source_rounding=[]
        for j in range(3):
            a,b,c,d=[Y[k][j] for k in range(4)];energy=[];rounding=[];model=[]
            for n in range(2049):
                num=F(n==base+2*j)-a*F(n==base)-lam*(b*F(n==base)+c*F(n==base+2)+d*F(n==base+4))
                center=a*e0[n]+num/(H[n]+sm)-b*O[0][n]-c*O[1][n]-d*O[2][n]
                rad=max(abs(num/(H[n]+sl)-num/(H[n]+sm)),abs(num/(H[n]+sh)-num/(H[n]+sm)))
                w=F(1) if n<first else down(1-lam/down(H[n]+sl));assert w>=mu
                energy.append(up(orig.mass(n)*(H[n]+sh)*center*center/w))
                rounding.append(up(orig.mass(n)*(H[n]+sh)*rad*rad/w))
                model.append(center)
            if reverse:energy.reverse();rounding.reverse()
            roundcost=up(sum(rounding,F(0)));source_rounding.append(roundcost);model_columns.append(model)
            correction=up((root(up(sum(energy,F(0))))+root(roundcost)+sum((abs(Y[k][j])*eps[k] for k in range(4)),F(0)))**2)
            corrections.append(correction)
            response_trials.append(dict(source='P'+str(base+2*j),exact_basis_coefficients=list(map(str,[a,b,c,d])),finite_model_weighted_inverse_energy_upper=str(up(sum(energy,F(0)))),source_rounding_weighted_inverse_energy_upper=str(roundcost),complete_added_inverse_covariance_diagonal_upper=str(correction)))
        gram=[]
        for i in range(3):
            gram.append([])
            for j in range(3):
                terms=[orig.mass(n)*(H[n]+sh)*model_columns[i][n]*model_columns[j][n]/weights[n] for n in range(2049)]
                if reverse:terms.reverse()
                gram[-1].append((sum((down(x) for x in terms),F(0)),sum((up(x) for x in terms),F(0))))
        gram_mid=[[(l+r)/2 for l,r in row] for row in gram]
        gram_rad=up(max(sum(((r-l)/2 for l,r in row),F(0)) for row in gram))
        gram_upper=p.add(gram_mid,p.scale(gram_rad,[[F(i==j) for j in range(3)] for i in range(3)]))
        noise=[[5*sum((eps[k]**2*Y[k][i]*Y[k][j] for k in range(4)),F(0))+(15*source_rounding[i] if i==j else F(0)) for j in range(3)] for i in range(3)]
        centers=[]
        for i in range(3):
            centers.append([])
            for j in range(3):
                u=[Y[k][i] for k in range(4)];v=[Y[k][j] for k in range(4)];l,r=bilinear(G,u,v)
                linear=sum((sourcepair[k][i]*Y[k][j]+Y[k][i]*sourcepair[k][j] for k in range(4)),F(0))
                centers[-1].append((down(linear-r),up(linear-l)))
        midpoint=[[(l+r)/2 for l,r in row] for row in centers]
        radius=up(max(sum(((r-l)/2 for l,r in row),F(0)) for row in centers))
        choices=[];enclosures=[]
        for k in range(1,201):
            theta=F(k,100)
            paid=p.add(p.scale(1+theta,gram_upper),p.scale(1+1/theta,noise))
            gate=[[F(i==j)*orig.mass(base+2*i)-lam*(midpoint[i][j]+paid[i][j]+(radius if i==j else 0)) for j in range(3)] for i in range(3)]
            gersh=down(min(gate[i][i]-sum((abs(gate[i][j]) for j in range(3) if j!=i),F(0)) for i in range(3)))
            enclosures.append((gersh,k,theta,paid,gate))
            # Certify a joint block containing the old source, not unrelated
            # positive diagonal entries. Every chosen restriction is exact.
            for subset in [[0],[0,1],[0,2],[0,1,2]]:
                small=[[gate[i][j] for j in subset] for i in subset]
                if p.psd(small) and p.inv(small):
                    inv=p.inv(small);floor=down(1/sum((inv[i][i] for i in range(len(subset))),F(0)))
                    assert floor>0 and p.psd(p.add(small,p.scale(floor,[[F(i==j) for j in subset] for i in subset]),-1))
                    choices.append((len(subset),floor,k,theta,paid,gate,subset))
        assert choices,('even the old source not recertified',base)
        count,floor,k,theta,paid,gate,subset=max(choices,key=lambda v:(v[0],v[1],-v[2]))
        full_floor,_,fulltheta,fullpaid,fullgate=max(enclosures,key=lambda v:(v[0],-v[1]))
        upper=[[F(i==j)*orig.mass(base+2*i)-lam*(midpoint[i][j]-(radius if i==j else 0)) for j in range(3)] for i in range(3)]
        rows.append(dict(parity=ref['parity'],auxiliary_degrees=[base,base+2,base+4],actual_polynomial_action_certificates=actions,trial_basis=['RC278_Z'+str(base),'P'+str(base),'P'+str(base+2),'P'+str(base+4)],trial_basis_form_intervals=[[[str(l),str(r)] for l,r in row] for row in G],actual_source_trial_pairings=p.ser(sourcepair),response_trials=response_trials,variational_response_center_intervals=[[[str(l),str(r)] for l,r in row] for row in centers],center_interval_Loewner_radius=str(radius),residual_covariance_diagonal_upper=list(map(str,corrections)),finite_residual_Gram_Loewner_upper=p.ser(gram_upper),complete_noise_Gram_Loewner_upper=p.ser(noise),selected_block_Young_parameter=str(theta),selected_block_covariance_payment=p.ser(paid),selected_block_full_gate_Loewner_lower=p.ser(gate),positive_block_degrees=[base+2*i for i in subset],positive_block_native_floor_lower=str(floor),positive_block_dimension=count,full_three_mode_joint_positive_certified=count==3,full_three_mode_gate_Loewner_lower=p.ser(fullgate),full_three_mode_gate_Loewner_upper=p.ser(upper),full_three_mode_lower_Young_parameter=str(fulltheta),full_three_mode_lower_Gershgorin_floor=str(full_floor),full_three_mode_lower_inertia=signed.inertia(fullgate),full_three_mode_upper_inertia=signed.inertia(upper),actual_negative_direction_proved=signed.inertia(upper)['negative']>0,remaining_same_parity_auxiliary_dimension=ref['reference_rank']-count))
        print('RC279 '+ref['parity']+': joint positive degrees '+str([base+2*i for i in subset])+'; native floor '+str(float(floor))+'; full lower inertia '+str(signed.inertia(fullgate)),flush=True)
    count=sum(r['positive_block_dimension'] for r in rows)
    return dict(milestone='RC279',starting_commit='0c17460bcf360d02c9007d6b387733c30676adbe',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,coupled_six_mode_gate_certificates=rows,exact_controls=controls(),reference_rank_unchanged=371,positive_auxiliary_block_dimension=count,remaining_exact_Schur_dimension=371-count,actual_original_polynomial_profiles_recomputed=['P0','P2','P4','P1','P3','P5'],new_original_output_cutoff=2048,all_infinite_output_tails_paid=True,joint_residual_covariance_paid=True,inverse_covariance_sign='added',source_trial_reuse_identity='e_j=a_j e_RC278+D^-1(u_j-a_j P_base)-sum_(k=0..2) b_kj N_new P_(base+2k)',full_remaining_principal_response_evaluated=False,new_selected_block_to_remaining_cross_columns_paid=False,old_two_pivot_cross_bound_not_transferred_to_new_block=True,original_nonpositive_count_upper_preserved=301,original_at_or_below_one_hundredth_count_upper_preserved=371,original_below_one_hundredth_count_lower_preserved=10,positive_block_not_subtracted_from_independent_index_bounds=True,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC280: pay the certified enlarged-block cross columns and bound its remaining Schur form; improve the modeled residual for any unresolved three-mode coupling')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
    if args.replay:assert result==json.loads(args.output.read_text())
    else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC279 VALIDATED: paid six-mode response enclosures and exact positive subblocks; full Schur gate open',flush=True)
