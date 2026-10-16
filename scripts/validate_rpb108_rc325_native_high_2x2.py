"""RC325. Certified original signed high-high block degrees 244/246 and
a coupled rational Ritz trial on RC323's almost-null low witness.

All original seven-prime translated Legendre *overlap integrals* are
computed in exact rational arithmetic at rigorously enclosed log
centers. Leibniz/Markov bounds pay moving support and coefficient
errors. The endpoint, scalar, RC324 operator regular remainder and
signed even pole are explicitly included. The actual 2x2 ORIGINAL
high matrix is positive definite and a nonzero 2-mode Ritz trial
improves even the OPTIMAL single-244-mode trial. This is an UPPER
bound on the actual Schur form, not a full C^-1 or positive lower
Schur bound. Stage I/F4/Lean/RH remain OPEN.
"""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
from math import comb,isqrt
import validate_rpb108_rc318_p0_signed_schur as rc318
import validate_rpb108_rc321_p4_boundary_native as rc321
import validate_rpb108_rc323_coercivity_nogo as rc323
import validate_rpb108_rc324_high_tail_smoothing as rc324

ROOT=Path(__file__).resolve().parents[1];B=F(11,10)
N=(244,246);G=10**25;CG=10**12
PINS={
 "certificates/rpb108_rc46_native_archimedean_head.json":"be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9",
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc313_prime_pole_distributions.json":"954b4892cf3b4e999e65476d7ce341021528d9e8",
 "certificates/rpb108_rc314_fredholm_schur.json":"6496be8d20176f173c0ff8b6e393b0ccd7c6ff5b",
 "certificates/rpb108_rc322_low_3d_gram.json":"ba344b44436c5c2d392a9feb5c6dc0c9892dfe88",
 "certificates/rpb108_rc323_coercivity_nogo.json":"3280e450654675c09292be902a8888e69c9a75ce",
 "certificates/rpb108_rc324_high_tail_smoothing.json":"33f73683424d6408a35aeced0bb205bdb7215686"
}
def dn(x,g=G):return F(x.numerator*g//x.denominator,g)
def up(x,g=G):return F((x.numerator*g+x.denominator-1)//x.denominator,g)
def nearest(x,g=CG):return F((2*x.numerator*g+x.denominator)//(2*x.denominator),g)
def root(x,upper=False,g=10**32):
 assert x>=0
 k=isqrt(x.numerator*g*g//x.denominator)
 assert F(k,g)**2<=x<F(k+1,g)**2
 return F(k+(1 if upper and x else 0),g)
def blob(b):return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
class IV:
 def __init__(self,l,h=None):self.l=F(l);self.h=F(l if h is None else h);assert self.l<=self.h
 def __add__(self,o):
  o=iv(o);return IV(self.l+o.l,self.h+o.h)
 __radd__=__add__
 def __neg__(self):return IV(-self.h,-self.l)
 def __sub__(self,o):return self+-iv(o)
 def __mul__(self,o):
  o=iv(o);q=[a*b for a in (self.l,self.h) for b in (o.l,o.h)]
  return IV(min(q),max(q))
 __rmul__=__mul__
 def __truediv__(self,o):
  o=iv(o);assert o.l>0
  return self*IV(1/o.h,1/o.l)
 def sqrt(self):return IV(root(self.l),root(self.h,True))
 def sq(self):
  if self.l>0:return IV(self.l*self.l,self.h*self.h)
  if self.h<0:return IV(self.h*self.h,self.l*self.l)
  return IV(0,max(self.l*self.l,self.h*self.h))
 def out(self):return [str(dn(self.l)),str(up(self.h))]
def iv(o):return o if isinstance(o,IV) else IV(o)
def legendre(n):
 a=[F(1)];b=[F(0),F(1)]
 for k in range(1,n):
  v=[F(0)]*(k+2)
  for j,x in enumerate(b):v[j+1]+=(2*k+1)*x
  for j,x in enumerate(a):v[j]-=k*x
  a,b=b,[x/F(k+1) for x in v]
 return b
def overlap(a,b,d):
 """Exact \int_{-1}^{1-d} P_i(t) P_j(t+d) dt."""
 pw=[F(1)]
 for _ in range(1,len(b)):pw.append(pw[-1]*d)
 shifted=[F(0)]*len(b)
 for k,x in enumerate(b):
  if x:
   for j in range(k+1):shifted[j]+=x*comb(k,j)*pw[k-j]
 coeff=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(shifted):
    if y:coeff[i+j]+=x*y
 z=1-d;h=F(0)
 for k in range(len(coeff)-1,-1,-1):h=h*z+coeff[k]/F(k+1)
 result=z*h-sum((x*F((-1)**(i+1),i+1) for i,x in enumerate(coeff)),F(0))
 assert -2<=result<=2
 return result
def primes(rows,reverse):
 pol={n:legendre(n) for n in N};D={}
 for n,m in ((244,244),(244,246),(246,246)):
  center=F(0);err=F(0)
  for r in (list(reversed(rows)) if reverse else rows):
   a,b=r["el"]/B,r["eu"]/B;d=nearest((a+b)/2)
   assert 0<a<=d<=b<2
   I=overlap(pol[n],pol[m],d)
   delta=max(abs(a-d),abs(b-d))
   # Leibniz + Markov: |I'|<=1+m(m+1). |I|<=2.
   err+=r["ch"]*(1+m*(m+1))*delta+2*r["cradius"]
   center-=r["c"]*I
  D[n,m]=IV(dn(center-err),up(center+err))
 return D
def low_to_high(rows,slo,shi,err,reverse):
 results={}
 hh=rc324.Htable(246)
 k0=IV(1)/IV(slo,shi).sqrt()
 k2=IV(5).sqrt()/IV(slo+F(3,2),shi+F(3,2)).sqrt()
 k4=IV(3)/IV(slo+F(25,12),shi+F(25,12)).sqrt()
 weights=(F(3,25)*k0,-F(23,8)*k2,k4)
 for n in N:
  A=[rc323.IV(0),rc323.IV(0),rc323.IV(0)]
  for r in (list(reversed(rows)) if reverse else rows):
   z=r["z"];d=1-z
   p=([F(1)],[(3*d*d-3)/2,3*d,F(3,2)],rc321.poly_shift_F(d))
   vals=rc323.P_intervals_at_center(z,252)
   mom=rc323.multiplication_moments(n,vals)
   for i,cs in enumerate(p):
    val=sum((cs[j]*mom[j] for j in range(len(cs))),rc323.IV(0))
    A[i]=(A[i]-(2*n+1)*r["c"]*val).grid(10**35)
  L=2*n+1
  e=(F(L,n*(n+1)),F(6*L,n*(n+1)*(n-2)*(n+3)),
     F(14*L,(n-4)*(n+5)*(n-2)*(n+3)))
  top=sum((weights[i]*(IV(A[i].lo,A[i].hi)+e[i]) for i in range(3)),IV(0))
  den=IV(L*(hh[n]+slo),L*(hh[n]+shi)).sqrt()
  val=top/den
  results[n]=IV(dn(val.l-err),up(val.h+err))
 return results
def run(reverse=False):
 docs={}
 for p,pin in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/p).read_bytes();assert blob(raw)==pin,p
  docs[p]=json.loads(raw)
 def cert(k):return docs["certificates/rpb108_rc"+k+".json"]
 assert cert("323_coercivity_nogo")["global_C_floor_only_3D_Loewner_Schur_method_impossible"]
 assert cert("324_high_tail_smoothing")["original_even_far_high_D_floor_strict_positive"]
 rows=rc318.source_info();prime=primes(rows,reverse)
 met=cert("129_four_vector_joint_moment");slo=F(met["actual_D_Gram_entry_lower"][0][0])/(2*B)
 shi=F(met["actual_D_Gram_entry_upper"][0][0])/(2*B)
 cLo,cHi=rc324.scalar_original(cert("322_low_3d_gram")["refined_Euler_Maclaurin_gamma"])
 hh=rc324.Htable(492)
 reg=F(cert("324_high_tail_smoothing")["original_high_regular_operator_norm_bound_244plus"])
 C={}
 for i,j in ((244,244),(244,246),(246,246)):
  if i==j:
   W=2*(hh[2*i]-hh[i])+F(1,2*i+1)
   term=(IV(hh[i]+W)+IV(cLo,cHi))/(2*i+1)
  else:term=IV(F(1,(j-i)*(i+j+1)))
  term+=prime[i,j]+IV(-reg,reg)
  pole=100*B*(B/2)**(i+j)
  if i==j:term+=IV(0,pole/F(2*i+1))
  else:term+=IV(-pole,pole)/IV((2*i+1)*(2*j+1)).sqrt()
  factor=IV((2*i+1)*(2*j+1)).sqrt()/(
     IV(hh[i]+slo,hh[i]+shi)*IV(hh[j]+slo,hh[j]+shi)).sqrt()
  x=term*factor;C[i,j]=IV(dn(x.l),up(x.h))
 a,t,d=C[244,244],C[244,246],C[246,246]
 det=a*d-t.sq()
 assert a.l>0 and d.l>0 and det.l>F(1,100)
 check={x["n"]:x for x in cert("324_high_tail_smoothing")[
  "selected_original_high_even_diagonal_enclosures"]}
 for n,c in ((244,a),(246,d)):
  assert F(check[n]["original_CC27_N0_high_diagonal_lower"])<=c.l
  assert c.h<=F(check[n]["original_CC27_N0_high_diagonal_upper"])
 err=F(cert("323_coercivity_nogo")["complete_original_high_source_error_upper"])
 b=low_to_high(rows,slo,shi,err,reverse)
 assert b[244].l>0 and b[246].h<0
 aa=(a.l+a.h)/2;tt=(t.l+t.h)/2;dd=(d.l+d.h)/2
 u=(b[244].l+b[244].h)/2;v=(b[246].l+b[246].h)/2
 den=aa*dd-tt*tt;assert den>0
 y0=nearest((dd*u-tt*v)/den,10**15)
 y1=nearest((aa*v-tt*u)/den,10**15)
 assert y0>0 and y1<0
 gain=2*(y0*b[244]+y1*b[246])-y0*y0*a-2*y0*y1*t-y1*y1*d
 assert gain.l>0
 optimal_one_upper=b[244].sq().h/a.l
 strict_gain=gain.l-optimal_one_upper
 assert strict_gain>F(1,10**12)
 Bxx=F(cert("323_coercivity_nogo")["original_low_quadratic_B_upper"])
 return dict(
  milestone="RC325",parent_route_head="3022b035ef24658abefc1d192bf36db822b3329a",
  input_git_blob_pins=PINS,original_CC27_signed_Weil_operator=True,
  original_native_high_degrees=list(N),
  exact_rational_center_prime_translation_overlap_integrals=21,
  original_log_and_prime_coefficient_uncertainties_fully_paid=True,
  native_regular_high_kernel_compression_error_paid=True,
  original_native_C_2by2_intervals={f"{i}_{j}":C[i,j].out()
    for i,j in ((244,244),(244,246),(246,246))},
  original_C_2by2_determinant_strict_lower=str(dn(det.l)),
  original_high_C_244_246_2by2_strict_positive=True,
  low_R323_witness_native_high_response={str(n):b[n].out() for n in N},
  explicit_original_high_rational_2mode_Ritz_trial=[str(y0),str(y1)],
  strict_original_2mode_Schur_upper_contraction_lower=str(dn(gain.l)),
  optimal_original_1mode244_Schur_upper_contraction_upper=str(up(optimal_one_upper)),
  certified_strict_extra_coupled_gain_over_optimal_single_mode_lower=str(dn(strict_gain)),
  original_witness_Schur_Ritz_upper=str(up(Bxx-gain.l)),
  actual_full_high_C_inverse_computed=False,
  full_signed_3D_Schur_positive=False,full_high_residual_paid=False,
  full_278_mode_high_head_certified=False,head_to_far_tail_action_paid=False,
  Stage_I_closed=False,F4=False,Lean=False,RH=False,
  next_cursor="RC326: expand original signed finite high compression and certify head-to-tail coupling. This 2-mode original inverse is only a finite Ritz trial: full T-CY residual is uncomputed; full high C inverse and positive full 3D Schur remain open."
 )
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true");a=p.parse_args()
 v=run(reverse=a.replay)
 if a.replay:assert v==json.loads(a.output.read_text(encoding="utf-8"))
 else:a.output.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n",encoding="utf-8")
 print("RC325 PASS: genuine original high 244/246 block positive; coupled Ritz strictly improves optimal one-mode; complete inverse/Stage I OPEN")
