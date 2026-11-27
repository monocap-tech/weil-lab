"""IV254: finite intermediate block certificate; NOT infinite complement certificate."""
import os
os.environ['OPENBLAS_NUM_THREADS']='4';os.environ['OMP_NUM_THREADS']='4'
import numpy as np
from scipy.linalg import lapack,blas
import math,sys,json,time
S=1<<80; T=1<<46; DS=1<<29; IS=1<<30; FS=1<<23
BANK=[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3),(11,11),(13,13),(16,2),(17,17),(19,19),(23,23),(25,5),(27,3),(29,29),(31,31),(32,2),(37,37),(41,41),(43,43),(47,47),(49,7),(53,53)]
M=512; J=int(sys.argv[2]) if len(sys.argv)>2 else 23552; shift=T//8
assert M<J<=32768 and J%2==0

def ce(n,d):return -((-n)//d)
def I(n,d=1):return n*S//d,ce(n*S,d)
def ad(a,b):return a[0]+b[0],a[1]+b[1]
def ne(a):return -a[1],-a[0]
def su(a,b):return ad(a,ne(b))
def mu(a,b):
 z=[x*y for x in a for y in b];return min(z)//S,ce(max(z),S)
def di(a,b):
 if b[0]<=0:raise ArithmeticError('denominator')
 return min(x*S//y for x in a for y in b),max(ce(x*S,y) for x in a for y in b)
def ra(a,n,d):return ne(ra(a,-n,d)) if n<0 else (a[0]*n//d,ce(a[1]*n,d))
def mid(a):return (a[0]+a[1])//2
def rad(a,c):return max(c-a[0],a[1]-c)
def logcore(n,d):
 u=n-d;v=n+d;up=u;vp=v;l=h=0
 for k in range(80):
  p=2*k+1;l+=2*S*up//(p*vp);h+=ce(2*S*up,p*vp);up*=u*u;vp*=v*v
 h+=ce(2*S*up*v*v,161*vp*(v*v-u*u));return l,h
L2=logcore(2,1)
def log(n,d=1):
 e=0
 while n>=2*d:d*=2;e+=1
 assert n>=d
 return ad(logcore(n,d),ra(L2,e,1))
def atan(d):
 a=I(0)
 for k in range(60):a=ad(a,I((-1)**k,(2*k+1)*d**(2*k+1)))
 return ad(a,(0,ce(S,121*d**121)))
pi=su(ra(atan(5),16,1),ra(atan(239),4,1));alpha=ra(pi,1,4)
assert pi[0]>3*S and alpha[0]>3*S//4
inv=di(I(1),alpha);ia=mid(inv)*IS//S
assert max(abs(inv[0]*IS-ia*S),abs(inv[1]*IS-ia*S))<=2*S
# Bound all pole tails by 2^-20 on j>=512, from IV243.
assert 4*4**4*(1<<20)<3**5*511**3

def trig(x):
 assert max(abs(x[0]),abs(x[1]))<=4*S
 xx=mu(x,x);st=x;ct=I(1);sn=st;co=ct
 for k in range(1,50):
  st=ne(ra(mu(st,xx),1,2*k*(2*k+1)));ct=ne(ra(mu(ct,xx),1,(2*k-1)*2*k));sn=ad(sn,st);co=ad(co,ct)
 e=ce(S*4**100,math.factorial(100));return ad(sn,(-e,e)),ad(co,(-e,e))

def nodes():
 ds=[I(0)]*J;ps=[I(0)]*J
 for n,p in BANK:
  l=log(n);sq=math.isqrt(n*S*S);a=di(log(p),(sq,sq+1));st,ct=trig(mu(alpha,l));b=mid(st);c=mid(ct);E=max(rad(st,b),rad(ct,c));assert J*(4*E+2)<S
  u=0;v=S;length=su(I(4),l)
  for j in range(J):
   if j>=M:
    e=j*(4*E+2);ss=(u-e,u+e);cc=(v-e,v+e)
    ds[j]=ad(ds[j],mu(a,ss));ps[j]=ad(ps[j],ra(mu(a,su(mu(length,cc),di(ss,ra(alpha,j,1)))),1,2))
   u,v=(u*c+v*b)//S,(v*c-u*b)//S
 dd=[];pd=[];gg=[];lg=ra(L2,6,1)[0]
 for j in range(M,J):
  d=mid(ds[j])*DS//S;p=mid(ps[j])*T//S
  assert max(abs(ds[j][0]*DS-d*S),abs(ds[j][1]*DS-d*S))<=2*S
  assert max(abs(ps[j][0]*T-p*S),abs(ps[j][1]*T-p*S))<=2*S
  assert max(abs(ds[j][0]),abs(ds[j][1]))<13*S
  # Exact lower Gamma diagonal: log(j/8)-8/(3j), less pole tail 2^-20.
  g=(lg-ce(8*S,3*j)-S//(1<<20))*T//S
  dd.append(d);pd.append(p);gg.append(g)
  # log((j+1)/j) positive atanh lower, 5 terms.
  for k in range(5):lg+=2*S//((2*k+1)*(2*j+1)**(2*k+1))
 return np.array(dd,dtype=np.int64),np.array(pd,dtype=np.int64),np.array(gg,dtype=np.int64)

# Off-diagonal centers: quotient in units 1/DS, multiply ia/IS, scale to T.
# True prime offdiag error <= (2/DS)/(2*alpha)+(1/DS)/alpha
# + (2/IS)*(13/2+2/DS) + 1/T < 1/2^24. Diagonal <=2/T.
# Use deliberately conservative uniform 2^-24; total row error <= n/2^24.
from fractions import Fraction
entryerr=Fraction(2,DS)*Fraction(2,3)+Fraction(4,3*DS)+Fraction(2,IS)*(Fraction(13,2)+Fraction(2,DS))+Fraction(1,T)
assert entryerr<Fraction(1,1<<24) and Fraction(2,T)<Fraction(1,1<<24)

def run(par):
 dd,pd,gg=nodes();j=np.arange(M+par,J,2,dtype=np.int64);d=dd[par::2];p=pd[par::2];g=gg[par::2];n=len(j);jd=j*d;jj=j*j
 assert int(np.max(np.abs(jd)))<2**61
 def target(i,k):
  x=jj[i,None]-jj[None,k];same=x==0;x[same]=1
  q=np.floor_divide(jd[None,k]-jd[i,None],x);q[same]=0
  assert int(np.max(np.abs(q)))<2**34 and int(np.max(np.abs(q)))*abs(ia)<2**63
  out=-np.floor_divide(q*ia,(DS*IS)//T)
  ii,kk=np.where(same);out[ii,kk]=g[np.arange(n)[i][ii]]-p[np.arange(n)[i][ii]]-shift
  assert int(np.max(np.abs(out)))<2**52
  return out
 start=time.time();A=np.empty((n,n),order='F');bs=128
 for i in range(0,n,bs):
  k=slice(i,min(i+bs,n));A[:,k]=target(slice(None),k).astype(float)/T
 print('built',par,n,time.time()-start,flush=True)
 R,info=lapack.dpotrf(A,lower=1,overwrite_a=1,clean=0);assert info==0 and np.shares_memory(A,R)
 print('factored',par,time.time()-start,flush=True)
 # Quantize the proposal to exact integers. No assumption about its numerical accuracy.
 for i in range(0,n,bs):
  s=slice(i,min(i+bs,n));R[s,:]=np.rint(R[s,:]*FS);R[s,:][np.arange(n)[None,:]>np.arange(n)[s,None]]=0
 assert np.isfinite(R).all()
 # Exact integer norms via blocks: all integer multiplications and sums safe in int64.
 row2=np.zeros(n,dtype=np.int64)
 for k in range(0,n,bs):
  s=slice(k,min(k+bs,n));x=R[:,s].astype(np.int64);assert np.array_equal(x,R[:,s]);mx=int(np.max(np.abs(x)));assert bs*mx*mx<2**62
  block=np.sum(x*x,axis=1,dtype=np.int64);assert int(row2.max())+int(block.max())<2**53;row2+=block
 bound=int(row2.max());assert bound<2**52
 # DGEMM acts here on exact integers: Cauchy-Schwarz bounds every partial sum
 # of absolute products by bound <2^52; no floating rounding is possible.
 # Single symmetric rank-k multiply; lower triangle contains the exact products.
 V=blas.dsyrk(1.0,R,lower=1,trans=0)
 print('product',par,time.time()-start,flush=True)
 rowerr=np.zeros(n,dtype=np.int64);maxentry=0
 for i in range(0,n,bs):
  k=slice(i,min(i+bs,n));vi=V[:,k].astype(np.int64);mask=np.arange(n)[:,None]>=np.arange(n)[None,k]
  assert np.array_equal(V[:,k][mask],vi[mask]) and int(np.max(np.abs(vi[mask])))<=bound
  err=np.abs(target(slice(None),k)-vi);err[~mask]=0;mx=int(err.max());assert n*mx<2**62
  maxentry=max(maxentry,mx)
  rowerr+=np.sum(err,axis=1,dtype=np.int64)
  rowerr[k]+=np.sum(err,axis=0,dtype=np.int64)-err[np.arange(n)[k],np.arange(k.stop-k.start)]
 maxerr=int(rowerr.max())
 print('verified',par,time.time()-start,flush=True)
 # Original finite form >= shift - exact max row residual - entry enclosure budget.
 loss=maxerr+n*(T//(1<<24));lb=shift-loss
 assert lb>T//10, (lb/T,maxerr/T,n/(1<<24))
 return {'parity':par,'first_mode':int(j[0]),'last_mode':int(j[-1]),'dimension':n,'scale':str(T),'shift_scaled':str(shift),'factor_row_square_max':str(bound),'max_residual_row_scaled':str(maxerr),'max_residual_entry_scaled':str(maxentry),'entry_error_budget_scaled':str(n*(T//(1<<24))),'margin_lower_scaled':str(lb),'certified_margin_gt':'1/10','classification':'finite block only; all mixed infinite-tail coupling outstanding'}

if __name__=='__main__':
 p=int(sys.argv[1]);o=run(p);print(json.dumps(o),flush=True);open(f'/tmp/iv254_parity_{p}_{J}.json','w').write(json.dumps(o,indent=2)+'\n')
