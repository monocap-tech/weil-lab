"""RC315: rational low-sector sign check for the identified ORIGINAL CC27 Weil form.

Physically orthonormal Legendre P0/P1 (not the D-normalized vectors).
Certified first two diagonal entries only: the rank301/317 Schur gate
and the signed high response are NOT computed. All transcendental
operations have explicit rational interval enclosures.
"""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
GRID=10**12
PINS={
 "certificates/rpb108_rc46_native_archimedean_head.json":
 "be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9",
 "certificates/rpb108_rc313_prime_pole_distributions.json":
 "954b4892cf3b4e999e65476d7ce341021528d9e8",
 "certificates/rpb108_rc314_fredholm_schur.json":
 "6496be8d20176f173c0ff8b6e393b0ccd7c6ff5b",
}
PRIMES=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))

class IV:
 def __init__(self,lo,hi=None):
  self.lo=F(lo);self.hi=F(lo if hi is None else hi)
  assert self.lo<=self.hi
 def __add__(self,o):
  o=iv(o);return IV(self.lo+o.lo,self.hi+o.hi)
 __radd__=__add__
 def __neg__(self):return IV(-self.hi,-self.lo)
 def __sub__(self,o):return self+-iv(o)
 def __rsub__(self,o):return iv(o)+-self
 def __mul__(self,o):
  o=iv(o);v=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
  return IV(min(v),max(v))
 __rmul__=__mul__
 def __truediv__(self,o):
  o=iv(o);assert o.lo*o.hi>0
  return self*IV(1/o.hi,1/o.lo)
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  if n==0:return IV(1)
  if n%2==0 and self.lo<=0<=self.hi:
   return IV(0,max(abs(self.lo),abs(self.hi))**n)
  v=[self.lo**n,self.hi**n]
  return IV(min(v),max(v))
 def bounds(self):
  return [str(F(self.lo.numerator*GRID//self.lo.denominator,GRID)),
   str(F((self.hi.numerator*GRID+self.hi.denominator-1)//self.hi.denominator,GRID))]

def iv(x):return x if isinstance(x,IV) else IV(x)

def sqrt_i(n):
 scale=10**35;t=isqrt(n*scale*scale)
 return IV(F(t,scale),F(t+1,scale))

def log_positive_rational(x,K=220):
 assert x>1
 t=(x-1)/(x+1)
 s=sum((2*t**(2*k+1)/F(2*k+1) for k in range(K)),F(0))
 tail=2*t**(2*K+1)/(F(2*K+1)*(1-t*t))
 return IV(s,s+tail)

def log_i(x):
 x=iv(x);assert x.lo>1
 a=log_positive_rational(x.lo);b=log_positive_rational(x.hi)
 return IV(a.lo,b.hi)

def atan_reciprocal(q,N=26):
 x=F(1,q)
 s=sum((F((-1)**k)*x**(2*k+1)/F(2*k+1)
        for k in range(N)),F(0))
 rem=x**(2*N+1)/F(2*N+1)
 return IV(s-rem,s) if N%2 else IV(s,s+rem)

def pi_iv():
 # Exact Machin identity, with alternating-series remainder.
 return 16*atan_reciprocal(5)-4*atan_reciprocal(239)

def gamma_iv():
 # H_N - log N - 1/(2N) < gamma
 # < H_N - log N - 1/(2N) + 1/(12N^2).
 N=128
 hn=sum((F(1,k) for k in range(1,N+1)),F(0))
 a=iv(hn)-7*log_i(F(2))-F(1,2*N)
 return IV(a.lo,a.hi+F(1,12*N*N))

def sinh_cosh_iv(x,N=25):
 assert F(0)<x<1
 S=sum((x**(2*k+1)/factorial(2*k+1) for k in range(N)),F(0))
 C=sum((x**(2*k)/factorial(2*k) for k in range(N)),F(0))
 snext=x**(2*N+1)/factorial(2*N+1)
 cnext=x**(2*N)/factorial(2*N)
 stail=snext/(1-x*x/F((2*N+2)*(2*N+3)))
 ctail=cnext/(1-x*x/F((2*N+1)*(2*N+2)))
 return IV(S,S+stail),IV(C,C+ctail)

def prime_correlation(n,ell):
 d=ell/B
 if n==0:return 1-d/2
 assert n==1
 return 1-3*d/2+d**3/4

def prime_diagonal(n,reverse=False):
 val=iv(0)
 for m,p in (reversed(PRIMES) if reverse else PRIMES):
  ell=log_i(F(m));c=log_i(F(p))/sqrt_i(m)
  assert 0<ell.lo<=ell.hi<R
  val=val-2*c*prime_correlation(n,ell)
 return val

def pole_diagonal(n):
 sn,ch=sinh_cosh_iv(B/2)
 if n==0:return F(16)/B*sn**2
 assert n==1
 return -F(3)/B*(4*ch-8*sn/B)**2

def independent_regular_coefficients():
 # Recurrence for e^(-t/2)/(1-e^(-2t)) - 1/(2t).
 a=[]
 for n in range(194):
  val=F(1,2**(n+1)*factorial(n))
  val-=sum((a[n-k]/factorial(k+1)
            for k in range(2,n+1,2)),F(0))
  a.append(val)
 assert a[:3]==[F(1,2),F(1,4),-F(1,48)]
 return a[1:]

def regular_diagonal(n,coef,err,reverse=False):
 # Normalized positive-displacement autocorrelations:
 # C00(t)=1-t/R, C11(t)=1-3t/R+2(t/R)^3.
 if n==0:
  moment=lambda k:F(1,k+1)-F(1,k+2)
 else:
  assert n==1
  moment=lambda k:F(1,k+1)-F(3,k+2)+F(2,k+4)
 pairs=list(enumerate(coef))
 if reverse:pairs.reverse()
 val=sum((2*c*R**(k+1)*moment(k) for k,c in pairs),F(0))
 # Bound |C_nn(t)|<=1 by shift contraction; pay both directions.
 return IV(val-2*R*err,val+2*R*err)

def pin_sha(raw):
 return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def run(reverse=False):
 source={}
 for path,sha in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes()
  assert pin_sha(raw)==sha,("source blob changed",path)
  source[path]=json.loads(raw)
 def src(k):return source["certificates/rpb108_rc"+k+".json"]
 assert src("313_prime_pole_distributions")[
   "original_CC27_Weil_polynomial_form_matches_native_model_on_all_degrees"]
 assert src("314_fredholm_schur")["rank301_high_complement_positive_in_both_parities"]
 reg=src("46_native_archimedean_head")
 coef=list(map(F,reg["regular_kernel_coefficients"]))
 err=F(reg["regular_kernel_uniform_error_upper"])
 assert coef==independent_regular_coefficients()
 assert len(coef)==193 and 0<err<F(1,10**22)
 g=gamma_iv();pi=pi_iv()
 # RC312 original supported archimedean constant, WITHOUT
 # an additional log2 or Poisson remainder.
 cr=-g-log_i(2*pi*R)
 out=[]
 for n in (0,1):
  # J(P_n)=H_n P_n; <W_B>_u0=1, <W_B>_u1=4/3.
  j=F(n)
  wb=F(1) if n==0 else F(4,3)
  prime=prime_diagonal(n,reverse)
  regular=regular_diagonal(n,coef,err,reverse)
  pole=pole_diagonal(n)
  diagonal=iv(j+wb)+cr-regular+prime+pole
  assert diagonal.lo>0,("necessary original diagonal fails",n)
  assert diagonal.hi-diagonal.lo<F(1,10000)
  out.append(dict(n=n,J=str(j),W_B=str(wb),
    physically_normalized_original_Weil_diagonal_interval=diagonal.bounds(),
    prime=prime.bounds(),regular=regular.bounds(),pole=pole.bounds()))
 assert F(out[0]["physically_normalized_original_Weil_diagonal_interval"][0])>F(4,100)
 assert F(out[1]["physically_normalized_original_Weil_diagonal_interval"][0])>F(13,100)
 return dict(
  milestone="RC315",standing="Original signed low-sector necessary check, not a Schur witness",
  source_blob_pins=PINS,
  arithmetic="outward rational intervals: atanh, Machin pi, harmonic Euler gamma, hyperbolic Taylor, RC46 analytic uniform remainder",
  original_cc27_operator_identification_imported_RC313=True,
  even_odd_low_mixed_entry_zero_exactly_by_reflection=True,
  normalized_P0_P1_original_principal_block_strictly_positive=True,
  original_low_diagonals=out,
  regular_uniform_error_upper=str(err),
  finite_rank301_or_317_Schur_matrix_computed=False,
  signed_high_response_Y_computed=False,
  residual_Gram_computed=False,
  signed_full_positivity_proved=False,
  Stage_I_closed=False,F4=False,RH=False,Lean=False,
  next_cursor="RC316: certify at least one nonzero cross-block original T=QN0P coefficient, then build rank317 high response Y and paid residual Gram with MINUS Schur correction. Full original positivity remains open.")

if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true")
 a=p.parse_args()
 result=run(reverse=a.replay)
 if a.replay:
  assert result==json.loads(a.output.read_text(encoding="utf-8"))
 else:
  a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n",encoding="utf-8")
 print("RC315: positive original P0/P1 principal diagonal, NOT a full Schur or Stage I certificate",flush=True)
