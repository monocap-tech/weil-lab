"""RC323 — certified high-mode witness that the global high-coercivity
floor alone CANNOT prove the full original signed P0/P2/P4 Schur block.

This is a methodological obstruction, NOT negative Schur positivity:
for the exact native original CC27/RC313 signed operator, a rational
low vector x=(3/25,-23/8,1) in the RC322 boundary-compatible basis
has a fully rigorous finite-high-mode response ||P_[244,800) T x||².
It exceeds mu_even <x,B_low x>, where mu_even is the precise pinned
RC283/314 lower bound for the full even high-complement C.

Therefore B_low-mu_even^{-1} T* T is NOT positive semidefinite,
independent of how accurately it is numerically approximated.
This does NOT establish S=B_low-T*C^{-1}T is negative; C^{-1}
can be strictly smaller than mu_even^{-1}I on relevant vectors.
RC324 must calculate actual inverse/energy-weighted covariance.

High-mode prime outputs are enclosed by FIXED-POINT rational
interval Legendre recurrence (independent from RC318-321 exact
fraction recurrence). Interval widths are propagated outward at
every recurrence step. No floating-point estimates enter.
Entire prime input log/weight uncertainty, RC46 regular remainder
and signed even pole are subtracted in the full physical norm before
squaring. Only 278 explicit high modes are needed for the no-go.
"""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from math import isqrt, comb
from fractions import Fraction as F
import validate_rpb108_rc318_p0_signed_schur as rc318
import validate_rpb108_rc319_p2_mixed_native as rc319
import validate_rpb108_rc320_boundary_cancelled_schur as rc320
import validate_rpb108_rc321_p4_boundary_native as rc321

