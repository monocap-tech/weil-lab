import WeilDefect.Morphology.NeutralGaussianFilteredSchwartz
import Mathlib.Analysis.Calculus.BumpFunction.InnerProduct

namespace WeilDefect

noncomputable section

open Set Filter
open scoped SchwartzMap Topology ContDiff

/-- Fixed smooth bump used to truncate Schwartz functions on the real line. -/
def neutralGaussianCutoffBump : ContDiffBump (0 : ℝ) where
  rIn := 1
  rOut := 2
  rIn_pos := by norm_num
  rIn_lt_rOut := by norm_num

/-- Expanding smooth cutoff at radius `R`. -/
def neutralGaussianCutoffScalar (R x : ℝ) : ℝ :=
  neutralGaussianCutoffBump (R⁻¹ * x)

theorem neutralGaussianCutoffScalar_contDiff (R : ℝ) :
    ContDiff ℝ ∞ (neutralGaussianCutoffScalar R) := by
  unfold neutralGaussianCutoffScalar
  exact neutralGaussianCutoffBump.contDiff.comp (by fun_prop)

theorem neutralGaussianCutoffScalar_compact {R : ℝ} (hR : R ≠ 0) :
    HasCompactSupport (neutralGaussianCutoffScalar R) := by
  unfold neutralGaussianCutoffScalar
  simpa [smul_eq_mul] using
    neutralGaussianCutoffBump.hasCompactSupport.comp_smul
      (G₀ := ℝ) (c := R⁻¹) (inv_ne_zero hR)

theorem neutralGaussianCutoffScalar_one
    {R x : ℝ} (hR : 0 < R) (hx : |x| ≤ R) :
    neutralGaussianCutoffScalar R x = 1 := by
  unfold neutralGaussianCutoffScalar
  apply neutralGaussianCutoffBump.one_of_mem_closedBall
  simp only [Metric.mem_closedBall, dist_zero_right, Real.norm_eq_abs]
  rw [abs_mul, abs_inv, abs_of_pos hR]
  exact (inv_mul_le_iff₀ hR).2 hx

/-- The fixed bump itself, bundled as a Schwartz function. -/
def neutralGaussianCutoffBumpSchwartz : SchwartzMap ℝ ℝ :=
  neutralGaussianCutoffBump.hasCompactSupport.toSchwartzMap
    neutralGaussianCutoffBump.contDiff

def neutralGaussianCutoffDerivativeBound (n : ℕ) : ℝ :=
  SchwartzMap.seminorm ℝ 0 n neutralGaussianCutoffBumpSchwartz + 1

theorem neutralGaussianCutoffDerivativeBound_nonneg (n : ℕ) :
    0 ≤ neutralGaussianCutoffDerivativeBound n := by
  unfold neutralGaussianCutoffDerivativeBound
  positivity

theorem neutralGaussianCutoffScalar_derivative_bound
    {R : ℝ} (hR : 1 ≤ R) (n : ℕ) (x : ℝ) :
    ‖iteratedFDeriv ℝ n (neutralGaussianCutoffScalar R) x‖ ≤
      SchwartzMap.seminorm ℝ 0 n neutralGaussianCutoffBumpSchwartz := by
  have hRpos : 0 < R := zero_lt_one.trans_le hR
  have he := congrFun
    (iteratedFDeriv_comp_const_smul
      R⁻¹
      (neutralGaussianCutoffBump.contDiff (n := (n : ℕ∞)))) x
  change ‖iteratedFDeriv ℝ n
      (fun z : ℝ => neutralGaussianCutoffBump (R⁻¹ • z)) x‖ ≤ _
  rw [he, norm_smul, Real.norm_eq_abs, abs_of_nonneg (by positivity)]
  have hp : R⁻¹ ^ n ≤ 1 :=
    pow_le_one₀ (by positivity) (inv_le_one_of_one_le₀ hR)
  exact
    (mul_le_of_le_one_left (norm_nonneg _) hp).trans
      (SchwartzMap.norm_iteratedFDeriv_le_seminorm
        ℝ neutralGaussianCutoffBumpSchwartz n _)

