#!/usr/bin/env python3
"""DNE15: Directed Decimal intervals for NF24 near-critical compensated sources.
No external dependencies. Analytic regular tail paid using DNE11 Cauchy bound.
"""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from fractions import Fraction as F
from math import factorial, comb
import json, time, os, sys, gzip, base64
P=int(os.environ.get("DNE15_PRECISION","600"))
loctx=Context(prec=P,rounding=ROUND_FLOOR); hictx=Context(prec=P,rounding=ROUND_CEILING)
near=Context(prec=P,rounding=ROUND_HALF_EVEN)
class I:
 def __init__(self,x=0,y=None):
  if isinstance(x,I): self.lo,self.hi=x.lo,x.hi;return
  if isinstance(x,F): self.lo=loctx.divide(D(x.numerator),D(x.denominator));self.hi=hictx.divide(D(x.numerator),D(x.denominator));return
  self.lo=D(x);self.hi=D(x if y is None else y)
 def __add__(s,t):
  t=I(t);return I(loctx.add(s.lo,t.lo),hictx.add(s.hi,t.hi))
 __radd__=__add__
 def __neg__(s):return I(s.hi.copy_negate(),s.lo.copy_negate())
 def __sub__(s,t):return s+-I(t)
 def __rsub__(s,t):return I(t)+-s
 def __mul__(s,t):
  t=I(t);return I(min(loctx.multiply(x,y) for x in (s.lo,s.hi) for y in (t.lo,t.hi)),max(hictx.multiply(x,y) for x in (s.lo,s.hi) for y in (t.lo,t.hi)))
 __rmul__=__mul__
 def __truediv__(s,t):
  t=I(t);assert t.lo>0 or t.hi<0
  return s*I(loctx.divide(D(1),t.hi),hictx.divide(D(1),t.lo))
 def __pow__(s,n):
  assert n>=0
  r=I(1)
  while n:
   if n&1:r=r*s
   s=s*s;n//=2
  return r
 def log(s):
  assert s.lo>0
  # Decimal ln/sqrt are correctly rounded nearest regardless of context mode.
  l=near.ln(s.lo);h=near.ln(s.hi)
  return I(near.next_minus(l),near.next_plus(h))
 def sqrt(s):
  assert s.lo>=0
  l=near.sqrt(s.lo);h=near.sqrt(s.hi)
  return I(near.next_minus(l),near.next_plus(h))
 def absmax(s):return max(s.lo.copy_abs(),s.hi.copy_abs())
 def data(s):return [str(s.lo),str(s.hi)]
Z=I(0);A=I(F(53,50));N=int(os.environ.get("DNE15_ORDER","360"))
PARITY=sys.argv[1];assert PARITY in ("even","odd")
TARGET_PATH=sys.argv[2]
import hashlib
target_bytes=open(TARGET_PATH,"rb").read()
if TARGET_PATH.endswith(".gz.b64"):target_bytes=gzip.decompress(base64.b64decode(target_bytes))
assert hashlib.sha256(target_bytes).hexdigest()=="6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00"
row=next(r for r in json.loads(target_bytes)["authenticated_compensated_targets"] if r["parity"]==PARITY)
START=0 if PARITY=="even" else 1

def conv(p,q):
 out=[I(0) for _ in range(len(p)+len(q)-1)]
 for i,x in enumerate(p):
  if x.lo==x.hi==0:continue
  for j,y in enumerate(q):
   if y.lo==y.hi==0:continue
   out[i+j]=out[i+j]+x*y
 return out

def plus(p,q,scale=1):
 out=list(p)+[Z]*max(0,len(q)-len(p))
 for i,x in enumerate(q):out[i]=out[i]+scale*x
 return out

def shift(p,b):
 out=[Z]*len(p)
 powers=[b**k for k in range(len(p))]
 for k,v in enumerate(p):
  if v.lo==v.hi==0:continue
  for i in range(k+1):out[i]=out[i]+v*comb(k,i)*powers[k-i]
 return out

def evalp(p,x):
 s=Z
 for v in reversed(p):s=s*x+v
 return s

def polyint(p,l,r):
 pp=[Z]+[v/(i+1) for i,v in enumerate(p)]
 return evalp(pp,r)-evalp(pp,l)

def atan_rat(q,K=400):
 x=F(1,q);s=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(K)),F(0))
 err=x**(2*K+1)/F(2*K+1)
 return I(s)+I(I(err).hi.copy_negate(),I(err).hi)

