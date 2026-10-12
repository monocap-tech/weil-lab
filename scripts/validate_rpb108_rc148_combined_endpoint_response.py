"""RC148: combined narrow-vector endpoint action and scalar inverse response."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import down,up,sqrtup
from validate_rpb108_rc129_four_vector_joint_moment import add,mm,cong
from validate_rpb108_rc147_endpoint_budget import run as rc147_run

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths]
    prior=json.loads(raw[0]);assert prior==rc147_run(paths[1:],replay)
    narrow=json.loads(raw[1]);old=json.loads(raw[2]);frame=json.loads(raw[9]);joint=json.loads(raw[11])
    sign=json.loads(raw[6]);tail=json.loads(raw[5])
    assert [x['milestone'] for x in (prior,narrow,old,frame,joint,sign,tail)]==['RC147','RC146','RC145','RC138','RC136','RC141','RC142']
    def mat(d,k):return [[F(x) for x in row] for row in d[k]]
    S,T=mat(frame,'trial_source_matrix'),mat(frame,'trial_action_approximation_matrix')
    D=mat(old,'trial_source_frame_coefficients');w=[F(x) for x in old['witness_mixture']]
    h=[sum(D[i][k]*w[k] for k in range(5)) for i in range(5)]
    def col(M,v):return [sum(M[i][j]*v[j] for j in range(len(v))) for i in range(len(M))]
    s,q,t=col(S,w),col(S,h),col(T,h)
    GL,GU=mat(joint,'actual_D_Gram_entry_lower'),mat(joint,'actual_D_Gram_entry_upper')
    GLo,GHi=mat(joint,'actual_D_Gram_Loewner_lower'),mat(joint,'actual_D_Gram_Loewner_upper')
    HL,HU=mat(frame,'trial_frame_endpoint_entry_lower'),mat(frame,'trial_frame_endpoint_entry_upper')
    HL[3][3]=F(sign['new_common_endpoint_energy_lower']);HU[3][3]=F(tail['new_common_endpoint_energy_upper'])
    pairs=[(i,j) for i in range(7) for j in range(7)]
    hpairs=[(i,j) for i in range(5) for j in range(5)]
    if replay:pairs.reverse();hpairs.reverse()
    def interval(x,y):
        lo=hi=F(0)
        for i,j in pairs:
            c=x[i]*y[j]
            lo+=c*(GL[i][j] if c>=0 else GU[i][j])
            hi+=c*(GU[i][j] if c>=0 else GL[i][j])
        return lo,hi
    def energy(x,M):return cong([[v] for v in x],M)[0][0]
    qNorm=sqrtup(energy(q,GHi))
    eps=[F(x) for x in frame['trial_action_D_norm_error_upper']]
    actionErrorNorm=sum(abs(h[i])*eps[i] for i in range(5))
    pairLo,pairHi=interval(t,q)
    actionHL=down(pairLo-actionErrorNorm*qNorm)
    actionHU=up(pairHi+actionErrorNorm*qNorm)
    # Independent endpoint entry intervals are intersected with the combined action
    # identity and 0 <= C <= I. The last bound uses actual q Gram upper.
    entryHL=entryHU=F(0)
    for i,j in hpairs:
        c=h[i]*h[j]
        entryHL+=c*(HL[i][j] if c>=0 else HU[i][j])
        entryHU+=c*(HU[i][j] if c>=0 else HL[i][j])
    hLo=max(entryHL,actionHL,F(0));hHi=min(entryHU,actionHU,energy(q,GHi))
    assert 0<hLo<=hHi
    # Aggregate signed coefficients before using any uncertain Gram entries.
    gLo=gHi=F(0)
    for i,j in pairs:
        c=s[i]*q[j]+q[i]*s[j]-q[i]*q[j]
        gLo+=c*(GL[i][j] if c>=0 else GU[i][j])
        gHi+=c*(GU[i][j] if c>=0 else GL[i][j])
    residual=[q[i]+t[i]-s[i] for i in range(7)]
    nominal=sqrtup(energy(residual,GHi))
    residualUpper=up((nominal+actionErrorNorm)**2)
    trialLo=down(gLo-hHi);trialHi=up(gHi-hLo+residualUpper)
    sourceLo=energy(s,GLo);sourceHi=energy(s,GHi)
    # The operator inequality I <= I+C <= 2I intersects the trial interval.
    responseLo=max(trialLo,sourceLo/2);responseHi=min(trialHi,sourceHi)
    width=responseHi-responseLo
    assert 0<responseLo<=responseHi and 0<sourceLo<=sourceHi
    assert width<sourceLo/2
    assert hHi-hLo<F(prior['signed_endpoint_interval_width_upper'])/4
    assert residualUpper<F(narrow['transformed_full_residual_Gram_upper'][4][4])
    # Signed scalar controls for both the endpoint identity and variational residual.
    controls=[]
    for lam in (F(0),F(1,3),F(1)):
        src=F(2,3);trial=F(1,4)
        rr=((1+lam)*trial-src)**2
        exact=src*src/(1+lam)
        L=2*src*trial-(1+lam)*trial*trial
        assert L<=exact<=L+rr
        controls.append(dict(C_eigenvalue=str(lam),variational_residual_identity_verified=True,
                             endpoint_contraction_verified=0<=lam*trial*trial<=trial*trial))
    return dict(milestone='RC148',status='PASS: combined endpoint action yields narrow-source scalar response width below half Gram',
        starting_commit='d01fb439f64115b55440c38752da58d4f93cba60',
        input_sha256=[hashlib.sha256(b).hexdigest() for b in raw],aperture='11/10',
        carrier_family_dimension=7,response_source_count=5,
        witness_mixture=list(map(str,w)),combined_frame_coefficients=list(map(str,h)),
        combined_trial_source_seven_vector=list(map(str,q)),
        combined_action_approximation_seven_vector=list(map(str,t)),
        combined_action_error_D_norm_upper=str(actionErrorNorm),
        combined_trial_D_norm_upper=str(qNorm),
        endpoint_from_action_lower=str(actionHL),endpoint_from_action_upper=str(actionHU),
        endpoint_from_entry_lower=str(entryHL),endpoint_from_entry_upper=str(entryHU),
        combined_endpoint_energy_lower=str(hLo),combined_endpoint_energy_upper=str(hHi),
        nominal_residual_D_norm_upper=str(nominal),full_residual_D_energy_upper=str(residualUpper),
        signed_nonendpoint_variational_lower=str(gLo),signed_nonendpoint_variational_upper=str(gHi),
        trial_reference_response_lower=str(trialLo),trial_reference_response_upper=str(trialHi),
        reference_response_lower=str(responseLo),reference_response_upper=str(responseHi),
        source_energy_lower=str(sourceLo),source_energy_upper=str(sourceHi),
        response_width_upper=str(width),relative_source_Gram_width_upper=str(up(width/sourceLo,10**6)),
        half_Gram_scalar_width_target_met=True,combined_endpoint_action_uses_same_trial_vector=True,
        mixed_action_errors_paid_by_triangle_norm=True,all_five_source_matrix_half_Gram_target_met=False,
        exact_scalar_controls=controls,required_Stage_I_matrix_tolerance_specified=False,
        original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,
        RH=False,F4=False,Lean=False,
        next_cursor='extend combined endpoint identities to the full five-source matrix, with conditioned mixed rows and paid residual correlations')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=16)
    a=p.parse_args();result=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==result
    else:Path(a.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC148 PASS: combined narrow endpoint and scalar response')
