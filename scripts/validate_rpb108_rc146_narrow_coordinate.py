"""RC146: evaluate signed endpoint and Gram intervals in the narrow fifth coordinate."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc129_four_vector_joint_moment import add,mm,transpose,cong,inv
from validate_rpb108_rc145_fifth_source_conditioning import run as rc145_run

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths]
    prior=json.loads(raw[0]);assert prior==rc145_run(paths[1:],replay)
    frame=json.loads(raw[7]);joint=json.loads(raw[9]);sign=json.loads(raw[4]);tail=json.loads(raw[3])
    assert [x['milestone'] for x in (prior,frame,joint,sign,tail)]==['RC145','RC138','RC136','RC141','RC142']
    def mat(d,key):return [[F(x) for x in row] for row in d[key]]
    GL,GU=mat(joint,'actual_D_Gram_entry_lower'),mat(joint,'actual_D_Gram_entry_upper')
    GLo,GHi=mat(joint,'actual_D_Gram_Loewner_lower'),mat(joint,'actual_D_Gram_Loewner_upper')
    S=mat(frame,'trial_source_matrix');T=mat(frame,'trial_action_approximation_matrix')
    D=mat(prior,'trial_source_frame_coefficients');Y=mm(S,D);R=add(mm(add(S,T),D),S,-1)
    eps=[F(x) for x in frame['trial_action_D_norm_error_upper']]
    HL,HU=mat(frame,'trial_frame_endpoint_entry_lower'),mat(frame,'trial_frame_endpoint_entry_upper')
    HL[3][3]=F(sign['new_common_endpoint_energy_lower']);HU[3][3]=F(tail['new_common_endpoint_energy_upper'])
    witness=[F(x) for x in prior['witness_mixture']]
    X=[[F(i==j) if j<4 else witness[i] for j in range(5)] for i in range(5)]
    assert X[4][4]==1 and psd(cong(mm(S,X),GLo))
    SX,YX,DX,RX=mm(S,X),mm(Y,X),mm(D,X),mm(R,X)
    sc,yc,dc=transpose(SX),transpose(YX),transpose(DX)
    pairs=[(a,b) for a in range(7) for b in range(7)]
    hpairs=[(a,b) for a in range(5) for b in range(5)]
    if replay:pairs.reverse();hpairs.reverse()
    LL=[[F(0)]*5 for _ in range(5)];LU=[[F(0)]*5 for _ in range(5)]
    # Signed combination is done after changing coordinates and before interval evaluation.
    for i in range(5):
        for j in range(i,5):
            low=high=F(0)
            for a,b in pairs:
                v=sc[i][a]*yc[j][b]+yc[i][a]*sc[j][b]-yc[i][a]*yc[j][b]
                low+=v*(GL[a][b] if v>=0 else GU[a][b]);high+=v*(GU[a][b] if v>=0 else GL[a][b])
            for a,b in hpairs:
                v=-dc[i][a]*dc[j][b]
                low+=v*(HL[a][b] if v>=0 else HU[a][b]);high+=v*(HU[a][b] if v>=0 else HL[a][b])
            LL[i][j]=LL[j][i]=down(low);LU[i][j]=LU[j][i]=up(high)
    sourceLo,sourceHi=cong(SX,GLo),cong(SX,GHi)
    weights=[sqrtup(sourceHi[i][i]) for i in range(5)]
    LLo,LHi,errs=loewner(LL,LU,weights)
    nominal=cong(RX,GHi)
    minor=cong(DX,[[4*eps[i]**2 if i==j and i<4 else F(0) for j in range(5)] for i in range(5)])
    major=[[eps[4]**2*DX[4][i]*DX[4][j] for j in range(5)] for i in range(5)]
    def width_gate(gap):
        def yes(n):return psd(add([[F(n,10**6)*x for x in row] for row in sourceLo],gap,-1))
        hi=1
        while not yes(hi):hi*=2;assert hi<10**12
        lo=0
        while hi-lo>1:
            mid=(lo+hi)//2
            if yes(mid):hi=mid
            else:lo=mid
        assert yes(hi) and not yes(lo)
        return F(hi,10**6)
    opts=[(F(1,100),F(1,20)),(F(1,10),F(1,20)),(F(1,10),F(1,10)),(F(1,2),F(1,10)),(F(1),F(1))]
    if replay:opts.reverse()
    best=None;candidates=[]
    for tau,gamma in opts:
        err=add([[(1+tau)*x for x in row] for row in major],
                [[(1+1/tau)*x for x in row] for row in minor])
        residual=add([[(1+gamma)*x for x in row] for row in nominal],
                     [[(1+1/gamma)*x for x in row] for row in err])
        gap=add(add(LHi,residual),LLo,-1)
        assert psd(err) and psd(residual) and psd(gap)
        beta=width_gate(gap)
        candidates.append(dict(tau=str(tau),gamma=str(gamma),relative_width_upper=str(beta)))
        if best is None or (beta,tau,gamma)<best[0]:best=((beta,tau,gamma),residual)
    (beta,tau,gamma),residual=best
    candidates.sort(key=lambda x:(F(x['tau']),F(x['gamma'])))
    assert beta<F(prior['relative_source_Gram_matrix_width_upper'])
    gap=add(add(LHi,residual),LLo,-1)
    assert psd(add([[beta*x for x in row] for row in sourceLo],gap,-1))
    Xi=inv(X)
    originalLower=cong(Xi,LLo);originalUpper=cong(Xi,add(LHi,residual))
    assert psd(add([[beta*x for x in row] for row in cong(S,GLo)],
                   add(originalUpper,originalLower,-1),-1))
    narrowSourceLo=sourceLo[4][4];narrowSourceHi=sourceHi[4][4]
    narrowInterval=LHi[4][4]-LLo[4][4];narrowResidual=residual[4][4]
    assert narrowInterval+narrowResidual==gap[4][4]
    assert narrowSourceLo>0 and narrowInterval+narrowResidual>narrowSourceHi/2
    return dict(milestone='RC146',status='PASS: narrow-coordinate signed interval improves paid five-source trial width',
        starting_commit='4886d0de40f93b66fd8ffe20e1105c4876ac98e1',
        input_sha256=[hashlib.sha256(b).hexdigest() for b in raw],aperture='11/10',carrier_family_dimension=7,
        response_source_count=5,original_source_transform=ser(X),
        transformed_source_Gram_lower=ser(sourceLo),transformed_source_Gram_upper=ser(sourceHi),
        transformed_variational_entry_lower=ser(LL),transformed_variational_entry_upper=ser(LU),
        transformed_variational_Loewner_lower=ser(LLo),transformed_variational_Loewner_upper=ser(LHi),
        transformed_interval_error_diagonal=list(map(str,errs)),transformed_full_residual_Gram_upper=ser(residual),
        transformed_response_Loewner_lower=ser(LLo),transformed_response_Loewner_upper=ser(add(LHi,residual)),
        original_source_response_Loewner_lower=ser(originalLower),
        original_source_response_Loewner_upper=ser(originalUpper),
        candidate_widths=candidates,selected_tau=str(tau),selected_gamma=str(gamma),
        relative_source_Gram_matrix_width_upper=str(beta),RC145_width_upper=prior['relative_source_Gram_matrix_width_upper'],
        improvement_factor_lower=str(down(F(prior['relative_source_Gram_matrix_width_upper'])/beta,10**6)),
        narrow_source_energy_lower=str(down(narrowSourceLo,10**18)),narrow_source_energy_upper=str(up(narrowSourceHi,10**18)),
        narrow_variational_interval_width_upper=str(up(narrowInterval,10**18)),
        narrow_residual_width_upper=str(up(narrowResidual,10**18)),
        narrow_total_width_lower=str(down(gap[4][4],10**18)),
        narrow_width_over_source_energy_upper_lower=str(down(gap[4][4]/narrowSourceHi,10**6)),
        half_Gram_width_target_met=False,transformed_variational_lower_psd=psd(LLo),
        structural_positive_response_lower='(1/2) * actual source Gram',
        mixed_action_errors_paid_without_orthogonality=True,required_Stage_I_matrix_tolerance_specified=False,
        original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,
        RH=False,F4=False,Lean=False,
        next_cursor='target t10 endpoint/covariance interval dependence; current narrow-coordinate width still exceeds source energy')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=14)
    a=p.parse_args();result=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==result
    else:Path(a.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC146 PASS: fifth-source narrow-coordinate interval')
