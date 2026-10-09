#!/usr/bin/env python3
"""DNE16: Joint projected native source Gram and CC59/CC60 directional gate.
No external dependencies. Analytic regular tail paid using DNE11 Cauchy bound.
"""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from fractions import Fraction as F
from math import factorial, comb
import json, time, os, sys, gzip, base64
P=int(os.environ.get("DNE16_PRECISION","600"))
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
Z=I(0);A=I(F(53,50));N=int(os.environ.get("DNE16_ORDER","360"))
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
def make_u(p,dp):
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
 
 u=plus(plus([v*C for v in p],dp),reg,-1)
 # even pole polynomial, profile and moment both truncated at 64
 ch=[I(F(1,2**k*factorial(k))) if k%2==START else Z for k in range(65)]
 moment=polyint(conv(p,ch),-A,A)
 u=plus(u,ch,2*((-1)**START)*moment)
 return u

ps=[p]+[bases[n] for n in row['high_indices']]
us=[make_u(ps[0],dp)]+[make_u(bases[n],[v*I(sum((F(1,k) for k in range(1,n+1)),F(0))) for v in bases[n]]) for n in row['high_indices']]
print('three source polynomials',time.time()-start,flush=True)
u=us[0]
# complete half interval prime cuts and piecewise U.
active=(2,3,4,5,7,8);ells={n:I(n).log() for n in active}
cs={n:ells[2 if n in (4,8) else n]/I(n).sqrt() for n in active}
cuts=[I(0),A]+[(ells[n]-A if ells[n].lo>A.hi else A-ells[n]) for n in active]
cuts.sort(key=lambda x:x.lo)
# Stable polynomial-division primitive, including both endpoint limits.
# J_k^sign(x)=([x^(k+1)-b^(k+1)]log(a+sign*x)-S_k)/(k+1),
# b=-sign*a, S_k=sum_(r=1)^(k+1) b^(k+1-r)x^r/r.
# S_k=b*S_(k-1)+x^(k+1)/(k+1). No binomial transformation is needed.
maxdeg=max(map(len,us))+max(map(len,ps))-2
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
for k in range(0,2*max(map(len,ps))-1,2):
 m=k//2
 # psi(1)-psi(m+3/2)=2log2-2 sum_(j=0)^m 1/(2j+1)
 d=2*log2-2*I(sum((F(1,2*j+1) for j in range(m+1)),F(0)))
 # psi1(1)-psi1(m+3/2)=-pi²/3+4 sum_(j=0)^m 1/(2j+1)^2
 dd=-pi*pi/3+4*I(sum((F(1,(2*j+1)**2) for j in range(m+1)),F(0)))
 base=A**(k+1)/I(k+1)
 L1.append(base*(2*loga+d));L2.append(base*((2*loga+d)**2+dd))
