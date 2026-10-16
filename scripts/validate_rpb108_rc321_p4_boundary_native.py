"""RC321 — original signed P4-P2 boundary-cancelled complete high response.

The original CC27/RC313 signed Weil form is used throughout.
Physical f4=u4-(3/sqrt(5))*u2=3/sqrt(2B)*(P4-P2),
P4-P2=(7/8)(t²-1)(5t²-1) vanishes at both endpoints.
The zero extension lies in H1(R), with ||f4||²=14/5,
||f4'||²=63/B², so moving edges incur LINEAR transport error.

The 14 signed prime translates of f4 form an exactly piecewise
quartic physical source, integrated with all cross-interference.
Compute 256 even Legendre output coefficients at rational centers
using exact adjacent-degree moment recurrences; independently
check the P0/P4 and P2/P4 prime matrix symmetry identities.
Parseval, source transport, exact endpoint leading-tail
cancellation, the pinned RC46 regular remainder and pole tail
rigorously pay the ENTIRE high-D response on the new P4-P2 mode.

This is a source-action certificate for a candidate third low
direction; no positivity of a 3D Schur block or Stage I is asserted.
"""
from __future__ import annotations
import argparse,hashlib,json
from math import isqrt,comb
from pathlib import Path
from fractions import Fraction as F
import validate_rpb108_rc318_p0_signed_schur as rc318
import validate_rpb108_rc319_p2_mixed_native as rc319

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
CUT=512
FIRST=244
GRID=10**35
OUT=10**25
BUD=10**32
PINS={
 "certificates/rpb108_rc46_native_archimedean_head.json":
  "be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9",
 "certificates/rpb108_rc129_four_vector_joint_moment.json":
  "33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc313_prime_pole_distributions.json":
  "954b4892cf3b4e999e65476d7ce341021528d9e8",
 "certificates/rpb108_rc314_fredholm_schur.json":
  "6496be8d20176f173c0ff8b6e393b0ccd7c6ff5b",
 "certificates/rpb108_rc318_p0_signed_schur.json":
  "85dbc5bc373de9922bfe17a6d43ab2cef7178cd6",
 "certificates/rpb108_rc319_p2_mixed_native.json":
  "9c1457d405305928b02f1e546378c0dc239d63a6",
 "certificates/rpb108_rc320_boundary_cancelled_schur.json":
  "fe8821aaba62ba50c2a8eba1a2fa0020ba818003",
}

