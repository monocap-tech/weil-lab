"""Finer Machin/log audit of the method ceiling and its witness comparison."""
import hashlib,json
from pathlib import Path
from fractions import Fraction as F
from certify_native_legendre_small_window import I,atan
from certify_native_exact_logarithm import log_rational

def certificate():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    raw=(root/'RPB108_PRIME7_SCALAR_METHOD_GATE_098_20261007.json').read_bytes();c=json.loads(raw)
    saved=I.grid;I.grid=10**180
    try:
        pi=16*atan(F(1,5),300)-4*atan(F(1,239),300)
        lo,hi=map(F,c['pi_enclosure']);assert lo<=pi.lo<=pi.hi<=hi
        T=F(c['rational_cutoff_upper']);assert T==F(157,10)
        assert (F(49,25)*pi.lo*T)**2>96*97
        upper=log_rational(T,600).hi-F(c['fixed_proved_prime_majorant'])
        assert upper<=F(c['scalar_band_method_output_ceiling'])<F(855,1000)
        wraw=(root/'RPB108_PRIME7_SCHUR96_098_STRONGER_OBSTRUCTION_20261007.json').read_bytes()
        assert hashlib.sha256(wraw).hexdigest()==c['input_sha256']['witness']
        needed=F(json.loads(wraw)['necessary_complement_lower'])
        assert needed>F(93317,100000)>F(c['scalar_band_method_output_ceiling'])
        assert c['actual_complement_upper_claimed'] is False
        return dict(certificate_sha256=hashlib.sha256(raw).hexdigest(),
            finer_pi_and_logarithm_enclosures_verified=True,positive_region_cutoff_cap_verified=True,
            method_ceiling_below_witness_requirement=True,actual_complement_upper_claimed=False,
            whole_domain_positivity_at_098=False,whole_domain_frontier='973/1000',f4_entry_closed=False)
    finally:I.grid=saved

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
