"""V10B18 numerical-only pilot. Requires numpy/scipy.
Reconstructs the 96-mode finite Fourier Galerkin seed, then minimizes the
full-support real-space residual at fixed constraint loads. No interval
enclosure, formal digamma-action attachment or exact load rank is claimed.
"""
import numpy as np
from scipy.special import digamma, eval_legendre, spherical_in, spherical_jn
from scipy.linalg import cholesky, solve_triangular, null_space, eigvalsh
from numpy.polynomial.legendre import leggauss, legvander
import json

t=.25
L=2*t
def load_values(y):
    jj=np.arange(15,34,2)
    coeff=(2*jj+1)*spherical_in(jj,t/2)/(31*spherical_in(15,t/2))
    return np.column_stack((np.stack([np.sqrt(2*j+1)*eval_legendre(j,y) for j in range(15)],axis=1),
        np.sqrt(31)*sum(c*eval_legendre(j,y) for j,c in zip(jj,coeff))))

def seed(n=96,U=2048,order=12):
    k=np.arange(n); x,g=leggauss(max(256,2*n)); scale=np.sqrt((2*k+1)/L)
    phi=np.array([eval_legendre(j,x) for j in k]).T*scale
    H=phi.T@(t*g[:,None]*load_values(x))
    ep=phi.T@(t*g*np.exp(t*x/2)); em=phi.T@(t*g*np.exp(-t*x/2))
    W=np.zeros((n,n)); A=np.zeros((n,n)); q,h=leggauss(order); phase=(-1j)**k
    for left in range(0,U,32):
        edges=np.arange(left,min(left+32,U),dtype=float)
        u=(edges[:,None]+(q+1)/2).ravel(); weights=np.tile(h/2,len(edges))*2
        F=L*scale*phase*spherical_jn(k[None,:],(2*np.pi*t*u)[:,None])
        w=np.log(2+2*np.pi*u); a=digamma(.25-1j*np.pi*u).real-np.log(np.pi)
        W+=(F.conj().T@((weights*w)[:,None]*F)).real
        A+=(F.conj().T@((weights*a)[:,None]*F)).real
    A+=np.outer(ep,em)+np.outer(em,ep)
    C=cholesky(W,lower=True); Ci=solve_triangular(C,np.eye(n),lower=True)
    G=Ci@A@Ci.T; G=(G+G.T)/2
    D=Ci@H; Q,_=np.linalg.qr(D,mode='reduced'); T=null_space(Q.T)
    Z=np.linalg.solve(T.T@G@T,T.T@G@Q)
    return Ci.T@(Q-T@Z)

def optimize(seed_bank,n,order,points):
    base=np.zeros((n,16));base[:seed_bank.shape[0]]=seed_bank
    y,h=leggauss(points);x=t*y; wt=t*h; k=np.arange(n);scale=np.sqrt((2*k+1)/L)
    vals=legvander(y,n-1)*scale; q,w=leggauss(order); loads=load_values(y)
    ep=np.exp(x/2);em=np.exp(-x/2)
    av=(-np.euler_gamma-np.log(np.pi)-np.log1p(-np.exp(-2*L)))*vals+ep[:,None]@((wt*em)@vals)[None,:]+em[:,None]@((wt*ep)@vals)[None,:]
    for i,xx in enumerate(x):
        edges=sorted([0.,t-xx,xx+t,L]);v=vals[i]
        for a,z in zip(edges[:-1],edges[1:]):
            r=a+(z-a)*(q+1)/2;rw=w*(z-a)/2;shifts=np.zeros((len(r),n))
            if (a+z)/2<t-xx:shifts+=legvander((xx+r)/t,n-1)*scale
            if (a+z)/2<xx+t:shifts+=legvander((xx-r)/t,n-1)*scale
            av[i]+=(rw*2/(-np.expm1(-2*r)))@(np.exp(-2*r)[:,None]*v-np.exp(-r/2)[:,None]*shifts/2)
    H=vals.T@(wt[:,None]*loads);T=null_space(H.T);A=vals.T@(wt[:,None]*av);A=(A+A.T)/2
    Y=np.linalg.lstsq(np.sqrt(wt[:,None])*loads,np.sqrt(wt[:,None])*av,rcond=None)[0]
    r=np.sqrt(wt[:,None])*(av-loads@Y)
    z=np.linalg.lstsq(r@T,-r@base,rcond=None)[0];V=base+T@z
    R=(r@V).T@(r@V); E=V.T@A@V;E=(E+E.T)/2;lower=E-R/(.125*np.log(2))
    row=dict(n=n,order=order,points=points,energy_min=float(eigvalsh(E)[0]),
        residual_norm=float(np.sqrt(eigvalsh(R)[-1])),lower_min=float(eigvalsh(lower)[0]),
        load_change=float(np.linalg.norm(H.T@(V-base),2)))
    return row,dict(V=V,Y=Y@V,R=R,E=E,lower=lower,H=H)

if __name__=='__main__':
    base=seed()
    rows=[]
    for n,o,p in [(96,128,1024),(128,160,1024),(160,192,1536)]:
        row,b=optimize(base,n,o,p); rows.append(row);print(json.dumps(row),flush=True)
    with open('optimized_diagnostic.json','w') as f:json.dump(rows,f,indent=2)
    np.savez_compressed('optimized_bank.npz',**b)
