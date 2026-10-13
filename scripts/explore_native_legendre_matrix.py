"""Exploratory actual Weil matrices; quadrature is NOT a rigorous enclosure.

Fourier convention exp(-2*pi*i*x*xi), logarithmic form carrier, full native
prime cutoff log(n)<=2*a, and unchanged cross-pole normalization.
"""
import json
import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import digamma, spherical_in, spherical_jn


def prime_terms(a):
    terms = []
    for n in range(2, math.floor(math.exp(2*a)) + 1):
        p = next((p for p in range(2, n+1) if n % p == 0), n)
        rest = n
        while rest % p == 0:
            rest //= p
        if rest == 1 and math.log(n) <= 2*a:
            terms.append((n, 2*math.log(p)/math.sqrt(n)))
    return terms


def matrix(a, degree=7, zmax=8192.0, nodes=32):
    if a <= 0 or degree < 0 or nodes < 1:
        raise ValueError("Require a>0, degree>=0, and nodes>=1")
    if zmax < max(1, degree*(degree+1)):
        raise ValueError("Tail estimate requires zmax>=max(1,degree*(degree+1))")
    order = np.arange(degree+1)
    norm = np.sqrt(2*order+1)
    phase = np.cos(np.pi*(order[:, None]-order[None, :])/2)
    # Exact parity prevents roundoff from being mistaken for mixed parity.
    phase[(order[:, None]-order[None, :]) % 2 != 0] = 0
    raw = np.zeros((degree+1, degree+1))
    xx, ww = leggauss(nodes)
    panels = math.ceil(zmax/math.pi)
    width = zmax/panels
    terms = prime_terms(a)
    for start in range(0, panels, 128):
        centers = (np.arange(start, min(start+128, panels))+.5)*width
        z = (centers[:, None]+xx[None, :]*width/2).ravel()
        weights = np.tile(ww*width/2, len(centers))
        xi = z/(2*math.pi*a)
        symbol = digamma(.25+1j*math.pi*xi).real-math.log(math.pi)
        for n, coefficient in terms:
            symbol -= coefficient*np.cos(2*math.pi*xi*math.log(n))
        bessel = np.array([spherical_jn(int(j), z) for j in order])
        raw += (bessel*(weights*symbol)) @ bessel.T
    q = (2/math.pi)*raw*norm[:, None]*norm[None, :]*phase
    plus = np.sqrt(2*a)*norm*spherical_in(order, a/2)
    minus = plus*(-1.0)**order
    q += np.outer(minus, plus)+np.outer(plus, minus)
    t = zmax/(2*math.pi*a)
    amplitude = sum(c for _, c in terms)
    # Analytic bound for the OMITTED tail only; not for interval quadrature.
    tail_bound = 4*(degree+1)**2/(math.pi**2*a*t)*(
        math.log(math.e+t)+11+amplitude)
    return q, tail_bound, terms


def main():
    results = []
    for a in (.25, .5, .75, 1.0):
        q32, bound, terms = matrix(a)
        q64, _, _ = matrix(a, nodes=64)
        eigenvalues = np.linalg.eigvalsh(q64)
        results.append(dict(a=a, degree=7, zmax=8192, nodes=64,
            prime_powers=[n for n, _ in terms],
            eigenvalues=eigenvalues.tolist(),
            quadrature_repeat_difference=float(np.linalg.norm(q64-q32, 2)),
            analytic_tail_bound_evaluated_in_float=bound,
            certified_sign=False))
    print(json.dumps(dict(status="exploratory; no interval quadrature enclosure",
                         results=results), indent=2))


if __name__ == "__main__":
    main()
