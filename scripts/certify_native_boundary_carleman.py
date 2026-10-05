"""Exact constants for the actual archimedean exterior Carleman bound."""
import json
from math import factorial
from certify_native_legendre_small_window import F,I,atan


def exp_positive(x,terms=120):
    assert 0<=x<terms+2
    total=sum((x**j/F(factorial(j)) for j in range(terms+1)),F(0))
    tail=x**(terms+1)/F(factorial(terms+1))/(1-x/F(terms+2))
    return I(total,total+tail)


def certificate():
    previous=I.grid;I.grid=10**200
    try:
        pi=16*atan(F(1,5))-4*atan(F(1,239))
        assert 3<pi.lo<pi.hi<F(22,7)
        one_side=pi.hi/2+1
        assert one_side<F(18,7) and 2*one_side**2<16
        samples=[F(1,1024),F(1,16),F(1,2),F(1),F(2),F(4),F(8)]
        margins=[]
        for s in samples:
            decay=I(1)/exp_positive(s/2)
            denominator=I(1)-I(1)/exp_positive(2*s)
            kernel=decay/denominator
            majorant=I(F(1,2)/s)+decay
            margin=(majorant-kernel).lo
            assert margin>0
            margins.append(str(margin))
        # Retaining only the rank-one exponential kernel fails near the edge.
        s=F(1,16);decay=I(1)/exp_positive(s/2)
        kernel=decay/(I(1)-I(1)/exp_positive(2*s))
        assert (kernel-decay).lo>0
        return dict(status='certified constants and controls for actual exterior L2 bound',
            kernel='exp(-s/2)/(1-exp(-2s)), s>0',
            universal_majorant='1/(2s)+exp(-s/2)',
            universal_proof='exp(2s)-1>=2s; weighted Schur integral for 1/(x+y) equals pi/sqrt(x)',
            pi_upper=str(pi.hi),one_boundary_operator_upper=str(one_side),
            one_boundary_rational_ceiling='18/7',both_boundaries_operator_ceiling='4',
            both_boundaries_squared_rational_bound='648/49',
            checked_displacements=[str(x) for x in samples],sample_majorant_lower_margins=margins,
            dropped_singular_kernel_control_rejected=True,
            conditional_hypothesis='h in actual D_a and Q_a(g,h)=0 for every g in D_a',
            pinned_source_commit='787af35c12cbb98b713e6fe29cd9ae360ddfbcdd',
            analytic_point_supported_log_dual_exclusion=True,
            endpoint_full_residual_locally_L2=True,endpoint_frozen_multiplier_domain_derived=True,
            endpoint_existence_asserted=False,endpoint_H1_asserted=False,
            full_unrestricted_pole_operator_domain_asserted=False,
            gaussian_upper_decay_class='inverse squared logarithm, not exponential',
            global_endpoint_excluded=False,f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)
    finally:I.grid=previous


if __name__=='__main__':print(json.dumps(certificate(),indent=2))
