"""RC329 — first genuine signed OUTSIDE-high <Tx,CY> covariance.

This extends the RC326/328 original CC27 native signed Ritz test to
the first OMITTED even high coordinate n=250. Original native
C_{250,m} for m=244,246,248 is evaluated through 21 exact rational
prime/Legendre translation overlaps at certified log centers.
Pay Leibniz/Markov support displacement, original endpoint,
refined scalar (offdiagonal zero), RC324 regular operator remainder,
and even pole. No proxy augmented operator.

The original *signed* Tx amplitude at n250 was independently pinned
and reverse-replayed in RC328. The actual Ritz y from RC326 is
unchanged. Compute a rigorous signed interval for
    <P_250 Tx, P_250 C Y> = b250 * (C250,head y).
Also compute its actual finite residual norm.

All other n>=252 are rigorously charged using RC328's complete
original source bound and RC327's actual native head-to-outside C
cross norm, with this n250 output subtracted from BOTH budgets
by orthogonality. This yields a strict sharpened entire-space
residual penalty. It is a one-coordinate native covariance theorem,
NOT a paid entire finite n250..798 covariance, full inverse,
positive 3D Schur, Stage I, F4, Lean or RH.
"""
from __future__ import annotations
import argparse, hashlib, json
from math import isqrt
from pathlib import Path
from fractions import Fraction as F
import validate_rpb108_rc323_coercivity_nogo as rc323
import validate_rpb108_rc324_high_tail_smoothing as rc324
import validate_rpb108_rc325_native_high_2x2 as rc325

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
HIGH=(244,246,248)
OUTSIDE=250
G=10**26
PINS={
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc313_prime_pole_distributions.json":"954b4892cf3b4e999e65476d7ce341021528d9e8",
 "certificates/rpb108_rc322_low_3d_gram.json":"ba344b44436c5c2d392a9feb5c6dc0c9892dfe88",
 "certificates/rpb108_rc323_coercivity_nogo.json":"3280e450654675c09292be902a8888e69c9a75ce",
 "certificates/rpb108_rc324_high_tail_smoothing.json":"33f73683424d6408a35aeced0bb205bdb7215686",
 "certificates/rpb108_rc326_native_high_3x3_residual.json":"62a7c8fe549ed4b0d1aec799e1d4f1402ea02e06",
 "certificates/rpb108_rc327_high_interface_residual.json":"dc6eadb88b8d148753d27318ed9a0cf5b52ad8f6",
 "certificates/rpb108_rc328_signed_finite_tail_residual.json":"49d9daf11defd0f272865d3780f3a53d0af6e130",
}
def dn(x,g=G):return F(x.numerator*g//x.denominator,g)
def up(x,g=G):return F((x.numerator*g+x.denominator-1)//x.denominator,g)
def root(x,upper=False,g=10**36):
 assert x>=0
 if not x:return F(0)
 k=isqrt(x.numerator*g*g//x.denominator)
 assert F(k,g)**2<=x<F(k+1,g)**2
 return F(k+int(upper),g)
def blob(raw):return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
IV=rc325.IV
def iv(x):return rc325.iv(x)
def absmin(v):
 if v.l<=0<=v.h:return F(0)
 return min(abs(v.l),abs(v.h))
def absmax(v):return max(abs(v.l),abs(v.h))

def native_mixed_prime(rows,reverse=False):
 # Original signed off-diagonal prime: -sum c_m I_{ij}(d)
 # where I=integral_-1^{1-d} P_i(t) P_j(t+d) dt.
 # Every term evaluated as exact rational polynomial integral,
 # then all actual log/weight/shift-support deviations are paid.
 p={n:rc325.legendre(n) for n in HIGH+(OUTSIDE,)}
 ans={}
 for m in HIGH:
  center=F(0);fault=F(0)
  for r in (list(reversed(rows)) if reverse else rows):
   left=r["el"]/B;right=r["eu"]/B
   centerD=rc325.nearest((left+right)/2)
   assert 0<left<=right<2 and 0<centerD<2
   integ=rc325.overlap(p[m],p[OUTSIDE],centerD)
   # Moving endpoint and derivative of P250:
   # |d/dz integral Pm(t)P250(t+z)|<=1+250*251.
   errorD=max(abs(left-centerD),abs(right-centerD))
   fault+=r["ch"]*(1+OUTSIDE*(OUTSIDE+1))*errorD+2*r["cradius"]
   center-=r["c"]*integ
  ans[m]=IV(dn(center-fault),up(center+fault))
 return ans

def run(reverse=False):
 docs={}
 for path,pin in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes()
  assert blob(raw)==pin,("source pin changed",path)
  docs[path]=json.loads(raw)
 def cert(k):return docs["certificates/rpb108_rc"+k+".json"]
 old=cert("328_signed_finite_tail_residual")
 prev=cert("327_high_interface_residual")
 c326=cert("326_native_high_3x3_residual")
 assert old["proved_strict_sharpening_of_complete_original_signed_residual"]
 assert c326["native_original_high_3x3_strictly_positive"]
 assert not old["unrepresented_original_Tx_CY_signed_covariance_computed"]
 met=cert("129_four_vector_joint_moment")
 sLo=F(met["actual_D_Gram_entry_lower"][0][0])/(2*B)
 sHi=F(met["actual_D_Gram_entry_upper"][0][0])/(2*B)
 assert 3<sLo<=sHi<5
 h=rc324.Htable(OUTSIDE)
 reg=F(cert("324_high_tail_smoothing")[
   "original_high_regular_operator_norm_bound_244plus"])
 P=rc323.rc318.source_info()
 rawprime=native_mixed_prime(P,reverse)
 C={}
 for m in HIGH:
  # Original W offdiagonal scaled Legendre matrix, full
  # D normalized. Original J, I and scalar are diagonal.
  endpoint=F(1,(OUTSIDE-m)*(OUTSIDE+m+1))
  phys=IV(endpoint)+rawprime[m]+IV(-reg,reg)
  # Even signed pole is rank-one. Its native cross can
  # have either sign: pay its complete absolute Taylor tail.
  pole=100*B*(B/2)**(OUTSIDE+m)
  phys+=IV(-pole,pole)/IV((2*m+1)*(2*OUTSIDE+1)).sqrt()
  f=IV((2*m+1)*(2*OUTSIDE+1)).sqrt() / (
    IV(h[m]+sLo,h[m]+sHi)*IV(h[OUTSIDE]+sLo,h[OUTSIDE]+sHi)).sqrt()
  z=phys*f
  C[m]=IV(dn(z.l),up(z.h))
 # The source amplitude is PINNED and independently computed
 # by RC328 before combining with the exact D output metric.
 source=old["selected_joint_original_signed_high_mode_intervals"][str(OUTSIDE)]
 signedamp=IV(*map(F,source["signed_combined_original_prime_plus_endpoint_amplitude"]))
 denom=IV((2*OUTSIDE+1)*(h[OUTSIDE]+sLo),
          (2*OUTSIDE+1)*(h[OUTSIDE]+sHi)).sqrt()
 bcenter=signedamp/denom
 # Charge the ENTIRE original CC27 physical source fault
 # as a safe bound on this individual D-normalized mode.
 perturb=F(cert("323_coercivity_nogo")[
   "complete_original_high_source_error_upper"])
 b=IV(dn(bcenter.l-perturb),up(bcenter.h+perturb))
 y=list(map(F,c326["explicit_original_high_3mode_Ritz_trial"]))
 Cy=sum((C[m]*y[i] for i,m in enumerate(HIGH)),IV(0))
 Cy=IV(dn(Cy.l),up(Cy.h))
 covariance=Cy*b
 covariance=IV(dn(covariance.l),up(covariance.h))
 residual=b-Cy
 residual=IV(dn(residual.l),up(residual.h))
 assert absmin(b)>0 and absmin(Cy)>0
 # Entire previous outside-high bounds (including n250).
 Tprev=F(old["true_entire_unrepresented_Tx_norm_upper"])
 Cprev=F(prev["actual_full_high_action_outside_first_three_C_y_norm_upper"])
 Rrepresented=F(old["certified_represented_3mode_original_residual_norm_upper"])
 assert Tprev*Tprev>absmin(b)**2
 assert Cprev*Cprev>absmin(Cy)**2
 # On all remaining n>=252, orthogonality permits
 # subtraction of guaranteed positive energy in mode250.
 Trest=up(root(Tprev*Tprev-absmin(b)**2,upper=True))
 Crest=up(root(Cprev*Cprev-absmin(Cy)**2,upper=True))
 Rrest=up(Trest+Crest)
 # Pay SIGNED covariance in actual first outside degree:
 # ||b250-Cy250||^2, using exact original native signs.
 R250=up(absmax(residual))
 Rtotal=up(root(Rrepresented**2+R250**2+Rrest**2,upper=True))
 mu=F(cert("324_high_tail_smoothing")[
   "inherited_even_244plus_global_floor"])
 penalty=up(Rtotal*Rtotal/mu)
 oldPenalty=F(old["certified_RC314_correct_sign_entire_residual_penalty_upper"])
 assert penalty<oldPenalty,("one-mode source-resolved covariance did not sharpen residual")
 assert Rtotal<F(old["certified_original_entire_infinite_R_T_minus_CY_norm_upper"])
 # The entire infinite Schur operator remains unknown.
 low=F(cert("323_coercivity_nogo")["original_low_quadratic_B_upper"])
 assert penalty>low
 return dict(
  milestone="RC329",
  parent_route_head="c6a25abccb7ee8ec1b36c27016abbaebc571fbaf",
  input_git_blob_pins=PINS,
  original_CC27_signed_Weil_operator=True,
  first_omitted_high_mode=OUTSIDE,
  exact_native_signed_prime_overlap_integrals=3*7,
  original_prime_log_and_moving_support_error_fully_paid=True,
  original_high_native_C_250_vs_244_246_248_intervals={
    str(m):C[m].out() for m in HIGH},
  original_joint_signed_b_250_interval=b.out(),
  pinned_rational_three_mode_Ritz_y=[str(v) for v in y],
  original_native_C_y_250_interval=Cy.out(),
  actual_signed_original_outside_covariance_b250_times_Cy250_interval=covariance.out(),
  actual_original_one_omitted_high_residual_250_interval=residual.out(),
  first_outside_true_source_energy_lower=str(dn(absmin(b)**2)),
  first_outside_true_Ritz_action_energy_lower=str(dn(absmin(Cy)**2)),
  remaining_252plus_true_source_norm_upper=str(Trest),
  remaining_252plus_Ritz_C_action_norm_upper=str(Crest),
  complete_one_omitted_mode_residual_norm_upper=str(R250),
  remaining_infinite_high_residual_norm_upper=str(Rrest),
  inherited_represented_three_mode_residual_norm_upper=str(Rrepresented),
  complete_original_full_infinite_residual_norm_upper=str(Rtotal),
  corrected_RC314_complete_full_residual_penalty_upper=str(penalty),
  RC328_previous_complete_residual_penalty_upper=str(oldPenalty),
  rigorous_strict_signed_outside_covariance_refinement=True,
  finite_original_250through798_covariance_fully_computed=False,
  native_278_by_278_high_inverse_computed=False,
  full_three_dimensional_Schur_positive=False,
  full_rank317_original_Schur_positive=False,
  Stage_I_closed=False,F4=False,Lean=False,RH=False,
  next_cursor=(
   "RC330: extend first truly signed outside covariance "
   "to even modes 252,254,... with original prime overlap "
   "and endpoint action; preserve joint covariance before "
   "squaring and charge all remaining infinite high modes. "
   "The 278x278 native high head and low three-dimensional "
   "Schur positivity remain open."
  )
 )
if __name__=="__main__":
 ap=argparse.ArgumentParser()
 ap.add_argument("--output",type=Path,required=True)
 ap.add_argument("--replay",action="store_true")
 a=ap.parse_args()
 d=run(reverse=a.replay)
 if a.replay:
  assert d==json.loads(a.output.read_text(encoding="utf-8"))
 else:
  a.output.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n",encoding="utf-8")
 print("RC329: signed original n250 outside Tx-CY covariance exact enclosing; entire high residual paid, full Schur and Stage I OPEN.")
