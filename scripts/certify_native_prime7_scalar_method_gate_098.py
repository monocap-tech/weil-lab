"""Ceiling on the saved positive-region scalar band method, not on the actual form."""
import gzip,hashlib,json
from pathlib import Path
from certify_native_legendre_small_window import F,I,atan
from certify_native_exact_logarithm import log_rational

def certificate():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    files={'prime':'RPB108_PRIME7_WEIGHTED_DEPTH10_098_CERTIFICATE_20261007.json.gz',
        'witness':'RPB108_PRIME7_SCHUR96_098_STRONGER_OBSTRUCTION_20261007.json',
        'conditional':'RPB108_PRIME7_SCHUR96_098_CONDITIONAL_094_20261007.json'}
    raw={k:(gzip.decompress((root/p).read_bytes()) if p.endswith('.gz') else (root/p).read_bytes()) for k,p in files.items()}
    prime,w,c=(json.loads(raw[k]) for k in ('prime','witness','conditional'))
    assert prime['coarse_offset_depth']==10 and prime['aperture']==w['aperture']==c['aperture']=='49/50'
    assert c['all_96_corrected_pivots_positive'] and not c['complement_proved']
    needed=F(w['necessary_complement_lower']);loss=F(prime['joint_prime_operator_norm_upper'])
    assert needed>F(93317,100000) and loss==F(1899459,1000000)
    saved=I.grid;I.grid=10**140
    try:
        pi=16*atan(F(1,5),200)-4*atan(F(1,239),200)
        cap=F(157,10);radius_squared=(F(49,25)*pi.lo*cap)**2
        assert radius_squared>96*97
        logcap=log_rational(cap,500)
        ceiling=logcap.hi-loss
        assert ceiling<F(855,1000)<needed
        return dict(aperture='49/50',input_sha256={k:hashlib.sha256(v).hexdigest() for k,v in raw.items()},
            retained_vectors=96,positive_region_limit_squared=96*97,
            rational_cutoff_upper=str(cap),pi_enclosure=[str(pi.lo),str(pi.hi)],
            cutoff_argument_squared_lower=str(radius_squared),log_cutoff_upper=str(logcap.hi),
            fixed_proved_prime_majorant=str(loss),
            scalar_band_method_output_ceiling=str(ceiling),method_ceiling_display=float(ceiling),
            scope='any monotone frequency-band lower estimate using this positive Bessel region and this fixed prime loss; all nonnegative mass and pole penalties omitted',
            necessary_scalar_complement_lower=str(needed),hypothetical_sufficient_complement='47/50',
            ordinary_frequency_cut_optimization_cannot_close=True,
            actual_complement_upper_claimed=False,actual_negative_weil_form_claimed=False,
            whole_domain_positivity_at_098=False,whole_domain_frontier='973/1000',f4_entry_closed=False)
    finally:I.grid=saved

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
