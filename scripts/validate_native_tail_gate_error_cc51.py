"""Pay constructive tail approximation in the fixed exact high carrier."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def run():
    n=0
    def check(x):
        nonlocal n
        assert x
        n+=1
    B=F(53,50);x=2*B;N=24
    s=sum(x**i/factorial(i) for i in range(N+1))
    upper=s+x**(N+1)/factorial(N+1)/(1-x/F(N+2))
    check(x/F(N+2)<1 and upper<9)
    check(8+2*F(12093,3740)<15)
    kappa=F(207,1000)
    check(16**2*(1+15/kappa)<144**2)
    for parity in (0,1):
        total=sum(10*j+13 for j in range(parity,112,2))
        check(total==(31528 if parity==0 else 32088) and total<180**2)
    check(10*135+13<37**2)
    check(F(444+34*12,10**79)/(1-F(12,10**79))<F(1,10**75))
    check(F(540,10**210)<F(1,10**200))
    epsilon=F(3,10**59)
    check(F(1,10**59)+F(1,10**75)+F(1,10**200)<epsilon)
    check(16*180+144**2*180<4*10**6)
    check((16+144**2)*(35+36)<4*10**6)
    check(4*10**6*epsilon<F(2,10**52))
    check(56*F(2,10**52)<F(2,10**50))
    mu=F(1,10)
    check(kappa-mu>0)
    check((16+mu)**2*(1+(15+mu)/(kappa-mu))<192**2)
    cert=json.loads((ROOT/'notes/data/RPB108_POSITIVE_MOMENT_SERIES_CC50_CERTIFICATE_20261009.json').read_text())
    for row in cert['coefficients']:
        def val(z):return F(int(z['numerator']),int(z['denominator']))
        lo,hi=val(row['relative_coefficient_lower']),val(row['relative_coefficient_upper'])
        check(0<lo<=hi and hi-lo<=F(1,10**79))
    for k in (112,113):
        eta2=F(212,25)*F(53,100)**(2*k)/factorial(k)**2
        check(0<eta2<F(1,10**420))
    return dict(stage='CC51 moment-tail signed gate error',all_passed=True,new_exact_checks=n,
                geometric_gate_operator_error_upper='2e-50',native_response_evaluated=False,
                other_gate_error_evaluated=False,native_gate_certified=False,
                RH_proved=False,lean_certified=False,
                constructor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_TAIL_GATE_ERROR_CC51_VALIDATION_20261009.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