def bernoulli(n):
 b=[F(1)]
 for m in range(1,n+1):b.append(-sum(F(comb(m+1,k))*b[k] for k in range(m))/F(m+1))
 return b

def gamma():
 # EM for H_n: remainder after B_2m has sign of next term and at most its magnitude.
 n=100;m=200;b=bernoulli(2*m+2)
 s=I(sum((F(1,k) for k in range(1,n+1)),F(0)))-I(n).log()-I(F(1,2*n))
 for k in range(1,m+1):s=s+I(b[2*k]/F(2*k*n**(2*k)))
 e=abs(b[2*m+2]/F((2*m+2)*n**(2*m+2)))
 return s+I(I(e).hi.copy_negate(),I(e).hi)

start=time.time();pi=16*atan_rat(5)-4*atan_rat(239);G=gamma();C=-G-(2*pi).log()
print('constants',flush=True)
# normalized Legendre basis in physical x coordinate.
bases=[];raw0=[I(1)];raw1=[Z,I(1)/A]
for n in range(116):
 if n==0:r=raw0
 elif n==1:r=raw1
 else:
  r=plus([Z]+[x*F(2*n-1,n)/A for x in raw1],raw0,-F(n-1,n));raw0,raw1=raw1,r
 bases.append([x*(I(2*n+1)/(2*A)).sqrt() for x in r])
degrees=row['retained_indices']+row['high_indices']
coeff=[I(F(v)) for v in row['retained_coefficients']+row['exact_rational_high_compensation']]
p=[Z]*(max(degrees)+1);dp=[Z]*len(p)
for c,n in zip(coeff,degrees):
 p=plus(p,bases[n],c);dp=plus(dp,bases[n],c*I(sum((F(1,k) for k in range(1,n+1)),F(0))))
