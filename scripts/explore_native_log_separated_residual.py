"""Exact log part plus exploratory regularized mixed/source quadrature."""
import json
from math import log,pi,comb
import numpy as np
from numpy.polynomial.legendre import leggauss,legvander
from scipy.special import eval_legendre,spherical_in
from certify_native_endpoint_log_gram import exact_log_data
from explore_native_legendre_physical import physical_matrix


def log_integral(k,a,b):
    def primitive(t):
        return 0. if t==0 else t**(k+1)*(log(t)/(k+1)-1/(k+1)**2)
    return primitive(b)-primitive(a)


def L_moment(k,a,b):
    return -.5*(log_integral(k,a,b)+sum(comb(k,j)*(-1)**j*
               log_integral(j,1-b,1-a) for j in range(k+1)))


def smooth_source(x,center,inner_nodes):
    orders=np.arange(8)
    basis=legvander(2*x,7)*np.sqrt(2*orders+1)
    def H(d):
        z=np.exp(-d/2)
        out=np.full(d.shape,log(2)+pi/4)
        active=d>0
        out[active]=.5*np.log(d[active]*(1+z[active])/(-np.expm1(-d[active]/2)))+np.arctan(z[active])
        return out
    coefficient=-np.euler_gamma-pi/2-3*log(2)-log(pi)+H(x+.5)+H(.5-x)
    q=coefficient[:,None]*basis
    plus=np.sqrt(2*orders+1)*spherical_in(orders,.25)
    q+=np.exp(x[:,None]/2)*(plus*(-1.)**orders)+np.exp(-x[:,None]/2)*plus
    for shift in (-log(2),log(2)):
        if abs(center+shift)<.5:
            q-=log(2)/np.sqrt(2)*legvander(2*(x+shift),7)*np.sqrt(2*orders+1)
    uu,vv=leggauss(inner_nodes)
    for sign,distance in [(-1,x+.5),(1,.5-x)]:
        active=distance>0
        xa=x[active]
        s=distance[active,None]*(uu+1)/2
        weights=vv*distance[active,None]/2*np.exp(-s/2)/(-np.expm1(-2*s))
        for n in orders:
            difference=eval_legendre(n,2*(xa[:,None]+sign*s))*np.sqrt(2*n+1)-basis[active,n,None]
            q[active,n]-=np.sum(weights*difference,axis=1)
    return q


def pilot(nodes,inner_nodes=64):
    p,log_coeff,log_gram=exact_log_data()
    CL=np.array([[float(c)*np.sqrt((2*n+1)*(2*i+1)) for i,c in enumerate(row)]
                 for n,row in enumerate(log_coeff)])
    RL=np.array([[float((x.lo+x.hi)/2) for x in row] for row in log_gram])
    xx,ww=leggauss(nodes)
    b=log(2)-.5
    allx,allw,allsmooth=[],[],[]
    cross=np.zeros((8,8))
    for lo,hi in [(-.5,-b),(-b,b),(b,.5)]:
        x=lo+(xx+1)*(hi-lo)/2
        w=ww*(hi-lo)/2
        smooth=smooth_source(x,(lo+hi)/2,inner_nodes)
        ends=smooth_source(np.array([lo,hi]),(lo+hi)/2,inner_nodes)
        ell=ends[0]+((x-lo)/(hi-lo))[:,None]*(ends[1]-ends[0])
        L=-.5*(np.log(x+.5)+np.log(.5-x))
        low=legvander(2*x,7)*np.sqrt(2*np.arange(8)+1)
        cross+=low.T@((w*L)[:,None]*(smooth-ell))
        tlo,thi=lo+.5,hi+.5
        for i in range(8):
            m0=sum(float(c)*L_moment(k,tlo,thi) for k,c in enumerate(p[i]))*np.sqrt(2*i+1)
            m1=sum(float(c)*L_moment(k+1,tlo,thi) for k,c in enumerate(p[i]))*np.sqrt(2*i+1)
            slope=(ends[1]-ends[0])/(hi-lo)
            cross[i]+=m0*(ends[0]-slope*tlo)+m1*slope
        allx.append(x);allw.append(w);allsmooth.append(smooth)
    x=np.concatenate(allx);w=np.concatenate(allw);smooth=np.concatenate(allsmooth)
    basis=legvander(2*x,63)*np.sqrt(2*np.arange(64)+1)
    CS=basis.T@(w[:,None]*smooth)
    residual=smooth-basis@CS
    RS=residual.T@(w[:,None]*residual)
    mixed=cross-CL.T@CS
    R=RL+RS+mixed+mixed.T
    raw=physical_matrix(.5)
    lower=raw-5*R
    return dict(nodes_per_panel=nodes,inner_nodes=inner_nodes,
                source_pairing_error=float(np.max(np.abs((CL+CS)[:8]-raw))),
                residual_gram=R.tolist(),
                residual_gram_minimum_display=float(np.linalg.eigvalsh(R)[0]),
                no_lift_lower_pilot_eigenvalues=np.linalg.eigvalsh(lower).tolist(),
                exact_endpoint_log_gram_used=True,full_source_gram_certified=False,
                actual_schur_sign_certified=False)


if __name__=='__main__':
    results=[pilot(128),pilot(256)]
    difference=np.array(results[1]['residual_gram'])-np.array(results[0]['residual_gram'])
    print(json.dumps(dict(status='exact endpoint-log component; mixed quadrature uncertified',
                         gram_repeat_norm_display=float(np.linalg.norm(difference,2)),results=results),indent=2))
