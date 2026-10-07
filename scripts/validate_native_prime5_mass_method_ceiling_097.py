"""Independent finer logarithms, Machin bound and scalar-method scope audit."""
import hashlib,json
from pathlib import Path
from certify_native_legendre_small_window import F,I,atan
from certify_native_exact_logarithm import log_rational

def certificate(path,repeat):
    raw=Path(path).read_bytes();assert raw==Path(repeat).read_bytes();c=json.loads(raw)
    root=Path(__file__).resolve().parents[1]/'notes/data'
    data=[]
    for n,h in c['input_sha256'].items():
        b=(root/n).read_bytes();assert hashlib.sha256(b).hexdigest()==h;data.append(json.loads(b))
    o,p=data;assert o['aperture']==p['aperture']==c['aperture']=='97/100'
    required=F(o['required_scalar_complement_lower_bound']);norm=F(p['combined_prime_upper'])
    assert norm==F(c['fixed_prime_loss'])==F(444727,250000)
    assert required==F(c['necessary_scalar_lower'])
    old=I.grid;I.grid=10**140
    try:
        pi=16*atan(F(1,5),140)-4*atan(F(1,239),140)
        cap=F(c['strict_outer_cutoff_upper']);assert cap==F(1387,100)
        assert (2*F(97,100)*cap*pi.lo)**2>=F(c['rejected_cap_argument_squared_lower'])>84*85
        assert (2*F(97,100)*F(69,5)*pi.hi)**2<84*85
        fresh=log_rational(cap,550).hi-norm
        ceiling=F(c['scalar_method_ceiling_upper']);assert fresh<=ceiling<required
        assert required-ceiling==F(c['exact_gap_lower'])>0
    finally:I.grid=old
    assert c['all_nonnegative_mass_penalties_dropped']
    assert c['arbitrary_finite_band_refinement_with_same_region_and_prime_loss_insufficient']
    assert c['actual_full_form_negative_witness'] is c['whole_domain_positivity'] is False
    return dict(aperture='97/100',certificate_sha256=hashlib.sha256(raw).hexdigest(),
        byte_identical_repeat=True,finer_log_and_machin_cap_verified=True,
        current_cutoff_69_over_5_inside_positive_region=True,
        every_admissible_outer_cutoff_below_cap=True,
        arbitrary_finite_step_refinement_with_fixed_prime_loss_insufficient=True,
        exact_gap_positive=True,scalar_ceiling_display=float(ceiling),
        required_scalar_display=float(required),actual_form_ceiling_claimed=False,
        actual_full_form_negative_witness=False,whole_domain_positivity=False,
        f4_entry_closed=False,lean_formalized=False)

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(*sys.argv[1:]),indent=2))
