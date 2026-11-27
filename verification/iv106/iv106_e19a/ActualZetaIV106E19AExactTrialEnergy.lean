import WeilDefect.Arithmetic.ActualZetaIV106E18STrialDerivative

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped Interval

/-- Primitive of the exact squared unit polynomial, with the literal
width substituted. Coefficients are rational, not fitted values. -/
def neutralIV106E19AMassPrimitive (t : ℝ) : ℝ :=
  14641*t^19/371569606187500 - 14641*t^18/39112590125000 -
  616425847411*t^17/265965612850000 + 3082130730437*t^16/156450360500000 +
  76225274168624641*t^15/2205597187500 - 506898843754111141*t^14/1955629506250 +
  62517546709638514589*t^13/72637667375000 - 7806246095919824641*t^12/4693510815000 +
  111165795329915109814*t^11/53779811421875 - 336806322535864273923*t^10/195562950625000 +
  684032252180086754641*t^9/704026622250000 - 161589013548*t^8/442225 +
  270641699274*t^7/3095575 - 12000*t^6 + 720*t^5

def neutralIV106E19ADerivativePrimitive (t : ℝ) : ℝ :=
  1185921*t^17/332457016062500 - 1185921*t^16/39112590125000 -
  4045294598928*t^15/24445368828125 + 638731038231*t^14/514639343750 +
  49676013827609742163*t^13/25423183581250 - 49676087452014610177*t^12/3911259012500 +
  1945647446173545037977*t^11/53779811421875 - 413967597363499660973*t^10/6984391093750 +
  3614003063514082077971*t^9/58668885187500 - 330385600344528331923*t^8/7822518025000 +
  658405684061247269641*t^7/34223516359375 - 505197835644*t^6/88445 +
  2324334594192*t^5/2211125 - 108000*t^4 + 4800*t^3

/-- The unit-cell mass reserve uses the original E18I polynomial. -/
theorem neutralIV106E19AMass_unit :
    (11/3325:ℝ)*(∫ t in (0:ℝ)..1, (neutralIV106E18IPoly (11/3325) t)^2) =
      12994320639248774641/98293908912022687500000 := by
  have hd (t : ℝ) : HasDerivAt neutralIV106E19AMassPrimitive
      ((neutralIV106E18IPoly (11/3325) t)^2) t := by
    unfold neutralIV106E19AMassPrimitive neutralIV106E18IPoly
    have d0 := ((hasDerivAt_id t).pow 19).const_mul (14641/371569606187500:ℝ)
    have d1 := ((hasDerivAt_id t).pow 18).const_mul (-14641/39112590125000:ℝ)
    have d2 := ((hasDerivAt_id t).pow 17).const_mul (-616425847411/265965612850000:ℝ)
    have d3 := ((hasDerivAt_id t).pow 16).const_mul (3082130730437/156450360500000:ℝ)
    have d4 := ((hasDerivAt_id t).pow 15).const_mul (76225274168624641/2205597187500:ℝ)
    have d5 := ((hasDerivAt_id t).pow 14).const_mul (-506898843754111141/1955629506250:ℝ)
    have d6 := ((hasDerivAt_id t).pow 13).const_mul (62517546709638514589/72637667375000:ℝ)
    have d7 := ((hasDerivAt_id t).pow 12).const_mul (-7806246095919824641/4693510815000:ℝ)
    have d8 := ((hasDerivAt_id t).pow 11).const_mul (111165795329915109814/53779811421875:ℝ)
    have d9 := ((hasDerivAt_id t).pow 10).const_mul (-336806322535864273923/195562950625000:ℝ)
    have d10 := ((hasDerivAt_id t).pow 9).const_mul (684032252180086754641/704026622250000:ℝ)
    have d11 := ((hasDerivAt_id t).pow 8).const_mul (-161589013548/442225:ℝ)
    have d12 := ((hasDerivAt_id t).pow 7).const_mul (270641699274/3095575:ℝ)
    have d13 := ((hasDerivAt_id t).pow 6).const_mul (-12000:ℝ)
    have d14 := ((hasDerivAt_id t).pow 5).const_mul (720:ℝ)
    have h1 := d0.add d1
    have h2 := h1.add d2
    have h3 := h2.add d3
    have h4 := h3.add d4
    have h5 := h4.add d5
    have h6 := h5.add d6
    have h7 := h6.add d7
    have h8 := h7.add d8
    have h9 := h8.add d9
    have h10 := h9.add d10
    have h11 := h10.add d11
    have h12 := h11.add d12
    have h13 := h12.add d13
    have h14 := h13.add d14
    convert h14 using 1 <;>
      first | rfl | (funext x; simp only [Pi.add_apply, Pi.mul_apply, Pi.pow_apply, id_eq]; ring) |
        (simp only [Pi.add_apply, Pi.mul_apply, Pi.pow_apply, id_eq]; ring)
  have hc : Continuous (fun t : ℝ => (neutralIV106E18IPoly (11/3325) t)^2) := by
    unfold neutralIV106E18IPoly
    fun_prop
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt (fun t _ => hd t)
    hc.intervalIntegrable]
  norm_num [neutralIV106E19AMassPrimitive]

