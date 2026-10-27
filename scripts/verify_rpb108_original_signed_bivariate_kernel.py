"""Rectangular two-frequency jets, including exact coincident divided differences."""
from math import comb
from flint import arb,acb,acb_series,ctx
from verify_rpb108_original_signed_frequency_kernel import Kernel

def zero(p,q):return [[acb(0) for _ in range(q)] for _ in range(p)]
def add(x,y,sign=1):return [[a+sign*b for a,b in zip(r,s)] for r,s in zip(x,y)]
def scale(x,c):return [[v*c for v in r] for r in x]
def mul(x,y):
 p=len(x);q=len(x[0]);z=zero(p,q)
 for a in range(p):
  for b in range(q):
   z[a][b]=sum((x[i][j]*y[a-i][b-j] for i in range(a+1) for j in range(b+1)),acb(0))
 return z
def lift(v,p,q,sign):return [[v[a+b]*comb(a+b,a)*sign**b for b in range(q)] for a in range(p)]
class TwoKernel:
 def __init__(self,precision=2048,terms=256):self.k=Kernel(precision,terms);self.cache={}
 def frequency(self,c):return self.k.pole if c is None else acb(2*self.k.pi*arb(str(c)))
 def data(self,c,p):
  key=(c,p)
  if key not in self.cache:
   v,A,I=self.k.functions(self.frequency(c),2*p);self.cache[key]=([A[j] for j in range(2*p)],[I[j] for j in range(2*p)])
  return self.cache[key]
 def trig(self,z0,c,n,sinc=False):
  ctx.cap=n;z=acb_series([z0,1])
  if sinc:
   if z0==0:
    from math import factorial
    return [(-1)**(j//2)*c**(j+1)/factorial(j+1) if j%2==0 else acb(0) for j in range(n)]
   v=self.k.sin(c*z)/z;return [v[j] for j in range(n)]
  v=self.k.cos(c*z);return [v[j] for j in range(n)]
 def divided(self,v0,mu,p,q,Iv,Im,plus,same=False):
  d=v0+mu if plus else acb(0) if same else v0-mu;z=zero(p,q)
  if d==0:
   assert same and not plus
   return [[Iv[a+b+1]*((-1)**b if plus else 1) for b in range(q)] for a in range(p)]
  for a in range(p):
   for b in range(q):
    num=(Iv[a] if b==0 else acb(0))+((1 if plus else -1)*Im[b] if a==0 else acb(0))
    z[a][b]=(num-(z[a-1][b] if a else 0)+(1 if not plus else -1)*(z[a][b-1] if b else 0))/d
  return z
 def overlap(self,v0,p):
  k=self.k
  a=self.trig(v0-k.pole,k.B,p,True);b=self.trig(v0+k.pole,k.B,p,True)
  return [-k.I*(a[j]-b[j]) for j in range(p)]
 def block(self,c,d,p,q):
  assert (c is None or c>0) and (d is None or d>0)
  k=self.k;v0=self.frequency(c);mu=self.frequency(d);same=c==d
  Av,Iv=self.data(c,max(p,q) if same else p);Am,Im=self.data(d,max(p,q) if same else q);n=p+q-1
  diff=acb(0) if same else v0-mu
  sm=lift(self.trig(diff,k.B,n,True),p,q,-1);sp=lift(self.trig(v0+mu,k.B,n,True),p,q,1);G=add(sm,sp,-1)
  Ap=zero(p,q)
  for a in range(p):Ap[a][0]+=Av[a]
  for b in range(q):Ap[0][b]+=Am[b]
  cm=lift(self.trig(diff,k.B,n),p,q,-1);cp=lift(self.trig(v0+mu,k.B,n),p,q,1)
  dm=self.divided(v0,mu,p,q,Iv,Im,False,same);dp=self.divided(v0,mu,p,q,Iv,Im,True)
  arch=scale(add(add(mul(G,Ap),mul(cm,dm)),mul(cp,dp),-1),acb('1/2'))
  prime=zero(p,q)
  for w,s in k.primes:
   t=(k.L-s)/2
   a=lift(self.trig(diff,t,n,True),p,q,-1);b=lift(self.trig(v0+mu,s/2,n),p,q,1)
   c=lift(self.trig(v0+mu,t,n,True),p,q,1);d=lift(self.trig(diff,s/2,n),p,q,-1)
   prime=add(prime,scale(add(mul(a,b),mul(c,d),-1),-2*w))
  hv=self.overlap(v0,p);hm=self.overlap(mu,q);pole=[[-2*hv[a]*hm[b] for b in range(q)] for a in range(p)]
  return arch,prime,pole
