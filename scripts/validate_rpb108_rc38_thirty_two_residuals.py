"""RC38 whole mixed residual Gram for thirty-two-mode rounded rational trials."""
from validate_rpb108_rc35_enriched_residuals import (
    I,PI,loctx,hictx,N,transformed,reflect,polyadd,scalar,integrate)
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc31_trial_riesz import mm,tr,psd
from fractions import Fraction as F
from math import comb,factorial
from pathlib import Path
import json,sys,hashlib

def build_forms(V):
    ntrial=len(V); ntarget=len(V[0])
    assert (ntrial,ntarget)==(32,8)
    assert all(V[i][j]==0 for i in range(ntrial) for j in range(ntarget) if (i-j)%2)
    H=[sum((F(1,k) for k in range(1,n+1)),F(0)) for n in range(2*(N+ntrial+1)+1)]
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
    eps=F(4,3)*(N+ntrial)*F(42)**(N+1)/factorial(N+1)
    assert eps<F(1,10**40)
    degree=2*(N+ntrial)
    moments=[[],[],[],[],[],[]]
    zeta=PI*PI/6
    for n in range(degree+1):
        a=n+1; ha=H[a]; hb=H2[a]
        vals=[I(F(1,a)),I(-F(1,a*a)),I(-ha/a),I(F(2,a**3)),
              I((ha*ha+hb)/a),I(ha/F(a*a)+hb/a)-zeta/a]
        for v,arr in zip(vals,moments): arr.append(v)
    P=[transformed(legendre(i)) for i in range(ntrial)]
    forms=[]
    for j in range(ntarget):
        v=[F(0)]*ntrial; tv=[F(0)]*ntrial
        for i in range(ntrial):
            for m,x in enumerate(P[i]):
                v[m]+=V[i][j]*x; tv[m]+=H[i]*V[i][j]*x
        aleft=[I(0)]*(N+ntrial); bleft=[I(0)]*(N+ntrial)
        for p in range(N):
            for m,vm in enumerate(v):
                if vm==0: continue
                d=p+m+1; beta=F(factorial(p)*factorial(m),factorial(d))
                bleft[d]=bleft[d]+l[p]*I(vm*beta)
                aleft[d]=aleft[d]+(q[p]+l[p]*I(H[p]-H[d]))*I(vm*beta)
        ka=polyadd(aleft,reflect(aleft),(-1)**j)
        kb=bleft; kc=scalar(reflect(bleft),(-1)**j)
        target=[I(x) for x in P[j]]
        base=polyadd(target,[I(tv[m]+cmid*v[m]) for m in range(ntrial)],-1)
        A=polyadd(base,ka,-1)
        BB=polyadd([I(x/2) for x in v],kb,-1)
        C=polyadd([I(x/2) for x in v],kc,-1)
        forms.append((A,BB,C))
        print('residual form',j,'built',file=sys.stderr,flush=True)
    return forms,moments,R,2*dc+eps

def pairing(f,g,mom,R):
    A,B,C=f; X,Y,Z=g
    return I(R)*(integrate(A,X,mom[0])+
        integrate(A,Y,mom[1])+integrate(B,X,mom[1])+
        integrate(A,Z,mom[2])+integrate(C,X,mom[2])+
        integrate(B,Y,mom[3])+integrate(C,Z,mom[4])+
        integrate(B,Z,mom[5])+integrate(C,Y,mom[5]))

def loewner_upper(Q,mass):
    # Every accepted endpoint is proved by exact rational LDL. No floating
    # eigensolver contributes to this upper certificate.
    n=len(Q)
    def accepts(t):
        return psd([[t*mass[i]*(i==j)-Q[i][j] for j in range(n)] for i in range(n)])
    low=F(0); high=sum((abs(Q[i][i])/mass[i] for i in range(n)),F(0))+1
    while not accepts(high): high*=2
    for _ in range(40):
        mid=(low+high)/2
        if accepts(mid): high=mid
        else: low=mid
    assert accepts(high)
    return high

