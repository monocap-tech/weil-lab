#!/usr/bin/env python3
"""NF11 candidate full native 112x112 interval reconstruction at a=53/50.

UNEXECUTED target full producer. A checkpoint of fewer than 112 rows is
INCOMPLETE AND NOT a positive-aperture certificate. No old CC18 numbers
are reused or redirected. Depends on original pinned integrator helpers.
"""
import argparse,gzip,hashlib,json,sys
from pathlib import Path
from functools import lru_cache
from fractions import Fraction as F
from math import isqrt
import certify_native_legendre112_106 as native
from certify_native_legendre112_106 import I,positive_pivots
from certify_native_exact_logarithm import log_rational as fast_log
from certify_native_exact_polynomial import mul as fast_mul,correlation as fast_correlation
from certify_native_matrix112_checkpoint import load,save

A=F(53,50); DIM=112; GRID=10**400
class PrefixReached(Exception):pass
def sqrt_interval(x):
    g=I.grid;k=isqrt((x*g*g).__floor__())
    return I(F(k,g),F(k+1,g))
def binding():
    parent=Path(__file__).resolve().parent
    names=['certify_native_prime8_matrix112_nf11_106.py',
      'certify_native_legendre112_106.py','certify_native_exact_polynomial.py',
      'certify_native_exact_kernel_integral.py','certify_native_exact_logarithm.py',
      'certify_native_matrix112_checkpoint.py']
    return dict(aperture='53/50',degree=111,exponential_order=400,
      bernoulli_pairs=400,gamma_order=20,interval_grid_digits=400,
      log_series_terms=220,scripts={p:hashlib.sha256((parent/p).read_bytes()).hexdigest() for p in names})
def build(checkpoint,max_rows=None,output=None):
    if max_rows is not None and not 1<=max_rows<=112:
        raise ValueError('max_rows must be 1..112')
    prior=(I.grid,native.correlation,native.sqrt_rational,native.mul,native.log_rational)
    I.grid=GRID
    native.correlation=fast_correlation
    native.sqrt_rational=sqrt_interval
    native.mul=fast_mul
    native.log_rational=lru_cache(maxsize=None)(lambda x,terms=220:fast_log(x,terms))
    try:
        binds=binding()
        resume=load(checkpoint,binds) if checkpoint and Path(checkpoint).exists() else None
        if resume and max_rows and resume[0]>=max_rows:
            return dict(status='incomplete/native checkpoint previously reached target',rows=resume[0])
        def observer(rows,raw):
            if checkpoint:save(checkpoint,binds,rows,raw)
            print('NF11 unnormalized native112 computed rows',rows,file=sys.stderr,flush=True)
            if max_rows and rows>=max_rows and rows<112:raise PrefixReached(rows)
        try:
            raw=native.certificate(A,return_matrix=True,degree=111,
                                    matrix_resume=resume,matrix_observer=observer)
        except PrefixReached as stop:
            return dict(status='INCOMPLETE checkpoint only',aperture='53/50',
                        completed_rows=stop.args[0],full_matrix=False,
                        full_source_gram=False,whole_sign=False)
        Q=[[sqrt_interval(F((2*i+1)*(2*j+1)))*raw[i][j]/(2*A)
            for j in range(DIM)] for i in range(DIM)]
        assert all(Q[i][j].lo==Q[i][j].hi==0 for i in range(DIM)
                   for j in range(DIM) if (i+j)%2)
        widths=[x.hi-x.lo for row in Q for x in row]
        try:
            pivots=positive_pivots(Q)
            finite_positive=True;failed=None
        except ArithmeticError as exc:
            pivots=[];finite_positive=False;failed=str(exc)
        result=dict(status='complete native interval matrix computed; full Weil sign open',
             aperture='53/50',dimension=DIM,all_six_prime_powers=[2,3,4,5,7,8],
             signed_poles=True,even_odd_mixed_exact_zero=True,
             largest_entry_width=str(max(widths)),finite_restriction_positive=finite_positive,
             failed_positive_pivot_reason=failed,positive_pivot_lower_bounds=[str(x.lo) for x in pivots],
             complement_lower='17/100',complement_used_for_matrix=False,
             full_source_gram=False,corrected_full_schur=False,
             entire_domain_positive=False,RH=False,lean_certified=False,
             row_major_lower_triangle=[[[str(Q[i][j].lo),str(Q[i][j].hi)]
                                        for j in range(i+1)] for i in range(DIM)])
        if output:
            Path(output).write_bytes(gzip.compress(json.dumps(result,sort_keys=True).encode(),mtime=0))
            result={k:v for k,v in result.items() if k!='row_major_lower_triangle'}
            result['full_matrix_archive']=output
        return result
    finally:
        I.grid,native.correlation,native.sqrt_rational,native.mul,native.log_rational=prior

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--checkpoint',help='SHA-bound incomplete native matrix rows')
    p.add_argument('--max-rows',type=int,default=None)
    p.add_argument('--output',help='gzip full native matrix archive when complete')
    a=p.parse_args()
    print(json.dumps(build(a.checkpoint,a.max_rows,a.output),indent=2))
