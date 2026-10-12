"""RC158: full seven-source variational inverse enclosure and width audit."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc129_four_vector_joint_moment import add,mm,transpose,cong,inv

def run(paths,reverse=False):
    raw=[Path(p).read_bytes() for p in paths]
    cross,new,actions,old,frame,joint,oldtrial,narrow=map(json.loads,raw)
    assert [d['milestone'] for d in (cross,new,actions,old,frame,joint,oldtrial,narrow)]==['RC157','RC156','RC155','RC149','RC138','RC136','RC145','RC146']
    hs=[hashlib.sha256(b).hexdigest() for b in raw]
    assert cross['input_sha256'][:2]==[hs[1],hs[4]]
    assert new['input_sha256'][2]==hs[2]
    assert actions['input_sha256'][1:3]==[hs[4],hs[5]]
    assert old['input_sha256'][2:4]==[hs[7],hs[6]]
    assert old['input_sha256'][10]==hs[4] and old['input_sha256'][12]==hs[5]
    mat=lambda d,k:[[F(x) for x in r] for r in d[k]]
    W=mat(actions,'source_frame_matrix');T=mat(frame,'trial_action_approximation_matrix')
    order=[0,2,3,4,6,1,5];P=[[F(j==i) for j in range(7)] for i in order]
    Wi=mm(inv(mm(P,W)),P)
    assert mm(W,Wi)==[[F(i==j) for j in range(7)] for i in range(7)]
    GL,GU=mat(joint,'actual_D_Gram_entry_lower'),mat(joint,'actual_D_Gram_entry_upper')
    GLo,GHi=mat(joint,'actual_D_Gram_Loewner_lower'),mat(joint,'actual_D_Gram_Loewner_upper')
    Gmid=[[(GL[i][j]+GU[i][j])/2 for j in range(7)] for i in range(7)]
    G=cong(W,Gmid);frameLo=cong(W,GLo);frameHi=cong(W,GHi)
    # Assemble the actual paid trial-source and trial Gram center blocks.
    # Centers choose rational trial coefficients only; acceptance encloses
    # every mixed term with its original directed rational intervals.
    Q=mm(transpose(T),mm(Gmid,[row[:5] for row in W]));R=cong(T,Gmid)
    fullQ=[[F(0)]*7 for _ in range(7)];fullR=[[F(0)]*7 for _ in range(7)]
    def midpoint(d,lo,hi):
        a,b=mat(d,lo),mat(d,hi)
        return [[(x+y)/2 for x,y in zip(ar,br)] for ar,br in zip(a,b)]
    qoldnew=midpoint(cross,'old_trial_new_source_pairing_lower','old_trial_new_source_pairing_upper')
    qnewold=midpoint(cross,'new_trial_old_source_pairing_lower','new_trial_old_source_pairing_upper')
    qnew=midpoint(new,'trial_source_pairing_entry_lower','trial_source_pairing_entry_upper')
    rnewold=midpoint(cross,'old_trial_new_trial_Gram_lower','old_trial_new_trial_Gram_upper')
    rnew=midpoint(new,'trial_Gram_entry_lower','trial_Gram_entry_upper')
    for i in range(7):
        for j in range(7):
            fullQ[i][j]=Q[i][j] if i<5 and j<5 else qoldnew[i][j-5] if i<5 else qnewold[i-5][j] if j<5 else qnew[i-5][j-5]
            fullR[i][j]=R[i][j] if i<5 and j<5 else rnewold[i][j-5] if i<5 else rnewold[j][i-5] if j<5 else rnew[i-5][j-5]
    K=add(add(add(G,fullQ),transpose(fullQ)),fullR)
    assert psd(K)
    fit=mm(inv(K),add(G,fullQ));fit=[[down(x,10**20) for x in row] for row in fit]
    # Preserve RC149's successful old trial and old source conditioning.
    Xold=mat(narrow,'original_source_transform')
    M=mm(mat(oldtrial,'trial_source_frame_coefficients'),Xold)
    base=[[M[i][j] if i<5 and j<5 else F(i==j) if i>=5 and j>=5 else F(0) for j in range(7)] for i in range(7)]
    A=[r[:5] for r in frameLo[:5]];Bcross=[r[5:] for r in frameLo[:5]]
    elimination=mm(inv(A),Bcross)
    schur=add([r[5:] for r in frameLo[5:]],mm(transpose(Bcross),elimination),-1)
    crit=down(-schur[0][1]/schur[0][0],10**20)
    X=[[Xold[i][j] if i<5 and j<5 else F(0) for j in range(7)] for i in range(7)]
    for i in range(5):X[i][5]=down(-elimination[i][0],10**20);X[i][6]=down(-elimination[i][1]-crit*elimination[i][0],10**20)
    X[5][5]=1;X[5][6]=crit;X[6][6]=1
    fitX=mm(fit,X)
    Y=[[base[i][j] if j<5 else fitX[i][j] for j in range(7)] for i in range(7)]
    Y=[[down(x,10**20) for x in row] for row in Y]
    U=mm(inv(base),Y)
    sx,yx=mm(W,X),mm(W,Y)
    sourceLo,sourceHi=cong(sx,GLo),cong(sx,GHi);assert psd(sourceLo)
    # Endpoint matrix in the fixed old-trial / new-source basis. RC149's
    # old block was evaluated after signed conditioning; keep that result.
    HBL=[[F(0)]*7 for _ in range(7)];HBU=[[F(0)]*7 for _ in range(7)]
    oldHL,oldHU=mat(old,'transformed_endpoint_pairing_lower'),mat(old,'transformed_endpoint_pairing_upper')
    crossHL,crossHU=mat(cross,'source_endpoint_five_by_two_lower'),mat(cross,'source_endpoint_five_by_two_upper')
    newHL,newHU=mat(new,'source_endpoint_pairing_entry_lower'),mat(new,'source_endpoint_pairing_entry_upper')
    def interval(coeff,L,U):
        lo=hi=F(0)
        terms=[(i,j) for i in range(len(L)) for j in range(len(L[0]))]
        if reverse:terms.reverse()
        for i,j in terms:
            c=coeff[i][j]
            lo+=c*(L[i][j] if c>=0 else U[i][j]);hi+=c*(U[i][j] if c>=0 else L[i][j])
        return down(lo),up(hi)
    for i in range(5):
        for j in range(5):HBL[i][j]=oldHL[i][j];HBU[i][j]=oldHU[i][j]
        for j in range(2):
            coeff=[[M[k][i] if l==j else F(0) for l in range(2)] for k in range(5)]
            lo,hi=interval(coeff,crossHL,crossHU)
            HBL[i][j+5]=HBL[j+5][i]=lo;HBU[i][j+5]=HBU[j+5][i]=hi
    for i in range(2):
        for j in range(2):HBL[i+5][j+5]=newHL[i][j];HBU[i+5][j+5]=newHU[i][j]
    LL=[[F(0)]*7 for _ in range(7)];LU=[[F(0)]*7 for _ in range(7)]
    for i in range(7):
        for j in range(i,7):
            gc=[[sx[a][i]*yx[b][j]+yx[a][i]*sx[b][j]-yx[a][i]*yx[b][j] for b in range(7)] for a in range(7)]
            hc=[[U[a][i]*U[b][j] for b in range(7)] for a in range(7)]
            gl,gu=interval(gc,GL,GU);hl,hu=interval(hc,HBL,HBU)
            LL[i][j]=LL[j][i]=down(gl-hu);LU[i][j]=LU[j][i]=up(gu-hl)
    weights=[sqrtup(sourceHi[i][i]) for i in range(7)]
    LLo,LHi,Lerr=loewner(LL,LU,weights)
    # Nominal residual = Z_native + q_new * Y_new. Aggregate the exact
    # carrier coefficients first so old action/source cancellation is paid.
    Z=add(mm(W,add(Y,X,-1)),mm(T,Y[:5]))
    Zframe=mm(Wi,Z)
    QNL=mat(cross,'new_trial_old_source_pairing_lower');QNU=mat(cross,'new_trial_old_source_pairing_upper')
    ql,qu=mat(new,'trial_source_pairing_entry_lower'),mat(new,'trial_source_pairing_entry_upper')
    QNL=[QNL[i]+ql[i] for i in range(2)];QNU=[QNU[i]+qu[i] for i in range(2)]
    RNL,RNU=mat(new,'trial_Gram_entry_lower'),mat(new,'trial_Gram_entry_upper')
    NL=[[F(0)]*7 for _ in range(7)];NU=[[F(0)]*7 for _ in range(7)]
    for i in range(7):
        for j in range(i,7):
            gl,gu=interval([[Z[a][i]*Z[b][j] for b in range(7)] for a in range(7)],GL,GU)
            ql,qu=interval([[Y[a+5][i]*Zframe[b][j]+Y[a+5][j]*Zframe[b][i] for b in range(7)] for a in range(2)],QNL,QNU)
            rl,ru=interval([[Y[a+5][i]*Y[b+5][j] for b in range(2)] for a in range(2)],RNL,RNU)
            NL[i][j]=NL[j][i]=down(gl+ql+rl);NU[i][j]=NU[j][i]=up(gu+qu+ru)
    _,NHi,Nerr=loewner(NL,NU,weights)
    assert psd(NHi)
    actionBound=F(actions['full_seven_source_action_error_relative_Gram_upper'])
    EHi=[[actionBound*x for x in row] for row in cong(Y,frameLo)]
    # Compare complete variational upper candidates to the structural upper.
    structuralLo=[[x/2 for x in row] for row in sourceLo]
    def width(gap):
        def yes(n):return psd(add([[F(n,10**6)*x for x in row] for row in sourceLo],gap,-1))
        hi=1
        while not yes(hi):hi*=2;assert hi<10**15
        lo=0
        while hi-lo>1:
            mid=(lo+hi)//2
            if yes(mid):hi=mid
            else:lo=mid
        assert yes(hi) and not yes(lo)
        return F(hi,10**6)
    lower=LLo if psd(LLo) else structuralLo
    candidates=[];best=None
    for tau in ([F(1,4),F(1,2),F(1),F(2),F(4)] if not reverse else [F(4),F(2),F(1),F(1,2),F(1,4)]):
        residual=add([[(1+tau)*x for x in row] for row in NHi],[[(1+1/tau)*x for x in row] for row in EHi])
        upper=add(LHi,residual);gap=add(upper,lower,-1)
        assert psd(gap)
        beta=width(gap);candidates.append(dict(tau=str(tau),relative_width_upper=str(beta)))
        if best is None or (beta,tau)<best[0]:best=((beta,tau),upper,residual)
    structuralWidth=width(add(sourceHi,lower,-1))
    if structuralWidth<best[0][0]:beta=structuralWidth;upper=sourceHi;selected='structural upper after full variational audit'
    else:beta=best[0][0];upper=best[1];selected='paid full variational upper'
    gap=add(upper,lower,-1);assert psd(lower) and psd(gap)
    assert psd(add([[beta*x for x in row] for row in sourceLo],gap,-1))
    # An exact witness locates failure of this enclosure's half-Gram gate.
    test=add([[F(1,2)*x for x in row] for row in sourceLo],gap,-1)
    witness=None
    if not psd(test):
        strongest=max(range(7),key=lambda k:gap[k][k]/sourceLo[k][k])
        if test[strongest][strongest]<0:witness=[F(i==strongest) for i in range(7)]
        for k in range(7):
            if witness is not None:break
            if test[k][k]<0:witness=[F(i==k) for i in range(7)];break
            prefix=[r[:k+1] for r in test[:k+1]]
            if not psd(prefix):
                previous=[r[:k] for r in test[:k]]
                coeff=mm(inv(previous),[[test[i][k]] for i in range(k)])
                witness=[-v[0] for v in coeff]+[F(1)]+[F(0)]*(6-k);break
        assert witness is not None
        quad=lambda M:sum(witness[i]*M[i][j]*witness[j] for i in range(7) for j in range(7))
        assert quad(test)<0
        witnessRatio=str(quad(gap)/quad(sourceLo))
    else:witnessRatio=None
    Xi=inv(X);nativeInverse=Wi
    nativeLower=cong(mm(Xi,nativeInverse),lower);nativeUpper=cong(mm(Xi,nativeInverse),upper)
    assert psd(nativeLower)
    candidates.sort(key=lambda d:F(d['tau']))
    return dict(milestone='RC158',status='PASS: complete positive seven-source inverse enclosure and exact width audit',
        starting_commit='fe3375694afaad01a879f069fff8b18a3df630f4',input_sha256=hs,aperture='11/10',
        source_order=actions['source_frame'],conditioned_source_transform=ser(X),trial_source_frame_coefficients=ser(Y),
        conditioned_source_Gram_lower=ser(sourceLo),conditioned_source_Gram_upper=ser(sourceHi),
        conditioned_variational_entry_lower=ser(LL),conditioned_variational_entry_upper=ser(LU),
        conditioned_variational_Loewner_lower=ser(LLo),conditioned_variational_Loewner_upper=ser(LHi),
        variational_interval_error_diagonal=list(map(str,Lerr)),
        nominal_residual_Gram_Loewner_upper=ser(NHi),nominal_residual_interval_error_diagonal=list(map(str,Nerr)),
        joint_action_error_Gram_Loewner_upper=ser(EHi),variational_width_candidates=candidates,
        structural_upper_width_after_selected_lower=str(structuralWidth),selected_upper=selected,
        variational_lower_psd_verified=psd(LLo),selected_lower_uses_structural_half_Gram=not psd(LLo),
        conditioned_reference_response_Loewner_lower=ser(lower),conditioned_reference_response_Loewner_upper=ser(upper),
        native_carrier_reference_response_Loewner_lower=ser(nativeLower),native_carrier_reference_response_Loewner_upper=ser(nativeUpper),
        relative_source_Gram_inverse_matrix_width_upper=str(beta),seven_source_inverse_response_certified=True,
        source_Gram_enclosure_relative_width_upper=str(width(add(sourceHi,sourceLo,-1))),
        half_Gram_inverse_width_gate_passed=psd(test),enclosure_width_failure_witness=None if witness is None else list(map(str,witness)),
        enclosure_width_witness_over_source_Gram_lower=witnessRatio,
        true_inverse_uncertainty_lower_bound_inferred=False,
        required_Stage_I_matrix_tolerance_specified=False,
        original_Weil_or_augmented_actions_performed=False,
        whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
        next_cursor='refine correlated source Gram tails and conditioned endpoint functional intervals; recheck full inverse width, retaining separate action and inverse gates')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=8)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC158 PASS: seven-source inverse enclosure and matrix-width audit')
