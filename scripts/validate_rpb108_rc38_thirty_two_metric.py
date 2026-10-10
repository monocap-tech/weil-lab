"""RC38 thirty-two-mode metric and rounded rational trials for eight targets."""
from validate_rpb108_rc30_interval_metric import I,PI,hictx,loctx,endpoint
from validate_rpb108_rc29_atom_reduction import overlap
from validate_rpb108_rc31_trial_riesz import inverse,mm,psd
from fractions import Fraction as F
from math import factorial
import json,sys

def run():
    ntrial=32; ntarget=8; N=192; B=F(11,10); R=2*B
    H=[sum((F(1,k) for k in range(1,n+1)),F(0)) for n in range(N+1)]
    cmid=F(-3203794213-3203306050,2*10**9); dc=F(488163,2*10**9)
    Z=I(1).exp()*2*PI*I(R); assert Z.h<42
    q=[I(0)]*N; l=[I(0)]*N; power=I(1)
    for n in range(1,N+1):
        power=power*Z/n
        if n%2==0: q[n-1]=(-1)**(n//2+1)*power/2
        else:
            sign=(-1)**((n-1)//2)
            q[n-1]=sign*power*I(H[n]+cmid-1)/PI
            l[n-1]=-sign*power/PI
    eps=F(4,3)*200*F(42)**193/factorial(193)
    mass=[2*B/F(2*j+1) for j in range(ntrial)]
    G=[[F(0)]*ntrial for _ in range(ntrial)]
    error=F(0); entries=[]
    for i in range(ntrial):
        for j in range(i,ntrial):
            if (i+j)%2: continue
            op=overlap(i,j)
            # Integrate each full overlap polynomial before summing kernel
            # coefficients; both spatial triangles are already in overlap.
            value=I(0)
            for p in range(N):
                regular=sum((a*R**m/F(p+m+1) for m,a in enumerate(op)),F(0))
                logarithmic=-sum((a*R**m/F((p+m+1)**2) for m,a in enumerate(op)),F(0))
                value=value+q[p]*I(regular)+l[p]*I(logarithmic)
            value=value+I(endpoint(i,j))
            if i==j: value=value+I((H[i]+cmid)*mass[i])
            assert hictx.subtract(value.h,value.l)<I(F(1,10**30)).h
            den=10**20
            low=int(loctx.multiply(value.l,I(den).l).to_integral_value(rounding='ROUND_FLOOR'))
            high=int(hictx.multiply(value.h,I(den).h).to_integral_value(rounding='ROUND_CEILING'))
            G[i][j]=G[j][i]=F(low+high,2*den)
            error=max(error,F(high-low,2*den))
            entries.append(dict(i=i,j=j,nominal_lower=str(F(low,den)),nominal_upper=str(F(high,den))))
        print('metric row',i,'done',file=sys.stderr,flush=True)
    E=2*dc+eps+ntrial*error/min(mass)
    assert E<F(1,1000)
    D=[[mass[i] if i==j else F(0) for j in range(ntrial)] for i in range(ntrial)]
    assert psd([[G[i][j]-(1-E)*D[i][j] for j in range(ntrial)] for i in range(ntrial)])
    rhs=[[mass[i] if i==j else F(0) for j in range(ntarget)] for i in range(ntrial)]
    V=mm(inverse(G),rhs); assert mm(G,V)==rhs
    coeff_den=10**30
    def rounded(x):
        scaled=x*coeff_den+F(1,2)
        return F(scaled.numerator//scaled.denominator,coeff_den)
    Vrounded=[[rounded(x) for x in row] for row in V]
    assert all(abs(Vrounded[i][j]-V[i][j])<=F(1,2*coeff_den)
               for i in range(ntrial) for j in range(ntarget))
    nominal_product=mm(G,Vrounded)
    solve_error=max(abs(nominal_product[i][j]-rhs[i][j]) for i in range(ntrial) for j in range(ntarget))
    assert solve_error<F(1,10**27)
    assert all(Vrounded[i][j]==0 for i in range(ntrial) for j in range(ntarget) if (i-j)%2)
    V=Vrounded
    return dict(milestone='RC38',status='PASS',trial_dimension=ntrial,target_dimension=ntarget,
        kernel_degree=N,kernel_remainder_upper=str(eps),
        coefficient_rounding_upper=str(F(1,2*coeff_den)),
        nominal_solve_entry_error_upper=str(solve_error),
        exact_nominal_solve_performed_before_rounding=True,
        emitted_coefficients_exact_nominal_solution=False,
        metric_center=[[str(x) for x in r] for r in G],physical_mass=list(map(str,mass)),
        mass_metric_error_upper=str(E),nominal_entry_intervals=entries,
        coefficients=[[str(x) for x in r] for r in V],native_head_certified=False,aperture_extended=False)

if __name__=='__main__': print(json.dumps(run(),indent=2))
