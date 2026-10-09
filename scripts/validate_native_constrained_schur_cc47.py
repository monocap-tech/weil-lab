"""Exact constrained Schur controls; no native source measurement."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def gate(q,b,c,l,n):
    w=b/c; s=q-b*b/c; beta=n*n/c; a=l-n*w
    return w,s,beta,a,(s+a*a/beta if beta else None)
def run():
    count=0
    def check(x):
        nonlocal count
        assert x
        count+=1
    cases=[(F(1),F(2),F(1),F(1),F(-1),F(6)),
           (F(1),F(2),F(1),F(1),F(1),F(-2)),
           (F(1),F(1),F(1),F(1),F(-1),F(4)),
           (F(1),F(1),F(1),F(1),F(1),F(0)),
           (F(1,2),F(2),F(1,2),F(1),F(-1),F(5)),
           (F(2),F(1),F(2),F(1),F(1),F(2))]
    for q,b,c,l,n,expected in cases:
        w,s,beta,a,k=gate(q,b,c,l,n)
        check(c>0 and beta>0)
        check(k==expected)
        for x in (F(1),F(-2),F(3,5)):
            y=-l*x/n
            check(q*x*x+2*b*x*y+c*y*y==k*x*x)
            z=y+w*x
            check(l*x+n*y==0 and z==-a*x*n/(c*beta))
    w,s,beta,a,k=gate(F(1),F(2),F(1),F(1),F(0))
    check(beta==0 and k is None and a==1)
    check(gate(F(1,2),F(2),F(1,2),F(1),F(-1))==(F(4),F(-15,2),F(2),F(5),F(5)))
    check(F(-3)+1<0<F(-3)+9)
    check(gate(F(2),F(1),F(2),F(1),F(1))[-1]==2)
    check(gate(F(1),F(1),F(1),F(1),F(1))[-1]==0)
    check(F(2)+F(2)-2*F(1)==2 and F(1)+F(1)-2*F(1)==0)
    return dict(stage='CC47 constrained Schur',all_passed=True,new_exact_checks=count,
                native_gate_evaluated=False,arithmetic_floor_certified=False,
                RH_proved=False,lean_certified=False,
                constructor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_CONSTRAINED_SCHUR_CC47_VALIDATION_20261009.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