/-- Multiply a Schwartz test by the expanding compact cutoff. -/
def neutralGaussianSchwartzCutoff
    (R : ℝ) (f : SchwartzMap ℝ ℂ) : SchwartzMap ℝ ℂ :=
  SchwartzMap.smulLeftCLM ℂ
    (fun x : ℝ => (neutralGaussianCutoffScalar R x : ℂ)) f

theorem neutralGaussianCutoffScalar_temperate {R : ℝ} (hR : R ≠ 0) :
    Function.HasTemperateGrowth
      (fun x : ℝ => (neutralGaussianCutoffScalar R x : ℂ)) :=
  Complex.ofRealCLM.hasTemperateGrowth.comp
    ((neutralGaussianCutoffScalar_compact hR).hasTemperateGrowth
      (neutralGaussianCutoffScalar_contDiff R))

@[simp]
theorem neutralGaussianSchwartzCutoff_apply
    {R : ℝ} (hR : R ≠ 0) (f : SchwartzMap ℝ ℂ) (x : ℝ) :
    neutralGaussianSchwartzCutoff R f x =
      (neutralGaussianCutoffScalar R x : ℂ) * f x := by
  simp [neutralGaussianSchwartzCutoff,
    neutralGaussianCutoffScalar_temperate hR, smul_eq_mul]

theorem neutralGaussianSchwartzCutoff_compact
    {R : ℝ} (hR : R ≠ 0) (f : SchwartzMap ℝ ℂ) :
    HasCompactSupport (neutralGaussianSchwartzCutoff R f : ℝ → ℂ) := by
  have hc :
      HasCompactSupport
        (fun x : ℝ => (neutralGaussianCutoffScalar R x : ℂ) * f x) :=
    ((neutralGaussianCutoffScalar_compact hR).comp_left
      (g := Complex.ofReal) (by simp)).mul_right
  convert hc using 1
  funext x
  exact neutralGaussianSchwartzCutoff_apply hR f x

theorem neutralGaussianCutoff_sub_one_derivative_bound
    {R : ℝ} (hR : 1 ≤ R) (n : ℕ) (x : ℝ) :
    ‖iteratedFDeriv ℝ n
        (fun y => neutralGaussianCutoffScalar R y - 1) x‖ ≤
      neutralGaussianCutoffDerivativeBound n := by
  change ‖iteratedFDeriv ℝ n
      (neutralGaussianCutoffScalar R - fun _ : ℝ => (1 : ℝ)) x‖ ≤ _
  rw [iteratedFDeriv_sub_apply
    ((neutralGaussianCutoffScalar_contDiff R).of_le (by simp)).contDiffAt
    contDiffAt_const]
  apply (norm_sub_le _ _).trans
  apply add_le_add (neutralGaussianCutoffScalar_derivative_bound hR n x)
  cases n with
  | zero => simp [neutralGaussianCutoffDerivativeBound]
  | succ n => simp [iteratedFDeriv_succ_const, neutralGaussianCutoffDerivativeBound]

theorem neutralGaussianSchwartzCutoff_sub_apply
    {R : ℝ} (hR : R ≠ 0) (f : SchwartzMap ℝ ℂ) :
    ((neutralGaussianSchwartzCutoff R f - f : SchwartzMap ℝ ℂ) : ℝ → ℂ)
      =
    fun x => (neutralGaussianCutoffScalar R x - 1) • f x := by
  funext x
  simp [neutralGaussianSchwartzCutoff_apply hR, sub_smul, Complex.real_smul]

def neutralGaussianSchwartzCutoffBound
    (k n : ℕ) (f : SchwartzMap ℝ ℂ) : ℝ :=
  ∑ i ∈ Finset.range (n + 1),
    (n.choose i : ℝ) * neutralGaussianCutoffDerivativeBound i *
      SchwartzMap.seminorm ℝ k (n - i) f

