import WeilDefect.MasterRecon.V10A

/-! V10A2: signed orbit energy and the correctly normalized positive
channel receiver. No global summation or arithmetic defect inequality
is asserted. -/
namespace WeilDefect.MasterRecon.V10A2

open scoped NNReal ENNReal ComplexConjugate
open V10A

theorem pair_energy_sum (u v : ℂ) :
    ‖V07A.pairPlus u v‖ ^ 2 + ‖V07A.pairMinus u v‖ ^ 2 =
      ‖u‖ ^ 2 + ‖v‖ ^ 2 := by
  have hroot : ‖(Real.sqrt 2 : ℂ)‖ ^ 2 = 2 := by
    rw [Complex.norm_real, Real.norm_of_nonneg (Real.sqrt_nonneg _),
      Real.sq_sqrt (by norm_num)]
  unfold V07A.pairPlus V07A.pairMinus
  rw [norm_div, norm_div, div_pow, div_pow, hroot]
  simp only [Complex.sq_norm, Complex.normSq_apply, Complex.add_re,
    Complex.add_im, Complex.sub_re, Complex.sub_im]
  ring

theorem pair_energy_difference (u v : ℂ) :
    ‖V07A.pairPlus u v‖ ^ 2 - ‖V07A.pairMinus u v‖ ^ 2 =
      2 * (u * conj v).re := by
  have hroot : ‖(Real.sqrt 2 : ℂ)‖ ^ 2 = 2 := by
    rw [Complex.norm_real, Real.norm_of_nonneg (Real.sqrt_nonneg _),
      Real.sq_sqrt (by norm_num)]
  unfold V07A.pairPlus V07A.pairMinus
  rw [norm_div, norm_div, div_pow, div_pow, hroot]
  simp only [Complex.sq_norm, Complex.normSq_apply, Complex.add_re,
    Complex.add_im, Complex.sub_re, Complex.sub_im, Complex.mul_re,
    Complex.conj_re, Complex.conj_im]
  ring

theorem weighted_energy (f : ℝ → ℂ) (m : ℕ) (z : ℂ) :
    ‖V07A.weightedMellin f m z‖ ^ 2 = (m : ℝ) * ‖V07A.mellin f z‖ ^ 2 := by
  unfold V07A.weightedMellin
  rw [norm_mul, mul_pow, Complex.norm_real,
    Real.norm_of_nonneg (Real.sqrt_nonneg _), Real.sq_sqrt (by positivity)]

theorem normalized_fixed_energy (f : ℝ → ℂ) (i : Index) (hi : displacement i = 0) :
    ‖(WithLp.ofLp (normalizedPair f i)).1‖ ^ 2 -
      ‖(WithLp.ofLp (normalizedPair f i)).2‖ ^ 2 =
      (multiplicity i : ℝ) * ‖V07A.mellin f ((ordinate i : ℂ) * Complex.I)‖ ^ 2 := by
  rw [normalizedPair_fixed f i hi]
  simp [weighted_energy]

theorem normalized_nonfixed_energy (f : ℝ → ℂ) (i : Index) (hi : displacement i ≠ 0) :
    ‖(WithLp.ofLp (normalizedPair f i)).1‖ ^ 2 -
      ‖(WithLp.ofLp (normalizedPair f i)).2‖ ^ 2 =
      2 * (V07A.weightedMellin f (multiplicity i) ((i : ℂ) - 1 / 2) *
        conj (V07A.weightedMellin f (multiplicity i) (reflect (i : ℂ) - 1 / 2))).re := by
  rw [normalizedPair_nonfixed f i hi]
  change ‖V07A.pairPlus _ _‖ ^ 2 - ‖V07A.pairMinus _ _‖ ^ 2 = _
  rw [pair_energy_difference, right_exponent, left_exponent]

theorem normalized_positive_kernel (t : ℝ) (ht : 0 ≤ t)
    (A : V08I.logCarrier t →L[ℂ] V09E.PositiveCoeff Index)
    (hm : ∀ ρ, V09D.stripZero ρ → 0 < V09D.mult ρ)
    (hdens : V09C.SuperlinearSupply V09C.CriticalSample)
    (hcoord : ∀ (g : V08I.logCarrier t) (i : Index),
      A g i = (WithLp.ofLp (normalizedPair
        (V08I.physicalInclusion t g : ℝ → ℂ) i)).1)
    (g : V08I.logCarrier t) (hg : A g = 0) : g = 0 := by
  apply V09C.critical_mellin_injective t ht g hdens
  intro z hz
  obtain ⟨i, hd, hm', hi⟩ := critical_coverage hm z hz
  have hzero : A g i = 0 := by
    rw [hg]
    rfl
  have hc := (hcoord g i).symm.trans hzero
  rw [← hi]
  exact normalized_fixed_zero _ i hd hm' hc

theorem normalized_positive_coercivity (t : ℝ) (ht : 0 ≤ t)
    (A : V08I.logCarrier t →L[ℂ] V09E.PositiveCoeff Index)
    (hm : ∀ ρ, V09D.stripZero ρ → 0 < V09D.mult ρ)
    (hdens : V09C.SuperlinearSupply V09C.CriticalSample)
    (hcoord : ∀ (g : V08I.logCarrier t) (i : Index),
      A g i = (WithLp.ofLp (normalizedPair
        (V08I.physicalInclusion t g : ℝ → ℂ) i)).1)
    (M : ℝ) (hM : 0 ≤ M)
    (hdef : ∀ g : V08I.logCarrier t,
      ‖g‖ ^ 2 ≤ ‖A g‖ ^ 2 + M * ‖V08I.physicalInclusion t g‖ ^ 2) :
    ∃ b : ℝ≥0, 0 < b ∧ ∀ g : V08I.logCarrier t,
      ‖g‖ ^ 2 * (b : ℝ) ≤ ‖A g‖ ^ 2 := by
  exact V08B.compact_defect_coercivity A (V08I.physicalInclusion t)
    (V08K.physicalInclusion_compact t ht)
    (normalized_positive_kernel t ht A hm hdens hcoord) M hM hdef

end WeilDefect.MasterRecon.V10A2

#print axioms WeilDefect.MasterRecon.V10A2.pair_energy_sum
#print axioms WeilDefect.MasterRecon.V10A2.pair_energy_difference
#print axioms WeilDefect.MasterRecon.V10A2.weighted_energy
#print axioms WeilDefect.MasterRecon.V10A2.normalized_fixed_energy
#print axioms WeilDefect.MasterRecon.V10A2.normalized_nonfixed_energy
#print axioms WeilDefect.MasterRecon.V10A2.normalized_positive_kernel
#print axioms WeilDefect.MasterRecon.V10A2.normalized_positive_coercivity
