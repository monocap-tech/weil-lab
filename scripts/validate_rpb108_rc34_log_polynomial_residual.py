"""RC34 whole residual enclosure by entire kernel series and exact log moments."""
from validate_rpb108_rc30_interval_metric import I, PI, iv, loctx, hictx
from validate_rpb108_rc29_atom_reduction import legendre
from fractions import Fraction as F
from math import comb,factorial
from pathlib import Path
import json,sys

N=192
def transformed(p):
    out=[F(0)]*len(p)
    for n,x in enumerate(p):
        for k in range(n+1): out[k]+=x*comb(n,k)*2**k*(-1)**(n-k)
    return out
def reflect(p):
    out=[I(0)]*len(p)
    for n,x in enumerate(p):
        for k in range(n+1): out[k]=out[k]+x*(comb(n,k)*(-1)**k)
    return out
def polyadd(a,b,scale=1):
    out=[I(0)]*max(len(a),len(b))
    for i,x in enumerate(a): out[i]=out[i]+x
    for i,x in enumerate(b): out[i]=out[i]+scale*x
    return out
def scalar(p,s): return [x*s for x in p]
def convolution(a,b):
    out=[I(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x.l==x.h==0: continue
        for j,y in enumerate(b):
            if y.l==y.h==0: continue
            out[i+j]=out[i+j]+x*y
    return out
def integrate(a,b,mom):
    return sum((x*mom[k] for k,x in enumerate(convolution(a,b))),I(0))

def run(path):
    V=[[F(x) for x in r] for r in json.loads(Path(path).read_text())['coefficients']]
    H=[sum((F(1,k) for k in range(1,n+1)),F(0)) for n in range(2*(N+9)+1)]
    H2=[sum((F(1,k*k) for k in range(1,n+1)),F(0)) for n in range(len(H))]
    cmid=F(-3203794213-3203306050,2*10**9)
    dc=F(488163,2*10**9)
    R=F(11,5); B=R/2; e=I(1).exp(); Z=e*2*PI*I(R)
    assert Z.h<42
    q=[I(0)]*N; l=[I(0)]*N
    power=I(1)
    for n in range(1,N+1):
        power=power*Z/n  # Z^n/n!
        if n%2==0:
            q[n-1]=q[n-1]+(-1)**(n//2+1)*power/2
        else:
            sign=(-1)**((n-1)//2)
            q[n-1]=q[n-1]+sign*power*(I(H[n]+cmid-1))/PI
            l[n-1]=-sign*power/PI
    # Bound regular and log series tails together, including division by s.
    eps=F(4,3)*(N+8)*F(42)**(N+1)/factorial(N+1)
    assert eps<F(1,10**40)
    degree=2*(N+8)
    moments=[[],[],[],[],[],[]]
    zeta=PI*PI/6
    for n in range(degree+1):
        a=n+1; ha=H[a]; hb=H2[a]
        vals=[I(F(1,a)),I(-F(1,a*a)),I(-ha/a),I(F(2,a**3)),
              I((ha*ha+hb)/a),I(ha/F(a*a)+hb/a)-zeta/a]
        for v,arr in zip(vals,moments): arr.append(v)
    P=[transformed(legendre(i)) for i in range(8)]
    rows=[]
    trace_bound=F(0)
    for j in range(8):
        v=[F(0)]*8; tv=[F(0)]*8
        for i in range(8):
            for m,x in enumerate(P[i]):
                v[m]+=V[i][j]*x; tv[m]+=H[i]*V[i][j]*x
        aleft=[I(0)]*(N+8); bleft=[I(0)]*(N+8)
        for p in range(N):
            for m,vm in enumerate(v):
                if vm==0: continue
                d=p+m+1; beta=F(factorial(p)*factorial(m),factorial(d))
                bleft[d]=bleft[d]+l[p]*I(vm*beta)
                aleft[d]=aleft[d]+(q[p]+l[p]*I(H[p]-H[d]))*I(vm*beta)
        ka=polyadd(aleft,reflect(aleft),(-1)**j)
        kb=bleft; kc=scalar(reflect(bleft),(-1)**j)
        target=[I(x) for x in P[j]]
        base=polyadd(target,[I(tv[m]+cmid*v[m]) for m in range(8)],-1)
        A=polyadd(base,ka,-1)
        BB=polyadd([I(x/2) for x in v],kb,-1)
        C=polyadd([I(x/2) for x in v],kc,-1)
        norm=I(R)*(integrate(A,A,moments[0])+2*integrate(A,BB,moments[1])+
            2*integrate(A,C,moments[2])+integrate(BB,BB,moments[3])+
            integrate(C,C,moments[4])+2*integrate(BB,C,moments[5]))
        assert norm.l>0 and hictx.subtract(norm.h,norm.l)<I(F(1,10**20)).h
        physical_sq=sum((2*B/F(2*i+1)*V[i][j]**2 for i in range(8)),F(0))
        # Full source error: scalar uncertainty times (I+band projection),
        # plus the bounded entire-kernel remainder.
        source_error=I(2*dc+eps)*I(physical_sq).sqrt()
        upper=(norm.sqrt()+source_error)
        sq=upper*upper
        den=10**12
        rat=F(int(hictx.multiply(sq.h,I(den).h).to_integral_value(rounding='ROUND_CEILING')),den)
        trace_bound+=rat/(2*B/F(2*j+1))
        rows.append(dict(column=j,nominal_squared_interval=norm.pair(),
            physical_residual_squared_upper=str(rat),
            physical_residual_upper_display=float(rat)**.5))
        print('column',j,'certified upper',float(rat)**.5,file=sys.stderr,flush=True)
    assert trace_bound<F(31,200), trace_bound
    canonical=F(252,257)*trace_bound
    assert canonical<F(19,125)
    return dict(milestone='RC34',status='PASS',kernel_degree=N,
        kernel_remainder_upper=str(eps),columns=rows,
        collective_physical_squared_upper=str(trace_bound),
        collective_canonical_squared_upper=str(canonical),
        whole_physical_residual_certified=True,actual_Riesz_inverse_certified=False,
        native_head_certified=False,aperture_extended=False)

if __name__=='__main__':
    path=sys.argv[1] if len(sys.argv)>1 else Path(__file__).parent.parent/'certificates/rpb108_rc31_trial_riesz.json'
    print(json.dumps(run(path),indent=2))
