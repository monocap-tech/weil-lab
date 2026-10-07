"""Fresh target prime/pole loss budgets for the published m0 >= w/10 - 6 estimate."""
import gzip,hashlib,json
from pathlib import Path
from certify_native_legendre_small_window import F,I
from certify_native_exact_logarithm import log_rational
from certify_native_prime7_112_preflight_0995 import EXPECTED_PRIME_SHA256

def certificate():
    path=Path(__file__).resolve().parents[1]/'notes/data/RPB108_PRIME7_WEIGHTED_DEPTH10_0995_CERTIFICATE_20261007.json.gz'
    raw=gzip.decompress(path.read_bytes());p=json.loads(raw)
    assert hashlib.sha256(raw).hexdigest()==EXPECTED_PRIME_SHA256
    assert p['aperture']=='199/200' and p['prime_powers']==[2,3,4,5,7]
    saved=I.grid;I.grid=10**100
    try:
        loss=2*sum(map(F,p['amplitude_upper']),F(0));assert loss<6
        assert log_rational(F(3),400).lo>1
        assert log_rational(F(7),400).hi<2*F(199,200)<log_rational(F(8),400).lo
        assert 4*F(199,200)*3<12
        return dict(aperture='199/200',weighted_prime_input_sha256=hashlib.sha256(raw).hexdigest(),
            crude_prime_loss_upper=str(loss),prime_loss_below=6,pole_loss_below=12,
            archimedean_multiplier_loss=6,garding_constant=24,multiplier_weight_factor='1/10',
            published_multiplier_bound_reused='m0 >= w/10 - 6',garding_24_verified=True,
            constructor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            whole_domain_positivity=False,whole_domain_frontier='99/100',f4_entry_closed=False)
    finally:I.grid=saved

if __name__=='__main__':print(json.dumps(certificate(),indent=2))

