"""Uniform actual smooth-source enclosure; no numerical quadrature or Gram claim."""
import json
from math import comb, factorial, isqrt
from certify_native_legendre_small_window import F, I, add, mul, bernoulli, atan, log_rational, log_interval, sqrt_rational
from certify_native_endpoint_log_gram import shifted_legendre


def compose(p, shift, scale=F(1)):
    out=[shift*0 for _ in p]
    for n,c in enumerate(p):
        for k in range(n+1):
            out[k]+=c*comb(n,k)*scale**k*power(shift,n-k)
    return out


def power(x,n):
    out=x*0+1
    for _ in range(n):
        out=out*x
    return out


def certificate(degree=19, a=F(27,50)):
    if a not in (F(1,2), F(51,100), F(27,50)):
        raise ValueError("Unsupported source aperture")
    d=2*a
    assert log_rational(F(2)).hi<d<log_rational(F(3)).lo
    assert 2*d<log_rational(F(9)).lo
    assert 2*d>log_rational(F(4)).hi
    assert 2*d<F(9,4)
    assert d/2<log_rational(F(2)).lo
    if degree not in (7,19):
        raise ValueError('Only eight or twenty actual sources are audited')
    N,K=60,32
    B=bernoulli(2*K+2)
    bp=[F(0)]*(2*K+1)
    bp[0],bp[1]=F(1),d
    for k in range(1,K+1):
        bp[2*k]=B[2*k]*(2*d)**(2*k)/factorial(2*k)
    A=[c/2 for c in mul(bp,[(-d/2)**k/factorial(k) for k in range(N+1)])]
    assert A[0]==F(1,2)
    # |A-Atilde| <= ce*s^(N+1)+cb*s^(2K+2), 0<=s<=1.
    ce=F(3,2)*(d/2)**(N+1)/factorial(N+1)
    cb=4*(d/3)**(2*K+2)/(1-(d/3)**2)
    he=ce/(N+1)+cb/(2*K+2)
    ae=ce/(N+2)+cb/(2*K+3)
    H=[F(0)]+[-c/k for k,c in enumerate(A) if k>0]
    pi=16*atan(F(1,5))-4*atan(F(1,239))
    logtwo=log_rational(F(2))
    ell=logtwo/d
    # Higher-order Euler--Maclaurin gamma enclosure.
    n,order=100,12
    gamma=I(sum((F(1,k) for k in range(1,n+1)),F(0))-F(1,2*n))-log_rational(F(n))
    gamma+=sum((B[2*k]/F(2*k*n**(2*k)) for k in range(1,order+1)),F(0))
    ge=abs(B[2*order+2])/F((2*order+2)*n**(2*order+2))
    gamma+=I(-ge,ge)
    # psi(1/4)-log pi+2H(0) = -gamma-log(2pi).
    constant=-gamma-logtwo-log_interval(pi)-log_rational(d)
    hsum=add(H,compose(H,F(1),F(-1)))
    pole_exp=[(d/2)**k/factorial(k) for k in range(N+1)]
    ep=compose(pole_exp,F(-1,2))
    em=compose(pole_exp,F(1,2),F(-1))
    exp_error=2*(d/4)**(N+1)/factorial(N+1)
    rows=[]
    source_degree=degree
    for degree,p in enumerate(shifted_legendre(source_degree)):
        smooth=mul(p,hsum)
        if source_degree==19:
            left=[F(0)]*(len(p)+len(A)-1)
            for j,c in enumerate(p):
                for k,kernel_coefficient in enumerate(A):
                    factor=sum((F(comb(j,r)*(-1)**r,k+r) for r in range(1,j+1)),F(0))
                    left[j+k]+=c*kernel_coefficient*factor
            right=[(-1)**degree*c for c in compose(left,F(1),F(-1))]
            smooth=add(smooth,[-c for c in add(left,right)])
        else:
            for sign,d in [(-1,[F(0),F(1)]),(1,[F(1),F(-1)])]:
                for j,c in enumerate(p):
                    for r in range(1,j+1):
                        for k,kernel_coefficient in enumerate(A):
                            power_d=[F(comb(k+r,v))*d[0]**(k+r-v)*d[1]**v for v in range(k+r+1)]
                            term=[F(0)]*(j-r)+[c*comb(j,r)*sign**r*kernel_coefficient/(k+r)*v for v in power_d]
                            smooth=add(smooth,[-v for v in term])
        # M_+= integral_0^1 p(t) exp((t-1/2)/2)dt.
        mp=d*sum((c/F(k+1) for k,c in enumerate(mul(p,ep))),F(0))
        mm=(-1)**degree*mp
        assert abs(mp)<3
        core=[I(c)+constant*(p[k] if k<len(p) else 0) for k,c in enumerate(smooth)]
        core=add(core,[mm*ep[k]+mp*em[k] for k in range(N+1)])
        prime=logtwo/sqrt_rational(F(2))
        panels=[]
        # t in [0,1-ell], [1-ell,ell], [ell,1].
        for shift in (ell,None,-ell):
            row=core[:] if shift is None else add(core,[-prime*c for c in compose(p,shift)])
            mids=[(c.lo+c.hi)/2 if isinstance(c,I) else c for c in row]
            radius=sum(((c.hi-c.lo)/2 if isinstance(c,I) else F(0) for c in row),F(0))
            panels.append(dict(coefficients=[str(c) for c in mids],coefficient_radius=str(radius)))
        # Actual |p|<=1, |d_x p|<=degree(degree+1); both distances <=1.
        truncation=2*he+2*degree*(degree+1)*ae+10*d*exp_error
        unnormalized=truncation+max(F(v['coefficient_radius']) for v in panels)
        normalized=sqrt_rational(F(2*degree+1)).hi*unnormalized
        assert normalized<F(1,10**25)
        rows.append(dict(degree=degree,panels=panels,unnormalized_uniform_error=str(unnormalized),normalized_uniform_error=str(normalized)))
    eta2=sum((F(r['normalized_uniform_error'])**2 for r in rows),F(0))
    eta=sqrt_rational(eta2).hi
    assert eta<F(1,10**25)
    result=dict(status='certified actual smooth-source piecewise polynomial approximation',
                exponential_order=N,bernoulli_pairs=K,aperture=str(a),coordinate='t=(x+a)/(2a)',
                panel_endpoints=['0','1-log(2)/(2a)','log(2)/(2a)','1'],
                normalization='physical source coefficients multiply by sqrt((2*degree+1)/(2a)); error fields are L2 bounds',
                source_map_error_upper=str(eta),source_map_error_display=float(eta),
                rows=rows,full_residual_gram_certified=False,actual_schur_sign_certified=False)
    return result


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--degree',type=int,choices=[7,19],default=19)
    args=parser.parse_args()
    print(json.dumps(certificate(args.degree),indent=2))
