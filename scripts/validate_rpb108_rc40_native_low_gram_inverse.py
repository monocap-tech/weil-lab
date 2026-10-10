"""RC40 validated inverse enclosure for the actual first eight native Gram entries."""
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from fractions import Fraction as F
from pathlib import Path
import json,sys,hashlib

def run(path):
    raw=Path(path).read_bytes(); data=json.loads(raw)
    assert data['actual_low_native_Gram_certified'] and data['native_features_certified']==list(range(8))
    P=[[F(x) for x in r] for r in data['physical_native_Gram']]
    N=[[F(x) for x in r] for r in data['canonical_native_Gram_enclosure_center']]
    tau=F(data['normalized_center_error_upper'])
    mu=F(1,8)
    assert P==tr(P) and N==tr(N)
    assert psd([[P[i][j]-mu*(i==j) for j in range(8)] for i in range(8)])
    den=10**12
    def rounded(q):
        scaled=q*den+F(1,2)
        return F(scaled.numerator//scaled.denominator,den)
    Q=[[rounded(x) for x in r] for r in N]
    assert Q==tr(Q)
    h=max(abs(Q[i][j]-N[i][j]) for i in range(8) for j in range(8))
    assert h<=F(1,2*den)
    assert all(Q[i][j]==N[i][j]==0 for i in range(8) for j in range(8) if (i-j)%2)
    # ||Q-N|| <=8h, and P>=mu I, so the rounding error is <=8h/mu
    # in the exact physical Chebyshev Gram. Combine with RC39's actual bound.
    rounding_error=8*h/mu
    total_error=tau+rounding_error
    def accepts(gamma):
        return psd([[Q[i][j]-gamma*P[i][j] for j in range(8)] for i in range(8)])
    low=F(0); high=F(1)
    assert accepts(low) and not accepts(high)
    for _ in range(40):
        mid=(low+high)/2
        if accepts(mid): low=mid
        else: high=mid
    gamma=low; assert gamma>0 and accepts(gamma)
    eta=total_error/gamma
    assert 0<eta<F(11,5000)
    B=inverse(Q); identity=[[F(i==j) for j in range(8)] for i in range(8)]
    assert B==tr(B) and mm(Q,B)==mm(B,Q)==identity and psd(B)
    lower=F(1)/(1+eta); upper=F(1)/(1-eta)
    inverse_error=eta/(1-eta)
    assert inverse_error<F(1,450)
    assert psd([[B[i][j]-lower*B[i][j] for j in range(8)] for i in range(8)])
    assert psd([[upper*B[i][j]-B[i][j] for j in range(8)] for i in range(8)])
    return dict(milestone='RC40',status='PASS',native_features_certified=list(range(8)),
        source_certificate_sha256=hashlib.sha256(raw).hexdigest(),
        physical_native_Gram=[[str(x) for x in r] for r in P],
        physical_native_Gram_Euclidean_lower=str(mu),
        rational_Gram_center=[[str(x) for x in r] for r in Q],
        rational_center_inverse=[[str(x) for x in r] for r in B],
        center_entry_rounding_error_upper=str(h),physical_rounding_error_upper=str(rounding_error),
        total_physical_Gram_error_upper=str(total_error),
        rational_center_physical_lower_factor=str(gamma),relative_Gram_error_upper=str(eta),
        actual_inverse_lower_multiplier=str(lower),actual_inverse_upper_multiplier=str(upper),
        center_normalized_inverse_error_upper=str(inverse_error),
        actual_native_metric_relative_solve_error_upper=str(eta),
        exact_center_inverse_verified=True,actual_low_native_inverse_enclosed=True,
        exact_actual_native_inverse_evaluated=False,complete_native_Gram_certified=False,
        native_remainder_sources_certified=False,original_Weil_head_floor_certified=False,
        aperture_extended=False)

if __name__=='__main__':
    path=sys.argv[1] if len(sys.argv)>1 else Path(__file__).parent.parent/'certificates/rpb108_rc39_native_low_chebyshev_gram.json'
    print(json.dumps(run(path),indent=2))