# exact rational r_N coefficients
q=[]
for n in range(N+1):q.append(F(1,2**(n+1)*factorial(n))-sum((q[n-2*k]/factorial(2*k+1) for k in range(1,n//2+1)),F(0)))
r=[I(v) for v in q[1:]]
# convolution of r(|x-y|) with even p. Formula derived by split polynomial primitives.
reg=[Z]*(N+len(p))
powers=[A**k for k in range(N+len(p)+1)]
# Group the endpoint moments BEFORE multiplying kernel coefficients.
# This is the same split-convolution polynomial, with only O(N^2+N deg p)
# interval operations instead of O(N^2 deg p).
endmom=[sum((p[k]*powers[k+t+1]/(k+t+1) for k in range(START,len(p),2)),Z) for t in range(N)]
for m,rm in enumerate(r):
 for l in range(START,m+1,2):
  reg[l]=reg[l]+2*((-1)**START)*rm*comb(m,l)*endmom[m-l]
 if m%2:
  for k in range(START,len(p),2):
   reg[m+k+1]=reg[m+k+1]+2*rm*p[k]*I(F(factorial(k)*factorial(m),factorial(k+m+1)))
print('regular polynomial',time.time()-start,flush=True)
u=plus(plus([v*C for v in p],dp),reg,-1)
# even pole polynomial, profile and moment both truncated at 64
ch=[I(F(1,2**k*factorial(k))) if k%2==START else Z for k in range(65)]
moment=polyint(conv(p,ch),-A,A)
u=plus(u,ch,2*((-1)**START)*moment)
# complete half interval prime cuts and piecewise U.
active=(2,3,4,5,7,8);ells={n:I(n).log() for n in active}
cs={n:ells[2 if n in (4,8) else n]/I(n).sqrt() for n in active}
cuts=[I(0),A]+[(ells[n]-A if ells[n].lo>A.hi else A-ells[n]) for n in active]
cuts.sort(key=lambda x:x.lo)
# Stable polynomial-division primitive, including both endpoint limits.
# J_k^sign(x)=([x^(k+1)-b^(k+1)]log(a+sign*x)-S_k)/(k+1),
# b=-sign*a, S_k=sum_(r=1)^(k+1) b^(k+1-r)x^r/r.
# S_k=b*S_(k-1)+x^(k+1)/(k+1). No binomial transformation is needed.
maxdeg=len(u)+len(p)-2
logprims={}
for j,x in enumerate(cuts):
 xp=[x**k for k in range(maxdeg+2)]
 vals=[Z]*(maxdeg+1)
 for sign in (-1,1):
  b=-sign*A;bp=[b**k for k in range(maxdeg+2)]
  t=A+sign*x
  endpoint=t.lo<=0<=t.hi
  if endpoint:assert abs(t.lo)<D('1e-170') and abs(t.hi)<D('1e-170')
  lt=Z if endpoint else t.log();S=Z
  for k in range(maxdeg+1):
   S=b*S+xp[k+1]/(k+1)
   first=Z if endpoint else (xp[k+1]-bp[k+1])*lt
   vals[k]=vals[k]+(first-S)/(k+1)
 for k,v in enumerate(vals):logprims[k,j]=v
logmom={(k,j):logprims[k,j+1]-logprims[k,j] for k in range(maxdeg+1) for j in range(len(cuts)-1)}
print('log moments',time.time()-start,flush=True)
# Complete half-interval log and log² moments by beta derivatives.
log2=I(2).log();loga=A.log();L1=[];L2=[]
for k in range(0,2*len(p)-1,2):
 m=k//2
 # psi(1)-psi(m+3/2)=2log2-2 sum_(j=0)^m 1/(2j+1)
 d=2*log2-2*I(sum((F(1,2*j+1) for j in range(m+1)),F(0)))
 # psi1(1)-psi1(m+3/2)=-pi²/3+4 sum_(j=0)^m 1/(2j+1)^2
 dd=-pi*pi/3+4*I(sum((F(1,(2*j+1)**2) for j in range(m+1)),F(0)))
 base=A**(k+1)/I(k+1)
 L1.append(base*(2*loga+d));L2.append(base*((2*loga+d)**2+dd))
moment_checks=0
for k in range(0,2*len(p)-1,2):
 direct=sum((logmom[k,j] for j in range(len(cuts)-1)),Z)
 assert direct.lo<=L1[k//2].hi and L1[k//2].lo<=direct.hi
 moment_checks+=1
odd_direct=sum((logmom[1,j] for j in range(len(cuts)-1)),Z)
odd_closed=A*A/2*(2*loga-1)
assert odd_direct.lo<=odd_closed.hi and odd_closed.lo<=odd_direct.hi
moment_checks+=1
pp=conv(p,p);total=sum((pp[k]*L2[k//2]/4 for k in range(0,len(pp),2)),Z)
ener=I(I(F(row["compensated_energy"][0])).lo,I(F(row["compensated_energy"][1])).hi)
for j,(l,h) in enumerate(zip(cuts[:-1],cuts[1:])):
 mid=(l+h)/2;uj=list(u)
 for n in active:
  for sign in (-1,1):
   pos=mid+sign*ells[n]
   if pos.lo>-A.lo and pos.hi<A.lo:uj=plus(uj,shift(p,sign*ells[n]),-cs[n])
   else:assert pos.hi<=-A.hi or pos.lo>=A.hi
 up=conv(uj,p)
 total=total+polyint(conv(uj,uj),l,h)-sum((up[k]*logmom[k,j] for k in range(len(up))),Z)
 print('panel',j,time.time()-start,flush=True)
total=2*total
projection=I(I(F(row['low_source_projection_squared'][0])).lo,I(F(row['low_source_projection_squared'][1])).hi)
res=total-projection
mass=I(F(row['compensated_norm_squared']))
delta=I(F(550,19))*I(F(106,125))**N
err=2*A*delta*mass.sqrt()+I('3e-99')*mass.sqrt()
assert total.lo>0
sqerr=err*(2*I(total.hi).sqrt()+err)
res=res+I(sqerr.hi.copy_negate(),sqerr.hi)
budget=I(F(207,1000))*ener
ratio=res/ener
out={'stage':'DNE15','parity':PARITY,'precision':P,'regular_order':N,
 'target_sha256':hashlib.sha256(target_bytes).hexdigest(),
 'gamma_bernoulli_pairs':200,'moment_consistency_checks':moment_checks,
 'complete_source_square_truncated':total.data(),
 'certified_low_projection_square':projection.data(),
 'actual_full_F112_residual_square':res.data(),
 'certified_compensated_energy':ener.data(),
 'sufficient_budget':budget.data(),'residual_square_over_energy':ratio.data(),
 'source_L2_error_bound':str(err.hi),'squared_norm_error_bound':str(sqerr.hi),
 'scalar_gate_passed':res.hi<budget.lo,'scalar_gate_failure_proved':res.lo>budget.hi,
 'elapsed_seconds':time.time()-start,'whole_matrix_certified':False,
 'true_inverse_response_evaluated':False,'RH':False,'Lean':False}
print(json.dumps(out,indent=2))
open(sys.argv[3],'w').write(json.dumps(out,indent=2)+'\n')
