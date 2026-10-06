"""Uniform actual smooth-source enclosure; no numerical quadrature or Gram claim."""
import json
from math import comb, factorial, isqrt
from functools import lru_cache
from certify_native_legendre_small_window import F, I, add, mul, bernoulli, atan, log_rational, log_interval, sqrt_rational
from certify_native_endpoint_log_gram import shifted_legendre


@lru_cache(maxsize=None)
def regular_difference_factor(j,k):
    """Exact beta-integral evaluation of the existing binomial sum."""
    if k==0:return -sum((F(1,r) for r in range(1,j+1)),F(0))
    return F(factorial(j)*factorial(k-1),factorial(k+j))-F(1,k)


def compose(p, shift, scale=F(1)):
    out=[shift*0 for _ in p]
    powers=[shift*0+1]
    for _ in range(len(p)-1):powers.append(powers[-1]*shift)
    for n,c in enumerate(p):
        for k in range(n+1):
            out[k]+=c*comb(n,k)*scale**k*powers[n-k]
    return out


def exact_reflect(p):
    """Exact p(1-t), clearing denominators before the binomial sum."""
    from math import lcm
    denominator=lcm(*(c.denominator for c in p))
    integers=[int(c*denominator) for c in p]
    out=[0]*len(p)
    for n,c in enumerate(integers):
        for k in range(n+1):out[k]+=c*comb(n,k)*(-1)**k
    return [F(c,denominator) for c in out]


def power(x,n):
    out=x*0+1
    for _ in range(n):
        out=out*x
    return out


def sqrt_rational(x):
    g=I.grid;n=isqrt((x*g*g).__floor__())
    return I(F(n,g),F(n+1,g))


def certificate():
    previous=I.grid;I.grid=10**200
    try:
        return quantize(compute())
    finally:
        I.grid=previous


def quantize(result,digits=40):
    """Store short rational coefficients with an explicit uniform rounding budget."""
    g=10**digits
    for row in result['rows']:
        old_radius=max(F(p['coefficient_radius']) for p in row['panels'])
        for panel in row['panels']:
            old=[F(c) for c in panel['coefficients']]
            new=[F((c*g).__floor__(),g) for c in old]
            extra=sum((abs(x-y) for x,y in zip(old,new)),F(0))
            panel['coefficients']=[str(c) for c in new]
            panel['coefficient_radius']=str(F(panel['coefficient_radius'])+extra)
        error=F(row['unnormalized_uniform_error'])-old_radius+max(F(p['coefficient_radius']) for p in row['panels'])
        row['unnormalized_uniform_error']=str(error)
        row['normalized_uniform_error']=str(sqrt_rational(F(2*row['degree']+1)).hi*error)
    eta=sqrt_rational(sum((F(r['normalized_uniform_error'])**2 for r in result['rows']),F(0))).hi
    assert eta<F(1,10**23)
    result['source_map_error_upper']=str(eta)
    result['source_map_error_display']=float(eta)
    result['coefficient_grid_digits']=digits
    return result


