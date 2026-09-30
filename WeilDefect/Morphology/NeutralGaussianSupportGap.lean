import WeilDefect.Morphology.NeutralWeilResidualCarrier
import Mathlib.Tactic

namespace WeilDefect

noncomputable section

open MeasureTheory

/--
Physical Gaussian envelope centered on the compact support interval [-c,c].

This is the modulus profile that appears after the moving-frequency Gaussian
filter is transferred to physical space.  RPB-88 isolates only the support-gap
geometry and pointwise domination; the later tail integral is not included
here.
-/
def gaussianSupportEnvelope (R c x : ℝ) : ℝ :=
  Real.exp (-R * (|x| - c) ^ 2 / 4)

/--
Outside the strict interval (-a,a), the absolute value is at least a whenever
a is nonnegative.
-/
theorem radius_le_abs_of_not_mem_Ioo
    {a x : ℝ}
    (ha : 0 ≤ a)
    (hx : x ∉ Set.Ioo (-a) a) :
    a ≤ |x| := by
  have hx' : x ≤ -a ∨ a ≤ x := by
    by_cases hleft : x ≤ -a
    · exact Or.inl hleft
    · right
      have hleft' : -a < x := lt_of_not_ge hleft
      by_contra hright
      have hright' : x < a := lt_of_not_ge hright
      exact hx ⟨hleft', hright'⟩
  rcases hx' with hleft | hright
  · have hx0 : x ≤ 0 :=
      hleft.trans (neg_nonpos.mpr ha)
    rw [abs_of_nonpos hx0]
    linarith
  · have hx0 : 0 ≤ x :=
      ha.trans hright
    rw [abs_of_nonneg hx0]
    exact hright

/--
Strict support-gap geometry: if 0 ≤ c < a and x lies outside (-a,a), then
the distance proxy |x|-c is at least the collar width a-c.
-/
theorem supportGap_le_abs_sub
    {c a x : ℝ}
    (hc : 0 ≤ c)
    (hca : c < a)
    (hx : x ∉ Set.Ioo (-a) a) :
    a - c ≤ |x| - c := by
  have ha : 0 ≤ a :=
    hc.trans (le_of_lt hca)
  exact sub_le_sub_right
    (radius_le_abs_of_not_mem_Ioo ha hx) c

/--
Squared version of the support-gap inequality, used by the Gaussian exponent.
-/
theorem supportGap_sq_le_abs_sub_sq
    {c a x : ℝ}
    (hc : 0 ≤ c)
    (hca : c < a)
    (hx : x ∉ Set.Ioo (-a) a) :
    (a - c) ^ 2 ≤ (|x| - c) ^ 2 := by
  have hgap := supportGap_le_abs_sub hc hca hx
  have hgap0 : 0 ≤ a - c :=
    sub_nonneg.mpr (le_of_lt hca)
  have hxgap0 : 0 ≤ |x| - c :=
    hgap0.trans hgap
  nlinarith

/--
The physical Gaussian envelope on the exterior is bounded by the value forced
by the positive support gap.
-/
theorem gaussianSupportEnvelope_le_gap
    {R c a x : ℝ}
    (hR : 0 ≤ R)
    (hc : 0 ≤ c)
    (hca : c < a)
    (hx : x ∉ Set.Ioo (-a) a) :
    gaussianSupportEnvelope R c x
      ≤ Real.exp (-R * (a - c) ^ 2 / 4) := by
  unfold gaussianSupportEnvelope
  apply Real.exp_le_exp.mpr
  have hsquare :=
    supportGap_sq_le_abs_sub_sq hc hca hx
  have hmul :
      R * (a - c) ^ 2 ≤
        R * (|x| - c) ^ 2 :=
    mul_le_mul_of_nonneg_left hsquare hR
  nlinarith

/--
Pointwise product domination before using the support gap.

The hypothesis on g is exactly the physical Gaussian-filter envelope that the
next F-3 subpass must derive from the actual Gaussian convolution kernel and
the compact support of the F-1 mode.
-/
theorem residual_mul_gaussianEnvelope_bound
    {c R A : ℝ}
    (residual : NeutralExponentialResidualCarrier c)
    (g : ℝ → ℂ)
    (hA : 0 ≤ A)
    (hg :
      ∀ x : ℝ,
        ‖g x‖
          ≤ A * Real.sqrt R
              * gaussianSupportEnvelope R c x)
    (x : ℝ) :
    ‖residual.q x * g x‖
      ≤
      residual.growthConstant
        * Real.exp (residual.growthRate * |x|)
        * (A * Real.sqrt R
            * gaussianSupportEnvelope R c x) := by
  rw [norm_mul]
  exact mul_le_mul
    (residual.growth_bound x)
    (hg x)
    (norm_nonneg _)
    (mul_nonneg
      residual.growthConstant_nonneg
      (Real.exp_nonneg _))

/--
Exterior pointwise domination after inserting the positive support gap.

