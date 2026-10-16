"""RC328 — strict signed finite-response Parseval + infinite tail residual.

Original CC27 / RC313 Weil D-Riesz carrier, rank317 buffered even
high cutoff 244; RC323 original low witness
 x=(3/25)v0-(23/8)w2+w4.

RC326/327 bounded ||Tx|| using the sum of three INDEPENDENT
whole-response source norms, losing their signed cancellation.
Here reconstruct and enclose EVERY one of the original 278 even
high coefficients 244,246,...,798 of the *combined signed source*
before squaring. The rational fixed-grid Legendre recurrence
is RC323's pinned independent n800 algorithm; pay the complete
real prime-log/weight and regular/pole correction by its native
whole-source error. The entire original infinite n>=800 tail
is separately paid by RC318 (P0) and RC320/321 (endpoint-vanishing
P2-P0, P4-P2) infinite Parseval envelopes, *not* set to zero.

Finite and infinite projections are orthogonal; sum squares
rather than adding their norms. Subtract certified represented
three-mode energy and use RC327's already-paid native original
high cross ||P_250+ C Y|| on its EXACT rational Y to obtain a
rigorous lower RC314 penalty with correct negative sign.

This pays full original signed Tx, but mixed <Tx,CY> in the
unrepresented high sector is still not directly calculated.
It is NOT a full C inverse or 3x3 signed Schur positivity theorem.
"""
from __future__ import annotations
import argparse,hashlib,json
from math import isqrt
from pathlib import Path
from fractions import Fraction as F
import validate_rpb108_rc323_coercivity_nogo as rc323
import validate_rpb108_rc318_p0_signed_schur as rc318
import validate_rpb108_rc324_high_tail_smoothing as rc324

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
FIRST=244
FAR=800
GRID=10**29
H2=F(3,2)
H4=F(25,12)
VEC=(F(3,25),-F(23,8),F(1))
PINS={
 "certificates/rpb108_rc46_native_archimedean_head.json":"be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9",
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc318_p0_signed_schur.json":"85dbc5bc373de9922bfe17a6d43ab2cef7178cd6",
 "certificates/rpb108_rc320_boundary_cancelled_schur.json":"fe8821aaba62ba50c2a8eba1a2fa0020ba818003",
 "certificates/rpb108_rc321_p4_boundary_native.json":"26eedd29ee80063c7b8ccc5f1d5de025e7050842",
 "certificates/rpb108_rc323_coercivity_nogo.json":"3280e450654675c09292be902a8888e69c9a75ce",
 "certificates/rpb108_rc325_native_high_2x2.json":"27f42ff30438613e335f39e232c8ac0329f1d854",
 "certificates/rpb108_rc326_native_high_3x3_residual.json":"62a7c8fe549ed4b0d1aec799e1d4f1402ea02e06",
 "certificates/rpb108_rc327_high_interface_residual.json":"dc6eadb88b8d148753d27318ed9a0cf5b52ad8f6"
}
def dn(x,g=GRID):return F(x.numerator*g//x.denominator,g)
def up(x,g=GRID):return F((x.numerator*g+x.denominator-1)//x.denominator,g)
def sqrtlo(x,g=10**38):
 assert x>=0
 if x==0:return F(0)
 t=isqrt(x.numerator*g*g//x.denominator)
 assert F(t,g)**2<=x<F(t+1,g)**2
 return F(t,g)
def sqrthi(x,g=10**38):
 assert x>=0
 if x==0:return F(0)
 t=isqrt(x.numerator*g*g//x.denominator)
 assert F(t,g)**2<=x<F(t+1,g)**2
 return F(t+1,g)
def sha(raw):return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def norm_absmin(v):
 if v.lo<=0<=v.hi:return F(0)
 return min(abs(v.lo),abs(v.hi))
def norm_absmax(v):return max(abs(v.lo),abs(v.hi))

def run(reverse=False):
 docs={}
 for path,pin in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes()
  assert sha(raw)==pin,("inherited certificate pin mismatch",path)
  docs[path]=json.loads(raw)
 def cert(n):return docs["certificates/rpb108_rc"+n+".json"]
 old=cert("327_high_interface_residual")
 c323=cert("323_coercivity_nogo")
 c326=cert("326_native_high_3x3_residual")
 c318=cert("318_p0_signed_schur")
 c320=cert("320_boundary_cancelled_schur")
 c321=cert("321_p4_boundary_native")
 c46=cert("46_native_archimedean_head")
 assert old["strict_residual_penalty_improvement_over_RC326"]
 assert c323["global_C_floor_only_3D_Loewner_Schur_method_impossible"]
 assert c326["native_original_high_3x3_strictly_positive"]
 assert not old["positive_full_three_dimensional_low_Schur_proved"]
 rows=rc318.source_info()
 scaled_prime=rc323.translated_coefficients(rows,reverse=reverse)
 assert len(scaled_prime)==278
 met=cert("129_four_vector_joint_moment")
 smin=F(met["actual_D_Gram_entry_lower"][0][0])/(2*B)
 smax=F(met["actual_D_Gram_entry_upper"][0][0])/(2*B)
 assert F(3)<smin<=smax<F(5)
 IV=rc323.IV
 roots=[IV(1)/IV(smin,smax).sqrt(),
       IV(5).sqrt()/IV(smin+H2,smax+H2).sqrt(),
       IV(3)/IV(smin+H4,smax+H4).sqrt()]
 H=rc323.harmonics(FAR)
 finite_center_lower=F(0)
 finite_center_upper=F(0)
 bins={"244_510":F(0),"512_798":F(0)}
 selected={}
 for n,coeff in (reversed(list(scaled_prime.items())) if reverse else scaled_prime.items()):
  a=F(2*n+1)
  e=(a/F(n*(n+1)),
      F(6*a,n*(n+1)*(n-2)*(n+3)),
      F(14*a,(n-4)*(n+5)*(n-2)*(n+3)))
  combined=sum((VEC[i]*roots[i]*(coeff[i]+e[i])
                for i in range(3)),IV(0)).grid(rc323.G)
  l=norm_absmin(combined)
  u=norm_absmax(combined)
  termlo=dn(l*l/(a*(H[n]+smax)))
  termhi=up(u*u/(a*(H[n]+smin)))
  assert termlo<=termhi
  finite_center_lower+=termlo
  finite_center_upper+=termhi
  bins["244_510" if n<512 else "512_798"]+=termhi
  if n in (244,246,248,250,256,510,512,700,798):
   selected[str(n)]={
     "signed_combined_original_prime_plus_endpoint_amplitude":combined.arr(),
     "actual_D_even_mode_energy_lower":str(termlo),
     "actual_D_even_mode_energy_upper":str(termhi)
   }
 finite_center_lower=dn(finite_center_lower)
 finite_center_upper=up(finite_center_upper)
 # Pinned RC323 entire true-source perturbation covers *every*
 # original input-log/weight, polynomial extension edge, original
 # RC46 regular remainder, and even pole high tail simultaneously.
 epsActual=F(c323["complete_original_high_source_error_upper"])
 assert 0<epsActual<F(1,10**11)
 finite_true_upper=up(sqrthi(finite_center_upper)+epsActual)
 finite_true_lower=dn(max(F(0),sqrtlo(finite_center_lower)-epsActual))
 assert finite_true_lower>0
 # Original n>=800 output lies inside the previously paid
 # n>=512 complete tails. Thus it is legal to bound it by
 # those earlier Parseval envelopes; the 512..798 part may
 # be overpaid, but is NEVER lost.
 t0=sqrthi(F(c318["all_D_high_output_512_to_infinity_energy_upper"]))
 t2=F(c320["complete_combination_infinite_high_norm_upper"])
 t4=F(c321["full_center_infinite_D_high_norm_upper"])
 # RC320/321 are center-tail measurements. Restore the entire
 # real-support/weight uncertainty and uniform kernel remainder
 # to those *infinite* tails. The original high signed pole
 # has geometric Taylor tail with z=B/2<3/5.
 epsReg=F(c46["regular_kernel_uniform_error_upper"])
 tail2Error=(F(c320["full_translation_arithmetic_L2_error_upper"])
              +10*B*epsReg+128*B*(B/2)**512)
 tail4Error=(F(c321["entire_signed_translation_L2_error_upper"])
              +10*B*epsReg+256*B*(B/2)**512)
 assert 0<tail2Error<F(1,10**16)
 assert 0<tail4Error<F(1,10**16)
 tailUpper=up(abs(VEC[0])*t0+abs(VEC[1])*(t2+tail2Error)
              +abs(VEC[2])*(t4+tail4Error))
 # Explicit orthogonal decomposition: n244..798 and n800+.
 totalT=up(sqrthi(finite_true_upper**2+tailUpper**2))
 assert totalT>finite_true_upper and totalT< F(old["original_pinned_whole_high_Tx_norm_upper"])
 # Represented three-mode energies are true, because their
 # signed original true-source source intervals were certified
 # independently in RC325/326. Subtract via Parseval to bound
 # the true OUTSIDE Tx energy. Use stronger lower from our
 # newly computed finite 244/246/248 if available.
 b325=cert("325_native_high_2x2")["low_R323_witness_native_high_response"]
 b248=c326["low_witness_high_248_signed_source_interval"]
 def absminpair(ar):
  a,b=map(F,ar)
  if a<=0<=b:return F(0)
  return min(abs(a),abs(b))
 representedEnergyOld=sum((absminpair(x)**2 for x in
  [b325["244"],b325["246"],b248]),F(0))
 representedEnergyNew=sum((F(selected[str(n)]["actual_D_even_mode_energy_lower"])
                             for n in (244,246,248)),F(0))
 representedEnergy=max(representedEnergyOld,representedEnergyNew)
 assert representedEnergy>0 and representedEnergy<totalT**2
 outsideT=up(sqrthi(totalT*totalT-representedEnergy))
 # The ACTUAL original signed C high off-block norm from RC327
 # pays the entire original finite and infinite CY output.
 y=list(map(F,c326["explicit_original_high_3mode_Ritz_trial"]))
 assert [str(x) for x in y]==old["actual_rational_R326_high_trial_y"]
 CYoutside=F(old["actual_full_high_action_outside_first_three_C_y_norm_upper"])
 Rrepresented=F(old["represented_three_high_residual_norm_upper"])
 Rout=up(outsideT+CYoutside)
 Rtot=up(sqrthi(Rrepresented**2+Rout**2))
 mu=F(cert("324_high_tail_smoothing")["inherited_even_244plus_global_floor"])
 assert mu>0
 penalty=up(Rtot*Rtot/mu)
 oldPenalty=F(old["RC314_correct_sign_complete_residual_penalty_upper"])
 assert penalty<oldPenalty*F(9,10),("signed finite cancellation insufficient")
 lowB=F(c323["original_low_quadratic_B_upper"])
 # This is still *not* a positive corrected Schur lower test.
 assert penalty>lowB
 return dict(
  milestone="RC328",
  parent_route_head="dcb33c606b704ba2ec93000c88c56ae340bda8a4",
  input_git_blob_pins=PINS,
  original_CC27_signed_D_operator=True,
  signed_original_combination="(3/25)v0-(23/8)w2+w4",
  exact_original_signed_even_finite_degrees=[244,798],
  computed_joint_signed_even_coefficients=278,
  Legendre_fixed_grid_decimal_digits=520,
  selected_joint_original_signed_high_mode_intervals=selected,
  original_combined_center_244to798_energy_lower=str(finite_center_lower),
  original_combined_center_244to798_energy_upper=str(finite_center_upper),
  original_combined_energy_244to510_upper=str(up(bins["244_510"])),
  original_combined_energy_512to798_upper=str(up(bins["512_798"])),
  whole_original_signed_source_perturbation_error_upper=str(epsActual),
  original_combined_actual_244to798_norm_lower=str(finite_true_lower),
  original_combined_actual_244to798_norm_upper=str(finite_true_upper),
  rigorously_inherited_P0_512plus_tail_norm_upper=str(up(t0)),
  rigorously_inherited_P2minusP0_512plus_tail_norm_upper=str(up(t2+tail2Error)),
  rigorously_inherited_P4minusP2_512plus_tail_norm_upper=str(up(t4+tail4Error)),
  whole_signed_combined_true_800plus_tail_norm_upper=str(tailUpper),
  original_combined_true_entire_high_Tx_norm_upper=str(totalT),
  inherited_old_Tx_whole_high_triangle_norm_upper=old["original_pinned_whole_high_Tx_norm_upper"],
  complete_signed_represented_three_mode_energy_lower=str(dn(representedEnergy)),
  true_entire_unrepresented_Tx_norm_upper=str(outsideT),
  RC327_paid_original_infinite_CYoutside_norm_upper=str(CYoutside),
  certified_represented_3mode_original_residual_norm_upper=str(Rrepresented),
  original_entire_unrepresented_residual_norm_upper=str(Rout),
  certified_original_entire_infinite_R_T_minus_CY_norm_upper=str(Rtot),
  certified_RC314_correct_sign_entire_residual_penalty_upper=str(penalty),
  RC327_inherited_entire_residual_penalty_upper=str(oldPenalty),
  proved_strict_sharpening_of_complete_original_signed_residual=True,
  unrepresented_original_Tx_CY_signed_covariance_computed=False,
  full_original_3D_Schur_positive=False,
  full_278_native_high_head_inverse_computed=False,
  full_infinite_C_inverse_computed=False,
  Stage_I_closed=False,F4=False,Lean=False,RH=False,
  next_cursor=(
   "RC329: reconstruct the original signed finite OUTSIDE "
   "high covariance <P_{250..798}Tx,P_{250..798}CY> using "
   "native high-to-high seven-prime translation overlaps "
   "and endpoint action, then pay the infinity tail. "
   "RC328 only reduces the complete Tx magnitude by "
   "sign-preserving 278-mode projection; full inverse and "
   "three-dimensional Schur positivity still OPEN."
  )
 )
if __name__=="__main__":
 ap=argparse.ArgumentParser()
 ap.add_argument("--output",type=Path,required=True)
 ap.add_argument("--replay",action="store_true")
 a=ap.parse_args()
 v=run(reverse=a.replay)
 if a.replay:assert v==json.loads(a.output.read_text(encoding="utf-8"))
 else:a.output.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n",encoding="utf-8")
 print("RC328: exact signed original 278-mode Tx norm + infinite Parseval tail, improved full residual, corrected Schur remains OPEN.")
