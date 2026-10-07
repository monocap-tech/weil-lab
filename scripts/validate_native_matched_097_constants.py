"""Exact independent ceiling and support-order checks for aperture 97/100."""
import json
from math import factorial
from certify_native_legendre_small_window import F,I,bernoulli
from certify_native_exact_logarithm import log_rational
from certify_native_translation_panel_order import translation_panels

def certificate():
    previous=I.grid;I.grid=10**100
    try:
        a=F(97,100);d=2*a;L=4*a
        assert log_rational(F(49),300).lo>L
        assert log_rational(F(5),300).hi<d<log_rational(F(7),300).lo
        assert 5*L/4==F(97,20) and L<6
        B=bernoulli(202)
        c=[abs(B[2*k]*(2*d)**(2*k)/factorial(2*k)) for k in range(1,101)]
        assert all(y<x for x,y in zip(c,c[1:]))
        assert all((B[2*k]>0)==(k%2==1) for k in range(1,101))
        assert (1+d+d*d/3)/2<F(9,4) and d/2<1 and d<3
        geometry=translation_panels(a,logarithm=lambda x:log_rational(x,300))
        expected=['0','1-log(5)/(2a)','1-log(4)/(2a)','log(2)/(2a)',
            '1-log(3)/(2a)','log(3)/(2a)','1-log(2)/(2a)','log(4)/(2a)','log(5)/(2a)','1']
        assert geometry['labels']==expected
        assert len(geometry['cuts'])==10
        assert all(x.hi<y.lo for x,y in zip(geometry['cuts'],geometry['cuts'][1:]))
        assert not log_rational(F(48),300).lo>L
        return dict(aperture=str(a),prime_powers=[2,3,4,5],native_exp_ceiling=49,
            native_kernel_ceiling='97/20',source_kernel_ceiling='9/4',
            decreasing_alternating_bernoulli_pairs=100,panel_endpoints=expected,
            strict_panel_order=True,obsolete_exp_ceiling_48_rejected=True,
            whole_domain_positivity=False,f4_entry_closed=False)
    finally:I.grid=previous

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
