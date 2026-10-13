"""Tail-free physical formula pilot; floating integration is NOT certified."""
from fractions import Fraction as F
from math import comb, log, sqrt
import json
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import spherical_in
from explore_native_legendre_matrix import matrix as fourier_matrix, prime_terms


def legendre_coefficients(degree):
    out = [[F(1)]]
    if degree:
        out.append([F(0), F(1)])
    for n in range(1, degree):
        row = [F(0)]*(n+2)
        for k, c in enumerate(out[n]):
            row[k+1] += F(2*n+1, n+1)*c
        for k, c in enumerate(out[n-1]):
            row[k] -= F(n, n+1)*c
        out.append(row)
    return out


def raw_correlation(pi, pj):
    # Integral from u-1 to 1 of Pi(r) Pj(r-u) dr, exactly in Q[u].
    row = [F(0)]*(len(pi)+len(pj))
    for p, cp in enumerate(pi):
        for q, cq in enumerate(pj):
            for k in range(q+1):
                c = cp*cq*comb(q,k)*(-1)**k/F(p+q-k+1)
                d = p+q-k+1
                row[k] += c
                for ell in range(d+1):
                    row[k+ell] -= c*comb(d,ell)*(-1)**(d-ell)
    return row


def bernstein_on_0_2(power):
    degree = len(power)-1
    return np.array([float(sum(power[k]*2**k*F(comb(i,k),comb(degree,k))
                              for k in range(i+1)))
                     for i in range(degree+1)])


def evaluate_bernstein(coefficients, u):
    u = np.asarray(u)
    work = np.repeat(coefficients[:,None], u.size, axis=1)
    t = u.ravel()/2
    for count in range(len(coefficients)-1, 0, -1):
        work[:count] = (1-t)*work[:count]+t*work[1:count+1]
    return work[0].reshape(u.shape)


def physical_matrix(a, degree=7, nodes=128):
    if a <= 0 or degree < 0 or nodes < 1:
        raise ValueError("Require a>0, degree>=0, and nodes>=1")
    polys = legendre_coefficients(degree)
    xx, ww = leggauss(nodes)
    t = (xx+1)*2*a
    weights = ww*2*a
    u = t/(2*a)
    q = np.zeros((degree+1,degree+1))
    arch_constant = -float(np.euler_gamma)-log(np.pi)-log(-np.expm1(-4*a))
    for i in range(degree+1):
        for j in range(i, degree+1):
            c1 = raw_correlation(polys[i],polys[j])
            c2 = raw_correlation(polys[j],polys[i])
            raw = [(x+y)/2 for x,y in zip(c1,c2)]
            scale = sqrt((2*i+1)*(2*j+1))/2
            delta = int(i == j)
            expected = F(2,2*i+1) if delta else F(0)
            if raw[0] != expected:
                raise ArithmeticError("Exact correlation normalization failed")
            if (i+j)%2:
                if any(raw):
                    raise ArithmeticError("Exact parity failed")
                continue
            tail_bernstein = bernstein_on_0_2(raw[1:])
            # C(t/2)-delta is evaluated without subtracting near-equal floats.
            correlation_minus_delta = scale*u*evaluate_bernstein(tail_bernstein,u)
            integrand = np.exp(-t/4)*(np.expm1(-3*t/4)*delta-
                         correlation_minus_delta)/(-np.expm1(-t))
            entry = arch_constant*delta+float(weights @ integrand)
            whole_bernstein = bernstein_on_0_2(raw)
            for n, coefficient in prime_terms(a):
                shift = np.array([log(n)/a])
                entry -= coefficient*scale*float(evaluate_bernstein(whole_bernstein,shift)[0])
            q[i,j] = q[j,i] = entry
    order = np.arange(degree+1)
    plus = np.sqrt(2*a*(2*order+1))*spherical_in(order,a/2)
    minus = plus*(-1.)**order
    q += np.outer(minus,plus)+np.outer(plus,minus)
    return q


def main():
    results = []
    for a in (.25,.5,.75,1.):
        q64 = physical_matrix(a,nodes=64)
        q128 = physical_matrix(a,nodes=128)
        truncated, _, _ = fourier_matrix(a,nodes=64)
        difference = q128-truncated
        results.append(dict(a=a,degree=7,physical_nodes=128,
            physical_pilot_eigenvalues=np.linalg.eigvalsh(q128).tolist(),
            repeat_difference=float(np.linalg.norm(q128-q64,2)),
            physical_minus_truncated_norm=float(np.linalg.norm(difference,2)),
            physical_minus_truncated_min_eigenvalue=float(np.linalg.eigvalsh(difference)[0]),
            certified_sign=False))
    print(json.dumps(dict(status="tail-free identity; numerical integration remains exploratory",
                         results=results),indent=2))


if __name__ == "__main__":
    main()
