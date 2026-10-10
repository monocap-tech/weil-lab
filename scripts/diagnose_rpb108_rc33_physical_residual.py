"""NONCERTIFIED physical source-residual quadrature of RC31's actual trials."""
import json, sys
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.special import sici
from numpy.polynomial.legendre import legvander, leggauss

B=1.1
c=-np.euler_gamma-np.log(2*np.pi*(2*B))
H=np.array([sum(1/k for k in range(1,j+1)) for j in range(8)])

def kernel(r):
    assert np.all(r>0)
    a=2*np.pi*r; z=np.e*a
    si,ci=sici(z)
    # Stable subtraction of the 1/(2r) density; still floating, not interval.
    return 2/a*(np.pi*np.sin(z/2)**2-np.sin(z)*ci+np.cos(z)*si)

def run(path,order):
    data=json.loads(Path(path).read_text())
    V=np.array([[float(Fraction(v)) for v in row] for row in data['coefficients']])
    order=int(order)
    q,w=leggauss(order); ys=(q+1)/2; ws=w/2
    def p(x): return legvander(x/B,7)[0]
    def source(x):
        px=p(x); v=px@V
        W=np.log(2)-.5*np.log1p(-(x/B)**2)
        def piece(sign,length):
            rs=length*ys*ys
            return (ws*(2*length*ys)*kernel(rs))@(legvander((x+sign*rs)/B,7)@V)
        Kv=piece(-1,x+B)+piece(1,B-x)
        return ((px*H)@V)+(W+c)*v+Kv
    # Integrate half interval, then enforce exact source parity for the other half.
    def gram_integrand(x):
        res=p(x)-source(x)
        return np.outer(res,res)
    A=sum((2*B*y*wt*gram_integrand(B*(1-y*y)) for y,wt in zip(ys,ws)),np.zeros((8,8)))
    A*=2
    for i in range(8):
        for j in range(8):
            if (i+j)%2: A[i,j]=0
    d=np.array([2*B/(2*j+1) for j in range(8)])
    normgram=A/np.sqrt(np.outer(d,d))
    return dict(milestone='RC33',evidence='NONCERTIFIED floating quadrature reconnaissance',
        quadrature_order=order,physical_residual_Gram=A.tolist(),
        physical_residual_norms=np.sqrt(np.diag(A)).tolist(),
        collective_physical_squared_estimate=float(np.linalg.eigvalsh(normgram)[-1]),
        endpoint_values_plus=(np.ones(8)@V).tolist(),
        source_scalar=c,whole_residual_certified=False,native_head_certified=False,
        aperture_extended=False)

if __name__=='__main__':
    print(json.dumps(run(sys.argv[1],int(sys.argv[2]) if len(sys.argv)>2 else 256),indent=2))
