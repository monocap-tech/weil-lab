"""Exact dual phase/transverse controls; not actual zeta covariance."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from validate_native_unsigned_remainder_barrier_cc34 import run as inherited_run
ROOT=Path(__file__).resolve().parents[1]

def run():
    n=0
    def check(v):
        nonlocal n
        assert v
        n+=1
    for b in (F(-1,3),F(0),F(1,3)):
        for a in (F(1,4),F(1),F(3,2)):
            for sigma in (-1,1):
                x=F(1,4);z0=b*x-sigma*a
                longitudinal=z0-b*x
                y=z0+sigma*a
                direct=(x*x-2*b*x*y+y*y)/(1-b*b)
                check(direct==x*x+(longitudinal+sigma*a)**2/(1-b*b))
                check(longitudinal+sigma*a==0)
                check(direct==F(1,16))
                check((x,-sigma*a+b*x)==(x,z0))
                component=a*a/(1-b*b)
                check(component>0)
                check((-sigma*a+sigma*a)**2/(1-b*b)==0)
                check((sigma*a+sigma*a)**2/(1-b*b)==4*component)
                check((z0-longitudinal==b*x) and ((b!=0)==(z0!=longitudinal)))
    old=inherited_run()
    assert old['all_passed'] and old['total_exact_checks']==25729 and n==144
    return {'stage':'CC35 parity pole correlation','all_passed':True,
            'new_exact_checks':n,'inherited_cc34_checks':25729,'total_exact_checks':25729+n,
            'actual_defect_relative_correlation_estimate_proved':False,
            'actual_zeta_covariance_evaluated':False,'RH_proved':False,'lean_certified':False,
            'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'input_sha256':hashlib.sha256((ROOT/'scripts/validate_native_unsigned_remainder_barrier_cc34.py').read_bytes()).hexdigest()}

if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_PARITY_POLE_CORRELATION_CC35_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
