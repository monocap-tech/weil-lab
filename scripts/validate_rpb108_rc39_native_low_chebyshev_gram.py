"""RC39 actual canonical Gram enclosures for the first eight native Chebyshev features."""
from validate_rpb108_rc31_trial_riesz import mm,tr,psd
from validate_rpb108_rc29_atom_reduction import legendre,add
from validate_rpb108_rc36_mixed_residual_gram import loewner_upper
from validate_rpb108_rc30_interval_metric import I,hictx,loctx
from fractions import Fraction as F
from pathlib import Path
import json,sys,hashlib

def lower_scalar(L,mass):
    def accepted(a):
        return psd([[L[i][j]-a*mass[i]*(i==j) for j in range(8)] for i in range(8)])
    low=F(0); high=F(1)
    assert accepted(low) and not accepted(high)
    for _ in range(40):
        mid=(low+high)/2
        if accepted(mid): low=mid
        else: high=mid
    assert low>0 and accepted(low)
    return low

def run(metric_path,residual_path):
    raw=Path(metric_path).read_bytes(); metric=json.loads(raw)
    residual=json.loads(Path(residual_path).read_bytes())
    assert residual['metric_certificate_sha256']==hashlib.sha256(raw).hexdigest()
    assert (metric['trial_dimension'],metric['target_dimension'])==(32,8)
    V=[[F(x) for x in r] for r in metric['coefficients']]
    G=[[F(x) for x in r] for r in metric['metric_center']]
    mass=list(map(F,metric['physical_mass'])); target=mass[:8]
    E=F(metric['mass_metric_error_upper']); beta=F(residual['collective_canonical_squared_upper'])
    rho=F(252,257)
    assert E<F(1,1000) and beta<F(1,500)
    D=[[target[i]*(i==j) for j in range(8)] for i in range(8)]
    J=[[target[i]*V[i][j] for j in range(8)] for i in range(8)]
    H=mm(mm(tr(V),G),V)
    T=mm(mm(tr(V),[[mass[i]*(i==j) for j in range(32)] for i in range(32)]),V)
    assert T==[[F(x) for x in r] for r in residual['trial_physical_Gram']]
    center=[[J[i][j]+J[j][i]-H[i][j] for j in range(8)] for i in range(8)]
    L=[[center[i][j]-E*T[i][j] for j in range(8)] for i in range(8)]
    U=[[center[i][j]+E*T[i][j]+beta*D[i][j] for j in range(8)] for i in range(8)]
    alpha=lower_scalar(L,target)
    tv=F(residual['trial_map_squared_upper'])
    assert psd([[tv*D[i][j]-T[i][j] for j in range(8)] for i in range(8)])
    tau=E*tv+beta/2
    middle=[[center[i][j]+beta*D[i][j]/2 for j in range(8)] for i in range(8)]
    # Exact Chebyshev-to-Legendre coefficient conversion.
    polys=[[F(1)],[F(0),F(1)]]
    for j in range(1,7): polys.append(add([F(0)]+[2*x for x in polys[-1]],[-x for x in polys[-2]]))
    C=[[F(0)]*8 for _ in range(8)]
    for j in range(8):
        remainder=polys[j][:]
        for i in range(j,-1,-1):
            p=legendre(i); coefficient=remainder[i]/p[i]
            C[i][j]=coefficient
            for k,x in enumerate(p): remainder[k]-=coefficient*x
        assert all(x==0 for x in remainder)
        assert C[j][j]>0
        assert all(C[i][j]==0 for i in range(8) if (i-j)%2)
    def converted(A): return mm(mm(tr(C),A),C)
    P=converted(D); lower=converted(L); upper=converted(U); nominal=converted(middle)
    assert psd([[lower[i][j]-alpha*P[i][j] for j in range(8)] for i in range(8)])
    assert psd(P) and psd(lower)
    native_trials=mm(V,C)
    normalized_error=beta/alpha
    assert normalized_error<F(1,100)
    entry_rows=[]
    den=10**12
    for i in range(8):
        for j in range(i,8):
            if (i-j)%2:
                assert nominal[i][j]==lower[i][j]==upper[i][j]==P[i][j]==0
                entry_rows.append(dict(i=i,j=j,lower='0',upper='0',reason='exact parity'))
                continue
            radius=I(tau)*I(P[i][i]*P[j][j]).sqrt()
            value=I(nominal[i][j])+I(radius.h.copy_negate(),radius.h)
            low=int(loctx.multiply(value.l,I(den).l).to_integral_value(rounding='ROUND_FLOOR'))
            high=int(hictx.multiply(value.h,I(den).h).to_integral_value(rounding='ROUND_CEILING'))
            entry_rows.append(dict(i=i,j=j,lower=str(F(low,den)),upper=str(F(high,den))))
    return dict(milestone='RC39',status='PASS',native_features_certified=list(range(8)),
        complete_native_feature_count=8600,trial_dimension=32,
        metric_certificate_sha256=hashlib.sha256(raw).hexdigest(),
        chebyshev_to_legendre=[[str(x) for x in r] for r in C],
        native_trial_coefficients=[[str(x) for x in r] for r in native_trials],
        physical_native_Gram=[[str(x) for x in r] for r in P],
        canonical_native_Gram_Loewner_lower=[[str(x) for x in r] for r in lower],
        canonical_native_Gram_Loewner_upper=[[str(x) for x in r] for r in upper],
        canonical_native_Gram_enclosure_center=[[str(x) for x in r] for r in nominal],
        canonical_native_Gram_entry_enclosures=entry_rows,
        canonical_native_Gram_physical_lower_factor=str(alpha),
        canonical_native_Gram_physical_upper_factor=str(rho),
        normalized_center_error_upper=str(tau),
        canonical_trial_error_physical_squared_upper=str(beta),
        canonical_trial_error_actual_native_metric_squared_upper=str(normalized_error),
        actual_low_native_Gram_certified=True,exact_Riesz_inverse_certified=False,
        complete_native_Gram_certified=False,original_Weil_head_floor_certified=False,
        native_remainder_sources_certified=False,aperture_extended=False)

if __name__=='__main__':
    root=Path(__file__).parent.parent/'certificates'
    metric=sys.argv[1] if len(sys.argv)>1 else root/'rpb108_rc38_thirty_two_metric.json'
    residual=sys.argv[2] if len(sys.argv)>2 else root/'rpb108_rc38_thirty_two_residuals.json'
    print(json.dumps(run(metric,residual),indent=2))
