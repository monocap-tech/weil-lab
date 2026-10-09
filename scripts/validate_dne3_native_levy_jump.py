"""Exact rational algebra audit of zero-extension, shift, and odd folding."""
from fractions import Fraction as F
from itertools import product
import json
def run():
    U=range(-7,8); I=range(-2,3)
    w={m:F(1,2**m)/(1-F(1,16**m)) for m in range(1,15)}
    shifts={1:F(1,3),2:F(2,5),3:F(5,7)}
    S=sum(shifts.values(),F(0)); a0=F(-9,2); K=-a0+2*S
    checks=0
    for z in product((-1,0,1),repeat=5):
        f={i:F(z[i+2]) for i in I}
        full={i:f.get(i,F(0)) for i in U}
        m=sum((v*v for v in f.values()),F(0))
        J=sum((w[abs(i-k)]*(full[i]-full[k])**2 for i in U for k in U if i!=k),F(0))/2
        interior=sum((w[abs(i-k)]*(f[i]-f[k])**2 for i in I for k in I if i!=k),F(0))/2
        exterior=sum((w[abs(i-k)]*f[i]**2 for i in I for k in U if k not in I),F(0))
        assert J==interior+exterior
        checks+=1
        D=sum((c*sum(((full[i]-full.get(i+k,F(0)))**2 for i in range(-7,8-k)),F(0)) for k,c in shifts.items()),F(0))
        P=-2*sum((c*sum((f[i]*f.get(i+k,F(0)) for i in I),F(0)) for k,c in shifts.items()),F(0))
        assert D-2*S*m==P
        checks+=1
        assert J+D-K*m==J+a0*m+P
        checks+=1
    for p,q in product((-2,-1,0,1,2),repeat=2):
        u={1:F(p),2:F(q)}
        f={-2:-u[2],-1:-u[1],0:F(0),1:u[1],2:u[2]}
        D=sum((w[abs(i-k)]*(f[i]-f[k])**2 for i in I for k in I if i!=k),F(0))/2
        fold=sum((((w[abs(i-k)]*(u[i]-u[k])**2) if i!=k else F(0))
                   +w[i+k]*(u[i]+u[k])**2 for i in (1,2) for k in (1,2)),F(0))
        assert D==fold+2*sum((w[i]*u[i]**2 for i in (1,2)),F(0))
        checks+=1
        floor=4*sum((u[i]**2*sum((w[i+k] for k in (1,2)),F(0)) for i in (1,2)),F(0))
        assert D>=floor
        checks+=1
    assert checks==779
    return {"stage":"DNE3","checks":checks,"passed":True,"true_zeta_null_tested":False}
if __name__=="__main__":print(json.dumps(run(),indent=2))
