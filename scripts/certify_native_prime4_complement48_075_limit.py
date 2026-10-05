"""Ceiling of the sharp 48-moment scalar cutoff family; not actual coercivity."""
import json,hashlib
from pathlib import Path
from math import factorial
from certify_native_legendre_small_window import F,I,log_rational,sqrt_rational
from certify_native_larger_aperture_complement import integrated_mass


def certificate():
    a=F(3,4);k=48;b=(2*a*F(22,7))**2/F(97*99);p=16*a*(a/2)**96/factorial(48)**2
    ell2=log_rational(F(2));A2=ell2/sqrt_rational(F(2));A4=ell2/2
    square=A4*A4+8*A2*A2
    J=(A4+I(sqrt_rational(square.lo).lo,sqrt_rational(square.hi).hi))/2
    A=J+log_rational(F(3))/sqrt_rational(F(3))
    def data(T):
        rho=integrated_mass(a,k,T);q=b*T*T
        rp=rho*(97/T+2*b*T/(1-q))
        c=log_rational(T)-F(7,216)/T**2
        cp=1/T+F(7,108)/T**3
        value=c-(10+c)*rho-p-A
        derivative=I(cp*(1-rho))-(10+c)*rp
        assert c.lo>0 and rho<1
        return value,derivative
    left,mid,right=F(186,25),F(373,50),F(187,25)
    fl,dl=data(left);fm,dm=data(mid);fr,dr=data(right)
    assert dl.lo>0 and dr.hi<0
    tangent=fm.hi+max(abs(dm.lo),abs(dm.hi))*max(mid-left,right-mid)
    cap=F(4763,10000);assert tangent<cap
    root=Path(__file__).resolve().parents[1]/'notes/data'
    obstruction_path=root/'RPB108_PRIME4_CORRECTED48_075_SHARP_CERTIFICATE_20261005.json'
    obstruction=json.loads(obstruction_path.read_text())
    required=F(obstruction['required_physical_coercivity_lower'])
    assert cap<F(4766,10000)<required
    return dict(aperture='3/4',physical_dimension=48,
        status='certified ceiling of the sharp 48-moment scalar cutoff proof family',
        family='F(T)=c(T)-(10+c(T))*rho(T)-p-J24-A3; c(T)=log(T)-7/(216T^2)',
        left_cutoff=str(left),middle_cutoff=str(mid),right_cutoff=str(right),
        left_derivative_lower=str(dl.lo),right_derivative_upper=str(dr.hi),
        middle_derivative_interval=[str(dm.lo),str(dm.hi)],tangent_upper=str(tangent),
        scalar_family_upper=str(cap),low_floor_used='-10',
        countervector_certificate_sha256=hashlib.sha256(obstruction_path.read_bytes()).hexdigest(),countervector_required_coercivity_lower=str(required),
        proof='F is strictly concave where c>=0 and rho<=1; rho has a positive power series. Positive lawful bounds require this region. Derivative signs trap its maximum; the middle tangent bounds it.',
        actual_complement_coercivity_upper_bound=False,actual_negative_witness=False,
        whole_domain_positivity=False,global_endpoint_excluded=False,f4_entry_closed=False,
        full_transport_closed=False,lean_formalized=False)


if __name__=='__main__':print(json.dumps(certificate(),indent=2))
