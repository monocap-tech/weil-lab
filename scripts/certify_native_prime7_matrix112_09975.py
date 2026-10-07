"""Certified full native 112-vector restriction at aperture 399/400; finite only."""
import json,hashlib
from pathlib import Path
from functools import lru_cache
from certify_native_exact_logarithm import log_rational as fast_log
from math import comb,lcm,isqrt
import certify_native_legendre112_09975 as native
from certify_native_legendre112_09975 import F,I,positive_pivots
from certify_native_exact_polynomial import mul as fast_mul,correlation as fast_correlation


def integer_correlation(p,q):
    """The existing correlation identity with one common integer denominator."""
    dp=lcm(*(c.denominator for c in p));dq=lcm(*(c.denominator for c in q))
    den=lcm(*range(1,len(p)+len(q)))
    pp=[int(c*dp) for c in p];qq=[int(c*dq) for c in q]
    out=[0]*(len(p)+len(q))
    binom=[[comb(n,k) for k in range(n+1)] for n in range(len(out))]
    for i,x in enumerate(pp):
        if not x:continue
        for j,y in enumerate(qq):
            if not y:continue
            for k in range(j+1):
                d=i+j-k+1
                c=x*y*binom[j][k]*(-1)**k*(den//d)
                out[k]+=c
                for ell in range(d+1):
                    out[k+ell]-=c*binom[d][ell]*(-1)**(d-ell)
    return [F(c,dp*dq*den) for c in out]


def precise_sqrt(x):
    g=I.grid;n=isqrt((x*g*g).__floor__())
    return I(F(n,g),F(n+1,g))


def certificate(checkpoint=None):
    previous=I.grid;old_correlation=native.correlation;old_sqrt=native.sqrt_rational;old_mul=native.mul;old_log=native.log_rational
    I.grid=10**400;native.correlation=fast_correlation;native.sqrt_rational=precise_sqrt;native.mul=fast_mul
    native.log_rational=lru_cache(maxsize=None)(lambda x,terms=220:fast_log(x,terms))
    try:
        a=F(399,400);size=112
        resume=None;observer=None
        if checkpoint is not None:
            from certify_native_matrix112_checkpoint import load,save
            root=Path(__file__).resolve().parent
            names=['certify_native_prime7_matrix112_09975.py','certify_native_legendre112_09975.py','certify_native_legendre_small_window.py',
                   'certify_native_exact_polynomial.py','certify_native_exact_kernel_integral.py',
                   'certify_native_exact_logarithm.py','certify_native_matrix112_checkpoint.py']
            bindings=dict(aperture='399/400',degree=111,exponential_order=360,bernoulli_pairs=360,
                          gamma_order=20,grid_digits=400,log_series_terms=220,
                          scripts={name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in names})
            if Path(checkpoint).exists():resume=load(checkpoint,bindings)
            def observer(done,matrix):
                save(checkpoint,bindings,done,matrix)
                print('native checkpoint completed rows',done,file=__import__('sys').stderr,flush=True)
        raw=native.certificate(a,return_matrix=True,degree=111,matrix_resume=resume,matrix_observer=observer)
        Q=[[precise_sqrt(F((2*i+1)*(2*j+1)))*raw[i][j]/(2*a)
            for j in range(size)] for i in range(size)]
        pivots=positive_pivots(Q)
        tau=F(1,10**18)
        while True:
            shifted=[row[:] for row in Q]
            for i in range(size):shifted[i][i]-=tau
            try:
                shifted_pivots=positive_pivots(shifted);break
            except ArithmeticError:
                if tau<F(1,10**60):raise
                tau/=2
        broken=[row[:] for row in Q];broken[0][0]=I(-1)
        try:positive_pivots(broken)
        except ArithmeticError:pass
        else:raise AssertionError('Negative control accepted')
        assert all(Q[i][j].lo==Q[i][j].hi==0 for i in range(size) for j in range(size) if (i+j)%2)
        width=max(x.hi-x.lo for row in Q for x in row)
        print("maximum native entry width",float(width),file=__import__("sys").stderr,flush=True)
        assert width<F(1,10**35)
        return dict(status='certified full native 112-vector finite restriction only',aperture='399/400',
                    physical_degrees=list(range(size)),prime_terms=[2,3,4,5,7],
                    physical_basis='sqrt((2n+1)/(2a)) P_n(x/a) on [-a,a]',
                    matrix_intervals=[[[str(x.lo),str(x.hi)] for x in row] for row in Q],
                    pivot_lower_bounds=[str(x.lo) for x in pivots],
                    raw_physical_coercivity_lower_bound=str(tau),
                    shifted_pivot_lower_bounds=[str(x.lo) for x in shifted_pivots],
                    maximum_entry_width=str(width),exact_reflection_parity=True,
                    negative_control_rejected=True,exponential_order=360,bernoulli_pairs=360,
                    gamma_order=20,interval_grid_digits=400,log_series_terms=220,
                    full_source_gram_certified=False,corrected_schur_sign_certified=False,
                    whole_domain_positivity=False,f4_entry_closed=False,full_transport_closed=False,
                    lean_formalized=False)
    finally:
        I.grid=previous;native.correlation=old_correlation;native.sqrt_rational=old_sqrt;native.mul=old_mul;native.log_rational=old_log


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--checkpoint')
    args=parser.parse_args()
    print(json.dumps(certificate(args.checkpoint),indent=2))

