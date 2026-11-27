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
    first | convert (by fun_prop : HasDerivAt (fun x : ℝ => _ ) _ t) using 1 <;> ring | fun_prop
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
    first | convert (by fun_prop : HasDerivAt (fun x : ℝ => _ ) _ t) using 1 <;> ring | fun_prop
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
