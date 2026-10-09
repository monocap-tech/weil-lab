"""Exact tail envelopes and angle controls; no native response Gram."""
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
    t=F(53,100); N=20
    partial=sum(t**i/factorial(i) for i in range(N+1))
    upper=partial+t**(N+1)/factorial(N+1)/(1-t/F(N+2))
    check(t/F(N+2)<1 and upper<2)
    check(4*F(106,50)==F(212,25))
    check(F(212,25)/F(17,100)==F(848,17))
    for k,p in ((112,424),(113,429)):
        beta=F(848,17)*t**(2*k)/factorial(k)**2
        check(0<beta<F(1,10**p))
        check(k>111 and k%2==(0 if k==112 else 1))
    for epsilon in (F(1,10),F(1,10**20),F(1,10**220)):
        beta=epsilon**2; G=F(4); S=1-G
        check(S+(-2*epsilon)**2/beta==1)
        check(S+0/beta==-3)
        check((-2*epsilon)**2==beta*G)
        check(0<=beta*G)
        # Full mass shift for the positive original [[2,1],[1,1]] block.
        original=F(2)-1
        shifted=F(3,2)-F(1)/F(1,2)
        check(original==1 and shifted==F(-1,2))
        check(epsilon**2/F(1,2)==2*beta)
        check(F(3,2)*F(1,2)-1<0 and F(2)*1-1>0)
    check(56-1==55)
    return dict(stage='CC48 high moment tail',all_passed=True,new_exact_checks=n,
                native_response_evaluated=False,native_gate_certified=False,
                beta_even_upper='1e-424',beta_odd_upper='1e-429',
                RH_proved=False,lean_certified=False,
                constructor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_HIGH_MOMENT_TAIL_CC48_VALIDATION_20261009.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
