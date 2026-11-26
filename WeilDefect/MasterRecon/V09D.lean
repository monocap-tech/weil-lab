import WeilDefect.MasterRecon.V09C

/-! V09D: arithmetic density transport receiver. These counting
definitions mirror the external Zeta23 statement surface, but no
external proof is imported and the two arithmetic estimates are
explicit hypotheses. -/
namespace WeilDefect.MasterRecon.V09D

open Set Metric
open scoped Topology BigOperators

def stripZero (ρ : ℂ) : Prop :=
  riemannZeta ρ = 0 ∧ 0 < ρ.re ∧ ρ.re < 1

def stripWindow (T₁ T₂ : ℝ) : Set ℂ :=
  {ρ | stripZero ρ ∧ T₁ < ρ.im ∧ ρ.im ≤ T₂}

noncomputable def mult (ρ : ℂ) : ℕ :=
  (analyticOrderAt riemannZeta ρ).toNat

noncomputable def count (T₁ T₂ : ℝ) : ℕ :=
  ∑ᶠ ρ ∈ stripWindow T₁ T₂, mult ρ

def lineWindow (T₁ T₂ : ℝ) : Set ℂ :=
  stripWindow T₁ T₂ ∩ {ρ | ρ.re = 1 / 2}

noncomputable def lineCount (T₁ T₂ : ℝ) : ℕ :=
  (lineWindow T₁ T₂).ncard

theorem shifted_line_sample (T : ℝ) (hT : 0 ≤ T) (ρ : ℂ)
    (hρ : ρ ∈ lineWindow T (2 * T)) :
    V09C.CriticalSample (ρ - (1 / 2 : ℂ)) ∧ ‖ρ - (1 / 2 : ℂ)‖ ≤ 2 * T := by
  rcases hρ with ⟨⟨⟨hz, _, _⟩, hlo, hhi⟩, hre⟩
  change ρ.re = (1 : ℝ) / 2 at hre
  have hrepr : ρ - (1 / 2 : ℂ) = (ρ.im : ℂ) * Complex.I := by
    apply Complex.ext <;> simp [Complex.sub_re, Complex.sub_im, Complex.div_re,
      Complex.div_im, Complex.mul_re, Complex.mul_im, hre] <;> norm_num
  have hp : 0 < ρ.im := hT.trans_lt hlo
  constructor
  · refine ⟨?_, ?_, ?_⟩
    · rw [hrepr]; simp [Complex.mul_re]
    · rw [hrepr]; simpa [Complex.mul_im] using hp
    · rw [show (1 / 2 : ℂ) + (ρ - (1 / 2 : ℂ)) = ρ by ring]
      exact hz
  · rw [hrepr, norm_mul, Complex.norm_I, mul_one, Complex.norm_real,
      Real.norm_eq_abs, abs_of_pos hp]
    exact hhi

theorem lineWindow_finite (T : ℝ) (hT : 0 ≤ T) :
    (lineWindow T (2 * T)).Finite := by
  apply (isCompact_closedBall (1 / 2 : ℂ) (2 * T)).inter_riemannZetaZeros_finite.subset
  intro ρ hρ
  refine ⟨?_, ?_⟩
  · rw [mem_closedBall, dist_eq_norm]
    exact (shifted_line_sample T hT ρ hρ).2
  · exact hρ.1.1.1

noncomputable def shiftedSamples (T : ℝ) (hT : 0 ≤ T) : Finset ℂ :=
  (lineWindow_finite T hT).toFinset.map
    ⟨fun ρ => ρ - (1 / 2 : ℂ), fun x y h => by
      change x - (1 / 2 : ℂ) = y - (1 / 2 : ℂ) at h
      linear_combination h⟩

theorem shiftedSamples_card (T : ℝ) (hT : 0 ≤ T) :
    (shiftedSamples T hT).card = lineCount T (2 * T) := by
  unfold shiftedSamples lineCount
  rw [Finset.card_map, Set.ncard_eq_toFinset_card _ (lineWindow_finite T hT)]

theorem shiftedSamples_spec (T : ℝ) (hT : 0 ≤ T) (z : ℂ)
    (hz : z ∈ shiftedSamples T hT) :
    V09C.CriticalSample z ∧ ‖z‖ ≤ 2 * T := by
  classical
  unfold shiftedSamples at hz
  obtain ⟨ρ, hρ, rfl⟩ := Finset.mem_map.mp hz
  exact shifted_line_sample T hT ρ (by simpa only [Set.Finite.mem_toFinset] using hρ)