def down(x,g=OUT):
 return F(x.numerator*g//x.denominator,g)
def up(x,g=OUT):
 return F((x.numerator*g+x.denominator-1)//x.denominator,g)
def sqrtup(x,g=10**30):
 assert x>=0
 if x==0:return F(0)
 t=isqrt(x.numerator*g*g//x.denominator)
 assert F(t,g)**2<=x<F(t+1,g)**2
 return F(t+1,g)
def sqrtlo(x,g=10**30):
 assert x>0
 t=isqrt(x.numerator*g*g//x.denominator)
 assert F(t,g)**2<=x<F(t+1,g)**2
 return F(t,g)
def gitblob(raw):
 return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def poly_shift_F(d):
 # F(t+d)=P4(t+d)-P2(t+d)=(35(t+d)^4-42(t+d)^2+7)/8.
 p=[F(35*comb(4,j),8)*d**(4-j) for j in range(5)]
 for j in range(3):p[j]-=F(42*comb(2,j),8)*d**(2-j)
 p[0]+=F(7,8)
 assert p[4]==F(35,8)
 return p
def poly_at(p,t):
 return sum((v*t**j for j,v in enumerate(p)),F(0))

def signed_piecewise_profile(rows,reverse=False):
 terms=[]
 for r in (reversed(rows) if reverse else rows):
  d=(r["el"]+r["eu"])/(2*B)
  assert 0<d<2
  for sign in (-1,1):
   left=max(F(-1),-1-sign*d)
   right=min(F(1),1-sign*d)
   assert left<right
   p=[-r["c"]*v for v in poly_shift_F(sign*d)]
   # Source polynomial is zero on the translated support edges.
   # A side may be clipped by [-1,1], so test native translated
   # support endpoints only when they fall into the aperture.
   for edge in (-1-sign*d,1-sign*d):
    if -1<=edge<=1:assert poly_at(p,edge)==0
   terms.append((left,right,p))
 bounds=sorted({F(-1),F(1)}|{t[i] for t in terms for i in (0,1)})
 assert len(terms)==14 and len(bounds)==16
 pieces=[]
 for l,h in zip(bounds,bounds[1:]):
  m=(l+h)/2
  active=[p for a,b,p in terms if a<m<b]
  coeff=[sum((p[j] for p in active),F(0)) for j in range(5)]
  pieces.append((l,h,coeff))
 assert len(pieces)==15
 for l,h,p in pieces:
  v=next((q for a,b,q in pieces if a==-h and b==-l),None)
  assert v is not None and p==[v[j]*(-1)**j for j in range(5)]
 norm=F(9,2)*sum((rc319.integ(rc319.poly_mul(p,p),l,h)
                    for l,h,p in pieces),F(0))
 assert 0<norm<8
 return norm,pieces

def shifted_moments_all_even(rows,reverse=False):
 # Integral I_n(d) = int_-1^(1-d) Pn(t)*[P4(t+d)-P2(t+d)] dt.
 # Multiplication by t in the Legendre basis has exact
 # tridiagonal recurrence; fourth powers therefore cost 5
 # shifts at most. All n even 0..510 are covered, including
 # small n=0,2,4 without fake negative-index recurrences.
 result={n:F(0) for n in range(0,CUT,2)}
 for r in (reversed(rows) if reverse else rows):
  d=(r["el"]+r["eu"])/(2*B)
  z=1-d
  c=r["c"]
  # P0..P516 at exact rational z; largest required J514
  # invokes P515. One extra degree is retained for audit.
  pv=[F(1),z]
  for k in range(1,CUT+5):
   pv.append(((2*k+1)*z*pv[-1]-k*pv[-2])/F(k+1))
  assert len(pv)==CUT+6
  def J(k):
   assert k>=0
   if k==0:return z+1
   return (pv[k+1]-pv[k-1])/F(2*k+1)
  coeff=poly_shift_F(d)
  for n in range(0,CUT,2):
   expansion={n:F(1)}
   moments=[J(n)]
   for power in range(1,5):
    newer={}
    for k,a in expansion.items():
     newer[k+1]=newer.get(k+1,F(0))+a*F(k+1,2*k+1)
     if k:newer[k-1]=newer.get(k-1,F(0))+a*F(k,2*k+1)
    expansion=newer
    assert all(k>=0 for k in expansion)
    moments.append(sum((a*J(k) for k,a in expansion.items()),F(0)))
   I=sum((coeff[j]*moments[j] for j in range(5)),F(0))
   result[n]-=c*F(2*n+1)*I
 return result

def exact_translation_fault(rows):
 # h=u4-(3/sqrt5)u2 has physical squared norm 14/5
 # and derivative squared norm 63/B²: exact Legendre
 # integrals, no singular edge masses because h(±B)=0.
 # sqrt(14/5)<17/10 and sqrt63<8. Each of the two signed
 # translations pays coefficient error and center-displacement.
 fault=F(0)
 for r in rows:
  delta=(r["eu"]-r["el"])/2
  dc=r["cradius"]
  fault+=2*(F(17,10)*dc+8*r["ch"]*delta/B)
 assert fault<F(1,10**25)
 return up(fault)

def run(reverse=False):
 docs={}
 for p,pin in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/p).read_bytes()
  assert gitblob(raw)==pin,("upstream pin mismatch",p)
  docs[p]=json.loads(raw)
 def get(key):return docs["certificates/rpb108_rc"+key+".json"]
 assert get("320_boundary_cancelled_schur")[
      "full_P0_P2_high_eliminated_Schur_2by2_positive"]
 assert get("319_p2_mixed_native")["original_P0_P2_low_principal_block_strictly_positive"]
 assert get("313_prime_pole_distributions")["original_CC27_Weil_polynomial_form_matches_native_model_on_all_degrees"]
 rows=rc318.source_info()
 sourcecenter,pieces=signed_piecewise_profile(rows,reverse)
 f4=shifted_moments_all_even(rows,reverse)
 f2=rc319.signed_j2_coefficients(rows,reverse)
 original_p0,f0_fault,a0lo,a0hi=rc318.scaled_prime_and_faults(rows,reverse)
 original_p0[0]=-sum((r["c"]*(2-(r["el"]+r["eu"])/(2*B))
                   for r in rows),F(0))
 assert 9*(f4[0]+f2[0])==original_p0[4],(
   "signed prime P0/P4 selfadjointness; f4 is P4-P2 diff")
 assert 9*f4[2]==5*f2[4]-9*f2[2],(
   "signed prime P2/P4 selfadjointness")
 assert len(f4)==256 and len(f2)==256
 prime_energy_center=F(0)
 for n,a in f4.items():
  prime_energy_center+=down(F(9)*a*a/F(2*n+1),BUD)
 source_upper=up(sourcecenter,BUD)
 assert F(0)<prime_energy_center<=source_upper
 tail_center=source_upper-prime_energy_center
 assert F(0)<tail_center<F(1,10000),(
   "native P4-P2 512+ prime Parseval tail not small")
 transport=exact_translation_fault(rows)
 met=get("129_four_vector_joint_moment")
 smin=F(met["actual_D_Gram_entry_lower"][0][0])/(2*B)
 smax=F(met["actual_D_Gram_entry_upper"][0][0])/(2*B)
 assert 3<smin<=smax<5
 H=rc318.harmonic_table()
 H4=H[4]
 assert H4==F(25,12)
 even=next(e for e in get("314_fredholm_schur")[
           "inherited_stronger_RC283_all_reference_choices"]
           if e["parity"]=="even" and e["reference_rank"]==122
               and e["first_discarded_degree"]==FIRST)
 mu=F(even["high_complement_D_floor_lower"])
 assert mu>0
 # E[n,4]-E[n,2] (original logarithmic endpoint D-model):
 # 14(2n+1)/((n-4)(n+5)(n-2)(n+3)), n even>4.
 # Decays as O(n^-3) rather than O(n^-1) separately.
 finite_energy=F(0)
 for n in range(FIRST,CUT,2):
  e=F(14*(2*n+1),(n-4)*(n+5)*(n-2)*(n+3))
  signed=f4[n]+e
  finite_energy+=up(9*signed*signed/
     (F(2*n+1)*(smin+H4)*(smin+H[n])),BUD)
 assert finite_energy>0
 # Physical endpoint tail squared bounded using P0 exact
 # telescope: sum_n>=N (2n+1)/(n²(n+1)²)=1/N².
 # For n>=N, ratio to E0 physical coefficient:
 # 3*14*n(n+1)/((n-4)(n+5)(n-2)(n+3)),
 # and n(n+1)/((n-4)(n+5)) <= N(N+1)/(N(N+1)-20),
 # 1/((n-2)(n+3)) <= 1/(N(N+1)-6).
 val=CUT*(CUT+1)
 physical_endpoint_tail=F(42*val,(val-20)*(val-6)*CUT)
 assert physical_endpoint_tail<F(1,10**6)
 den_tail=sqrtlo((smin+H4)*(smin+H[CUT]))
 den_first=sqrtlo((smin+H4)*(smin+H[FIRST]))
 assert den_tail>den_first>F(7)
 centered_finite_norm=sqrtup(finite_energy)
 centered_infinite_norm=(
     sqrtup(tail_center)+physical_endpoint_tail)/den_tail
 # Endpoint+prime centered pieces are orthogonal over the
 # explicit 244..510 and remaining 512+ sets.
 centered_high_norm=sqrtup(
   centered_finite_norm**2+centered_infinite_norm**2)
 # Pay the whole signed prime transport residual exactly once
 # on the entire high space (not 256 independent errors).
 actual_transport_D=transport/den_first
 reg_error=F(get("46_native_archimedean_head")[
   "regular_kernel_uniform_error_upper"])
 assert reg_error<F(1,10**22)
 regular_remainder=5*B*reg_error # 2B eps ||h||<4B eps; loose.
 even_pole=256*B*(B/2)**FIRST
 assert even_pole<F(1,10**50)
 entire_high_norm=centered_high_norm+actual_transport_D+regular_remainder+even_pole
 entire_high_sq=up(entire_high_norm**2,BUD)
 assert entire_high_sq<F(1,10000),(
    "first original boundary-cancelled P4-P2 response too large")
 # It is invalid to certify the full 3x3 Schur form with the
 # P4 response alone: low 3x3 entries/cross-covariances must
 # be computed and paid. This is the next frontier.
 prior=get("319_p2_mixed_native")
 assert entire_high_sq<F(prior[
        "P2_D_normalized_complete_high_source_squared_upper"])
 return dict(
   milestone="RC321",
   parent_route_head="6e4c2b358ec47f83f5c22f4cd790c462fd80c596",
   input_git_blob_pins=PINS,
   original_CC27_signed_Weil_source=True,
   source_direction="u4-(3/sqrt5)u2 = 3/sqrt(2B)*(P4-P2), then D-normalize by sqrt(s+H4)",
   polynomial_factorization="P4-P2=(7/8)(t^2-1)(5t^2-1)",
   zero_extension_in_H1_with_zero_boundary=True,
   exact_physical_source_norm_squared=str(F(14,5)),
   exact_physical_source_derivative_norm_squared=str(F(63)/B**2),
   exact_endpoint_difference="14*(2*n+1)/((n-4)*(n+5)*(n-2)*(n+3))",
   original_signed_prime_translations=14,
   signed_piecewise_quartic_segments=len(pieces),
   exactly_computed_even_Legendre_coefficients=len(f4),
   P0_P4_P2_P4_native_prime_selfadjoint_crosschecks=True,
   signed_prime_entire_physical_center_mass_squared_upper=str(source_upper),
   signed_prime_center_256_mode_energy_lower=str(prime_energy_center),
   entire_prime_center_infinite_tail_mass_squared_upper=str(tail_center),
   entire_signed_translation_L2_error_upper=str(transport),
   full_original_endpoint_physical_512plus_tail_norm_upper=str(physical_endpoint_tail),
   explicit_original_D_high_244_to_510_energy_upper=str(finite_energy),
   full_center_infinite_D_high_norm_upper=str(up(centered_infinite_norm)),
   full_original_D_high_source_norm_upper=str(up(entire_high_norm)),
   full_original_D_high_source_energy_upper=str(entire_high_sq),
   even_high_complement_floor_inherited_RC314=str(mu),
   original_P4_P2_boundary_cancellation_complete_native_source=True,
   three_dimensional_P0_P2_P4_Schur_positive=False,
   full_even_Schur_positive=False,
   full_rank317_Schur_positive=False,
   Stage_I_closed=False,F4=False,Lean=False,RH=False,
   next_cursor=(
    "RC322: compute the original low P0/P2/P4 signed Gram "
    "including endpoint/regular/pole mixed entries and combine "
    "with the full original high source for P4-P2. "
    "Test the actual 3x3 Schur determinant and offdiagonals "
    "with signed covariance; 120 even and 195 odd low "
    "coordinates have not been discharged."
   )
 )
if __name__=="__main__":
 pa=argparse.ArgumentParser()
 pa.add_argument("--output",type=Path,required=True)
 pa.add_argument("--replay",action="store_true")
 a=pa.parse_args()
 result=run(reverse=a.replay)
 if a.replay:
  assert result==json.loads(a.output.read_text(encoding="utf-8"))
 else:
  a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",
                     encoding="utf-8")
 print("RC321: ORIGINAL signed P4-P2 complete source/Parseval/endpoint cancellation paid; full 3D Schur and Stage I OPEN",flush=True)
