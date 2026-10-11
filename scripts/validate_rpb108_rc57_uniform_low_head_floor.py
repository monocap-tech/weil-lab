"""RC57: whole low-eight positivity from correlated original-source errors.

All matrix acceptance checks use exact rational arithmetic. RC56 supplies
the certified precision attachment; RC44 supplies the 1250-complement floor.
The new 1250 Schur gate is conditional and is not a low-eight tail claim.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,sys
from validate_rpb108_rc31_trial_riesz import mm,tr,psd,inverse
from validate_rpb108_rc47_correlated_native_transport import matrix,entries,serialize
from validate_rpb108_rc55_weak_head_schur import block,sub
from validate_rpb108_rc56_precision_attached_head import DC0

def rounded_bound(A,sign,den=10**30):
    """Symmetric entry rounding with diagonal row-sum Loewner transport."""
    n=len(A);C=[[F(0)]*n for _ in range(n)];R=[[F(0)]*n for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            a=A[i][j]*den;low=a.numerator//a.denominator
            high=-(-a.numerator//a.denominator)
            C[i][j]=C[j][i]=F(low+high,2*den)
            R[i][j]=R[j][i]=F(high-low,2*den)
    bound=[[C[i][j]+sign*(i==j)*sum(R[i],F(0)) for j in range(n)] for i in range(n)]
    assert psd(sub(bound,A) if sign==1 else sub(A,bound))
    return bound,[sum(row,F(0)) for row in R]

def ldl_pivots(A):
    B=[r[:] for r in A];out=[]
    for k in range(len(B)):
        pivot=B[k][k];assert pivot>0;out.append(pivot)
        for i in range(k+1,len(B)):
            for j in range(k+1,len(B)):B[i][j]-=B[i][k]*B[k][j]/pivot
    return out

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths]
    native,metric,transport,prime,complete,head,precision,reduced=[json.loads(x) for x in raw]
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert [precision['input_sha256'][k] for k in [0,1,3,4,6,7]]==hashes[:6]
    assert reduced['prime_certificate_sha256']==hashes[3]
    assert precision['proposed_one_over_4000_low_head_floor_ruled_out']
    P=matrix(native['physical_native_Gram']);V=matrix(native['native_trial_coefficients'])
    T=matrix(prime['physical_native_trial_Gram']);G=matrix(metric['metric_center'])
    GT=mm(mm(tr(V),G),V);H=entries(complete['nominal_complete_signed_remainder_head_entry_enclosures'])
    Qr=matrix(transport['nominal_native_residual_Gram_Loewner_upper'])
    U=matrix(head['nominal_physical_original_source_Gram_Loewner_upper'])
    rho=F(252,257);shift=F(precision['constant_center_shift'])
    deltaR=F(precision['residual_error_from_old_nominal_forms_upper'])
    deltaS=F(precision['source_error_from_old_nominal_forms_upper'])
    deltaH=F(precision['combined_recentered_trial_head_operator_error_upper'])
    deltaG=2*(abs(shift)+F(precision['constant_radius']))+F(metric['mass_metric_error_upper'])-2*DC0
    k=list(map(F,complete['complete_physical_operator_parity_norm_upper']))
    t=F(1,256);u=F(1,65536);s=F(42)
    # Whole-map Young bounds; preserve all source/residual correlations.
    B=[[ (1+t)*Qr[i][j]+(1+1/t)*deltaR**2*T[i][j] for j in range(8)] for i in range(8)]
    Ua=[[(1+u)*U[i][j]+(1+1/u)*deltaS**2*T[i][j] for j in range(8)] for i in range(8)]
    assert psd(B) and psd(Ua)
    N=[[GT[i][j]+sum(H[tuple(sorted((i,j)))])/2+shift*T[i][j] for j in range(8)] for i in range(8)]
    Rh=[[(H[tuple(sorted((i,j)))][1]-H[tuple(sorted((i,j)))][0])/2 for j in range(8)] for i in range(8)]
    D=[sum(row,F(0)) for row in Rh]
    for A in [P,T,Qr,U,B,Ua,N]:
        assert A==tr(A)
        assert all(A[i][j]==0 for i in range(8) for j in range(8) if (i-j)%2)
    # Q>=N-deltaH T-D-rho B-rho^2(s+k_parity)B-Ua/s.
    # The rho B term pays the negative canonical Riesz Gram exactly once.
    Lpre=[[N[i][j]-deltaH*T[i][j]-(i==j)*D[i]
        -rho*B[i][j]-rho*rho*(s+k[i%2])*B[i][j]-Ua[i][j]/s
        for j in range(8)] for i in range(8)]
    C=matrix(native['chebyshev_to_legendre']);mass=list(map(F,metric['physical_mass']))
    J=mm(tr(C),[[mass[i]*V[i][j] for j in range(8)] for i in range(8)])
    # M=J+J*-Gtrial_actual+E*E; |Gtrial_actual-Gnom|<=deltaG T.
    Mpre=[[J[i][j]+J[j][i]-GT[i][j]+deltaG*T[i][j]+rho*B[i][j] for j in range(8)] for i in range(8)]
    L,roundL=rounded_bound(Lpre,-1);Mup,roundM=rounded_bound(Mpre,1)
    assert psd(Mup)
    h=F(1,2900000)
    target=[[L[i][j]-h*Mup[i][j] for j in range(8)] for i in range(8)]
    assert psd(target)
    parity=[]
    for S,W in [([0,6],[2,4]),([1,7],[3,5])]:
        A=block(target,S,S);X=block(target,S,W);Z=block(target,W,W)
        AI=inverse(A);Schur=sub(Z,mm(mm(tr(X),AI),X))
        pivots=ldl_pivots(block(target,S+W,S+W))
        assert psd(Schur) and Schur[0][0]>0
        det=Schur[0][0]*Schur[1][1]-Schur[0][1]**2;assert det>0
        if replay:
            # Independent 2x2 adjugate inverse and completion of squares.
            ad=A[0][0]*A[1][1]-A[0][1]**2;assert ad>0
            adj=[[A[1][1]/ad,-A[0][1]/ad],[-A[0][1]/ad,A[0][0]/ad]]
            assert AI==adj
            assert Z==[[Schur[i][j]+sum((X[a][i]*AI[a][b]*X[b][j]
                for a in range(2) for b in range(2)),F(0)) for j in range(2)] for i in range(2)]
        parity.append(dict(strong_features=S,weak_features=W,
            positive_LDL_pivots=list(map(str,pivots)),target_weak_Schur=serialize(Schur),
            target_weak_Schur_determinant=str(det)))
    if replay:
        # Independently reconstruct trial and error matrices entry by entry.
        for i in range(8):
            for j in range(8):
                assert GT[i][j]==sum((V[a][i]*G[a][b]*V[b][j] for a in range(32) for b in range(32)),F(0))
                assert T[i][j]==sum((mass[a]*V[a][i]*V[a][j] for a in range(32)),F(0))
                assert s*rho*rho*B[i][j]+Ua[i][j]/s==s*rho*rho*((1+t)*Qr[i][j]
                    +(1+1/t)*deltaR**2*T[i][j])+((1+u)*U[i][j]+(1+1/u)*deltaS**2*T[i][j])/s
        assert psd(sub(Lpre,L)) and psd(sub(Mup,Mpre))
        assert all(x>0 for x in ldl_pivots(target))
    tail=F(reduced['preserved_original_complement_floor']);cross=F(1,8000);gamma=cross**2
    reserve=h-gamma/tail;assert reserve>h/2>0
    oldgamma=F(reduced['conditional_actual_source_cross_norm'])**2
    assert oldgamma/gamma==F(6400,9)
    return dict(milestone='RC57',status='PASS',input_sha256=hashes,native_features_certified=list(range(8)),
        physical_residual_Young_parameter=str(t),original_source_Young_parameter=str(u),
        linear_Riesz_source_Young_parameter=str(s),
        actual_original_Weil_low_head_Loewner_lower=serialize(L),
        actual_canonical_native_Gram_Loewner_upper=serialize(Mup),
        lower_head_rounding_diagonal_allowances=list(map(str,roundL)),
        upper_metric_rounding_diagonal_allowances=list(map(str,roundM)),
        original_Weil_uniform_low_eight_canonical_floor_lower=str(h),
        full_low_eight_original_Weil_head_floor_certified=True,
        target_lower_matrix_L_minus_h_Mupper=serialize(target),parity_target_Schur_certificates=parity,
        retained_uniform_head_floor_upper=precision['any_uniform_low_eight_canonical_head_floor_upper'],
        proposed_one_over_4000_floor_remains_ruled_out=True,
        conditional_1250_gate=dict(feature_count=reduced['Chebyshev_feature_count'],
            required_actual_head_floor=str(h),required_actual_canonical_source_residual_relative_Gram_upper=str(gamma),
            required_source_cross_norm_upper=str(cross),inherited_actual_complement_floor=str(tail),
            resulting_head_Schur_reserve=str(reserve),squared_source_target_tightening_factor=str(oldgamma/gamma),
            actual_1250_head_floor_certified=False,actual_1250_source_residual_certified=False,
            gate_is_sufficient_conditional_only=True),
        complement_floor_applies_to_1250_orthogonal_complement_not_low_eight=True,
        retained_low_eight_source_residual_relative_Gram_upper=precision['retained_low_eight_canonical_source_residual_relative_native_metric_upper'],
        full_1250_native_projection_constructed=False,whole_aperture_positivity_extended=False,RH=False,F4=False)

if __name__=='__main__':
    base=Path(__file__).parent.parent/'certificates'
    defaults=[base/n for n in ['rpb108_rc39_native_low_chebyshev_gram.json','rpb108_rc38_thirty_two_metric.json',
        'rpb108_rc47_correlated_native_transport.json','rpb108_rc43_native_prime_head.json',
        'rpb108_rc52_complete_source_covariance.json','rpb108_rc54_original_source_cancellation.json',
        'rpb108_rc56_precision_attached_head.json','rpb108_rc44_reduced_native_head.json']]
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        cert=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True)==cert
        print('PASS: scalar Gram reconstruction, outward Loewner rounding, positive rational LDL and adjugate Schur replay, conditional 1250 gate')
    else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
