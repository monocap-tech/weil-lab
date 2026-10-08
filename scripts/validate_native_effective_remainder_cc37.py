"""Rational enclosures for CC37; analytic digamma bound is separate."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib,json
from validate_native_shifted_pole_test_cc36 import run as inherited_run
ROOT=Path(__file__).resolve().parents[1]

def exp_bounds(x,N=20):
    assert x>=0 and x<F(N+2)
    lower=sum((x**j/F(factorial(j)) for j in range(N+1)),F(0))
    upper=lower+(x**(N+1)/F(factorial(N+1)))/(1-x/F(N+2))
    return lower,upper

def run():
    n=0
    def check(v):
        nonlocal n
        assert v
        n+=1
    for p,x in ((2,F(7,10)),(3,F(11,10)),(5,F(81,50)),(7,F(39,20))):
        check(exp_bounds(x)[0]>p)
    check(exp_bounds(F(21,20))[1]<3)
    for p,x in ((2,F(7,5)),(3,F(17,10)),(5,F(11,5)),(7,F(13,5)),(8,F(14,5))):
        check(x*x<p)
    check(F(271,7)<F(8,3)**4)
    S=F(7,10)/F(7,5)+F(11,10)/F(17,10)+F(7,10)/2+F(81,50)/F(11,5)+F(39,20)/F(13,5)+F(7,10)/F(14,5)
    check(S==F(12093,3740))
    check(8+2*S+F(16,3)==F(111079,5610)<20)
    old=inherited_run()
    assert old['all_passed'] and old['total_exact_checks']==25972 and n==13
    return {'stage':'CC37 effective native remainder','all_passed':True,
            'new_exact_checks':n,'inherited_cc36_checks':25972,'total_exact_checks':25972+n,
            'global_archimedean_bound':8,'cap':'21/20','full_remainder_bound':20,
            'rational_upper_bound':'111079/5610','actual_native_finite_matrix_evaluated':False,
            'defect_suppression_proved':False,'new_aperture':False,'RH_proved':False,
            'lean_certified':False,'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_EFFECTIVE_NATIVE_REMAINDER_CC37_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
