#!/usr/bin/env python3
"""NF15: exact directed Fraction native matrix for 80 modes at a=53/50.
Full archimedean, six original primes with both shifts, and signed poles.
Complete interval archive only; whole 112/source Schur sign remains open.
"""
from fractions import Fraction as F
from math import comb, factorial, isqrt, lcm
from functools import lru_cache
import time, json
A=F(53,50); N=490; K=430; DEG=79; GRID=10**180
class I:
 def __init__(self,a,b=None):
  if isinstance(a,I):self.lo,self.hi=a.lo,a.hi;return
  a=F(a);b=F(a if b is None else b);assert a<=b
  self.lo=F((a*GRID).__floor__(),GRID);self.hi=F((b*GRID).__ceil__(),GRID)
 def __add__(self,v):
  v=I(v);return I(self.lo+v.lo,self.hi+v.hi)
 __radd__=__add__
 def __neg__(self):return I(-self.hi,-self.lo)
 def __sub__(self,v):return self+-I(v)
 def __rsub__(self,v):return I(v)+-self
 def __mul__(self,v):
  v=I(v);p=[a*b for a in (self.lo,self.hi) for b in (v.lo,v.hi)]
  return I(min(p),max(p))
 __rmul__=__mul__
 def __truediv__(self,v):
  v=I(v);assert v.lo>0 or v.hi<0
  return self*I(1/v.hi,1/v.lo)
 def __rtruediv__(self,v):return I(v)/self
def sq(n):
 g=10**80;k=isqrt(n*g*g);return I(F(k,g),F(k+1,g))
@lru_cache(None)
def log(n,terms=500):
 n=F(n);assert n>0
 def unit(x):
  z=(x-1)/(x+1);p=z;s=F(0)
  for j in range(terms):s+=2*p/F(2*j+1);p*=z*z
  e=2*abs(p)/(F(2*terms+1)*(1-z*z))
  return I(s-e,s+e)
 k=0
 while n>=2:n/=2;k+=1
 while n<1:n*=2;k-=1
 return unit(n)+k*unit(F(2))
def logI(v):return I(log(v.lo).lo,log(v.hi).hi)
def atan(x,terms=130):
 p=x;s=F(0)
 for k in range(terms):s+=(-1)**k*p/F(2*k+1);p*=x*x
 return I(s-abs(p)/F(2*terms+1),s+abs(p)/F(2*terms+1))
def bern(n):
 b=[F(1)]
 for m in range(1,n+1):b.append(-sum((F(comb(m+1,k))*b[k] for k in range(m)),F(0))/F(m+1))
 return b
def mul(p,q):
 dp=lcm(*(x.denominator for x in p));dq=lcm(*(x.denominator for x in q))
 pp=[int(x*dp) for x in p];qq=[int(x*dq) for x in q];z=[0]*(len(p)+len(q)-1)
 for i,x in enumerate(pp):
  if x:
   for j,y in enumerate(qq):
    if y:z[i+j]+=x*y
 return [F(v,dp*dq) for v in z]
