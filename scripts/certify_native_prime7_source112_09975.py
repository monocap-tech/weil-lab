#!/usr/bin/env python3
"""Actual 112-source enclosure at 399/400 with checked new kernel constants."""
import json,hashlib
from pathlib import Path
from functools import lru_cache
from math import factorial
import certify_native_prime7_source112_engine_09975 as source
from certify_native_legendre_small_window import F,I,bernoulli
from certify_native_exact_logarithm import log_rational
from certify_native_prime5_source_codec import compact_sources


def certificate(checkpoint=None):
    a=F(399,400);d=2*a;K=114
    B=bernoulli(2*K+2)
    coefficients=[abs(B[2*k]*(2*d)**(2*k)/factorial(2*k)) for k in range(1,K+1)]
    assert all(y<x for x,y in zip(coefficients,coefficients[1:]))
    assert all((B[2*k]>0)==(k%2==1) for k in range(1,K+1))
    # Alternating decreasing pairs give 0<BP(s)<=1+d*s+d^2*s^2/3 on [0,1].
    assert (1+d+d*d/3)/2 < F(9,4)
    assert d/2<1 and d<3
    previous=I.grid;old_log=source.log_rational;old_interval=source.log_interval
    I.grid=10**400
    source.log_rational=lru_cache(maxsize=None)(lambda x,terms=220:log_rational(x,terms))
    source.log_interval=lambda x:I(source.log_rational(x.lo).lo,source.log_rational(x.hi).hi)
    try:
        names=['certify_native_prime7_source112_09975.py','certify_native_prime7_source112_engine_09975.py','certify_native_prime7_translation_panels_09975.py','certify_native_prime5_source_codec.py','certify_native_legendre_small_window.py','certify_native_exact_logarithm.py','certify_native_endpoint_log_gram.py']
        bindings={name:hashlib.sha256((Path(__file__).parent/name).read_bytes()).hexdigest() for name in names}
        resume=[];observer=None
        if checkpoint is not None:
            import gzip,os,sys
            folder=Path(checkpoint);folder.mkdir(parents=True,exist_ok=True)
            manifest=folder/'bindings.json'
            if manifest.exists():assert json.loads(manifest.read_bytes())==bindings
            else:manifest.write_text(json.dumps(bindings,sort_keys=True)+'\n')
            for index in range(112):
                path=folder/f'row{index:03}.json.gz'
                if not path.exists():break
                row=json.loads(gzip.decompress(path.read_bytes()));assert row['degree']==index;resume.append(row)
            assert not any((folder/f'row{index:03}.json.gz').exists() for index in range(len(resume),112))
            def observer(row):
                path=folder/f"row{row['degree']:03}.json.gz";temp=path.with_suffix('.tmp')
                temp.write_bytes(gzip.compress(json.dumps(row,sort_keys=True,separators=(',',':')).encode(),mtime=0));os.replace(temp,path)
                print('source checkpoint completed rows',row['degree']+1,file=sys.stderr,flush=True)
        result=compact_sources(source.quantize(source.compute(degree=111,a=a,rows_resume=resume,row_observer=observer),digits=40))
        result.update(source_log_series_terms=220,source_pi_machin_terms=160,kernel_taylor_ceiling='9/4',
                      alternating_kernel_coefficient_controls_passed=True,
                      coefficient_rounding_budget_retained=True,
                      whole_domain_positivity=False,whole_domain_positivity_frontier='199/200',
                      f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)
        names=['certify_native_prime7_source112_09975.py','certify_native_prime7_source112_engine_09975.py','certify_native_prime7_translation_panels_09975.py','certify_native_prime5_source_codec.py','certify_native_legendre_small_window.py','certify_native_exact_logarithm.py','certify_native_endpoint_log_gram.py']
        result['constructor_sha256']={name:hashlib.sha256((Path(__file__).parent/name).read_bytes()).hexdigest() for name in names}
        return result
    finally:
        I.grid=previous;source.log_rational=old_log;source.log_interval=old_interval


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--checkpoint');args=parser.parse_args()
    print(json.dumps(certificate(args.checkpoint),indent=2))

