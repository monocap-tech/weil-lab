"""Exact rational native restrictions at audited apertures through a=3/5.

Larger apertures require an audited matrix-return constructor.

No floating values enter the certificate. Floats in JSON are display only.
"""
from fractions import Fraction as F
from math import comb, factorial
import json


def add(p, q):
    return [(p[k] if k < len(p) else F(0)) +
            (q[k] if k < len(q) else F(0)) for k in range(max(len(p), len(q)))]


def mul(p, q):
    out = [F(0)] * (len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] += x*y
    return out


def legendre(n):
    rows = [[F(1)], [F(0), F(1)]]
    for k in range(1, n):
        rows.append(add([F(0)]+[F(2*k+1,k+1)*x for x in rows[k]],
                        [-F(k,k+1)*x for x in rows[k-1]]))
    return rows[:n+1]


def correlation(p, q):
    out = [F(0)]*(len(p)+len(q))
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            for k in range(j+1):
                d = i+j-k+1
                c = x*y*comb(j,k)*(-1)**k/d
                out[k] += c
                for ell in range(d+1):
                    out[k+ell] -= c*comb(d,ell)*(-1)**(d-ell)
    return out


from certify_native_legendre_small_window import I


def log_rational(x, terms=100):
    assert x > 0
    # Reduce to [1,2); ln2 uses the same absolutely convergent series.
    def unit(y):
        z = (y-1)/(y+1)
        s = 2*sum((z**(2*k+1)/F(2*k+1) for k in range(terms)), F(0))
        e = 2*abs(z)**(2*terms+1)/((2*terms+1)*(1-z*z))
        return I(s-e,s+e)
    power = 0
    while x >= 2:
        x /= 2
        power += 1
    while x < 1:
        x *= 2
        power -= 1
    return unit(x)+power*unit(F(2))


def log_interval(x):
    return I(log_rational(x.lo).lo, log_rational(x.hi).hi)


def atan(x, terms=80):
    s = sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
    e = x**(2*terms+1)/F(2*terms+1)
    return I(s-e,s+e)


def bernoulli(n):
    rows = [F(1)]
    for m in range(1,n+1):
        rows.append(-sum((F(comb(m+1,k))*rows[k] for k in range(m)),F(0))/F(m+1))
    return rows


def positive_pivots(matrix):
    m = [row[:] for row in matrix]
    pivots = []
    for k in range(len(m)):
        pivot = m[k][k]
        if pivot.lo <= 0:
            raise ArithmeticError('Cannot certify positive pivot')
        pivots.append(pivot)
        for i in range(k+1,len(m)):
            for j in range(i,len(m)):
                m[i][j] = m[i][j]-m[i][k]*m[k][j]/pivot
                m[j][i] = m[i][j]
    return pivots


def sqrt_rational(x):
    from math import isqrt
    grid = 10**50
    lower = isqrt((x*grid*grid).__floor__())
    return I(F(lower,grid),F(lower+1,grid))