/-- Unit-cell derivative energy retains the physical inverse-width factor. -/
theorem neutralIV106E19ADerivative_unit :
    (∫ t in (0:ℝ)..1, (neutralIV106E18SDPoly (11/3325) t)^2)/(11/3325:ℝ) =
      27926390440838204641/16514364829462500 := by
  have hd (t : ℝ) : HasDerivAt neutralIV106E19ADerivativePrimitive
      ((neutralIV106E18SDPoly (11/3325) t)^2) t := by
    unfold neutralIV106E19ADerivativePrimitive neutralIV106E18SDPoly
      neutralIV106E18SB4 neutralIV106E18K1B2
    have d0 := ((hasDerivAt_id t).pow 17).const_mul (1185921/332457016062500:ℝ)
    have d1 := ((hasDerivAt_id t).pow 16).const_mul (-1185921/39112590125000:ℝ)
    have d2 := ((hasDerivAt_id t).pow 15).const_mul (-4045294598928/24445368828125:ℝ)
    have d3 := ((hasDerivAt_id t).pow 14).const_mul (638731038231/514639343750:ℝ)
    have d4 := ((hasDerivAt_id t).pow 13).const_mul (49676013827609742163/25423183581250:ℝ)
    have d5 := ((hasDerivAt_id t).pow 12).const_mul (-49676087452014610177/3911259012500:ℝ)
    have d6 := ((hasDerivAt_id t).pow 11).const_mul (1945647446173545037977/53779811421875:ℝ)
    have d7 := ((hasDerivAt_id t).pow 10).const_mul (-413967597363499660973/6984391093750:ℝ)
    have d8 := ((hasDerivAt_id t).pow 9).const_mul (3614003063514082077971/58668885187500:ℝ)
    have d9 := ((hasDerivAt_id t).pow 8).const_mul (-330385600344528331923/7822518025000:ℝ)
    have d10 := ((hasDerivAt_id t).pow 7).const_mul (658405684061247269641/34223516359375:ℝ)
    have d11 := ((hasDerivAt_id t).pow 6).const_mul (-505197835644/88445:ℝ)
    have d12 := ((hasDerivAt_id t).pow 5).const_mul (2324334594192/2211125:ℝ)
    have d13 := ((hasDerivAt_id t).pow 4).const_mul (-108000:ℝ)
    have d14 := ((hasDerivAt_id t).pow 3).const_mul (4800:ℝ)
    have h1 := d0.add d1
    have h2 := h1.add d2
    have h3 := h2.add d3
    have h4 := h3.add d4
    have h5 := h4.add d5
    have h6 := h5.add d6
    have h7 := h6.add d7
    have h8 := h7.add d8
    have h9 := h8.add d9
    have h10 := h9.add d10
    have h11 := h10.add d11
    have h12 := h11.add d12
    have h13 := h12.add d13
    have h14 := h13.add d14
    convert h14 using 1 <;>
      first | rfl | (funext x; simp only [Pi.add_apply, Pi.mul_apply, Pi.pow_apply, id_eq]; ring) |
        (simp only [Pi.add_apply, Pi.mul_apply, Pi.pow_apply, id_eq]; ring)
  have hc : Continuous (fun t : ℝ => (neutralIV106E18SDPoly (11/3325) t)^2) := by
    unfold neutralIV106E18SDPoly neutralIV106E18SB4 neutralIV106E18K1B2
    fun_prop
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt (fun t _ => hd t)
    hc.intervalIntegrable]
  norm_num [neutralIV106E19ADerivativePrimitive]

theorem neutralIV106E19ARational_reserve :
    (4:ℝ)*(12994320639248774641/98293908912022687500000) +
      (27926390440838204641/16514364829462500)/36 < 49 := by norm_num

#print axioms neutralIV106E19AMass_unit
#print axioms neutralIV106E19ADerivative_unit
#print axioms neutralIV106E19ARational_reserve
end
end WeilDefect