This is the first load-bearing F-3 estimate.  It still retains the residual's
fixed exponential growth in |x|; the next pass must integrate/complete the
square against the remaining Gaussian tail.
-/
theorem residual_mul_gaussianExterior_bound
    {c R A x : ℝ}
    (residual : NeutralExponentialResidualCarrier c)
    (hc : 0 ≤ c)
    (hR : 0 ≤ R)
    (hA : 0 ≤ A)
    (g : ℝ → ℂ)
    (hg :
      ∀ y : ℝ,
        ‖g y‖
          ≤ A * Real.sqrt R
              * gaussianSupportEnvelope R c y)
    (hx : x ∉ Set.Ioo (-residual.a) residual.a) :
    ‖residual.q x * g x‖
      ≤
      residual.growthConstant
        * Real.exp (residual.growthRate * |x|)
        * (A * Real.sqrt R
            * Real.exp
                (-R * (residual.a - c) ^ 2 / 4)) := by
  have henv :
      gaussianSupportEnvelope R c x
        ≤ Real.exp
            (-R * (residual.a - c) ^ 2 / 4) :=
    gaussianSupportEnvelope_le_gap
      hR hc residual.strict hx
  calc
    ‖residual.q x * g x‖
        ≤ residual.growthConstant
            * Real.exp (residual.growthRate * |x|)
            * (A * Real.sqrt R
                * gaussianSupportEnvelope R c x) :=
      residual_mul_gaussianEnvelope_bound
        residual g hA hg x
    _ ≤ residual.growthConstant
            * Real.exp (residual.growthRate * |x|)
            * (A * Real.sqrt R
                * Real.exp
                    (-R * (residual.a - c) ^ 2 / 4)) := by
      apply mul_le_mul_of_nonneg_left
      · apply mul_le_mul_of_nonneg_left henv
        exact mul_nonneg hA (Real.sqrt_nonneg R)
      · exact mul_nonneg
          residual.growthConstant_nonneg
          (Real.exp_nonneg _)


/--
Convention-parametric moving Gaussian physical kernel.

The scalar `Ck` retains the fixed Fourier-normalization constant explicitly.
Only its norm matters for the support-gap envelope.
-/
def movingGaussianPhysicalKernel
    (Ck : ℂ) (R z : ℝ) : ℂ :=
  Ck
    * (Real.sqrt R : ℂ)
    * (Real.exp (-R * |z| ^ 2 / 4) : ℂ)
    * Complex.exp (((R * z : ℝ) : ℂ) * Complex.I)

/-- Exact modulus of the moving Gaussian physical kernel. -/
theorem norm_movingGaussianPhysicalKernel
    (Ck : ℂ) (R z : ℝ)
    (hR : 0 ≤ R) :
    ‖movingGaussianPhysicalKernel Ck R z‖
      =
    ‖Ck‖ * Real.sqrt R
      * Real.exp (-R * |z| ^ 2 / 4) := by
  have hgauss :
      ‖((Real.exp (-R * |z| ^ 2 / 4) : ℝ) : ℂ)‖
        = Real.exp (-R * |z| ^ 2 / 4) := by
    rw [Complex.norm_exp]
    simp
  have hphase :
      ‖Complex.exp (((R * z : ℝ) : ℂ) * Complex.I)‖ = 1 := by
    rw [Complex.norm_exp]
    simp
  rw [movingGaussianPhysicalKernel, norm_mul, norm_mul, norm_mul,
    hgauss, hphase]
  simp [Real.norm_eq_abs, abs_of_nonneg (Real.sqrt_nonneg R), mul_assoc]

/--
The concrete F-1 representative is integrable on its certified compact support
interval.
-/
theorem neutralPhysicalRepresentative_integrableOn
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) :
    IntegrableOn carrier.h (Set.Icc (-c) c) volume := by
  exact
    (carrier.h_memLp.locallyIntegrable
      (by norm_num)).integrableOn_isCompact isCompact_Icc

/-- Compact L1 mass of the concrete F-1 representative. -/
def neutralPhysicalCompactL1Mass
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) : ℝ :=
  ∫ y in Set.Icc (-c) c, ‖carrier.h y‖

theorem neutralPhysicalCompactL1Mass_nonneg
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) :
    0 ≤ neutralPhysicalCompactL1Mass carrier := by
  unfold neutralPhysicalCompactL1Mass
  exact integral_nonneg (fun _ => norm_nonneg _)

/--
Actual physical moving-Gaussian filtered mode of the certified F-1
representative.
-/
def movingGaussianFilteredMode
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (Ck : ℂ) (R : ℝ)
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (x : ℝ) : ℂ :=
  ∫ y in Set.Icc (-c) c,
    carrier.h y * movingGaussianPhysicalKernel Ck R (x - y)

/--
For y in [-c,c] and x outside (-a,a), the physical kernel displacement
inherits the same strict collar a-c.
-/
theorem supportGap_le_abs_sub_point
    {c a x y : ℝ}
    (hc : 0 ≤ c)
    (hca : c < a)
    (hx : x ∉ Set.Ioo (-a) a)
    (hy : y ∈ Set.Icc (-c) c) :
    a - c ≤ |x - y| := by
  have ha : 0 ≤ a := hc.trans (le_of_lt hca)
  have hxabs : a ≤ |x| :=
    radius_le_abs_of_not_mem_Ioo ha hx
  have hyabs : |y| ≤ c := by
    exact (abs_le).2 hy
  calc
    a - c ≤ |x| - |y| := sub_le_sub hxabs hyabs
    _ ≤ |x - y| := abs_sub_abs_le_abs_sub x y

