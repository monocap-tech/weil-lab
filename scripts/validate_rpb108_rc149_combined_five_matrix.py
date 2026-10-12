"""RC149: full five-source reference response from combined endpoint actions."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc129_four_vector_joint_moment import add,mm,transpose,cong,inv
from validate_rpb108_rc148_combined_endpoint_response import run as rc148_run

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths]
    prior=json.loads(raw[0]);assert prior==rc148_run(paths[1:],replay)
    narrow=json.loads(raw[2]);old=json.loads(raw[3]);frame=json.loads(raw[10]);joint=json.loads(raw[12])
    sign=json.loads(raw[7]);tail=json.loads(raw[6])
    assert [x['milestone'] for x in (prior,narrow,old,frame,joint,sign,tail)]==['RC148','RC146','RC145','RC138','RC136','RC141','RC142']
    def mat(d,k):return [[F(x) for x in row] for row in d[k]]
    GL,GU=mat(joint,'actual_D_Gram_entry_lower'),mat(joint,'actual_D_Gram_entry_upper')
    GLo,GHi=mat(joint,'actual_D_Gram_Loewner_lower'),mat(joint,'actual_D_Gram_Loewner_upper')
    HL,HU=mat(frame,'trial_frame_endpoint_entry_lower'),mat(frame,'trial_frame_endpoint_entry_upper')
    HL[3][3]=F(sign['new_common_endpoint_energy_lower']);HU[3][3]=F(tail['new_common_endpoint_energy_upper'])
    S,T=mat(frame,'trial_source_matrix'),mat(frame,'trial_action_approximation_matrix')
    D=mat(old,'trial_source_frame_coefficients');X=mat(narrow,'original_source_transform')
    SX,DX=mm(S,X),mm(D,X);Y=mm(S,DX);A=mm(T,DX)
    R=add(add(Y,A),SX,-1)
    eps=[F(x) for x in frame['trial_action_D_norm_error_upper']]
    actionError=[sum(abs(DX[a][i])*eps[a] for a in range(5)) for i in range(5)]
    sourceLo,sourceHi=cong(SX,GLo),cong(SX,GHi)
    qNorm=[sqrtup(cong([[Y[a][i]] for a in range(7)],GHi)[0][0]) for i in range(5)]
    sc,yc,ac,dc=map(transpose,(SX,Y,A,DX))
    gpairs=[(a,b) for a in range(7) for b in range(7)]
    hpairs=[(a,b) for a in range(5) for b in range(5)]
    if replay:gpairs.reverse();hpairs.reverse()
    def bil(x,y):
        lo=hi=F(0)
        for a,b in gpairs:
            c=x[a]*y[b]
            lo+=c*(GL[a][b] if c>=0 else GU[a][b])
            hi+=c*(GU[a][b] if c>=0 else GL[a][b])
        return lo,hi
    HLo=[[F(0)]*5 for _ in range(5)];HHi=[[F(0)]*5 for _ in range(5)]
    LL=[[F(0)]*5 for _ in range(5)];LU=[[F(0)]*5 for _ in range(5)]
    for i in range(5):
        for j in range(i,5):
            hlo=hhi=F(0)
            for a,b in hpairs:
                c=dc[i][a]*dc[j][b]
                hlo+=c*(HL[a][b] if c>=0 else HU[a][b])
                hhi+=c*(HU[a][b] if c>=0 else HL[a][b])
            # Each direction is a valid action identity for the same symmetric
            # endpoint pairing. Its error is paid in the actual D norm.
            for acted,other in ((i,j),(j,i)):
                blo,bhi=bil(ac[acted],yc[other])
                hlo=max(hlo,down(blo-actionError[acted]*qNorm[other]))
                hhi=min(hhi,up(bhi+actionError[acted]*qNorm[other]))
            assert hlo<=hhi
            HLo[i][j]=HLo[j][i]=hlo;HHi[i][j]=HHi[j][i]=hhi
            glo=ghi=F(0)
            for a,b in gpairs:
                c=sc[i][a]*yc[j][b]+yc[i][a]*sc[j][b]-yc[i][a]*yc[j][b]
                glo+=c*(GL[a][b] if c>=0 else GU[a][b])
                ghi+=c*(GU[a][b] if c>=0 else GL[a][b])
            LL[i][j]=LL[j][i]=down(glo-hhi)
            LU[i][j]=LU[j][i]=up(ghi-hlo)
    assert HLo[4][4]>=F(prior['combined_endpoint_energy_lower'])
    assert HHi[4][4]<=F(prior['combined_endpoint_energy_upper'])
    weights=[sqrtup(sourceHi[i][i]) for i in range(5)]
    LLo,LHi,errs=loewner(LL,LU,weights)
    assert psd(LLo)
    nominal=cong(R,GHi)
    minor=cong(DX,[[4*eps[i]**2 if i==j and i<4 else F(0) for j in range(5)] for i in range(5)])
    major=[[eps[4]**2*DX[4][i]*DX[4][j] for j in range(5)] for i in range(5)]
    def gate(gap):
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
    opts=[(F(1,10),F(1)),(F(1,10),F(2)),(F(1,4),F(1)),(F(1,4),F(2)),
          (F(1,4),F(4)),(F(1,2),F(2)),(F(1),F(1))]
    if replay:opts.reverse()
    best=None;candidates=[]
    for tau,gamma in opts:
        err=add([[(1+tau)*x for x in row] for row in major],
                [[(1+1/tau)*x for x in row] for row in minor])
        residual=add([[(1+gamma)*x for x in row] for row in nominal],
                     [[(1+1/gamma)*x for x in row] for row in err])
        assert psd(err) and psd(residual)
        gap=add(add(LHi,residual),LLo,-1)
        assert psd(gap)
        beta=gate(gap)
        candidates.append(dict(tau=str(tau),gamma=str(gamma),relative_width_upper=str(beta)))
        if best is None or (beta,tau,gamma)<best[0]:best=((beta,tau,gamma),residual)
    (beta,tau,gamma),residual=best
    candidates.sort(key=lambda x:(F(x['tau']),F(x['gamma'])))
    assert beta<F(1,2) and beta<F(narrow['relative_source_Gram_matrix_width_upper'])
    upper=add(LHi,residual);gap=add(upper,LLo,-1)
    assert psd(add([[beta*x for x in row] for row in sourceLo],gap,-1))
    Xi=inv(X);originalLo=cong(Xi,LLo);originalHi=cong(Xi,upper)
    assert psd(originalLo)
    assert psd(add([[beta*x for x in row] for row in cong(S,GLo)],add(originalHi,originalLo,-1),-1))
    floor=[[sourceHi[i][i]/10**8 if i==j else F(0) for j in range(5)] for i in range(5)]
    assert psd(add(LLo,floor,-1))
    controls=[]
    for x,y in ((F(1),F(-1)),(F(1),F(1)),(F(2,3),F(-1,7))):
        for parameter in (tau,gamma):
            assert (x+y)**2<=(1+parameter)*x*x+(1+1/parameter)*y*y
            controls.append(dict(x=str(x),y=str(y),parameter=str(parameter),signed_Young_verified=True))
    return dict(milestone='RC149',status='PASS: positive five-source reference response matrix with width below half source Gram',
        starting_commit='6780612cab00433d11d6c0a7ab517bdd1637eb73',
        input_sha256=[hashlib.sha256(b).hexdigest() for b in raw],aperture='11/10',
        carrier_family_dimension=7,response_source_count=5,
        transformed_endpoint_pairing_lower=ser(HLo),transformed_endpoint_pairing_upper=ser(HHi),
        transformed_variational_entry_lower=ser(LL),transformed_variational_entry_upper=ser(LU),
        transformed_variational_Loewner_lower=ser(LLo),transformed_variational_Loewner_upper=ser(LHi),
        transformed_interval_error_diagonal=list(map(str,errs)),
        transformed_source_Gram_lower=ser(sourceLo),transformed_source_Gram_upper=ser(sourceHi),
        transformed_residual_Gram_upper=ser(residual),
        original_source_response_Loewner_lower=ser(originalLo),
        original_source_response_Loewner_upper=ser(originalHi),
        selected_tau=str(tau),selected_gamma=str(gamma),candidate_widths=candidates,
        relative_source_Gram_matrix_width_upper=str(beta),
        RC146_width_upper=narrow['relative_source_Gram_matrix_width_upper'],
        reference_lower_positive_diagonal_floor=ser(floor),
        reference_lower_strict_positive_verified=True,
        all_five_source_mixtures_certified=True,half_Gram_matrix_width_target_met=True,
        mixed_endpoint_action_directions_both_paid=True,
        mixed_action_errors_paid_without_orthogonality=True,signed_Young_controls=controls,
        required_Stage_I_matrix_tolerance_specified=False,
        original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,
        RH=False,F4=False,Lean=False,
        next_cursor='compare five-source coverage and achieved matrix width to explicit Stage I tolerance; transport original native-source actions')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=17)
    a=p.parse_args();result=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==result
    else:Path(a.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC149 PASS: positive five-source joint reference inverse matrix')
