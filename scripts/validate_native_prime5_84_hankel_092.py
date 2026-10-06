"""Independent exact convolution and interval checks for actual source pairs."""
import json
from pathlib import Path
from certify_native_legendre_small_window import F,I
from certify_native_exact_hankel import moment_apply,bilinear_bounds,convolution_window
from certify_native_prime5_gram84_092 import endpoint_primitives,fixed_moments
from certify_native_exact_logarithm import log_rational
from certify_native_endpoint_log_gram import shifted_legendre,exact_log_data


def direct_convolution(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c


def certificate():
    old=I.grid;I.grid=10**300
    try:
        source=json.loads((Path(__file__).resolve().parents[1]/'notes/data/RPB108_PRIME5_SOURCE84_092_CERTIFICATE_20261006.json').read_text())
        rows=source['rows'];p=[[int(c) for c in q] for q in shifted_legendre(83)]
        d=F(46,25);ell={n:log_rational(F(n),500)/d for n in (2,3,4,5)}
        from certify_native_translation_panel_order import translation_panels
        geometry=translation_panels(F(23,25),logarithm=lambda x:log_rational(x,500))
        assert source['panel_endpoints']==geometry['labels']
        cuts=geometry['cuts']
        for pair in [(83,52),(51,84)]:
            try:exact_log_data(*pair)
            except ValueError:pass
            else:raise AssertionError("Mismatched source/projection accepted")
        panels=[0,3,4,5,8];checks=0;logchecks=0
        for panel in panels:
            a,b=[endpoint_primitives(t,746) for t in cuts[panel:panel+2]]
            moments=fixed_moments([(b[0][k+1]-a[0][k+1])/I(k+1) for k in range(747)])
            logs=fixed_moments([b[1][k]-a[1][k] for k in range(747)])
            moments=[(max(0,lo),hi) for lo,hi in moments];logs=[(max(0,lo),hi) for lo,hi in logs]
            def verify(x,y,m):
                packed=bilinear_bounds(x,moment_apply(y,m,len(x)))
                center=sum((u*v*(m[i+j][0]+m[i+j][1]) for i,u in enumerate(x) for j,v in enumerate(y)),0)
                radius=sum((abs(u*v)*(m[i+j][1]-m[i+j][0]) for i,u in enumerate(x) for j,v in enumerate(y)),0)
                assert packed==(center-radius,center+radius)
                c=direct_convolution(x,y)
                lo=sum((v*(m[k][0] if v>=0 else m[k][1]) for k,v in enumerate(c)),0)
                hi=sum((v*(m[k][1] if v>=0 else m[k][0]) for k,v in enumerate(c)),0)
                assert packed[0]<=2*lo and packed[1]>=2*hi
            for i,j in [(0,83),(41,83),(83,83)]:
                x=rows[i]['panels'][panel]['low_degree_numerators']+rows[i]['common_high_degree_numerators']
                y=rows[j]['panels'][panel]['low_degree_numerators']+rows[j]['common_high_degree_numerators']
                verify(x,y,moments);checks+=1
                verify(p[i],y,logs);logchecks+=1
        for a,b in [([0,10**120,1],[10**600,0,3]),([1,2,3],[4,5,6])]:
            expected=direct_convolution(a,b);assert convolution_window(a,b,0,len(expected))==expected
        return dict(actual_source_pair_checks=checks,actual_endpoint_log_pair_checks=logchecks,
                    tested_panels=panels,independent_direct_double_sum_agreement=True,
                    original_convolution_interval_containment=True,large_integer_carry_controls_passed=True,mismatched_projection_controls_rejected=True)
    finally:I.grid=old

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