ROOT=Path(__file__).resolve().parents[1]
FIRST=244
STOP=800
B=F(11,10)
Q=10**520
G=10**35
OUT=10**28
H2=F(3,2)
H4=F(25,12)
VEC=(F(3,25), -F(23,8), F(1))
PINS={
 "certificates/rpb108_rc46_native_archimedean_head.json":"be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9",
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc314_fredholm_schur.json":"6496be8d20176f173c0ff8b6e393b0ccd7c6ff5b",
 "certificates/rpb108_rc318_p0_signed_schur.json":"85dbc5bc373de9922bfe17a6d43ab2cef7178cd6",
 "certificates/rpb108_rc319_p2_mixed_native.json":"9c1457d405305928b02f1e546378c0dc239d63a6",
 "certificates/rpb108_rc320_boundary_cancelled_schur.json":"fe8821aaba62ba50c2a8eba1a2fa0020ba818003",
 "certificates/rpb108_rc321_p4_boundary_native.json":"26eedd29ee80063c7b8ccc5f1d5de025e7050842",
 "certificates/rpb108_rc322_low_3d_gram.json":"ba344b44436c5c2d392a9feb5c6dc0c9892dfe88",
}
def dn(x,g=OUT):
 return F(x.numerator*g//x.denominator,g)
def up(x,g=OUT):
 return F((x.numerator*g+x.denominator-1)//x.denominator,g)
def sqrtlo(x,g=G):
 assert x>0
 y=isqrt(x.numerator*g*g//x.denominator)
 assert F(y,g)**2<=x<F(y+1,g)**2
 return F(y,g)
def sqrthi(x,g=G):
 assert x>=0
 if x==0:return F(0)
 y=isqrt(x.numerator*g*g//x.denominator)
 assert F(y,g)**2<=x<F(y+1,g)**2
 return F(y+1,g)
def blob(raw):
 return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

class IV:
 def __init__(self,lo,hi=None):
  self.lo=F(lo)
  self.hi=F(lo if hi is None else hi)
  assert self.lo<=self.hi
 def __add__(self,o):
  o=iv(o);return IV(self.lo+o.lo,self.hi+o.hi)
 __radd__=__add__
 def __neg__(self):return IV(-self.hi,-self.lo)
 def __sub__(self,o):return self+-iv(o)
 def __rsub__(self,o):return iv(o)+-self
 def __mul__(self,o):
  o=iv(o)
  p=[x*y for x in (self.lo,self.hi) for y in (o.lo,o.hi)]
  return IV(min(p),max(p))
 __rmul__=__mul__
 def __truediv__(self,o):
  o=iv(o);assert o.lo*o.hi>0
  return self*IV(F(1,o.hi) if False else 1/o.hi,1/o.lo)
 def grid(self,g=G):
  return IV(dn(self.lo,g),up(self.hi,g))
 def sqrt(self):
  assert self.lo>0
  return IV(sqrtlo(self.lo),sqrthi(self.hi))
 def absmin(self):
  return F(0) if self.lo<=0<=self.hi else min(abs(self.lo),abs(self.hi))
 def arr(self):
  v=self.grid(OUT)
  return [str(v.lo),str(v.hi)]
def iv(x):return x if isinstance(x,IV) else IV(x)

def harmonics(stop):
 h=F(0);result={0:h}
 for i in range(1,stop+1):
  h+=F(1,i)
  if i>=FIRST and i%2==0:result[i]=h
 return result

def P_intervals_at_center(z,max_n):
 # This rational interval recurrence is independent of the
 # huge-numerator exact Fraction recurrence in prior scripts:
 # the value of each P_n(z) lies in the tracked rational box.
 # High precision Q=10^520 pays worst-case forward interval
 # dependency growth through degree 805.
 arr=[IV(1),IV(z).grid(Q)]
 for n in range(1,max_n):
  nxt=((2*n+1)*IV(z)*arr[-1]-n*arr[-2])/(n+1)
  nxt=nxt.grid(Q)
  arr.append(nxt)
 assert len(arr)==max_n+1
 for n in (FIRST,STOP//2,STOP):
  assert arr[n].hi-arr[n].lo<F(1,10**25),(
    "insufficient rigorous fixed-point precision",n)
  assert arr[n].lo>=-1-F(1,10**25) and arr[n].hi<=1+F(1,10**25)
 return arr

def multiplication_moments(n,pr):
 def J(k):
  assert k>0
  return (pr[k+1]-pr[k-1])/F(2*k+1)
 expansion={n:F(1)}
 moments=[J(n)]
 for i in range(1,5):
  nxt={}
  for j,c in expansion.items():
   nxt[j+1]=nxt.get(j+1,F(0))+c*F(j+1,2*j+1)
   if j:nxt[j-1]=nxt.get(j-1,F(0))+c*F(j,2*j+1)
  expansion=nxt
  moments.append(sum((a*J(k) for k,a in nxt.items()),IV(0)).grid(G))
 return moments

def translated_coefficients(rows,reverse=False):
 # A_j(n) = -(2n+1) sum c_m int_-1^(1-d_m)
 #            P_n(t) f_j(t+d_m) dt,
 # f_0=P0, f_2=P2-P0, f_4=P4-P2. All originals are SIGNED.
 output={n:[IV(0),IV(0),IV(0)] for n in range(FIRST,STOP,2)}
 for src in (list(reversed(rows)) if reverse else rows):
  z=src["z"];d=1-z;c=src["c"]
  assert -1<z<1 and 0<d<2 and c>0
  p2=[(3*d*d-3)/2,3*d,F(3,2)]
  p4=rc321.poly_shift_F(d)
  polynomials=([F(1)],p2,p4)
  pv=P_intervals_at_center(z,STOP+6)
  for n in range(FIRST,STOP,2):
   mom=multiplication_moments(n,pv)
   for k,coeff in enumerate(polynomials):
    val=sum((a*mom[j] for j,a in enumerate(coeff)),IV(0))
    output[n][k]=(output[n][k]-(2*n+1)*c*val).grid(G)
 assert len(output)==(STOP-FIRST)//2
 return output

def complete_bound(reverse=False):
 inp={}
 for p,pin in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/p).read_bytes()
  assert blob(raw)==pin,("upstream input changed",p)
  inp[p]=json.loads(raw)
 def src(k):return inp["certificates/rpb108_rc"+k+".json"]
 assert src("320_boundary_cancelled_schur")[
   "full_P0_P2_high_eliminated_Schur_2by2_positive"]
 assert src("322_low_3d_gram")["original_signed_low_P0_P2_P4_3x3_strictly_positive"]
 assert not src("322_low_3d_gram")["full_3D_Schur_positive_certified"]
 rows=rc318.source_info()
 co=translated_coefficients(rows,reverse)
 met=src("129_four_vector_joint_moment")
 slo=F(met["actual_D_Gram_entry_lower"][0][0])/(2*B)
 shi=F(met["actual_D_Gram_entry_upper"][0][0])/(2*B)
 assert 3<slo<=shi<5
 k0=(IV(slo,shi).sqrt()).__rtruediv__(IV(1)) if False else IV(1)/IV(slo,shi).sqrt()
 k2=IV(5).sqrt()/IV(slo+H2,shi+H2).sqrt()
 k4=IV(3)/IV(slo+H4,shi+H4).sqrt()
 roots=[k0,k2,k4]
 assert all(x.lo>0 for x in roots)
 h=harmonics(STOP)
 finite_lower=F(0)
 positive_modes=0
 sample=[]
 for n,amp in (reversed(list(co.items())) if reverse else co.items()):
  base=F(2*n+1)
  e0=base/F(n*(n+1))
  e2=6*base/F(n*(n+1)*(n-2)*(n+3))
  e4=14*base/F((n-4)*(n+5)*(n-2)*(n+3))
  total=sum((VEC[i]*roots[i]*(amp[i]+(e0,e2,e4)[i])
             for i in range(3)),IV(0)).grid(G)
  squared=total.absmin()**2 / (base*(shi+h[n]))
  budget=dn(squared,OUT)
  finite_lower+=budget
  if budget>0:positive_modes+=1
  if n in (244,256,284,400,570,798):
   sample.append(dict(degree=n,original_signed_combined_amplitude_interval=total.arr(),
                   D_weighted_high_mode_energy_lower=str(budget)))
 assert positive_modes>=200
 finite_lower=dn(finite_lower)
 assert finite_lower>F(1,10**8)
 # Physical source error of the ACTUAL original prime
 # output vs rational center, including shifted supports.
 # For f0, discontinuous extension incurs sqrt displacement;
 # for f2/f4 H1 cancellation makes it linear.
 e0=rc319.translation_error(rows,0)
 e2=rc320.native_transport_fault(rows)
 e4=rc321.exact_translation_fault(rows)
 # D-mode weighting is contractive on both input and output,
 # since s>3 and Hn+s>3: charge errors *without* dividing.
 transport=sum((abs(VEC[i])*v for i,v in enumerate((e0,e2,e4))),F(0))
 eps=F(src("46_native_archimedean_head")[
  "regular_kernel_uniform_error_upper"])
 # Original regular polynomial's high projections vanish
 # for all three low source directions at n>=244.
 reg=(2*B*abs(VEC[0])+5*B*(abs(VEC[1])+abs(VEC[2])))*eps
 # Original signed even pole high tail: RC316–321 valid
 # complete geometric Taylor bounds; no uncharged residue.
 pole=(32*abs(VEC[0])+128*abs(VEC[1])+256*abs(VEC[2]))*B*(B/2)**FIRST
 full_error=up(transport+reg+pole)
 assert 0<full_error<F(1,10**11)
 true_norm_low=sqrtlo(finite_lower)-full_error
 assert true_norm_low>0
 true_energy_low=dn(true_norm_low**2)
 # Upper ORIGINAL low quadratic form on the same exact
 # rational low vector, no augmented comparison used.
 low=src("322_low_3d_gram")["original_D_boundary_basis_low_entries"]
 low_quadratic=IV(0)
 for i in range(3):
  for j in range(i,3):
   interval=low[f"{i}_{j}"]
   v=IV(*map(F,interval))
   low_quadratic+=(VEC[i]*VEC[j]*(2 if i!=j else 1))*v
 assert low_quadratic.lo>0
 low_up=up(low_quadratic.hi)
 mu=F(src("322_low_3d_gram")["complete_high_coercivity_floor"])
 assert mu>0
 benchmark=mu*low_up
 gap=true_energy_low-benchmark
 # Strictly NEGATIVE Rayleigh direction for the *surrogate*
 # B - mu^{-1}T*T. Not for actual S=B-T*C^{-1}T!
 assert gap>F(1,10**10),(
    "finite signed high modes do not obstruct coarse-floor method")
 surrogate_negative_upper=low_up-true_energy_low/mu
 assert surrogate_negative_upper<0
 return dict(
  milestone="RC323",
  parent_merge="99eb1d3ce26ec10bbf612fbbd21c9fd5d46b8349",
  input_git_blob_pins=PINS,
  original_signed_CC27_D_Riesz_operator=True,
  tested_low_basis="v0, w2=(u2-sqrt5*u0)/sqrt(s+H2), w4=(u4-3/sqrt5*u2)/sqrt(s+H4)",
  rational_low_test_coordinates=[str(x) for x in VEC],
  finite_high_even_first_degree=FIRST,
  finite_high_even_last_degree=STOP-2,
  evaluated_signed_original_high_mode_count=len(co),
  certified_nonzero_high_modes=positive_modes,
  interval_legendre_recursion_fractional_grid_denominator_decimal_digits=520,
  source_logs_and_sqrt_coefficients_outward_enclosed=True,
  signed_high_mode_samples=sorted(sample,key=lambda x:x["degree"]),
  rational_center_finite_high_D_energy_lower=str(finite_lower),
  complete_original_prime_translation_error_upper=str(up(transport)),
  complete_original_regular_and_even_pole_error_upper=str(up(reg+pole)),
  complete_original_high_source_error_upper=str(full_error),
  original_actual_finite_high_D_energy_lower=str(true_energy_low),
  original_low_quadratic_B_upper=str(low_up),
  inherited_even_C_coercivity_floor_mu=str(mu),
  mu_times_low_original_B_upper=str(up(benchmark)),
  strict_finite_high_energy_excess_over_mu_B_lower=str(dn(gap)),
  original_global_floor_surrogate_rayleigh_upper=str(up(surrogate_negative_upper)),
  global_C_floor_only_3D_Loewner_Schur_method_impossible=True,
  negative_actual_Schur_direction_proved=False,
  actual_C_inverse_signed_high_covariance_computed=False,
  original_full_3D_Schur_positive=False,
  full_rank317_Schur_positive=False,
  Stage_I_closed=False,F4=False,Lean=False,RH=False,
  next_cursor=(
   "RC324: global C>=mu is provably too weak even with exact "
   "signed T on the full P0/P2/P4 span. Compute mode-sensitive "
   "C^-1 signed high response using finite original high C "
   "block and rigorously invert it with the remaining infinite "
   "tail/Schur residual paid. This certificate does NOT "
   "establish a negative actual Weil direction."
  ))
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true")
 args=p.parse_args()
 result=complete_bound(reverse=args.replay)
 if args.replay:
  assert result==json.loads(args.output.read_text(encoding="utf-8"))
 else:
  args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n",encoding="utf-8")
 print("RC323: strict no-go for global high C-floor-only 3D Schur positivity; actual signed Schur and Stage I OPEN",flush=True)
