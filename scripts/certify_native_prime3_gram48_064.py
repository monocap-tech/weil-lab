"""Actual 48-source residual Gram and rigorous no-lift sign decision."""
import json,hashlib
from pathlib import Path
from certify_native_legendre_small_window import F,I,log_rational,positive_pivots
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

from certify_native_coupled_schur import log_point
from certify_native_prime3_complement48_064 import certificate as complement_certificate


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


def fixed_moments(moments):
    return [(int(x.lo*I.grid),int(x.hi*I.grid)) for x in moments]


def dot(p,moments):
    """Exact linear combination of fixed-grid moment intervals, rounded once."""
    den=lcm(*(c.denominator for c in p));lower=upper=0
    for c,(lo,hi) in zip(p,moments):
        n=c.numerator*(den//c.denominator)
        lower+=n*(lo if n>=0 else hi)
        upper+=n*(hi if n>=0 else lo)
    assert len(p)<=len(moments)
    return I(F(lower,den*I.grid),F(upper,den*I.grid))


def negative_candidate(matrix):
    grid=10**60
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
            return [F((x/scale*10**12+F(1,2)).__floor__(),10**12) for x in v]
        for i in range(k+1,size):
            L[i][k]=rounded(work[i][k]/pivot)
            for j in range(i,size):
                work[i][j]=rounded(work[i][j]-work[i][k]*work[k][j]/pivot)
                work[j][i]=work[i][j]
    return None


def certificate():
    previous=I.grid;I.grid=10**200;log_point.cache_clear()
    try:
        return compute()
    finally:
        I.grid=previous;log_point.cache_clear()


def compute():
    complement=complement_certificate()
    assert complement["physical_lower"]=="24/25" and complement["complement_inverse_factor"]=="25/24"
    root=Path(__file__).resolve().parents[1]/'notes/data'
    source_path=root/'RPB108_PRIME3_SOURCE48_064_CERTIFICATE_20261005.json'
    native_path=root/'RPB108_PRIME3_MATRIX48_064_CERTIFICATE_20261005.json'
    source=json.loads(source_path.read_text());native=json.loads(native_path.read_text())
    assert len(source['rows'])==48 and native['physical_degrees']==list(range(48))
    old_mul=endpoint.mul;old_sqrt=endpoint.sqrt_rational
    endpoint.mul=mul;endpoint.sqrt_rational=sqrt_rational
    try:p,CL,RL=exact_log_data(47,48)
    finally:endpoint.mul=old_mul;endpoint.sqrt_rational=old_sqrt
    print("endpoint Gram done",file=__import__("sys").stderr,flush=True)
    polys=[[[F(c) for c in panel['coefficients']] for panel in row['panels']] for row in source['rows']]
    assert source["aperture"]==native["aperture"]=="16/25"
    beta=F(25,24)
    ell2=log_rational(F(2),220)/F(32,25);ell3=log_rational(F(3),220)/F(32,25)
    cuts=[I(0),I(1)-ell3,I(1)-ell2,ell2,ell3,I(1)]
    degree=2*max(len(row)-1 for panels in polys for row in panels)
    primitives=[endpoint_primitives(t,degree) for t in cuts]
    CS=[[I(0) for _ in range(48)] for _ in range(48)]
    smooth=[[I(0) for _ in range(48)] for _ in range(48)]
    cross=[[I(0) for _ in range(48)] for _ in range(48)]
    for panel in range(5):
        print("panel",panel,file=__import__("sys").stderr,flush=True)
        a,b=primitives[panel:panel+2]
        moments=[(b[0][k+1]-a[0][k+1])/I(k+1) for k in range(degree+1)]
        logmoments=[b[1][k]-a[1][k] for k in range(degree+1)]
        moments=fixed_moments(moments);logmoments=fixed_moments(logmoments)
        for i in range(48):
            for n in range(48):
                CS[n][i]+=dot(mul(p[n],polys[i][panel]),moments)
            for j in range(48):
                cross[i][j]+=dot(mul(p[i],polys[j][panel]),logmoments)
            for j in range(i,48):
                smooth[i][j]+=dot(mul(polys[i][panel],polys[j][panel]),moments)
    R=[[I(0) for _ in range(48)] for _ in range(48)]
    pairing_error=F(0)
    Q=[[I(*x) for x in row] for row in native['matrix_intervals']]
    for i in range(48):
        for j in range(48):
            pairing=sqrt_rational(F((2*i+1)*(2*j+1)))*(CL[j][i]+CS[j][i])
            difference=pairing-Q[i][j]
            e=max(abs(difference.lo),abs(difference.hi))
            assert e<F(source['rows'][i]['normalized_uniform_error'])
            pairing_error=max(pairing_error,e)
        for j in range(i,48):
            correction=smooth[i][j]+cross[i][j]+cross[j][i]
            correction-=sum(((2*n+1)*(CS[n][i]*CS[n][j]+CL[n][i]*CS[n][j]+CL[n][j]*CS[n][i]) for n in range(48)),I(0))
            R[i][j]=R[j][i]=RL[i][j]+sqrt_rational(F((2*i+1)*(2*j+1)))*correction
    width=max(x.hi-x.lo for row in R for x in row)
    assert width<F(1,10**25)
    M=sqrt_rational(sum((R[i][i].hi for i in range(48)),F(0))).hi
    eta=F(source['source_map_error_upper']);delta=eta*(2*M+eta)
    assert delta<F(1,10**20)
    G=[[Q[i][j]-beta*R[i][j] for j in range(48)] for i in range(48)]
    result=dict(status='certified full actual 48-source residual Gram at aperture 16/25',aperture='16/25',complement_inverse_factor=str(beta),
                physical_degrees=list(range(48)),projected_away_degrees=list(range(48)),
                interval_grid_digits=200,log_series_terms=220,all_mixed_terms_retained=True,
                residual_gram_surrogate=[[[str(x.lo),str(x.hi)] for x in row] for row in R],
                maximum_entry_width=str(width),maximum_entry_width_display=float(width),
                source_pairing_error_upper=str(pairing_error),
                surrogate_residual_map_norm_upper=str(M),actual_gram_operator_error_upper=str(delta),
                source_certificate_sha256=hashlib.sha256(source_path.read_bytes()).hexdigest(),
                native_certificate_sha256=hashlib.sha256(native_path.read_bytes()).hexdigest(),
                native_source_pairing_count=2304,physical_complement_lower="24/25",
                logarithmic_complement_lower="9/100",whole_domain_positivity=False,
                global_endpoint_excluded=False,f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)
    try:
        positive_pivots(G);v=None
    except ArithmeticError:
        v=negative_candidate(G)
    if v is not None:
        norm2=sum((x*x for x in v),F(0))
        value=sum((v[i]*G[i][j]*v[j] for i in range(48) for j in range(48)),I(0))
        upper=value.hi+beta*delta*norm2
        assert upper<0
        raw_value=sum((v[i]*Q[i][j]*v[j] for i in range(48) for j in range(48)),I(0))
        assert raw_value.lo>0
        result.update(no_lift_estimator_status='certified negative direction of actual Q48-(25/24)R48 estimator',
                      estimator_negative_vector=[str(x) for x in v],
                      actual_estimator_quadratic_upper=str(upper),
                      actual_estimator_rayleigh_upper=str(upper/norm2),
                      required_inverse_slack_lower_bound=str(-upper),
                      same_vector_raw_quadratic_lower=str(raw_value.lo),
                      actual_negative_witness=False,corrected_schur_sign_certified=False)
    else:
        tau=F(1,10**7)
        while True:
            lower=[row[:] for row in G]
            for i in range(48):lower[i][i]-=beta*delta+tau
            try:
                pivots=positive_pivots(lower);break
            except ArithmeticError:
                if tau<F(1,10**20):raise
                tau/=2
        result.update(no_lift_estimator_status='certified positive actual corrected form',
                      corrected_coercivity_lower_bound=str(tau),
                      shifted_pivot_lower_bounds=[str(x.lo) for x in pivots],
                      corrected_schur_sign_certified=True,whole_domain_positivity=True)
        lift2=beta**2*(sum((R[i][i].hi for i in range(48)),F(0))+delta)
        lift_integer=1
        while lift_integer**2<=lift2:lift_integer+=1
        whole=min(tau/(2*(1+lift_integer**2)),F(12,25))
        assert 2*whole<=F(24,25)
        broken=[row[:] for row in lower];broken[0][0]=I(-1)
        try:positive_pivots(broken)
        except ArithmeticError:pass
        else:raise AssertionError('Negative control accepted')
        result.update(lift_norm_squared_upper=str(lift2),lift_operator_norm_integer_upper=lift_integer,
                      whole_domain_physical_coercivity_lower=str(whole),negative_control_rejected=True,
                      fixed_aperture_weak_kernel_zero=True,fixed_aperture_unit_domination=True,
                      global_endpoint_excluded=False,f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)
    return result


if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))