moment_checks=0
for k in range(0,2*max(map(len,ps))-1,2):
 direct=sum((logmom[k,j] for j in range(len(cuts)-1)),Z)
 assert direct.lo<=L1[k//2].hi and L1[k//2].lo<=direct.hi
 moment_checks+=1
odd_direct=sum((logmom[1,j] for j in range(len(cuts)-1)),Z)
odd_closed=A*A/2*(2*loga-1)
assert odd_direct.lo<=odd_closed.hi and odd_closed.lo<=odd_direct.hi
moment_checks+=1
# Exact moments of the common finite source approximations. Projection onto
# the full retained-plus-measured basis is performed on these SAME sources.
indices=row['retained_indices']+row['high_indices']
gram=[[Z for _ in range(3)] for _ in range(3)]
moments=[[Z for _ in range(max(indices)+1)] for _ in range(3)]
for i in range(3):
 for j in range(i,3):
  pp=conv(ps[i],ps[j])
  gram[i][j]=sum((pp[k]*L2[k//2]/4 for k in range(0,len(pp),2)),Z)
for panel,(l,h) in enumerate(zip(cuts[:-1],cuts[1:])):
 mid=(l+h)/2;ups=[]
 for p,u in zip(ps,us):
  uj=list(u)
  for n in active:
   for sign in (-1,1):
    pos=mid+sign*ells[n]
    if pos.lo>-A.lo and pos.hi<A.lo:uj=plus(uj,shift(p,sign*ells[n]),-cs[n])
    else:assert pos.hi<=-A.hi or pos.lo>=A.hi
  ups.append(uj)
 for i in range(3):
  for j in range(i,3):
   up=plus(conv(ups[i],ps[j]),conv(ups[j],ps[i]))
   gram[i][j]=gram[i][j]+polyint(conv(ups[i],ups[j]),l,h)-sum((up[k]*logmom[k,panel]/2 for k in range(len(up))),Z)
 # Monomial moments avoid repeating 56 polynomial convolutions per panel.
 maxk=max(map(len,ups))+max(indices)
 pm=[(h**(k+1)-l**(k+1))/(k+1) for k in range(maxk)]
 for i in range(3):
  for n in indices:
   moments[i][n]=moments[i][n]+sum((v*pm[k+n] for k,v in enumerate(ups[i])),Z)-sum((v*logmom[k+n,panel]/2 for k,v in enumerate(ps[i])),Z)
 print('joint panel',panel,time.time()-start,flush=True)
coords=[]
for i in range(3):
 coords.append([2*sum((v*moments[i][k] for k,v in enumerate(bases[n])),Z) for n in indices])
# moments above include only n in indices. Basis monomials have the same parity
# and every degree <=115 is present in indices, so all needed moments exist.
projected=[[Z for _ in range(3)] for _ in range(3)]
for i in range(3):
 for j in range(i,3):
  gram[i][j]=2*gram[i][j];gram[j][i]=gram[i][j]
  projected[i][j]=gram[i][j]-sum((x*y for x,y in zip(coords[i],coords[j])),Z)
  projected[j][i]=projected[i][j]
delta=I(F(550,19))*I(F(106,125))**N
operr=2*A*delta+I('3e-99')
errs=[operr*I(F(row['compensated_norm_squared'])).sqrt(),operr,operr]
# Transfer the frozen target to the exact H2 minimizer, using DNE15's ledger.
assert all(abs(F(v)-F(b))<F(1,10**60) for v,enclosure in zip(row['exact_rational_high_compensation'],row['true_H2_minimizer_enclosures']) for b in enclosure)
errs[0]=errs[0]+I('4e-58')
native=[[Z for _ in range(3)] for _ in range(3)]
for i in range(3):
 assert projected[i][i].lo>0
 for j in range(i,3):
  e=errs[i]*I(projected[j][j].hi).sqrt()+errs[j]*I(projected[i][i].hi).sqrt()+errs[i]*errs[j]
  native[i][j]=projected[i][j]+I(e.hi.copy_negate(),e.hi);native[j][i]=native[i][j]
# Check native finite form input against the independent source projection.
cc=json.load(open(sys.argv[4]))
crow=next(v for v in cc['native_penalty_bounds'] if v['parity']==PARITY)
def enclosure(v):return I(I(F(v[0])).lo,I(F(v[1])).hi)
C2=[[enclosure(crow['native_full_intervals_rounded_outward_1e45'][','.join(map(str,sorted((n,m))))]) for m in row['high_indices']] for n in row['high_indices']]
for i in range(2):
 for j in range(2):
  computed=coords[i+1][-2+j]+I(errs[i+1].hi.copy_negate(),errs[i+1].hi)
  assert computed.lo<=C2[i][j].hi and C2[i][j].lo<=computed.hi
for k,v in enumerate(row['low_source_coordinates']):
 exact=enclosure(v);computed=coords[0][k]+I(errs[0].hi.copy_negate(),errs[0].hi)
 assert computed.lo<=exact.hi and exact.lo<=computed.hi
kappa=I(F(207,1000));P2=native[0][0];Z2=[native[0][j+1] for j in range(2)]
H=[[native[i+1][j+1] for j in range(2)] for i in range(2)]
W=[[sum((C2[i][k]*C2[k][j] for k in range(2)),Z)-kappa*C2[i][j] for j in range(2)] for i in range(2)]
V=[[W[i][j]+H[i][j] for j in range(2)] for i in range(2)]
det=V[0][0]*V[1][1]-V[0][1]*V[1][0];assert det.lo>0
gain=(V[1][1]*Z2[0]**2-2*V[0][1]*Z2[0]*Z2[1]+V[0][0]*Z2[1]**2)/det
minimum=P2-gain
energy=enclosure(row['compensated_energy'])+I('-1e-118',0)
budget=kappa*energy
Y=[(V[1][1]*Z2[0]-V[0][1]*Z2[1])/det,(V[0][0]*Z2[1]-V[1][0]*Z2[0])/det]
# Freeze midpoint trials to rationals with denominator 10^60; certification
# below uses exact trials, independent of any interval inverse identity.
yr=[F(round((F(v.lo)+F(v.hi))/2*10**60),10**60) for v in Y]
J=P2-2*sum((I(yr[i])*Z2[i] for i in range(2)),Z)+sum((I(yr[i])*V[i][j]*I(yr[j]) for i in range(2) for j in range(2)),Z)
out={'stage':'DNE16','parity':PARITY,'precision':P,'regular_order':N,
 'target_sha256':hashlib.sha256(target_bytes).hexdigest(),
 'projected_truncated_Gram':[[v.data() for v in rr] for rr in projected],
 'native_exact_H2_projected_Gram':[[v.data() for v in rr] for rr in native],
 'C2':[[v.data() for v in rr] for rr in C2],
 'source_error_bounds':[str(e.hi) for e in errs],
 'projected_basis_indices':indices,'native_finite_pairing_overlap_checks':60,
 'P2':P2.data(),'Z': [v.data() for v in Z2],'H':[[v.data() for v in rr] for rr in H],
 'W0':[[v.data() for v in rr] for rr in W], 'V':[[v.data() for v in rr] for rr in V],
 'det_V':det.data(),'optimized_gain':gain.data(),'gain_fraction':(gain/P2).data(),
 'required_gain_fraction':(1-budget/P2).data(),
 'optimized_J':minimum.data(),'optimized_J_over_energy':(minimum/energy).data(),
 'fixed_rational_Y':[str(v) for v in yr], 'fixed_rational_J':J.data(),
 'fixed_rational_J_over_energy':(J/energy).data(),
 'energy':energy.data(),'budget':budget.data(),
 'fixed_gate_passed':J.hi<budget.lo,'optimized_gate_failure_proved':minimum.lo>budget.hi,
 'elapsed_seconds':time.time()-start,'whole_matrix_certified':False,
 'true_inverse_response_evaluated':False,'RH':False,'Lean':False}
print(json.dumps({k:out[k] for k in ('parity','gain_fraction','required_gain_fraction','optimized_J_over_energy','fixed_gate_passed','optimized_gate_failure_proved','elapsed_seconds')},indent=2))
open(sys.argv[3],'w').write(json.dumps(out,indent=2)+'\n')
