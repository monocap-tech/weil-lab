"""Independent recurrence, endpoint, infinite-tail and width audit for 112 moments."""
import gzip,hashlib,json
from math import factorial,prod,comb,lcm
from pathlib import Path
from certify_native_legendre_small_window import F,I,atan,log_rational
from validate_native_prime5_depth6_complement_097 import polynomial

def certificate(path):
    raw=Path(path).read_bytes();c=json.loads(raw)
    assert c['aperture']=='199/200' and c['retained_vectors']==112
    assert c['physical_degrees']==list(range(112))
    root=Path(__file__).resolve().parents[1]/'notes/data'
    prime_raw=gzip.decompress((root/c['prime_input_file']).read_bytes())
    assert hashlib.sha256(prime_raw).hexdigest()==c['prime_input_uncompressed_sha256']
    norm=F(json.loads(prime_raw)['joint_prime_operator_norm_upper'])
    assert norm==F(c['combined_prime_upper']) and 0<norm<2
    assert json.loads(prime_raw)['prime_powers']==[2,3,4,5,7]
    a=F(199,200);k=112;old=I.grid;I.grid=10**120
    try:
        pi=16*atan(F(1,5),180)-4*atan(F(1,239),180)
        cuts=list(map(F,c['cutoffs']));assert cuts==[F(16),F(17),F(179,10)]
        highs=[log_rational(t,350)-F(7,216)/t**2 for t in cuts]
    finally:I.grid=old
    intervals=[tuple(map(F,p)) for p in c['archimedean_high_intervals']]
    assert all(lo<=h.lo<=h.hi<=hi for (lo,hi),h in zip(intervals,highs))
    assert all(0<x[0]<=x[1]<y[0] for x,y in zip(intervals,intervals[1:]))
    assert c['invalid_region_controls_rejected']==[[96,'16'],[112,'18']]
    for size,T in [(96,F(16)),(112,F(18))]:
        assert (2*a*T*pi.lo)**2>=size*(size+1)
    checks=0
    for T,rho_text,d in zip(cuts,c['frequency_masses_upper'],c['complete_mass_details']):
        assert d['degrees']==list(range(k,k+48)) and d['iteration_depth']==6
        U=F(d['positive_region_argument_squared_upper']);assert (2*a*T*pi.hi)**2<=U<k*(k+1)
        Ylo=2*a*T*pi.lo
        for i,n in enumerate(d['degrees']):
            H=polynomial(n,6)
            rate_exact=F(2*n+1)-sum((power*v*U**(power//2) for power,v in H.items()),F(0))
            rate=F(d['integrated_rate_lower'][i]);assert rate==F((rate_exact*10**80).__floor__(),10**80)>0
            exponent=F(d['squared_damping_exponent_lower'][i])
            assert 0<exponent<=sum((v*Ylo**power for power,v in H.items()),F(0))
            term=F(1);den=term
            for j in range(1,101):term*=exponent/j;den+=term
            D=prod(range(1,2*n+2,2))
            assert F(d['individual_integrated_term_upper'][i])>=4*a*T*(2*n+1)*U**n/(rate*D*D*den)
            checks+=1
        tail_degree=k+48;upper=2*a*F(22,7)*T
        D=prod(range(1,2*tail_degree+2,2));ratio=upper**2/F((2*tail_degree+1)*(2*tail_degree+3))
        tail=F(d['infinite_undamped_tail_upper']);assert 0<ratio<1
        assert tail>=4*a*T*upper**(2*tail_degree)/(D*D*(1-ratio))
        assert F(rho_text)==sum(map(F,d['individual_integrated_term_upper']),F(0))+tail
    masses=list(map(F,c['frequency_masses_upper']))
    arch=intervals[-1][0]-(intervals[0][1]+F(27,5))*masses[0]
    for i in range(1,3):arch-=(intervals[i][1]-intervals[i-1][0])*masses[i]
    pole=16*a*(a/2)**(2*k)/factorial(k)**2
    assert pole==F(c['pole_absolute_upper']) and arch==F(c['three_band_archimedean_lower'])
    lower=arch-norm-pole;assert lower==F(c['physical_unrounded_lower'])>F(c['physical_lower'])>F(3,4)
    for region in range(4):
        flags=[int(region<=i) for i in range(3)]
        step=intervals[-1][0]-(intervals[0][1]+F(27,5))*flags[0]
        for i in range(1,3):step-=(intervals[i][1]-intervals[i-1][0])*flags[i]
        assert step<=(-F(27,5) if region==0 else intervals[region-1][0])
    assert c['highest_diagonal_only'] and c['full_entry_widths_pending']
    assert c['exponential_remainder_bound']==54 and F(c['kernel_remainder_bound'])==5*a
    saved=I.grid;I.grid=10**140
    try:assert log_rational(F(5),450).hi<4*a<log_rational(F(54),450).lo and 4*a<6
    finally:I.grid=saved
    assert c['rejected_exponential_guards']==[49,50,51,52,53]
    saved=I.grid;I.grid=10**140
    try:assert log_rational(F(53),450).hi<4*a<log_rational(F(54),450).lo
    finally:I.grid=saved
    saved=I.grid;I.grid=10**140
    try:assert 2*log_rational(F(7),450).hi<4*a
    finally:I.grid=saved
    n=111
    coefficients=[0]*(n+1)
    for r in range(n//2+1):coefficients[n-2*r]=(-1)**r*comb(n,r)*comb(2*n-2*r,n)
    common=lcm(*range(1,2*n+2));out=[0]*(2*n+2)
    # Direct binomial evaluation of both integration endpoints, without Horner.
    for i,ci in enumerate(coefficients):
        if not ci:continue
        for j,cj in enumerate(coefficients):
            if not cj:continue
            for k in range(j+1):
                d=i+j-k+1;value=ci*cj*comb(j,k)*(-1)**k*(common//d)
                out[k]+=value
                for ell in range(d+1):out[k+ell]-=value*comb(d,ell)*(-1)**(d-ell)
    correlation=[F(x,2**(2*n)*common) for x in out]
    physical=[a*x*2**j for j,x in enumerate(correlation)]
    delta=2*a/F(2*n+1)
    assert physical[0]==delta
    L=4*a;mass=sum(map(abs,physical));abound=F(3,4)*L*delta+sum(map(abs,physical[1:]))
    def width(N,K):
        exp=54*L**(N+1)/factorial(N+1)*(delta+mass/F(4**(N+1)))
        bernoulli=4*(L/6)**(2*K+2)/(1-(L/6)**2)
        return 2*(5*a*exp+abound*bernoulli)*F(2*n+1)/(2*a)
    assert width(300,300)==F(c['obsolete_diagonal_truncation_width'])
    assert width(360,360)==F(c['repaired_diagonal_truncation_width'])
    assert F(c['obsolete_diagonal_truncation_width'])>F(1,10**35)>F(c['repaired_diagonal_truncation_width'])
    assert all(c[key] is False for key in ['native112_finite_sign','source112_map','gram112_complete','whole_domain_positivity_at_0995','f4_closed','lean_formalized'])
    return dict(certificate_sha256=hashlib.sha256(raw).hexdigest(),aperture='199/200',retained_vectors=112,
        independent_degree_mass_bounds_verified=checks,complete_infinite_tails_verified=3,
        finer_machin_and_logarithm_enclosures_verified=True,pointwise_step_regions_verified=4,
        complement_lower=c['physical_lower'],complement_unrounded_display=float(lower),
        diagonal_width_thresholds_checked=True,independent_binomial_diagonal_budget_verified=True,invalid_positive_regions_rejected=2,all_native_entry_widths_pending=True,
        whole_domain_positivity_at_0995=False,whole_domain_frontier='99/100',f4_closed=False)

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(sys.argv[1]),indent=2))


