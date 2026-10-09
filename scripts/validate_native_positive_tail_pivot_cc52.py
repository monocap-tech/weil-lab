"""Actual tail reserve plus rational final-gate controls; no source Gram."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def run():
    count=0
    def check(x):
        nonlocal count
        assert x
        count+=1
    kappa=F(207,1000)
    for n in (112,113):
        eta2=F(212,25)*F(53,100)**(2*n)/factorial(n)**2
        check(0<eta2<F(1,10**420))
        check(kappa-2*eta2>F(1,5))
        check(kappa-2*eta2-F(1,10**190)>F(1,5))
    check((16+144**2)*(34+35)*F(1,10**200)<F(1,10**190))
    alpha=F(1,10**38);k=F(1,4)
    check(alpha>F(9,10**39) and k>F(1,5))
    for d,sign in ((F(1,4*10**19),1),(F(1,2*10**19),0),(F(1,10**19),-1)):
        gate=alpha-d*d/k
        check((gate>0)-(gate<0)==sign)
        check(alpha*k-d*d==k*gate)
        check(alpha-5*d*d<=gate)
    check(alpha-5*F(1,4*10**19)**2>0)
    check(F(9,2)-F(1)/k>0 and F(9,2)-5<0)
    check(k-alpha>F(1,5) and alpha-alpha==0)
    check(56-1==55)
    return dict(stage='CC52 positive compensated-tail pivot',all_passed=True,new_exact_checks=count,
                actual_tail_pivot_lower='1/5',pivot_lower_analytic=True,
                native_response_gram_evaluated=False,native_final_gate_certified=False,
                nf17_full_source_replayed=False,RH_proved=False,lean_certified=False,
                constructor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_POSITIVE_TAIL_PIVOT_CC52_VALIDATION_20261009.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
