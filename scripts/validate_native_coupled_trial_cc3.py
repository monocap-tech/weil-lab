"""Exact finite controls for CC3's trial-residual inverse upper bound."""
from fractions import Fraction as F
import json

def run():
    checks=0
    for c in (F(1,2),F(699,1000),F(1),F(3,2)):
        for ratio in (F(1),F(3,2),F(2),F(5)):
            diagonal=(c,ratio*c)
            for b in ((F(1),F(0)),(F(1),F(1)),(F(2),F(-1))):
                true=sum((x*x/d for x,d in zip(b,diagonal)),F(0))
                baseline=sum((x*x/c for x in b),F(0))
                for z in ((F(1),F(0)),(F(0),F(1)),(F(1),F(-2))):
                    pairing=sum((x*y for x,y in zip(b,z)),F(0))
                    native=sum((d*y*y for d,y in zip(diagonal,z)),F(0))
                    cross=sum((x*d*y for x,d,y in zip(b,diagonal,z)),F(0))
                    norm=sum((d*d*y*y for d,y in zip(diagonal,z)),F(0))
                    A=2*cross/c-2*pairing;B=norm/c-native
                    assert B>=0;checks+=1
                    for t in (F(-2),F(-1,2),F(0),F(1,2),F(2)):
                        residual=sum(((x-t*d*y)**2/c for x,d,y in zip(b,diagonal,z)),F(0))
                        upper=2*t*pairing-t*t*native+residual
                        assert upper==baseline-t*A+t*t*B and upper>=true
                        checks+=1
                    if B>0:
                        optimum=A/(2*B)
                        improvement=optimum*A-optimum*optimum*B
                        assert improvement==A*A/(4*B) and baseline-improvement>=true
                        checks+=1
    # Alignment changes a lawful trial despite the same scalar source Gram.
    c=F(1);C=(F(1),F(4));z=(F(0),F(1))
    gains=[]
    for b in ((F(1),F(0)),(F(0),F(1))):
        A=2*sum((x*d*y for x,d,y in zip(b,C,z)),F(0))-2*sum((x*y for x,y in zip(b,z)),F(0))
        B=sum((d*d*y*y-d*y*y for d,y in zip(C,z)),F(0))
        gains.append(A*A/(4*B))
    assert gains==[F(0),F(3,4)];checks+=1
    # Wrong native-pairing sign can produce a false inverse bound.
    b=F(1);d=F(4);t=F(1,4)
    lawful=2*t*b-t*t*d+(b-t*d)**2
    unlawful=-2*t*b-t*t*d+(b-t*d)**2
    assert lawful==b*b/d and unlawful<b*b/d;checks+=1
    return dict(exact_controls=checks,all_passed=True,analytic_theorem_formalized=False,
                actual_target_certificate_replayed=False,full_target_schur_certified=False)

if __name__=='__main__':print(json.dumps(run(),indent=2))
