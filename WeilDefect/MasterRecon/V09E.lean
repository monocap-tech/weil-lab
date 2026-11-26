import WeilDefect.MasterRecon.V09C

/-! V09E: identify vanishing positive-channel coordinates with the
actual critical-line Mellin samples, then attach the certified compact
defect receiver. Arithmetic density, bounded analysis, coverage, and
the arithmetic defect inequality remain explicit inputs.
Staged independently of V09D native acceptance. -/
namespace WeilDefect.MasterRecon.V09E

open scoped ENNReal NNReal
open V07C

variable {ι : Type*}

noncomputable abbrev PositiveCoeff (ι : Type*) := lp (fun _ : ι => ℂ) 2

theorem critical_coordinate_zero (f : ℝ → ℂ) (m : ℕ) (hm : 0 < m)
    (γ : ℝ) (h : (WithLp.ofLp (V07E.samplePair f m 0 γ)).1 = 0) :
    V07A.mellin f ((γ : ℂ) * Complex.I) = 0 := by
  let q : ℂ := (Real.sqrt (m : ℝ) : ℂ)
  let w : ℂ := V07A.mellin f ((γ : ℂ) * Complex.I)
  have hq : q ≠ 0 := by
    have hp : 0 < Real.sqrt (m : ℝ) := Real.sqrt_pos.2 (by exact_mod_cast hm)
    change (Real.sqrt (m : ℝ) : ℂ) ≠ 0
    exact_mod_cast hp.ne'
  have hd : (Real.sqrt 2 : ℂ) ≠ 0 := by
    exact_mod_cast (Real.sqrt_pos.2 (by norm_num : (0 : ℝ) < 2)).ne'
  have he : (q * w + q * w) / (Real.sqrt 2 : ℂ) = 0 := by
    simpa [V07E.samplePair, V07A.pairPlus, V07A.weightedMellin, q, w] using h
  have hn : q * w + q * w = 0 := by
    have he' := congrArg (fun v : ℂ => v * (Real.sqrt 2 : ℂ)) he
    simpa [div_mul_cancel₀ _ hd] using he'
  have hw : q * w = 0 := by linear_combination hn / 2
  exact (mul_eq_zero.mp hw).resolve_left hq

theorem positive_coordinate_injective (t : ℝ) (ht : 0 ≤ t)
    (A : V08I.logCarrier t →L[ℂ] PositiveCoeff ι)
    (m : ι → ℕ) (d γ : ι → ℝ)
    (hdens : V09C.SuperlinearSupply V09C.CriticalSample)
    (hcover : ∀ z, V09C.CriticalSample z →
      ∃ i, d i = 0 ∧ 0 < m i ∧ (γ i : ℂ) * Complex.I = z)
    (hcoord : ∀ (g : V08I.logCarrier t) (i : ι),
      A g i = (WithLp.ofLp (V07E.samplePair
        (V08I.physicalInclusion t g : ℝ → ℂ) (m i) (d i) (γ i))).1)
    (g : V08I.logCarrier t) (hg : A g = 0) : g = 0 := by
  apply V09C.critical_mellin_injective t ht g hdens
  intro z hz
  obtain ⟨i, hi, hm, hγ⟩ := hcover z hz
  have hzero : A g i = 0 := by
    rw [hg]
    rfl
  have hc := hcoord g i
  rw [hzero, hi] at hc
  rw [← hγ]
  exact critical_coordinate_zero _ _ hm _ hc.symm

theorem positive_analysis_injective (t : ℝ) (ht : 0 ≤ t)
    (A : V08I.logCarrier t →L[ℂ] PositiveCoeff ι)
    (m : ι → ℕ) (d γ : ι → ℝ)
    (hdens : V09C.SuperlinearSupply V09C.CriticalSample)
    (hcover : ∀ z, V09C.CriticalSample z →
      ∃ i, d i = 0 ∧ 0 < m i ∧ (γ i : ℂ) * Complex.I = z)
    (hcoord : ∀ (g : V08I.logCarrier t) (i : ι),
      A g i = (WithLp.ofLp (V07E.samplePair
        (V08I.physicalInclusion t g : ℝ → ℂ) (m i) (d i) (γ i))).1) :
    Function.Injective A := by
  intro g h heq
  have hz : A (g - h) = 0 := by rw [map_sub, heq, sub_self]
  exact sub_eq_zero.mp
    (positive_coordinate_injective t ht A m d γ hdens hcover hcoord (g - h) hz)

theorem positive_analysis_coercive (t : ℝ) (ht : 0 ≤ t)
    (A : V08I.logCarrier t →L[ℂ] PositiveCoeff ι)
    (m : ι → ℕ) (d γ : ι → ℝ)
    (hdens : V09C.SuperlinearSupply V09C.CriticalSample)
    (hcover : ∀ z, V09C.CriticalSample z →
      ∃ i, d i = 0 ∧ 0 < m i ∧ (γ i : ℂ) * Complex.I = z)
    (hcoord : ∀ (g : V08I.logCarrier t) (i : ι),
      A g i = (WithLp.ofLp (V07E.samplePair
        (V08I.physicalInclusion t g : ℝ → ℂ) (m i) (d i) (γ i))).1)
    (M : ℝ) (hM : 0 ≤ M)
    (hdef : ∀ g : V08I.logCarrier t,
      ‖g‖ ^ 2 ≤ ‖A g‖ ^ 2 + M * ‖V08I.physicalInclusion t g‖ ^ 2) :
    ∃ b : ℝ≥0, 0 < b ∧ ∀ g : V08I.logCarrier t,
      ‖g‖ ^ 2 * (b : ℝ) ≤ ‖A g‖ ^ 2 := by
  exact V08B.compact_defect_coercivity A (V08I.physicalInclusion t)
    (V08K.physicalInclusion_compact t ht)
    (positive_coordinate_injective t ht A m d γ hdens hcover hcoord)
    M hM hdef

end WeilDefect.MasterRecon.V09E

#print axioms WeilDefect.MasterRecon.V09E.critical_coordinate_zero
#print axioms WeilDefect.MasterRecon.V09E.positive_coordinate_injective
#print axioms WeilDefect.MasterRecon.V09E.positive_analysis_injective
#print axioms WeilDefect.MasterRecon.V09E.positive_analysis_coercive
