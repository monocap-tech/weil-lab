"""Exact rational native restrictions at audited apertures through a=14/25.

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


class I:
    grid = 10**50
    def __init__(self, lo, hi=None):
        lo, hi = F(lo), F(lo if hi is None else hi)
        assert lo <= hi
        grid = self.grid
        self.lo = F((lo*grid).__floor__(),grid)
        self.hi = F((hi*grid).__ceil__(),grid)

    def __add__(self, other):
        other = other if isinstance(other, I) else I(other)
        return I(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -(other if isinstance(other, I) else I(other))

    def __mul__(self, other):
        other = other if isinstance(other, I) else I(other)
        ends = [x*y for x in (self.lo,self.hi) for y in (other.lo,other.hi)]
        return I(min(ends),max(ends))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = other if isinstance(other, I) else I(other)
        assert other.lo > 0 or other.hi < 0
        return self*I(1/other.hi,1/other.lo)


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


def certificate(a=F(1,4), return_matrix=False, degree=7):
    if a not in (F(1,4), F(1,2), F(51,100), F(27,50), F(11,20), F(14,25)):
        raise ValueError('Unsupported audited aperture')
    if degree not in (7,19,35,47) or (degree==19 and (a not in (F(1,2), F(51,100), F(27,50), F(11,20)) or not return_matrix)):
        raise ValueError('Degree 19 requires a supported matrix constructor')
    if degree==35 and (a not in (F(11,20), F(14,25)) or not return_matrix):
        raise ValueError('Degree 35 requires the prime-3 aperture matrix constructor')
    if degree==47 and (a!=F(14,25) or not return_matrix):
        raise ValueError("Degree 47 requires the aperture 14/25 matrix constructor")
    if a in (F(51,100), F(27,50), F(11,20), F(14,25)) and (degree not in (19,35,47) or not return_matrix):
        raise ValueError('The larger aperture requires a supported matrix constructor')
    N,K=(160,120) if degree==47 else ((120,100) if degree==35 else ((80,60) if degree==19 else (60,24 if a==F(1,4) else 40)))
    L = 4*a
    exponential_bound = 3 if L == 1 else 9
    kernel_bound = 2 if L == 1 else 3
    if a in (F(11,20), F(14,25)):
        exponential_bound = 10
        assert L < log_rational(F(10)).lo
        assert L > log_rational(F(4)).hi and L < F(9,4)
        assert log_rational(F(3)).hi < 2*a < log_rational(F(4)).lo
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
    n, order = 100, 12 if degree in (19,35,47) else 6
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
    exp1 = [(-L)**k/factorial(k) for k in range(N+1)]
    expquarter = [(-L/4)**k/factorial(k) for k in range(N+1)]
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
    for i,p in enumerate(polys):
        for j in range(i,len(polys)):
            if (i+j)%2:
                continue
            if degree in (19,35,47):
                # Reflection makes the two correlations equal for even i+j.
                c=[a*x*2**k for k,x in enumerate(correlation(p,polys[j]))]
            else:
                c = [a*(x+y)/2*2**k for k,(x,y) in
                     enumerate(zip(correlation(p,polys[j]),correlation(polys[j],p)))]
            delta = F(2*a,2*i+1) if i == j else F(0)
            assert c[0] == delta
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
            if a in (F(11,20), F(14,25)):
                for prime_power in (2,3):
                    ell=log_rational(F(prime_power))
                    y=ell/I(2*a)
                    value=I(0)
                    for coefficient in reversed(c):
                        value=value*y+coefficient
                    prime+=2*ell/sqrt_rational(F(prime_power))*value
            matrix[i][j] = matrix[j][i] = arch+pole-prime
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
