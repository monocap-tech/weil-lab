"""RC145: exact five-source response enclosure and conditioning witness."""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json
from validate_rpb108_rc127_enriched_even_endpoint_action import down, up, sqrtup, psd, ser, loewner
from validate_rpb108_rc129_four_vector_joint_moment import add, mm, transpose, cong, inv
from validate_rpb108_rc144_conditioned_joint_response import run as rc144_run

def run(paths, replay=False):
    raw=[Path(p).read_bytes() for p in paths]
    prior=json.loads(raw[0]); assert prior==rc144_run(paths[1:],replay)
    frame=json.loads(raw[6]);joint=json.loads(raw[8]);sign=json.loads(raw[3]);tail=json.loads(raw[2])
    assert [x['milestone'] for x in (prior,frame,joint,sign,tail)]==['RC144','RC138','RC136','RC141','RC142']
    def matrix(d,key):return [[F(x) for x in row] for row in d[key]]
    GL,GU=matrix(joint,'actual_D_Gram_entry_lower'),matrix(joint,'actual_D_Gram_entry_upper')
    GLo,GHi=matrix(joint,'actual_D_Gram_Loewner_lower'),matrix(joint,'actual_D_Gram_Loewner_upper')
    GM=[[(GL[i][j]+GU[i][j])/2 for j in range(7)] for i in range(7)]
    S,T=matrix(frame,'trial_source_matrix'),matrix(frame,'trial_action_approximation_matrix')
    K=add(S,T);Q=cong(K,GM);assert psd(Q)
    D=[[down(x,10**20) for x in row] for row in mm(inv(Q),mm(transpose(K),mm(GM,S)))]
    Y=mm(S,D);R=add(mm(K,D),S,-1)
    eps=[F(x) for x in frame['trial_action_D_norm_error_upper']]
    HL,HU=matrix(frame,'trial_frame_endpoint_entry_lower'),matrix(frame,'trial_frame_endpoint_entry_upper')
    HL[3][3]=F(sign['new_common_endpoint_energy_lower'])
    HU[3][3]=F(tail['new_common_endpoint_energy_upper'])
    assert HL[3][3]<=HU[3][3]
    pairs=[(a,b) for a in range(7) for b in range(7)]
    hpairs=[(a,b) for a in range(5) for b in range(5)]
    if replay:pairs.reverse();hpairs.reverse()
    sc,yc,dc=transpose(S),transpose(Y),transpose(D)
    LL=[[F(0)]*5 for _ in range(5)];LU=[[F(0)]*5 for _ in range(5)]
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
    sourceLo,sourceHi=cong(S,GLo),cong(S,GHi)
    assert psd(sourceLo)
    weights=[sqrtup(sourceHi[i][i]) for i in range(5)]
    variationalLo,variationalHi,intervalErr=loewner(LL,LU,weights)
    nominal=cong(R,GHi)
    # Four errors in the first group and one t10 error in the second.
    minor=cong(D,[[4*eps[i]**2 if i==j and i<4 else F(0) for j in range(5)] for i in range(5)])
    major=[[eps[4]**2*D[4][i]*D[4][j] for j in range(5)] for i in range(5)]
    def width_gate(gap):
        def accepts(n):return psd(add([[F(n,10**6)*x for x in row] for row in sourceLo],gap,-1))
        hi=1
        while not accepts(hi):hi*=2;assert hi<10**12
        lo=0
        while hi-lo>1:
            mid=(lo+hi)//2
            if accepts(mid):hi=mid
            else:lo=mid
        assert accepts(hi) and not accepts(lo)
        return F(hi,10**6)
    candidates=[]
    opts=[(F(1,100),F(1,20)),(F(1,10),F(1,20)),(F(1,10),F(1,10)),(F(1,2),F(1,10)),(F(1),F(1))]
    if replay:opts.reverse()
    best=None
    for tau,gamma in opts:
        err=add([[(1+tau)*x for x in row] for row in major],
                [[(1+1/tau)*x for x in row] for row in minor])
        residual=add([[(1+gamma)*x for x in row] for row in nominal],
                     [[(1+1/gamma)*x for x in row] for row in err])
        gap=add(add(variationalHi,residual),variationalLo,-1)
        assert psd(err) and psd(residual) and psd(gap)
        beta=width_gate(gap)
        candidates.append(dict(tau=str(tau),gamma=str(gamma),relative_width_upper=str(beta)))
        if best is None or (beta,tau,gamma)<best[0]:best=((beta,tau,gamma),residual)
    candidates.sort(key=lambda x:(F(x['tau']),F(x['gamma'])))
    (beta,tau,gamma),residual=best
    gap=add(add(variationalHi,residual),variationalLo,-1)
    assert psd(add([[beta*x for x in row] for row in sourceLo],gap,-1))
    # Least-source-energy fifth-coordinate mixture; rounding only selects a rational witness.
    cross=[[sourceLo[i][4]] for i in range(4)]
    proj=mm(inv([row[:4] for row in sourceLo[:4]]),cross)
    witness=[down(-proj[i][0],10**12) for i in range(4)]+[F(1)]
    def quadratic(M):return sum(witness[i]*M[i][j]*witness[j] for i in range(5) for j in range(5))
    sourceEnergyLo=quadratic(sourceLo);sourceEnergyHi=quadratic(sourceHi)
    intervalWidth=quadratic(add(variationalHi,variationalLo,-1))
    residualWidth=quadratic(residual);totalWidth=quadratic(gap)
    assert 0<sourceEnergyLo<=sourceEnergyHi and totalWidth==intervalWidth+residualWidth
    assert totalWidth>sourceEnergyHi/2
    # Universal 0 <= C <= I implies half the actual source Gram <= response <= Gram.
    # It supplies a positive fallback independent of the fragile trial lower matrix.
    assert psd(add([[x/2 for x in row] for row in sourceLo],
                   [[x/2 for x in row] for row in sourceLo],-1))
    return dict(milestone='RC145',status='PASS: paid fifth-source enclosure and certified conditioning obstruction for this trial',
        starting_commit='f0ec243e0b970325d2017dca925b0a6adb2ab790',input_sha256=[hashlib.sha256(b).hexdigest() for b in raw],
        aperture='11/10',carrier_family_dimension=7,response_sources=['P0','f0','w14-alpha*psi0','(v10+z_b6)/2','t10'],
        source_Gram_Loewner_lower=ser(sourceLo),source_Gram_Loewner_upper=ser(sourceHi),
        trial_source_frame_coefficients=ser(D),variational_entry_lower=ser(LL),variational_entry_upper=ser(LU),
        variational_Loewner_lower=ser(variationalLo),variational_Loewner_upper=ser(variationalHi),
        variational_interval_error_diagonal=list(map(str,intervalErr)),
        full_residual_Gram_upper=ser(residual),reference_response_Loewner_lower=ser(variationalLo),
        reference_response_Loewner_upper=ser(add(variationalHi,residual)),candidate_widths=candidates,
        selected_tau=str(tau),selected_gamma=str(gamma),relative_source_Gram_matrix_width_upper=str(beta),
        witness_mixture=list(map(str,witness)),witness_source_energy_lower=str(down(sourceEnergyLo,10**18)),
        witness_source_energy_upper=str(up(sourceEnergyHi,10**18)),
        witness_variational_interval_width_lower=str(down(intervalWidth,10**18)),
        witness_residual_width_lower=str(down(residualWidth,10**18)),
        witness_total_width_lower=str(down(totalWidth,10**18)),
        witness_width_over_source_energy_upper_lower=str(down(totalWidth/sourceEnergyHi,10**6)),
        half_Gram_width_gate_fails_for_this_enclosure=True,
        structural_positive_response_lower='(1/2) * actual source Gram; valid because I<=I+C<=2I',
        full_five_source_trial_lower_psd=psd(variationalLo),mixed_action_errors_paid_without_orthogonality=True,
        half_Gram_width_target_met=False,required_Stage_I_matrix_tolerance_specified=False,
        original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,
        RH=False,F4=False,Lean=False,
        next_cursor='refine t10 endpoint and action correlations along the certified nearly dependent mixture before claiming five-source matrix accuracy')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=13)
    a=p.parse_args();result=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==result
    else:Path(a.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC145 PASS: fifth-source conditioning audit')
