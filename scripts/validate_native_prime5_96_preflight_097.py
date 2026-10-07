"""Independent recurrence, endpoint, infinite-tail and width audit for 96 moments."""
import gzip,hashlib,json
from math import factorial,prod
from pathlib import Path
from certify_native_legendre_small_window import F,I,atan,log_rational
from validate_native_prime5_depth6_complement_097 import polynomial

def certificate(path):
    raw=Path(path).read_bytes();c=json.loads(raw)
    assert c['aperture']=='97/100' and c['retained_vectors']==96
    assert c['physical_degrees']==list(range(96))
    root=Path(__file__).resolve().parents[1]/'notes/data'
    prime_raw=gzip.decompress((root/c['prime_input_file']).read_bytes())
    assert hashlib.sha256(prime_raw).hexdigest()==c['prime_input_uncompressed_sha256']
    norm=F(json.loads(prime_raw)['joint_prime_operator_norm_upper'])
    assert norm==F(c['combined_prime_upper'])==F(444727,250000)
    a=F(97,100);k=96;old=I.grid;I.grid=10**120
    try:
        pi=16*atan(F(1,5),180)-4*atan(F(1,239),180)
        cuts=list(map(F,c['cutoffs']));assert cuts==[F(14),F(74,5),F(77,5)]
        highs=[log_rational(t,350)-F(7,216)/t**2 for t in cuts]
    finally:I.grid=old
    intervals=[tuple(map(F,p)) for p in c['archimedean_high_intervals']]
    assert all(lo<=h.lo<=h.hi<=hi for (lo,hi),h in zip(intervals,highs))
    assert all(0<x[0]<=x[1]<y[0] for x,y in zip(intervals,intervals[1:]))
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
    lower=arch-norm-pole;assert lower==F(c['physical_unrounded_lower'])>F(c['physical_lower'])>F(17,20)
    for region in range(4):
        flags=[int(region<=i) for i in range(3)]
        step=intervals[-1][0]-(intervals[0][1]+F(27,5))*flags[0]
        for i in range(1,3):step-=(intervals[i][1]-intervals[i-1][0])*flags[i]
        assert step<=(-F(27,5) if region==0 else intervals[region-1][0])
    assert c['highest_diagonal_only'] and c['full_entry_widths_pending']
    assert F(c['obsolete_diagonal_truncation_width'])>F(1,10**35)>F(c['repaired_diagonal_truncation_width'])
    assert all(c[key] is False for key in ['native96_finite_sign','source96_map','gram96_complete','whole_domain_positivity_at_097','f4_closed','lean_formalized'])
    return dict(certificate_sha256=hashlib.sha256(raw).hexdigest(),aperture='97/100',retained_vectors=96,
        independent_degree_mass_bounds_verified=checks,complete_infinite_tails_verified=3,
        finer_machin_and_logarithm_enclosures_verified=True,pointwise_step_regions_verified=4,
        complement_lower=c['physical_lower'],complement_unrounded_display=float(lower),
        diagonal_width_thresholds_checked=True,all_native_entry_widths_pending=True,
        whole_domain_positivity_at_097=False,whole_domain_frontier='24/25',f4_closed=False)

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(sys.argv[1]),indent=2))