theorem neutralGaussianSchwartzCutoffBound_nonneg
    (k n : ℕ) (f : SchwartzMap ℝ ℂ) :
    0 ≤ neutralGaussianSchwartzCutoffBound k n f := by
  unfold neutralGaussianSchwartzCutoffBound
  exact Finset.sum_nonneg fun i _ =>
    mul_nonneg
      (mul_nonneg (Nat.cast_nonneg _)
        (neutralGaussianCutoffDerivativeBound_nonneg i))
      (apply_nonneg _ _)

theorem neutralGaussianSchwartzCutoff_derivative_bound
    {R : ℝ} (hR : 1 ≤ R) (k n : ℕ)
    (f : SchwartzMap ℝ ℂ) (x : ℝ) :
    ‖x‖ ^ k *
        ‖iteratedFDeriv ℝ n
          (neutralGaussianSchwartzCutoff R f - f : SchwartzMap ℝ ℂ) x‖
      ≤
    neutralGaussianSchwartzCutoffBound k n f := by
  rw [neutralGaussianSchwartzCutoff_sub_apply
    (ne_of_gt (zero_lt_one.trans_le hR))]
  have hd :=
    norm_iteratedFDeriv_smul_le
      ((neutralGaussianCutoffScalar_contDiff R).sub
        (contDiff_const (c := (1 : ℝ))))
      (f.smooth ⊤) x (n := n) (by simp)
  apply (mul_le_mul_of_nonneg_left hd (by positivity)).trans
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro i hi
  calc
    _ = (n.choose i : ℝ)
        * ‖iteratedFDeriv ℝ i
            (fun y => neutralGaussianCutoffScalar R y - 1) x‖
        * (‖x‖ ^ k * ‖iteratedFDeriv ℝ (n - i) f x‖) := by ring
    _ ≤ _ := mul_le_mul
      (mul_le_mul_of_nonneg_left
        (neutralGaussianCutoff_sub_one_derivative_bound hR i x)
        (by positivity))
      (SchwartzMap.le_seminorm ℝ k (n - i) f x)
      (by positivity)
      (mul_nonneg (Nat.cast_nonneg _)
        (neutralGaussianCutoffDerivativeBound_nonneg i))

theorem neutralGaussianSchwartzCutoff_derivative_zero
    {R : ℝ} (hR : 0 < R) (n : ℕ)
    (f : SchwartzMap ℝ ℂ) {x : ℝ} (hx : |x| < R) :
    iteratedFDeriv ℝ n
      (neutralGaussianSchwartzCutoff R f - f : SchwartzMap ℝ ℂ) x = 0 := by
  have he :
      (neutralGaussianSchwartzCutoff R f - f : SchwartzMap ℝ ℂ)
        =ᶠ[𝓝 x] (fun _ : ℝ => (0 : ℂ)) := by
    filter_upwards
      [((continuous_abs : Continuous fun x : ℝ => |x|).isOpen_preimage
        (Set.Iio R) isOpen_Iio).mem_nhds hx] with y hy
    change neutralGaussianSchwartzCutoff R f y - f y = 0
    rw [neutralGaussianSchwartzCutoff_apply (ne_of_gt hR),
      neutralGaussianCutoffScalar_one hR (le_of_lt hy)]
    simp
  have hd := (he.iteratedFDeriv ℝ n).self_of_nhds
  simpa using hd

