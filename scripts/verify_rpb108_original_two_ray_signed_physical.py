"""512-bit whole signed form of the fixed original sine/sinh rays.

Physical shift integral, analytic zero-shift regularization, seven clipped
prime overlaps, true pole and explicit infinite Laplace tail. No cutoff
frequency or FFT is used. Native evaluation/domain standing remains separate.
"""
from flint import arb,acb,ctx
from fractions import Fraction as F
from math import factorial
import time
ctx.prec=512;pi=arb.pi();B=arb('11/10');L=2*B;w=2*pi*arb('37/64');I=acb(0,1);SH=(B/2).sinh();CH=(B/2).cosh()
lam=[acb(0,w),acb(0,-w),acb('1/2'),acb('-1/2')];desc=[(0,1),(0,-1),(1,0),(-1,0)]
def exprel(z):return (z/2).exp()*(I*z/2).sinc()
def setup(a,b):
 co=[acb(0,-arb(a)/2),acb(0,arb(a)/2),acb(arb(b)/2),acb(-arb(b)/2)]
 terms=[];norm=acb(0)
 for j in range(4):
  for k in range(4):
   zero=desc[j][0]+desc[k][0]==0 and desc[j][1]+desc[k][1]==0
   rho=lam[j]+lam[k];coef=co[j]*co[k]
   if zero:norm+=coef*L
   else:norm+=coef*((rho*B).exp()-(-rho*B).exp())/rho
   terms.append((j,k,rho,coef,zero))
 def overlap(s):
  z=acb(0)
  for j,k,rho,c,zero in terms:
   z+=c*( (L-s)*(lam[k]*s).exp() if zero else ((rho*B-lam[j]*s).exp()-(-rho*B+lam[k]*s).exp())/rho )
  return z
 def D(s):
  z=acb(0)
  for j,k,rho,c,zero in terms:
   z+=c*((lam[k]*s).exp()-L*lam[k]*exprel(lam[k]*s) if zero else ((rho*B).exp()*lam[j]*exprel(-lam[j]*s)+(-rho*B).exp()*lam[k]*exprel(lam[k]*s))/rho)
  return z
 return norm,overlap,D

def signed_form(a,b):
 start=time.monotonic();norm,A,D=setup(a,b)
 assert norm.imag.contains(0)
 integ=acb.integral(lambda s,_: (s/2).exp()/(I*s).sinc()*D(s),0,L,rel_tol=arb(2)**-128,abs_tol=arb(2)**-128,eval_limit=20000,depth_limit=20)
 assert integ.is_finite() and integ.imag.contains(0)
 tail=arb(0)
 for n in range(64):
  ln=arb(2*n)+arb('1/2');tail+=2*(-ln*L).exp()/ln
 rem=2*(-arb('257/2')*L).exp()/(arb('257/2')*(1-(-2*L).exp()));tail+=arb(0,rem.upper())
 c0=-arb.const_euler()-pi/2-3*arb(2).log()-pi.log()
 assert (c0-(acb('1/4').digamma().real-pi.log())).contains(0)
 arch=c0*norm+integ+tail*norm
 prime=acb(0);translations=[]
 for n,p in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]:
  shift=arb(n).log();ov=A(shift);prime-=2*arb(p).log()/arb(n).sqrt()*ov;translations.append((n,ov))
 co=[acb(0,-arb(a)/2),acb(0,arb(a)/2),acb(arb(b)/2),acb(-arb(b)/2)];pole=acb(0)
 for j in range(4):
  for real,sign in [(arb('1/2'),1),(arb('-1/2'),-1)]:
   zero=(j==2 and sign==-1) or(j==3 and sign==1);v=lam[j]+real
   pole+=co[j]*sign/2*(L if zero else ((v*B).exp()-(-v*B).exp())/v)
 Q=arch+prime-2*pole*pole
 assert Q.is_finite() and Q.imag.contains(0) and Q.real.rad()<arb('1/1000')
 # Independent inherited trig/Laurent physical primitives on this genuine ray.
 import verify_rpb108_si29_original_prime_mixed as p
 terms=[(n,t,f,c*a) for n,t,f,c in p.m.source_terms(F(37,64),0)]+[(n,t,f,c*b) for n,t,f,c in p.m.pole_terms()]
 kernel=p.m.Integrals();norm2=p.m.gram(terms,terms,kernel);pole2=p.m.gram(terms,p.m.pole_terms(),kernel)
 assert (norm.real-norm2).contains(0) and (pole.real-pole2).contains(0)
 endpoint=sum((co[j]*(lam[j]*B).exp() for j in range(4)),acb(0));assert (D(acb(0))-endpoint*endpoint).contains(0)
 for s in [acb('1/7'),acb('11/10'),acb('11/5')]:assert (D(s)-(norm-A(s))/s).contains(0)
 for n,ov in translations:
  ck=p.Clipped(arb(n).log());shifted=p.shifted(terms,ck);ref=p.clipped_gram(terms,shifted,ck)
  assert (ov.real-ref).contains(0) and ov.imag.contains(0)
 for q in [F(0),F(37,64),F(1),F(12)]:
  fq=p.m.gram(p.m.source_terms(q,0),terms,kernel)
  assert (fourier_basis(arb(str(q)))[0]*a+fourier_basis(arb(str(q)))[1]*b-fq).contains(0)
 assert all(v.imag.contains(0) for v in [arch,prime,pole])
 return dict(norm=norm.real,arch=arch.real,arch_constant=c0,arch_integral=integ.real,tail=tail,prime=prime.real,pole=pole.real,signed=Q.real,elapsed=time.monotonic()-start)

def fourier_basis(q):
 t=2*pi*q
 sine=B*((2*pi*B*(arb('37/64')-q)).sinc()-(2*pi*B*(arb('37/64')+q)).sinc())
 pole=2*(arb('1/2')*CH*(t*B).sin()-t*SH*(t*B).cos())/(arb('1/4')+t*t)
 return sine,pole