def run(metric_path,previous_path):
    raw=Path(metric_path).read_bytes(); data=json.loads(raw)
    V=[[F(x) for x in r] for r in data['coefficients']]
    mass=list(map(F,data['physical_mass'])); targets=mass[:8]
    G=[[F(x) for x in r] for r in data['metric_center']]
    product=mm(G,V)
    solve_error=max(abs(product[i][j]-(mass[i] if i==j else F(0)))
                    for i in range(32) for j in range(8))
    assert solve_error==F(data['nominal_solve_entry_error_upper'])<F(1,10**27)
    forms,mom,R,delta=build_forms(V)
    previous=json.loads(Path(previous_path).read_text())
    Q=[[F(0)]*8 for _ in range(8)]; maxhalf=F(0); rows=[]
    for i in range(8):
        for j in range(i,8):
            if (i-j)%2: continue  # exact opposite-parity orthogonality
            value=pairing(forms[i],forms[j],mom,R)
            assert hictx.subtract(value.h,value.l)<I(F(1,10**20)).h
            if i==j:
                assert value.l>0
            den=10**20
            low=int(loctx.multiply(value.l,I(den).l).to_integral_value(rounding='ROUND_FLOOR'))
            high=int(hictx.multiply(value.h,I(den).h).to_integral_value(rounding='ROUND_CEILING'))
            Q[i][j]=Q[j][i]=F(low+high,2*den)
            half=F(high-low,2*den); maxhalf=max(maxhalf,half)
            rows.append(dict(i=i,j=j,lower=str(F(low,den)),upper=str(F(high,den))))
            print('Gram entry',i,j,'enclosed',file=sys.stderr,flush=True)
    eta=8*maxhalf/min(targets)
    beta_center=loewner_upper(Q,targets)
    beta_nominal=beta_center+eta
    trial_gram=mm(mm(tr(V),[[mass[i]*(i==j) for j in range(32)] for i in range(32)]),V)
    beta_trial=loewner_upper(trial_gram,targets)
    upper=I(beta_nominal).sqrt()+I(delta)*I(beta_trial).sqrt()
    squared=upper*upper
    den=10**12
    physical=F(int(hictx.multiply(squared.h,I(den).h).to_integral_value(rounding='ROUND_CEILING')),den)
    canonical=F(252,257)*physical
    assert physical<F(previous['collective_physical_squared_upper'])
    assert canonical<F(previous['collective_canonical_squared_upper'])
    return dict(milestone='RC38',status='PASS',trial_dimension=32,target_dimension=8,
        metric_certificate_sha256=hashlib.sha256(raw).hexdigest(),
        nominal_Gram_center=[[str(x) for x in r] for r in Q],
        nominal_Gram_entry_enclosures=rows,normalized_Gram_rounding_error_upper=str(eta),
        nominal_center_Loewner_upper=str(beta_center),nominal_residual_squared_upper=str(beta_nominal),
        trial_physical_Gram=[[str(x) for x in r] for r in trial_gram],
        trial_map_squared_upper=str(beta_trial),source_operator_error_upper=str(delta),
        collective_physical_squared_upper=str(physical),collective_canonical_squared_upper=str(canonical),
        previous_collective_physical_upper=previous['collective_physical_squared_upper'],
        previous_collective_canonical_upper=previous['collective_canonical_squared_upper'],
        whole_physical_mixed_residuals_certified=True,exact_Riesz_inverse_certified=False,
        native_head_certified=False,aperture_extended=False)

if __name__=='__main__':
    root=Path(__file__).parent.parent/'certificates'
    metric=sys.argv[1] if len(sys.argv)>1 else root/'rpb108_rc38_thirty_two_metric.json'
    previous=sys.argv[2] if len(sys.argv)>2 else root/'rpb108_rc36_mixed_residual_gram.json'
    print(json.dumps(run(metric,previous),indent=2))