def certificate(a=F(1,4), return_matrix=False, degree=7, matrix_resume=None, matrix_observer=None):
    if a!=F(21,20) or degree!=111 or not return_matrix:
        raise ValueError('112-vector engine requires aperture 1, degree 111 and matrix return')
    if (matrix_resume is not None or matrix_observer is not None) and not (a in (F(23,25),F(93,100),F(47,50),F(19,20),F(24,25),F(21,20)) and degree==111 and return_matrix):
        raise ValueError("Native row recovery requires the 23/25 degree-111 matrix constructor")
    if a not in (F(1,4), F(1,2), F(51,100), F(27,50), F(11,20), F(14,25), F(3,5),F(16,25),F(69,100),F(7,10),F(3,4),F(4,5),F(81,100),F(41,50),F(17,20),F(22,25),F(9,10),F(91,100),F(23,25),F(93,100),F(47,50),F(19,20),F(24,25),F(21,20)):
        raise ValueError('Unsupported audited aperture')
    if degree not in (7,19,35,47,51,111) or (degree==19 and (a not in (F(1,2), F(51,100), F(27,50), F(11,20)) or not return_matrix)):
        raise ValueError('Degree 19 requires a supported matrix constructor')
    if degree==35 and (a not in (F(11,20), F(14,25)) or not return_matrix):
        raise ValueError('Degree 35 requires the prime-3 aperture matrix constructor')
    if degree==111 and (a not in (F(81,100),F(41,50),F(17,20),F(22,25),F(9,10),F(91,100),F(23,25),F(93,100),F(47,50),F(19,20),F(24,25),F(21,20)) or not return_matrix):
        raise ValueError("Degree 111 requires aperture 81/100 or 41/50 matrix")
    if a in (F(81,100),F(41,50),F(17,20),F(22,25),F(9,10),F(91,100),F(23,25),F(93,100),F(47,50),F(19,20),F(24,25),F(21,20)) and degree!=111:
        raise ValueError("Aperture 81/100 or 41/50 requires degree 111")
    if degree==51 and (a!=F(4,5) or not return_matrix):
        raise ValueError("Degree 51 requires aperture 4/5 matrix")
    if a==F(4,5) and degree!=51:
        raise ValueError("Aperture 4/5 requires degree 51")
    if degree==47 and (a not in (F(14,25),F(3,5),F(16,25),F(69,100),F(7,10),F(3,4)) or not return_matrix):
        raise ValueError("Degree 47 requires an audited prime-3 matrix constructor")
    if a in (F(51,100), F(27,50), F(11,20), F(14,25), F(3,5),F(16,25),F(69,100),F(7,10),F(3,4),F(4,5),F(81,100),F(41,50),F(17,20),F(22,25),F(9,10),F(91,100),F(23,25),F(93,100),F(47,50),F(19,20),F(24,25),F(21,20)) and (degree not in (19,35,47,51,111) or not return_matrix):
        raise ValueError('The larger aperture requires a supported matrix constructor')
    N,K=(400,400)
    L = 4*a
    exponential_bound = 3 if L == 1 else 9
    kernel_bound = 2 if L == 1 else 3
    if a in (F(11,20), F(14,25)):
        exponential_bound = 10
        assert L < log_rational(F(10)).lo
        assert L > log_rational(F(4)).hi and L < F(9,4)
        assert log_rational(F(3)).hi < 2*a < log_rational(F(4)).lo
    if a==F(3,5):
        exponential_bound=12
        assert L<log_rational(F(12)).lo
        assert L>log_rational(F(5)).hi and L<=F(12,5)
        assert log_rational(F(3)).hi<2*a<log_rational(F(4)).lo
    if a==F(16,25):
        exponential_bound=13
        assert L<log_rational(F(13)).lo
        assert L>log_rational(F(8)).hi and L<F(21,8)
        assert log_rational(F(3)).hi<2*a<log_rational(F(4)).lo
    if a==F(69,100):
        exponential_bound=16
        assert L<log_rational(F(16)).lo
        assert L>log_rational(F(15)).hi and L<F(14,5)
        assert log_rational(F(3)).hi<2*a<log_rational(F(4)).lo
    if a==F(7,10):
        exponential_bound=17
        assert log_rational(F(16)).hi<L<log_rational(F(17)).lo
        assert L<=F(14,5)
        assert log_rational(F(4)).hi<2*a<log_rational(F(5)).lo
    if a==F(3,4):
        exponential_bound=21;kernel_bound=4
        assert L<log_rational(F(21)).lo
        assert L>log_rational(F(4)).hi and L<=3
        assert log_rational(F(4)).hi<2*a<log_rational(F(5)).lo
    if a==F(4,5):
        exponential_bound=25;kernel_bound=4
        assert L<log_rational(F(25)).lo
        assert L>log_rational(F(5)).hi and L<=F(16,5)
        assert log_rational(F(4)).hi<2*a<log_rational(F(5)).lo
    if a==F(81,100):
        exponential_bound=26;kernel_bound=F(81,20)
        assert log_rational(F(5)).hi<L<log_rational(F(26)).lo
        assert L<=F(81,25)
        assert log_rational(F(5)).hi<2*a<log_rational(F(7)).lo
    if a==F(41,50):
        exponential_bound=27;kernel_bound=F(41,10)
        assert log_rational(F(5)).hi<L<log_rational(F(27)).lo
        assert L<=F(82,25)
        assert log_rational(F(5)).hi<2*a<log_rational(F(7)).lo
    if a==F(17,20):
        exponential_bound=30;kernel_bound=F(17,4)
        assert log_rational(F(5)).hi<L<log_rational(F(30)).lo
        assert L<=F(17,5) and L<6
        assert log_rational(F(5)).hi<2*a<log_rational(F(7)).lo
    if a==F(22,25):
        exponential_bound=34;kernel_bound=F(22,5)
        assert log_rational(F(5)).hi<L<log_rational(F(34)).lo
        assert L<=F(88,25) and L<6
        assert log_rational(F(5)).hi<2*a<log_rational(F(6)).lo
    if a==F(9,10):
        exponential_bound=37;kernel_bound=F(9,2)
        assert log_rational(F(5)).hi<L<log_rational(F(37)).lo
        assert L<=F(18,5) and L<6
        assert log_rational(F(5)).hi<2*a<log_rational(F(7)).lo
    if a==F(91,100):
        exponential_bound=39;kernel_bound=F(91,20)
        assert log_rational(F(5)).hi<L<log_rational(F(39)).lo
        assert L<=F(91,25) and L<6
        assert log_rational(F(5)).hi<2*a<log_rational(F(7)).lo
    if a==F(23,25):
        exponential_bound=40;kernel_bound=F(23,5)
        assert log_rational(F(5)).hi<L<log_rational(F(40)).lo
        assert L<=F(92,25) and L<6
        assert log_rational(F(5)).hi<2*a<log_rational(F(7)).lo
    if a==F(93,100):
        exponential_bound=42;kernel_bound=F(93,20)
        assert log_rational(F(5)).hi<L<log_rational(F(42)).lo
        assert L<=F(93,25) and L<6
        assert log_rational(F(5)).hi<2*a<log_rational(F(7)).lo
    if a==F(47,50):
        exponential_bound=43;kernel_bound=F(47,10)
        assert log_rational(F(5)).hi<L<log_rational(F(43)).lo
        assert L<=F(94,25) and L<6
        assert log_rational(F(5)).hi<2*a<log_rational(F(7)).lo
    if a==F(19,20):
        exponential_bound=45;kernel_bound=F(19,4)
        assert log_rational(F(5)).hi<L<log_rational(F(45)).lo
        assert L<=F(19,5) and L<6
        assert log_rational(F(5)).hi<2*a<log_rational(F(7)).lo
    if a==F(24,25):
        exponential_bound=47;kernel_bound=F(24,5)
        assert log_rational(F(5)).hi<L<log_rational(F(47)).lo
        assert L<=F(96,25) and L<6
        assert log_rational(F(5)).hi<2*a<log_rational(F(7)).lo
    if a in (F(51,100), F(27,50)):
        # exp(L)<9 and L/(1-exp(-L))<3 retain the audited error constants.
        assert L < log_rational(F(9)).lo
        assert L > log_rational(F(4)).hi
        assert L < F(9,4)
        assert log_rational(F(2)).hi < 2*a < log_rational(F(3)).lo
    assert log_rational(F(2)).lo > F(1,2)
    polys = legendre(degree)
    B = bernoulli(2*K+2)
    pi = 16*atan(F(1,5))-4*atan(F(1,239))
    # Euler--Maclaurin for gamma: alternating, next-term bounded remainder.
    if a==F(21,20):
        exponential_bound=67;kernel_bound=F(21,4)
        assert log_rational(F(5)).hi<L<log_rational(F(67)).lo
        assert L<=F(21,5) and L<6
        assert log_rational(F(8)).hi<2*a<log_rational(F(9)).lo
        assert log_rational(F(50)).hi<L
        assert 2*log_rational(F(7)).hi<L
    n, order = 100, 20 if degree==111 else (12 if degree in (19,35,47,51) else 6)
    gamma = I(sum((F(1,k) for k in range(1,n+1)),F(0))-F(1,2*n))
    gamma = gamma-log_rational(F(n))
    gamma = gamma+sum((B[2*k]/F(2*k*n**(2*k)) for k in range(1,order+1)),F(0))
    ge = abs(B[2*order+2])/F((2*order+2)*n**(2*order+2))
    gamma = gamma+I(-ge,ge)
    e1 = sum(((-L)**k/factorial(k) for k in range(N+1)),F(0))
    ee = exponential_bound*L**(N+1)/factorial(N+1)
    constant = -gamma-log_interval(pi)-log_interval(I(1-e1-ee,1-e1+ee))
    kernel = [F(0)]*(2*K+1)
    kernel[0], kernel[1] = F(1), L/2
    for k in range(1,K+1):
        kernel[2*k] = B[2*k]*L**(2*k)/factorial(2*k)
    kernel_error = 4*(L/6)**(2*K+2)/(1-(L/6)**2)
    if degree==111:
        from certify_native_exact_kernel_integral import make_archimedean_integrator
    exp1 = [(-L)**k/factorial(k) for k in range(N+1)]
    expquarter = [(-L/4)**k/factorial(k) for k in range(N+1)]
    if degree==111:
        arch_integral=make_archimedean_integrator(kernel,expquarter,2*degree+2)
    logtwo = log_rational(F(2))
    assert logtwo.hi < 1 and log_rational(F(3)).lo > 1
    prime_coefficient = 2*logtwo/sqrt_rational(F(2))
    moments = []
    for p in polys:
        ep = [(a/2)**k/factorial(k) for k in range(N+1)]
        product = mul(p,ep)
        v = a*sum((2*c/F(k+1) for k,c in enumerate(product) if k%2 == 0),F(0))
        err = 4*a*sum(map(abs,p))*(a/2)**(N+1)/factorial(N+1)
        moments.append(I(v-err,v+err))
    matrix = [[I(0) for _ in polys] for _ in polys]
    start=0
    if matrix_resume is not None:
        start,matrix=matrix_resume
        assert type(start) is int and 0<=start<=112
        assert len(matrix)==112 and all(len(row)==112 for row in matrix)
        for i in range(112):
            for j in range(112):
                x=matrix[i][j];y=matrix[j][i]
                assert isinstance(x,I) and x.lo<=x.hi and (x.lo,x.hi)==(y.lo,y.hi)
                if (i+j)%2 or min(i,j)>=start:assert x.lo==x.hi==0
    for i in range(start,len(polys)):
        p=polys[i]
        for j in range(i,len(polys)):
            if (i+j)%2:
                continue
            if degree in (19,35,47,51,111):
                # Reflection makes the two correlations equal for even i+j.
                c=[a*x*2**k for k,x in enumerate(correlation(p,polys[j]))]
            else:
                c = [a*(x+y)/2*2**k for k,(x,y) in
                     enumerate(zip(correlation(p,polys[j]),correlation(polys[j],p)))]
            delta = F(2*a,2*i+1) if i == j else F(0)
            assert c[0] == delta
            if degree==111:
                integral=arch_integral(c,delta)
            else:
                numerator = add([delta*x for x in exp1],[-x for x in mul(expquarter,c)])
                assert numerator[0] == 0
                integrand = mul(numerator[1:],kernel)
                integral = sum((x/F(k+1) for k,x in enumerate(integrand)),F(0))
            csum = sum(map(abs,c))
            exp_error = exponential_bound*L**(N+1)/factorial(N+1)*(delta+csum/F(4**(N+1)))
            abound = F(3,4)*L*delta+sum(map(abs,c[1:]))
            err = kernel_bound*exp_error+abound*kernel_error
            arch = delta*constant+I(integral-err,integral+err)
            pole = (int((-1)**i)+int((-1)**j))*moments[i]*moments[j]
            prime = I(0)
            if a in (F(1,2), F(51,100), F(27,50)):
                # c is the polynomial in y=t/L; shift t/2=log 2 means y=log 2/(2a).
                y = logtwo/I(2*a)
                value = I(0)
                for coefficient in reversed(c):
                    value = value*y+coefficient
                prime = prime_coefficient*value
            if a in (F(11,20), F(14,25), F(3,5),F(16,25),F(69,100)):
                for prime_power in (2,3):
                    ell=log_rational(F(prime_power))
                    y=ell/I(2*a)
                    value=I(0)
                    for coefficient in reversed(c):
                        value=value*y+coefficient
                    prime+=2*ell/sqrt_rational(F(prime_power))*value
            if a in (F(7,10),F(3,4),F(4,5),F(81,100),F(41,50),F(17,20),F(22,25),F(9,10),F(91,100),F(23,25),F(93,100),F(47,50),F(19,20),F(24,25),F(21,20)):
                for prime_power,lambda_n in ((2,logtwo),(3,log_rational(F(3))),(4,logtwo)):
                    ell=log_rational(F(prime_power));y=ell/I(2*a);value=I(0)
                    for coefficient in reversed(c):value=value*y+coefficient
                    prime+=2*lambda_n/sqrt_rational(F(prime_power))*value
                if a in (F(81,100),F(41,50),F(17,20),F(22,25),F(9,10),F(91,100),F(23,25),F(93,100),F(47,50),F(19,20),F(24,25),F(21,20)):
                    ell=log_rational(F(5));y=ell/I(2*a);value=I(0)
                    for coefficient in reversed(c):value=value*y+coefficient
                    prime+=2*ell/sqrt_rational(F(5))*value
            if a==F(21,20):
                ell=log_rational(F(7));y=ell/I(2*a);value=I(0)
                for coefficient in reversed(c):value=value*y+coefficient
                prime+=2*ell/sqrt_rational(F(7))*value
                ell=log_rational(F(8));y=ell/I(2*a);value=I(0)
                for coefficient in reversed(c):value=value*y+coefficient
                prime+=2*logtwo/sqrt_rational(F(8))*value
            matrix[i][j] = matrix[j][i] = arch+pole-prime
        if matrix_observer is not None:matrix_observer(i+1,matrix)
    width_bound = F(9,10**30) if a == F(1,4) else F(2,10**29)
    assert max(x.hi-x.lo for row in matrix for x in row) < width_bound
    if return_matrix:
        return matrix
    pivots = positive_pivots(matrix)
    broken = [row[:] for row in matrix]
    broken[0][0] = I(-1)
    try:
        positive_pivots(broken)
    except ArithmeticError:
        pass
    else:
        raise AssertionError('Negative control was incorrectly certified')
    result = dict(status='certified strictly positive finite restriction only',a=str(a),degree=degree,
                basis='P_n(x/a) on [-a,a], unnormalized physical basis',
                arithmetic='Fraction; outward 10^-50 grid; rational interval Schur elimination',
                exponential_order=N,bernoulli_pairs=K,
                pivot_lower_bounds=[str(x.lo) for x in pivots],
                pivot_lower_display=[float(x.lo) for x in pivots],
                largest_entry_width_display=float(max(x.hi-x.lo for row in matrix for x in row)),
                negative_control_rejected=True,whole_domain_positivity=False)
    if a == F(1,2):
        tau = F(1,200000)
        shifted = [row[:] for row in matrix]
        for i in range(degree+1):
            shifted[i][i] = shifted[i][i]-tau*F(2*a,2*i+1)
        shifted_pivots = positive_pivots(shifted)
        result.update(physical_coercivity_lower_bound=str(tau),
                      shifted_pivot_lower_bounds=[str(x.lo) for x in shifted_pivots],
                      shifted_pivot_lower_display=[float(x.lo) for x in shifted_pivots],
                      prime_terms=[2])
    return result


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--half',action='store_true',help='Certify a=1/2 including the prime 2')
    args = parser.parse_args()
    print(json.dumps(certificate(F(1,2) if args.half else F(1,4)),indent=2))


