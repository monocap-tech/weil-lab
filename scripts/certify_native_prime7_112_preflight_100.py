"""Prime-7 112-moment complement and degree-111 truncation preflight at 1."""
import gzip,hashlib,json
from pathlib import Path
from math import factorial
from certify_native_legendre_small_window import F,I,legendre,log_rational
from certify_native_exact_polynomial import correlation
from certify_native_iterated_damped_mass_depth6 import integrated_iterated_mass

EXPECTED_PRIME_SHA256 = 'ebc844d726eea10225ae773e4d0368a78993d4bcf3b6eda79cbe634f64483ae4'

def certificate():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    name='RPB108_PRIME7_WEIGHTED_DEPTH10_100_CERTIFICATE_20261007.json.gz'
    raw=gzip.decompress((root/name).read_bytes());prime=json.loads(raw)
    assert hashlib.sha256(raw).hexdigest()==EXPECTED_PRIME_SHA256
    assert prime['aperture']=='1' and prime['prime_powers']==[2,3,4,5,7]
    norm=F(prime['joint_prime_operator_norm_upper']);assert 0<norm<2
    a=F(1);k=112;cuts=[F(16),F(17),F(179,10)]
    old=I.grid;I.grid=10**80
    try:
        high=[log_rational(t)-F(7,216)/t**2 for t in cuts]
        masses=[];details=[]
        for t in cuts:
            rho,d=integrated_iterated_mass(a,k,t,depth=6)
            masses.append(rho);details.append(d)
        assert 0<masses[0]<masses[1]<masses[2]
        arch=high[-1].lo-(high[0].hi+F(27,5))*masses[0]
        for i in range(1,len(cuts)):arch-=(high[i].hi-high[i-1].lo)*masses[i]
        pole=16*a*(a/2)**(2*k)/factorial(k)**2
        lower=arch-norm-pole
        rounded=F((lower*1000).__floor__(),1000)
        assert lower>rounded>F(3,4)
        rejected=[]
        for size,cut in [(96,F(16)),(112,F(18))]:
            try:integrated_iterated_mass(a,size,cut,depth=6)
            except ValueError:rejected.append([size,str(cut)])
            else:raise AssertionError('Invalid positive-region control accepted')
    finally:I.grid=old
    n=111;L=4*a
    assert log_rational(F(5)).hi<L<log_rational(F(55)).lo and L<6
    assert log_rational(F(54)).hi<L<log_rational(F(55)).lo
    assert 2*log_rational(F(7)).hi<L
    p=legendre(n)[n]
    c=[a*x*2**j for j,x in enumerate(correlation(p,p))]
    delta=2*a/F(2*n+1);assert c[0]==delta
    mass=sum(map(abs,c));abound=F(3,4)*L*delta+sum(map(abs,c[1:]))
    def width(N,K):
        e=55*L**(N+1)/factorial(N+1)*(delta+mass/F(4**(N+1)))
        b=4*(L/6)**(2*K+2)/(1-(L/6)**2)
        return 2*(5*a*e+abound*b)*F(2*n+1)/(2*a)
    obsolete=width(300,300);repaired=width(360,360)
    assert obsolete>F(1,10**35)>repaired
    return dict(aperture='1',retained_vectors=k,physical_degrees=list(range(k)),
        prime_input_file=name,prime_input_uncompressed_sha256=hashlib.sha256(raw).hexdigest(),
        combined_prime_upper=str(norm),cutoffs=list(map(str,cuts)),
        archimedean_high_intervals=[[str(h.lo),str(h.hi)] for h in high],
        frequency_masses_upper=list(map(str,masses)),complete_mass_details=details,
        three_band_archimedean_lower=str(arch),pole_absolute_upper=str(pole),
        physical_unrounded_lower=str(lower),physical_lower=str(rounded),
        physical_lower_display=float(lower),invalid_region_controls_rejected=rejected,
        rejected_exponential_guards=[49,50,51,52,53,54],exponential_remainder_bound=55,kernel_remainder_bound=str(5*a),
        highest_degree=111,obsolete_orders=[300,300],proposed_orders=[360,360],
        obsolete_diagonal_truncation_width=str(obsolete),repaired_diagonal_truncation_width=str(repaired),
        obsolete_width_display=float(obsolete),repaired_width_display=float(repaired),
        highest_diagonal_only=True,full_entry_widths_pending=True,
        complement_only=True,native112_finite_sign=False,source112_map=False,
        gram112_complete=False,whole_domain_positivity_at_100=False,
        whole_domain_frontier='399/400',f4_closed=False,lean_formalized=False)

if __name__=='__main__':print(json.dumps(certificate(),indent=2))


