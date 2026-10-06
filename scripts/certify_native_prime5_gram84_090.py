"""Actual 84-source residual Gram and rigorous no-lift sign decision."""
import json,hashlib
from pathlib import Path
from certify_native_legendre_small_window import F,I,positive_pivots
from certify_native_exact_logarithm import log_rational
from certify_native_exact_hankel import moment_apply,bilinear_bounds
import certify_native_endpoint_log_gram as endpoint
from certify_native_endpoint_log_gram import exact_log_data
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
from certify_native_prime5_integrated_complement84_090 import certificate as complement_certificate


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


def certificate():
    previous=I.grid;I.grid=10**300;log_point.cache_clear()
    try:
        return compute()
    finally:
        I.grid=previous;log_point.cache_clear()


def compute():
    complement=complement_certificate()
    assert complement["physical_lower"]=="149/250" and complement["complement_inverse_factor"]=="250/149"
    root=Path(__file__).resolve().parents[1]/'notes/data'
    source_path=root/'RPB108_PRIME5_SOURCE84_090_CERTIFICATE_20261006.json'
    native_path=root/'RPB108_PRIME5_MATRIX84_090_COMPACT80_20261006.json'
    source=json.loads(source_path.read_text());native=json.loads(native_path.read_text())
    assert native['matrix_encoding']=='row-major lower triangle integer endpoints on grid 10^-80'
    triangle=native['lower_triangle_row_major'];assert len(triangle)==3570
    entries=[[None for _ in range(84)] for _ in range(84)];index=0
    for i in range(84):
        for j in range(i+1):
            pair=[str(F(int(x),10**80)) for x in triangle[index]]
            entries[i][j]=entries[j][i]=pair;index+=1
    native['matrix_intervals']=entries
    assert len(source['rows'])==84 and native['physical_degrees']==list(range(84))
    old_mul=endpoint.mul;old_sqrt=endpoint.sqrt_rational
    endpoint.mul=mul;endpoint.sqrt_rational=sqrt_rational
    try:p,CL,RL=exact_log_data(83,84)
    finally:endpoint.mul=old_mul;endpoint.sqrt_rational=old_sqrt
    print("endpoint Gram done",file=__import__("sys").stderr,flush=True)
    assert source['coefficient_encoding']=='integer numerators with common decimal denominator and row tail'
    coefficient_denominator=10**source['coefficient_grid_digits']
    polys=[[panel['low_degree_numerators']+row['common_high_degree_numerators'] for panel in row['panels']] for row in source['rows']]
    assert all(c.denominator==1 for row in p for c in row)
    legendre_integers=[[int(c) for c in row] for row in p]
    assert source["aperture"]==native["aperture"]=="9/10"
    beta=F(250,149)
    ell2=log_rational(F(2),500)/F(9,5);ell3=log_rational(F(3),500)/F(9,5)
    ell4=log_rational(F(4),500)/F(9,5)
    ell5=log_rational(F(5),500)/F(9,5)
    from certify_native_translation_panel_order import translation_panels
    geometry=translation_panels(F(9,10),logarithm=log_point)
    assert source['panel_endpoints']==geometry['labels']
    cuts=geometry['cuts']
    assert all(x.hi<y.lo for x,y in zip(cuts,cuts[1:]))
    degree=2*max(len(row)-1 for panels in polys for row in panels)
    primitives=[endpoint_primitives(t,degree) for t in cuts]
    CS=[[I(0) for _ in range(84)] for _ in range(84)]
    smooth=[[I(0) for _ in range(84)] for _ in range(84)]
    cross=[[I(0) for _ in range(84)] for _ in range(84)]
    for panel in range(9):
        print("panel",panel,file=__import__("sys").stderr,flush=True)
        a,b=primitives[panel:panel+2]
        moments=[(b[0][k+1]-a[0][k+1])/I(k+1) for k in range(degree+1)]
        logmoments=[b[1][k]-a[1][k] for k in range(degree+1)]
        # The power and endpoint-log integrands are nonnegative on [0,1].
        moments=[(max(0,lo),hi) for lo,hi in fixed_moments(moments)]
        logmoments=[(max(0,lo),hi) for lo,hi in fixed_moments(logmoments)]
        applied=[moment_apply(polys[j][panel],moments,len(polys[j][panel])) for j in range(84)]
        logapplied=[moment_apply(polys[j][panel],logmoments,84) for j in range(84)]
        def enclosed(coefficients,values,denominator):
            lo,hi=bilinear_bounds(coefficients,values)
            return I(F(lo,2*I.grid*denominator),F(hi,2*I.grid*denominator))
        for i in range(84):
            for n in range(84):
                CS[n][i]+=enclosed(legendre_integers[n],applied[i],coefficient_denominator)
            for j in range(84):
                cross[i][j]+=enclosed(legendre_integers[i],logapplied[j],coefficient_denominator)
            for j in range(i,84):
                smooth[i][j]+=enclosed(polys[i][panel],applied[j],coefficient_denominator**2)
    R=[[I(0) for _ in range(84)] for _ in range(84)]
    pairing_error=F(0)
    Q=[[I(*x) for x in row] for row in native['matrix_intervals']]
    for i in range(84):
        for j in range(84):
            pairing=sqrt_rational(F((2*i+1)*(2*j+1)))*(CL[j][i]+CS[j][i])
            difference=pairing-Q[i][j]
            e=max(abs(difference.lo),abs(difference.hi))
            assert e<F(source['rows'][i]['normalized_uniform_error'])
            pairing_error=max(pairing_error,e)
        for j in range(i,84):
            correction=smooth[i][j]+cross[i][j]+cross[j][i]
            correction-=sum(((2*n+1)*(CS[n][i]*CS[n][j]+CL[n][i]*CS[n][j]+CL[n][j]*CS[n][i]) for n in range(84)),I(0))
            R[i][j]=R[j][i]=RL[i][j]+sqrt_rational(F((2*i+1)*(2*j+1)))*correction
    width=max(x.hi-x.lo for row in R for x in row)
    print("Gram width",float(width),file=__import__("sys").stderr,flush=True)
    assert width<F(1,10**55)
    M=sqrt_rational(sum((R[i][i].hi for i in range(84)),F(0))).hi
    eta=F(source['source_map_error_upper']);delta=eta*(2*M+eta)
    assert delta<F(1,10**30)
    G=[[Q[i][j]-beta*R[i][j] for j in range(84)] for i in range(84)]
    result=dict(status='certified full actual 84-source residual Gram at aperture 9/10',aperture='9/10',complement_inverse_factor=str(beta),
                physical_degrees=list(range(84)),projected_away_degrees=list(range(84)),
                interval_grid_digits=300,log_series_terms=500,all_mixed_terms_retained=True,
                panel_count=9,coefficient_encoding=source["coefficient_encoding"],
                integration_method="exact integer Hankel moments with outward absolute-coefficient radius",
                residual_interval_encoding="exact finite decimal strings on outward grid 10^-300",
                residual_gram_surrogate=[[[fixed_decimal(x.lo),fixed_decimal(x.hi)] for x in row] for row in R],
                maximum_entry_width=str(width),maximum_entry_width_display=float(width),
                source_pairing_error_upper=str(pairing_error),
                surrogate_residual_map_norm_upper=str(M),actual_gram_operator_error_upper=str(delta),
                source_certificate_sha256=hashlib.sha256(source_path.read_bytes()).hexdigest(),
                native_certificate_sha256=hashlib.sha256(native_path.read_bytes()).hexdigest(),
                native_source_pairing_count=7056,physical_complement_lower="149/250",
                logarithmic_complement_lower="9/100",whole_domain_positivity=False,
                global_endpoint_excluded=False,f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)
    try:
        positive_pivots(G);v=None
    except ArithmeticError:
        v=negative_candidate(G)
    if v is not None:
        norm2=sum((x*x for x in v),F(0))
        value=sum((v[i]*G[i][j]*v[j] for i in range(84) for j in range(84)),I(0))
        upper=value.hi+beta*delta*norm2
        assert upper<0
        raw_value=sum((v[i]*Q[i][j]*v[j] for i in range(84) for j in range(84)),I(0))
        assert raw_value.lo>0
        result.update(no_lift_estimator_status='certified negative direction of actual Q84-(250/149)R84 estimator',
                      estimator_negative_vector=[str(x) for x in v],
                      actual_estimator_quadratic_upper=str(upper),
                      actual_estimator_rayleigh_upper=str(upper/norm2),
                      required_inverse_slack_lower_bound=str(-upper),
                      same_vector_raw_quadratic_lower=str(raw_value.lo),
                      actual_negative_witness=False,corrected_schur_sign_certified=False)
    else:
        tau=F(native["raw_physical_coercivity_lower_bound"])
        while True:
            lower=[row[:] for row in G]
            for i in range(84):lower[i][i]-=beta*delta+tau
            try:
                pivots=positive_pivots(lower);break
            except ArithmeticError:
                if tau<F(1,10**60):raise
                tau/=2
        result.update(no_lift_estimator_status='certified positive actual corrected form',
                      corrected_coercivity_lower_bound=str(tau),
                      shifted_pivot_lower_bounds=[str(x.lo) for x in pivots],
                      corrected_schur_sign_certified=True,whole_domain_positivity=True)
        lift2=beta**2*(sum((R[i][i].hi for i in range(84)),F(0))+delta)
        lift_integer=1
        while lift_integer**2<=lift2:lift_integer+=1
        whole=tau*F(149,250)/(tau+F(149,250)*(1+lift_integer**2))
        assert whole<=F(149,250)
        broken=[row[:] for row in lower];broken[0][0]=I(-1)
        try:positive_pivots(broken)
        except ArithmeticError:pass
        else:raise AssertionError('Negative control accepted')
        result.update(lift_norm_squared_upper=str(lift2),lift_operator_norm_integer_upper=lift_integer,
                      whole_domain_physical_coercivity_lower=str(whole),logarithmic_coercivity_lower=str(whole/(10*(whole+23))),negative_control_rejected=True,
                      fixed_aperture_weak_kernel_zero=True,fixed_aperture_unit_domination=True,
                      global_endpoint_excluded=False,f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)
    return result


if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))

