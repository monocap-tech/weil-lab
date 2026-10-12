"""RC143: four-source full-carrier inverse response with paid mixed errors."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
from validate_rpb108_rc127_enriched_even_endpoint_action import down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc129_four_vector_joint_moment import add,mm,transpose,cong,inv
from validate_rpb108_rc142_centered_common_tail import run as rc142_run

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths]
    prior=json.loads(raw[0]);assert prior==rc142_run(paths[1:],replay)
    frame=json.loads(raw[4]);joint=json.loads(raw[6]);sign=json.loads(raw[1])
    assert [x['milestone'] for x in (prior,frame,joint,sign)]==['RC142','RC138','RC136','RC141']
    def mat(key):return [[F(x) for x in row] for row in joint[key]]
    GL,GU=mat('actual_D_Gram_entry_lower'),mat('actual_D_Gram_entry_upper')
    GLo,GHi=mat('actual_D_Gram_Loewner_lower'),mat('actual_D_Gram_Loewner_upper')
    GM=[[(GL[i][j]+GU[i][j])/2 for j in range(7)] for i in range(7)]
    S=[[F(x) for x in row[:4]] for row in frame['trial_source_matrix']]
    T=[[F(x) for x in row[:4]] for row in frame['trial_action_approximation_matrix']]
    K=add(S,T);Q=cong(K,GM);assert psd(Q)
    # Nominal least residual solve chooses rational trials, never accepts a center as exact.
    D=mm(inv(Q),mm(transpose(K),mm(GM,S)))
    D=[[down(x,10**20) for x in row] for row in D]
    Y=mm(S,D);R=add(mm(K,D),S,-1)
    eps=[F(x) for x in frame['trial_action_D_norm_error_upper'][:4]]
    HL=[[F(x) for x in row[:4]] for row in frame['trial_frame_endpoint_entry_lower'][:4]]
    HU=[[F(x) for x in row[:4]] for row in frame['trial_frame_endpoint_entry_upper'][:4]]
    HL[3][3]=F(sign['new_common_endpoint_energy_lower'])
    HU[3][3]=F(prior['new_common_endpoint_energy_upper'])
    assert HL[3][3]<=HU[3][3]
    pairs=[(i,j) for i in range(7) for j in range(7)]
    hpairs=[(i,j) for i in range(4) for j in range(4)]
    if replay:pairs.reverse();hpairs.reverse()
    def bil(x,y,L,U,order):
        lo=hi=F(0)
        for i,j in order:
            v=x[i]*y[j];lo+=v*(L[i][j] if v>=0 else U[i][j]);hi+=v*(U[i][j] if v>=0 else L[i][j])
        return lo,hi
    sc,yc,dc=transpose(S),transpose(Y),transpose(D)
    LL=[[F(0)]*4 for _ in range(4)];LU=[[F(0)]*4 for _ in range(4)]
    for i in range(4):
        for j in range(i,4):
            pL,pU=bil(sc[i],yc[j],GL,GU,pairs)
            qL,qU=bil(yc[i],sc[j],GL,GU,pairs)
            gL,gU=bil(yc[i],yc[j],GL,GU,pairs)
            hL,hU=bil(dc[i],dc[j],HL,HU,hpairs)
            LL[i][j]=LL[j][i]=pL+qL-gU-hU
            LU[i][j]=LU[j][i]=pU+qU-gL-hL
    sourceLo,sourceHi=cong(S,GLo),cong(S,GHi);assert psd(sourceLo)
    weights=[sqrtup(sourceHi[i][i]) for i in range(4)]
    LLo,LHi,Lerror=loewner(LL,LU,weights)
    nominal=cong(R,GHi);assert psd(nominal)
    # Four action-error generators: E^*E <= 4 D^* diag(eps_j^2) D.
    Eupper=cong(D,[[4*eps[i]**2 if i==j else F(0) for j in range(4)] for i in range(4)])
    # (R_nom+E)^*(R_nom+E) <= 2 R_nom^*R_nom+2 E^*E.
    residualUpper=[[2*(nominal[i][j]+Eupper[i][j]) for j in range(4)] for i in range(4)]
    assert psd(Eupper) and psd(residualUpper)
    SigmaLo=LLo;SigmaHi=add(LHi,residualUpper)
    positiveFloor=[[sourceHi[i][i]/10**8 if i==j else F(0) for j in range(4)] for i in range(4)]
    assert psd(add(SigmaLo,positiveFloor,-1))
    gap=add(SigmaHi,SigmaLo,-1);assert psd(gap)
    # Exact rational relative matrix-width gate: gap <= beta*actual source Gram.
    # Acceptance uses its certified Loewner lower, and includes arbitrary mixtures.
    def accepts(n):return psd(add([[F(n,10**6)*x for x in row] for row in sourceLo],gap,-1))
    hi=1
    while not accepts(hi):hi*=2;assert hi<10**12
    lo=0
    while hi-lo>1:
        mid=(lo+hi)//2
        if accepts(mid):hi=mid
        else:lo=mid
    beta=F(hi,10**6);assert accepts(hi) and not accepts(lo)
    diagonals=[]
    for i in range(4):
        diagonals.append(dict(source=i,normalized_reference_lower=str(down(SigmaLo[i][i]/sourceHi[i][i],10**12)),normalized_reference_upper=str(up(SigmaHi[i][i]/sourceLo[i][i],10**12))))
    controls=[]
    for lam in (F(0),F(1,2),F(1)):
        # Two-source scalar spectral model with a nonzero mixed residual.
        src=[F(1),F(-2,3)];yy=[F(1,3),F(-1,5)];r=[(1+lam)*y-s for y,s in zip(yy,src)]
        sigma=[[x*y/(1+lam) for y in src] for x in src]
        L=[[src[i]*yy[j]+yy[i]*src[j]-(1+lam)*yy[i]*yy[j] for j in range(2)] for i in range(2)]
        rr=[[r[i]*r[j] for j in range(2)] for i in range(2)]
        assert sigma==add(L,[[x/(1+lam) for x in row] for row in rr])
        assert psd(add(add(sigma,L,-1),[[x/2 for x in row] for row in rr],-1))
        assert psd(add(add(L,rr),sigma,-1))
        controls.append(dict(C_eigenvalue=str(lam),signed_mixed_matrix_identity_verified=True))
    result=dict(milestone='RC143',status='PASS: full four-source joint reference inverse matrix enclosure with paid mixed residuals',starting_commit='d6c1dda4b8c9950768f2d0c4424d99701d103b98',input_sha256=[hashlib.sha256(b).hexdigest() for b in raw],aperture='11/10',carrier_family_dimension=7,new_family_vectors_added=0,response_sources=['P0','f0','w14-alpha*psi0','(v10+z_b6)/2'],response_source_matrix=ser(S),trial_source_frame_coefficients=ser(D),trial_seven_vector_matrix=ser(Y),nominal_residual_seven_vector_matrix=ser(R),source_Gram_Loewner_lower=ser(sourceLo),source_Gram_Loewner_upper=ser(sourceHi),variational_matrix_entry_lower=ser(LL),variational_matrix_entry_upper=ser(LU),variational_matrix_Loewner_lower=ser(LLo),variational_matrix_Loewner_upper=ser(LHi),variational_interval_error_diagonal=list(map(str,Lerror)),nominal_residual_Gram_Loewner_upper=ser(nominal),action_error_Gram_Loewner_upper=ser(Eupper),full_residual_Gram_Loewner_upper=ser(residualUpper),reference_response_matrix_Loewner_lower=ser(SigmaLo),reference_response_matrix_Loewner_upper=ser(SigmaHi),reference_matrix_width=ser(gap),relative_source_Gram_matrix_width_upper=str(beta),relative_width_grid='1/1000000',reference_lower_matrix_psd_verified=psd(SigmaLo),all_four_source_mixtures_certified=True,mixed_residuals_paid_without_zero_cross_assumption=True,center_matrices_used_only_for_trial_selection=True,normalized_diagonal_response_enclosures=diagonals,inherited_sharper_P0_lower=prior['normalized_P0_reference_response_lower'],inherited_sharper_P0_upper=prior['normalized_P0_reference_response_upper'],exact_signed_mixed_controls=controls,required_Stage_I_matrix_tolerance_specified=False,high_accuracy_reference_inverse_completed=False,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,next_cursor='compare achieved joint matrix width with explicit Stage I budget; refine source conditioning and t endpoint row or extend to required native sources')
    result['reference_lower_positive_diagonal_floor']=ser(positiveFloor)
    result['reference_lower_strict_positive_verified']=True
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=11)
    a=p.parse_args();result=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==result
    else:Path(a.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC143 PASS: four-source joint variational inverse matrix')
