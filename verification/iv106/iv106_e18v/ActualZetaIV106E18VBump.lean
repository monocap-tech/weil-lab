import WeilDefect.Arithmetic.ActualZetaIV106E18UTrialClosure
import Mathlib.Analysis.Calculus.BumpFunction.Normed

namespace WeilDefect
noncomputable section
open MeasureTheory Set Metric
open scoped SchwartzMap ContDiff

/-- A fixed bump on every positive-width interval. The inner plateau
supplies a width-explicit normalization bound, rather than an existential
constant depending on the approximation. -/
theorem neutralIV106E18VBump (A B : ℝ) (hAB : A < B) :
    ∃ ρ : 𝓢(ℝ,ℂ), (∀ x, x ≤ A ∨ B ≤ x → ρ x = 0) ∧
      (∫ x in A..B, ρ x) = 1 ∧ (∀ x, ‖ρ x‖ ≤ 4/(B-A)) := by
  let c := (A+B)/2
  let L := B-A
  have hL : 0 < L := sub_pos.mpr hAB
  let φ : ContDiffBump c := ⟨L/8,L/4,by positivity,by linarith⟩
  let J := Icc (c-L/8) (c+L/8)
  let m : ℝ := ∫ x : ℝ, φ x
  have hle : (∫ x in J, φ x) ≤ m :=
    integral_mono_measure Measure.restrict_le_self
      (Filter.Eventually.of_forall φ.nonneg') φ.integrable
  have hJ : (∫ x in J, φ x) = L/4 := by
    calc
      _ = ∫ x in J, (1:ℝ) := by
        apply setIntegral_congr_fun measurableSet_Icc
        intro x hx
        apply φ.one_of_mem_closedBall
        change dist x c ≤ L/8
        rw [Real.dist_eq,abs_le]
        exact ⟨by linarith [hx.1],by linarith [hx.2]⟩
      _ = _ := by
        dsimp [J]
        rw [integral_Icc_eq_integral_Ioc,
          ← intervalIntegral.integral_of_le (by linarith : c-L/8 ≤ c+L/8),
          intervalIntegral.integral_const]
        simp
        ring
  rw [hJ] at hle
  have hm : 0 < m := lt_of_lt_of_le (by positivity) hle
  let u : ℝ → ℝ := φ.normed volume
  have huout (x : ℝ) (hx : x ≤ A ∨ B ≤ x) : u x = 0 := by
    have hz : φ x = 0 := by
      apply φ.zero_of_le_dist
      change L/4 ≤ dist x c
      rw [Real.dist_eq]
      rcases hx with h | h
      · exact (show L/4 ≤ -(x-c) by dsimp [L,c]; linarith).trans (neg_le_abs _)
      · exact (show L/4 ≤ x-c by dsimp [L,c]; linarith).trans (le_abs_self _)
    simp [u,ContDiffBump.normed,hz]
  let v : ℝ → ℂ := fun x => (u x : ℂ)
  have hvout (x : ℝ) (hx : x ≤ A ∨ B ≤ x) : v x = 0 := by
    simp [v,huout x hx]
  have hc : HasCompactSupport v := by
    apply HasCompactSupport.intro (K := Icc A B) isCompact_Icc
    intro x hx
    apply hvout
    by_contra! hn
    exact hx ⟨hn.1.le,hn.2.le⟩
  let ρ := hc.toSchwartzMap (Complex.ofRealCLM.contDiff.comp φ.contDiff_normed)
  refine ⟨ρ,hvout,?_,?_⟩
  · change (∫ x in A..B, (u x : ℂ)) = 1
    rw [intervalIntegral.integral_ofReal]
    have hmass : (∫ x in A..B, u x) = 1 := by
      rw [intervalIntegral.integral_eq_integral_of_support_subset]
      · exact φ.integral_normed
      · intro x hx
        constructor
        · by_contra! hh
          exact hx (huout x (Or.inl hh))
        · by_contra! hh
          exact hx (huout x (Or.inr hh.le))
    rw [hmass]
    norm_num
  · intro x
    change ‖(u x : ℂ)‖ ≤ 4/(B-A)
    rw [Complex.norm_real,Real.norm_eq_abs,abs_of_nonneg (φ.nonneg_normed x)]
    change φ x / m ≤ 4/L
    have hb : φ x ≤ 1 := φ.le_one
    calc
      _ ≤ 1/m := div_le_div_of_nonneg_right hb hm.le
      _ ≤ 4/L := by
        apply (div_le_div_iff₀ hm hL).mpr
        linarith

/-- The original clipped polynomial now belongs to the joint graph
without an external bump premise. -/
theorem neutralIV106E18VTrial_graph (l h ε : ℝ) (hh : 0 < h) (hε : 0 < ε) :
    ((neutralIV106E18JTrial_memLp l h hh).toLp _,
      (neutralIV106E18SDTrial_memLp l h hh).toLp _) ∈
      neutralIV106E18UGraphSpace (l-ε) (l+h+ε) := by
  have hAB : l-ε < l+h+ε := by linarith
  obtain ⟨ρ,hout,hm,hb⟩ := neutralIV106E18VBump (l-ε) (l+h+ε) hAB
  exact neutralIV106E18UTrial_graph l h ε hh hε ρ hout hm _
    (by positivity : 0 ≤ 4/(l+h+ε-(l-ε))) hb

#print axioms neutralIV106E18VBump
#print axioms neutralIV106E18VTrial_graph
end
end WeilDefect
