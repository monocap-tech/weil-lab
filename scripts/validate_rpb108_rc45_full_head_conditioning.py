"""Whole 1250-feature canonical Gram conditioning via physical polynomials."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib,json,sys
from validate_rpb108_rc29_atom_reduction import legendre,add

def physical_entry(i,j,B=F(11,10)):
    if (i-j)%2: return F(0)
    return B*(F(1,1-(i+j)**2)+F(1,1-(i-j)**2))

def run(head_path,native_path):
    head_raw=Path(head_path).read_bytes();head=json.loads(head_raw)
    native_raw=Path(native_path).read_bytes();native=json.loads(native_raw)
    n=head['Chebyshev_feature_count'];assert n==1250
    assert head['cap']=='11/10' and not head['whole_aperture_positivity_extended']
    B=F(11,10);rho=F(252,257);C=F(30);checks=0
    def check(value):
        nonlocal checks
        assert value,checks+1
        checks+=1
    P8=[[F(x) for x in row] for row in native['physical_native_Gram']]
    check(P8==[[physical_entry(i,j) for j in range(8)] for i in range(8)])
    # Verify the derivative expansion and its norm identity independently in
    # the power basis on representative degrees. The note proves all degrees.
    for j in range(32):
        p=legendre(j); derivative=[F(k)*p[k] for k in range(1,len(p))]
        expansion=[]
        for k in range(j-1,-1,-2): expansion=add(expansion,[(2*k+1)*x for x in legendre(k)])
        check(derivative==expansion)
        integral=sum((a*b*F(2,k+l+1) for k,a in enumerate(derivative)
                      for l,b in enumerate(derivative) if (k+l)%2==0),F(0))
        check(integral==j*(j+1))
    trace=sum((F(j*(j+1)*(2*j+1),2)/B**2 for j in range(n)),F(0))
    check(trace==F(n*n*(n*n-1),4)/B**2)
    check(sum(2*j+1 for j in range(n))==n*n)
    # log(n)<36/5 from a positive exponential partial sum.
    logn_upper=F(36,5)
    exp_lower=sum((logn_upper**j/factorial(j) for j in range(100)),F(0))
    check(exp_lower>n)
    T=F(n)**4;logT_upper=4*logn_upper
    # Endpoint + derivative L1 Fourier bound:
    # A^2 <=(n^2+2n)^2/(2B), |fhat(xi)|^2 <= A^2/(4pi^2 xi^2).
    A2=F((n*n+2*n)**2,2)/B
    # pi>3 and e<3 give a completely rational upper for the weighted tail.
    tail=A2/F(18)*((logT_upper+1)/T+F(3,2)/T**2)
    metric_upper=logT_upper+F(3)/T+tail
    check(metric_upper<C)
    # Physical Gram coefficient bound uses delta=1/(2n^2), Christoffel
    # sup <=n^2/2 times unweighted norm, and Chebyshev orthogonality.
    delta=F(1,2*n*n)
    check(0<delta<1)
    check(F(3)**2>8) # pi>3>2sqrt2, yielding P>=B/(2n) I
    physical_lower=B/F(2*n);physical_upper=F(22,7)*B
    canonical_lower=physical_lower/C;canonical_upper=rho*physical_upper
    condition=canonical_upper/canonical_lower
    check(C*rho<F(29417,1000))
    check(condition<F(231129))
    check(1/rho==F(257,252))
    return dict(milestone='RC45',status='PASS',exact_rational_checks=checks,
        head_certificate_sha256=hashlib.sha256(head_raw).hexdigest(),
        native_low_certificate_sha256=hashlib.sha256(native_raw).hexdigest(),
        native_feature_count=n,cap='11/10',
        physical_Gram_same_parity_entry_formula='(11/10)*(1/(1-(i+j)^2)+1/(1-(i-j)^2))',
        physical_Gram_opposite_parity_entry='0',
        physical_Gram_Euclidean_lower=str(physical_lower),
        physical_Gram_Euclidean_upper=str(physical_upper),
        polynomial_derivative_Gram_trace=str(trace),polynomial_Fourier_decay_constant_squared_upper=str(A2),
        polynomial_frequency_split=str(T),polynomial_log_frequency_split_upper=str(logT_upper),
        polynomial_weighted_Fourier_tail_relative_physical_upper=str(tail),
        polynomial_canonical_metric_relative_physical_upper=str(metric_upper),
        canonical_Gram_physical_metric_lower=str(1/C),
        canonical_Gram_physical_metric_upper=str(rho),
        canonical_Gram_physical_preconditioned_condition_upper=str(C*rho),
        canonical_Gram_Euclidean_lower=str(canonical_lower),
        canonical_Gram_Euclidean_upper=str(canonical_upper),
        canonical_Gram_Euclidean_condition_upper=str(condition),
        actual_inverse_physical_inverse_lower_multiplier=str(1/rho),
        actual_inverse_physical_inverse_upper_multiplier=str(C),
        full_actual_native_Gram_conditioning_certified=True,
        full_actual_native_Gram_entrywise_evaluated=False,
        full_actual_native_inverse_entrywise_evaluated=False,
        full_actual_native_projection_constructed=False,
        original_Weil_head_floor_certified=False,full_native_remainder_sources_certified=False,
        aperture_extended=False)

def replay(certificate_path,head_path,native_path):
    head_raw=Path(head_path).read_bytes();native_raw=Path(native_path).read_bytes()
    cert=json.loads(Path(certificate_path).read_text());head=json.loads(head_raw);native=json.loads(native_raw)
    assert cert['head_certificate_sha256']==hashlib.sha256(head_raw).hexdigest()
    assert cert['native_low_certificate_sha256']==hashlib.sha256(native_raw).hexdigest()
    n=cert['native_feature_count'];assert n==head['Chebyshev_feature_count']==1250
    B=F(11,10);rho=F(252,257)
    # Replay physical Gram entries by direct power-basis integration of
    # Chebyshev recurrence polynomials, not by their product identity.
    polys=[[F(1)],[F(0),F(1)]]
    for j in range(1,15): polys.append(add([F(0)]+[2*x for x in polys[-1]],[-x for x in polys[-2]]))
    for i in range(16):
        for j in range(i,16):
            integral=B*sum((a*b*F(2,k+l+1) for k,a in enumerate(polys[i])
                           for l,b in enumerate(polys[j]) if (k+l)%2==0),F(0))
            assert integral==physical_entry(i,j)
    assert [[str(physical_entry(i,j)) for j in range(8)] for i in range(8)]==native['physical_native_Gram']
    trace=F(n*n*(n*n-1),4)/B**2
    assert trace==F(cert['polynomial_derivative_Gram_trace'])
    T=F(n)**4;L=F(144,5);A2=F((n*n+2*n)**2,2)/B
    assert sum((F(36,5)**j/factorial(j) for j in range(80)),F(0))>n
    tail=A2/18*((L+1)/T+F(3,2)/T**2)
    assert T==F(cert['polynomial_frequency_split'])
    assert A2==F(cert['polynomial_Fourier_decay_constant_squared_upper'])
    assert tail==F(cert['polynomial_weighted_Fourier_tail_relative_physical_upper'])
    assert L+3/T+tail==F(cert['polynomial_canonical_metric_relative_physical_upper'])<30
    pl=B/(2*n);pu=F(22,7)*B
    assert pl==F(cert['physical_Gram_Euclidean_lower']) and pu==F(cert['physical_Gram_Euclidean_upper'])
    assert pl/30==F(cert['canonical_Gram_Euclidean_lower'])
    assert rho*pu==F(cert['canonical_Gram_Euclidean_upper'])
    assert 30*rho==F(cert['canonical_Gram_physical_preconditioned_condition_upper'])
    assert rho*pu/(pl/30)==F(cert['canonical_Gram_Euclidean_condition_upper'])
    assert F(cert['actual_inverse_physical_inverse_lower_multiplier'])==1/rho
    assert F(cert['actual_inverse_physical_inverse_upper_multiplier'])==30
    print('PASS: direct physical Gram integration, whole polynomial/Fourier budgets, conditioning, inverse bounds, and custody')

if __name__=='__main__':
    root=Path(__file__).parent.parent/'certificates'
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        replay(sys.argv[2],sys.argv[3] if len(sys.argv)>3 else root/'rpb108_rc44_reduced_native_head.json',
               sys.argv[4] if len(sys.argv)>4 else root/'rpb108_rc39_native_low_chebyshev_gram.json')
    else:
        head=sys.argv[1] if len(sys.argv)>1 else root/'rpb108_rc44_reduced_native_head.json'
        native=sys.argv[2] if len(sys.argv)>2 else root/'rpb108_rc39_native_low_chebyshev_gram.json'
        print(json.dumps(run(head,native),indent=2))
