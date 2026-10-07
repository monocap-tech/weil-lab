"""Actual 112-source residual Gram at 1; corrected sign is separate."""
import json,hashlib
from pathlib import Path
from certify_native_legendre_small_window import F,I,positive_pivots
from certify_native_exact_logarithm import log_rational
from certify_native_exact_hankel import moment_apply,bilinear_bounds
import certify_native_endpoint_log112_100 as endpoint
from certify_native_endpoint_log112_100 import exact_log_data
from certify_native_prime3_matrix36 import precise_sqrt as sqrt_rational
from math import lcm

def mul(p,q):
    dp=lcm(*(x.denominator for x in p));dq=lcm(*(x.denominator for x in q))
    pp=[int(x*dp) for x in p];qq=[int(x*dq) for x in q]
    out=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(pp):
        if x:
            for j,y in enumerate(qq):
                if y:out[i+j]+=x*y
    return [F(x,dp*dq) for x in out]

from functools import lru_cache
@lru_cache(None)
def log_point(x):return log_rational(x,500)
def complement_certificate():
    path=Path(__file__).resolve().parents[1]/'notes/data/RPB108_PRIME7_112_PREFLIGHT_100_CERTIFICATE_20261007.json'
    raw=path.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='e9dccb28286930e2aa469986341f95401b0ab8263a1be213b3ca3e3f7bedd52c'
    result=json.loads(raw)
    assert result['retained_vectors']==112 and result['aperture']=='1'
    result['complement_inverse_factor']=str(1/F(result['physical_lower']))
    return result


def endpoint_primitives(t,degree):
    powers=[I(1)]
    for _ in range(degree+1):
        powers.append(powers[-1]*t)
    logt=None if t.hi==0 else I(log_point(t.lo).lo,log_point(t.hi).hi)
    reverse=I(1)-t
    logreverse=None if reverse.hi==0 else I(log_point(reverse.lo).lo,log_point(reverse.hi).hi)
    harmonic=I(0);logs=[]
    for k in range(degree+1):
        n=k+1;harmonic+=powers[n]/I(n)
        first=I(0) if logt is None else powers[n]*(logt/I(n)-F(1,n*n))
        second=-harmonic/I(n) if logreverse is None else ((powers[n]-1)*logreverse-harmonic)/I(n)
        logs.append(-(first+second)/I(2))
    return powers,logs



def fixed_decimal(x):
    """Lossless finite-decimal encoding of an exact fixed-grid endpoint."""
    scaled=x*I.grid
    assert scaled.denominator==1
    sign='-' if scaled<0 else ''
    digits=len(str(I.grid))-1
    text=str(abs(scaled.numerator)).rjust(digits+1,'0')
    return sign+(text[:-digits]+'.'+text[-digits:]).rstrip('0').rstrip('.')


def fixed_moments(moments):
    return [(int(x.lo*I.grid),int(x.hi*I.grid)) for x in moments]


def negative_candidate(matrix):
    grid=10**600
    def rounded(x):return F((x*grid).__floor__(),grid)
    work=[[rounded((x.lo+x.hi)/2) for x in row] for row in matrix]
    size=len(work);L=[[F(int(i==j)) for j in range(size)] for i in range(size)]
    for k in range(size):
        pivot=work[k][k]
        if pivot<=0:
            v=[F(0)]*size;v[k]=F(1)
            for i in range(k-1,-1,-1):
                v[i]=-sum((L[j][i]*v[j] for j in range(i+1,k+1)),F(0))
            scale=max(map(abs,v))
            return [F((x/scale*10**40+F(1,2)).__floor__(),10**40) for x in v]
        for i in range(k+1,size):
            L[i][k]=rounded(work[i][k]/pivot)
            for j in range(i,size):
                work[i][j]=rounded(work[i][j]-work[i][k]*work[k][j]/pivot)
                work[j][i]=work[i][j]
    return None


def certificate(checkpoint=None):
    previous=I.grid;I.grid=10**300;log_point.cache_clear()
    try:
        return compute(checkpoint)
    finally:
        I.grid=previous;log_point.cache_clear()


