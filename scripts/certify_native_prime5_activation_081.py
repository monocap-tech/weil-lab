"""Exact prime-5 activation, nine source panels and coefficient controls at 81/100."""
import json
from certify_native_legendre_small_window import F,I,log_rational,sqrt_rational


def certificate():
    a=F(81,100);d=2*a
    logs=[log_rational(F(n)) for n in (2,3,4,5)]
    ell=[s/d for s in logs]
    assert logs[3].hi<d<log_rational(F(7)).lo
    assert F(8,5)<logs[3].lo # previous 4/5 aperture lies below activation
    cuts=[I(0),I(1)-ell[3],I(1)-ell[2],I(1)-ell[1],ell[0],
          I(1)-ell[0],ell[1],ell[2],ell[3],I(1)]
    assert all(x.hi<y.lo for x,y in zip(cuts,cuts[1:]))
    expected=[[(0,1),(1,1),(2,1),(3,1)],[(0,1),(1,1),(2,1)],[(0,1),(1,1)],[(0,1)],
              [(0,1),(0,-1)],[(0,-1)],[(0,-1),(1,-1)],[(0,-1),(1,-1),(2,-1)],
              [(0,-1),(1,-1),(2,-1),(3,-1)]]
    observed=[]
    for left,right in zip(cuts,cuts[1:]):
        t=(left+right)/2;active=[]
        for index,s in enumerate(ell):
            if (t+s).hi<1:active.append((index,1))
            else:assert (t+s).lo>1
            if (t-s).lo>0:active.append((index,-1))
            else:assert (t-s).hi<0
        observed.append(active)
    assert observed==expected
    A5=logs[3]/sqrt_rational(F(5))
    omission_gap=2*A5*(I(1)-ell[3])
    incorrect_lambda_gap=2*(logs[3]-logs[0])/sqrt_rational(F(5))*(I(1)-ell[3])
    assert omission_gap.lo>F(9,1000) and incorrect_lambda_gap.lo>F(5,1000)
    # Deleting either edge panel's prime-5 translation fails an actual interior test.
    assert (cuts[1]/2+ell[3]).hi<1
    assert ((cuts[-2]+I(1))/2-ell[3]).lo>0
    return dict(status='certified actual prime-5 activation geometry and coefficient controls',aperture=str(a),
        active_prime_powers=[2,3,4,5],panel_count=9,
        panel_endpoints=['0','1-log(5)/(2a)','1-log(4)/(2a)','1-log(3)/(2a)','log(2)/(2a)',
                         '1-log(2)/(2a)','log(3)/(2a)','log(4)/(2a)','log(5)/(2a)','1'],
        panel_endpoint_intervals=[[str(x.lo),str(x.hi)] for x in cuts],panel_translation_indices=observed,
        all_panel_activation_controls_passed=True,prime5_source_amplitude='log(5)/sqrt(5)',
        prime5_native_correlation_coefficient='2*log(5)/sqrt(5)',prime4_source_amplitude='log(2)/2',
        constant_coordinate_prime5_omission_gap_lower=str(omission_gap.lo),
        constant_coordinate_wrong_lambda5_gap_lower=str(incorrect_lambda_gap.lo),
        prime5_omission_control_rejected=True,prime5_wrong_lambda_control_rejected=True,
        prime5_edge_panel_omission_controls_rejected=True,previous_080_prime5_inactive=True,
        actual_source_enclosures_certified=False,full_native_matrix_certified=False,
        full_actual_source_gram_certified=False,whole_domain_positivity=False,actual_negative_witness=False,
        global_endpoint_excluded=False,f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
