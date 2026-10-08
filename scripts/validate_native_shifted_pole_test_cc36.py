"""Full shifted mass and parity pole correlation controls."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from validate_native_parity_pole_correlation_cc35 import run as inherited_run
ROOT=Path(__file__).resolve().parents[1]

def run():
    n=0
    def check(v):
        nonlocal n
        assert v
        n+=1
    a,k,mu=F(9,25),F(12,25),F(16,25)
    lam=a*a+mu;delta=1-lam;originaldelta=1-a*a
    check(originaldelta==F(544,625))
    check(delta==F(144,625) and lam==F(481,625))
    check(originaldelta==delta+mu)
    check(k*k/originaldelta==F(9,34)<1)
    critical=a*a*k*k/(lam*delta);low=k*k+mu-a*a*k*k/lam
    check(critical+low==1 and low>0)
    check(1-k*k-mu-a*a*k*k/delta==0)
    check(a*a+k*k==1-mu)
    check(a*(1-a*a)-a*k*k==mu*a)
    check(k*(1-k*k)-a*a*k==mu*k)
    for b in (F(-1,3),F(0),F(1,3)):
        for level in (F(0),F(1,4),mu):
            for sigma in (-1,1):
                x,z0,xw,zw,amp=F(1,4),F(2,3),F(1,2),F(-1,4),F(3,5)
                long0=z0-b*x;longw=zw-b*xw
                X=x-level*xw;Y=z0-level*zw+sigma*amp
                direct=(X*X-2*b*X*Y+Y*Y)/(1-b*b)
                check(direct==X*X+(long0-level*longw+sigma*amp)**2/(1-b*b))
                check(long0-level*longw==z0-level*zw-b*X)
                check(direct>=X*X)
                check((X!=x)==(level!=0))
                check((long0-level*longw!=long0)==(level!=0))
    old=inherited_run()
    assert old['all_passed'] and old['total_exact_checks']==25873 and n==99
    return {'stage':'CC36 shifted pole test','all_passed':True,'new_exact_checks':n,
            'inherited_cc35_checks':25873,'total_exact_checks':25873+n,
            'original_arithmetic_suppression_proved':False,'actual_zeta_covariance_evaluated':False,
            'RH_proved':False,'lean_certified':False,
            'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_SHIFTED_POLE_TEST_CC36_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