def compute(checkpoint=None):
    complement=complement_certificate()
    assert complement["physical_lower"]=="93/100" and complement["complement_inverse_factor"]=="100/93"
    root=Path(__file__).resolve().parents[1]/'notes/data'
    source_path=root/'RPB108_PRIME7_SOURCE112_100_CERTIFICATE_20261007.json'
    native_path=root/'RPB108_PRIME7_MATRIX112_100_COMPACT80_20261007.json'
    source_raw=source_path.read_bytes() if source_path.exists() else __import__('gzip').decompress(source_path.with_suffix('.json.gz').read_bytes())
    source=json.loads(source_raw);native=json.loads(native_path.read_text())
    assert native['matrix_encoding']=='row-major lower triangle integer endpoints on grid 10^-80'
    triangle=native['lower_triangle_row_major'];assert len(triangle)==6328
    entries=[[None for _ in range(112)] for _ in range(112)];index=0
    for i in range(112):
        for j in range(i+1):
            pair=[str(F(int(x),10**80)) for x in triangle[index]]
            entries[i][j]=entries[j][i]=pair;index+=1
    native['matrix_intervals']=entries
    assert len(source['rows'])==112 and native['physical_degrees']==list(range(112))
    old_mul=endpoint.mul;old_sqrt=endpoint.sqrt_rational
    endpoint.mul=mul;endpoint.sqrt_rational=sqrt_rational
    try:p,CL,RL=exact_log_data(111,112)
    finally:endpoint.mul=old_mul;endpoint.sqrt_rational=old_sqrt
    print("endpoint Gram done",file=__import__("sys").stderr,flush=True)
    assert source['coefficient_encoding']=='integer numerators with common decimal denominator and row tail'
    coefficient_denominator=10**source['coefficient_grid_digits']
    polys=[[panel['low_degree_numerators']+row['common_high_degree_numerators'] for panel in row['panels']] for row in source['rows']]
    assert all(c.denominator==1 for row in p for c in row)
    legendre_integers=[[int(c) for c in row] for row in p]
    assert source["aperture"]==native["aperture"]=="1"
    beta=F(100,93)
    ell2=log_rational(F(2),500)/F(2);ell3=log_rational(F(3),500)/F(2)
    ell4=log_rational(F(4),500)/F(2)
    ell5=log_rational(F(5),500)/F(2)
    from certify_native_prime7_translation_panels_100 import translation_panels
    geometry=translation_panels(F(1),logarithm=log_point)
    assert source['panel_endpoints']==geometry['labels']
    cuts=geometry['cuts']
    assert all(x.hi<y.lo for x,y in zip(cuts,cuts[1:]))
    degree=2*max(len(row)-1 for panels in polys for row in panels)
    assert degree==858
    primitives=[endpoint_primitives(t,degree) for t in cuts]
    CS=[[I(0) for _ in range(112)] for _ in range(112)]
    smooth=[[I(0) for _ in range(112)] for _ in range(112)]
    cross=[[I(0) for _ in range(112)] for _ in range(112)]
    bindings=dict(source=hashlib.sha256(source_raw).hexdigest(),
        native=hashlib.sha256(native_path.read_bytes()).hexdigest(),
        constructor=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        geometry=hashlib.sha256((Path(__file__).parent/'certify_native_prime7_translation_panels_100.py').read_bytes()).hexdigest(),
        hankel=hashlib.sha256((Path(__file__).parent/'certify_native_exact_hankel.py').read_bytes()).hexdigest(),
        checkpoint_codec=hashlib.sha256((Path(__file__).parent/'certify_native_prime7_gram112_checkpoint_100.py').read_bytes()).hexdigest(),
        endpoint=hashlib.sha256((Path(__file__).parent/'certify_native_endpoint_log112_100.py').read_bytes()).hexdigest(),
        aperture='1',log_series_terms=500,integration_degree=degree,source_maximum_degree=degree//2)
    start=0
    if checkpoint is not None and Path(checkpoint).exists():
        from certify_native_prime7_gram112_checkpoint_100 import load
        start,matrices=load(checkpoint,bindings,size=112)
        CS,smooth,cross=[matrices[key] for key in ('CS','smooth','cross')]
        print('resumed after panel',start-1,file=__import__('sys').stderr,flush=True)
    for panel in range(start,11):
        print("panel",panel,file=__import__("sys").stderr,flush=True)
        a,b=primitives[panel:panel+2]
        moments=[(b[0][k+1]-a[0][k+1])/I(k+1) for k in range(degree+1)]
        logmoments=[b[1][k]-a[1][k] for k in range(degree+1)]
        # The power and endpoint-log integrands are nonnegative on [0,1].
        moments=[(max(0,lo),hi) for lo,hi in fixed_moments(moments)]
        logmoments=[(max(0,lo),hi) for lo,hi in fixed_moments(logmoments)]
        applied=[moment_apply(polys[j][panel],moments,len(polys[j][panel])) for j in range(112)]
        logapplied=[moment_apply(polys[j][panel],logmoments,112) for j in range(112)]
        def enclosed(coefficients,values,denominator):
            lo,hi=bilinear_bounds(coefficients,values)
            return I(F(lo,2*I.grid*denominator),F(hi,2*I.grid*denominator))
        for i in range(112):
            for n in range(112):
                CS[n][i]+=enclosed(legendre_integers[n],applied[i],coefficient_denominator)
            for j in range(112):
                cross[i][j]+=enclosed(legendre_integers[i],logapplied[j],coefficient_denominator)
            for j in range(i,112):
                smooth[i][j]+=enclosed(polys[i][panel],applied[j],coefficient_denominator**2)
        if checkpoint is not None:
            from certify_native_prime7_gram112_checkpoint_100 import save
            save(checkpoint,bindings,panel+1,dict(CS=CS,smooth=smooth,cross=cross))
            print('checkpointed panel',panel,file=__import__('sys').stderr,flush=True)
    R=[[I(0) for _ in range(112)] for _ in range(112)]
    pairing_error=F(0)
    Q=[[I(*x) for x in row] for row in native['matrix_intervals']]
    for i in range(112):
        for j in range(112):
            pairing=sqrt_rational(F((2*i+1)*(2*j+1)))*(CL[j][i]+CS[j][i])
            difference=pairing-Q[i][j]
            e=max(abs(difference.lo),abs(difference.hi))
            source_allowance=F(source['rows'][i]['normalized_uniform_error'])
            enclosure_width=(pairing.hi-pairing.lo)+(Q[i][j].hi-Q[i][j].lo)
            interval_gap=max(F(0),pairing.lo-Q[i][j].hi,Q[i][j].lo-pairing.hi)
            assert interval_gap<source_allowance
            assert e<source_allowance+enclosure_width
            pairing_error=max(pairing_error,e)
        for j in range(i,112):
            correction=smooth[i][j]+cross[i][j]+cross[j][i]
            correction-=sum(((2*n+1)*(CS[n][i]*CS[n][j]+CL[n][i]*CS[n][j]+CL[n][j]*CS[n][i]) for n in range(112)),I(0))
            R[i][j]=R[j][i]=RL[i][j]+sqrt_rational(F((2*i+1)*(2*j+1)))*correction
    width=max(x.hi-x.lo for row in R for x in row)
    print("Gram width",float(width),file=__import__("sys").stderr,flush=True)
    assert width<F(1,10**55)
    M=sqrt_rational(sum((R[i][i].hi for i in range(112)),F(0))).hi
    eta=F(source['source_map_error_upper']);delta=eta*(2*M+eta)
    assert delta<F(1,10**30)
    G=[[Q[i][j]-beta*R[i][j] for j in range(112)] for i in range(112)]
    result=dict(status='certified full actual 112-source residual Gram at aperture 1',aperture='1',complement_inverse_factor=str(beta),
                physical_degrees=list(range(112)),projected_away_degrees=list(range(112)),
                interval_grid_digits=300,log_series_terms=500,all_mixed_terms_retained=True,
                panel_count=11,integration_degree=degree,source_maximum_degree=degree//2,coefficient_encoding=source["coefficient_encoding"],
                integration_method="exact integer Hankel moments with outward absolute-coefficient radius",
                residual_interval_encoding="exact finite decimal strings on outward grid 10^-300",
                residual_gram_surrogate=[[[fixed_decimal(x.lo),fixed_decimal(x.hi)] for x in row] for row in R],
                maximum_entry_width=str(width),maximum_entry_width_display=float(width),
                source_pairing_error_upper=str(pairing_error),
                pairing_audit_includes_both_enclosure_widths=True,
                pairing_interval_gap_below_actual_source_allowance=True,
                surrogate_residual_map_norm_upper=str(M),actual_gram_operator_error_upper=str(delta),
                source_certificate_sha256=hashlib.sha256(source_raw).hexdigest(),
                native_certificate_sha256=hashlib.sha256(native_path.read_bytes()).hexdigest(),
                native_source_pairing_count=12544,physical_complement_lower="93/100",
                whole_domain_positivity=False,
                global_endpoint_excluded=False,f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)
    result.update(full_source_gram_certified=True,corrected_schur_sign_certified=False,
        no_lift_estimator_status='complete Gram; separate corrected sign pending',
        gram_constructor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        complete_panel_checkpoint_sha256=None if checkpoint is None else hashlib.sha256(Path(checkpoint).read_bytes()).hexdigest(),
        extraction_stage='native complete Gram output before any sign decision')
    return result

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoint')
    args=parser.parse_args()
    print(json.dumps(certificate(args.checkpoint),indent=2))