def compute(degree=35, a=F(11,20)):
    if a not in (F(11,20),F(14,25),F(3,5),F(16,25),F(69,100),F(7,10),F(3,4),F(4,5),F(81,100),F(41,50),F(17,20),F(22,25),F(9,10),F(91,100)):
        raise ValueError("Unsupported source aperture")
    d=2*a
    if a in (F(81,100),F(41,50),F(17,20),F(22,25),F(9,10),F(91,100)):
        assert log_rational(F(5)).hi<d<log_rational(F(7)).lo
    elif a in (F(7,10),F(3,4),F(4,5)):
        assert log_rational(F(4)).hi<d<log_rational(F(5)).lo
    else:
        assert log_rational(F(3)).hi<d<log_rational(F(4)).lo
    if a==F(81,100):
        assert log_rational(F(5)).hi<2*d<log_rational(F(26)).lo
        assert 2*d<=F(81,25)
    elif a==F(41,50):
        assert log_rational(F(5)).hi<2*d<log_rational(F(27)).lo
        assert 2*d<=F(82,25)
    elif a==F(17,20):
        assert log_rational(F(5)).hi<2*d<log_rational(F(30)).lo
        assert 2*d<=F(17,5)
    elif a==F(22,25):
        assert log_rational(F(5)).hi<2*d<log_rational(F(34)).lo
        assert 2*d<=F(88,25)
    elif a==F(9,10):
        assert log_rational(F(5)).hi<2*d<log_rational(F(37)).lo
        assert 2*d<=F(18,5)
    elif a==F(91,100):
        assert log_rational(F(5)).hi<2*d<log_rational(F(39)).lo
        assert 2*d<=F(91,25)
    elif a==F(4,5):
        assert 2*d<log_rational(F(25)).lo
        assert 2*d>log_rational(F(5)).hi and 2*d<=F(16,5)
    elif a==F(3,4):
        assert 2*d<log_rational(F(21)).lo
        assert 2*d>log_rational(F(4)).hi and 2*d<=3
    elif a==F(7,10):
        assert log_rational(F(16)).hi<2*d<log_rational(F(17)).lo
        assert 2*d<=F(14,5)
    elif a==F(69,100):
        assert 2*d<log_rational(F(16)).lo
        assert 2*d>log_rational(F(15)).hi and 2*d<F(14,5)
    elif a==F(16,25):
        assert 2*d<log_rational(F(13)).lo
        assert 2*d>log_rational(F(8)).hi and 2*d<F(21,8)
    elif a==F(3,5):
        assert 2*d<log_rational(F(12)).lo
        assert 2*d>log_rational(F(5)).hi and 2*d<=F(12,5)
    else:
        assert 2*d<log_rational(F(10)).lo
        assert 2*d>log_rational(F(4)).hi
        assert 2*d<F(9,4)
    assert (d/4 if a in (F(7,10),F(3,4),F(4,5),F(81,100),F(41,50),F(17,20),F(22,25),F(9,10),F(91,100)) else d/2)<log_rational(F(2)).lo
    if degree==83:
        if a not in (F(81,100),F(41,50),F(17,20),F(22,25),F(9,10),F(91,100)):raise ValueError('Degree 83 requires aperture 81/100 or 41/50')
    elif degree==51:
        if a!=F(4,5):raise ValueError('Degree 51 requires aperture 4/5')
    elif degree not in (35,47) or (degree==47 and a not in (F(14,25),F(3,5),F(16,25),F(69,100),F(7,10),F(3,4))) or (a in (F(3,5),F(16,25),F(69,100),F(7,10),F(3,4),F(4,5),F(81,100),F(41,50),F(17,20),F(22,25),F(9,10),F(91,100)) and degree!=47) or a in (F(4,5),F(81,100),F(41,50),F(17,20),F(22,25),F(9,10),F(91,100)):
        raise ValueError('Unsupported source dimension/aperture')
    N,K=(90,100) if degree==83 else (60,52) if a==F(4,5) else ((60,48) if a==F(3,4) else ((60,44) if a==F(7,10) else ((60,40) if a in (F(3,5),F(16,25),F(69,100)) else (60,32))))
    B=bernoulli(2*K+2)
    bp=[F(0)]*(2*K+1)
    bp[0],bp[1]=F(1),d
    for k in range(1,K+1):
        bp[2*k]=B[2*k]*(2*d)**(2*k)/factorial(2*k)
    A=[c/2 for c in mul(bp,[(-d/2)**k/factorial(k) for k in range(N+1)])]
    assert A[0]==F(1,2)
    # |A-Atilde| <= ce*s^(N+1)+cb*s^(2K+2), 0<=s<=1.
    ce=(F(9,4) if a in (F(9,10),F(91,100)) else F(11,5) if a==F(22,25) else F(17,8) if a==F(17,20) else F(41,20) if a==F(41,50) else F(81,40) if a==F(81,100) else (F(2) if a in (F(3,4),F(4,5)) else F(3,2)))*(d/2)**(N+1)/factorial(N+1)
    cb=4*(d/3)**(2*K+2)/(1-(d/3)**2)
    he=ce/(N+1)+cb/(2*K+2)
    ae=ce/(N+2)+cb/(2*K+3)
    H=[F(0)]+[-c/k for k,c in enumerate(A) if k>0]
    pi=16*atan(F(1,5))-4*atan(F(1,239))
    logtwo=log_rational(F(2))
    ell=logtwo/d
    ell3=log_rational(F(3))/d
    if a in (F(7,10),F(3,4),F(4,5),F(81,100),F(41,50),F(17,20),F(22,25),F(9,10),F(91,100)):
        ell4=log_rational(F(4))/d
        if a in (F(9,10),F(91,100)):
            from certify_native_translation_panel_order import translation_panels
            panel_geometry=translation_panels(a,logarithm=log_rational)
        else:
            assert (I(1)-ell4).hi<(I(1)-ell3).lo<ell.lo
            assert ell.hi<(I(1)-ell).lo<ell3.lo<ell4.lo<1
    else:
        assert (I(1)-ell3).hi<(I(1)-ell).lo<ell.hi<ell3.lo
    # Higher-order Euler--Maclaurin gamma enclosure.
    n,order=100,50 if degree==83 else 20
    gamma=I(sum((F(1,k) for k in range(1,n+1)),F(0))-F(1,2*n))-log_rational(F(n))
    gamma+=sum((B[2*k]/F(2*k*n**(2*k)) for k in range(1,order+1)),F(0))
    ge=abs(B[2*order+2])/F((2*order+2)*n**(2*order+2))
    gamma+=I(-ge,ge)
    # psi(1/4)-log pi+2H(0) = -gamma-log(2pi).
    constant=-gamma-logtwo-log_interval(pi)-log_rational(d)
    reflect=exact_reflect if degree==83 else lambda p:compose(p,F(1),F(-1))
    hsum=add(H,reflect(H))
    pole_exp=[(d/2)**k/factorial(k) for k in range(N+1)]
    ep=compose(pole_exp,F(-1,2))
    em=compose(pole_exp,F(1,2),F(-1))
    exp_error=2*(d/4)**(N+1)/factorial(N+1)
    rows=[]
    source_degree=degree
    for degree,p in enumerate(shifted_legendre(source_degree)):
        smooth=mul(p,hsum)
        if source_degree in (35,47,51,83):
            left=[F(0)]*(len(p)+len(A)-1)
            for j,c in enumerate(p):
                for k,kernel_coefficient in enumerate(A):
                    factor=(regular_difference_factor(j,k) if source_degree in (47,51,83) else
                            sum((F(comb(j,r)*(-1)**r,k+r) for r in range(1,j+1)),F(0)))
                    left[j+k]+=c*kernel_coefficient*factor
            right=[(-1)**degree*c for c in (reflect(left) if source_degree==83 else compose(left,F(1),F(-1)))]
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
        primes=[(logtwo/sqrt_rational(F(2)),ell),
                (log_rational(F(3))/sqrt_rational(F(3)),ell3)]
        if a in (F(7,10),F(3,4),F(4,5),F(81,100),F(41,50),F(17,20),F(22,25),F(9,10),F(91,100)):primes.append((logtwo/2,ell4))
        if a in (F(81,100),F(41,50),F(17,20),F(22,25),F(9,10),F(91,100)):primes.append((log_rational(F(5))/sqrt_rational(F(5)),log_rational(F(5))/d))
        panels=[]
        # Exact order: 0, 1-ell3, 1-ell2, ell2, ell3, 1.
        active=[[(0,1),(1,1)],[(0,1)],[],[(0,-1)],[(0,-1),(1,-1)]]
        if a in (F(7,10),F(3,4),F(4,5),F(81,100),F(41,50),F(17,20),F(22,25),F(9,10),F(91,100)):
            active=[[(0,1),(1,1),(2,1)],[(0,1),(1,1)],[(0,1)],
                    [(0,1),(0,-1)],[(0,-1)],[(0,-1),(1,-1)],[(0,-1),(1,-1),(2,-1)]]
        if a in (F(81,100),F(41,50),F(17,20),F(22,25),F(9,10),F(91,100)):
            active=[[(0,1),(1,1),(2,1),(3,1)],[(0,1),(1,1),(2,1)],[(0,1),(1,1)],[(0,1)],
                    [(0,1),(0,-1)],[(0,-1)],[(0,-1),(1,-1)],[(0,-1),(1,-1),(2,-1)],
                    [(0,-1),(1,-1),(2,-1),(3,-1)]]
        if a in (F(9,10),F(91,100)):active=panel_geometry['active']
        translated={}
        if source_degree==83:
            for index,(amplitude,shift) in enumerate(primes):
                for sign in (1,-1):translated[index,sign]=[-amplitude*c for c in compose(p,sign*shift)]
        for translations in active:
            row=core[:]
            for index,sign in translations:
                amplitude,shift=primes[index]
                row=add(row,translated[index,sign] if source_degree==83 else [-amplitude*c for c in compose(p,sign*shift)])
            mids=[(c.lo+c.hi)/2 if isinstance(c,I) else c for c in row]
            radius=sum(((c.hi-c.lo)/2 if isinstance(c,I) else F(0) for c in row),F(0))
            panels.append(dict(coefficients=[str(c) for c in mids],coefficient_radius=str(radius)))
        # Actual |p|<=1, |d_x p|<=degree(degree+1); both distances <=1.
        truncation=2*he+2*degree*(degree+1)*ae+10*d*exp_error
        unnormalized=truncation+max(F(v['coefficient_radius']) for v in panels)
        normalized=sqrt_rational(F(2*degree+1)).hi*unnormalized
        assert normalized<F(1,10**23)
        rows.append(dict(degree=degree,panels=panels,unnormalized_uniform_error=str(unnormalized),normalized_uniform_error=str(normalized)))
    eta2=sum((F(r['normalized_uniform_error'])**2 for r in rows),F(0))
    eta=sqrt_rational(eta2).hi
    assert eta<F(1,10**23)
    result=dict(status=f'certified full {source_degree+1}-source prime-3 piecewise polynomial approximation',
                exponential_order=N,bernoulli_pairs=K,gamma_order=order,interval_grid_digits=len(str(I.grid))-1,aperture=str(a),coordinate='t=(x+a)/(2a)',
                prime_terms=[2,3],panel_endpoints=['0','1-log(3)/(2a)','1-log(2)/(2a)','log(2)/(2a)','log(3)/(2a)','1'],
                normalization='physical source coefficients multiply by sqrt((2*degree+1)/(2a)); error fields are L2 bounds',
                source_map_error_upper=str(eta),source_map_error_display=float(eta),
                rows=rows,full_residual_gram_certified=False,actual_schur_sign_certified=False)
    if a in (F(7,10),F(3,4),F(4,5),F(81,100),F(41,50),F(17,20),F(22,25),F(9,10),F(91,100)):
        result['status']=f'certified full {source_degree+1}-source prime-4 piecewise polynomial approximation'
        result['prime_terms']=[2,3,4]
        result['panel_endpoints']=['0','1-log(4)/(2a)','1-log(3)/(2a)','log(2)/(2a)',
                                   '1-log(2)/(2a)','log(3)/(2a)','log(4)/(2a)','1']
        result['prime4_amplitude']='log(2)/2'
    if a in (F(81,100),F(41,50),F(17,20),F(22,25),F(9,10),F(91,100)):
        result['status']=f'certified full {source_degree+1}-source prime-5 piecewise polynomial approximation'
        result['prime_terms']=[2,3,4,5]
        result['panel_endpoints']=['0','1-log(5)/(2a)','1-log(4)/(2a)','1-log(3)/(2a)','log(2)/(2a)',
                                 '1-log(2)/(2a)','log(3)/(2a)','log(4)/(2a)','log(5)/(2a)','1']
        result['prime5_amplitude']='log(5)/sqrt(5)'
    if a in (F(9,10),F(91,100)):
        result['panel_endpoints']=panel_geometry['labels']
        result['panel_order_interface']='strictly certified actual support cutoff order'
        result['panel_active_argument_shifts']=panel_geometry['active']
    return result


if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
