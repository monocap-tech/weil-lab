import WeilDefect.MasterRecon.V10B5c
import WeilDefect.MasterRecon.V10B5a
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Analysis.Complex.RealDeriv

/-! V10B5d: literal Mellin rectangle evaluation, continuity of
the outer integral, and bounded sampling for an arbitrary strip
sample bank with an explicit multiplicity-count hypothesis. -/
namespace WeilDefect.MasterRecon.V10B5d

open Set MeasureTheory
open scoped Interval ENNReal BigOperators

open V10B5c (angularMoment)

theorem continuous_unit_integral (F : ℝ → ℝ → ℝ)
    (hF : Continuous (fun p : ℝ × ℝ => F p.1 p.2)) (b : ℝ) :
    Continuous (fun x => ∫ y in b..b+1, F x y) := by
  have h : Continuous (fun x => ∫ y in Icc b (b+1), F x y) :=
    continuous_parametric_integral_of_continuous
      (f := F) hF isCompact_Icc
  convert h using 1
  funext x
  rw [intervalIntegral.integral_of_le (by linarith : b ≤ b+1),
    integral_Icc_eq_integral_Ioc]

theorem row_continuous (H Y : ℝ → ℝ → ℂ)
    (hH : Continuous (fun p : ℝ × ℝ => H p.1 p.2))
    (hY : Continuous (fun p : ℝ × ℝ => Y p.1 p.2)) (b : ℝ) :
    Continuous (fun x => V10B2.rowEnergy H Y b x) :=
  continuous_unit_integral _ ((hH.norm.pow 2).add (hY.norm.pow 2)) b

noncomputable def energy (t : ℝ) (g : V08I.logCarrier t) (n : ℤ) : ℝ :=
  V10B2.rectangleEnergy (angularMoment t g 0) (angularMoment t g 1)
    (fun s y => Complex.I * angularMoment t g 1 s y)
    (fun s y => Complex.I * angularMoment t g 2 s y)
    (-(1/2):ℝ) (n : ℝ)

theorem moment_outer_integrable (t : ℝ) (ht : 0 ≤ t)
    (g : V08I.logCarrier t) (b : ℝ) :
    IntervalIntegrable (fun s =>
      V10B2.rowEnergy (angularMoment t g 0)
        (fun x y => Complex.I * angularMoment t g 1 x y) b s +
      V10B2.rowEnergy (angularMoment t g 1)
        (fun x y => Complex.I * angularMoment t g 2 x y) b s)
      volume (-(1/2):ℝ) (-(1/2)+1) := by
  have h (j : ℕ) := V10B5c.angularMoment_continuous t ht g j
  have hI (j : ℕ) : Continuous (fun p : ℝ × ℝ =>
      Complex.I * angularMoment t g j p.1 p.2) :=
    continuous_const.mul (h j)
  exact ((row_continuous _ _ (h 0) (hI 1) b).add
    (row_continuous _ _ (h 1) (hI 2) b)).intervalIntegrable _ _

theorem angular_horizontal_deriv (t : ℝ) (ht : 0 ≤ t)
    (g : V08I.logCarrier t) (j : ℕ) (s y : ℝ) :
    HasDerivAt (fun x : ℝ => angularMoment t g j x y)
      (angularMoment t g (j+1) s y) s := by
  let f := V08I.physicalInclusion t g
  let M := V07A.mellin (V10B4f.momentInput (f : ℝ → ℂ) j)
  have hf := V08K.supported_integrable t f (V08I.physicalInclusion_support t g)
  have hd := V10B4f.moment_derivative t ht (f : ℝ → ℂ) hf
    (V08I.physicalInclusion_support t g) j ((s : ℂ)+(y : ℂ)*Complex.I)
  have ha : HasDerivAt (fun z : ℂ => z+(y : ℂ)*Complex.I) 1 (s : ℂ) :=
    (hasDerivAt_id (s : ℂ)).add_const _
  have h := hd.comp (s : ℂ) ha
  simpa only [Function.comp_apply, mul_one, angularMoment, f] using h.comp_ofReal

theorem angular_vertical_deriv (t : ℝ) (ht : 0 ≤ t)
    (g : V08I.logCarrier t) (j : ℕ) (s y : ℝ) :
    HasDerivAt (fun v : ℝ => angularMoment t g j s v)
      (Complex.I * angularMoment t g (j+1) s y) y := by
  let f := V08I.physicalInclusion t g
  have hf := V08K.supported_integrable t f (V08I.physicalInclusion_support t g)
  have hd := V10B4f.moment_derivative t ht (f : ℝ → ℂ) hf
    (V08I.physicalInclusion_support t g) j ((s : ℂ)+(y : ℂ)*Complex.I)
  have ha : HasDerivAt (fun z : ℂ => (s : ℂ)+z*Complex.I) Complex.I (y : ℂ) := by
    simpa only [one_mul] using ((hasDerivAt_id (y : ℂ)).mul_const Complex.I).const_add (s : ℂ)
  have h := hd.comp (y : ℂ) ha
  simpa only [Function.comp_apply, mul_comm, angularMoment, f] using h.comp_ofReal

theorem real_deriv_component (F : ℝ → ℂ) (d : ℂ) (x : ℝ)
    (h : HasDerivAt F d x) :
    HasDerivAt (fun u => (F u).re) d.re x :=
  Complex.reCLM.hasFDerivAt.comp_hasDerivAt x h

theorem imag_deriv_component (F : ℝ → ℂ) (d : ℂ) (x : ℝ)
    (h : HasDerivAt F d x) :
    HasDerivAt (fun u => (F u).im) d.im x :=
  Complex.imCLM.hasFDerivAt.comp_hasDerivAt x h

