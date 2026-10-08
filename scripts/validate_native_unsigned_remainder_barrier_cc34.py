"""CC34 exact estimator controls; no actual zeta leakage certification."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from validate_native_remainder_forcing_cc33 import run as inherited_run
ROOT=Path(__file__).resolve().parents[1]

def run():
    n=0
    def check(v):
        nonlocal n
        assert v
        n+=1
    for j in (2,4,8,16,32,48):
        u=1-F(1,2**j);lam=u*u;delta=1-lam
        for v in (F(0),F(1,4)):
            interior=-lam;q=-u*v;envelope=lam
            check(interior==delta-1)
            check(envelope==abs(interior)==1-delta)
            check(interior*interior+q*q>=lam*lam)
            determinant=delta*(1-v*v)-lam*v*v
            check(determinant==delta-v*v)
            check((determinant<0)==(delta<v*v))
            check((q==0)==(v==0))
    inherited=inherited_run()
    assert inherited['all_passed'] and inherited['total_exact_checks']==25657
    assert n==72
    return {'stage':'CC34 unsigned native remainder barrier','all_passed':True,
            'new_exact_checks':n,'inherited_cc33_checks':25657,'total_exact_checks':25657+n,
            'native_analytic_lower_bound':'V_B(h)>=1/U_B^2-delta',
            'actual_arithmetic_outward_suppression_proved':False,
            'full_source_identity_nonimplication_proved':False,
            'actual_critical_covariance_evaluated':False,'RH_proved':False,
            'lean_certified':False,'new_aperture':False,
            'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'input_sha256':hashlib.sha256((ROOT/'scripts/validate_native_remainder_forcing_cc33.py').read_bytes()).hexdigest()}

if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_UNSIGNED_REMAINDER_BARRIER_CC34_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
