"""Ceiling for the degree-84 positive-region step method with fixed prime loss."""
import hashlib,json
from pathlib import Path
from certify_native_legendre_small_window import F,I,atan
from certify_native_exact_logarithm import log_rational

def certificate():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    names=['RPB108_PRIME5_THREEBAND_OBSTRUCTION_097_CERTIFICATE_20261007.json',
           'RPB108_PRIME5_THREEBAND_COMPLEMENT84_097_CERTIFICATE_20261007.json']
    raw={n:(root/n).read_bytes() for n in names};obstruction,complement=[json.loads(raw[n]) for n in names]
    assert obstruction['aperture']==complement['aperture']=='97/100'
    norm=F(complement['combined_prime_upper']);assert norm==F(444727,250000)
    required=F(obstruction['required_scalar_complement_lower_bound'])
    old=I.grid;I.grid=10**100
    try:
        a=F(97,100);cap=F(1387,100);pi=16*atan(F(1,5))-4*atan(F(1,239))
        rejected=(2*a*cap*pi.lo)**2;assert rejected>84*85
        assert (2*a*F(69,5)*pi.hi)**2<84*85
        ceiling=log_rational(cap,500).hi-norm
        assert ceiling<required
        # Every admissible outer cutoff obeys (2*a*T*pi)^2<84*85,
        # hence T<cap. The step lower is g(T) minus nonnegative mass
        # penalties, with g(T)=log(T)-7/(216*T^2), and pole loss >=0.
        return dict(aperture='97/100',retained_dimension=84,
            input_sha256={n:hashlib.sha256(b).hexdigest() for n,b in raw.items()},
            positive_region_argument_squared_ceiling=84*85,strict_outer_cutoff_upper=str(cap),
            rejected_cap_argument_squared_lower=str(rejected),fixed_prime_loss=str(norm),
            scalar_method_ceiling_upper=str(ceiling),scalar_method_ceiling_display=float(ceiling),
            necessary_scalar_lower=str(required),necessary_scalar_display=float(required),
            exact_gap_lower=str(required-ceiling),all_nonnegative_mass_penalties_dropped=True,
            arbitrary_finite_band_refinement_with_same_region_and_prime_loss_insufficient=True,
            scope='degree-84 positive-region step method with fixed proved prime loss; not an actual form ceiling',
            actual_full_form_negative_witness=False,whole_domain_positivity=False,
            changing_prime_bound_or_mass_method_outside_scope=True,f4_entry_closed=False,lean_formalized=False)
    finally:I.grid=old

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
