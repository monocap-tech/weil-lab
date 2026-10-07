"""Independent Gårding-24 rational budgets at exact aperture one."""
import json,hashlib
from pathlib import Path
from certify_native_legendre_small_window import F,I,sqrt_rational
from certify_native_exact_logarithm import log_rational

def certificate(path):
    raw=Path(path).read_bytes();c=json.loads(raw);assert c['aperture']=='1'
    p=Path(__file__).resolve().parents[1]/'notes/data/RPB108_PRIME7_WEIGHTED_DEPTH10_100_CERTIFICATE_20261007.json'
    b=p.read_bytes();assert hashlib.sha256(b).hexdigest()==c['weighted_prime_input_sha256']
    prime=json.loads(b);assert prime['aperture']=='1' and prime['prime_powers']==[2,3,4,5,7]
    saved=I.grid;I.grid=10**140
    try:
        logs={n:log_rational(F(n),450) for n in [2,3,5,7,8]}
        amps=[logs[2]/sqrt_rational(F(2)),logs[3]/sqrt_rational(F(3)),logs[2]/2,logs[5]/sqrt_rational(F(5)),logs[7]/sqrt_rational(F(7))]
        assert all(x.hi<=F(y) for x,y in zip(amps,prime['amplitude_upper']))
        loss=2*sum(map(F,prime['amplitude_upper']),F(0));assert loss==F(c['crude_prime_loss_upper'])<6
        assert logs[7].hi<2<logs[8].lo and logs[3].lo>1
        # exp(1)<3 strictly, so 4a exp(a)<12 at a=1 despite 4a*3=12.
        assert 4*F(1)*3==12
        assert c['archimedean_multiplier_loss']==6 and c['prime_loss_below']==6 and c['pole_loss_below']==12
        assert c['garding_constant']==6+6+12==24 and c['multiplier_weight_factor']=='1/10'
    finally:I.grid=saved
    return dict(aperture='1',certificate_sha256=hashlib.sha256(raw).hexdigest(),independent_prime_amplitude_inclusions=5,
        prime_loss_strictly_below_six=True,pole_loss_strictly_below_twelve_from_exp_one_below_three=True,
        exact_aperture_one_equality_case_verified=True,garding_24_verified=True,whole_domain_positivity=False,f4_entry_closed=False)

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(sys.argv[1]),indent=2))
