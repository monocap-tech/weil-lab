"""RC320: boundary-cancelled ORIGINAL signed P0/P2 Schur 2x2.

Let u_n=sqrt((2n+1)/(2B))P_n(x/B) be physical-L2 orthonormal;
D_n=H_n+s, v_n=u_n/sqrt(D_n), s>3.

On the even rank317 reference take the independent low pair
 v0, w=v2-alpha*v0, alpha=sqrt(5*s/(s+3/2)).
Thus w=(u2-sqrt(5)u0)/sqrt(s+3/2), whose physical polynomial
is proportional to P2-1 = 3/2(t^2-1). Its boundary values VANISH.

The 14 original signed zero-extended prime translations on this
boundary-cancelled source are continuous at every shifted endpoint,
so moving a prime boundary costs O(|delta|), not O(sqrt|delta|).
Evaluate 256 exact rational-center prime coefficients and the full
physical source norm of all 15 overlapping polynomial segments;
use Parseval for the entire n>=512 remainder and pay ALL source
uncertainty, endpoint, RC46 regular, and pole terms.

The resulting full-high norm of T(w) and RC318's full-high norm of
T(v0), together with the native RC314 even complement C>=mu, give
a strictly positive 2x2 Schur lower determinant in the {v0,w}
basis. This is NOT positivity on the other 120 even/195 odd low
coordinates, full Stage I, F4, Lean or RH.
"""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import validate_rpb108_rc318_p0_signed_schur as rc318
import validate_rpb108_rc319_p2_mixed_native as rc319

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
Z=B/2
CUT=512
FIRST=244
OUT=10**25
BUD=10**32
PINS={
 "certificates/rpb108_rc46_native_archimedean_head.json":
 "be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9",
 "certificates/rpb108_rc129_four_vector_joint_moment.json":
 "33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc314_fredholm_schur.json":
 "6496be8d20176f173c0ff8b6e393b0ccd7c6ff5b",
 "certificates/rpb108_rc315_low_mode_sign.json":
 "a8cd974c8218e18943dda0082f48cca36a3350a8",
 "certificates/rpb108_rc318_p0_signed_schur.json":
 "85dbc5bc373de9922bfe17a6d43ab2cef7178cd6",
 "certificates/rpb108_rc319_p2_mixed_native.json":
 "9c1457d405305928b02f1e546378c0dc239d63a6",
}
def lower(x,g=OUT):
 return F(x.numerator*g//x.denominator,g)
def upper(x,g=OUT):
 return F((x.numerator*g+x.denominator-1)//x.denominator,g)
def rootlo(x,g=10**30):
 assert x>0
 k=isqrt(x.numerator*g*g//x.denominator)
 assert F(k,g)**2<=x<F(k+1,g)**2
 return F(k,g)
def roothi(x,g=10**30):
 assert x>=0
 if x==0:return F(0)
 k=isqrt(x.numerator*g*g//x.denominator)
 assert F(k,g)**2<=x<F(k+1,g)**2
 return F(k+1,g)
def blob(raw):
 return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def source_rational_center(rows,reverse=False):
 pieces=rc319.step_segments(rows,reverse)
 norm=F(0)
 for l,h,g0,g2 in pieces:
  g=[g2[0]-g0[0],g2[1],g2[2]]
  norm+=F(5,2)*rc319.integ(rc319.poly_mul(g,g),l,h)
 assert norm>0
 a0,f0,a0min,a0max=rc318.scaled_prime_and_faults(rows,reverse)
 a0[0]=-sum((r["c"]*(2-(r["el"]+r["eu"])/(2*B))
           for r in rows),F(0))
 assert -a0max<=a0[0]<=-a0min
 a2=rc319.signed_j2_coefficients(rows,reverse)
 assert len(a2)==CUT//2 and len(a0)==CUT//2
 assert 5*a2[0]==a0[2],("RC319 independent selfadjoint check")
 diff={n:a2[n]-a0[n] for n in a2}
 return norm,diff,pieces

def native_transport_fault(rows):
 # u2-sqrt5*u0 has physical norm sqrt6 < 5/2.
 # Zero-extension is continuous because P2(+/-1)-1=0.
 # Its weak physical derivative has norm sqrt15/B < 4/B.
 # Thus ||T_{ell+delta}f - T_ell f||_L2 <= 4*|delta|/B
 # by the translation theorem for compactly supported H1.
 fault=F(0)
 for r in rows:
  de=(r["eu"]-r["el"])/2
  dc=r["cradius"]
  fault+=2*(F(5,2)*dc+r["ch"]*4*de/B)
 assert 0<=fault<F(1,10**25)
 return upper(fault)

def run(reverse=False):
 docs={}
 for path,pin in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes()
  assert blob(raw)==pin,("pinned source changed",path)
  docs[path]=json.loads(raw)
 def cert(q):return docs["certificates/rpb108_rc"+q+".json"]
 assert cert("319_p2_mixed_native")["original_P0_P2_low_principal_block_strictly_positive"]
 assert not cert("319_p2_mixed_native")["full_P0_P2_high_eliminated_Schur_2by2_positive"]
 assert cert("318_p0_signed_schur")["original_P0_full_even_high_eliminated_Schur_diagonal_strictly_positive"]
 metric=cert("129_four_vector_joint_moment")
 smin=F(metric["actual_D_Gram_entry_lower"][0][0])/(2*B)
 smax=F(metric["actual_D_Gram_entry_upper"][0][0])/(2*B)
 assert F(3)<smin<=smax<5
 H=rc318.harmonic_table()
 H2=H[2]
 assert H2==F(3,2)
 even=next(v for v in cert("314_fredholm_schur")[
  "inherited_stronger_RC283_all_reference_choices"]
  if v["parity"]=="even" and v["reference_rank"]==122
    and v["first_discarded_degree"]==FIRST)
 mu=F(even["high_complement_D_floor_lower"])
 assert 0<mu<F(1,100)
 alpha_lo=rootlo(5*smin/(smin+H2))
 alpha_hi=roothi(5*smax/(smax+H2))
 assert F(1)<alpha_lo<=alpha_hi<F(2)
 rows=rc318.source_info()
 norm0,diff,pieces=source_rational_center(rows,reverse)
 projected_lower=F(0)
 for n,a in diff.items():
  projected_lower+=lower(5*a*a/F(2*n+1),BUD)
 norm_upper=upper(norm0,BUD)
 assert 0<projected_lower<=norm_upper
 physical_tail_center=norm_upper-projected_lower
 assert 0<physical_tail_center<F(1,100000)
 transport=native_transport_fault(rows)
 high_finite_upper=F(0)
 for n in range(FIRST,CUT,2):
  # Actual original endpoint (P2-P0) Pn mixed difference:
  # E[n,2]-E[n,0] = 6*(2n+1) /
  # [n(n+1)(n-2)(n+3)]. The degree-independent leading
  # 1/n term CANCELS identically.
  endpoint_delta=F(6*(2*n+1),n*(n+1)*(n-2)*(n+3))
  amp=diff[n]+endpoint_delta
  v=5*amp*amp/(F(2*n+1)*(smin+H2)*(smin+H[n]))
  high_finite_upper+=upper(v,BUD)
 # Complete n>=512 prime physical tail by Parseval, with the
 # *whole* true-source transport defect paid by Minkowski.
 prime_phys_tail=roothi(physical_tail_center)
 physical_prime_actual=prime_phys_tail+transport
 # End P2-P0 L2 tail: |E2-E0|<= E0 * 6/((CUT-2)(CUT+3)).
 # sqrt5<9/4 and all-degree E0-tail mass <=1/CUT.
 endpoint_phys_tail=F(9,4)*F(6,(CUT-2)*(CUT+3)*CUT)
 tail_den=rootlo((smin+H2)*(smin+H[CUT]))
 assert tail_den>F(5)
 infinite_high_up=(physical_prime_actual+endpoint_phys_tail)/tail_den
 # The centered finite and infinite output spaces are orthogonal;
 # the global prime transport defect is paid just ONCE in D.
 # Finite output includes original endpoint+center signed prime.
 center_total=roothi(high_finite_upper+infinite_high_up**2)
 # We conservatively pay an EXTRA transport charge rather than
 # rely on subtraction of the previous full-source fault.
 err=F(cert("46_native_archimedean_head")[
  "regular_kernel_uniform_error_upper"])
 regular=5*B*err # 2B * ||u2-sqrt5 u0|| < 5B.
 pole=128*B*Z**FIRST
 assert err<F(1,10**22) and pole<F(1,10**50)
 # No omitted regular polynomial coefficients: r192 applied to
 # source polynomial P2-1 has degree <=195 < FIRST=244.
 Tw_upper=center_total+transport+regular+pole
 Tw2_upper=upper(Tw_upper**2,BUD)
 assert Tw2_upper<F(1,1000000),("boundary cancellation failed")
 old=cert("319_p2_mixed_native")
 old_T2=F(old["P2_D_normalized_complete_high_source_squared_upper"])
 assert Tw2_upper<old_T2/F(100)
 # Low original signed P0/P2 physical entries, with the
 # high-cancelled basis w=v2-alpha*v0:
 # w=(u2-sqrt5 u0)/sqrt(s+3/2).
 prev0=next(v for v in cert("315_low_mode_sign")["original_low_diagonals"]
            if v["n"]==0)
 q00l,q00h=map(F,prev0["physically_normalized_original_Weil_diagonal_interval"])
 q22l,q22h=map(F,old["original_P0_P2_physical_low_diagonal_P2"])
 q02l,q02h=map(F,old["original_P0_P2_physical_offdiagonal_div_sqrt5"])
 assert q00l>0 and 0<q02l<=q02h<q00l
 low_w_numerator=q22l+5*q00l-10*q02h
 Bwwlower=low_w_numerator/(smax+H2)
 assert Bwwlower>0
 B0w_abs=F(9,4)*(q00h-q02l)/rootlo(smin*(smin+H2))
 assert B0w_abs>0
 low00=F(cert("318_p0_signed_schur")["certified_original_P0_Schur_diagonal_lower"])
 T0sq=F(cert("318_p0_signed_schur")["complete_even_D_high_source_Tv0_norm_squared_upper"])
 T0_upper=roothi(T0sq)
 assert low00>0 and T0_upper<F(1,100)
 # Schur correction on each of the two inputs bounded by C^-1
 # <= 1/mu; cross covariance is charged by Cauchy-Schwarz.
 Schurwwlower=Bwwlower-Tw2_upper/mu
 Schur0w_abs_upper=B0w_abs+T0_upper*Tw_upper/mu
 assert Schurwwlower>0
 determinant_lower=low00*Schurwwlower-Schur0w_abs_upper**2
 assert determinant_lower>0,("full two-vector Schur test failed")
 return dict(
   milestone="RC320",
   parent_route_head="b9441943e1e289453290c9ce46d75fd4e62ca405",
   source_blob_pins=PINS,
   original_CC27_signed_Weil_D_Riesz_operator=True,
   rank317_buffered_even_high_floor=str(mu),
   low_basis="v0 and w=v2-alpha*v0, alpha=sqrt(5s/(s+3/2))",
   alpha_rational_enclosure=[str(lower(alpha_lo)),str(upper(alpha_hi))],
   physical_combination="u2 - sqrt5*u0; physical polynomial P2(t)-1 vanishes at ±1",
   source_boundary_jump_cancelled_exactly=True,
   original_prime_terms=14,
   piecewise_quadratic_segments=len(pieces),
   signed_prime_even_legendre_coefficients_evaluated=len(diff),
   exact_prime_source_full_center_mass_upper=str(norm_upper),
   prime_center_projected_even_mass_lower=str(projected_lower),
   prime_center_all_degree_512_plus_tail_mass_upper=str(physical_tail_center),
   full_translation_arithmetic_L2_error_upper=str(transport),
   endpoint_leading_degree_asymptotic_cancels_exactly=True,
   explicit_combination_D_high_244_through_510_energy_upper=str(high_finite_upper),
   complete_combination_infinite_high_norm_upper=str(upper(infinite_high_up)),
   entire_original_boundary_cancelled_D_high_response_norm_upper=str(upper(Tw_upper)),
   entire_original_boundary_cancelled_D_high_response_energy_upper=str(Tw2_upper),
   original_low_Bww_diagonal_lower=str(lower(Bwwlower)),
   original_low_B0w_abs_upper=str(upper(B0w_abs)),
   inherited_original_S00_positive_lower=str(low00),
   rigorous_full_even_Sww_schur_diagonal_lower=str(lower(Schurwwlower)),
   rigorous_full_even_S0w_offdiagonal_abs_upper=str(upper(Schur0w_abs_upper)),
   certified_full_even_two_by_two_schur_determinant_lower=str(lower(determinant_lower)),
   full_P0_P2_high_eliminated_Schur_2by2_positive=True,
   conditional_result_on_RC313_original_CC27_identification=True,
   original_rank317_remaining_even_low_coordinates=120,
   original_rank317_remaining_odd_low_coordinates=195,
   full_rank317_principal_Schur_positive=False,
   Stage_I_closed=False,F4=False,RH=False,Lean=False,
   next_cursor=(
      "RC321: extend boundary-vanishing source cancellation from "
      "P2-P0 to a certified even polynomial family P4,P6,..., "
      "and build a full Loewner Schur positive block with explicit "
      "cross-covariances. The remaining 120 even /195 odd low "
      "coordinates and Stage I remain OPEN."
   ),
 )
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true")
 a=p.parse_args()
 d=run(reverse=a.replay)
 if a.replay:assert d==json.loads(a.output.read_text(encoding="utf-8"))
 else:a.output.write_text(json.dumps(d,sort_keys=True,indent=2)+"\n",encoding="utf-8")
 print("RC320: boundary-cancelled original P0/P2 FULL 2x2 EVEN SCHUR POSITIVE; remaining even/odd and Stage I OPEN",flush=True)
