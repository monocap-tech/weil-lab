"""Two-band archimedean comparison on the unchanged 84-moment complement."""
import hashlib,json
from pathlib import Path
from certify_native_legendre_small_window import F,I,log_rational
from certify_native_iterated_damped_mass_depth6 import integrated_iterated_mass

def certificate():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    raw=(root/'RPB108_PRIME5_BASELINE_COMPLEMENT84_093_CERTIFICATE_20261006.json').read_bytes()
    prior=json.loads(raw);assert prior['aperture']=='93/100'
    old=I.grid;I.grid=10**80
    try:
        S=F(13);T=F(71,5);assert 1<=S<T
        rho,detail=integrated_iterated_mass(F(93,100),84,S,depth=6)
        def high(t):return log_rational(t)-F(7,216)/t**2
        gs,gt=high(S),high(T);assert 0<gs.lo<gs.hi<gt.lo
        outer,outer_detail=integrated_iterated_mass(F(93,100),84,T,depth=6);assert 0<rho<outer
        loss=F(prior['joint_prime24_operator_upper'])+F(prior['joint_prime35_operator_upper'])
        pole=F(prior['pole_absolute_upper'])
        lower=gt.lo-(gt.hi-gs.lo)*outer-(gs.hi+F(27,5))*rho-loss-pole
        c=F(2,3);assert lower>c
        # Keep the legacy single-band inner certificate for independent reuse
        # of all degree, tail, normalization and positive-region audits.
        inner=dict(prior)
        legacy=gs.lo-(F(27,5)+gs.lo)*rho-loss-pole
        ci=F((legacy*10**6).__floor__(),10**6);assert 0<ci<legacy
        inner.update(physical_cutoff=str(S),physical_low_frequency_mass_upper=str(rho),
            iterated_damping_details=detail,physical_unrounded_lower=str(legacy),
            physical_lower=str(ci),complement_inverse_factor=str(1/ci))
        outer_cert=dict(prior)
        outer_legacy=gt.lo-(F(27,5)+gt.lo)*outer-loss-pole
        co=F((outer_legacy*10**6).__floor__(),10**6);assert 0<co<outer_legacy
        outer_cert.update(physical_cutoff=str(T),physical_low_frequency_mass_upper=str(outer),
            iterated_damping_details=outer_detail,physical_unrounded_lower=str(outer_legacy),
            physical_lower=str(co),complement_inverse_factor=str(1/co))
        result=dict(outer_cert)
        result.update(status='certified two-band complement only; matching sign separate',
            previous_complement_sha256=hashlib.sha256(raw).hexdigest(),inner_cutoff=str(S),
            inner_mass_upper=str(rho),inner_mass_certificate=inner,outer_mass_certificate=outer_cert,
            inner_archimedean_high_interval=[str(gs.lo),str(gs.hi)],
            outer_archimedean_high_interval=[str(gt.lo),str(gt.hi)],
            two_band_archimedean_lower=str(lower+loss+pole),
            physical_unrounded_lower=str(lower),physical_lower=str(c),
            complement_inverse_factor=str(1/c),physical_lower_display=float(lower),
            whole_domain_positivity_frontier='91/100',whole_domain_positivity=False)
        return result
    finally:I.grid=old

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
