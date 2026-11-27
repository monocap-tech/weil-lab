"""IV252: finite original-form Galerkin diagnostic. Binary64 only; not a certificate."""
import os
os.environ['OPENBLAS_NUM_THREADS']='4'
os.environ['OMP_NUM_THREADS']='4'
import numpy as np
import scipy
from scipy.special import digamma, polygamma
from scipy.linalg import lapack, solve_triangular, eigh
import json, sys, time
BANK=[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3),(11,11),(13,13),(16,2),(17,17),(19,19),(23,23),(25,5),(27,3),(29,29),(31,31),(32,2),(37,37),(41,41),(43,43),(47,47),(49,7),(53,53)]
a=np.pi/4
J=33280; M=int(sys.argv[2]) if len(sys.argv)>2 else 128; N=32768

def data(j):
    j=np.asarray(j,dtype=float); r=a*j; z=r*r; c=np.where(j==0,.5,1/np.sqrt(2))
    p=digamma(.25+1j*r/2); w=.25+1j*r/2
    # trigamma recurrence and asymptotic (diagnostic only)
    tr=np.zeros_like(w)
    for k in range(32):tr+=1/(w+k)**2
    x=1/(w+32); tr+=x+x*x/2+x**3/6-x**5/30+x**7/42-x**9/30+x**11*5/66
    S=np.empty_like(r); D=np.empty_like(r); nz=r!=0
    S[nz]=p[nz].imag/(2*r[nz]); D[nz]=p[nz].imag/(4*r[nz])+tr[nz].real/8
    S[~nz]=D[~nz]=polygamma(1,.25)/4
    sn=np.zeros_like(r); pd=np.zeros_like(r)
    for n,prime in BANK:
        s=np.log(n); b=np.log(prime)/np.sqrt(n); t=r*s
        sn+=b*np.sin(t); pd+=b*(4-s)*np.cos(t)/2
        pd[nz]-=b*np.sin(t[nz])/(2*r[nz]);pd[~nz]-=0 # diagonal constant formula already correct
    return j,z,c,p.real-np.log(np.pi),j*sn,pd,S,D

def block(row,col,par):
    j,z,c,g,d,pd,S,D=row; k,w,h,gg,e,pp,T,E=col
    same=j[:,None]==k[None,:]; den=z[:,None]-w[None,:]; den[same]=1
    # P off diagonal, A_N diagonal, combined boundary / pole exact series via digamma.
    P=2*c[:,None]*h[None,:]*a*(e[None,:]-d[:,None])/den
    ii,jj=np.where(same); P[ii,jj]=pd[ii]
    B=(z[:,None]*S[:,None]-w[None,:]*T[None,:])/den
    B[ii,jj]=D[ii]
    B*=2
    sig=1 if par==0 else -1
    # Remove n=0 unweighted contribution and replace with exact combined pole weight.
    B+=((sig*np.exp(2)-1)/2-.5)/((.25+z[:,None])*(.25+w[None,:]))
    # exact n>=1 weight correction; terms n>=10 < exp(-82) (numerical approximation only)
    for n in range(1,10):
        t=(2*n+.5)**2
        B-=sig*2*t*np.exp(-4*(2*n+.5))/((t+z[:,None])*(t+w[None,:]))
    B*=c[:,None]*h[None,:]
    Q=B-P; Q[ii,jj]+=g[ii]
    return Q

def cut(d,s):return tuple(x[s] for x in d)
def run(par):
    start=time.time(); low=np.arange(par,M,2); high=np.arange(M+par,J,2); L=data(low); H=data(high)
    A=np.empty((len(high),len(high)),order='F');
    for i in range(0,len(high),128):
        sl=slice(i,min(i+128,len(high))); A[:,sl]=block(H,cut(H,sl),par)
    print('built',par,A.shape, time.time()-start,flush=True)
    R,info=lapack.dpotrf(A,lower=1,overwrite_a=1,clean=0)
    if info!=0:return {'parity':par,'split':M,'finite_cutoff':J,'high_cholesky_info':int(info)}
    Y=block(H,L,par); X=solve_triangular(R,Y,lower=True,check_finite=False)
    Q=block(L,L,par); F=Q-X.T@X; F=(F+F.T)/2
    e=eigh(F,eigvals_only=True,check_finite=False); ec=eigh((Q+Q.T)/2,eigvals_only=True,check_finite=False)
    out={'parity':par,'split':M,'finite_cutoff':J,'low_modes':len(low),'eliminated_modes':len(high),'high_cholesky_info':int(info),'high_min_cholesky_pivot_squared':float(np.min(np.diag(R))**2),'compression_smallest_12':ec[:12].tolist(),'galerkin_schur_smallest_12':e[:12].tolist(),'galerkin_negative_count':int(np.sum(e<0)),'galerkin_abs_below_1e-10':int(np.sum(np.abs(e)<1e-10)),'galerkin_max':float(e[-1]),'schur_correction_norm':float(np.linalg.norm(X.T@X,2))}
    if par==0:
        # IV250 positive witness, same exact residue formula evaluated in float.
        r2=(a*np.arange(0,18,2))**2; z=(np.array([14134725,21022040,25010858,30424876])/1e6)**2; C=np.prod(r2[1:])/np.prod(z); b=np.array([C*np.prod(z-t)/np.prod(np.delete(r2-t,i)) for i,t in enumerate(r2)]); v=b/np.where(np.arange(9)==0,.5,1/np.sqrt(2));out['iv250_float_original']=float(v@Q[:9,:9]@v);out['iv250_float_galerkin']=float(v@F[:9,:9]@v)
    print(json.dumps(out),flush=True);return out
if __name__=='__main__':
    p=int(sys.argv[1]); result=run(p); open(f'iv252_am_parity_{p}_split_{M}.json','w').write(json.dumps(result,indent=2)+'\n')
