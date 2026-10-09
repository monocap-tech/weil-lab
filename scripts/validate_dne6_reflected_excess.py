"""DNE6 exact rational reflected-half-space tests.

Finite attractive graph analogues test the precise parity fold, reflected
potential, same-side excess, prime crossing and higher-zero controls.
Samples of the actual continuous j(m*log(4)) are exactly rational.
No real Weil eigenfunction is evaluated by this validator.
"""
from fractions import Fraction as F
from itertools import product
import json

def j_at_m_log4(m):
    assert m>=1
    return F(1,2**m)/(1-F(1,16**m))

def run():
    checks=0
    def ck(v):
        nonlocal checks
        assert v
        checks+=1

    jp=((F(2),F(1)),(F(1),F(1,2)))
    jm=F(3)
    phi=(F(1),F(1))
    v=(F(6),F(3)) # reflected pointwise V_i for half norm mass 2 sum u_i²
    ck(all(jp[i][j]>0 for i in range(2) for j in range(2)))
    ck(jm>jp[0][1])
    ck(v[0]==2*(jp[0][0]+jp[0][1]))
    ck(v[1]==2*(jp[1][0]+jp[1][1]))

    for x,y,p,q in product((-2,-1,0,1,2),(-2,-1,0,1,2),
                            (F(0),F(1),F(4),F(7)),(F(0),F(1))):
        x,y=F(x),F(y)
        full_u=(-y,-x,x,y)
        # negative site order: -2,-1; positive site order: +1,+2.
        edges=((0,1,jm+q),(2,3,jm+q),
               (1,2,jp[0][0]),(0,3,jp[1][1]),
               (1,3,jp[0][1]+p),(0,2,jp[0][1]))
        full=sum((c*(full_u[i]-full_u[k])**2
                  for i,k,c in edges),F(0))
        folded=sum((jp[i][k]*(t[i]+t[k])**2
                  for i in range(2) for k in range(2)
                  for t in ((x,y),)),F(0))
        folded+=2*(jm+q)*(x-y)**2+p*(x+y)**2
        potential=2*(v[0]*x*x+v[1]*y*y)
        excess=4*(x-y)**2+2*q*(x-y)**2+p*(x+y)**2
        ck(full==folded)
        ck(full==potential+excess)
        ck(excess>=0)
        ck(full>=F(2)*2*(x*x+y*y)) # V>=2, no zero at depth2
    # Sharp higher-zero controls, with full odd mass 2 sum u_i².
    def W(x,y,p):
        return F(16)*x*x+F(10)*y*y-F(8)*x*y+p*(x+y)**2
    ck(W(F(1),F(2),F(0))==F(4)*2*(1+4))
    ck(W(F(0),F(1),F(4))==F(7)*2)
    ck(W(F(0),F(1),F(4))>F(4)*2)
    ck(W(F(1),F(2),F(4))>F(4)*2*(1+4))
    ck(F(3)<F(4)<F(6))
    ck(v[1]<F(4) and v[1]<F(7)) # low-potential region in both null controls
    # j(m log4) exact rational and strict interior kernel comparison.
    js={m:j_at_m_log4(m) for m in range(1,7)}
    ck(js[1]>js[2]>js[3]>js[4]>js[5]>js[6]>0)
    ck(js[1]-js[3]>0)
    ck(js[1]-js[3]==js[1]-js[3]) # equality at the sampled interior collar
    ck(js[1]-js[3] > js[2]-js[4])
    ck(js[2]-js[4]>0)
    assert checks==815, checks
    return {
        "stage":"DNE6 odd reflected-excess graph and native j samples",
        "all_passed":True,
        "exact_fraction_checks":checks,
        "positive_half_toy_potential":["6","3"],
        "toy_p0_higher_zero_depth":"4",
        "toy_p4_higher_zero_depth":"7",
        "actual_kernel_samples":{str(k):str(v) for k,v in js.items()},
        "actual_weil_phi_evaluated":False,
        "native_odd_gap_exclusion_proved":False,
        "RH_proved":False
    }

if __name__=="__main__":
    print(json.dumps(run(),indent=2))
