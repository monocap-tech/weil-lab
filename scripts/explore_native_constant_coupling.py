"""Exploratory actual constant-source residual; quadrature is NOT certified."""
import json
from math import log, pi, sinh
import numpy as np
from scipy.special import eval_legendre
from numpy.polynomial.legendre import leggauss


def pilot(count):
    nodes, weights = leggauss(count)
    b = log(2)-.5
    panels = [(-.5,-b),(-b,b),(b,.5)]
    x = np.concatenate([lo+(nodes+1)*(hi-lo)/2 for lo,hi in panels])
    w = np.concatenate([weights*(hi-lo)/2 for lo,hi in panels])

    def J(d):
        z = np.exp(-d/2)
        return .5*np.log1p(2*z/(-np.expm1(-d/2)))+np.arctan(z)

    q = (-np.euler_gamma-pi/2-3*log(2)-log(pi)+J(x+.5)+J(.5-x)
         +8*sinh(.25)*np.cosh(x/2))
    q -= log(2)/np.sqrt(2)*((x>=b).astype(float)+(x<=-b).astype(float))
    coeff = np.array([sum(w*q*np.sqrt(2*n+1)*eval_legendre(n,2*x)) for n in range(64)])
    norm = sum(w*q*q)
    residual2 = norm-sum(coeff*coeff)
    return dict(nodes_per_panel=count,Q00_display=float(coeff[0]),
                residual_squared_display=float(residual2),
                coupling_majorant_display=float(5*residual2),certified_sign=False)


if __name__ == '__main__':
    print(json.dumps(dict(status='uncertified constant-source residual pilot only',
                         results=[pilot(512),pilot(1024)]),indent=2))
