"""RC322: native signed P0/P2/P4 low Gram, three-mode Schur audit.

All original CC27/RC313 terms are recomputed: J, Legendre endpoint,
scalar with rigorous Euler-Maclaurin gamma refinement, original prime
polynomial overlaps, RC46 regular convolution and signed even pole.
Exact rational calculations plus rigorous outward intervals. The
positive *low* 3x3 block is explicitly distinguished from the
high-eliminated 3x3 Schur operator (which remains open unless
its mixed covariance is sufficiently paid).
"""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial,isqrt
import validate_rpb108_rc315_low_mode_sign as rc315
import validate_rpb108_rc318_p0_signed_schur as rc318
import validate_rpb108_rc319_p2_mixed_native as rc319
import validate_rpb108_rc321_p4_boundary_native as rc321

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10);N=(0,2,4);G=10**26
LEG={0:[F(1)],2:[F(-1,2),F(0),F(3,2)],
     4:[F(3,8),F(0),F(-30,8),F(0),F(35,8)]}
PINS={
 "certificates/rpb108_rc46_native_archimedean_head.json":"be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9",
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc313_prime_pole_distributions.json":"954b4892cf3b4e999e65476d7ce341021528d9e8",
 "certificates/rpb108_rc314_fredholm_schur.json":"6496be8d20176f173c0ff8b6e393b0ccd7c6ff5b",
 "certificates/rpb108_rc315_low_mode_sign.json":"a8cd974c8218e18943dda0082f48cca36a3350a8",
 "certificates/rpb108_rc318_p0_signed_schur.json":"85dbc5bc373de9922bfe17a6d43ab2cef7178cd6",
 "certificates/rpb108_rc319_p2_mixed_native.json":"9c1457d405305928b02f1e546378c0dc239d63a6",
 "certificates/rpb108_rc320_boundary_cancelled_schur.json":"fe8821aaba62ba50c2a8eba1a2fa0020ba818003",
 "certificates/rpb108_rc321_p4_boundary_native.json":"26eedd29ee80063c7b8ccc5f1d5de025e7050842",
}
def dn(x,g=G):return F(x.numerator*g//x.denominator,g)
def up(x,g=G):return F((x.numerator*g+x.denominator-1)//x.denominator,g)
def sl(x):
 assert x>0
 g=10**32;t=isqrt(x.numerator*g*g//x.denominator)
 assert F(t,g)**2<=x<F(t+1,g)**2
 return F(t,g)
def sh(x):
 assert x>=0
 if x==0:return F(0)
 g=10**32;t=isqrt(x.numerator*g*g//x.denominator)
 assert F(t,g)**2<=x<F(t+1,g)**2
 return F(t+1,g)
def blob(x):return hashlib.sha1(b"blob "+str(len(x)).encode()+b"\0"+x).hexdigest()
class IV:
 def __init__(self,l,h=None):
  self.l=F(l);self.h=F(l if h is None else h)
  assert self.l<=self.h
 def __add__(self,o):
  o=iv(o);return IV(self.l+o.l,self.h+o.h)
 __radd__=__add__
 def __neg__(self):return IV(-self.h,-self.l)
 def __sub__(self,o):return self+-iv(o)
 def __rsub__(self,o):return iv(o)+-self
 def __mul__(self,o):
  o=iv(o);q=[a*b for a in (self.l,self.h) for b in (o.l,o.h)]
  return IV(min(q),max(q))
 __rmul__=__mul__
 def __truediv__(self,o):
  o=iv(o);assert o.l*o.h>0
  return self*IV(1/o.h,1/o.l)
 def sq(self):
  if self.l>=0:return IV(self.l*self.l,self.h*self.h)
  if self.h<=0:return IV(self.h*self.h,self.l*self.l)
  return IV(0,max(self.l*self.l,self.h*self.h))
 def sqrt(self):
  assert self.l>0
  return IV(sl(self.l),sh(self.h))
 def clip(self):return IV(dn(self.l),up(self.h))
 def out(self):
  x=self.clip();return [str(x.l),str(x.h)]
def iv(x):return x if isinstance(x,IV) else IV(x)
def H(n):return sum((F(1,k) for k in range(1,n+1)),F(0))
def scalar():
 # Euler-Maclaurin alternating error: N=128,
 # H_N-lnN-1/(2N)+1/(12N^2)-1/(120N^4)
 # <=gamma<=H_N-lnN-1/(2N)+1/(12N^2).
 n=128
 a,b=rc318.log_bounds(2)
 base=H(n)-F(1,2*n)+F(1,12*n*n)
 gl=base-7*b-F(1,120*n**4); gh=base-7*a
 assert 0<gh-gl<F(1,10**9)
 old=rc315.gamma_iv();assert old.lo<=gl<=gh<=old.hi
 L=rc315.log_i(2*rc315.pi_iv()*rc315.R)
 return (IV(-gh-L.hi,-gl-L.lo).clip(),IV(gl,gh).clip())
def mul(a,b):
 o=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):o[i+j]+=x*y
 return o
def shift(p,d):
 o=[F(0)]*len(p)
 for j,x in enumerate(p):
  for k in range(j+1):o[k]+=x*comb(j,k)*d**(j-k)
 return o
def corr(i,j):
 # Cij(r)= int_-1^(1-r) Pi(t)Pj(t+r)dt, even symmetry.
 o=[F(0)]*(i+j+2)
 for a,x in enumerate(LEG[i]):
  for b,y in enumerate(LEG[j]):
   for k in range(b+1):
    z=x*y*comb(b,k)/F(a+k+1)
    for h in range(a+k+2):
     o[b-k+h]+=z*comb(a+k+1,h)*(-1)**h
    o[b-k]-=z*(-1)**(a+k+1)
 while o and o[-1]==0:o.pop()
 return o
def regular_exact(coeff):
 r={}
 for i in N:
  for j in N:
   if i>j:continue
   cs=corr(i,j)
   assert cs==corr(j,i)
   if (i,j)==(0,0):assert cs==[F(2),F(-1)]
   if (i,j)==(0,2):assert cs==[F(0),-F(1),F(3,2),-F(1,2)]
   if (i,j)==(2,2):assert cs==[F(2,5),-F(1),F(0),F(1,2),F(0),-F(3,40)]
   val=F(0)
   for k,c in enumerate(coeff):
    moment=sum((x*2**(k+h+1)/F(k+h+1) for h,x in enumerate(cs)),F(0))
    val+=B**(k+1)*c*moment
   r[i,j]=dn(val,10**42)
 return r
def primes(rows,reverse):
 r={}
 for i in N:
  for j in N:
   if i>j:continue
   val=F(0)
   for x in (list(reversed(rows)) if reverse else rows):
    d=(x["el"]+x["eu"])/(2*B);z=1-d
    p=rc319.integ(mul(LEG[i],shift(LEG[j],d)),-1,z)
    q=rc319.integ(mul(LEG[j],shift(LEG[i],d)),-1,z)
    assert p==q,("native original even prime adjointness",i,j)
    val-=x["c"]*p
   r[i,j]=dn(val,10**42)
 return r
def pole():
 z=B/2;K=42
 rem=F(2)*z**(2*K)/factorial(2*K)/(1-z*z/F((2*K+1)*(2*K+2)))
 assert 0<rem<F(1,10**90)
 m={}
 for i in N:
  v=sum((z**(2*k)/factorial(2*k)*
    sum((F(2)*c/F(2*k+h+1) for h,c in enumerate(LEG[i]) if h%2==0),F(0))
    for k in range(K)),F(0))
  m[i]=IV(v-rem,v+rem).clip()
  assert m[i].l>0
 return m
def determinant(a):
 x,y,z=a[0];_,w,p=a[1];_,_,q=a[2]
 return x*w*q+2*y*z*p-x*p.sq()-w*z.sq()-q*y.sq()
def run(reverse=False):
 docs={}
 for p,pin in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/p).read_bytes();assert blob(raw)==pin,p
  docs[p]=json.loads(raw)
 def get(k):return docs["certificates/rpb108_rc"+k+".json"]
 assert get("313_prime_pole_distributions")[
  "original_CC27_Weil_polynomial_form_matches_native_model_on_all_degrees"]
 assert get("320_boundary_cancelled_schur")[
  "full_P0_P2_high_eliminated_Schur_2by2_positive"]
 assert get("321_p4_boundary_native")[
  "original_P4_P2_boundary_cancellation_complete_native_source"]
 coef=list(map(F,get("46_native_archimedean_head")[
    "regular_kernel_coefficients"]))
 epsreg=F(get("46_native_archimedean_head")[
    "regular_kernel_uniform_error_upper"])
 assert len(coef)==193
 reg=regular_exact(coef);rows=rc318.source_info()
 prime=primes(rows,reverse);pm=pole()
 eps0=rc319.translation_error(rows,0)
 eps2=rc319.translation_error(rows,2)
 eps4=rc321.exact_translation_fault(rows)+2*eps2
 emax=max(eps0,eps2,eps4)
 assert emax<F(1,10**14)
 cr,gamma=scalar()
 hh={i:H(i) for i in range(9)}
 m={}
 for i in N:
  for j in N:
   if j<i:continue
   if i==j:
    endpoint=2*(hh[2*i]-hh[i])+F(1,2*i+1)
    base=(IV(hh[i]+endpoint)+cr)/F(2*i+1)
   else:base=IV(F(1,(j-i)*(i+j+1)))
   regular=IV(reg[i,j]-2*B*epsreg,reg[i,j]+2*B*epsreg)
   prime_iv=IV(prime[i,j]-emax,prime[i,j]+emax)
   m[i,j]=(base-regular+prime_iv+B*pm[i]*pm[j]).clip()
 old0=next(x for x in get("315_low_mode_sign")["original_low_diagonals"] if x["n"]==0)
 old0iv=IV(*map(F,old0["physically_normalized_original_Weil_diagonal_interval"]))
 assert old0iv.l<=m[0,0].l<=m[0,0].h<=old0iv.h
 old=get("319_p2_mixed_native")
 old02=IV(*map(F,old["original_P0_P2_physical_offdiagonal_div_sqrt5"]))
 old22=IV(*map(F,old["original_P0_P2_physical_low_diagonal_P2"]))
 assert m[0,2].l<=old02.h and old02.l<=m[0,2].h
 assert (5*m[2,2]).l<=old22.h and old22.l<=(5*m[2,2]).h
 low=[[m[0,0],m[0,2],m[0,4]],
      [m[0,2],m[2,2],m[2,4]],
      [m[0,4],m[2,4],m[4,4]]]
 minor2=low[0][0]*low[1][1]-low[0][1].sq()
 minor3=determinant(low)
 assert low[0][0].l>0 and minor2.l>0 and minor3.l>0
 met=get("129_four_vector_joint_moment")
 s=IV(F(met["actual_D_Gram_entry_lower"][0][0])/(2*B),
      F(met["actual_D_Gram_entry_upper"][0][0])/(2*B))
 assert 3<s.l<=s.h<5
 a,b,c=m[0,0],m[0,2],m[0,4]
 d,e,f=m[2,2],m[2,4],m[4,4]
 B00=a/s
 B02=IV(5).sqrt()*(b-a)/(s*(s+hh[2])).sqrt()
 B04=3*(c-b)/(s*(s+hh[4])).sqrt()
 B22=5*(d-2*b+a)/(s+hh[2])
 B24=IV(45).sqrt()*(e-d-c+b)/((s+hh[2])*(s+hh[4])).sqrt()
 B44=9*(f-2*e+d)/(s+hh[4])
 bb=[[B00.clip(),B02.clip(),B04.clip()],
     [B02.clip(),B22.clip(),B24.clip()],
     [B04.clip(),B24.clip(),B44.clip()]]
 detB=determinant(bb)
 assert detB.l>0
 # A 2D SCHUR positive block is inherited from RC320.
 # The third source has a complete high norm RC321, but
 # only C>=mu and Cauchy bounds its unresolved inverse
 # cross-covariance. Test transparently, never assume.
 t0=sh(F(get("318_p0_signed_schur")[
   "complete_even_D_high_source_Tv0_norm_squared_upper"]))
 t2=F(get("320_boundary_cancelled_schur")[
   "entire_original_boundary_cancelled_D_high_response_norm_upper"])
 t4=F(get("321_p4_boundary_native")[
   "full_original_D_high_source_norm_upper"])
 mu=F(get("314_fredholm_schur")[
   "buffered_rank317_high_complement_D_floor_lower"])
 assert mu>0
 ts=[t0,t2,t4]
 def corrected(i,j):
  q=ts[i]*ts[j]/mu;v=bb[i][j]
  return IV(v.l-q,v.h+(q if i!=j else 0)).clip()
 S44=corrected(2,2)
 S04=corrected(0,2);S24=corrected(1,2)
 S00=IV(F(get("320_boundary_cancelled_schur")[
  "inherited_original_S00_positive_lower"]),bb[0][0].h)
 S22=IV(F(get("320_boundary_cancelled_schur")[
  "rigorous_full_even_Sww_schur_diagonal_lower"]),bb[1][1].h)
 det2=F(get("320_boundary_cancelled_schur")[
  "certified_full_even_two_by_two_schur_determinant_lower"])
 off2=F(get("320_boundary_cancelled_schur")[
  "rigorous_full_even_S0w_offdiagonal_abs_upper"])
 a04=max(abs(S04.l),abs(S04.h))
 a24=max(abs(S24.l),abs(S24.h))
 # Actual third determinant >= det(S_old2) S44 -
 # S00*S24²-S22*S04²+2*S02*S04*S24.
 # Use inherited positive TWO-D determinant lower.
 det3bound=(det2*S44.l-S00.h*a24*a24-S22.h*a04*a04
            -2*off2*a04*a24)
 result=dict(
  milestone="RC322",
  parent_route_head="b31d610c6b1927fb94be78d8909dba8800636361",
  pinned_git_blobs=PINS,
  original_signed_CC27_low_gram=True,
  refined_Euler_Maclaurin_gamma=[str(gamma.l),str(gamma.h)],
  all_original_3x3_low_scaled_M_entries={
    f"{i}_{j}":m[i,j].out() for i in N for j in N if j>=i},
  original_low_M_2x2_principal_minor_lower=str(dn(minor2.l)),
  original_low_M_3x3_determinant_lower=str(dn(minor3.l)),
  original_signed_low_P0_P2_P4_3x3_strictly_positive=True,
  D_normalized_boundary_basis="v0, w2=(u2-sqrt5*u0)/sqrt(s+H2), w4=(u4-3/sqrt5*u2)/sqrt(s+H4)",
  original_D_boundary_basis_low_entries={
    f"{i}_{j}":bb[i][j].out() for i in range(3) for j in range(i,3)},
  original_D_low_3x3_determinant_lower=str(dn(detB.l)),
  inherited_full_2D_Schur_determinant_lower=str(det2),
  complete_native_high_T_norm_bounds=[str(t) for t in ts],
  complete_high_coercivity_floor=str(mu),
  conservative_Schur_S44_lower=str(dn(S44.l)),
  conservative_Schur_S04_abs_upper=str(up(a04)),
  conservative_Schur_S24_abs_upper=str(up(a24)),
  conservative_full_3D_Schur_determinant_lower_test=str(dn(det3bound)),
  full_3D_Schur_positive_certified=bool(det3bound>0 and S44.l>0),
  other_119_even_low_coordinates_not_certified=True,
  odd_195_low_coordinates_not_certified=True,
  full_rank317_Schur_positive=False,Stage_I_closed=False,
  F4=False,Lean=False,RH=False,
  next_cursor="RC323: replace coarse C^-1 covariance bounds in 3D Schur determinant with signed native mode-resolved high response, then pass the genuinely high-eliminated 3D gate. Low 3x3 positivity does not suffice."
 )
 return result
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true");a=p.parse_args()
 d=run(reverse=a.replay)
 if a.replay:assert d==json.loads(a.output.read_text(encoding="utf-8"))
 else:a.output.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n",encoding="utf-8")
 print("RC322: certified original low signed 3D Gram; high-eliminated 3D gate measured separately; Stage I OPEN",flush=True)
