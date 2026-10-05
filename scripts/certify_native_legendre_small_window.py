"""Exact rational enclosure of the actual a=1/4, degree-seven restriction.

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
    def __init__(self, lo, hi=None):
        lo, hi = F(lo), F(lo if hi is None else hi)
        assert lo <= hi
        grid = 10**50
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


def certificate():
    a, degree, N, K = F(1,4), 7, 60, 24
    assert log_rational(F(2)).lo > F(1,2)
    polys = legendre(degree)
    B = bernoulli(2*K+2)
    pi = 16*atan(F(1,5))-4*atan(F(1,239))
    # Euler--Maclaurin for gamma: alternating, next-term bounded remainder.
    n, order = 100, 6
    gamma = I(sum((F(1,k) for k in range(1,n+1)),F(0))-F(1,2*n))
    gamma = gamma-log_rational(F(n))
    gamma = gamma+sum((B[2*k]/F(2*k*n**(2*k)) for k in range(1,order+1)),F(0))
    ge = abs(B[2*order+2])/F((2*order+2)*n**(2*order+2))
    gamma = gamma+I(-ge,ge)
    e1 = sum((F((-1)**k,factorial(k)) for k in range(N+1)),F(0))
    ee = F(3,factorial(N+1))
    constant = -gamma-log_interval(pi)-log_interval(I(1-e1-ee,1-e1+ee))
    kernel = [F(0)]*(2*K+1)
    kernel[0], kernel[1] = F(1), F(1,2)
    for k in range(1,K+1):
        kernel[2*k] = B[2*k]/factorial(2*k)
    kernel_error = F(4,6**(2*K+2))/F(35,36)
    exp1 = [F((-1)**k,factorial(k)) for k in range(N+1)]
    expquarter = [F((-1)**k,4**k*factorial(k)) for k in range(N+1)]
    moments = []
    for p in polys:
        ep = [F(1,8**k*factorial(k)) for k in range(N+1)]
        product = mul(p,ep)
        v = a*sum((2*c/F(k+1) for k,c in enumerate(product) if k%2 == 0),F(0))
        err = 4*a*sum(map(abs,p))*F(1,8**(N+1)*factorial(N+1))
        moments.append(I(v-err,v+err))
    matrix = [[I(0) for _ in polys] for _ in polys]
    for i,p in enumerate(polys):
        for j in range(i,len(polys)):
            if (i+j)%2:
                continue
            c = [a*(x+y)/2*2**k for k,(x,y) in
                 enumerate(zip(correlation(p,polys[j]),correlation(polys[j],p)))]
            delta = F(2*a,2*i+1) if i == j else F(0)
            assert c[0] == delta
            numerator = add([delta*x for x in exp1],[-x for x in mul(expquarter,c)])
            assert numerator[0] == 0
            integrand = mul(numerator[1:],kernel)
            integral = sum((x/F(k+1) for k,x in enumerate(integrand)),F(0))
            csum = sum(map(abs,c))
            exp_error = F(3,factorial(N+1))*(delta+csum/F(4**(N+1)))
            abound = F(3,4)*delta+sum(map(abs,c[1:]))
            err = 2*exp_error+abound*kernel_error
            arch = delta*constant+I(integral-err,integral+err)
            pole = (int((-1)**i)+int((-1)**j))*moments[i]*moments[j]
            matrix[i][j] = matrix[j][i] = arch+pole
    assert max(x.hi-x.lo for row in matrix for x in row) < F(9,10**30)
    pivots = positive_pivots(matrix)
    broken = [row[:] for row in matrix]
    broken[0][0] = I(-1)
    try:
        positive_pivots(broken)
    except ArithmeticError:
        pass
    else:
        raise AssertionError('Negative control was incorrectly certified')
    return dict(status='certified strictly positive finite restriction only',a='1/4',degree=degree,
                basis='P_n(x/a) on [-a,a], unnormalized physical basis',
                arithmetic='Fraction; outward 10^-50 grid; rational interval Schur elimination',
                exponential_order=N,bernoulli_pairs=K,
                pivot_lower_bounds=[str(x.lo) for x in pivots],
                pivot_lower_display=[float(x.lo) for x in pivots],
                largest_entry_width_display=float(max(x.hi-x.lo for row in matrix for x in row)),
                negative_control_rejected=True,whole_domain_positivity=False)


if __name__ == '__main__':
    print(json.dumps(certificate(),indent=2))