theorem neutralGaussianSchwartzCutoff_seminorm_le
    {R : ℝ} (hR : 1 ≤ R) (k n : ℕ)
    (f : SchwartzMap ℝ ℂ) :
    SchwartzMap.seminorm ℝ k n
      (neutralGaussianSchwartzCutoff R f - f)
      ≤
    neutralGaussianSchwartzCutoffBound (k + 1) n f / R := by
  have hRpos : 0 < R := zero_lt_one.trans_le hR
  apply SchwartzMap.seminorm_le_bound ℝ k n _
    (div_nonneg
      (neutralGaussianSchwartzCutoffBound_nonneg _ _ _) hRpos.le)
  intro x
  by_cases hx : |x| < R
  · have hz :=
      neutralGaussianSchwartzCutoff_derivative_zero hRpos n f hx
    rw [hz, norm_zero, mul_zero]
    exact div_nonneg
      (neutralGaussianSchwartzCutoffBound_nonneg _ _ _) hRpos.le
  · have hb :=
      neutralGaussianSchwartzCutoff_derivative_bound hR (k + 1) n f x
    rw [le_div_iff₀ hRpos]
    have hxR : R ≤ |x| := le_of_not_gt hx
    calc
      |x| ^ k *
          ‖iteratedFDeriv ℝ n
            (neutralGaussianSchwartzCutoff R f - f : SchwartzMap ℝ ℂ) x‖
          * R
        ≤
      |x| ^ k *
          ‖iteratedFDeriv ℝ n
            (neutralGaussianSchwartzCutoff R f - f : SchwartzMap ℝ ℂ) x‖
          * |x| := by
            exact mul_le_mul_of_nonneg_left hxR (by positivity)
      _ =
      |x| ^ (k + 1) *
          ‖iteratedFDeriv ℝ n
            (neutralGaussianSchwartzCutoff R f - f : SchwartzMap ℝ ℂ) x‖ := by
            ring
      _ ≤ _ := by simpa [Real.norm_eq_abs] using hb

/-- Expanding compact cutoffs converge to any Schwartz function in the full Schwartz topology. -/
theorem neutralGaussianSchwartzCutoff_tendsto
    (f : SchwartzMap ℝ ℂ) :
    Tendsto
      (fun N : ℕ => neutralGaussianSchwartzCutoff ((N : ℝ) + 1) f)
      atTop (𝓝 f) := by
  apply (schwartz_withSeminorms ℝ ℝ ℂ).tendsto_nhds _ _ |>.mpr
  rintro ⟨k, n⟩ ε hε
  have hr :
      Tendsto (fun N : ℕ => (N : ℝ) + 1) atTop atTop :=
    (tendsto_natCast_atTop_atTop :
      Tendsto (fun N : ℕ => (N : ℝ)) atTop atTop).atTop_add
        (tendsto_const_nhds (x := (1 : ℝ)))
  have hb :
      Tendsto
        (fun N : ℕ =>
          neutralGaussianSchwartzCutoffBound (k + 1) n f / ((N : ℝ) + 1))
        atTop (𝓝 0) := by
    simpa only [div_eq_mul_inv, mul_zero, Pi.inv_apply] using
      tendsto_const_nhds.mul hr.inv_tendsto_atTop
  filter_upwards [hb.eventually (gt_mem_nhds hε)] with N hN
  exact
    (neutralGaussianSchwartzCutoff_seminorm_le
      (R := (N : ℝ) + 1)
      (by linarith [Nat.cast_nonneg (α := ℝ) N]) k n f).trans_lt hN

/-- The actual compactly supported cutoff sequence for the moving filtered mode. -/
def movingGaussianFilteredModeCompactCutoff
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (Ck : ℂ) (R : ℝ) (hR : 0 < R)
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (N : ℕ) : SchwartzMap ℝ ℂ :=
  neutralGaussianSchwartzCutoff ((N : ℝ) + 1)
    (movingGaussianFilteredModeSchwartz Ck R hR carrier)

theorem movingGaussianFilteredModeCompactCutoff_compact
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (Ck : ℂ) (R : ℝ) (hR : 0 < R)
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (N : ℕ) :
    HasCompactSupport
      (movingGaussianFilteredModeCompactCutoff Ck R hR carrier N) := by
  exact neutralGaussianSchwartzCutoff_compact
    (by positivity : (N : ℝ) + 1 ≠ 0)
    (movingGaussianFilteredModeSchwartz Ck R hR carrier)

theorem movingGaussianFilteredModeCompactCutoff_tendsto
    {c : ℝ}
    {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (Ck : ℂ) (R : ℝ) (hR : 0 < R)
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) :
    Tendsto
      (movingGaussianFilteredModeCompactCutoff Ck R hR carrier)
      atTop
      (𝓝 (movingGaussianFilteredModeSchwartz Ck R hR carrier)) := by
  exact neutralGaussianSchwartzCutoff_tendsto
    (movingGaussianFilteredModeSchwartz Ck R hR carrier)

end

end WeilDefect
