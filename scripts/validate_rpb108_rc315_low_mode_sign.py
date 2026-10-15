"""RC315: certified original signed Weil P0/P1 diagonal test (not full Schur)."""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
B=F(11,10); R=2*B; GRID=10**12
REG_SOURCE='certificates/rpb108_rc46_native_archimedean_head.json'
REG_PIN='be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9'
ORIGINAL_SOURCE='certificates/rpb108_rc313_prime_pole_distributions.json'
ORIGINAL_PIN='954b4892cf3b4e999e65476d7ce341021528d9e8'
FREDHOLM_SOURCE='certificates/rpb108_rc314_fredholm_schur.json'
FREDHOLM_PIN='6496be8d20176f173c0ff8b6e393b0ccd7c6ff5b'
PRIMES=[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]
class IV:
 def __init__(self,lo,hi=None):
  self.lo=F(lo);self.hi=F(lo if hi is None else hi)
  assert self.lo<=self.hi
 def __add__(self,o):
  o=asiv(o);return IV(self.lo+o.lo,self.hi+o.hi)
 __radd__=__add__
 def __neg__(self):return IV(-self.hi,-self.lo)
 def __sub__(self,o):return self+-asiv(o)
 def __rsub__(self,o):return asiv(o)+-self
 def __mul__(self,o):
  o=asiv(o);p=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
  return IV(min(p),max(p))
 __rmul__=__mul__
 def __truediv__(self,o):
  o=asiv(o);assert o.lo*o.hi>0
  return self*IV(1/o.hi,1/o.lo)
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  if n==0:return IV(1)
  if n%2==0 and self.lo<=0<=self.hi:
   return IV(0,max(abs(self.lo),abs(self.hi))**n)
  p=[self.lo**n,self.hi**n];return IV(min(p),max(p))
 def bounds(self):
  return [str(F(self.lo.numerator*GRID//self.lo.denominator,GRID)),
          str(F((self.hi.numerator*GRID+self.hi.denominator-1)//self.hi.denominator,GRID))]
def asiv(x):return x if isinstance(x,IV) else IV(x)
def sqrt_i(n):
 scale=10**35;f=isqrt(n*scale*scale)
 return IV(F(f,scale),F(f+1,scale))
def log_positive_rational(x,K=220):
 assert x>1
 t=(x-1)/(x+1)
 s=sum((2*t**(2*k+1)/F(2*k+1) for k in range(K)),F(0))
 tail=2*t**(2*K+1)/(F(2*K+1)*(1-t*t))
 return IV(s,s+tail)
def log_i(x,K=220):
 x=asiv(x);assert x.lo>1
 lo=log_positive_rational(x.lo,K);hi=log_positive_rational(x.hi,K)
 return IV(lo.lo,hi.hi)
def atan_one_over(q,N=26):
 x=F(1,q)
 s=sum((F((-1)**k)*x**(2*k+1)/(2*k+1) for k in range(N)),F(0))
 nextterm=x**(2*N+1)/F(2*N+1)
 return IV(s-nextterm,s) if N%2 else IV(s,s+nextterm)
def pi_iv():return 16*atan_one_over(5)-4*atan_one_over(239)
def gamma_iv():
 # H_N - log N - 1/(2N) < gamma < previous + 1/(12N^2).
 N=128;hn=sum((F(1,k) for k in range(1,N+1)),F(0))
 a=IV(hn)-7*log_i(F(2))-F(1,2*N)
 return IV(a.lo,a.hi+F(1,12*N*N))
def sinh_cosh_iv(x,N=25):
 assert 0<x<1
 S=sum((x**(2*k+1)/factorial(2*k+1) for k in range(N)),F(0))
 C=sum((x**(2*k)/factorial(2*k) for k in range(N)),F(0))
 snext=x**(2*N+1)/factorial(2*N+1)
 cnext=x**(2*N)/factorial(2*N)
 return (IV(S,S+snext/(1-x*x/F((2*N+2)*(2*N+3)))),
         IV(C,C+cnext/(1-x*x/F((2*N+1)*(2*N+2)))))
def corr(n,dist):
 d=dist/B
 return 1-d/2 if n==0 else 1-3*d/2+d**3/4
def prime_diagonal(n):
 ans=IV(0)
 for m,p in PRIMES:
  ell=log_i(F(m));coef=log_i(F(p))/sqrt_i(m)
  assert 0<ell.lo<=ell.hi<R
  ans=ans-2*coef*corr(n,ell)
 return ans
def pole_diagonal(n):
 sn,cs=sinh_cosh_iv(B/2)
 return F(16)/B*sn**2 if n==0 else -F(3)/B*(4*cs-8*sn/B)**2
def regular_coefficients():
 a=[]
 for n in range(194):
  val=F(1,2**(n+1)*factorial(n))
  val-=sum((a[n-k]/factorial(k+1) for k in range(2,n+1,2)),F(0))
  a.append(val)
 assert a[:3]==[F(1,2),F(1,4),-F(1,48)]
 return a[1:]
def reg_diagonal(n,coef,err):
 # C00(t)=1-t/R, C11(t)=1-3t/R+2(t/R)^3 on [0,R].
 f=(lambda k:F(1,k+1)-F(1,k+2)) if n==0 else (lambda k:F(1,k+1)-F(3,k+2)+F(2,k+4))
 val=sum((2*v*R**(k+1)*f(k) for k,v in enumerate(coef)),F(0))
 # |C00|, |C11|<=1, so kernel uniform error <=2R*err.
 return IV(val-2*R*err,val+2*R*err)
def blob_sha(raw):
 return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
def run():
 raw=(ROOT/REG_SOURCE).read_bytes()
 assert blob_sha(raw)==REG_PIN,'RC46 input blob changed'
 source=json.loads(raw)
 coef=list(map(F,source['regular_kernel_coefficients']))
 err=F(source['regular_kernel_uniform_error_upper'])
 assert len(coef)==193 and coef==regular_coefficients() and err<F(1,10**22)
 for file,pin,key in [(ORIGINAL_SOURCE,ORIGINAL_PIN,'original_CC27_Weil_polynomial_form_matches_native_model_on_all_degrees'),
                      (FREDHOLM_SOURCE,FREDHOLM_PIN,'rank301_high_complement_positive_in_both_parities')]:
  content=(ROOT/file).read_bytes()
  assert blob_sha(content)==pin,('upstream model changed',file)
  assert json.loads(content)[key]
 cr=-gamma_iv()-log_i(2*pi_iv()*R)
 results=[]
 for n in (0,1):
  prime=prime_diagonal(n);pole=pole_diagonal(n);regular=reg_diagonal(n,coef,err)
  diag=IV(n)+IV(1 if n==0 else F(4,3))+cr-regular+prime+pole
  assert diag.lo>0,('first signed diagonal not positive',n)
  assert diag.hi-diag.lo<F(1,10000)
  results.append(dict(n=n,physically_normalized_original_Weil_diagonal_interval=diag.bounds(),
    prime=prime.bounds(),regular=regular.bounds(),pole=pole.bounds(),
    J=str(F(n)),E=str(F(1) if n==0 else F(4,3))))
 assert F(results[0]['physically_normalized_original_Weil_diagonal_interval'][0])>F(4,100)
 assert F(results[1]['physically_normalized_original_Weil_diagonal_interval'][0])>F(132,1000)
 return dict(milestone='RC315',standing='original low-sector necessary check, not full Schur test',
   original_CC27_native_source_from_RC313=True,reg_source=REG_SOURCE,reg_blob_pin=REG_PIN,
   original_source_pin=ORIGINAL_PIN,fredholm_source_pin=FREDHOLM_PIN,reg_source_verified=True,
   method='exact rational outward bounds: Machin pi, Euler harmonic gamma, atanh log, hyperbolic Taylor, RC46 regular remainder',
   normalized_low_block_positive_2_by_2=True,offdiagonal_P0_P1_exactly_zero_by_parity=True,
   original_low_diagonals=results,tail_uniform=str(err),
   full_rank301_or_317_principal_block_evaluated=False,
   signed_high_response_Y_computed=False,signed_residual_Gram_computed=False,
   signed_Schur_positive_certified=False,Stage_I_closed=False,F4=False,RH=False,Lean=False,
   next_cursor='RC316: compute signed original high response and residual Gram for rank301 or better conditioned rank317; test minus-sign Schur lower witness.')
if __name__=='__main__':
 ap=argparse.ArgumentParser()
 ap.add_argument('--output',type=Path,required=True)
 ap.add_argument('--replay',action='store_true')
 a=ap.parse_args();v=run()
 if a.replay:assert v==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(v,sort_keys=True,indent=2)+'\n')
 print('RC315: signed original P0/P1 diagonal certified; Schur and Stage I OPEN')
