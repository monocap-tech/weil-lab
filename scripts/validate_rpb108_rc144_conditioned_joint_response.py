"""RC144: combine signed uncertainties before conditioned matrix acceptance."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
from validate_rpb108_rc127_enriched_even_endpoint_action import down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc129_four_vector_joint_moment import add,mm,transpose,cong,inv
from validate_rpb108_rc143_joint_variational_matrix import run as rc143_run

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths]
    prior=json.loads(raw[0]);assert prior==rc143_run(paths[1:],replay)
    frame=json.loads(raw[5]);joint=json.loads(raw[7]);tail=json.loads(raw[1]);sign=json.loads(raw[2])
    assert [x['milestone'] for x in (prior,frame,joint,tail,sign)]==['RC143','RC138','RC136','RC142','RC141']
    def mat(key):return [[F(x) for x in row] for row in joint[key]]
    GL,GU=mat('actual_D_Gram_entry_lower'),mat('actual_D_Gram_entry_upper')
    GLo,GHi=mat('actual_D_Gram_Loewner_lower'),mat('actual_D_Gram_Loewner_upper')
    S=[[F(x) for x in row] for row in prior['response_source_matrix']]
    Y=[[F(x) for x in row] for row in prior['trial_seven_vector_matrix']]
    D=[[F(x) for x in row] for row in prior['trial_source_frame_coefficients']]
    R=[[F(x) for x in row] for row in prior['nominal_residual_seven_vector_matrix']]
    eps=[F(x) for x in frame['trial_action_D_norm_error_upper'][:4]]
    HL=[[F(x) for x in row[:4]] for row in frame['trial_frame_endpoint_entry_lower'][:4]]
    HU=[[F(x) for x in row[:4]] for row in frame['trial_frame_endpoint_entry_upper'][:4]]
    HL[3][3]=F(sign['new_common_endpoint_energy_lower']);HU[3][3]=F(tail['new_common_endpoint_energy_upper'])
    GS=cong(S,GLo)
    # Rational Gram-Schmidt chooses coordinates only; acceptance uses actual enclosures.
    cols=[]
    for j in range(4):
        v=[F(i==j) for i in range(4)]
        for w in cols:
            num=sum(w[a]*GS[a][b]*v[b] for a in range(4) for b in range(4))
            den=sum(w[a]*GS[a][b]*w[b] for a in range(4) for b in range(4));assert den>0
            v=[v[i]-num/den*w[i] for i in range(4)]
        cols.append([down(x,10**20) for x in v])
    W=transpose(cols);I=[[F(i==j) for j in range(4)] for i in range(4)]
    assert all(W[i][i]==1 and all(W[i][j]==0 for j in range(i)) for i in range(4))
    pairs=[(a,b) for a in range(7) for b in range(7)];hpairs=[(a,b) for a in range(4) for b in range(4)]
    if replay:pairs.reverse();hpairs.reverse()
    def width_gate(gap,gram):
        def yes(n):return psd(add([[F(n,10**6)*x for x in row] for row in gram],gap,-1))
        hi=1
        while not yes(hi):hi*=2;assert hi<10**12
        lo=0
        while hi-lo>1:
            mid=(hi+lo)//2
            if yes(mid):hi=mid
            else:lo=mid
        assert yes(hi) and not yes(lo)
        return F(hi,10**6)
    summaries=[];best=None
    transforms=[('identity',I),('rational_orthogonalized',W)]
    if replay:transforms.reverse()
    for name,X in transforms:
        SX,YX,DX,RX=mm(S,X),mm(Y,X),mm(D,X),mm(R,X)
        sc,yc,dc=transpose(SX),transpose(YX),transpose(DX)
        LL=[[F(0)]*4 for _ in range(4)];LU=[[F(0)]*4 for _ in range(4)]
        for i in range(4):
            for j in range(i,4):
                lo=hi=F(0)
                # Form the entire signed Gram coefficient before interval evaluation.
                for a,b in pairs:
                    v=sc[i][a]*yc[j][b]+yc[i][a]*sc[j][b]-yc[i][a]*yc[j][b]
                    lo+=v*(GL[a][b] if v>=0 else GU[a][b]);hi+=v*(GU[a][b] if v>=0 else GL[a][b])
                for a,b in hpairs:
                    v=-dc[i][a]*dc[j][b]
                    lo+=v*(HL[a][b] if v>=0 else HU[a][b]);hi+=v*(HU[a][b] if v>=0 else HL[a][b])
                LL[i][j]=LL[j][i]=down(lo);LU[i][j]=LU[j][i]=up(hi)
        gramLo,gramHi=cong(SX,GLo),cong(SX,GHi)
        weights=[sqrtup(gramHi[i][i]) for i in range(4)]
        LLo,LHi,errs=loewner(LL,LU,weights)
        nominal=cong(RX,GHi)
        minor=cong(DX,[[3*eps[i]**2 if i==j and i<3 else F(0) for j in range(4)] for i in range(4)])
        major=[[eps[3]**2*DX[3][i]*DX[3][j] for j in range(4)] for i in range(4)]
        options=[(F(1,100),F(1,20)),(F(1,10),F(1,20)),(F(1,10),F(1,10)),(F(1,10),F(1,4)),(F(1,10),F(1))]
        if replay:options.reverse()
        for tau,gamma in options:
            errorGram=add([[x*(1+tau) for x in row] for row in major],[[x*(1+1/tau) for x in row] for row in minor])
            residual=add([[x*(1+gamma) for x in row] for row in nominal],[[x*(1+1/gamma) for x in row] for row in errorGram])
            assert psd(errorGram) and psd(residual)
            upper=add(LHi,residual);gap=add(upper,LLo,-1);assert psd(gap)
            beta=width_gate(gap,gramLo)
            summaries.append(dict(coordinates=name,tau=str(tau),gamma=str(gamma),relative_width_upper=str(beta)))
            key=(beta,name,tau,gamma)
            if best is None or key<best[0]:best=(key,dict(X=X,LL=LL,LU=LU,LLo=LLo,upper=upper,gap=gap,errorGram=errorGram,residual=residual,errs=errs,gramLo=gramLo))
    summaries.sort(key=lambda x:(x['coordinates'],F(x['tau']),F(x['gamma'])))
    (beta,name,tau,gamma),b=best
    oldBeta=F(prior['relative_source_Gram_matrix_width_upper']);assert beta<oldBeta
    Xi=inv(b['X']);lowerOriginal=cong(Xi,b['LLo']);upperOriginal=cong(Xi,b['upper'])
    gapOriginal=add(upperOriginal,lowerOriginal,-1)
    assert psd(add([[beta*x for x in row] for row in GS],gapOriginal,-1))
    floor=[[F(prior['source_Gram_Loewner_upper'][i][i])/10**8 if i==j else F(0) for j in range(4)] for i in range(4)]
    assert psd(add(lowerOriginal,floor,-1))
    # Exact Young inequalities include arbitrary signed aligned or opposed errors.
    controls=[]
    for x,y in ((F(1),F(1)),(F(1),F(-1)),(F(2,3),F(-1,7))):
        for t in (tau,gamma):
            assert (x+y)**2<=(1+t)*x*x+(1+1/t)*y*y
            controls.append(dict(x=str(x),y=str(y),parameter=str(t),signed_Young_bound_verified=True))
    return dict(milestone='RC144',status='PASS: conditioned joint response and tuned mixed error bounds improve uniform matrix width',starting_commit='ffc8edbb172a97d1eb5d7a5fe7397ff73163910d',input_sha256=[hashlib.sha256(x).hexdigest() for x in raw],aperture='11/10',carrier_family_dimension=7,response_source_count=4,new_family_vectors_added=0,candidate_widths=summaries,selected_coordinates=name,selected_tau=str(tau),selected_gamma=str(gamma),selected_rational_source_transform=ser(b['X']),transformed_variational_entry_lower=ser(b['LL']),transformed_variational_entry_upper=ser(b['LU']),transformed_action_error_Gram_upper=ser(b['errorGram']),transformed_full_residual_Gram_upper=ser(b['residual']),reference_response_matrix_Loewner_lower_original_sources=ser(lowerOriginal),reference_response_matrix_Loewner_upper_original_sources=ser(upperOriginal),reference_lower_positive_diagonal_floor=ser(floor),reference_lower_strict_positive_verified=True,relative_source_Gram_matrix_width_upper=str(beta),RC143_relative_width_upper=str(oldBeta),previous_width_over_new_width_lower=str(down(oldBeta/beta,10**6)),all_four_source_mixtures_certified=True,mixed_errors_paid_without_orthogonality_assumption=True,coordinate_transform_used_only_for_enclosure_selection=True,signed_Young_controls=controls,inherited_sharper_P0_lower=prior['inherited_sharper_P0_lower'],inherited_sharper_P0_upper=prior['inherited_sharper_P0_upper'],required_Stage_I_matrix_tolerance_specified=False,high_accuracy_reference_inverse_completed=False,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,next_cursor='audit response width contributions against concrete Stage I budget; refine common/t action data or extend required source coverage')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=12)
    a=p.parse_args();result=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==result
    else:Path(a.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC144 PASS: conditioned four-source joint inverse matrix')
