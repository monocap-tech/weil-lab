"""Favorable-kernel higher-null controls; no actual Weil eigenvectors."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
from validate_native_dirichlet_log_localization_cc41 import run as inherited
ROOT=Path(__file__).resolve().parents[1]
def run():
    count=0
    def check(v):
        nonlocal count
        assert v
        count+=1
    for u in (F(1,2),F(1),F(2)):
        b=u*u
        H=lambda x,y:-b*(x+y)**2
        Q=lambda x,y:b*(x+y)**2
        c=lambda x,y:u*(x+y)
        check(b>0 and -b<0)
        check(H(1,1)==-4*b)
        check(H(1,-1)==0)
        check(c(1,-1)==0)
        check(Q(1,-1)==0)
        check(Q(1,1)>0)
        for x,y in ((F(1),F(-2)),(F(2),F(3)),(F(-3),F(1))):
            check(H(x,y)-H(abs(x),abs(y))==2*b*(abs(x*y)-x*y)>=0)
    old=inherited()
    assert old['all_passed'] and old['new_exact_checks']==16 and count==27
    return {'stage':'CC43 pole-free ground state','all_passed':True,
            'new_exact_checks':count,'cc41_checks_replayed':16,'local_chain_checks':43,
            'older_large_chain_replayed':False,'actual_zeta_eigenvectors_evaluated':False,
            'higher_zero_moment_channel_excluded':False,'RH_proved':False,'lean_certified':False,
            'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_POLE_FREE_GROUND_STATE_CC43_VALIDATION_20261009.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
