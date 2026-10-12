"""RC155: joint seven-source action-error interface, with signed controls."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import down,up,sqrtup,psd,ser
from validate_rpb108_rc129_four_vector_joint_moment import add,mm,transpose,cong,inv

def run(paths,reverse=False):
    raw=[Path(p).read_bytes() for p in paths]
    coverage,frame,joint,psi,delta=map(json.loads,raw)
    assert [x['milestone'] for x in (coverage,frame,joint,psi,delta)]==['RC150','RC138','RC136','RC154','RC153']
    assert frame['input_sha256'][1]==hashlib.sha256(raw[2]).hexdigest()
    assert coverage['input_sha256'][11]==hashlib.sha256(raw[1]).hexdigest()
    assert coverage['input_sha256'][13]==hashlib.sha256(raw[2]).hexdigest()
    assert psi['input_sha256'][3]==hashlib.sha256(raw[4]).hexdigest()
    assert psi['half_Gram_action_error_envelope_gate_passed']
    mat=lambda d,k:[[F(x) for x in row] for row in d[k]]
    W=mat(coverage,'augmented_source_frame');Wi=mat(coverage,'augmented_frame_inverse')
    assert mm(W,Wi)==[[F(i==j) for j in range(7)] for i in range(7)]
    assert [row[:5] for row in W]==mat(frame,'trial_source_matrix')
    GL,GU=mat(joint,'actual_D_Gram_Loewner_lower'),mat(joint,'actual_D_Gram_Loewner_upper')
    G=cong(W,GL);Gupper=cong(W,GU);assert psd(G)
    eps=list(map(F,frame['trial_action_D_norm_error_upper']))+[F(psi['full_Cpsi_trial_D_norm_error_upper']),F(delta['full_Cdelta_trial_D_norm_error_upper'])]
    K=inv(G)
    # For real c, the column error bounds give ||sum c_i e_i|| <=
    # sum eps_i |c_i| = max_sign (sign*eps)^T c. Each rank-one
    # bound is certified against G. Simultaneous sign reversal leaves
    # its square unchanged, so exactly 64 controls suffice.
    controls=[];signs=[(1,)+s for s in product((-1,1),repeat=6)]
    if reverse:signs.reverse()
    for sign in signs:
        v=[F(sign[i])*eps[i] for i in range(7)]
        q=sum(v[i]*K[i][j]*v[j] for i in range(7) for j in range(7))
        assert q>0
        controls.append(dict(sign=list(sign),relative_rank_one_error_factor=str(q)))
    controls.sort(key=lambda x:x['sign'])
    worst=max(controls,key=lambda x:(F(x['relative_rank_one_error_factor']),x['sign']))
    exact=F(worst['relative_rank_one_error_factor']);beta=up(exact,10**6)
    # Congruence by G^-1 and Cauchy-Schwarz establish beta G-vv^T
    # PSD iff v^T G^-1 v <= beta. Direct exact PSD additionally checks
    # the worst witness and every signed rank-one control.
    for control in controls:
        v=[F(control['sign'][i])*eps[i] for i in range(7)]
        assert psd(add([[beta*x for x in row] for row in G],[[x*y for y in v] for x in v],-1))
    assert beta<F(1,2)
    independent=[[7*eps[i]**2 if i==j else F(0) for j in range(7)] for i in range(7)]
    assert not psd(add([[F(1,2)*x for x in row] for row in G],independent,-1))
    # The actual actions, sources, and trial coefficients are real.
    # The real quadratic estimate extends to complex mixtures by applying
    # it separately to real and imaginary parts; no complex phase enumeration
    # or orthogonality between the seven errors is assumed.
    HLo,HHi=mat(joint,'actual_endpoint_pairing_entry_lower'),mat(joint,'actual_endpoint_pairing_entry_upper')
    cols=transpose(W);pairs=[(a,b) for a in range(7) for b in range(7)]
    if reverse:pairs.reverse()
    HL=[[F(0)]*7 for _ in range(7)];HU=[[F(0)]*7 for _ in range(7)]
    for i in range(7):
        for j in range(i,7):
            lo=hi=F(0)
            for a,b in pairs:
                c=cols[i][a]*cols[j][b]
                lo+=c*(HLo[a][b] if c>=0 else HHi[a][b])
                hi+=c*(HHi[a][b] if c>=0 else HLo[a][b])
            assert lo<=hi
            HL[i][j]=HL[j][i]=down(lo);HU[i][j]=HU[j][i]=up(hi)
    norms=[sqrtup(Gupper[i][i]) for i in range(7)]
    errorSource=[[up(eps[i]*norms[j]) for j in range(7)] for i in range(7)]
    errorError=[[up(eps[i]*eps[j]) for j in range(7)] for i in range(7)]
    QL=[[down(HL[i][j]-errorSource[i][j]) for j in range(7)] for i in range(7)]
    QU=[[up(HU[i][j]+errorSource[i][j]) for j in range(7)] for i in range(7)]
    # Q_ij=<q_i,s_j> need not be symmetric: the true endpoint action
    # pairings are symmetric, but the paid trial-error rows can differ.
    nativeError=[[beta*x for x in row] for row in GL]
    assert cong(W,nativeError)==[[beta*x for x in row] for row in G]
    return dict(milestone='RC155',status='PASS: complete seven-source action-error half-Gram interface',
        starting_commit='b94120e31a5bdff45abbb5c512d0c0ca355267e4',
        input_sha256=[hashlib.sha256(b).hexdigest() for b in raw],aperture='11/10',
        source_frame=['P0','f0','w14-alpha*psi0','(v10+z_b6)/2','t10','psi0','z_b6-v10'],
        source_frame_matrix=ser(W),full_source_Gram_lower=ser(G),
        full_source_Gram_upper=ser(Gupper),action_column_D_norm_error_upper=list(map(str,eps)),
        real_signed_rank_one_control_count=len(controls),signed_rank_one_controls=controls,
        worst_signed_mixture=worst['sign'],exact_joint_error_factor=str(exact),
        full_seven_source_action_error_relative_Gram_upper=str(beta),
        native_carrier_action_error_Gram_Loewner_upper=ser(nativeError),
        all_seven_source_real_and_complex_mixtures_paid=True,
        half_Gram_full_action_error_gate_passed=True,
        generic_sevenfold_diagonal_half_Gram_gate_failed=True,
        mutual_action_error_pairing_absolute_upper=ser(errorError),
        action_error_source_pairing_absolute_upper=ser(errorSource),
        source_endpoint_pairing_entry_lower=ser(HL),source_endpoint_pairing_entry_upper=ser(HU),
        action_trial_source_pairing_entry_lower=ser(QL),action_trial_source_pairing_entry_upper=ser(QU),
        all_49_trial_source_pairings_enclosed=True,
        new_trial_pairings_evaluated_directly_from_coefficients=False,
        trial_pairing_enclosures_use_inherited_endpoint_intervals_and_paid_action_errors=True,
        mixed_action_error_sign_or_orthogonality_assumed=False,
        complex_extension_uses_real_operator_and_real_trials=True,
        seven_source_inverse_response_certified=False,
        inverse_response_half_Gram_width_inferred_from_action_gate=False,
        original_Weil_or_augmented_actions_performed=False,
        whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
        next_cursor='evaluate sharper trial-source and trial-trial pairings directly from the explicit finite and analytic coefficients; assemble a seven-source variational inverse enclosure and certify its width separately')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=5)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC155 PASS: all-seven action-error and mixed pairing interface')
