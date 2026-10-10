"""RC32 exact supported-metric floors and inverse/residual envelopes."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
from validate_rpb108_rc31_trial_riesz import run, psd

def certify(data):
    base=run(data); n=base['dimension']; ds=list(map(F,data['physical_mass']))
    lower=[[F(v) for v in r] for r in base['full_response_lower']]
    D=[[ds[i] if i==j else F(0) for j in range(n)] for i in range(n)]
    B=F(11,10); omega=F(5,44)
    eupper=sum((F(1,factorial(j)) for j in range(9)),F(0))+F(1,factorial(9))*F(10,9)
    assert eupper<F(87,32)<F(11,4)<3
    assert 1-4*B*omega==F(1,2)
    lam=1+(1-4*B*omega)*omega/(F(11,4)+omega)
    stronger=1+(1-4*B*omega)*omega/(F(87,32)+omega)
    assert lam==F(257,252) and stronger==F(1017,997)
    rho=1/lam; gap=rho-1/stronger
    assert gap==F(55,261369)>F(1,400)**2
    U=[[rho*D[i][j]-lower[i][j] for j in range(n)] for i in range(n)]
    assert psd(U)
    beta=next(F(k,100) for k in range(1,101) if psd(
        [[F(k,100)*D[i][j]-U[i][j] for j in range(n)] for i in range(n)]))
    assert beta< F(base['collective_residual_squared_upper'])
    assert psd([[U[i][j]-gap*D[i][j] for j in range(n)] for i in range(n)])
    return dict(milestone='RC32',status='PASS',cap='11/10',metric_floor=str(lam),
        supported_inverse_upper_factor=str(rho),stronger_metric_control=str(stronger),
        collective_residual_squared_upper=str(beta),
        envelope_intrinsic_floor=str(gap),
        full_residual_Gram_upper=[[str(v) for v in row] for row in U],
        per_column_residual_upper_display=[float(U[i][i])**0.5 for i in range(n)],
        actual_residual_lower_bound=False,native_head_certified=False,aperture_extended=False)

if __name__=='__main__':
    import sys
    path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).parent.parent/'certificates/rpb108_rc30_interval_trial_metric.json'
    print(json.dumps(certify(json.loads(path.read_text())),indent=2))