/-- Quantitative RvM-type estimate implies arbitrarily large linear
lower bounds, without any asymptotic convention or multiplicity
conversion hidden in the receiver. -/
theorem count_superlinear_of_rvm (N : ℝ → ℝ) (a b C T₀ : ℝ) (ha : 0 < a)
    (hmain : ∀ T ≥ T₀, |N T - T * (a * Real.log T + b)| ≤ C * Real.log T)
    (L T₁ : ℝ) :
    ∃ T : ℝ, 1 ≤ T ∧ T₁ ≤ T ∧ (4 * |L| + 1) * T ≤ N T := by
  let K := (2 / a) * (4 * |L| + |b| + 1)
  let U := 2 * max C 0 / a
  let T := max 1 (max T₀ (max T₁ (max U (Real.exp K))))
  have h1 : 1 ≤ T := le_max_left _ _
  have h0 : T₀ ≤ T := (le_max_left T₀ _).trans (le_max_right 1 _)
  have hT₁ : T₁ ≤ T := (le_max_left T₁ _).trans
    ((le_max_right T₀ _).trans (le_max_right 1 _))
  have hU : U ≤ T := (le_max_left U _).trans
    ((le_max_right T₁ _).trans ((le_max_right T₀ _).trans (le_max_right 1 _)))
  have hK : Real.exp K ≤ T := (le_max_right U _).trans
    ((le_max_right T₁ _).trans ((le_max_right T₀ _).trans (le_max_right 1 _)))
  have hp : 0 < T := by linarith
  have hl : 0 ≤ Real.log T := Real.log_nonneg h1
  have hk : K ≤ Real.log T := by
    have h := Real.log_le_log (Real.exp_pos K) hK
    rwa [Real.log_exp] at h
  have hc : C ≤ T * a / 2 := by
    have h := (div_le_iff₀ ha).mp (show 2 * max C 0 / a ≤ T from hU)
    linarith [le_max_left C (0 : ℝ)]
  have hcl := mul_le_mul_of_nonneg_right hc hl
  have hkl : 4 * |L| + |b| + 1 ≤ a * Real.log T / 2 := by
    have h := mul_le_mul_of_nonneg_left hk ha.le
    have he : a * K = 2 * (4 * |L| + |b| + 1) := by
      dsimp [K]
      field_simp [ha.ne']
    linarith
  have hb : 4 * |L| + 1 ≤ a * Real.log T / 2 + b := by
    linarith [neg_abs_le b]
  have hbl := mul_le_mul_of_nonneg_left hb hp.le
  have hm := (abs_le.mp (hmain T h0)).1
  refine ⟨T, h1, hT₁, ?_⟩
  nlinarith only [hm, hcl, hbl]

/-- A positive dyadic proportion and RvM main term give the exact
finite distinct-sample supply required by V09C. -/
theorem critical_supply_of_count_bounds
    (a b C T₀ T₁ : ℝ) (ha : 0 < a)
    (hmain : ∀ T ≥ T₀,
      |(count T (2 * T) : ℝ) - T * (a * Real.log T + b)| ≤ C * Real.log T)
    (hprop : ∀ T ≥ T₁, (1 / 2 : ℝ) * (count T (2 * T) : ℝ) ≤ lineCount T (2 * T)) :
    V09C.SuperlinearSupply V09C.CriticalSample := by
  intro L
  obtain ⟨T, hT, hT₁, hlarge⟩ := count_superlinear_of_rvm
    (fun T => (count T (2 * T) : ℝ)) a b C T₀ ha hmain L T₁
  have hp : 0 ≤ T := by linarith
  refine ⟨2 * T, shiftedSamples T hp, by linarith, shiftedSamples_spec T hp, ?_⟩
  rw [shiftedSamples_card]
  have h := hprop T hT₁
  have hL := mul_le_mul_of_nonneg_right (le_abs_self L) hp
  nlinarith only [h, hlarge, hL, hT]

/-- Match the precise published dyadic RvM main term, not merely an
informal O(T log T) assertion. -/
theorem critical_supply_of_dyadic_estimates
    (hmain : ∃ C T₀ : ℝ, ∀ T ≥ T₀,
      |(count T (2 * T) : ℝ) -
        T / (2 * Real.pi) * (Real.log (T / (2 * Real.pi)) + 2 * Real.log 2 - 1)|
        ≤ C * Real.log T)
    (hprop : ∀ ε > 0, ∃ T₁ : ℝ, ∀ T ≥ T₁,
      (2 / 3 - ε) * (count T (2 * T) : ℝ) ≤ lineCount T (2 * T)) :
    V09C.SuperlinearSupply V09C.CriticalSample := by
  obtain ⟨C, T₀, hm⟩ := hmain
  obtain ⟨T₁, hp⟩ := hprop (1 / 6) (by norm_num)
  let p := 2 * Real.pi
  have hpos : 0 < p := by dsimp [p]; positivity
  apply critical_supply_of_count_bounds p⁻¹
    (p⁻¹ * (-Real.log p + 2 * Real.log 2 - 1)) C (max 1 T₀) T₁ (inv_pos.mpr hpos)
  · intro T hT
    have h1 : 1 ≤ T := (le_max_left 1 T₀).trans hT
    have hT₀ : T₀ ≤ T := (le_max_right 1 T₀).trans hT
    have h := hm T hT₀
    change |(count T (2 * T) : ℝ) -
      T / p * (Real.log (T / p) + 2 * Real.log 2 - 1)| ≤ _ at h
    rw [Real.log_div (by linarith : T ≠ 0) hpos.ne'] at h
    convert h using 2 <;> ring
  · intro T hT
    simpa only [show (2 / 3 - 1 / 6 : ℝ) = 1 / 2 by norm_num] using hp T hT

end WeilDefect.MasterRecon.V09D

#print axioms WeilDefect.MasterRecon.V09D.shifted_line_sample
#print axioms WeilDefect.MasterRecon.V09D.lineWindow_finite
#print axioms WeilDefect.MasterRecon.V09D.shiftedSamples_card
#print axioms WeilDefect.MasterRecon.V09D.shiftedSamples_spec
#print axioms WeilDefect.MasterRecon.V09D.count_superlinear_of_rvm
#print axioms WeilDefect.MasterRecon.V09D.critical_supply_of_count_bounds
#print axioms WeilDefect.MasterRecon.V09D.critical_supply_of_dyadic_estimates