/--
Pointwise exterior modulus bound for the actual moving Gaussian physical
kernel.
-/
theorem movingGaussianPhysicalKernel_norm_le_gap
    {Ck : ℂ} {R c a x y : ℝ}
    (hR : 0 ≤ R)
    (hc : 0 ≤ c)
    (hca : c < a)
    (hx : x ∉ Set.Ioo (-a) a)
    (hy : y ∈ Set.Icc (-c) c) :
    ‖movingGaussianPhysicalKernel Ck R (x - y)‖
      ≤
    ‖Ck‖ * Real.sqrt R
      * Real.exp (-R * (a - c) ^ 2 / 4) := by
  rw [norm_movingGaussianPhysicalKernel Ck R (x - y) hR]
  have hgap := supportGap_le_abs_sub_point hc hca hx hy
  have hgap0 : 0 ≤ a - c := sub_nonneg.mpr (le_of_lt hca)
  have hsq : (a - c) ^ 2 ≤ |x - y| ^ 2 := by
    nlinarith [sq_nonneg (|x - y| - (a - c))]
  have hexp :
      Real.exp (-R * |x - y| ^ 2 / 4)
        ≤ Real.exp (-R * (a - c) ^ 2 / 4) := by
    apply Real.exp_le_exp.mpr
    have hmul :
        R * (a - c) ^ 2 ≤ R * |x - y| ^ 2 :=
      mul_le_mul_of_nonneg_left hsq hR
    nlinarith
  exact mul_le_mul_of_nonneg_left hexp
    (mul_nonneg (norm_nonneg Ck) (Real.sqrt_nonneg R))

/--
Exterior Gaussian envelope for the actual filtered F-1 mode.

This is the corrected RPB-90 form: the estimate is asserted only outside the
strict enlarged interval, where the support gap is available.  No global
interior envelope is claimed.
-/
theorem movingGaussianFilteredMode_norm_le_exterior
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (Ck : ℂ) (R x : ℝ)
    (hc : 0 ≤ c)
    (hR : 0 ≤ R)
    (hx : x ∉ Set.Ioo (-residual.a) residual.a) :
    ‖movingGaussianFilteredMode Ck R carrier x‖
      ≤
    (‖Ck‖ * Real.sqrt R
      * Real.exp (-R * (residual.a - c) ^ 2 / 4))
      * neutralPhysicalCompactL1Mass carrier := by
  let K : ℝ :=
    ‖Ck‖ * Real.sqrt R
      * Real.exp (-R * (residual.a - c) ^ 2 / 4)
  have hInt :
      IntegrableOn carrier.h (Set.Icc (-c) c) volume :=
    neutralPhysicalRepresentative_integrableOn carrier
  have hKernelCont :
      Continuous
        (fun y : ℝ =>
          movingGaussianPhysicalKernel Ck R (x - y)) := by
    unfold movingGaussianPhysicalKernel
    fun_prop
  have hProd :
      IntegrableOn
        (fun y : ℝ =>
          carrier.h y * movingGaussianPhysicalKernel Ck R (x - y))
        (Set.Icc (-c) c) volume := by
    exact hInt.mul_continuousOn
      hKernelCont.continuousOn isCompact_Icc
  calc
    ‖movingGaussianFilteredMode Ck R carrier x‖
        ≤ ∫ y in Set.Icc (-c) c,
            ‖carrier.h y
              * movingGaussianPhysicalKernel Ck R (x - y)‖ := by
      unfold movingGaussianFilteredMode
      exact norm_integral_le_integral_norm _
    _ ≤ ∫ y in Set.Icc (-c) c,
          K * ‖carrier.h y‖ := by
      refine setIntegral_mono_ae_restrict
        hProd.norm
        (hInt.norm.const_mul K) ?_
      filter_upwards [self_mem_ae_restrict measurableSet_Icc] with y hy
      rw [norm_mul]
      calc
        ‖carrier.h y‖
            * ‖movingGaussianPhysicalKernel Ck R (x - y)‖
            ≤ ‖carrier.h y‖ * K := by
              apply mul_le_mul_of_nonneg_left
              · exact movingGaussianPhysicalKernel_norm_le_gap
                  hR hc residual.strict hx hy
              · exact norm_nonneg _
        _ = K * ‖carrier.h y‖ := by ring
    _ = K * neutralPhysicalCompactL1Mass carrier := by
      rw [integral_const_mul]
      rfl
    _ = (‖Ck‖ * Real.sqrt R
          * Real.exp (-R * (residual.a - c) ^ 2 / 4))
          * neutralPhysicalCompactL1Mass carrier := by
      rfl

end

end WeilDefect