theorem angular_rectangle_eval (t : ℝ) (ht : 0 ≤ t)
    (g : V08I.logCarrier t) (s y : ℝ)
    (hs : s ∈ Icc (-(1/2):ℝ) (1/2)) :
    ‖angularMoment t g 0 s y‖^2 ≤ 4 * energy t g (V10B5a.cell y) := by
  let H := angularMoment t g 0
  let X := angularMoment t g 1
  let Y := fun x v => Complex.I * X x v
  let Z := fun x v => Complex.I * angularMoment t g 2 x v
  have hj (j : ℕ) := V10B5c.angularMoment_continuous t ht g j
  have hc (j : ℕ) (v : ℝ) : Continuous (fun x => angularMoment t g j x v) :=
    (hj j).comp (continuous_id.prodMk continuous_const)
  have hv (j : ℕ) (x : ℝ) : Continuous (angularMoment t g j x) :=
    (hj j).comp (continuous_const.prodMk continuous_id)
  have hs' : s ∈ Icc (-(1/2):ℝ) (-(1/2)+1) := by
    convert hs using 1 <;> norm_num
  change ‖H s y‖^2 ≤ 4 * V10B2.rectangleEnergy H X Y Z
    (-(1/2):ℝ) (V10B5a.cell y : ℝ)
  apply V10B2.rectangle_eval H X Y Z _ _ s y hs' (V10B5a.cell_closed y)
  · exact hc 0 y
  · exact hc 1 y
  · intro x
    exact real_deriv_component _ _ _ (angular_horizontal_deriv t ht g 0 x y)
  · intro x
    exact imag_deriv_component _ _ _ (angular_horizontal_deriv t ht g 0 x y)
  · exact hv 0
  · exact hv 1
  · intro x
    exact continuous_const.mul (hv 1 x)
  · intro x
    exact continuous_const.mul (hv 2 x)
  · intro x v
    exact real_deriv_component _ _ _ (angular_vertical_deriv t ht g 0 x v)
  · intro x v
    exact imag_deriv_component _ _ _ (angular_vertical_deriv t ht g 0 x v)
  · intro x v
    exact real_deriv_component _ _ _ (angular_vertical_deriv t ht g 1 x v)
  · intro x v
    exact imag_deriv_component _ _ _ (angular_vertical_deriv t ht g 1 x v)
  · exact moment_outer_integrable t ht g _

theorem energy_nonnegative (t : ℝ) (g : V08I.logCarrier t) (n : ℤ) :
    0 ≤ energy t g n :=
  V10B2.rectangle_energy_nonnegative _ _ _ _ _ _

theorem global_energy_budget (t : ℝ) (ht : 0 ≤ t) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ (g : V08I.logCarrier t) (J : Finset ℤ),
      (∑ n ∈ J, Real.log (|(n : ℝ)|+3) * energy t g n) ≤ C * ‖g‖^2 := by
  obtain ⟨C,hC,h⟩ := V10B5c.angular_rectangle_budget t ht
  exact ⟨C,hC,fun g J => h g J (fun n _ => moment_outer_integrable t ht g n)⟩

/-- All analytical hypotheses have been attached to the carrier.
Only the counting estimate and strip placement are explicit inputs. -/
theorem bounded_strip_sampling (t : ℝ) (ht : 0 ≤ t) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ {ι : Type} (s y m : ι → ℝ)
      (A : ℝ), 0 ≤ A →
      (∀ i, s i ∈ Icc (-(1/2):ℝ) (1/2)) →
      (∀ i, 0 ≤ m i) →
      (∀ (S : Finset ι) (n : ℤ),
        ∑ i ∈ S.filter (fun i => V10B5a.cell (y i) = n), m i ≤
          A * Real.log (|(n : ℝ)|+3)) →
      ∀ g : V08I.logCarrier t,
        (∑' i, ENNReal.ofReal (m i * ‖angularMoment t g 0 (s i) (y i)‖^2)) ≤
          ENNReal.ofReal (4 * (A * (C * ‖g‖^2))) := by
  obtain ⟨C,hC,hbudget⟩ := global_energy_budget t ht
  refine ⟨C,hC,?_⟩
  intro ι s y m A hA hs hm hcount g
  exact V10B5a.infinite_log_sampling y m
    (fun i => ‖angularMoment t g 0 (s i) (y i)‖^2)
    (energy t g) A (C*‖g‖^2) hA hm (fun i => sq_nonneg _)
    (energy_nonnegative t g)
    (fun i => angular_rectangle_eval t ht g (s i) (y i) (hs i))
    hcount (hbudget g)

end WeilDefect.MasterRecon.V10B5d

#print axioms WeilDefect.MasterRecon.V10B5d.continuous_unit_integral
#print axioms WeilDefect.MasterRecon.V10B5d.row_continuous
#print axioms WeilDefect.MasterRecon.V10B5d.moment_outer_integrable
#print axioms WeilDefect.MasterRecon.V10B5d.angular_horizontal_deriv
#print axioms WeilDefect.MasterRecon.V10B5d.angular_vertical_deriv
#print axioms WeilDefect.MasterRecon.V10B5d.real_deriv_component
#print axioms WeilDefect.MasterRecon.V10B5d.imag_deriv_component
#print axioms WeilDefect.MasterRecon.V10B5d.angular_rectangle_eval
#print axioms WeilDefect.MasterRecon.V10B5d.energy_nonnegative
#print axioms WeilDefect.MasterRecon.V10B5d.global_energy_budget
#print axioms WeilDefect.MasterRecon.V10B5d.bounded_strip_sampling
