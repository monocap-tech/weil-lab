"""RC59: 22-feature actual native Gram, inverse envelope and trial interface.

Ritz lower bounds use the corrected actual 32-mode canonical trial metric;
the global physical embedding gives the upper bound. No enlarged Weil
head positivity or source-residual threshold is asserted.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,sys
from validate_rpb108_rc29_atom_reduction import legendre,add
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,entries,root,intersect,rows
from validate_rpb108_rc56_precision_attached_head import DC0
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound

N=22;TRIAL=32

def chebyshev_conversion(n):
    polys=[[F(1)],[F(0),F(1)]]
    for j in range(1,n-1):polys.append(add([F(0)]+[2*x for x in polys[-1]],[-x for x in polys[-2]]))
    C=[[F(0)]*n for _ in range(n)]
    for j in range(n):
        rem=polys[j][:]
        for i in range(j,-1,-1):
            p=legendre(i);C[i][j]=rem[i]/p[i]
            for k,x in enumerate(p):rem[k]-=C[i][j]*x
        assert all(x==0 for x in rem) and C[j][j]>0
    assert all(C[i][j]==0 for i in range(n) for j in range(n) if (i-j)%2)
    return C,polys

def nearest(x,den):
    a=x*den+F(1,2);return F(a.numerator//a.denominator,den)

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths]
    metric,native,precision,floor,leakage=[json.loads(x) for x in raw]
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert native['metric_certificate_sha256']==hashes[0]
    assert [precision['input_sha256'][k] for k in [1,0]]==hashes[:2]
    assert floor['input_sha256'][6]==hashes[2]
    assert [leakage['input_sha256'][k] for k in [1,0,5,6]]==hashes[:4]
    assert leakage['necessary_consecutive_native_head_count_for_revised_source_gate_lower']==N
    G=matrix(metric['metric_center']);mass=list(map(F,metric['physical_mass']))
    assert len(G)==TRIAL and len(mass)==TRIAL
    D=[[mass[i]*(i==j) for j in range(TRIAL)] for i in range(TRIAL)]
    assert psd([[G[i][j]-D[i][j] for j in range(TRIAL)] for i in range(TRIAL)])
    identity=[[F(i==j) for j in range(TRIAL)] for i in range(TRIAL)]
    GI=inverse(G);assert mm(G,GI)==mm(GI,G)==identity
    corrected=2*(abs(F(precision['constant_center_shift']))+F(precision['constant_radius']))+F(metric['mass_metric_error_upper'])-2*DC0
    eps=F(1,10000000);assert 0<corrected<eps
    # Gactual<=G+eps D<=(1+eps)G, so its inverse is >=GI/(1+eps).
    C,polys=chebyshev_conversion(N)
    assert [r[:8] for r in C[:8]]==matrix(native['chebyshev_to_legendre'])
    rhs=[[mass[i]*C[i][j] if i<N else F(0) for j in range(N)] for i in range(TRIAL)]
    P=mm(mm(tr(C),[[mass[i]*(i==j) for j in range(N)] for i in range(N)]),C)
    A=mm(mm(tr(rhs),GI),rhs)
    exact_lower=[[x/(1+eps) for x in row] for row in A]
    Mlo,roundL=rounded_bound(exact_lower,-1,10**20)
    rho=F(252,257);Mup=[[rho*x for x in row] for row in P]
    alpha=F(3,10)
    assert psd([[Mlo[i][j]-alpha*P[i][j] for j in range(N)] for i in range(N)])
    assert psd([[Mup[i][j]-Mlo[i][j] for j in range(N)] for i in range(N)])
    assert [r[:8] for r in P[:8]]==matrix(native['physical_native_Gram'])
    mid=[[(Mlo[i][j]+Mup[i][j])/2 for j in range(N)] for i in range(N)]
    center=[[nearest(x,10**18) for x in row] for row in mid]
    rd=[sum((abs(center[i][j]-mid[i][j]) for j in range(N)),F(0)) for i in range(N)]
    Err=[[(Mup[i][j]-Mlo[i][j])/2+(i==j)*rd[i] for j in range(N)] for i in range(N)]
    eta=F(11,20)
    assert psd([[eta*center[i][j]-Err[i][j] for j in range(N)] for i in range(N)])
    assert psd(center) and center==tr(center)
    CI=inverse(center);ident22=[[F(i==j) for j in range(N)] for i in range(N)]
    assert mm(center,CI)==mm(CI,center)==ident22
    inverse_lo=[[x/(1+eta) for x in row] for row in CI]
    inverse_up=[[x/(1-eta) for x in row] for row in CI]
    oldM=entries(precision['refined_actual_native_Gram_entry_enclosures']);E={}
    for i in range(N):
        for j in range(i,N):
            if (i-j)%2:E[i,j]=(F(0),F(0));continue
            rad=root(Err[i][i]*Err[j][j]);value=(center[i][j]-rad,center[i][j]+rad)
            E[i,j]=intersect(value,oldM[i,j]) if j<8 else value
    # Generate all 22 Legendre target trials with the same rounded solve
    # rule as RC38. The original eight coefficient columns are preserved.
    leg_rhs=[[mass[i]*(i==j) for j in range(N)] for i in range(TRIAL)]
    exact_trials=mm(GI,leg_rhs)
    leg_trials=[[nearest(x,10**30) for x in row] for row in exact_trials]
    assert [r[:8] for r in leg_trials]==matrix(metric['coefficients'])
    V=mm(leg_trials,C);assert [r[:8] for r in V]==matrix(native['native_trial_coefficients'])
    GT=mm(mm(tr(V),G),V);T=mm(mm(tr(V),D),V);J=mm(tr(rhs),V)
    # Actual M=J+J*-GTactual+E*E, hence a safe whole-map error upper.
    Ec=[[Mup[i][j]-J[i][j]-J[j][i]+GT[i][j]+eps*T[i][j] for j in range(N)] for i in range(N)]
    assert psd(Ec)
    Ep=[[rho*x for x in row] for row in Ec]
    if replay:
        # Direct physical polynomial integration independently reconstructs P.
        for i in range(N):
            for j in range(N):
                value=sum((x*y*F(11,10)*F(2,a+b+1) for a,x in enumerate(polys[i])
                    for b,y in enumerate(polys[j]) if (a+b)%2==0),F(0))
                assert value==P[i][j]
                ritz=sum((rhs[a][i]*GI[a][b]*rhs[b][j] for a in range(TRIAL) for b in range(TRIAL)),F(0))
                assert ritz==A[i][j]
        assert psd([[(1+eta)*center[i][j]-Mup[i][j] for j in range(N)] for i in range(N)])
        assert psd([[Mlo[i][j]-(1-eta)*center[i][j] for j in range(N)] for i in range(N)])
        assert all(abs(leg_trials[i][j]-exact_trials[i][j])<=F(1,2*10**30) for i in range(TRIAL) for j in range(N))
    return dict(milestone='RC59',status='PASS',input_sha256=hashes,cap='11/10',native_features_certified=list(range(N)),
        trial_dimension=TRIAL,corrected_actual_metric_error_before_coarsening=str(corrected),
        actual_metric_error_upper_used=str(eps),chebyshev_to_legendre=serialize(C),
        physical_native_Gram=serialize(P),actual_canonical_native_Gram_Loewner_lower=serialize(Mlo),
        actual_canonical_native_Gram_Loewner_upper=serialize(Mup),
        actual_canonical_native_Gram_physical_lower_factor=str(alpha),
        actual_canonical_native_Gram_physical_upper_factor=str(rho),
        physical_Gram_preconditioned_actual_metric_condition_number_upper=str(rho/alpha),
        rational_native_Gram_center=serialize(center),relative_actual_Gram_center_error_upper=str(eta),
        exact_rational_center_inverse=serialize(CI),actual_native_Gram_inverse_Loewner_lower=serialize(inverse_lo),
        actual_native_Gram_inverse_Loewner_upper=serialize(inverse_up),
        center_preconditioned_actual_metric_condition_number_upper=str((1+eta)/(1-eta)),
        actual_native_Gram_entry_enclosures=rows(E),Ritz_lower_rounding_diagonal_allowances=list(map(str,roundL)),
        center_rounding_diagonal_allowances=list(map(str,rd)),
        native_trial_coefficients=serialize(V),physical_native_trial_Gram=serialize(T),
        actual_canonical_Riesz_error_Gram_Loewner_upper=serialize(Ec),
        actual_physical_Riesz_error_Gram_Loewner_upper=serialize(Ep),
        original_eight_trial_columns_preserved_exactly=True,original_low_eight_metric_enclosures_intersected=True,
        actual_orthogonal_projection_rank_certified=N,
        actual_projection_characterization='Pi22 u = R22 M22_inverse R22_star u; kernel is the first 22 physical native moments',
        actual_projection_Gram_and_inverse_enclosures_certified=True,exact_actual_projection_coefficients_evaluated=False,
        enlarged_original_Weil_head_floor_certified=False,enlarged_projected_source_threshold_certified=False,
        retained_actual_low_eight_Weil_floor=floor['original_Weil_uniform_low_eight_canonical_floor_lower'],
        full_1250_native_projection_constructed=False,whole_aperture_positivity_extended=False,RH=False,F4=False)

if __name__=='__main__':
    base=Path(__file__).parent.parent/'certificates'
    defaults=[base/n for n in ['rpb108_rc38_thirty_two_metric.json','rpb108_rc39_native_low_chebyshev_gram.json',
        'rpb108_rc56_precision_attached_head.json','rpb108_rc57_uniform_low_head_floor.json',
        'rpb108_rc58_complementary_source_leakage.json']]
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True)==saved
        print('PASS: direct Chebyshev mass integration, scalar Ritz reconstruction, actual Gram bounds and exact inverse envelope, 22 trials with unchanged low-eight prefix')
    else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
