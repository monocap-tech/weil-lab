"""Fresh three-band step comparison with complete projected frequency masses."""
import json,hashlib
from pathlib import Path
from certify_native_legendre_small_window import F,I,log_rational
from certify_native_iterated_damped_mass_depth6 import integrated_iterated_mass
EXPECTED = {'RPB108_PRIME5_BASELINE_COMPLEMENT84_097_CERTIFICATE_20261007.json': 'c39e09035931e9965c9e4222aa5fe1a7640533891076effa378c09adda796cbb', 'RPB108_PRIME5_WEIGHTED_POINTWISE_097_CERTIFICATE_20261007.json': 'b349ec2ca617ede3f7bc238abd9b65a56a28e2e9f1265688600b5fdbe912463e'}

def certificate():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    def read(n):
        p=root/n
        return p.read_bytes() if p.exists() else __import__('gzip').decompress(p.with_suffix('.json.gz').read_bytes())
    raw={n:read(n) for n in EXPECTED}
    assert {n:hashlib.sha256(v).hexdigest() for n,v in raw.items()}==EXPECTED
    prior,joint=[json.loads(raw[n]) for n in EXPECTED]
    assert prior['aperture']==joint['aperture']=='97/100'
    norm=F(joint['joint_prime_operator_norm_upper']);assert norm==F(444727,250000)
    old=I.grid;I.grid=10**80
    try:
        cuts=[F(64,5),F(67,5),F(69,5)]
        high=[log_rational(t)-F(7,216)/t**2 for t in cuts]
        assert all(0<x.lo<=x.hi<y.lo for x,y in zip(high,high[1:]))
        mass=[];certs=[]
        separated=F(prior['joint_prime24_operator_upper'])+F(prior['joint_prime35_operator_upper'])
        pole=F(prior['pole_absolute_upper'])
        for t,h in zip(cuts,high):
            rho,details=integrated_iterated_mass(F(97,100),84,t,depth=6)
            legacy=h.lo-(F(27,5)+h.lo)*rho-separated-pole
            rounded=F((legacy*10**6).__floor__(),10**6);assert rounded<legacy and rounded!=0
            cert=dict(prior)
            cert.update(physical_cutoff=str(t),physical_low_frequency_mass_upper=str(rho),
                iterated_damping_details=details,physical_unrounded_lower=str(legacy),
                physical_lower=str(rounded),complement_inverse_factor=str(1/rounded),
                single_band_positive_lower_claimed=False)
            mass.append(rho);certs.append(cert)
        assert 0<mass[0]<mass[1]<mass[2]
        arch=high[-1].lo-(high[0].hi+F(27,5))*mass[0]
        for k in range(1,3):arch-=(high[k].hi-high[k-1].lo)*mass[k]
        lower=arch-norm-pole;c=F(4,5);assert lower>c
        return dict(aperture='97/100',input_sha256=EXPECTED,cutoffs=list(map(str,cuts)),
            archimedean_high_intervals=[[str(h.lo),str(h.hi)] for h in high],
            complete_mass_certificates=certs,frequency_masses_upper=list(map(str,mass)),
            three_band_archimedean_lower=str(arch),combined_prime_upper=str(norm),
            pole_absolute_upper=str(pole),physical_unrounded_lower=str(lower),
            physical_lower=str(c),complement_inverse_factor=str(1/c),
            physical_lower_display=float(lower),logarithmic_lower=prior['logarithmic_lower'],
            all_single_band_values_are_intermediates=True,whole_domain_positivity=False,
            matching_native_source_gram_sign_pending=True,f4_entry_closed=False,lean_formalized=False)
    finally:I.grid=old

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
