"""Rational consequences of analytic native archimedean tail bounds."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from validate_native_effective_remainder_cc37 import run as inherited_run
ROOT=Path(__file__).resolve().parents[1]

def run():
    n=0
    def check(v):
        nonlocal n
        assert v
        n+=1
    for x in (F(1),F(2),F(10),F(1000)):
        check(F(7,2)/x+F(1,288)/(x*x)<4/x)
        # log(e+x)>=1 gives a conservative whole-domain tail envelope.
        check(4/x<=4)
    old=inherited_run()
    assert old['all_passed'] and old['total_exact_checks']==25985 and n==8
    return {'stage':'CC38 archimedean tail','all_passed':True,
            'new_exact_checks':n,'inherited_cc37_checks':25985,'total_exact_checks':25985+n,
            'analytic_tail_bound':'4/[R log(e+R)] for R>=1',
            'actual_critical_covariance_evaluated':False,'defect_suppression_proved':False,
            'new_aperture':False,'RH_proved':False,'lean_certified':False,
            'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_ARCHIMEDEAN_TAIL_CC38_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
