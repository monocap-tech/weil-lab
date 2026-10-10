"""RC44 exact budgets: reduced native Chebyshev head, unchanged carrier."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib,json,sys

def exp_bounds(x,n=100):
    assert 0<=x<n+2
    low=sum((x**j/factorial(j) for j in range(n+1)),F(0))
    return low,low+x**(n+1)/factorial(n+1)/(1-x/F(n+2))

def run(pole_path,prime_path):
    pole_raw=Path(pole_path).read_bytes();prime_raw=Path(prime_path).read_bytes()
    pole=json.loads(pole_raw);prime=json.loads(prime_raw)
    assert pole['actual_signed_pole_head_enclosed'] and prime['complete_active_prime_set_certified']
    assert pole['source_certificate_sha256']==prime['native_certificate_sha256']
    checks=0
    def check(value):
        nonlocal checks
        assert value,checks+1
        checks+=1
    B=F(11,10);alpha=F(1,10);L=F(51,10);n=1250
    prime_physical=F(prime['full_paired_prime_physical_operator_norm_upper'])
    negative_pole_physical=2*F(pole['sinh_physical_norm_squared_upper'])
    nonarch=prime_physical+negative_pole_physical
    kappa=F(183,40)
    check(nonarch<kappa)
    check(F(prime['full_paired_prime_canonical_operator_norm_upper'])==F(252,257)*prime_physical)
    check(F(pole['canonical_negative_pole_part_norm_upper'])==F(252,257)*negative_pole_physical)
    low,high=exp_bounds(L)
    check(160<low<high<165)
    e_low,e_high=exp_bounds(F(1))
    check(F(8,3)<e_low<e_high<3)
    log2_lower=F(693,1000)
    check(exp_bounds(log2_lower)[1]<2)
    # RC19's entire high multiplier inequality applies whenever pi*x>=1/4.
    # For x>=exp(L)>160: .9 log(x)-kappa-1.3/x >=this reserve.
    high_reserve=(1-alpha)*L-kappa-(1+3*alpha)/160
    check(high_reserve==F(11,1600)>0)
    # e+T<e*T since e>2, T>160, and e<3; hence w< L+1 in band.
    check(160>3 and e_low>2)
    penalty=F(31,5)+kappa+alpha*(L+1)
    check(penalty==F(2277,200)<12)
    BT=B*165;z_upper=2*F(22,7)*BT
    gap=n*log2_lower-F(3,4)*z_upper
    check(gap==F(297,28)>10)
    # Rectangle-area factor: 2sqrt(BT)<27. The RC22 Laurent-contour
    # kernel tail is 4 exp(3z/4-n log2)<4 exp(-10)<4(3/8)^10.
    check(4*BT<27**2)
    kernel_upper=4*F(3,8)**10
    residual_upper=27*kernel_upper
    check(residual_upper<F(1,100))
    floor=alpha-F(12,10000)
    check(floor==F(247,2500)>F(1,11))
    sharper_floor=alpha-penalty*residual_upper**2
    check(sharper_floor>F(99598,1000000)>floor)
    m=F(1,4000);cross=F(1,300)
    schur=m-cross**2/floor
    check(schur==F(1223,8892000)>0)
    check(F(8600,n)==F(172,25))
    check(F(8600-n,8600)==F(147,172))
    check(F(n*n,8600*8600)==F(625,29584))
    # Control: diagonal head/tail positivity alone does not prove coupling.
    check(m*floor-F(1,100)**2<0)
    # Controls: a complement that kills eight moments need not kill the
    # retained degree-eight feature; smaller head conditions are distinct.
    check(n>8 and n<8600)
    return dict(milestone='RC44',status='PASS',exact_rational_checks=checks,
        pole_certificate_sha256=hashlib.sha256(pole_raw).hexdigest(),
        prime_certificate_sha256=hashlib.sha256(prime_raw).hexdigest(),
        original_form_source_blob=pole['original_form_source_blob'],cap='11/10',
        actual_prime_physical_norm_upper=str(prime_physical),
        actual_negative_pole_physical_norm_upper=str(negative_pole_physical),
        nonarch_physical_negative_allowance_upper=str(nonarch),
        rounded_nonarch_negative_allowance=str(kappa),frequency_cutoff='exp(51/10)',
        frequency_cutoff_lower='160',frequency_cutoff_upper='165',
        high_multiplier_reserve_lower=str(high_reserve),low_band_penalty_upper=str(penalty),
        Chebyshev_feature_count=n,previous_sufficient_feature_count=8600,
        log2_lower=str(log2_lower),Fourier_rectangle_area_factor_upper='27',
        contour_exponent_gap_lower=str(gap),kernel_uniform_error_upper=str(kernel_upper),
        whole_low_band_operator_error_upper=str(residual_upper),
        preserved_original_complement_floor=str(floor),
        sharper_original_complement_floor=str(sharper_floor),
        conditional_actual_head_floor=str(m),conditional_actual_source_cross_norm=str(cross),
        conditional_preserved_Schur_reserve=str(schur),
        sufficient_feature_count_reduction_fraction=str(F(147,172)),
        dense_entry_count_remaining_fraction=str(F(625,29584)),
        low_eight_feature_certificates_reusable=True,
        reduced_head_actual_Gram_constructed=False,reduced_head_actual_projection_constructed=False,
        reduced_head_actual_Weil_floor_certified=False,reduced_head_actual_source_residual_certified=False,
        whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

def replay(certificate_path,pole_path,prime_path):
    cert=json.loads(Path(certificate_path).read_text())
    pole_raw=Path(pole_path).read_bytes();prime_raw=Path(prime_path).read_bytes()
    pole=json.loads(pole_raw);prime=json.loads(prime_raw)
    assert cert['pole_certificate_sha256']==hashlib.sha256(pole_raw).hexdigest()
    assert cert['prime_certificate_sha256']==hashlib.sha256(prime_raw).hexdigest()
    assert F(cert['nonarch_physical_negative_allowance_upper'])==F(prime['full_paired_prime_physical_operator_norm_upper'])+2*F(pole['sinh_physical_norm_squared_upper'])
    assert F(cert['nonarch_physical_negative_allowance_upper'])<F(183,40)
    # Independent positive atanh series for log2, rather than exponentiating
    # its proposed lower bound as in generation.
    log2_lower=2*sum((F(1,3)**(2*j+1)/F(2*j+1) for j in range(12)),F(0))
    assert log2_lower>F(cert['log2_lower'])==F(693,1000)
    L=F(51,10); low,high=exp_bounds(L,96)
    assert 160<low<high<165
    # A direct exp(10) partial sum verifies the coarsened kernel bound.
    exp10_lower=sum((F(10)**j/factorial(j) for j in range(51)),F(0))
    assert 4/exp10_lower<F(cert['kernel_uniform_error_upper'])
    B=F(11,10);alpha=F(1,10);kappa=F(183,40);n=cert['Chebyshev_feature_count']
    assert n==1250
    assert (1-alpha)*L-kappa-F(13,1600)==F(cert['high_multiplier_reserve_lower'])>0
    penalty=F(31,5)+kappa+alpha*(L+1)
    assert penalty==F(cert['low_band_penalty_upper'])<12
    gap=n*F(693,1000)-F(3,4)*2*F(22,7)*B*165
    assert gap==F(cert['contour_exponent_gap_lower'])>10
    assert 4*B*165<27**2
    residual=F(cert['whole_low_band_operator_error_upper'])
    assert residual==27*F(cert['kernel_uniform_error_upper'])<F(1,100)
    assert alpha-penalty*residual**2==F(cert['sharper_original_complement_floor'])
    floor=F(cert['preserved_original_complement_floor'])
    assert floor==alpha-F(12,10000)==F(247,2500)
    assert F(1,4000)-F(1,300)**2/floor==F(cert['conditional_preserved_Schur_reserve'])>0
    assert F(8600-n,8600)==F(cert['sufficient_feature_count_reduction_fraction'])
    assert F(n*n,8600*8600)==F(cert['dense_entry_count_remaining_fraction'])
    assert not cert['reduced_head_actual_projection_constructed']
    assert not cert['whole_aperture_positivity_extended']
    print('PASS: positive log2-series replay, cutoff and contour budgets, whole floor, Schur reserve, and source custody')

if __name__=='__main__':
    root=Path(__file__).parent.parent/'certificates'
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        replay(sys.argv[2],sys.argv[3] if len(sys.argv)>3 else root/'rpb108_rc42_native_signed_pole_head.json',
               sys.argv[4] if len(sys.argv)>4 else root/'rpb108_rc43_native_prime_head.json')
    else:
        pole=sys.argv[1] if len(sys.argv)>1 else root/'rpb108_rc42_native_signed_pole_head.json'
        prime=sys.argv[2] if len(sys.argv)>2 else root/'rpb108_rc43_native_prime_head.json'
        print(json.dumps(run(pole,prime),indent=2))
