"""RC53: paid variational bound for the actual canonical P8 source residual."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,entries,serialize
from validate_rpb108_rc49_prime_pole_covariance import relative_upper

def add(A,B,scale=F(1)):
    return [[A[i][j]+scale*B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths]
    native,solve,transport,prime,metric,complete=[json.loads(x) for x in raw]
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert solve['source_certificate_sha256']==hashes[0]
    assert [transport['input_sha256'][k] for k in [0,2,4]]==[hashes[k] for k in [4,0,3]]
    assert [complete['input_sha256'][k] for k in [0,1,3]]==[hashes[k] for k in [0,3,2]]
    assert native['metric_certificate_sha256']==hashes[4]
    assert complete['complete_nominal_archimedean_prime_pole_trial_covariance_evaluated']
    P=matrix(native['physical_native_Gram']);V=matrix(native['native_trial_coefficients'])
    T=matrix(prime['physical_native_trial_Gram']);G=matrix(metric['metric_center'])
    mass=list(map(F,metric['physical_mass']))
    assert T==mm(mm(tr(V),[[mass[i]*(i==j) for j in range(32)] for i in range(32)]),V)
    rho=F(252,257);alpha=F(native['canonical_native_Gram_physical_lower_factor'])
    G0=matrix(solve['rational_Gram_center']);NI=matrix(solve['rational_center_inverse'])
    ident=[[F(i==j) for j in range(8)] for i in range(8)]
    assert mm(G0,NI)==mm(NI,G0)==ident and psd(G0)
    assert psd(add(G0,P,-F(solve['rational_center_physical_lower_factor'])))
    assert F(solve['relative_Gram_error_upper'])<F(11,5000)
    Q=matrix(complete['nominal_complete_signed_physical_source_Gram_Loewner_upper'])
    H=entries(complete['nominal_complete_signed_remainder_head_entry_enclosures'])
    H0=[[F(0)]*8 for _ in range(8)];Rh=[[F(0)]*8 for _ in range(8)]
    for (i,j),(a,b) in H.items():
        H0[i][j]=H0[j][i]=(a+b)/2;Rh[i][j]=Rh[j][i]=(b-a)/2
    L=mm(NI,H0);assert mm(G0,L)==H0
    assert all(L[i][j]==0 for i in range(8) for j in range(8) if (i-j)%2)
    Z=[[abs(x) for x in row] for row in L]
    D1=mm(tr(Z),Rh);D2=mm(Rh,Z)
    rounding=[[sum((D1[i][j]+D2[i][j] for j in range(8)),F(0))*(i==k) for k in range(8)] for i in range(8)]
    Emetric=F(metric['mass_metric_error_upper'])
    Gtrial=mm(mm(tr(V),G),V);Gup=add(Gtrial,T,Emetric)
    assert psd(Gup)
    # Y=i^*F_nom-V L. The canonical norm of i^*F_nom is bounded
    # by rho times its physical Gram; V's metric error remains paid.
    if replay:
        # Independent square completion around the trial metric minimizer.
        GI=inverse(Gup);Lopt=mm(GI,H0);D=add(L,Lopt,-1)
        Y=add(add([[rho*x for x in row] for row in Q],mm(mm(tr(H0),GI),H0),-1),
              mm(mm(tr(D),Gup),D))
    else:
        HL=mm(H0,L)
        Y=add(add(add([[rho*x for x in row] for row in Q],HL,-1),tr(HL),-1),mm(mm(tr(L),Gup),L))
    Y=add(Y,rounding);assert psd(Y)
    Ep=matrix(transport['actual_physical_Riesz_error_Gram_Loewner_upper'])
    Ec=matrix(transport['actual_canonical_Riesz_error_Gram_Loewner_upper'])
    assert Ep==[[rho*x for x in row] for row in Ec]
    k=list(map(F,complete['complete_physical_operator_parity_norm_upper']))
    delta=F(complete['archimedean_source_approximation_operator_error_upper'])
    if replay:
        S=[[k[i%2]*(i==j) for j in range(8)] for i in range(8)]
        phys=add([[F(33,32)*x for x in row] for row in mm(mm(S,Ep),S)],T,33*delta**2)
    else:
        phys=[[F(33,32)*k[i%2]*k[j%2]*Ep[i][j]+33*delta**2*T[i][j] for j in range(8)] for i in range(8)]
    assert psd(phys)
    EL=mm(mm(tr(L),Ec),L);assert psd(EL)
    candidates=[]
    for u in [F(1,16),F(1,8),F(1,4),F(1,2),F(1),F(2),F(4)]:
        error=add([[rho*(1+u)*x for x in row] for row in phys],EL,1+1/u)
        for t in [F(1,8),F(1,4),F(1,2),F(1),F(2),F(4)]:
            A=add([[(1+t)*x for x in row] for row in Y],error,1+1/t)
            candidates.append((relative_upper(A,P),u,t,A,error))
    lam,u,t,A,error=min(candidates,key=lambda x:x[0]);bound=lam/alpha
    prior=F(complete['whole_actual_complete_signed_source_Gram_relative_native_metric_upper'])
    assert bound<F(1619,500) and bound<prior
    assert prior/bound>F(233,200)
    assert psd(A) and psd(add([[lam*x for x in row] for row in P],A,-1))
    # P8 sigma is characterized by M c=R^* sigma. Any exact L gives
    # ||(I-P8)sigma a|| <= ||sigma a-R L a||. No approximate solve
    # is identified with the unknown actual orthogonal coefficients.
    # The original identity term R is in ran(P8), hence has zero residual.
    return dict(milestone='RC53',status='PASS',input_sha256=hashes,native_features_certified=list(range(8)),
        residual_source_feature_scope='native source columns 0 through 7 only',
        projection_target='canonical orthogonal projection onto actual native representatives 0 through 7',
        exact_rational_projection_trial_coefficients=serialize(L),
        nominal_trial_source_head_center=serialize(H0),nominal_trial_source_head_entry_halfwidths=serialize(Rh),
        head_rounding_variational_Gram_allowance=serialize(rounding),
        canonical_trial_Gram_Loewner_upper=serialize(Gup),
        nominal_variational_source_residual_Gram_Loewner_upper=serialize(Y),
        source_approximation_and_actual_physical_transfer_Gram_Loewner_upper=serialize(phys),
        canonical_Riesz_error_projection_coefficients_Gram_Loewner_upper=serialize(EL),
        complete_variational_error_Gram_Loewner_upper=serialize(error),
        actual_canonical_orthogonal_source_residual_Gram_Loewner_upper=serialize(A),
        actual_canonical_orthogonal_source_residual_Gram_relative_physical_native_Gram_upper=str(lam),
        whole_actual_canonical_orthogonal_source_residual_Gram_relative_native_metric_upper=str(bound),
        previous_unprojected_source_Gram_relative_native_metric_upper=str(prior),
        actual_error_split_Young_parameter=str(u),nominal_error_split_Young_parameter=str(t),
        canonical_orthogonal_residual_upper_bound_certified=True,
        exact_actual_projection_coefficients_evaluated=False,actual_canonical_source_Gram_evaluated=False,
        original_identity_source_term_projected_residual_zero=True,
        final_1250_projected_residual_gate_met=False,
        original_Weil_head_floor_certified=False,full_1250_native_projection_constructed=False,aperture_extended=False)

if __name__=='__main__':
    base=Path(__file__).parent.parent/'certificates'
    defaults=[base/name for name in ['rpb108_rc39_native_low_chebyshev_gram.json','rpb108_rc40_native_low_gram_inverse.json',
        'rpb108_rc47_correlated_native_transport.json','rpb108_rc43_native_prime_head.json',
        'rpb108_rc38_thirty_two_metric.json','rpb108_rc52_complete_source_covariance.json']]
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        cert=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True)==cert
        print('PASS: independent square-completion residual replay, exact trial solve, paid metric and Riesz errors, and canonical orthogonal residual PSD bound')
    else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
