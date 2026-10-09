"""Exact atomic-limit geometry, not smooth nulls or actual eigenvectors."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def run():
    n=0
    def check(x):
        nonlocal n
        assert x
        n+=1
    r=F(3,2); e=r*r; cb=(r+1/r)/2; jb=r**3/(r**4-1)
    check(e==F(9,4))
    check(cb==F(13,12))
    check(jb==F(54,65))
    check(jb/cb==F(648,845)<2)
    check(2*(r-1)==1<F(21,20))
    positive_mass=F(1); negative_mass=1/cb
    check(positive_mass==negative_mass*cb==1)
    check(4*jb*positive_mass*negative_mass/4==jb/cb)
    for k in range(2,9):
        check(abs(e-k)>0)
        check(abs(e*e-k)>0)
    check(min(abs(e-k) for k in range(2,9))==F(1,4))
    for mu in (F(0),F(1,3),F(7,2)):
        qh,qa,m=F(4),F(3),F(5)
        check((qh-mu*m)-(qa-mu*m)==qh-qa)
    return dict(stage='CC45 native nodal correlation',all_passed=True,
                new_exact_checks=n,actual_null_vectors_evaluated=False,
                null_adapted_arithmetic_estimate_certified=False,RH_proved=False,
                constructor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_NODAL_CORRELATION_CC45_VALIDATION_20261009.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
