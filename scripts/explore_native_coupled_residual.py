"""Actual eight-source residual pilot; all quadrature signs are uncertified."""
import json
from math import log, pi
import numpy as np
from numpy.polynomial.legendre import leggauss, legvander
from scipy.special import eval_legendre, spherical_in
from explore_native_legendre_physical import physical_matrix


def pilot(nodes, inner_nodes=64):
    xx, ww = leggauss(nodes)
    b = log(2)-.5
    panels = [(-.5,-b),(-b,b),(b,.5)]
    x = np.concatenate([lo+(xx+1)*(hi-lo)/2 for lo,hi in panels])
    w = np.concatenate([ww*(hi-lo)/2 for lo,hi in panels])
    basis = legvander(2*x,63)*np.sqrt(2*np.arange(64)+1)
    orders = np.arange(8)
    plus = np.sqrt(2*orders+1)*spherical_in(orders,.25)
    minus = plus*(-1.)**orders
    def J(d):
        z = np.exp(-d/2)
        return .5*np.log1p(2*z/(-np.expm1(-d/2)))+np.arctan(z)
    coefficient = -np.euler_gamma-pi/2-3*log(2)-log(pi)+J(x+.5)+J(.5-x)
    q = coefficient[:,None]*basis[:,:8]
    q += np.exp(x[:,None]/2)*minus+np.exp(-x[:,None]/2)*plus
    for shift in (-log(2),log(2)):
        y = x+shift
        active = np.abs(y)<=.5
        for n in orders:
            q[:,n] -= log(2)/np.sqrt(2)*active*eval_legendre(n,2*np.clip(y,-.5,.5))*np.sqrt(2*n+1)
    uu, vv = leggauss(inner_nodes)
    for sign, distance in [(-1,x+.5),(1,.5-x)]:
        s = distance[:,None]*(uu+1)/2
        kernel_weights = vv*distance[:,None]/2*np.exp(-s/2)/(-np.expm1(-2*s))
        for n in orders:
            shifted = eval_legendre(n,2*(x[:,None]+sign*s))*np.sqrt(2*n+1)
            q[:,n] -= np.sum(kernel_weights*(shifted-basis[:,n,None]),axis=1)
    projections = basis.T@(w[:,None]*q)
    residual = q-basis@projections
    gram = residual.T@(w[:,None]*residual)
    raw = physical_matrix(.5)
    lower = raw-5*gram
    result = dict(nodes_per_panel=nodes,inner_nodes=inner_nodes,
                  source_pairing_error=float(np.max(np.abs(projections[:8]-raw))),
                  residual_gram=gram.tolist(),
                  no_lift_lower_pilot_eigenvalues=np.linalg.eigvalsh(lower).tolist(),
                  raw_minimum_display=float(np.linalg.eigvalsh(raw)[0]),
                  certified_sign=False,actual_schur_sign_certified=False)
    for parity,name in [(0,'even'),(1,'odd')]:
        indices=list(range(parity,8,2))
        block=lower[np.ix_(indices,indices)]
        values,vectors=np.linalg.eigh(block)
        result[name+'_lower_minimum_display']=float(values[0])
        result[name+'_weak_direction_coefficients']=vectors[:,0].tolist()
    return result


if __name__ == '__main__':
    print(json.dumps(dict(status='uncertified coupled no-lift residual diagnostic',
                         results=[pilot(512),pilot(1024)]),indent=2))
