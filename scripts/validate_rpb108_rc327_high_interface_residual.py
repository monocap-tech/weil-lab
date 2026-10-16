"""RC327: certified native original high-interface norm and sharpER full residual.

The three exact original high coordinates 244,246,248 (RC326) are
separated from the unrepresented high modes 250,252,..., including
the infinite far tail >=800. Rather than charging C*Y by the entire
CC27 N0 norm (~9.92), compute its genuine NATIVE CROSS map:

  P_{>=250} C P_{244,246,248}
    = offdiag(W_B) + signed original prime translations
        - regular archimedean convolution + even pole.

Identity, J, original scalar and the D diagonal vanish across
orthogonal Legendre projections. Offdiag W_B is the EXACT known
Legendre endpoint coefficient, and its complete infinite cross
Hilbert-Schmidt norm is certified with a finite harmonic sum and
a rational n^-3 tail. Prime physical L2 norm and RC324 high/high
regular compression are paid with the correct INPUT and OUTPUT
D denominator; the even pole cross is exponentially bounded.

This is a rigorous cross OPERATOR norm for 3D input to ALL 250+
high output, with separately proven n250..798 and n>=800 budgets.
No offdiagonal matrix elements are assumed zero.

Represented residual R_3 is inherited by pinned RC326. Entire
unrepresented residual obeys
  ||P_rest R|| <= ||P_rest T x|| + ||P_rest C Y||,
where the signed complete Tx source bound is pinned and its
represented energy subtracted by Parseval. Orthogonality then
certifies the complete infinite ||R||.

This improves the RC326 residual bound, but still does NOT prove
positive low 3D Schur, full C inverse, far-tail Schur inversion,
Stage I, F4, Lean or RH.
"""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import validate_rpb108_rc324_high_tail_smoothing as rc324

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
HEAD_INPUT=(244,246,248)
FIRST_UNREPRESENTED=250
FAR=800
G=10**28
PINS={
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc313_prime_pole_distributions.json":"954b4892cf3b4e999e65476d7ce341021528d9e8",
 "certificates/rpb108_rc323_coercivity_nogo.json":"3280e450654675c09292be902a8888e69c9a75ce",
 "certificates/rpb108_rc324_high_tail_smoothing.json":"33f73683424d6408a35aeced0bb205bdb7215686",
 "certificates/rpb108_rc325_native_high_2x2.json":"27f42ff30438613e335f39e232c8ac0329f1d854",
 "certificates/rpb108_rc326_native_high_3x3_residual.json":"62a7c8fe549ed4b0d1aec799e1d4f1402ea02e06"
}
def down(x,g=G):return F(x.numerator*g//x.denominator,g)
def up(x,g=G):return F((x.numerator*g+x.denominator-1)//x.denominator,g)
def sqrtlo(x,g=10**38):
 assert x>=0
 k=isqrt(x.numerator*g*g//x.denominator)
 assert F(k,g)**2<=x<F(k+1,g)**2 if x else k==0
 return F(k,g)
def sqrthi(x,g=10**38):
 assert x>=0
 if x==0:return F(0)
 k=isqrt(x.numerator*g*g//x.denominator)
 assert F(k,g)**2<=x<F(k+1,g)**2
 return F(k+1,g)
def gitblob(x):return hashlib.sha1(b"blob "+str(len(x)).encode()+b"\0"+x).hexdigest()
def parse_interval(xs):return F(xs[0]),F(xs[1])
def absolute_lower(xs):
 lo,hi=parse_interval(xs)
 if lo<=0<=hi:return F(0)
 return min(abs(lo),abs(hi))

def run(reverse=False):
 docs={}
 for path,pin in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes()
  assert gitblob(raw)==pin,("pinned upstream source changed",path)
  docs[path]=json.loads(raw)
 def cert(k):return docs["certificates/rpb108_rc"+k+".json"]
 prev=cert("326_native_high_3x3_residual")
 old3=cert("325_native_high_2x2")
 oldFar=cert("324_high_tail_smoothing")
 assert prev["native_original_high_3x3_strictly_positive"]
 assert prev["infinite_even_far_tail_action_included_via_global_norm"]
 assert oldFar["original_even_far_high_D_floor_strict_positive"]
 assert old3["original_high_C_244_246_2by2_strict_positive"]
 met=cert("129_four_vector_joint_moment")
 slo=F(met["actual_D_Gram_entry_lower"][0][0])/(2*B)
 shi=F(met["actual_D_Gram_entry_upper"][0][0])/(2*B)
 assert 3<slo<=shi<5
 h=rc324.Htable(FAR)
 D=lambda n:h[n]+slo
 Din=min(D(m) for m in HEAD_INPUT)
 Dnear=D(FIRST_UNREPRESENTED)
 Dfar=D(FAR)
 assert Din>9 and Dnear>Din and Dfar>Dnear
 # Native exact logarithmic endpoint offdiag:
 # <v_n,Wv_m>=sqrt((2n+1)(2m+1)) /
 #    [(n-m)(n+m+1)sqrt((H_n+s)(H_m+s))]
 # for n>m of the same even parity.
 finite=F(0)
 for n in (reversed(range(FIRST_UNREPRESENTED,FAR,2))
           if reverse else range(FIRST_UNREPRESENTED,FAR,2)):
  for m in (reversed(HEAD_INPUT) if reverse else HEAD_INPUT):
   x=F((2*n+1)*(2*m+1),
          (n-m)**2*(n+m+1)**2*D(n)*D(m))
   finite+=up(x,10**44)
 finite=up(finite,10**36)
 assert finite>0
 # The infinite n>=800 even sum is dominated by the sum
 # of ALL integers n>=800. n-m>=n(1-m/800),
 # n+m+1>=n, 2n+1<=(2+1/800)n, Hn>=H800.
 # Therefore each squared entry <= c_m/n^3.
 # Sum_{n>=800} 1/n^3 <=int_799^infty t^-3 dt
 # =1/(2*799^2). No asymptotic fit/finite sampling.
 far=F(0)
 for m in HEAD_INPUT:
  c=F((2*FAR+1)*(2*m+1)*FAR,
        (FAR-m)**2*Dfar*D(m))
  # exactly (2+1/FAR)*(2m+1) /
  #         [(1-m/FAR)^2 Dfar Dm].
  far+=c/F(2*(FAR-1)**2)
 far=up(far,10**36)
 assert 0<far<finite/F(10)
 endpointHS=sqrthi(finite+far)
 endpointNearHS=sqrthi(finite)
 endpointFarHS=sqrthi(far)
 # Native signed seven-prime translations: original
 # physical operator norm, not source samples.
 prime=F(cert("313_prime_pole_distributions")[
   "original_prime_finite_chain_L2_norm_upper"])
 regular=F(oldFar[
   "original_high_regular_operator_norm_bound_244plus"])
 assert F(4)<prime<F(5) and 0<regular<F(1,1000)
 # Each three-coordinate input is D-normalized, as is
 # the entire even output. The prime and regular FULL
 # physical L2 norms are attenuated by both D factors.
 primeCross=prime/sqrtlo(Din*Dnear)
 regularCross=regular/sqrtlo(Din*Dnear)
 # Signed even pole on the even carrier is the positive
 # physical rank-one 2|cosh><cosh|. For any n>=1 even,
 # |<u_n,cosh(x/2)>| <=2sqrt(2B)*(B/2)^n:
 # Taylor of degree n-1 is orthogonal; uniform remainder
 # <=2 (B/2)^n (Taylor factorial discarded).
 # Three represented n>=244 coefficients have squared
 # mass <=24B z^(2*244); all even n>=250 squared mass
 # <=8B z^(2*250)/(1-z^4). The pole cross norm is
 # at most 2 times product /sqrt(Din Dnear). Bound the
 # square-root prefactor 2sqrt(192)<28:
 # 2*sqrt(24B*8B/(1-z^4)) <= 50B.
 z=B/2
 assert 0<z<F(3,5)
 poleCross=F(50)*B*z**(244+250)/sqrtlo(Din*Dnear)
 cross=up(endpointHS+primeCross+regularCross+poleCross)
 # Separate, independent whole-to-800+ restriction. The
 # original far regular compression is smaller and prime
 # D-weight benefits from H800 instead of H250.
 regFar=F(oldFar["original_high_regular_operator_norm_bound_800plus"])
 farCross=up(endpointFarHS+prime/sqrtlo(Din*Dfar)
             +regFar/sqrtlo(Din*Dfar)+poleCross)
 nearCross=up(endpointNearHS+primeCross+regularCross+poleCross)
 assert farCross<cross and nearCross<cross and cross<F(3,5)
 # The y vector is the exact rational RC326 native three-
 # coordinate Ritz trial; its outside-high action is paid
 # without ANY global ||N0|| replacement.
 y=list(map(F,prev["explicit_original_high_3mode_Ritz_trial"]))
 assert len(y)==3
 yNorm=sqrthi(sum((v*v for v in y),F(0)))
 outsideC=up(cross*yNorm)
 outsideFar=up(farCross*yNorm)
 outsideNear=up(nearCross*yNorm)
 prevCY=F(prev["actual_Ritz_trial_full_high_action_CY_norm_upper"])
 assert outsideC<prevCY/F(15)
 # Entire original Tx already paid by full signed P0,w2,w4
 # native-source certificates in RC326. Its three actual
 # represented coordinates are pinned enclosures; Parseval
 # permits subtracting their guaranteed finite energy.
 Twhole=F(prev["independently_pinned_whole_original_high_source_Tx_norm_upper"])
 b=prev["low_witness_high_248_signed_source_interval"]
 oldb=old3["low_R323_witness_native_high_response"]
 bs=[oldb["244"],oldb["246"],b]
 knownEnergy=sum((absolute_lower(x)**2 for x in bs),F(0))
 assert knownEnergy>0 and Twhole*Twhole>knownEnergy
 Toutside=sqrthi(Twhole*Twhole-knownEnergy)
 # Actual outside-space residual retains signs, but the
 # source C*y cross covariance is not yet computed; pay a
 # triangle bound ONLY on the outside space.
 Routside=up(Toutside+outsideC)
 Rinside=F(prev["explicit_represented_3mode_residual_norm_upper"])
 # Orthogonal represented/outside decomposition, unlike
 # RC326's whole-space triangle double counting.
 Rtotal=up(sqrthi(Rinside*Rinside+Routside*Routside))
 mu=F(oldFar["inherited_even_244plus_global_floor"])
 assert mu>0
 penalty=up(Rtotal*Rtotal/mu)
 oldPenalty=F(prev["RC314_correct_sign_full_high_residual_penalty_upper"])
 assert penalty<oldPenalty/F(2),(
  "new native head-to-infinite interface fails residual reduction")
 assert Rtotal<F(2,1000)
 # No hidden positivity theorem: present loss still exceeds
 # the original almost-null low principal quadratic scale.
 lowB=F(cert("323_coercivity_nogo")["original_low_quadratic_B_upper"])
 assert penalty>lowB
 return dict(
  milestone="RC327",
  parent_route_head="99316d9eda3f74323603c9f6da2a6cfd34bec022",
  input_git_blob_pins=PINS,
  original_CC27_signed_Weil_D_operator=True,
  represented_even_high_degrees=list(HEAD_INPUT),
  finite_unrepresented_even_degree_first=FIRST_UNREPRESENTED,
  finite_unrepresented_even_degree_last=FAR-2,
  infinite_even_far_tail_starts=FAR,
  exact_endpoint_offdiag_squared_Hilbert_Schmidt_finite_upper=str(finite),
  exact_endpoint_offdiag_squared_Hilbert_Schmidt_800plus_upper=str(far),
  exact_endpoint_whole_unrepresented_cross_HS_norm_upper=str(up(endpointHS)),
  native_prime_physical_L2_operator_bound=str(prime),
  native_regular_244plus_physical_operator_bound=str(regular),
  even_pole_rank_one_cross_tail_upper=str(up(poleCross)),
  original_signed_high_cross_operator_3mode_to_all_250plus_norm_upper=str(cross),
  original_signed_high_cross_operator_3mode_to_250through798_norm_upper=str(nearCross),
  original_signed_high_cross_operator_3mode_to_all_800plus_norm_upper=str(farCross),
  real_head_to_far_tail_action_norm_upper_on_chosen_rational_y=str(outsideFar),
  actual_rational_R326_high_trial_y=[str(v) for v in y],
  actual_rational_high_trial_norm_upper=str(up(yNorm)),
  actual_full_high_action_outside_first_three_C_y_norm_upper=str(outsideC),
  original_pinned_whole_high_Tx_norm_upper=str(Twhole),
  represented_three_signed_high_source_energy_lower=str(down(knownEnergy)),
  all_unrepresented_high_Tx_norm_upper=str(up(Toutside)),
  represented_three_high_residual_norm_upper=str(Rinside),
  all_unrepresented_high_R_norm_upper=str(Routside),
  complete_original_infinite_high_R_T_minus_CY_norm_upper=str(Rtotal),
  RC314_correct_sign_complete_residual_penalty_upper=str(penalty),
  preceding_RC326_complete_residual_penalty_upper=str(oldPenalty),
  strict_residual_penalty_improvement_over_RC326=True,
  full_native_278_head_to_far_tail_operator_norm_certified=False,
  full_original_high_inverse_computed=False,
  positive_full_three_dimensional_low_Schur_proved=False,
  Stage_I_closed=False,F4=False,Lean=False,RH=False,
  next_cursor=(
    "RC328: the 3-coordinate C->250+ interface is now charged "
    "by a genuine original signed cross operator norm (not 9.92). "
    "The current residual remains dominated by the full signed "
    "Tx source triangle bound and coarse prime cross. Evaluate "
    "the original *combined* Tx source Parseval and signed "
    "outside cross covariance <Tx,Cy> to sharpen the negative "
    "RC314 residual penalty. The finite 278x278 high head "
    "and its unrestricted coupling to the far tail remain open."
  ))
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true")
 a=p.parse_args()
 result=run(reverse=a.replay)
 if a.replay:
  assert result==json.loads(a.output.read_text(encoding="utf-8"))
 else:
  a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n",
                      encoding="utf-8")
 print("RC327: original high three-mode-to-entire-outside coupling paid; corrected full-space residual tightened. 3D Schur and Stage I OPEN.")