def corr(p,q):
 dp=lcm(*(x.denominator for x in p));dq=lcm(*(x.denominator for x in q))
 pp=[int(x*dp) for x in p];qq=[int(x*dq) for x in q]
 sz=len(p)+len(q);den=lcm(*range(1,sz));P=[[0]*sz for _ in range(sz)]
 for i,x in enumerate(pp):
  if x:
   for j,y in enumerate(qq):
    if y:
     for k in range(j+1):
      m=i+j-k+1;P[m][k]+=x*y*comb(j,k)*(-1)**k*(den//m)
 hi=[sum(row[k] for row in P) for k in range(sz)];lo=[0]*sz
 for row in reversed(P):
  assert lo[-1]==0
  lo=[row[k]-lo[k]+(lo[k-1] if k else 0) for k in range(sz)]
 return [F(x-y,dp*dq*den) for x,y in zip(hi,lo)]
def make_integrator(ker,ex,maxcorr):
 den=lcm(*(c.denominator for c in ker));raw=[int(c*den) for c in ker]
 jd=lcm(*range(1,len(ker)+len(ex)+maxcorr));M=len(ex)+maxcorr-2
 weights=[sum((c*(jd//(m+k+1)) for k,c in enumerate(raw) if c),0) for m in range(M)]
 ed=lcm(*(c.denominator for c in ex));ec=[int(c*ed) for c in ex]
 shifted=[sum((x*weights[q+r-1] for q,x in enumerate(ec) if q+r>0),0) for r in range(maxcorr)]
 full=sum((4**q*x*weights[q-1] for q,x in enumerate(ec) if q>0),0)
 def integrate(c,delta):
  assert len(c)<=maxcorr and c[0]==delta
  d=lcm(*(x.denominator for x in c));nc=[int(x*d) for x in c]
  return F(nc[0]*full-sum((x*w for x,w in zip(nc,shifted)),0),d*ed*den*jd)
 return integrate
@lru_cache(None)
def P(i):
 if i==0:return [F(1)]
 if i==1:return [F(0),F(1)]
 a=P(i-1);b=P(i-2);out=[F(0)]*(i+1)
 for k,x in enumerate(a):out[k+1]+=F(2*i-1,i)*x
 for k,x in enumerate(b):out[k]-=F(i-1,i)*x
 return out
def construct():
 t=time.monotonic();L=4*A;B=bern(2*K+2)
 pi=16*atan(F(1,5))-4*atan(F(1,239))
 g=I(sum((F(1,k) for k in range(1,101)),F(0))-F(1,200))-log(100)
 for k in range(1,21):g+=B[2*k]/F(2*k*100**(2*k))
 e=abs(B[42])/F(42*100**42);g+=I(-e,e)
 e1=sum(((-L)**k/factorial(k) for k in range(N+1)),F(0))
 ee=F(70)*L**(N+1)/factorial(N+1)
 constant=-g-logI(pi)-logI(I(1-e1-ee,1-e1+ee))
 ker=[F(0)]*(2*K+1);ker[0]=1;ker[1]=L/2
 for k in range(1,K+1):ker[2*k]=B[2*k]*L**(2*k)/factorial(2*k)
 kerr=4*(L/6)**(2*K+2)/(1-(L/6)**2)
 fn=make_integrator(ker,[(-L/4)**k/factorial(k) for k in range(N+1)],2*DEG+4)
 poles=[]
 for i in range(DEG+1):
  p=P(i);prod=mul(p,[(A/2)**k/factorial(k) for k in range(N+1)])
  v=A*sum((2*c/F(k+1) for k,c in enumerate(prod) if k%2==0),F(0))
  err=4*A*sum(map(abs,p))*(A/2)**(N+1)/factorial(N+1)
  poles.append(I(v-err,v+err))
 prime_set=(2,3,4,5,7,8);ln={n:log(n) for n in prime_set}
 coef={n:(log(2) if n in (4,8) else ln[n])/sq(n) for n in prime_set}
 out={};maxwidth=F(0)
 for i in range(DEG+1):
  for j in range(i,DEG+1):
   if (i+j)%2:continue
   c=[A*x*2**k for k,x in enumerate(corr(P(i),P(j)))]
   delta=F(2*A,2*i+1) if i==j else F(0);assert c[0]==delta
   val=fn(c,delta);csum=sum(map(abs,c))
   exp_err=70*L**(N+1)/factorial(N+1)*(delta+csum/F(4**(N+1)))
   aerr=F(3,4)*L*delta+sum(map(abs,c[1:]))
   err=F(53,10)*exp_err+aerr*kerr
   arch=delta*constant+I(val-err,val+err)
   pole=(int((-1)**i)+int((-1)**j))*poles[i]*poles[j]
   prime=I(0)
   for n in prime_set:
    q=ln[n]/I(2*A);p=I(0)
    for k in reversed(c):p=p*q+k
    prime+=2*coef[n]*p
   norm=sq((2*i+1)*(2*j+1))/I(2*A)
   parts={'arch':norm*arch,'poles':norm*pole,'prime':-norm*prime,'full':norm*(arch+pole-prime)}
   out[f'{i},{j}']={k:[str(v.lo),str(v.hi)] for k,v in parts.items()}
   maxwidth=max(maxwidth,parts['full'].hi-parts['full'].lo)
 return out,maxwidth,time.monotonic()-t
def certificate():
 out,width,seconds=construct()
 return dict(aperture='53/50',native_dimension=4,full_112=False,
   original_archimedean=True,all_prime_powers=[2,3,4,5,7,8],
   both_translation_orientations=True,signed_Hermitian_poles=True,
   original_native_entries=out,maximum_full_interval_width=str(width),
   elapsed_seconds=seconds,full_source_Gram=False,whole_aperture_positive=False)
if __name__=='__main__':
 import argparse, pathlib, hashlib
 parser=argparse.ArgumentParser()
 parser.add_argument('--dimension',type=int,choices=(80,),default=80)
 parser.add_argument('--exponential-order',type=int,choices=(490,),default=490)
 parser.add_argument('--bernoulli-pairs',type=int,choices=(430,),default=430)
 parser.add_argument('--output',required=True)
 args=parser.parse_args()
 if (args.exponential_order,args.bernoulli_pairs) not in ((490,430),):
  parser.error('Only proposed order pair 490/430; sign validated separately')
 DEG=args.dimension-1;N=args.exponential_order;K=args.bernoulli_pairs
 records,width,seconds=construct()
 assert len(records)==(args.dimension//2)*(args.dimension//2+1)
 payload=dict(aperture='53/50',dim=args.dimension,N=N,K=K,complete_form=records,width=str(width))
 output=pathlib.Path(args.output)
 output.write_text(json.dumps(payload,sort_keys=True,separators=(',',':')))
 digest=hashlib.sha256(output.read_bytes()).hexdigest()
 print(json.dumps(dict(status='matrix generated; finite sign requires separate validator',
    dimension=args.dimension,entries=len(records),N=N,K=K,
    maximum_interval_width=str(width),seconds=seconds,sha256=digest,
    output=str(output),full_112=False,whole_original_positive=False),indent=2))
