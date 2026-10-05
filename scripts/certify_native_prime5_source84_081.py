"""Actual 84-source enclosures with nine prime-5 panels at aperture 81/100."""
import json
import certify_native_prime3_source36 as source
from certify_native_legendre_small_window import F,I
from certify_native_exact_logarithm import log_rational

def certificate():
    old=I.grid;old_log=source.log_rational;old_interval=source.log_interval;I.grid=10**400
    source.log_rational=lambda x,terms=220:log_rational(x,terms)
    source.log_interval=lambda x:I(log_rational(x.lo,220).lo,log_rational(x.hi,220).hi)
    try:
        result=source.quantize(source.compute(degree=83,a=F(81,100)),digits=60)
        result['source_log_series_terms']=220
        from certify_native_prime5_source_codec import compact_sources
        return compact_sources(result)
    finally:I.grid=old;source.log_rational=old_log;source.log_interval=old_interval

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
