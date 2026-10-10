"""RC37 exact endpoint-zero trial control and certified canonical error increase."""
from validate_rpb108_rc31_trial_riesz import inverse,mm,psd
from validate_rpb108_rc36_mixed_residual_gram import build_forms,pairing
from validate_rpb108_rc30_interval_metric import I,loctx,hictx
from fractions import Fraction as F
from pathlib import Path
import json,sys,hashlib

DEN=10**12
def down(q): return F(q.numerator*DEN//q.denominator,DEN)
def up(q): return -down(-q)

def run(metric_path,prior_path):
    raw=Path(metric_path).read_bytes(); data=json.loads(raw)
    prior=json.loads(Path(prior_path).read_text())
    assert (data['trial_dimension'],data['target_dimension'])==(16,8)
    assert prior['metric_certificate_sha256']==hashlib.sha256(raw).hexdigest()
    G=[[F(x) for x in r] for r in data['metric_center']]
    V=[[F(x) for x in r] for r in data['coefficients']]
    mass=list(map(F,data['physical_mass'])); E=F(data['mass_metric_error_upper'])
    assert E<F(1,1000)
    assert psd([[G[i][j]-(1-E)*mass[i]*(i==j) for j in range(16)] for i in range(16)])
    rhs=[[mass[i] if i==j else F(0) for j in range(8)] for i in range(16)]
    assert mm(G,V)==rhs
    assert all(V[i][j]==0 for i in range(16) for j in range(8) if (i-j)%2)
    b=[[F(i%2==q) for q in range(2)] for i in range(16)]
    H=mm(inverse(G),b)
    denominators=[sum(H[i][q] for i in range(16) if i%2==q) for q in range(2)]
    assert all(x>0 for x in denominators)
    W=[[H[i][q]/denominators[q] for q in range(2)] for i in range(16)]
    traces=[sum(V[i][j] for i in range(16)) for j in range(8)]
    assert all(x!=0 for x in traces)
    U=[[V[i][j]-traces[j]*W[i][j%2] for j in range(8)] for i in range(16)]
    assert all(sum(U[i][j] for i in range(16))==0 for j in range(8))
    assert all(sum((-1)**i*U[i][j] for i in range(16))==0 for j in range(8))
    assert all(U[i][j]==0 for i in range(16) for j in range(8) if (i-j)%2)
    GU=mm(G,U)
    assert GU==[[rhs[i][j]-traces[j]/denominators[j%2]*b[i][j%2]
                 for j in range(8)] for i in range(16)]
    columns=[]; all_zero_map_lower=F(0)
    for j in range(8):
        # Actual squared Riesz error = ||r_j||_canonical^2 -2 ell_j(v)
        # + v^*G_actual v. The unknown first term cancels in the difference.
        nominal=sum((U[i][j]*GU[i][j]-V[i][j]*rhs[i][j] for i in range(16)),F(0))
        nominal-=2*mass[j]*(U[j][j]-V[j][j])
        assert nominal==traces[j]**2/denominators[j%2]
        budget=E*sum((mass[i]*(U[i][j]**2+V[i][j]**2) for i in range(16)),F(0))
        lower=nominal-budget
        assert lower>F(1,200)  # every target loses >0.005 in squared error
        old_physical_sq=sum((mass[i]*V[i][j]**2 for i in range(16)),F(0))
        # For any endpoint-zero trial u, put z=u-v_j. Nominal constrained
        # minimization gives z*G_hat*z >= nominal. Also ||u||_M^2 <=
        # 2||z||_M^2+2||v_j||_M^2 and G_hat >= (1-E)M. These bound
        # actual error increase uniformly over the whole constrained space.
        all_zero_lower=(1-3*E)/(1-E)*nominal-3*E*old_physical_sq
        assert all_zero_lower>F(1,200)
        all_zero_map_lower=max(all_zero_map_lower,all_zero_lower/mass[j])
        columns.append(dict(column=j,old_endpoint_trace=str(traces[j]),
            nominal_squared_error_increase_lower=str(down(nominal)),
            metric_uncertainty_budget_upper=str(up(budget)),
            actual_canonical_squared_error_increase_lower=str(down(lower)),
            any_endpoint_zero_trial_canonical_squared_error_increase_lower=str(down(all_zero_lower))))
    # One whole physical source-residual lower bound is sufficient to refute
    # improvement of the collective physical residual map over RC36.
    forms,mom,R,delta=build_forms(U)
    norm=pairing(forms[0],forms[0],mom,R)
    assert norm.l>0 and hictx.subtract(norm.h,norm.l)<I(F(1,10**20)).h
    physical_sq=sum((mass[i]*U[i][0]**2 for i in range(16)),F(0))
    lowernorm=norm.sqrt()-I(delta)*I(physical_sq).sqrt()
    assert lowernorm.l>0
    squared=lowernorm*lowernorm
    floor=loctx.multiply(squared.l,I(DEN).l).to_integral_value(rounding='ROUND_FLOOR')
    physical_lower=F(int(floor),DEN)
    normalized_lower=physical_lower/mass[0]
    assert normalized_lower>F(prior['collective_physical_squared_upper'])
    assert all_zero_map_lower>F(prior['collective_canonical_squared_upper'])
    return dict(milestone='RC37',status='PASS',trial_dimension=16,target_dimension=8,
        metric_certificate_sha256=hashlib.sha256(raw).hexdigest(),
        construction='parity-preserving nominal-metric endpoint-zero projection',
        endpoint_zero_coefficients=[[str(x) for x in r] for r in U],columns=columns,
        exact_both_endpoint_zero=True,nominal_constrained_stationarity=True,
        every_target_actual_canonical_squared_error_increase_lower='1/200',
        every_endpoint_zero_trial_in_fixed_space_error_increase_lower='1/200',
        any_endpoint_zero_collective_canonical_squared_lower=str(down(all_zero_map_lower)),
        previous_collective_canonical_squared_upper=prior['collective_canonical_squared_upper'],
        control_column=0,control_nominal_physical_squared_interval=norm.pair(),
        control_actual_physical_squared_lower=str(physical_lower),
        collective_physical_squared_lower=str(normalized_lower),
        previous_collective_physical_squared_upper=prior['collective_physical_squared_upper'],
        endpoint_zero_strategy_improves_certified_trials=False,
        native_head_certified=False,aperture_extended=False)

if __name__=='__main__':
    root=Path(__file__).parent.parent/'certificates'
    metric=sys.argv[1] if len(sys.argv)>1 else root/'rpb108_rc35_enriched_metric.json'
    previous=sys.argv[2] if len(sys.argv)>2 else root/'rpb108_rc36_mixed_residual_gram.json'
    print(json.dumps(run(metric,previous),indent=2))
