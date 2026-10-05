"""Actual eight-source Schur lower bound with exact prime-panel integration."""
import json
import hashlib
from pathlib import Path
from functools import lru_cache
from certify_native_legendre_small_window import F,I,mul,log_rational,sqrt_rational,certificate as raw_certificate,positive_pivots
from certify_native_endpoint_log_gram import exact_log_data
from certify_native_smooth_source import compose


def evaluate(p,t):
    out=I(0)
    for c in reversed(p):
        out=out*t+c
    return out


def integral(p,a,b):
    primitive=[F(0)]+[c/F(k+1) for k,c in enumerate(p)]
    return evaluate(primitive,b)-evaluate(primitive,a)


@lru_cache(None)
def log_point(x):
    assert x>0
    shift=0
    while x<1:
        x*=2
        shift-=1
    while x>=2:
        x/=2
        shift+=1
    def unit(y):
        z=I((y-1)/(y+1));z2=z*z;term=z;total=I(0)
        for k in range(220):
            total+=2*term/I(2*k+1)
            term=term*z2
        tail=F(2,441*3**441)*F(9,8)
        return total+I(-tail,tail)
    return unit(x)+shift*unit(F(2))


def log_primitive(p,t):
    if t.hi==0:
        return I(0)
    logt=I(log_point(t.lo).lo,log_point(t.hi).hi)
    first=[F(0)]+[c/F(k+1) for k,c in enumerate(p)]
    second=[F(0)]+[c/F((k+1)**2) for k,c in enumerate(p)]
    return evaluate(first,t)*logt-evaluate(second,t)


def mixed_integral(p,a,b):
    reverse=compose(p,F(1),F(-1))
    return -(log_primitive(p,b)-log_primitive(p,a)
             +log_primitive(reverse,I(1)-a)-log_primitive(reverse,I(1)-b))/I(2)


def certificate():
    previous=I.grid
    I.grid=10**120
    try:
        return compute()
    finally:
        I.grid=previous


def compute():
    source=json.loads((Path(__file__).resolve().parents[1]/'notes/data/RPB108_SMOOTH_SOURCE_CERTIFICATE_20261005.json').read_text())
    p,CL,RL=exact_log_data()
    ell=log_rational(F(2),220)
    cuts=[I(0),I(1)-ell,ell,I(1)]
    polys=[[[F(v) for v in panel['coefficients']] for panel in row['panels']] for row in source['rows']]
    CS=[[I(0) for _ in range(8)] for _ in range(64)]
    smooth=[[I(0) for _ in range(8)] for _ in range(8)]
    cross=[[I(0) for _ in range(8)] for _ in range(8)]
    for panel,(a,b) in enumerate(zip(cuts,cuts[1:])):
        for i in range(8):
            for n in range(64):
                CS[n][i]+=integral(mul(p[n],polys[i][panel]),a,b)
            for j in range(8):
                cross[i][j]+=mixed_integral(mul(p[i],polys[j][panel]),a,b)
            for j in range(i,8):
                smooth[i][j]+=integral(mul(polys[i][panel],polys[j][panel]),a,b)
    R=[[I(0) for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(i,8):
            correction=smooth[i][j]+cross[i][j]+cross[j][i]
            correction-=sum(((2*n+1)*(CS[n][i]*CS[n][j]+CL[n][i]*CS[n][j]+CL[n][j]*CS[n][i]) for n in range(64)),I(0))
            R[i][j]=R[j][i]=RL[i][j]+sqrt_rational(F((2*i+1)*(2*j+1)))*correction
    # Trace is its Hilbert--Schmidt norm squared; hence ||rtilde|| <= sqrt(trace).
    trace=sum((R[i][i].hi for i in range(8)),F(0))
    assert trace>0
    M=sqrt_rational(trace).hi
    eta=F(source['source_map_error_upper'])
    delta=eta*(2*M+eta)
    raw=raw_certificate(F(1,2),return_matrix=True)
    Q=[[sqrt_rational(F((2*i+1)*(2*j+1)))*raw[i][j] for j in range(8)] for i in range(8)]
    lower=[[Q[i][j]-5*R[i][j] for j in range(8)] for i in range(8)]
    tau=F(1,250000)
    for i in range(8):
        lower[i][i]-=5*delta+tau
    pivots=positive_pivots(lower)
    broken=[row[:] for row in lower]
    broken[0][0]=I(-1)
    try:
        positive_pivots(broken)
    except ArithmeticError:
        pass
    else:
        raise AssertionError('Negative control accepted')
    width=max(x.hi-x.lo for row in R for x in row)
    assert width<F(1,10**25)
    return dict(status='certified corrected actual eight-source Schur restriction',
                physical_degrees=list(range(8)),complement_projection_degrees=list(range(64)),
                interval_grid_digits=120,log_series_terms=220,
                residual_gram_surrogate=[[[str(x.lo),str(x.hi)] for x in row] for row in R],
                maximum_gram_entry_width=str(width),maximum_gram_entry_width_display=float(width),
                surrogate_residual_map_norm_upper=str(M),actual_gram_operator_error_upper=str(delta),
                corrected_physical_coercivity_lower_bound=str(tau),
                shifted_pivot_lower_bounds=[str(x.lo) for x in pivots],
                shifted_pivot_lower_display=[float(x.lo) for x in pivots],
                source_certificate_sha256=hashlib.sha256((Path(__file__).resolve().parents[1]/'notes/data/RPB108_SMOOTH_SOURCE_CERTIFICATE_20261005.json').read_bytes()).hexdigest(),
                negative_control_rejected=True,
                all_mixed_terms_retained=True,whole_domain_positivity=False,full_64_schur_sign_certified=False)


if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
